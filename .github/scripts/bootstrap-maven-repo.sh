#!/usr/bin/env bash
# Prepara ~/.m2 con el repositorio Maven de la org (parents drakes-slimefun-labs, slimefun-core Drake, dough...).
#
# QUE HACE
#   Clona SlimefunNewHorizons/maven-repo, lo copia a ~/.m2/repository y crea la variante -SNAPSHOT de cada
#   version publicada (los poms de los addons piden `...-SNAPSHOT`).
# POR QUE EXISTE
#   Estaba incrustado (y con `|| true`, que ocultaba errores) en 130 copias de modrinth-publish.yml.
#   Ahora vive en un solo sitio y FALLA de forma visible si el repo no se puede clonar.
set -euo pipefail

DESTINO="${HOME}/.m2/repository"
mkdir -p "$DESTINO"
git clone --depth 1 https://github.com/SlimefunNewHorizons/maven-repo.git /tmp/drakes-maven-repo
cp -rn /tmp/drakes-maven-repo/com "$DESTINO"/

python3 - <<'PY'
import os, shutil
repo = os.path.expanduser("~/.m2/repository/com/github/drakescraft_labs")
if not os.path.isdir(repo):
    raise SystemExit(0)
for d in os.listdir(repo):
    dp = os.path.join(repo, d)
    if not os.path.isdir(dp):
        continue
    for v in list(os.listdir(dp)):
        vp = os.path.join(dp, v)
        if os.path.isdir(vp) and v.endswith("-SNAPSHOT"):
            # SNAPSHOT publicado con marca de tiempo (name-1.3.1-X-20260529.143737-1.jar): Maven no lo resuelve
            # desde ~/.m2 sin la copia sin marca (name-1.3.1-X-SNAPSHOT.jar). Se crea con la mas reciente.
            base = v[: -len("-SNAPSHOT")]
            for ext in ("jar", "pom"):
                con_marca = sorted(f for f in os.listdir(vp)
                                   if f.startswith(f"{d}-{base}-") and f.endswith("." + ext)
                                   and f != f"{d}-{v}.{ext}")
                destino = os.path.join(vp, f"{d}-{v}.{ext}")
                if con_marca and not os.path.exists(destino):
                    shutil.copy(os.path.join(vp, con_marca[-1]), destino)
            continue
        if not os.path.isdir(vp):
            continue
        snap_p = os.path.join(dp, v + "-SNAPSHOT")
        if os.path.exists(snap_p):
            continue
        shutil.copytree(vp, snap_p)
        for f in os.listdir(snap_p):
            if v in f:
                os.rename(os.path.join(snap_p, f), os.path.join(snap_p, f.replace(v, v + "-SNAPSHOT")))
PY
echo "Repositorio Maven de la org listo en $DESTINO"
