#!/usr/bin/env python3
"""Detecta de que core de Slimefun depende un repo y genera las notas de la release.

QUE HACE
  `detectar-core.py json`  -> JSON con la linea de core (drake | igdrassil | ninguno), version de MC, plugin, etc.
  `detectar-core.py notas --version V --jar J --sha256 H [--repo R]` -> notas de release en Markdown (es).

POR QUE EXISTE
  Los addons de la org compilan contra el core Slimefun4-Drake (`slimefun-core` 11.0-Drake-1.21.11) y NO cargan en
  un Slimefun 4 "normal" porque el core Drake renombro la libreria base `io.github.bakedlibs.dough` a
  `dev.drake.dough` (en el addon se importa `dev.drake.dough...`; un Slimefun upstream solo trae el paquete
  original, asi que el addon falla con NoClassDefFoundError). Esto se detecta leyendo el codigo, no se asume: asi
  la explicacion de cada release es verdadera para ESE repo, incluidos los que vuelven a la linea compatible.
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys

RAIZ = pathlib.Path(".")
DRAKE_IMPORT = re.compile(r"\bdev\.drake\.dough\b")
UPSTREAM_IMPORT = re.compile(r"\bio\.github\.bakedlibs\.dough\b")
SF_IMPORT = re.compile(r"\bio\.github\.thebusybiscuit\.slimefun4\b|\bme\.mrCookieSlime\.Slimefun\b")


def _leer(ruta):
    try:
        return pathlib.Path(ruta).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def _yml(texto):
    try:
        import yaml
        d = yaml.safe_load(texto)
        return d if isinstance(d, dict) else {}
    except Exception:  # noqa: BLE001  (sin PyYAML o plugin.yml raro: se sigue sin esos datos)
        return {}


def _lista(d, clave):
    v = d.get(clave) or []
    if isinstance(v, str):
        v = [v]
    return [str(x) for x in v]


def _contar():
    drake = upstream = sf = 0
    for ruta in RAIZ.glob("src/main/**/*.java"):
        t = ruta.read_text(encoding="utf-8", errors="replace")
        drake += len(DRAKE_IMPORT.findall(t))
        upstream += len(UPSTREAM_IMPORT.findall(t))
        sf += 1 if SF_IMPORT.search(t) else 0
    return drake, upstream, sf


def detectar():
    plugin_yml = _leer("src/main/resources/plugin.yml")
    pom = _leer("pom.xml")
    gradle = _leer("build.gradle") + _leer("build.gradle.kts")
    y = _yml(plugin_yml)
    nombre = str(y.get("name") or RAIZ.resolve().name)
    depend = _lista(y, "depend")
    soft = _lista(y, "softdepend")
    api = str(y.get("api-version") or "")
    drake, upstream, sf_clases = _contar()
    core_ver = ""
    m = re.search(r"<slimefun\.drake\.version>([^<]+)<", pom) or re.search(
        r"<artifactId>slimefun-core</artifactId>\s*<version>([^<$]+)<", pom)
    if m:
        core_ver = m.group(1)
    paper = (re.search(r"paper-api</artifactId>\s*<version>([^<]+)<", pom) or [None, ""])[1]
    # Slimefun OBLIGATORIO (depend o artefacto slimefun-core); una integracion opcional (softdepend) no cuenta.
    necesita_sf = "Slimefun" in depend or "slimefun-core" in pom or drake > 0 or upstream > 0
    if nombre == "Slimefun":
        linea = "nucleo"
    elif drake and drake >= upstream:
        linea = "drake"
    elif necesita_sf and upstream:
        linea = "igdrassil"
    elif necesita_sf and "slimefun-core" in pom:
        linea = "drake"
    elif necesita_sf:
        linea = "igdrassil"
    else:
        linea = "ninguno"
    return {
        "plugin": nombre, "depend": depend, "softdepend": soft, "api_version": api, "paper_api": paper,
        "core_version": core_ver, "linea": linea, "imports_drake": drake, "imports_upstream": upstream,
        "clases_slimefun": sf_clases, "requiere_slimefun": "Slimefun" in depend,
    }


def notas(a):
    d = detectar()
    repo = a.repo
    pa = d["paper_api"]
    mc = pa.split("-")[0] if pa and "$" not in pa else (f"{d['api_version']}.x" if d["api_version"] else "1.21.x")
    l = [f"## {d['plugin']} {a.version}", ""]
    l += ["| | |", "|---|---|",
          f"| **Minecraft / servidor** | Paper o Purpur {mc} (Java 21) |",
          f"| **Archivo** | `{pathlib.Path(a.jar).name}` |",
          f"| **SHA-256** | `{a.sha256}` |", ""]
    if d["linea"] == "drake":
        core = d["core_version"] or "11.0-Drake-1.21.11"
        l += ["### Que core de Slimefun necesita", "",
              f"Necesita **Slimefun4-Drake** (`slimefun-core` **{core}**): "
              "[descargar el core](https://github.com/SlimefunNewHorizons/Slimefun4-Drake/releases).", "",
              "### Por que NO funciona con el Slimefun 4 normal", "",
              f"Este addon importa `dev.drake.dough` ({d['imports_drake']} referencias en el codigo). Slimefun4-Drake renombro la "
              "libreria base `io.github.bakedlibs.dough` a `dev.drake.dough` para fijar la version que usa el servidor. Un "
              "Slimefun 4 upstream (o Slimefun-Gugu) solo trae el paquete original, asi que al cargar este plugin falta "
              "`dev.drake.dough` y el servidor lo desactiva con `NoClassDefFoundError`.",
              "Ademas, el core Drake usa la Paper API 1.21.11 directamente (cabezas con perfiles, atributos de salud, "
              "eliminacion de API deprecada) y esta probado en Paper 1.21.11, 26.1 y 26.2."
              ""]
        if d["imports_upstream"]:
            l += ["", f"> En migracion: quedan {d['imports_upstream']} referencias a `io.github.bakedlibs.dough` "
                  "(el objetivo es volver a ser compatible con el core Slimefun 4 normal)."]
    elif d["linea"] == "nucleo":
        l += ["### Que es", "",
              "Este es el **core** (`slimefun-core`) que necesitan los addons de la linea Drake. Los addons de la org "
              "no cargan en un Slimefun 4 normal porque importan `dev.drake.dough` (libreria base renombrada desde "
              "`io.github.bakedlibs.dough`); este core es el que la trae. Instalalo en lugar del Slimefun 4 normal, no junto a el.", ""]
    elif d["linea"] == "igdrassil":
        l += ["### Que core de Slimefun necesita", "",
              "Compatible con el **Slimefun 4 estandar** (importa `io.github.bakedlibs.dough`, el paquete upstream). "
              "Funciona con Slimefun4 upstream, Slimefun-Gugu y con [Slimefun4-Igdrassil]"
              "(https://github.com/SlimefunNewHorizons/Slimefun4-Igdrassil/releases) (el fork de la org alineado con upstream).", ""]
    else:
        l += ["### Que core de Slimefun necesita", "", "**Ninguno**: este plugin funciona por si solo en Paper/Purpur, sin Slimefun."
              + (" Si Slimefun esta instalado, activa integraciones opcionales." if "Slimefun" in d["softdepend"] else ""), ""]
    l += ["", "### Verificacion de esta release", "",
          "Compilado y con tests ejecutados en CI antes de publicar (si algun test falla no se publica). "
          "Detalle del flujo: [AUDITORIA de CI](https://github.com/SlimefunNewHorizons/.github/blob/main/docs/CI_ORG.md).", "",
          f"Repositorio: https://github.com/SlimefunNewHorizons/{repo}"]
    sys.stdout.write("\n".join(l) + "\n")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("json")
    n = sub.add_parser("notas")
    n.add_argument("--version", required=True)
    n.add_argument("--jar", required=True)
    n.add_argument("--sha256", required=True)
    n.add_argument("--repo", default=RAIZ.resolve().name)
    a = ap.parse_args()
    if a.cmd == "json":
        print(json.dumps(detectar(), ensure_ascii=False))
    else:
        notas(a)
