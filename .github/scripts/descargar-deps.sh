#!/usr/bin/env bash
# Descarga las dependencias extra que un repo declara en `.github/smoke-deps.txt` para el smoke test de servidor.
#
#   descargar-deps.sh <archivo-de-lista> <directorio-destino> <version-de-minecraft>
#
# Cada linea del archivo puede ser:
#   modrinth:<slug>   -> ultima version de ese proyecto de Modrinth para Paper (p. ej. modrinth:luckperms)
#   https://...jar    -> descarga directa
#   # comentario
#
# POR QUE EXISTE: un plugin con softdepend (LuckPerms, Vault, PlaceholderAPI...) puede asumir que esa API esta
# presente. El smoke test sobre un servidor vacio daria un falso fallo; con esta lista se prueba como en produccion.
set -euo pipefail
LISTA="$1"; DESTINO="$2"; MC="${3:-1.21.11}"
mkdir -p "$DESTINO"
[ -f "$LISTA" ] || exit 0
while IFS= read -r linea || [ -n "$linea" ]; do
    linea="$(echo "$linea" | sed 's/#.*//' | xargs)"
    [ -z "$linea" ] && continue
    case "$linea" in
        modrinth:*)
            slug="${linea#modrinth:}"
            url="$(curl -fsSL "https://api.modrinth.com/v2/project/${slug}/version?loaders=%5B%22paper%22%5D&game_versions=%5B%22${MC}%22%5D" \
                   | jq -r '[.[] | select(.version_type=="release")][0].files | (map(select(.primary))[0] // .[0]).url' || true)"
            if [ -z "$url" ] || [ "$url" = "null" ]; then
                url="$(curl -fsSL "https://api.modrinth.com/v2/project/${slug}/version?loaders=%5B%22paper%22%5D" \
                       | jq -r '.[0].files | (map(select(.primary))[0] // .[0]).url' || true)"
            fi
            [ -n "$url" ] && [ "$url" != "null" ] || { echo "::warning::sin version de Modrinth para $slug"; continue; }
            ;;
        http*) url="$linea" ;;
        *) echo "::warning::linea no reconocida en $LISTA: $linea"; continue ;;
    esac
    echo "Descargando $url"
    curl -fsSL -o "$DESTINO/$(basename "${url%%\?*}")" "$url"
done < "$LISTA"
