# CI de la organizacion (workflows reutilizables)

Fuente de verdad: este repo (`SlimefunNewHorizons/.github`). Cada repo solo tiene dos archivos de ~15 lineas
(`ci.yml` y `publicar.yml`, ver `templates/ci/`) que llaman a los workflows de aqui. Cambiar la logica aqui la cambia
en todos los repos.

## Por que existe (auditoria 2026-10-14)
324 workflows en 139 repos con codigo: el CI "verde" no verificaba nada (`drake-ci.yml` hacia `exit 0`), se publicaba
en Modrinth con `-DskipTests`, no habia analisis de seguridad y la prueba entre versiones de Minecraft era manual.
Chagui68 ya habia resuelto esto en MultiverseCreatures/MultiverseNets (`verify.yml`, `compatibility.yml`,
`server-smoke-test.sh`); su enfoque es la base de esta plantilla y sus repos **conservan** sus propios workflows
(se les anade encima, no se sustituyen).

## Capas
| Workflow | Que hace | Bloquea |
|---|---|---|
| `verificar.yml` | Maven/Gradle con tests (`mvn verify`), prepara el maven-repo de la org (falla si no puede), sube jar + informe | merge y release |
| `seguridad.yml` | CodeQL (Java), dependency-review en PR, gitleaks sobre el historial | merge |
| `compatibilidad.yml` | Paper real con el MISMO jar en 1.21.11 y 26.2; descarga el core de Slimefun si el addon lo necesita | release (opcional, `smoke-bloquea`) |
| `publicar.yml` | umbral de lineas/hotfix -> verificar -> compatibilidad -> GitHub Release (jar + SHA-256 + notas) -> Modrinth | -- |

## Notas de cada release (que version corre, que core, por que no sirve el Slimefun 4 normal)
`detectar-core.py` lee el codigo del repo y escribe notas VERDADERAS para ese repo:
- **Linea Drake** (`dev.drake.dough`): necesita Slimefun4-Drake (`slimefun-core` 11.0-Drake-1.21.11). No carga con un
  Slimefun 4 normal porque el core Drake renombro la libreria base `io.github.bakedlibs.dough` a `dev.drake.dough`: en un
  Slimefun upstream falta ese paquete y el plugin se desactiva con `NoClassDefFoundError`. Ademas usa la Paper API
  1.21.11 directamente.
- **Linea Igdrassil / estandar** (`io.github.bakedlibs.dough`): compatible con Slimefun 4 upstream, Gugu e Igdrassil.
- **Sin Slimefun**: funciona solo en Paper/Purpur.
- Un repo en migracion de Drake a estandar cambia de linea solo cuando el codigo lo hace: las notas se corrigen solas.

## Reglas de la plantilla
`permissions` minimos; acciones fijadas por SHA (Dependabot las actualiza); la publicacion nunca corre en PR (el token
no se expone a forks); un fallo de test o de servidor impide publicar; scripts compartidos en `.github/scripts/`.

## Dependencias extra para el smoke test
Un plugin con softdepend puede asumir que esa API existe. Declarala en `.github/smoke-deps.txt` del repo:
```
modrinth:luckperms
https://ejemplo.org/otro.jar
```

## Estado
Primer barrido el 2026-10-14 en 134 repos: ver `docs/ESTADO_CI_ORG_20261014.md` en ai-hub (99 verdes, 48 rojos reales).
