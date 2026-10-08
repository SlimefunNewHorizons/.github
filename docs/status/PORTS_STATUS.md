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
| Maven (`*-drake`, `Drakes*`, `DiosesDrakes`, `ArcanaDrakes`) | 61 | 24 |
| Gradle | 9 | 9 |
| Sin código fuente en el repo | 28 | 28 |
| **Total** | **97** | **61** |

## Tabla

| repo | build | 1.21.11 compila | 26.x compila | tests | bloqueo / nota |
|---|---|---|---|---|---|
| AdvancedTech-drake | maven | ✅ sí | ✅ sí | sin tests | sin bloqueo; medido 2026-10-06 en el VPS (`AdvancedTech-drake-jdk21.log` y `-jdk25.log`: `clean package`, 26.x con Paper 26.2/Java 25). `port-26x` `1c54445` migra al Slimefun universal y **arranca** en staging 26.2 (ticket #95: `Done` 104.842 s, 554 + 276 ítems de 8 addons; ver `TEMPORADA2_STAGING.md`) |
| AlchimiaVitae-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| ArcanaDrakes | maven | ✅ sí | ✅ sí | ✅ ok | sin bloqueo (paper.version parametrizado y shade 3.6.2 para clases Java 25 en c5c5f65) |
| BentoBox-Drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| Better-Nuclear-Generator-drake | maven | ⏳ pendiente | ✅ sí | sin tests | 2026-10-07 04:20 CLT: rama `port-26x` `0b63314` (universaliza 13 archivos a `io.github.thebusybiscuit.slimefun4.*`, Java 25), jar major 69, SHA-256 `820e66b7…f496`. **Corre (carga)** en staging Paper 26.2 build 129/JDK 25 como plugin `BetterReactor` 1.3.0 sin WARN/ERROR; falta smoke funcional del reactor. 1.21.11 (main) sin medir. |
| BreweryX-Drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| ChestTerminal-drake | maven | ✅ sí | ✅ sí | ⚠️ indeterminado | sin bloqueo; 26.x re-medido con `clean` el 2026-10-04 (bytecode 69) |
| ColoredEnderChests-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| CompressionCraft-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| CrystamaeHistoria-drake | maven | ✅ sí | ✅ sí | ✅ ok (1/1 JDK 25) | 2026-10-07 CLT (ticket #154): rama `port-26x` `630c2e5` migra al Slimefun universal (`io.github.thebusybiscuit`, `me.mrCookieSlime`, dough del core), InfinityLib/InfinityExpansion/ExoticGarden UNIVERSAL-26x, release 25 (bytecode major 69). NetheoPlants excluido y velo de Networks por reflexión: ambos addons solo existen contra la API propietaria. Corre en staging 26.2 (273 IDs `CRY_*`); ver `TEMPORADA2_STAGING.md`. |
| DankTech2-Drake | maven | ✅ sí | ✅ sí | sin tests | 2026-10-07 CLT: `port-26x` `3bd9f75` migra al Slimefun universal (21 archivos); build JDK 25 major 69; **corre** en staging 26.2 (habilita, `sf versions` 15 addons, sin WARN/ERROR propios). 1.21.11 (`master`) medido el 2026-10-03 `1a33d22`, sin arranque nuevo en esta pasada |
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
| DemonicExpansion | maven | ⏳ pendiente | ✅ sí | sin tests | **corre** en staging Paper 26.2 build 129/Java 25 (2026-10-07 CLT): rama `port-26x` `57c329b` migra 24 archivos al Slimefun universal (`io.github.thebusybiscuit`), release 25 (compiler 3.14.0), shade 3.6.2 y `jsr305` provided (Paper 26.2 ya no lo trae); bytecode major 69, SHA-256 `d93fc3d78d10f578ffdcb50a7630ad4dfe1e3a7280d723868c89b6daf4b5a045`. Registra 9/9 ítems `DX_*`. |
| Drugfun | maven | ⏳ pendiente | ✅ sí | sin tests | `port-26x` `45f8554`: build JDK 25/Paper 26.2 con `clean test package`, bytecode 69. **Corre** en staging Paper 26.2 build 129: habilita con Slimefun universal y servidor `Done` en 108.405 s; Dough queda relocalizado dentro del addon. 1.21.11 (`main`) no se midió en esta pasada. |
| DyeBench-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| DyedBackpacks-drake | maven | ⏳ pendiente | ✅ sí | sin tests | `port-26x` `cb288f7`: JDK 25/Paper 26.2 `clean test package`, bytecode 69. **Corre** en staging Paper 26.2 build 129/Java 25: ciclo independiente de carga, habilitación y parada limpia; `Done` en 116.280 s. JAR probado SHA-256 `cfdec50b9168f2bf5e324a18770dcf7037e40eac2256e27804e0656821e0d2ce`; no se midió 1.21.11 en esta pasada. |
| DynaTech-drake | maven | ✅ sí | ✅ sí | sin tests | 2026-10-07 CLT (ticket #114): rama `port-26x` `3ee9f3e` vincula dependencias universales `ExoticGarden-drake 1.3-UNIVERSAL-26x-SNAPSHOT` y `Gastronomicon-drake 1.21.11-Drake.1-UNIVERSAL-26x-SNAPSHOT`. Compila con éxito en JDK 25 / Paper 26.2 (101 fuentes, bytecode major 69.0), 0 referencias al core propietario. 1.21.11 ✅ heredado de `main` (`f0fb4e0`). |
| EcoPower-drake | maven | ⏳ pendiente | ✅ sí (rama `port-26x` `a58119d`) | sin tests | 2026-10-08 CLT (ticket #137 / #161): rama `port-26x` `a58119d` migra al Slimefun universal (`io.github.thebusybiscuit` y `me.mrCookieSlime`), coord `1.20.6-Universal-26.x-SNAPSHOT`, sin `dough-core` ni autoupdate J21; jar major 69, 0 refs propietarias. **Corre** en staging Paper 26.2 build 129: carga y habilita sin WARN/ERROR, 23 claves en Items.yml, DrakesGenerators activó el módulo EcoPower Clean & Sustainable Energy Grids. SHA-256 `34139689b267a5fde52b88f6dd8495adc88462290e35a2fd1922aa600b9f7d47`. Solo staging; Dallas intacto. Desbloqueó Ticket #136. |
| EMCTech-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| ElectricSpawners-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| EquivalencyTech | maven | ⏳ pendiente | ✅ sí (`port-26x` `dddf25d`) | ✅ 28/28 JDK 25 | 2026-10-07 22:06-22:09 CLT (ticket #94): `maven-compiler-plugin` 3.13.0 con `release` 25 corrige el compilador implícito que emitía Java 21; `clean test package` por `build_seguro.sh`, bytecode major 69 y SHA-256 verificado. **Corre** en staging Paper 26.2 build 129: habilita, indexa 1707 recetas EMC y completa 1165 materiales vanilla / 183 objetos Slimefun; sin ERROR/Exception propio. Dallas intacto. |
| EssentialsX-Drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| ExcellentEnchants-Drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| ExoticGarden-drake | maven | ✅ sí | ✅ sí | ✅ ok (11/11 JDK 25) | 2026-10-07 CLT (ticket #114): rama `port-26x` `9966ca4` migra 16 fuentes al Slimefun universal (`io.github.thebusybiscuit` y `me.mrCookieSlime`), release 25, Paper 26.2.build.129-stable; build JDK 25 clean test package OK (11/11 tests verdes, bytecode major 69.0); instalado en ~/.m2 como `1.3-UNIVERSAL-26x-SNAPSHOT`. |
| ExtraGear-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| ExtraHeads-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| ExtraUtils-drake | maven | ✅ sí | ✅ sí | sin tests | 2026-10-07 CLT: rama `port-26x` `f6a24ba` (+`6067bff`: coordenadas propias `1.20.6-Drake-UNIVERSAL-26x-SNAPSHOT` para no pisar el jar de main en ~/.m2) migra al Slimefun universal (io.github.thebusybiscuit y me.mrCookieSlime), release 25; compilado e instalado con JDK 25 / Paper 26.2 (bytecode major 69) para desbloquear DynaTech y FluffyMachines |
| FlowerPower-drake | maven | ✅ sí | ✅ sí | sin tests | 2026-10-06 CLT: `port-26x` `65d140a` migra al Slimefun universal y empaqueta `drakes-labs-autoupdate` (antes no iba en el jar); build JDK 25 sin avisos, major 69; **corre** en staging 26.2 (habilita, `sf versions` 11→12). El jar de `main` (1.21.11) sigue sin empaquetar el actualizador |
| FluffyMachines-drake | maven | ✅ sí | ✅ sí | ✅ ok (14/14 JDK 25) | 2026-10-07 CLT: rama `port-26x` `6c28647` migra 52 archivos al Slimefun universal (`io.github.thebusybiscuit` y `me.mrCookieSlime`), release 25, Lombok en annotationProcessorPaths; ExtraUtils-drake 1.20.6 instalado en JDK 25; build JDK 25 clean package y 14/14 tests OK (bytecode major 69) |
| FoxyMachines-drake | maven | ✅ sí | ✅ sí | ✅ ok (1/1 JDK 25) | 2026-10-07 CLT: rama `port-26x` `8f2a480` migra 52 archivos al Slimefun universal (`io.github.thebusybiscuit` y `me.mrCookieSlime`), release 25, Paper 26.2.build.129-stable; build JDK 25 clean package OK (1/1 tests verdes, bytecode major 69.0), 0 refs al core propietario; JAR instalado en staging como `FoxyMachines-drake-26x.jar` (SHA-256 `803239b9bf4d3d68d37969e01068dbaec0f9924583a68816b11c93f3c66f95ed`). 1.21.11 heredado de `main`. |
| Galactifun2-drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| Galaxyfun-drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| Gastronomicon-drake | maven | ⏳ pendiente | ✅ sí | sin tests | 2026-10-07 CLT (ticket #114): rama `port-26x` `ca80ae6` migra 46 fuentes al Slimefun universal (`io.github.thebusybiscuit` y `me.mrCookieSlime`), release 25, Lombok 1.18.46 en compiler plugin y vincula infinitylib universal y SlimeHUD universal; build JDK 25 clean package OK (bytecode major 69.0); instalado en ~/.m2 como `1.21.11-Drake.1-UNIVERSAL-26x-SNAPSHOT`. 1.21.11 no medido en esta pasada. |
| GeneticChickengineering-Reborn-drake | maven | ⏳ pendiente | ✅ sí | ✅ ok (2/2 JDK 25) | 2026-10-07 CLT: rama `port-26x` `2619542` migra 26 fuentes al Slimefun universal (`io.github.thebusybiscuit` y `me.mrCookieSlime`), release 25, shade 3.6.2, quita la relocalización a la API propietaria y cambia `Material.CHAIN` → `IRON_CHAIN`; bytecode major 69; SHA-256 `05a98f3f4494c909e95c7856879b5348a49666ce9405a48a2b4d7643b820b987`. Carga en staging 26.2 (64 pollos registrados). 1.21.11 (`main`) sin medir. |
| Geyser-Slimefun-Heads-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| HeadLimiter-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| HotbarPets-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| InfernalExpansion | maven | ⏳ pendiente | ✅ sí | sin tests | 26.x medido 2026-10-06 en el VPS (build_seguro JDK 25, Paper 26.2 build 129, major 69). `port-26x` `7bbdb0c` migra al Slimefun universal y **arranca** en staging 26.2 (ticket #98). 1.21.11 (main) sin medir en esta pasada |
| InfinityExpansion-drake | maven | ⏳ pendiente | ✅ sí | ✅ 1/1 | 2026-10-07 02:44-02:47 CLT (#111): rama `port-26x` `0c0a4e1` (main + arreglos del reactor) migra 47 fuentes al Slimefun universal y usa `infinitylib-drake 1.3.11-UNIVERSAL-26x-SNAPSHOT`; JDK 25 major 69, 0 refs propietarias. **Corre** en staging 26.2: habilita, `sf versions` 16 addons, `/infinityexpansion` responde, sin WARN/ERROR propios. |
| InfinityLib-Drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente | Fork mooy1 1.3.10 sin consumidores; los addons usan `infinitylib-drake` (clon local `DrakeInfinityLib`, `port-26x` `d587b74`, compilado JDK 25 major 69). Ese clon aún no tiene remoto (#113). |
| InvSwitcher-Drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| Inventory-Rollback-Plus-Drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| KinematicCore-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| LevelledMobs-Drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| Liquid-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| LiteXpansion-drake | maven | ⏳ pendiente | ✅ sí | ✅ ok (JDK 25) | 2026-10-07 CLT: rama `port-26x` `dd4ca3a` migra 36 archivos al Slimefun universal, sin dough-core, release 25 y ExtraUtils-drake universal sombreado (`1.20.6-Drake-UNIVERSAL-26x-SNAPSHOT`, ExtraUtils `6067bff`); JDK 25 / Paper 26.2, bytecode major 69, 0 refs propietarias; arrancado en staging Purpur 26.2 (34 recetas UU-Matter, 66/76 IDs como main). 1.21.11 sin recompilar en esta pasada |
| Magic-8-Ball-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| MapJammers-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| MiniBlocks-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| MultiverseNets | maven | ✅ sí (hotfix `441e2fe` sobre v5.0) | ⚠️ no medido (JDK 25) | ✅ ok (267 pruebas JDK 21) | El JAR 5.0 del hotfix **corre** en staging Paper 26.2 build 129/Java 25: habilita, detecta Slimefun y registra 46 recetas; no equivale aún a compilar la rama 26.x. |
| MissileWarfare-drake | maven | ⏳ pendiente | ✅ sí | sin tests | 26.x medido 2026-10-06 en el VPS (build_seguro JDK 25, `clean test package`, major 69). `port-26x` `c49c23a` migra al Slimefun universal y **arranca** en staging 26.2 (addons 7→8, ticket #96). 1.21.11 (main) sin medir en esta pasada |
| MobCapturer-drake | maven | ⏳ pendiente | ✅ sí (`port-26x` `701cc33`) | sin tests | **corre** en staging Paper 26.2 build 129/Java 25 (2026-10-07 CLT): rama `port-26x` `701cc33` migra 31 archivos al Slimefun universal (`io.github.thebusybiscuit` y `me.mrCookieSlime`), soporta AbstractCubeMob para MagmaCube/Slime en Paper 26.2, release 25 y Lombok 1.18.46 en maven-compiler-plugin 3.14.0; build JDK 25 clean package OK (major 69.0, 0 refs propietarias). Habilita correctamente en staging (`Done` 120.6s, aparece en `/sf versions` con 21 addons, 0 WARN/ERROR propios). SHA-256 `a9535bcaa6d1bde2930659a9cd42ad79aa7a369e286d5b2fff9a7b0dfcf920b2`. 1.21.11 pendiente de medición. |
| MoreResearches-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| NetworksV6-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| Odysseia | maven | ✅ sí | ✅ sí (`port-26x` `9004d68`) | ✅ 333/333 en JDK 21 y JDK 25 | **corre** en staging Paper 26.2 build 129/Java 25 (2026-10-03): habilita correctamente y alcanza `Done` en 91.112 s; API Slimefun universal validada sin fallos de `SlimefunGuideMode` ni `SlimefunItem`. |
| PlayerVaultZ-Drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| PotionExpansion-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| ProtectionStones-Drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| Pylon-Drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| Quaptics-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| Rebar-Drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| RelicsOfCthonia-drake | maven | ✅ sí | ✅ sí | sin tests | 2026-10-07 CLT (ticket #124): `main` compila con JDK 21 (major 65); rama `port-26x` `e018732` migra 48 archivos al Slimefun universal (`io.github.thebusybiscuit`, Dough del núcleo en vez de `dev.drake.dough`), compila con JDK 25 / Paper 26.2 (major 69) y CORRE en staging: habilita y registra 38 ítems `*_RELIC_*`. SHA-256 `48f00d8982b2cb0cae5aa2b8af5a8def09151a653c8805745dd9d4db9953114e` |
| RykenSlimeCustomizer-EN-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| S-PlayerWarps-Drake | gradle | n/a | ⏳ pendiente (gradle) | sin tests | gradle: medir con wrapper |
| SFCalc-drake | maven | ⏳ pendiente | ✅ sí (`port-26x` `bfa4914`) | sin tests | 2026-10-07 CLT: rama `port-26x` (`bfa4914`) migra al Slimefun universal (`io.github.thebusybiscuit.slimefun4.*`), Lombok 1.18.46 en compiler plugin 3.14.0 y `maven.compiler.release` 25. Build JDK 25 `clean package` OK con `build_seguro.sh` (bytecode major 69.0, 0 refs propietarias). Jar SHA-256 `5bb2c5ec011c3bb123c24374c0d92c175e8a6d0d2413b6e24dbf1632054709a2` desplegado en `season2-staging/plugins/SFCalc-drake-26x.jar`. 1.21.11 pendiente de medición. |
| SFMobDrops-drake | maven | ⏳ pendiente | ✅ sí | ❌ MockBukkit v1.21 no soporta 26.2 (`Material.CHAIN`) | 2026-10-07 CLT: rama `port-26x` `0edd3e2` migra al Slimefun universal (`io.github.thebusybiscuit`), compiler 3.14.0 con `release` y Lombok en `annotationProcessorPaths`; JDK 25/Paper 26.2 `clean package -DskipTests`, bytecode 69, 0 refs propietarias. **Corre** en staging 26.2 build 129: habilita, carga 3 drops, `sf versions` 20 addons, `/mobdrops` y `/mobdrops reload` responden. 1.21.11 (`main`) sin medir en esta pasada |
| SMG-drake | maven | ⏳ pendiente | ✅ sí (`port-26x` `e3d2876`) | sin tests | 2026-10-07 CLT (ticket #127): rama `port-26x` `e3d2876` migra 6 fuentes al Slimefun universal (`io.github.thebusybiscuit` y `me.mrCookieSlime`), quita `dough-core`, compiler 3.14.0 con `release` y shade con `<executions>` (antes no corría y el jar salía sin `drakes-labs-autoupdate`). Build JDK 25 major 69, 0 refs propietarias. **Corre (carga)** en staging Paper 26.2 build 129: habilita `SimpleMaterialGenerators` 1.0.0, 19/19 IDs `SMG_*` en Items.yml, sin WARN/ERROR ni choque con el SMGModule de DrakesGenerators (solo PDC). SHA-256 `7f52efe3…cf49d`. Falta smoke funcional del generador; 1.21.11 (`main`) sin medir. |
| SaneCrafting-drake | maven | ⏳ pendiente | ✅ sí (`port-26x` `63623fa`) | sin tests | 2026-10-07 08:13-08:32 CLT: build JDK 25/Paper 26.2 `clean package` con `build_seguro.sh` OK, bytecode major 69, 0 refs propietarias, `drakes-labs-autoupdate` shadeado. SHA-256 `e037db34…575f`. **Corre** en staging Paper 26.2 build 129: habilita, convierte 1300 de 1304 recetas de la mesa mejorada a la mesa normal (4 con salida sobre el stack máximo quedan solo en la mesa mejorada), sin WARN/ERROR propios y desaparece `Can't create item stack` (receta de 4 pociones). Expuso un bloqueo del hilo principal en EquivalencyTech, corregido en su `port-26x` `fbe447a` (ticket #131). 1.21.11 (`main`) sin medir; Dallas no carga SaneCrafting. |
| SensibleToolbox-drake | maven | ✅ sí (main `1e7e345`, ticket #4) | ✅ sí (rama `port-26x` `e09c7a7`, core universal) | ✅ 86/86 en JDK 25 perfil mc-26.2 | **corre** en staging Paper 26.2 build 129 (2026-10-03 00:16 CLT): habilita sin excepciones con Slimefun universal; antes fallaba por `ClassNotFoundException` del wrapper propietario |
| SfBetterChests-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| SfChunkInfo-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| Simple-Storage-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| SimpleUtils-drake | maven | ⏳ pendiente | ✅ sí | sin tests | 2026-10-07 CLT: rama `port-26x` `b807778` migra al Slimefun universal (`io.github.thebusybiscuit` y `me.mrCookieSlime`), release 25, Paper 26.2.build.129-stable, infinitylib universal (`1.3.11-UNIVERSAL-26x-SNAPSHOT`); build JDK 25 clean package OK (bytecode major 69.0), 0 refs al core propietario; JAR instalado en staging como `SimpleUtils-drake-26x.jar` (SHA-256 `aa6716c350b66df7d06bdb3c5c8b839814e078bcf2579feee253ae3c630d7d50`). 1.21.11 pendiente de medir en esta pasada. |
| SlimeChem-drake | maven | ⏳ pendiente | ✅ sí (`port-26x` `598704a`) | ✅ 8/8 (JDK 25) | 2026-10-08 CLT (ticket #159): rama `port-26x` `598704a` migra 23 fuentes al Slimefun universal (`io.github.thebusybiscuit` y `me.mrCookieSlime`), sin `dough-core`, `infinitylib-drake` `1.3.11-UNIVERSAL-26x-SNAPSHOT`, compiler 3.14.0 con release 25; jar major 69 y 0 refs propietarias. **Corre** en staging Purpur 26.2 build 129/Java 25: habilita sin WARN/ERROR, 3125 IDs en `Items.yml` (120 elementos, 2977 isótopos, 28 moléculas). Solo staging; Dallas sin cambios. |
| SlimeFrame-drake | maven | ⏳ pendiente | ✅ sí (`port-26x` `9582f2e`) | sin tests | 2026-10-07 CLT (ticket #152): rama `port-26x` `9582f2e` migra 65 fuentes (403 imports) al Slimefun universal (`io.github.thebusybiscuit` y `me.mrCookieSlime`), compiler con `<release>` y Lombok 1.18.46; build JDK 25/Paper 26.2 `clean package` OK, bytecode major 69, 0 refs propietarias. **Corre (carga)** en staging Paper 26.2 build 129/Java 25: habilita sin WARN/ERROR propios, 178 IDs `WF_*` en Items.yml, `/slimeframe` responde, aparece en `/sf versions` (32 addons). SHA-256 `00bef850…bb2a6`. Falta smoke funcional de máquinas/reliquias con jugador; 1.21.11 (`main`) sin medir. |
| SlimeHUD-drake | maven | ✅ sí | ✅ sí (rama `port-26x` `0fb3a66`) | sin tests | 2026-10-07 CLT (ticket #139): `port-26x` `82bf1ca` ya migraba al Slimefun universal (`JavaPlugin` + `SlimefunAddon` de `io.github.thebusybiscuit`, sin InfinityLib); `0fb3a66` añade guardas de nulos en `PlaceholderHook`/`/slimehud toggle`. Build JDK 25/Paper 26.2 `clean package`, bytecode 69, 0 refs propietarias. **Corre** en staging Paper 26.2 build 129: habilita, registra la expansión PAPI `slimehud`, `Done` en 135 s, sin WARN/ERROR propios; antes del parche `papi parse --null %slimehud_toggle%` lanzaba NPE. Mismo parche para 1.21.11 en PR #1 (`fix/placeholder-npe`, compila JDK 21). Convive con el módulo `slimehud` de DrakesUtility sin conflictos observados. |
| SlimeTinker-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| Slimefun-Disc-drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| Slimefun4-Drake | maven | ⏳ pendiente | ✅ sí | ❌ fallan | Rama `feat/universal-slimefun-abi` a08023b2: JAR universal compila y carga en staging Paper 26.2; MockBukkit falla al inicializar `org.bukkit.Registry` en Java 25. |
| SlimefunWarfare-Drake | maven | ⏳ pendiente | ⏳ pendiente | ⏳ pendiente |  |
| SlimyRepair-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| SlimyTreeTaps-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| SlimyBees | maven | ⏳ pendiente | ✅ sí (`port-26x` `0bab82e`) | ⚠️ no ejecutados (MockBukkit-v1.18 no soporta 26.2) | 2026-10-07 21:13-21:19 CLT (ticket #166): rama `port-26x` migra 52 clases al Slimefun universal (`io.github.thebusybiscuit` y `me.mrCookieSlime`), `slimefun-core 11.0-Universal-26.x-SNAPSHOT`, compiler 3.14.0 con `release`, shade 3.6.2; `build_seguro.sh` JDK 25/Paper 26.2 `clean package -DskipTests`, bytecode 69, 0 refs propietarias. **Corre** en staging Paper 26.2 build 129: habilita, registra 26 especies y 18/18 IDs literales en Items.yml; `/sb help` responde por consola. SHA-256 `cb6cd07af69d1209be62a61618edf216f80efcc6b8ebdd7f0318b0a4fac557ee`. 1.21.11 (`main`) sin medir; Dallas sin cambios. |
| SmallSpace-drake | maven | ⏳ pendiente | ✅ sí (certif. #125 / #164) | — sin tests | 2026-10-07/08 CLT (ticket #125 / #164): rama `port-26x` `9edaf4f` migra 11 fuentes al Slimefun universal (`io.github.thebusybiscuit` y `me.mrCookieSlime`), compiler 3.14.0 con release 25 (major 69) y shade 3.6.2. Certificación QA independiente por antigravity2: 0 refs propietarias, bytecode major 69 verificado, 0 secretos, SHA-256 `a2cdb8ab25ae6940a2e9cb2d11c261fa1f9217ef21af52d30dc1d31ca3bf2f14`. **Corre** en staging 26.2 build 129: habilita limpio, registra 10 ítems, DrakesUtility activa módulo SmallSpace y `/smallspace` responde (fix AIOOBE en `3b1860d` / PR #1). 1.21.11 (`main`) sin medir. |
| SoulJars-drake | maven | ✅ sí | ✅ sí (rama `port-26x`, PR #1) | sin tests | 2026-10-03: `port-26x` migra imports al Slimefun universal (`11.0-Universal-26.x-SNAPSHOT`). **Corre** en staging Paper 26.2: habilita sin excepciones y aparece en `/sf versions`. |
| SoundMuffler-drake | maven | ⏳ pendiente | ✅ sí | sin tests | 2026-10-07 CLT (ticket #116): rama `port-26x` `b9c5c9e` migra 3 fuentes al Slimefun universal (`io.github.thebusybiscuit` y `me.mrCookieSlime`) y fija `<release>` en el compiler plugin; build JDK 25/Paper 26.2 `clean test package`, bytecode 69. **Corre** en staging Paper 26.2 build 129/Java 25: `Done` en 126.707 s, habilita y aparece en `/sf versions`, sin WARN/ERROR propios. JAR probado SHA-256 `9a0926df2b6fb1410bb3b5b2907ce3a78a50d6303da9b70047084e5478f422ad`. Ojo: el módulo `soundmuffler` de DrakesUtility empareja el mismo ID `SOUND_MUFFLER` por PDC; si conviven ambos, un muffler colocado abre también la GUI del módulo. 1.21.11 no medido en esta pasada. |
| SpiritsUnchained-drake | sin-codigo | n/a (sin fuente) | n/a (sin fuente) | n/a | sin codigo fuente en el repo (solo README/docs) |
| Supreme-Drake | maven | ✅ sí | ✅ sí | ✅ ok (39/39 JDK 25) | 2026-10-07 CLT (ticket #123): rama `port-26x` `0f51137` migra 71 archivos al Slimefun universal (`io.github.thebusybiscuit` y `me.mrCookieSlime`), infinitylib `1.3.11-UNIVERSAL-26x-SNAPSHOT`, compiler 3.14.0 con release 25 (major 69). **Corre** en staging 26.2: habilita sin excepciones y registra 509 ítems `SUPREME_*`. |
| TranscEndence-drake | maven | ⏳ pendiente | ✅ sí (rama `port-26x` `1be9348`) | ✅ 3/3 (JDK 25) | 2026-10-08 CLT (ticket #109 / #160): rama `port-26x` `1be9348` migra al Slimefun universal y fija maven-compiler-plugin 3.14.0 (release explícito 25); build JDK 25 major 69, 0 refs drakescraft_labs/slimefun4, `DaxiWorldPolicyTest` 3/3; **corre** en staging Paper 26.2 build 129/Java 25: habilita limpio sin excepciones ni advertencias, `sf versions` lo reporta activo, DrakesMagic habilita TranscEndence Dimensional Arcana y `/te` responde. SHA-256 staging `1e66ac312a8abb9deb5a886e105367c0ff0678e66cfa41950b6d3f4b20842795`. 1.21.11 (`main`) no medido en esta pasada. |
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
