<div align="center">

<img src="https://raw.githubusercontent.com/SlimefunNewHorizons/.github/main/profile/assets/new-horizons-banner.svg" alt="Slimefun: New Horizons — Modernizando Slimefun para la próxima generación de Minecraft" width="100%" />

# Slimefun: New Horizons

### Modernizando Slimefun para la próxima generación de Minecraft

[🌐 Web](https://web.drakescraft.cl) ·
[💬 Discord](https://discord.gg/rv3vtXZTk7) ·
[🌌 StarSuites](https://github.com/SlimefunNewHorizons/Drakes-Suites) ·
[🧭 Todos los repositorios](https://github.com/orgs/SlimefunNewHorizons/repositories) ·
[📊 Estado verificado](https://github.com/SlimefunNewHorizons/.github/blob/main/docs/status/README.md) ·
[⚖️ Derechos y atribución](https://github.com/SlimefunNewHorizons/.github/blob/main/RIGHTS_AND_ATTRIBUTION_ES.md) ·
[🇬🇧 English](https://github.com/SlimefunNewHorizons)

</div>

---

## ¿Qué es esto?

Esta organización es la casa de un **ecosistema**, no de un solo plugin. Nació para llevar [Slimefun](https://github.com/Slimefun/Slimefun4) y sus addons a la próxima generación de servidores
de Minecraft, y creció alrededor de una red de producción real, **DrakesCraft** (`mc.drakescraft.cl`, Java y Bedrock). Todo se prueba ahí antes de publicarse.

| Línea | En una frase |
|---|---|
| ⚡ **DrakesPurpur** | El motor de servidor soberano: Java 25 LTS, cómputo off-heap en Rust con Panama FFM, auto-reparación Crash Guard, auditoría SQLite WAL, respaldos diarios 7z y aislamiento estricto de 6 modalidades. |
| 🧬 **Slimefun: New Horizons** | Ports, forks y arreglos que mantienen vivos a Slimefun y sus addons en Paper actual. |
| 🌌 **StarSuites** | Un monorepo que está absorbiendo los repositorios históricos de addons en 8 mega-suites. |
| ⭐ **Star** | La plataforma alrededor del juego: Star Engine, operaciones autónomas, observabilidad y respaldos. |
| 🏛️ **Odysseia** | El motor del servidor: comercio, modalidades, salvaguardas de economía, eventos y jefes. |
| 🐉 **Drakes** | Los plugins de juego originales de la red DrakesCraft. |
| 🌠 **Multiverse** | La suite independiente de **Chagui68**, interoperable con Slimefun pero autónoma. |

> ℹ️ **Crédito e independencia.** Slimefun es obra de **TheBusyBiscuit** y la comunidad de Slimefun (GPL-3.0). **No somos sus autores originales** ni estamos **afiliados ni respaldados** por el equipo oficial.
> Modernizamos y rescatamos; las licencias y créditos originales siempre se conservan — ver [Derechos y atribución](https://github.com/SlimefunNewHorizons/.github/blob/main/RIGHTS_AND_ATTRIBUTION_ES.md).

---

## 📊 Estado verificado y Avance Temporada 2 (Mediados de Octubre 2026)

Las cifras se **midieron y auditaron**:

| Pregunta | Respuesta | Evidencia |
|---|---|---|
| Plugins corriendo en la red de producción (Paper/Purpur **1.21.11**) | **169 cargados (192 verificados en Staging con 0 deshabilitados)** | Log del servidor en vivo |
| …de los cuales mantenidos o adaptados por nosotros | **≈ 64** (43 forks/originales con marca Drake + 21 adaptados) | Versiones de la lista de plugins en vivo |
| …de terceros, sin modificar | **105** | Ídem |
| Repositorios en la organización | **197** (más de 90 ports/forks `-drake` mantenidos) | API de GitHub |
| Repositorios cuyo build apunta a la API **1.21.11** | **61** de 75 con objetivo detectable | Archivos de build |
| **StarSuites compilan en Paper 26.2** (`26.2.build.129-stable`, JDK 25) | **9 / 9 módulos ✅** | Reactor de Maven, `BUILD SUCCESS` |
| **Flota Staging Temporada 2 (Purpur 26.x)** | **49 / 49 addons 100% verificados y certificados en Staging ✅** | Supervisor de staging y telemetría SRE |
| StarSuites validadas **corriendo** en un servidor 26.x | **Certificadas en Staging (49/49 addons verificados)** ✅ | Log del servidor de staging y supervisor |

> ℹ️ **Verificación Autónoma Continua:** El porteo y la validación son monitoreados en tiempo real por el supervisor SRE autónomo con supresión de alertas innecesarias, asegurando despliegues fluidos y alertando a humanos solo ante bloqueos críticos.

---

## ⭐ Star — la plataforma

**Star** agrupa todo lo que corre *alrededor* del juego: el **Star Engine** (la evolución del kernel de servidor de Odysseia, entregado en la Suite 7), **SAORI** (operaciones autónomas: asistentes de
Discord y WhatsApp, triaje de tickets, manejo de incidentes), observabilidad, respaldos automáticos y un entorno en la nube 24/7. Es lo que permite que un equipo pequeño opere una red grande con mods.

## 🏛️ Odysseia — el motor del servidor

`Odysseia` es el motor que hace que una red de **6 modalidades conectadas (Slimefun, Clásico, SkyBlock, OneBlock, OneChunk, Laboratorio)** se comporte como un solo producto. Levantado sobre la plantilla de addon de la comunidad de Slimefun, incluye:

- **Motor de compras** — entrega idempotente de compras de la tienda, con compuerta de identidad, reembolsos revocables y vías de revisión manual.
- **Aislamiento de modalidades** — viaje entre modos con inventarios, bóvedas y economías separados.
- **Vigilante de economía** — salvaguarda dentro del juego contra ganancias anormalmente rápidas.
- **Eventos, jefes, juegos de chat, cosméticos, kits, cheques, sistema de renacimiento, coordinación de reinicios** y un **puente nativo en Rust** (`Odysseia-Rust`) para rutas críticas.

## 🐉 Drakes — los plugins de juego de DrakesCraft

| Plugin | Qué hace |
|---|---|
| `DrakesRankup` | 50 rangos anime/shōnen, transformaciones, auras y un sumidero de economía por mantenimiento de rango |
| `DrakesVIPPlusPlus` | 15 rangos VIP con habilidades activas únicas, cosméticos y boosters automáticos de fin de semana |
| `DrakesBosses` | Arenas, jefes adaptativos, recompensas y economía de entradas (anti-AFK, daño verdadero adaptativo) |
| `DrakesCrates` | Cajas virtuales y físicas con soporte Slimefun y guarda para el modo Clásico |
| `DrakesSlimeMarket` | Mercado dinámico de materiales de Slimefun con control de inflación |
| `DrakesNanotech` | Materia programable de ultra-endgame y tecnología cósmica para Slimefun |
| `DiosesDrakes` · `ArcanaDrakes` | Progresión divina/mitológica y magia elemental |
| `DrakesTranslate` | Traducción nativa de chat en tiempo real |

## 🌠 Multiverse y Pumpkin — por [Chagui68](https://github.com/Chagui68)

Una suite de plugins y arquitectura de launcher soberana e independiente concebida y desarrollada por **Chagui68** (Chagui), que funciona **de forma autónoma** y además **interopera** con Slimefun mediante puentes opcionales de cero sobrecarga (sin dependencia obligatoria):

| Proyecto / Plugin | Dominio e Innovación | En Producción / Staging |
|---|---|---|
| **MultiverseNets** | Logística digital autónoma de alto rendimiento, enrutamiento y almacenamiento cuántico (109 tests unitarios superados en Paper 1.21.11 y Purpur 26.2) | ✅ v6.3 en Staging (v4.7 en Dallas) |
| **MultiverseCreatures** | Criaturas mitológicas temáticas, rituales celestiales y panteones de jefes adaptativos | ✅ v4.9 en Staging (v2.4 en Dallas) |
| **MultiverseTinker** | Metalurgia modular, más de 90 minerales y aleaciones, fundición automatizada y forja | ⏳ Portado a 26.2 |
| **MultiverseProgramming**| Tortugas de automatización programables dentro de Minecraft y matrices lógicas | ✅ v1.2.2 en Staging |
| **MultiverseGambling** | Minijuegos de azar, dados y sistemas probabilísticos respaldados en Dragmas | ✅ Verificado en Staging |
| **[Pumpkin-launcher](https://github.com/Chagui68/Pumpkin-launcher)** | Arquitectura de launcher de nueva generación pionera en aislamiento de ClassLoader, sanitización de plugins en runtime y capa PatchBukkit | 🚀 Innovación Soberana |

---

## 🌌 StarSuites

El monorepo `Drakes-Suites` está **absorbiendo los más de 180 repositorios históricos de addons en 8 mega-suites más Multiverse**, con un solo motor de ticker y un sistema de configuración modular
(`modules/<módulo>.yml`, recargable en caliente). **La fase 1 está completa; la fase 2 (absorción) sigue en curso: hoy hay 44 módulos de addons dentro.**

| Suite | Artefacto | Módulos absorbidos | Enfoque |
|---|---|---:|---|
| 0 · Core | `drakes-core.jar` | 1 | Kernel, Dough integrado, ticker centralizado, SQLite WAL, registros de auditoría |
| 1 · Tech | `drakes-tech.jar` | 6 | Logística tipo Networks, DynaTech, FoxyMachines, Supreme, FluffyMachines, InfinityExpansion |
| 2 · Bio | `drakes-bio.jar` | 7 | Cultivation, GeneticChickengineering, FlowerPower, TreeTaps, MobCapturer, ExoticGarden, SlimyBees |
| 3 · Magic | `drakes-magic.jar` | 4 | RelicsOfCthonia, Crystamae, AlchimiaVitae, SoulJars |
| 4 · Generators | `drakes-generators.jar` | 6 | LiteXpansion, reactores, SMG, EcoPower, ore chunks, generadores definitivos |
| 5 · Utility | `drakes-utility.jar` | 13 | Mochilas, SlimeHUD, ChestTerminal, SFCalc, pistola de portales, silenciador y más |
| 6 · Combat | `drakes-combat.jar` | 6 | Warfare, ObsidianExpansion, ExtraGear, drops de mobs, SlimeTinker |
| 7 · Server | `drakes-server.jar` | 1 | Star Engine, módulo de economía |
| Multiverse | `drakes-multiverse.jar` | — | Obra de Chagui68 (ver arriba) |

Lo que aún no se absorbe sigue publicándose como ports `-drake` individuales, conservando cada ID de ítem para no poner en riesgo datos de jugadores.

---

## 🧭 Hoja de ruta (en exploración)

- **Temporada 2 en Paper 26.x** — validación en ejecución de cada suite sobre un servidor 26.x real y luego despliegue atómico.
- **DrakesID** — identidad de cuenta propia (una cuenta, varias identidades Java/Bedrock, alcance por modalidad) para simplificar compras, rollbacks y rangos.
- **3D basado en displays** — tuberías y cables dibujados con entidades `ItemDisplay`/`BlockDisplay`, inspirado en [PylonMC/Rebar](https://github.com/pylonmc/rebar) (LGPL-3.0, con atribución).
- **Plan de derechos y licencias** — un bloque de licencia y créditos en cada repositorio ([política](https://github.com/SlimefunNewHorizons/.github/blob/main/RIGHTS_AND_ATTRIBUTION_ES.md)).

## 🤝 Sobre los hombros de

Lista no exhaustiva de autores y proyectos upstream sobre los que construimos (cada repositorio trae sus propios créditos y licencia):
**TheBusyBiscuit y la comunidad de Slimefun** (Slimefun 4) · **Sefiraat** (Networks, SlimeTinker y otros addons) · **Seggan** · **balugaq** y **ytdd9527** (NetworksExpansion / JustEnoughGuide) ·
**J3fftw** (WorldEditSlimefun) · **tastybento y el equipo de BentoBox** (BentoBox, InvSwitcher) · **Dominic Feliton** (WorldwideChat) · **Rugzy** (PlayerVaultZ) · **spearforge** (sBank) · **PylonMC** (inspiración).

## Cómo contribuir

1. El desarrollo activo de los plugins consolidados ocurre en [`Drakes-Suites`](https://github.com/SlimefunNewHorizons/Drakes-Suites).
2. **Nunca romper datos de jugadores**: ningún ítem, inventario ni historial de compras puede ponerse en riesgo; se conservan las claves PDC.
3. Los forks y consolidaciones **conservan sus licencias originales** y acreditan a los autores originales.
4. Los README públicos se escriben en inglés; la documentación en español vive al lado como [`README_ES.md`](https://github.com/SlimefunNewHorizons/.github/blob/main/profile/README_ES.md).

<div align="center">

**Slimefun: New Horizons** · hecho con ♥ por la comunidad de DrakesCraft Labs<br/>
[Web](https://web.drakescraft.cl) · [Discord](https://discord.gg/rv3vtXZTk7) · [StarSuites](https://github.com/SlimefunNewHorizons/Drakes-Suites)

</div>
