#!/usr/bin/env python3
"""Imprime la version de Java que necesita el repo (21 por defecto, hasta 25).

Lee pom.xml / build.gradle(.kts) / pom hijos y toma la MAYOR version pedida (release, source/target, java.version,
JavaVersion.VERSION_N, JavaLanguageVersion.of(N), jvmToolchain(N)). Antes todos se compilaban con 21 y los repos que
piden 25 fallaban con "release version 25 not supported".
"""
import pathlib
import re
import sys

MIN, MAX = 21, 25
# Override explicito del repo: `.github/java-version` con un numero (p. ej. 25), para los que dependen de jars compilados
# para Java 25 (worldguard-core 7.0.18, invui 2.3.0...) sin que el pom lo diga.
_override = pathlib.Path(".github/java-version")
if _override.is_file():
    try:
        print(int(_override.read_text().strip()))
        sys.exit(0)
    except ValueError:
        pass
pedidas = []
patrones = [
    r"<(?:maven\.compiler\.(?:release|source|target)|java\.version|release|source|target|jdk\.version|java-version)>\s*(\d+)\s*<",
    r"JavaVersion\.VERSION_(\d+)",
    r"JavaLanguageVersion\.of\((\d+)\)",
    r"jvmToolchain\((\d+)\)",
    r"(?:sourceCompatibility|targetCompatibility)\s*=\s*['\"]?(?:JavaVersion\.VERSION_)?(\d+)",
]
for ruta in list(pathlib.Path(".").glob("pom.xml")) + list(pathlib.Path(".").glob("*/pom.xml")) + \
        list(pathlib.Path(".").glob("build.gradle*")) + list(pathlib.Path(".").glob("*/build.gradle*")):
    try:
        t = ruta.read_text(encoding="utf-8", errors="replace")
    except OSError:
        continue
    for p in patrones:
        for m in re.findall(p, t):
            n = int(m)
            if 8 <= n <= 30:
                pedidas.append(n)
# Paper API 26.x esta compilada para Java 25 ("class file has wrong version 69.0, should be 65.0" con Java 21)
for ruta in list(pathlib.Path(".").glob("pom.xml")) + list(pathlib.Path(".").glob("*/pom.xml")) +         list(pathlib.Path(".").glob("build.gradle*")) + list(pathlib.Path(".").glob("*/build.gradle*")):
    try:
        t = ruta.read_text(encoding="utf-8", errors="replace")
    except OSError:
        continue
    if re.search(r"paper-api</artifactId>\s*<version>\s*2[6-9]\.", t) or re.search(r"paper-api:2[6-9]\.", t)             or re.search(r"<paper\.version>\s*[\[(]?\s*2[6-9]\.", t):
        pedidas.append(25)
print(max([MIN] + [n for n in pedidas if n <= MAX]))
