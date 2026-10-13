#!/usr/bin/env bash
#
# Arranca un servidor Paper real con el jar del plugin y comprueba que carga, se habilita y se apaga limpio,
# sin errores de enlace con la API de esa version.
#
#   server-smoke-test.sh <version-de-minecraft> <jar-del-plugin> [jar-dependencia ...]
#
# CREDITO: idea y primera implementacion de Chagui68 (MultiverseCreatures/.github/scripts/server-smoke-test.sh).
# Esta version es generica: lee el nombre del plugin de su plugin.yml y acepta jars de dependencia (p. ej. el core
# Slimefun4-Drake) que se copian a plugins/ antes de arrancar.
#
# POR QUE: el MISMO jar (compilado una vez) se prueba en todas las versiones. Un metodo que falte o haya cambiado
# en una API mas nueva solo aparece al enlazar las clases en ese servidor, nunca al compilar.
set -euo pipefail

VERSION="$1"
PLUGIN_JAR="$(realpath "$2")"
shift 2
DEPS=("$@")
WORK="server-$VERSION"
START_TIMEOUT="${START_TIMEOUT:-600}"
SETTLE_SECONDS="${SETTLE_SECONDS:-30}"

NOMBRE="$(unzip -p "$PLUGIN_JAR" plugin.yml | sed -n 's/^name:[[:space:]]*["'\'']\{0,1\}\([^"'\''[:space:]]*\).*/\1/p' | head -n1)"
if [ -z "$NOMBRE" ]; then echo "::error::El jar no tiene plugin.yml con name:" >&2; exit 1; fi
echo "Plugin a probar: $NOMBRE"

rm -rf "$WORK"
mkdir -p "$WORK/plugins"
cd "$WORK"

echo "::group::Descargar Paper $VERSION"
BUILDS="$(curl -fsSL "https://fill.papermc.io/v3/projects/paper/versions/$VERSION/builds")"
URL="$(echo "$BUILDS" | jq -r '([.[] | select(.channel == "STABLE")] + .)[0].downloads."server:default".url')"
SHA="$(echo "$BUILDS" | jq -r '([.[] | select(.channel == "STABLE")] + .)[0].downloads."server:default".checksums.sha256')"
if [ -z "$URL" ] || [ "$URL" = "null" ]; then
    echo "::error::No hay build de Paper para $VERSION" >&2
    exit 1
fi
curl -fsSL -o paper.jar "$URL"
echo "$SHA  paper.jar" | sha256sum -c -
echo "::endgroup::"

for dep in "${DEPS[@]:-}"; do
    [ -n "$dep" ] && cp "$(realpath "$dep")" plugins/
done
cp "$PLUGIN_JAR" plugins/
echo "eula=true" > eula.txt
cat > server.properties <<'PROPERTIES'
online-mode=false
spawn-protection=0
max-players=2
view-distance=4
simulation-distance=4
PROPERTIES

echo "::group::Arrancar el servidor"
mkfifo console
java -Xms1G -Xmx3G -jar paper.jar --nogui < console > server.log 2>&1 &
SERVER_PID=$!
exec 3> console   # mantener abierta la consola para que el servidor no la vea cerrarse

started=false
for _ in $(seq 1 "$START_TIMEOUT"); do
    if grep -q "Done (" server.log; then started=true; break; fi
    if ! kill -0 "$SERVER_PID" 2>/dev/null; then break; fi
    sleep 1
done
echo "::endgroup::"

if [ "$started" != true ]; then
    echo "::error::El servidor no termino de arrancar" >&2
    tail -n 200 server.log >&2
    kill "$SERVER_PID" 2>/dev/null || true
    exit 1
fi

sleep "$SETTLE_SECONDS"   # dejar correr lo programado tras el arranque (recetas diferidas, tickers)
echo "stop" >&3

for _ in $(seq 1 120); do
    if ! kill -0 "$SERVER_PID" 2>/dev/null; then break; fi
    sleep 1
done
if kill -0 "$SERVER_PID" 2>/dev/null; then
    echo "::error::El servidor no se apago a tiempo" >&2
    kill -9 "$SERVER_PID" 2>/dev/null || true
fi
exec 3>&-

echo "::group::Log del servidor"
cat server.log
echo "::endgroup::"

failed=false
require() {
    if ! grep -qE "$1" server.log; then
        echo "::error::Paper $VERSION: falta en el log: $2"
        failed=true
    fi
}
forbid() {
    if grep -nE "$1" server.log; then
        echo "::error::Paper $VERSION: $2"
        failed=true
    fi
}

require "Enabling $NOMBRE" "el plugin no se habilito"
require "Disabling $NOMBRE" "el plugin no se deshabilito al apagar"
forbid "Could not load 'plugins/[^']*' in folder|Error occurred while enabling $NOMBRE" \
       "el servidor rechazo cargar o habilitar el plugin"
forbid "NoSuchMethodError|NoSuchFieldError|NoClassDefFoundError|AbstractMethodError|IncompatibleClassChangeError" \
       "una clase o miembro del plugin no enlaza con esta API"

if [ "$failed" = true ]; then exit 1; fi
echo "Paper $VERSION: $NOMBRE cargo, se habilito y se apago limpio."
