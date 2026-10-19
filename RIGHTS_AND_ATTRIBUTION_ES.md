# Política de Derechos, Licencias y Atribución

> **Estado: BORRADOR para revisión del dueño.** Es una política de ingeniería, **no asesoría legal**. Antes de hacerla valer frente a terceros o de cambiar la
> licencia de un repositorio publicado, debe revisarla un abogado. 🇬🇧 [English version](RIGHTS_AND_ATTRIBUTION.md)

Aplica a todos los repositorios de la organización **SlimefunNewHorizons** (Slimefun: New Horizons / StarSuites / DrakesCraft) y a todo lo publicado desde ella
(GitHub, Modrinth, Maven, releases).

## 1. Principios

1. **Nuestra obra original es © JackStar6677-1 y los colaboradores de DrakesCraft Labs — TODOS LOS DERECHOS RESERVADOS**, salvo que el repositorio incluya un archivo `LICENSE` que diga lo contrario.
2. **Los autores originales siempre reciben crédito y sus licencias siempre se conservan.** Nunca quitamos, reemplazamos, acortamos ni contradecimos un aviso de copyright o licencia del upstream.
3. **Los creadores de Slimefun conservan todos sus derechos.** Slimefun 4 es obra de **TheBusyBiscuit y la comunidad de Slimefun** y está bajo **GPL-3.0**. Nada de esta política
   licencia, restringe ni "reserva" su obra ni ninguna modificación de ella.
4. **El copyleft no es opcional.** Una obra derivada de código GPL-3.0 debe distribuirse bajo GPL-3.0; "todos los derechos reservados" **no** puede aplicarse a ella.
   Por eso "todos los derechos reservados" se aplica solo al código que realmente es nuestro (§2).

## 2. Clases de repositorio

Cada repositorio pertenece a una sola clase, registrada en [`docs/rights/repo-rights-manifest.csv`](docs/rights/repo-rights-manifest.csv).

| Clase | Qué es | Licencia | Créditos |
|---|---|---|---|
| **A · ORIGINAL** | Escrito 100 % por nosotros; no deriva de código ajeno ni de una biblioteca copyleft. | **Todos los Derechos Reservados** (`templates/rights/LICENSE-ARR.txt`). | Nuestra línea de copyright; dependencias de terceros en `NOTICE`. |
| **B · DERIVADO ABIERTO** | Fork, port, reescritura o consolidación de un proyecto ajeno (p. ej. Slimefun y sus addons), incluido el código propio que usa la API de Slimefun. | **Se conserva la licencia del upstream** (GPL-3.0 / LGPL-3.0 / MIT / Apache-2.0 …). Los módulos ligados a Slimefun usan **GPL-3.0** por defecto. | Copyright del upstream + `NOTICE` + bloque de créditos en el README (§4). |
| **C · DE AUTORÍA AJENA, ALOJADO AQUÍ** | Escrito por otra persona que lo desarrolla o aloja en la organización (p. ej. **Chagui68**: MultiverseNets / MultiverseTinker / MultiverseCreatures / MultiverseProgramming). | **La que elija el autor**, constando en el archivo. Nunca es nuestra para relicenciar. | Autor nombrado en README y `NOTICE`. |
| **D · UPSTREAM DESCONOCIDO** | Derivado de código ajeno cuya licencia **no hemos verificado**. | **Sin resolver: se trata con el criterio más estricto** (no copiar, no publicar versiones nuevas) hasta verificar. | `NOTICE` con el autor original de inmediato. |

> **Repositorios mixtos** (p. ej. el monorepo `Drakes-Suites`) se clasifican por su componente *más restrictivo*: si algún módulo deriva de código GPL, el distribuible
> combinado es GPL-3.0. Los módulos originales conviene mantenerlos en su propio repositorio de clase A.

## 3. Qué debe contener cada clase

* **A:** `LICENSE` (texto ARR), encabezado de copyright (opcional por archivo), pie de README.
* **B / C / D:** el `LICENSE` del upstream **sin modificar**, un `NOTICE` (plantilla: `templates/rights/NOTICE-UPSTREAM.md`) y el bloque de créditos del README.
* **Todas:** nunca borrar `LICENSE`, `NOTICE`, `AUTHORS` ni encabezados de copyright heredados.

## 4. Bloque de créditos obligatorio para todo lo relacionado con Slimefun

Va en el README de cada repositorio clase B/C/D que extienda o derive de Slimefun (ajustar la segunda línea al addon real):

```markdown
## Credits & License
This project is based on / extends **[Slimefun 4](https://github.com/Slimefun/Slimefun4)** by **TheBusyBiscuit** and the Slimefun community (GPL-3.0).
Derived from **<Addon name>** by **<original author>** (<upstream URL>, <upstream license>).
It is an independent community project and is **not affiliated with or endorsed by** the official Slimefun team.
Modifications © DrakesCraft Labs contributors, distributed under the same license as the original.
```

## 5. Reglas de distribución

* Las obligaciones de la GPL se activan al **distribuir** (publicar un jar en Modrinth, GitHub Releases o Maven cuenta). Un jar derivado de GPL solo puede publicarse junto
  con su código fuente y el archivo `LICENSE`. **Los repositorios sin `LICENSE` que publican builds están hoy fuera de cumplimiento** (ver §7).
* **Los repositorios clase D no publican nada** (ni releases ni proyecto en Modrinth) hasta verificar la licencia del upstream u obtener permiso.
* Correr el software en nuestro propio servidor no es distribuir; publicar una descarga sí.

## 6. Contribuciones

Las contribuciones a repositorios clase A se aceptan solo si quien contribuye declara, en el pull request, que su aporte puede usarse bajo la licencia del repositorio y que tiene
derecho a enviarlo. Las contribuciones a B/C/D se aceptan bajo la licencia vigente del repositorio.

## 7. Estado actual (auditoría del 2026-10-02) y plan de aplicación

La auditoría de 179 clones locales encontró: **75 repositorios sin archivo de licencia**, 66 GPL-3.0, 29 MIT, 4 LGPL-3.0, 1 Apache-2.0, y 100 repositorios que dependen de Slimefun
(17 sin licencia; 15 sin créditos en el README). Solo **5 repositorios son claramente clase A**; 42 no se pueden clasificar sin el criterio del dueño.
Tabla completa y acción propuesta por repositorio: [`docs/rights/repo-rights-manifest.csv`](docs/rights/repo-rights-manifest.csv).

Orden de aplicación (no aplicar a ciegas: cada licencia necesita la confirmación del dueño):

1. **Frenar el riesgo:** en repositorios clase D, pausar releases y publicación en Modrinth; agregar `NOTICE` con el autor original.
2. **Agregar los archivos de licencia faltantes**, empezando por los 17 repositorios ligados a Slimefun sin ninguno (GPL-3.0) y los clase A confirmados (ARR).
3. **Agregar el bloque de créditos (§4)** a los 15 README relacionados con Slimefun que no lo tienen.
4. Resolver la clase D: obtener el texto de licencia del upstream, un permiso escrito, o retirar/reescribir el código.
5. Revisión trimestral y manifiesto al día (se recomienda un chequeo de CI de presencia de `LICENSE`/`NOTICE`).

## 8. Ajustes de la organización en GitHub que respaldan esta política

La página *Repository policies* (rulesets de organización) **no se aplica en el plan Free**: GitHub indica que solo rige al pasar a **GitHub Team**.
Controles equivalentes y gratuitos: **Organization → Settings → Member privileges**:

| Control | Recomendado |
|---|---|
| Creación de repositorios | Solo dueños (o sin creación pública) |
| Borrado y transferencia de repositorios | **No permitir a miembros** |
| Permisos base | *Read* |
| Exigir autenticación en dos pasos | **Activar** (hoy está desactivada) |

Si la organización pasa a GitHub Team, crear una política de repositorio con: **Restrict deletions** y **Restrict transfers** (lista permitida = dueños),
**Restrict creations** (lista permitida = dueños) y **Restrict visibility** solo si se quiere privado por defecto.
