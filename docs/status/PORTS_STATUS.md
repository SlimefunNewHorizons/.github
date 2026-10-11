# Ports status — 1.21.11 y 26.x (medición en el VPS)

> Generado por `~/ai-hub/scripts/gen_ports_status.sh` el 2026-10-11 desde `~/ai-hub/log/ports/ports_status_raw.csv`.
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

* El build 26.x lleva `clean`: sin él, el compilador incremental reutiliza las clases del build JDK 21 («Nothing to compile») y el resultado no prueba nada. `check_ports.sh` marca `NO_MEDIDO` si no recompiló.
* Siempre vía `build_seguro.sh` (un solo build a la vez en todo el VPS, `nice`/`ionice`, espera si la carga ≥ 5). Máximo ~450 s de presupuesto por pasada.
* `indeterminado` = el build falló sin llegar a compilar (p. ej. no resolvió dependencias): **no es un no-compila**, hay que repetirlo.
* Los cambios propios de 26.x van a la rama `port-26x` de cada repo, nunca directo a `main`.

## Resumen

| Alcance | Repos | Medidos |
|---|---:|---:|
| Maven (`*-drake`, `Drakes*`, `DiosesDrakes`, `ArcanaDrakes`) | 70 | 49 |
| Gradle | 9 | 9 |
| Sin código fuente en el repo | 28 | 28 |
| **Total** | **107** | **86** |

## Tabla

| repo | build | 1.21.11 compila | 26.x compila | tests | bloqueo / nota |
|---|---|---|---|---|---|
| AdvancedTech-drake | maven | ✅ sí | ✅ sí | sin tests | sin bloqueo |
| AlchimiaVitae-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| ArcanaDrakes | maven | ✅ sí | ✅ sí | ✅ ok | sin bloqueo (paper.version parametrizado y shade 3.6.2 para clases Java 25 en c5c5f65) |
| BentoBox-Drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| Better-Nuclear-Generator-drake | maven | ⚠️ indeterminado (dependencias) | ✅ sí | sin tests | Failed to execute goal org.apache.maven.plugins:maven-compiler-plugin:3.13.0:compile (default-compile) on project BetterNuclearReactor-drake |
| BreweryX-Drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| ChestTerminal-drake | maven | ✅ sí | ✅ sí | ⚠️ indeterminado | sin bloqueo |
| ColoredEnderChests-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| CompressionCraft-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| Coronalis-drake | maven | ✅ sí | ✅ sí | sin tests | sin bloqueo |
| CrystamaeHistoria-drake | maven | ✅ sí | ✅ sí | ✅ ok | sin bloqueo (deps corregidas en 012c8d1) |
| DankTech2-Drake | maven | ✅ sí | ✅ sí | sin tests | 2026-10-11 21:14 UTC: port-26x `3bd9f75` `clean package` con build_seguro JDK 25 y `-Dpaper.version=26.2.build.129-stable -Djava.version=25`, bytecode major 69 (jar 163 KB, 118 clases), compila contra Slimefun universal `11.0-Universal-26.x-SNAPSHOT`. Corre en staging 26.2 el 2026-10-07 (ver TEMPORADA2_STAGING.md) |
| DiosesDrakes | maven | ✅ sí | ✅ sí | ✅ ok | sin bloqueo (DrakesBosses en maven.drakescraft.cl; paper.version parametrizado en e952e05) |
| Drakes-Suites | maven | ❌ no | ✅ sí | sin tests | Failed to execute goal org.apache.maven.plugins:maven-jar-plugin:2.4:jar (default-jar) on project drakes-core: Error assembling JAR: /home/j (1.21.11 en main; 26.x en 26.x) |
| DrakesBosses | maven | ✅ sí | ✅ sí | ✅ ok | sin bloqueo |
| DrakesCore | maven | n/a | n/a | sin tests | repo archivado en GitHub (solo lectura; sustituido por Drakes-Suites y Odysseia) |
| DrakesCrates | maven | ✅ sí | ✅ sí | ✅ 3 (0 fallos) | 2026-10-11 12:20 CLT: main 0710c12 `clean test package` con build_seguro JDK 25 y `-Dpaper.version=26.2.build.129-stable`, bytecode major 69, jar SHA 3041032e. **Arranca** en staging Paper 26.2-133/Java 25: Done 149,9 s, se engancha al Slimefun universal (`io.github.thebusybiscuit`), 3 crates + 3 llaves, PAPI `drakescrates` registrado; `/drakescrates reload` y `/oraculo reload` por consola sin WARN/ERROR propios. Sin jugadores: no se probó apertura de crates ni Votifier (ausente en staging). |
| DrakesLabPresence-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| DrakesMotd | maven | ✅ sí | ✅ sí | sin tests | sin bloqueo (paper.version parametrizado en 4b2c0a6) |
| DrakesNanotech | maven | ✅ sí | ✅ sí | ✅ ok | 2026-10-11 18:43 CLT: port-26x 34c77e6 `clean package` con build_seguro JDK 25 y `-Dpaper.version=26.2.build.129-stable`, bytecode major 69 (jar 0.4.0, 107 KB). El jar standalone **no se instala** en staging: su contenido corre absorbido como `NanotechModule` de DrakesTech (Drakes-Suites `26.x`), que arranca en staging 26.2 con 158 ítems, 15 máquinas y 8 multibloques. Instalar ambos duplicaría IDs. 2026-10-11 21:17 UTC: port-26x `bbdcc92` ya compila contra el core universal `11.0-Universal-26.x-SNAPSHOT` (imports remapeados), tests 7/7, 0 referencias a `com/github/drakescraft_labs` en el jar. |
| DrakesRanks | maven | ✅ sí | ✅ sí | sin tests | sin bloqueo (paper.version parametrizado en c718cfc) |
| DrakesRankup | maven | ✅ sí | ✅ sí | ✅ ok | sin bloqueo |
| DrakesSlimeMarket | maven | ✅ sí | ✅ sí | ✅ ok | 2026-10-04 `3660685`: `paper.version` parametrizada (antes fija; el 26.x previo no era válido). JDK 25 `clean package` → bytecode 69. Solo compila; sin arranque en staging |
| DrakesTab | maven | ✅ sí | ✅ sí | sin tests | sin bloqueo (paper.version parametrizado en f34e343) |
| DrakesTech | maven | ✅ sí | ✅ sí | sin tests | sin bloqueo |
| DrakesTranslate | maven | ✅ sí | ✅ sí | sin tests | d2ac01b: compila JDK 21/Paper 1.21.11 y JDK 25/Paper 26.2 (bytecode 69); no arrancado aún en staging |
| DrakesVIPPlusPlus | maven | ✅ sí | ✅ sí | sin tests | 2026-10-05 `7e66cba`: JSR-305 provided para Paper 26.2. Compila en JDK 21 y JDK 25; **corre** en staging Paper 26.2 build 129/Java 25 y alcanza `Done` (121.417 s); con DrakesVIP++ habilitado y 15 tiers cargados. |
| DrakesWorlds | maven | ✅ sí | ✅ sí | sin tests | sin bloqueo (Biome como registro + jsr305; corregido en 003529d; carga y genera mundo en staging 26.2) |
| DyeBench-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| DyedBackpacks-drake | maven | ⏳ pendiente | ✅ sí | sin tests | `port-26x` `371b062`: JDK 25/Paper 26.2 `clean test package`; bytecode 69. **Corre** en staging Paper 26.2 build 129/Java 25: habilitado junto al núcleo Slimefun universal y servidor `Done` (115.540 s); no se midió 1.21.11 en esta pasada. |
| DynaTech-drake | maven | ⏳ pendiente | ✅ sí | sin tests | 2026-10-11: port-26x 47f1cb9 cablea deps universales (ExtraUtils/ExoticGarden/Gastronomicon/InfinityExpansion/InfinityLib); BUILD SUCCESS JDK25 con flags 26.2.build.129 en log 2026-10-07 + bytecode major 69 verificado en target/ (SHA 930ec9b8); 0 refs propietarias y 86 ficheros al ABI io.github.thebusybiscuit; sin tests declarados. 1.21.11 pendiente de re-medicion (ultimo log 2026-10-02 FAILURE con pom antiguo). 2026-10-11 (#279): rebuild 47f1cb9 JDK25 SHA 6e210b16; arranque real en staging 26.2 Done 182 s, Enabling sin excepciones, 120 IDs DYNATECH_* registrados (carga, sin smoke funcional: NO portado) |
| EMCTech-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| EcoPower-drake | maven | ✅ sí | ✅ sí | sin tests | sin bloqueo |
| ElectricSpawners-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| Element-Manipulation-drake | maven | ✅ sí | ✅ sí | sin tests | sin bloqueo |
| EssentialsX-Drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| ExcellentEnchants-Drake | maven | ❌ no | ⚠️ indeterminado (dependencias) | sin tests | Failed to execute goal on project MC_1_21_8: Could not resolve dependencies for project su.nightexpress.excellentenchants:MC_1_21_8:jar:5.4. |
| ExoticGarden-drake | maven | ✅ sí | ✅ sí | ✅ ok | sin bloqueo |
| ExtraGear-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| ExtraHeads-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| ExtraTools-drake | maven | ✅ sí | ✅ sí | sin tests | port-26x abb04c9: desacoplar API Slimefun propietaria hacia núcleo universal 26.x; bytecode major 69; verificado y habilitado en staging Paper 26.2 (Done 150s) |
| ExtraUtils-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| FN-FAL-s-Amplifications-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| FlowerPower-drake | maven | ✅ sí | ✅ sí | sin tests | sin bloqueo |
| FluffyMachines-drake | maven | ✅ sí | ✅ sí | ✅ ok | sin bloqueo (main no compilaba: Lombok duplicaba constructor; corregido en ce841f7) |
| FoxyMachines-drake | maven | ✅ sí | ✅ sí | ✅ ok | sin bloqueo (26.x en rama port-26x commit 7139fb5) |
| Galactifun2-drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| Galaxyfun-drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| Gastronomicon-drake | maven | ✅ sí (rama fix/dynatech-growth-chamber-ids, 2026-10-11) | ✅ sí | sin tests ejecutados (surefire 2.12.4) | 2026-10-11 (#279): port-26x 4b686b0 corrige los IDs de las Growth Chambers de DynaTech; JDK25 BUILD SUCCESS, major 69; arranque real en staging 26.2 sin WARN de integracion (carga). 1.21.11: JDK21 BUILD SUCCESS en PR borrador #1 |
| GeneticChickengineering-Reborn-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| Geyser-Slimefun-Heads-drake | maven | ✅ sí | ✅ sí | sin tests | port-26x cc623cb: 2 imports a Slimefun universal |
| HeadLimiter-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| HotbarPets-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| InfinityExpansion-drake | maven | ❌ `main` `a80a5c4` no / ✅ PR borrador #2 | ✅ sí (`port-26x`, #111) | ✅ 1/1 (JDK 21) | 2026-10-11 CLT: `main` `a80a5c4` **no compila** con JDK 21 en limpio: el pom no declara `maven-compiler-plugin`, Maven usa 3.1 con source/target 5 (`Source option 5 is no longer supported`). La rama `fix/reactor-radiacion-main` (`c12e4a1`, PR borrador #2) lleva encima de `main` el arreglo de #90 (radiación del InfinityReactor en el hilo principal) y el compiler plugin con release 21: BUILD SUCCESS, `InfinityReactorTest` 1/1, major 65. Dallas corre una compilación sin Laser Excavator (comprobado en solo lectura); el hotfix de producción es el artefacto `0462229` de #90. 26.x: `port-26x` compila con JDK 25 y corre en staging 26.2 (#111). |
| InfinityLib-Drake | maven | ⏳ pendiente | ✅ sí | ✅ 65 (0 fallos, 3 omitidos) | 2026-10-11: port-26x 950276f (sobre aa5c297 ABI io.github.thebusybiscuit) BUILD SUCCESS con build_seguro.sh JDK25, bytecode major 69; tests adaptados a mockbukkit-v26.2 4.116.1 (constructor de pruebas sin loader). 1.21.11 pendiente de re-medicion. Sin arranque en staging: compila, NO portado. Nota: los addons usan infinitylib-drake (DrakeInfinityLib), no este repo |
| InvSwitcher-Drake | maven | ✅ sí | ✅ sí | ✅ ok | 2026-10-11 11:45 CLT: `port-26x` `858247d` recompilado con `build_seguro.sh 25` (`clean package`, 133 tests en verde, bytecode 69). **Corre** en staging Paper 26.2 build 133/Java 25 como addon de BentoBox 3.22.4: carga, habilita y engancha `world`/`world_nether`/`world_the_end` sin WARN; el contenido del JAR de staging es idéntico al recompilado (`diff -r` vacío). Solo se probó arranque: el cambio de inventario entre mundos no se ejercitó (no hay jugadores en staging ni otros mundos de modalidad cargados). |
| Inventory-Rollback-Plus-Drake | maven | ✅ sí | ✅ sí | ✅ ok | sin bloqueo (1.21.11 en main; 26.x en port-26x) |
| KinematicCore-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| LevelledMobs-Drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| Liquid-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| LiteXpansion-drake | maven | ⏳ pendiente | ✅ sí | ✅ ok | 2026-10-07 CLT: rama port-26x dd4ca3a migra 36 archivos al Slimefun universal sin dough-core release 25 y ExtraUtils-drake universal sombreado (1.20.6-Drake-UNIVERSAL-26x-SNAPSHOT ExtraUtils 6067bff); JDK 25 / Paper 26.2 bytecode major 69 0 refs propietarias; arrancado en staging Purpur 26.2 (34 recetas UU-Matter 66/76 IDs como main). 1.21.11 sin recompilar en esta pasada |
| Magic-8-Ball-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| MapJammers-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| MiniBlocks-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| MissileWarfare-drake | maven | ⏳ pendiente | ✅ sí | sin tests | 26.x medido 2026-10-06 en el VPS (build_seguro JDK 25; `clean test package`; major 69). `port-26x` `c49c23a` migra al Slimefun universal y **arranca** en staging 26.2 (addons 7→8; ticket #96). 1.21.11 (main) sin medir en esta pasada |
| MobCapturer-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| MoreResearches-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| NetworksV6-drake | maven | ❌ no | ✅ sí | ❌ fallan | Tests run: 13; Failures: 0; Errors: 13; Skipped: 0; Time elapsed: 0.782 s <<< FAILURE! -- in io.github.sefiraat.networks.slimefun.network.Ne |
| PlayerVaultZ-Drake | maven | ⚠️ indeterminado (dependencias) | ⚠️ indeterminado (dependencias) | sin tests | 2026-10-11 CLT: no es un fallo de compilación. El parche se compila contra el binario cerrado `vendor/PlayerVaultZ-1.1.0.jar` (dependencia `system`, sin licencia pública, no versionado) y ese JAR no existe en Star. Para medir hay que obtenerlo y validar el SHA-256 indicado en el README; además, es un binario de 1.21 sin fuente, por lo que «compila» en 26.x no implicaría que el plugin original corra en 26.2. |
| PotionExpansion-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| ProtectionStones-Drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| Pylon-Drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| Quaptics-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| Rebar-Drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| RelicsOfCthonia-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| RykenSlimeCustomizer-EN-drake | maven | ✅ sí | ✅ sí | sin tests | sin bloqueo (1.21.11 en main; 26.x en port-26x) |
| S-PlayerWarps-Drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| SFCalc-drake | maven | ❌ no | ✅ sí | sin tests | COMPILATION ERROR :  |
| SFMobDrops-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| SMG-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| SaneCrafting-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| SensibleToolbox-drake | maven | ✅ sí | ✅ sí | ✅ ok | **corre** en staging Paper 26.2 build 129 (2026-10-03 00:16 CLT): habilita sin excepciones con Slimefun universal; antes fallaba por `ClassNotFoundException` del wrapper propietario |
| SfBetterChests-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| SfChunkInfo-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| Simple-Storage-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| SimpleUtils-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| SlimeChem-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| SlimeFrame-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| SlimeHUD-drake | maven | ✅ sí | ✅ sí | sin tests | **No corre** en staging Paper 26.2: `NoClassDefFoundError` `com/github/drakescraft_labs/slimefun4/api/SlimefunAddon` (core universal usa `io.github.thebusybiscuit`). En 26.x la función ya vive como módulo `slimehud` de DrakesUtility; que sí carga. |
| SlimeTinker-drake | maven | ✅ sí | ✅ sí | sin tests | 2026-10-08 rama fix/attribute-max-health-1211 d9e6af6 (Attribute.MAX_HEALTH para 1.21.11); jdk21 BUILD SUCCESS sin tests; jdk25 clean package release 25 BUILD SUCCESS 107 fuentes recompiladas y bytecode major 69 verificado en target/; paper.version parametrizada. Solo compila; sin arranque en staging 26.x |
| Slimefun-Disc-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| Slimefun4-Drake | maven | ⏳ pendiente | ✅ sí | ❌ fallan | Rama `feat/universal-slimefun-abi` a08023b2: JAR universal compila y carga en staging Paper 26.2; MockBukkit falla al inicializar `org.bukkit.Registry` en Java 25. |
| SlimefunWarfare-Drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| SlimyRepair-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| SlimyTreeTaps-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| SmallSpace-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| SoulJars-drake | maven | ✅ sí | ✅ sí | sin tests | 2026-10-03: `port-26x` migra imports al Slimefun universal (`11.0-Universal-26.x-SNAPSHOT`). **Corre** en staging Paper 26.2: habilita sin excepciones y aparece en `/sf versions`. |
| SoundMuffler-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| SpiritsUnchained-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| Supreme-Drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| TranscEndence-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| VillagerTrade-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| VillagerUtil-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| Wildernether-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| WorldEditSlimefun-drake | maven | PENDIENTE | ✅ sí | sin tests | sin bloqueo (rama port-26x d69bc35 bytecode 69) |
| WorldwideChat-Drake | maven | ❌ no | ❌ no | ✅ ok | Failed to execute goal org.codehaus.mojo:exec-maven-plugin:3.6.3:java (default) on project WorldwideChat-bukkit-core: An exception occurred  (1.21.11 en main; 26.x en main) |
| luckyblocks-sf-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |

## Fuente de las mediciones

* CSV crudo: `~/ai-hub/log/ports/ports_status_raw.csv` (repo | jdk21 | tests | jdk26 | bloqueo | fecha UTC).
* Logs completos por repo: `~/ai-hub/log/ports/<repo>-jdk21.log` y `-jdk25.log`.
* Script: `~/ai-hub/scripts/check_ports.sh <repo>` o `--batch <raiz> <regex>`.

## Pendiente evidente

* Repos Gradle: medir con su `gradlew` (no hay Gradle global en el VPS).
* `Drakes-Suites`: reactor de 9 módulos, se mide aparte (ver `ECOSYSTEM_STATUS_2026-10-02.md` §4).
* Ningún resultado de esta tabla certifica *ejecución*; el staging 26.x sigue sin construirse.
