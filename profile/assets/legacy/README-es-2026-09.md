<div align="center">

<img src="https://raw.githubusercontent.com/SlimefunNewHorizons/.github/main/profile/assets/labs-hero.svg" alt="DrakesCraft Labs" width="100%" />

# ✦ DrakesCraft Labs ✦

### Ingeniería de Sistemas, Redes de Producción & Suites de Nueva Generación

[![StarSuites](https://img.shields.io/badge/StarSuites-Monorepo_LTS-8B5CF6?style=for-the-badge&logo=github&logoColor=white)](https://github.com/SlimefunNewHorizons/Drakes-Suites)
[![DrakesCraft](https://img.shields.io/badge/DrakesCraft-Producción-22C55E?style=for-the-badge&logo=minecraft&logoColor=white)](https://web.drakescraft.cl)
[![Java 21](https://img.shields.io/badge/Java-21_LTS-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)](https://openjdk.org/)
[![Rust Workspace](https://img.shields.io/badge/Rust-Off--Heap_SIMD-DEA584?style=for-the-badge&logo=rust&logoColor=white)](https://www.rust-lang.org/)
[![Community](https://img.shields.io/badge/Discord-Comunidad-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/rv3vtXZTk7)

**DrakesCraft Labs es la organización de ingeniería de software, videojuegos e infraestructura de JackStar.**  
Aquí se investigan, desarrollan y blindan las tecnologías que sostienen la red de producción de Minecraft DrakesCraft (Dallas, TX), motores off-heap en Rust, suites modulares y sistemas de orquestación autónoma.

[🌐 Web Oficial](https://web.drakescraft.cl) ·
[💬 Comunidad Discord](https://discord.gg/rv3vtXZTk7) ·
[🌌 StarSuites Monorepo](https://github.com/SlimefunNewHorizons/Drakes-Suites) ·
[🧭 Explorar Repositorios](https://github.com/orgs/SlimefunNewHorizons/repositories)

</div>

---

## 🏛️ El Proyecto Insignia: StarSuites (`Drakes-Suites`)

La organización opera bajo la arquitectura unificada **[StarSuites](https://github.com/SlimefunNewHorizons/Drakes-Suites)**, concebida y dirigida por **JackStar**.  
StarSuites consolida y moderniza más de 180 micro-repositorios históricos en **8 Mega-Suites oficiales** más la Suite soberana Multiverse:

* **Suite 0 (`drakes-core.jar`):** Kernel, motor Dough-core shadeado, Ticker centralizado (`SuiteTickerEngine`), JNI Bindings y persistencia SQLite WAL.
* **Suite 1 (`drakes-tech.jar`):** Logística digital (Networks), celdas de almacenamiento masivo cuántico, InfinityExpansion, DynaTech y FastMachines.
* **Suite 2 (`drakes-bio.jar`):** GeneticChickengineering (Tiers 0-9), ExoticGarden, Cultivation y apicultura SlimyBees.
* **Suite 3 (`drakes-magic.jar`):** AlchimiaVitae, Crystamae, RelicsOfCthonia, transmutación y botánica oscura.
* **Suite 4 (`drakes-generators.jar`):** LiteXpansion, SMG, reactores solares, nucleares y celdas energéticas.
* **Suite 5 (`drakes-utility.jar`):** DyedBackpacks, ColoredEnderChests, ChestTerminal, SFCalc y SlimeHUD.
* **Suite 6 (`drakes-combat.jar`):** DrakesBosses, SlimeTinker, SlimefunWarfare, armaduras reactivas y arsenal divino.
* **Suite 7 (`drakes-server.jar`):** **Star Engine** (evolución canónica de Odysseia a **Star**), enlace Rust nativo (`Star-Rust`), InvSwitcher (5 modalidades), PlayerVaultZ y economía macroeconómica dinámica.
* **Suite Multiverse (`drakes-multiverse.jar`):** **Autoría Soberana de Chagui68**, consolidando `MultiverseCreatures` y `MultiverseNets`.

> ℹ️ **Aclaración Canónica de Autoría Upstream (Slimefun):**  
> Slimefun original es una creación monumental de código abierto de **TheBusyBiscuit** y la comunidad. **DrakesCraft Labs / JackStar no es su autor original**, sino el arquitecto de modernización y rescate: resolución de cuellos de botella en Paper 1.21.11, aceleración off-heap en Rust ([`Slimefun-Rust`](https://github.com/SlimefunNewHorizons/Slimefun-Rust)) y unificación en suites desacopladas.

---

## 🌐 Líneas de Desarrollo

| Línea | Dominio y Enfoque | Tecnologías y Proyectos Clave |
|---|---|---|
| 🌌 **StarSuites & Gaming** | Suites consolidadas, plugins de alto rendimiento y modalidades para Minecraft. | [StarSuites](https://github.com/SlimefunNewHorizons/Drakes-Suites), [DrakesBosses](https://github.com/SlimefunNewHorizons/DrakesBosses), [BentoBox-Drake](https://github.com/SlimefunNewHorizons/BentoBox-Drake) |
| ⚡ **Motores Nativos Rust** | Aceleración matemática SIMD, algoritmos de grafos y bypass de Garbage Collector. | [Slimefun-Rust](https://github.com/SlimefunNewHorizons/Slimefun-Rust), [Odysseia-Rust](https://github.com/SlimefunNewHorizons/Odysseia-Rust) (`libodysseia_ffi.so`) |
| 🌸 **SRE & IA Autónoma** | Coordinación de agentes autónomos, observabilidad y resiliencia de producción. | [SAORI Core](https://github.com/JackStar6677-1/saori), Tríada Simétrica (Antigravity · Codex · Claude) |
| 🛡️ **Seguridad e Infraestructura** | Protección perimetral, auditoría de logs, persistencia transaccional y proxying. | [IP-Detector](https://github.com/SlimefunNewHorizons/IP-Detector), [maven-repo](https://github.com/SlimefunNewHorizons/maven-repo) |
| 🌐 **Plataformas Web & Portal** | Portales de comunidad, tiendas sincronizadas y telemetría de jugadores. | [drakescraft-web](https://github.com/SlimefunNewHorizons/drakescraft-web) |

---

## 📋 Directiva de Desarrollo y Contribución

1. **Monorepo Central (`Drakes-Suites`):** Todo desarrollo activo para plugins consolidados se realiza exclusivamente en el monorepo [StarSuites](https://github.com/SlimefunNewHorizons/Drakes-Suites).
2. **Integridad de Datos:** Ningún cambio puede comprometer ítems de jugadores, inventarios o compras históricas. Claves PDC estrictamente conservadas.
3. **Respaldo de Producción:** Despliegues en Dallas protegidos mediante backups automáticos y reinicios programados con aviso previo.
4. **Crédito y Licencias:** Todo fork y consolidación preserva sus licencias de origen (GPLv3 / MIT / Apache 2.0) y menciones a los autores originales.

---

<div align="center">

**DrakesCraft Labs · Arquitectura Diseñada por JackStar**  
[DrakesCraft](https://web.drakescraft.cl) · [Discord](https://discord.gg/rv3vtXZTk7) · [StarSuites](https://github.com/SlimefunNewHorizons/Drakes-Suites)

</div>
