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
print(max([MIN] + [n for n in pedidas if n <= MAX]))
