# Ports status — 1.21.11 y 26.x (medición en el VPS)

> Generado por `~/ai-hub/scripts/gen_ports_status.sh` el 2026-10-02 desde `~/ai-hub/log/ports/ports_status_raw.csv`.
> **«compila» ≠ «corre».** *Compila* = `mvn -B -fae package` terminó en el VPS con el JDK indicado.
> *Corre* = el plugin arrancó y cargó en un servidor real de esa versión; **esta página no lo certifica**.
> Nada de aquí se llama «portado» hasta que exista prueba de ejecución (staging 26.x / producción 1.21.11).

## Metodología

```bash
# 1.21.11 (JDK 21) — compila + tests
~/ai-hub/scripts/build_seguro.sh 21 <repo> mvn -B -fae package
# 26.x (JDK 25) — compila sin tests
~/ai-hub/scripts/build_seguro.sh 25 <repo> mvn -B -fae -DskipTests \
    -Dpaper.version=26.2.build.129-stable -Djava.version=25 -Dmaven.compiler.release=25 clean package
```

* El build 26.x lleva `clean`: sin él, el compilador incremental reutiliza las clases del build JDK 21 («Nothing to compile») y el resultado no prueba nada. Desde 2026-10-04 `check_ports.sh` lo incluye y marca `NO_MEDIDO` si no recompiló.
* Siempre vía `build_seguro.sh` (un solo build a la vez en todo el VPS, `nice`/`ionice`, espera si la carga ≥ 5). Máximo ~450 s de presupuesto por pasada.
* `indeterminado` = el build falló sin llegar a compilar (p. ej. no resolvió dependencias): **no es un no-compila**, hay que repetirlo.
* Los cambios propios de 26.x van a la rama `port-26x` de cada repo, nunca directo a `main`.

## Resumen

| Alcance | Repos | Medidos |
|---|---:|---:|
| Maven (`*-drake`, `Drakes*`, `DiosesDrakes`, `ArcanaDrakes`) | 61 | 23 |
| Gradle | 9 | 9 |
| Sin código fuente en el repo | 28 | 28 |
| **Total** | **97** | **60** |

## Tabla

| repo | build | 1.21.11 compila | 26.x compila | tests | bloqueo / nota |
|---|---|---|---|---|---|
| AdvancedTech-drake | maven | ✅ sí | ✅ sí | sin tests | sin bloqueo; medido 2026-10-06 en el VPS (`AdvancedTech-drake-jdk21.log` y `-jdk25.log`: `clean package`, 26.x con Paper 26.2/Java 25). `port-26x` `1c54445` migra al Slimefun universal y **arranca** en staging 26.2 (ticket #95: `Done` 104.842 s, 554 + 276 ítems de 8 addons; ver `TEMPORADA2_STAGING.md`) |
| AlchimiaVitae-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| ArcanaDrakes | maven | ✅ sí | ✅ sí | ✅ ok | sin bloqueo (paper.version parametrizado y shade 3.6.2 para clases Java 25 en c5c5f65) |
| BentoBox-Drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| BreweryX-Drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| ChestTerminal-drake | maven | ✅ sí | ✅ sí | ⚠️ indeterminado | sin bloqueo; 26.x re-medido con `clean` el 2026-10-04 (bytecode 69) |
| ColoredEnderChests-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| CompressionCraft-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| CrystamaeHistoria-drake | maven | ✅ sí | ✅ sí | ✅ ok | sin bloqueo (deps corregidas en 012c8d1) |
| DankTech2-Drake | maven | ✅ sí | ✅ sí | sin tests | 2026-10-03 `1a33d22`: paper-api `${paper.version}`, Lombok en annotationProcessorPaths (JDK 25), Particle.DUST/EntityType.ITEM; solo compila, sin arranque en staging |
| DiosesDrakes | maven | ✅ sí | ✅ sí | ✅ ok | sin bloqueo (DrakesBosses en maven.drakescraft.cl; paper.version parametrizado en e952e05) |
| Drakes-Suites | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| DrakesBosses | maven | ✅ sí | ✅ sí | ✅ ok | sin bloqueo; 26.x re-medido con `clean` el 2026-10-04 (bytecode 69) |
| DrakesCore | maven | — archivado | — archivado | — | repo archivado en GitHub (solo lectura); sustituido por Drakes-Suites y Odysseia, se omite |
| DrakesCrates | maven | ✅ sí | ✅ sí | ✅ ok (3/3 JDK 21 y JDK 25) | sin bloqueo (paper.version parametrizado, Material.CHAIN→IRON_CHAIN y test sin registro de ítems en 536ecc4); solo compila, no arrancado en staging 26.x |
| DrakesLabPresence-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| DrakesMotd | maven | ✅ sí | ✅ sí | sin tests | sin bloqueo (paper.version parametrizado en 4b2c0a6) |
| DrakesNanotech | maven | ✅ sí | ✅ sí (rama `port-26x`, PR #1) | ✅ ok (7/7 en 21 y 25) | 2026-10-03: `paper.version` parametrizada + `jsr305` provided (paper-api 26.2 ya no trae `@Nonnull`). Compila; sin prueba de ejecución en staging. |
| DrakesRanks | maven | ✅ sí | ✅ sí | sin tests | sin bloqueo (paper.version parametrizado en c718cfc); solo compila, no arrancado en staging 26.x |
| DrakesRankup | maven | ✅ sí | ✅ sí | ✅ ok | sin bloqueo; 26.x re-medido con `clean` el 2026-10-04 (bytecode 69, árbol con cambios locales de #21) |
| DrakesSlimeMarket | maven | ✅ sí | ✅ sí | ✅ ok (19/19 en 21 y 25) | 2026-10-04 `3660685`: `paper.version` parametrizada (antes fija; el 26.x previo no era válido). JDK 25 `clean package` → bytecode 69. Solo compila; sin arranque en staging |
| DrakesTab | maven | ✅ sí | ✅ sí | sin tests | sin bloqueo (paper.version parametrizado en f34e343) |
| DrakesTech | maven | ✅ sí | ✅ sí | sin tests | sin bloqueo |
| DrakesTranslate | maven | ✅ sí | ✅ sí | sin tests | d2ac01b: compila JDK 21/Paper 1.21.11 y JDK 25/Paper 26.2 (bytecode 69); no arrancado aún en staging |
| DrakesVIPPlusPlus | maven | ✅ sí | ✅ sí | sin tests | 2026-10-05 `7e66cba`: JSR-305 provided para Paper 26.2. Compila en JDK 21 y JDK 25; **corre** en staging Paper 26.2 build 129/Java 25 y alcanza `Done` (121.417 s), con DrakesVIP++ habilitado y 15 tiers cargados. |
| DrakesWorlds | maven | ✅ sí | ✅ sí | sin tests | sin bloqueo (Biome como registro + jsr305; corregido en 003529d; carga y genera mundo en staging 26.2) |
| DyeBench-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| DyedBackpacks-drake | maven | ⏳ pendiente | ✅ sí | sin tests | `port-26x` `371b062`: JDK 25/Paper 26.2 `clean test package`, bytecode 69. **Corre** en staging Paper 26.2 build 129/Java 25: habilitado junto al núcleo Slimefun universal y servidor `Done` (115.540 s); no se midió 1.21.11 en esta pasada. |
| DynaTech-drake | maven | ✅ sí | ❌ no | sin tests | 2026-10-07: `port-26x` `f85a5c9` migra 87 archivos al Slimefun universal (`11.0-Universal-26.x-SNAPSHOT`) pero NO compila en JDK 25 (BUILD FAILURE, 12 errores): ExoticGarden/Gastronomicon/ExtraUtils/InfinityExpansion solo existen como artefactos propietarios antiguos y sus clases no encajan con el ABI `io.github.thebusybiscuit`; hay que portar esas 4 dependencias a universal primero. 1.21.11 ✅ heredado de `main` (2026-10-03, `f0fb4e0`). Solo compila; sin arranque en staging. |
| EMCTech-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| ElectricSpawners-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| EssentialsX-Drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| ExcellentEnchants-Drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| ExoticGarden-drake | maven | ✅ sí | ✅ sí | ✅ ok | sin bloqueo; 26.x re-medido con `clean` el 2026-10-04 contra Paper 26.2 (bytecode 65: el pom fija source/target 21) |
| ExtraGear-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| ExtraHeads-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| FlowerPower-drake | maven | ✅ sí | ✅ sí | sin tests | 2026-10-06 CLT: `port-26x` `65d140a` migra al Slimefun universal y empaqueta `drakes-labs-autoupdate` (antes no iba en el jar); build JDK 25 sin avisos, major 69; **corre** en staging 26.2 (habilita, `sf versions` 11→12). El jar de `main` (1.21.11) sigue sin empaquetar el actualizador |
| FluffyMachines-drake | maven | ✅ sí | ✅ sí | ✅ ok | sin bloqueo (main no compilaba: Lombok duplicaba constructor; corregido en ce841f7) |
| FoxyMachines-drake | maven | ✅ sí | ✅ sí | ✅ ok | sin bloqueo (26.x en rama port-26x commit 7139fb5) |
| Galactifun2-drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| Galaxyfun-drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| Gastronomicon-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| GeneticChickengineering-Reborn-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| Geyser-Slimefun-Heads-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| HeadLimiter-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| HotbarPets-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| InfernalExpansion | maven | ⏳ pendiente | ✅ sí | sin tests | 26.x medido 2026-10-06 en el VPS (build_seguro JDK 25, Paper 26.2 build 129, major 69). `port-26x` `7bbdb0c` migra al Slimefun universal y **arranca** en staging 26.2 (ticket #98). 1.21.11 (main) sin medir en esta pasada |
| InfinityExpansion-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| InfinityLib-Drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| InvSwitcher-Drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| Inventory-Rollback-Plus-Drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| KinematicCore-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| LevelledMobs-Drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| Liquid-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| LiteXpansion-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| Magic-8-Ball-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| MapJammers-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| MiniBlocks-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| MultiverseNets | maven | ✅ sí (hotfix `441e2fe` sobre v5.0) | ⚠️ no medido (JDK 25) | ✅ ok (267 pruebas JDK 21) | El JAR 5.0 del hotfix **corre** en staging Paper 26.2 build 129/Java 25: habilita, detecta Slimefun y registra 46 recetas; no equivale aún a compilar la rama 26.x. |
| MissileWarfare-drake | maven | ⏳ pendiente | ✅ sí | sin tests | 26.x medido 2026-10-06 en el VPS (build_seguro JDK 25, `clean test package`, major 69). `port-26x` `c49c23a` migra al Slimefun universal y **arranca** en staging 26.2 (addons 7→8, ticket #96). 1.21.11 (main) sin medir en esta pasada |
| MobCapturer-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| MoreResearches-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| NetworksV6-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| Odysseia | maven | ✅ sí | ✅ sí (`port-26x` `9004d68`) | ✅ 333/333 en JDK 21 y JDK 25 | **corre** en staging Paper 26.2 build 129/Java 25 (2026-10-03): habilita correctamente y alcanza `Done` en 91.112 s; API Slimefun universal validada sin fallos de `SlimefunGuideMode` ni `SlimefunItem`. |
| PlayerVaultZ-Drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| PotionExpansion-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| ProtectionStones-Drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| Pylon-Drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| Quaptics-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| Rebar-Drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| RelicsOfCthonia-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| RykenSlimeCustomizer-EN-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| S-PlayerWarps-Drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| SFCalc-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| SFMobDrops-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| SMG-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| SaneCrafting-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| SensibleToolbox-drake | maven | ✅ sí (main `1e7e345`, ticket #4) | ✅ sí (rama `port-26x` `e09c7a7`, core universal) | ✅ 86/86 en JDK 25 perfil mc-26.2 | **corre** en staging Paper 26.2 build 129 (2026-10-03 00:16 CLT): habilita sin excepciones con Slimefun universal; antes fallaba por `ClassNotFoundException` del wrapper propietario |
| SfBetterChests-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| SfChunkInfo-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| Simple-Storage-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| SimpleUtils-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| SlimeChem-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| SlimeFrame-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| SlimeHUD-drake | maven | ✅ sí | ✅ sí (rama `port-26x` f23b2c0: Lombok en annotationProcessorPaths) | sin tests | **No corre** en staging Paper 26.2: `NoClassDefFoundError` `com/github/drakescraft_labs/slimefun4/api/SlimefunAddon` (core universal usa `io.github.thebusybiscuit`). En 26.x la función ya vive como módulo `slimehud` de DrakesUtility, que sí carga. |
| SlimeTinker-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| Slimefun-Disc-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| Slimefun4-Drake | maven | ⏳ pendiente | ✅ sí | ❌ fallan | Rama `feat/universal-slimefun-abi` a08023b2: JAR universal compila y carga en staging Paper 26.2; MockBukkit falla al inicializar `org.bukkit.Registry` en Java 25. |
| SlimefunWarfare-Drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| SlimyRepair-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| SlimyTreeTaps-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| SmallSpace-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| SoulJars-drake | maven | ✅ sí | ✅ sí (rama `port-26x`, PR #1) | sin tests | 2026-10-03: `port-26x` migra imports al Slimefun universal (`11.0-Universal-26.x-SNAPSHOT`). **Corre** en staging Paper 26.2: habilita sin excepciones y aparece en `/sf versions`. |
| SoundMuffler-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| SpiritsUnchained-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| Supreme-Drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| TranscEndence-drake | maven | ⏳ pendiente | ✅ sí | ✅ 3/3 | 2026-10-07 CLT: `port-26x` `1be9348` migra al Slimefun universal y fija maven-compiler-plugin 3.14.0 (release explícito); build JDK 25 major 69, `DaxiWorldPolicyTest` 3/3; **corre** en staging 26.2 (habilita, `sf versions` 13 addons, `/te` responde). 1.21.11 (`main`) no medido en esta pasada |
| VillagerTrade-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| VillagerUtil-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| Wildernether-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| WorldEditSlimefun-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| WorldwideChat-Drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| luckyblocks-sf-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |

## Fuente de las mediciones

* CSV crudo: `~/ai-hub/log/ports/ports_status_raw.csv` (repo | jdk21 | tests | jdk26 | bloqueo | fecha UTC).
* Logs completos por repo: `~/ai-hub/log/ports/<repo>-jdk21.log` y `-jdk25.log`.
* Script: `~/ai-hub/scripts/check_ports.sh <repo>` o `--batch <raiz> <regex>`.

## Pendiente evidente

* Repos Gradle: medir con su `gradlew` (no hay Gradle global en el VPS).
* `Drakes-Suites`: reactor de 9 módulos, se mide aparte (ver `ECOSYSTEM_STATUS_2026-10-02.md` §4).
* Los resultados que dicen **corre** incluyen evidencia de ejecución en staging; el resto solo certifica compilación. El staging 26.x ya está reconstruido y se sigue completando por módulos.
