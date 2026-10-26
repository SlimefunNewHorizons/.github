# AuditorÃ­a Comparativa de Plugins: Dallas (1.21.11) vs Temporada 2 Staging (Paper 26.2)

> **Fecha:** 2026-10-26  
> **Alcance:** Inventario exhaustivo y auditorÃ­a de compatibilidad de los plugins activos en producciÃ³n Dallas frente a la flota de pruebas de la Temporada 2 (Paper 26.2 / Java 25).  
> **Estado:** 163 JARs en Dallas | 128 JARs en Staging | **61 Plugins de producciÃ³n faltantes en Staging**.

---

## 1. Resumen Ejecutivo de la Discrepancia

Durante la preparaciÃ³n de la Temporada 2, el esfuerzo estuvo concentrado en la **modernizaciÃ³n de Slimefun (49/49 addons verificados)** y la compilaciÃ³n de **StarSuites (9 mÃ³dulos)**. Sin embargo, al auditar los JARs fÃ­sicos de producciÃ³n en **Dallas** contra el entorno de **Staging**, se constatÃ³ que Staging carece de la mayor parte de la infraestructura de soporte, jugabilidad no-Slimefun, economÃ­a de tienda y herramientas de staff:

| MÃ©trica | Dallas (ProducciÃ³n 1.21.11) | Staging (Temporada 2 26.2) | Delta / Estado |
|:---|:---:|:---:|:---|
| **Total Archivos JAR en `/plugins`** | **163** | **128** | -35 JARs netos |
| **Plugins Coincidentes / Portados** | 96 | 96 | âœ…… Verificados en 26.2 |
| **Absorbidos en StarSuites** | 35 | 35 | âœ…… Integrados en los 8 mega-jars |
| **Plugins de Dallas NO presentes en Staging** | **61** | **0** | âš ï¸� **Faltan en Staging** |

> âš ï¸� **Impacto CrÃ­tico:** Si la Temporada 2 se desplegase en Dallas con Ãºnicamente los 128 JARs actuales de Staging, **el servidor perderÃ­a la pasarela de compras Tebex (donaciones), el crossplay con Bedrock (Geyser/Floodgate), el puente de Discord (DiscordSRV), el sistema de habilidades (AuraSkills), trabajos (Jobs), clanes (BetterTeams), tumbas (AxGraves), warps de jugadores y el tablist formateado (TAB)**.

---

## 2. Ecosistema Multiverse (Chagui68 & Mundos)

Se auditÃ³ en detalle la suite de mundos y plugins Multiverse:

| Plugin en Dallas | VersiÃ³n Dallas | Estado en Staging | Compatibilidad 26.2 / DiagnÃ³stico |
|:---|:---:|:---:|:---|
| `multiverse-core-5.8.2-pre.jar` | 5.8.2-pre | âœ…… Presente | **Compatible.** Carga mundos sin excepciones en 26.2. |
| `multiverse-netherportals-5.1.0.jar` | 5.1.0 | âœ…… Presente | **Compatible.** Vincula portales al Nether/End. |
| `MultiverseCreatures-v4.9-RELEASE.jar` | **v4.9** | âš ï¸� Tiene **v3.6** | **Desactualizado en Staging.** El repo local tiene `v4.9-RELEASE` con el fix de arenas y boss_dimension (`6f4b797`). Debe reemplazarse en Staging. |
| `MultiverseNets-v6.3.jar` | **v6.3** | âš ï¸� `drakes-multiverse.jar` | Dallas corre el JAR independiente v6.3 con Stock Crafters. Debe asegurarse que el mÃ³dulo de DrakesMultiverse contenga la versiÃ³n 6.3 completa. |
| `MultiverseProgramming-1.1.8.jar` | **1.1.8** | â�Œ **Ausente** | **Falta en Staging.** En `/home/jack/workspace/drakescraft/MultiverseProgramming` el repo estÃ¡ en `v1.2.2`. Compatible (pure Bukkit). Debe compilarse e incluirse. |
| `MultiverseTinker` | â€”” | â�Œ Pendiente | Repo en desarrollo (`v1.2.0`), aÃºn no en producciÃ³n Dallas. |

---

## 3. Matriz de los 61 Plugins de Dallas Faltantes en Staging

A continuaciÃ³n se detalla el anÃ¡lisis de compatibilidad con **Paper 26.2 / Java 25** para cada uno de los 61 plugins ausentes:

### A. MonetizaciÃ³n, Tienda y Donaciones (CRÃ�TICO P0)
| JAR en Dallas | Tipo / Origen | Compatibilidad Paper 26.2 | AcciÃ³n Requerida para Staging |
|:---|:---|:---:|:---|
| `tebex-bukkit-2.4.3-d51129a.jar` | Upstream Tebex | âœ…… **Alta** (HTTP REST polling puro, sin NMS) | Copiar directo a Staging y validar entrega con token test. |
| `UltimateShop-4.2.10.jar` | Upstream Spigot | âœ…… **Alta** (Bukkit GUI + Vault) | Copiar directo. Verificar menÃºs de compra/venta en 26.2. |
| `ExcellentCrates-6.6.1.jar` | Upstream NightExpress | âœ…… **Alta** (Depende de `NightCore`, ya presente en Staging) | Copiar a Staging. Las crates dependen de NightCore 2.16.4. |
| `VotifierPlus-1.4.3.jar` | Upstream Spigot | âœ…… **Alta** (Socket listener puro) | Copiar directo a Staging. |
| `40ServidoresMC-2.5.jar` | Votaciones ES | âœ…… **Alta** (API de votaciÃ³n estÃ¡ndar) | Copiar directo a Staging. |

---

### B. Infraestructura Crossplay Bedrock & Red (P0)
| JAR en Dallas | Tipo / Origen | Compatibilidad Paper 26.2 | AcciÃ³n Requerida para Staging |
|:---|:---|:---:|:---|
| `Geyser-Spigot.jar` | Upstream GeyserMC | âš ï¸� **Media** (Requiere build reciente para Paper 26.x) | Actualizar al Ãºltimo build de Geyser compatible con el protocolo 26.x. |
| `floodgate-spigot.jar` | Upstream GeyserMC | âš ï¸� **Media** (Protocol handshake) | Alinear con el build de Geyser para auth Bedrock. |
| `GeyserHeads-drake v1.2.jar` | Fork propio | âœ…… **Alta** (Mapeo de cabezas Slimefun) | Copiar a Staging; verificar compatibilidad con heads de 26.2. |
| `PojavDetector-1.0.0.jar` | Upstream Spigot | âœ…… **Alta** (DetecciÃ³n de handshake) | Copiar directo a Staging. |

---

### C. Comunidad, Chat y Discord (P1)
| JAR en Dallas | Tipo / Origen | Compatibilidad Paper 26.2 | AcciÃ³n Requerida para Staging |
|:---|:---|:---:|:---|
| `DiscordSRV-Build-1.30.5.jar` | Upstream | âœ…… **Alta** (AsyncPlayerChatEvent + JDA) | Copiar a Staging con token de pruebas de canal staging. |
| `InteractiveChat.jar` | Upstream | âœ…… **Media** (Usa ProtocolLib para tooltips en chat) | ProtocolLib ya corre en Staging; copiar y validar `[item]`. |
| `InteractiveChatDiscordSrvAddon-2026.1.1.0.jar` | Addon DiscordSRV | âœ…… **Alta** (Puente de menciones de Ã­tems a Discord) | Copiar a Staging junto a DiscordSRV e InteractiveChat. |
| `DrakesChatBridge.jar` | Fork propio | âœ…… **Alta** (IntercomunicaciÃ³n de canales) | Copiar a Staging. |
| `DrakesTranslate-1.0.0.jar` | Repo propio | âœ…… **Alta** (Llama a Docker `drakes-translate:5001`) | Copiar a Staging; verificar conectividad al puerto 5001. |
| `AutoMessage-2.0.0.jar` | Upstream | âœ…… **Alta** (Scheduler Bukkit simple) | Copiar directo a Staging. |
| `ChatGames-Paper-1.4.5.jar` | Upstream | âœ…… **Alta** (Eventos de chat y premios de economÃ­a) | Copiar directo a Staging. |

---

### D. Jugabilidad, RPG y ProgresiÃ³n de Usuarios (P1)
| JAR en Dallas | Tipo / Origen | Compatibilidad Paper 26.2 | AcciÃ³n Requerida para Staging |
|:---|:---|:---:|:---|
| `AuraSkills-2.4.0.jar` | Upstream Archon | âœ…… **Alta** (Java puro, Paper Adventure) | Copiar directo a Staging. Verificar persistencia de stats. |
| `BetterTeams-5.1.2.jar` | Upstream | âœ…… **Alta** (Bukkit API + Vault) | Copiar directo a Staging. |
| `Jobs-Reborn.jar` | Upstream | âœ…… **Alta** (Economy hooks) | Copiar directo a Staging. |
| `Quests.jar` | Upstream | âœ…… **Alta** (Bukkit quest listeners) | Copiar directo a Staging. |
| `GSit-3.7.0.jar` | Upstream | âœ…… **Alta** (Entity mount API) | Copiar directo a Staging. |
| `AxGraves-1.0-Drake.jar` | Repo `AxGraves-Drakes` | âœ…… **Alta** (Tiene rama `port-26x`) | Desplegar build de la rama `port-26x` en Staging. |
| `WildRTP-3.3.5.jar` | Upstream | âœ…… **Alta** (Async chunk search) | Copiar directo a Staging. |
| `S-PlayerWarps-1.1.jar` | Repo `S-PlayerWarps-Drake` | âœ…… **Alta** (Build Gradle disponible) | Copiar o construir jar en Staging. |
| `RealisticVillagers-Drake-1.21.11.jar` | Repo `RealisticVillagers` | âš ï¸� **Media** (AI goals en aldeanos) | Probar en Staging si el listener de aldeanos requiere ajuste en 26.x. |
| `MarriageMaster-2.9.2.jar` | Upstream | âœ…… **Alta** (Bukkit social) | Copiar directo a Staging. |
| `SlotMachine.jar` | Upstream | âœ…… **Alta** (GUI minigame) | Copiar directo a Staging. |
| `VanillaPatPat-1.0.1.jar` | Repo `VanillaPatPat` | âœ…… **Alta** (Interact event) | Copiar directo a Staging. |
| `RapidLeafFall-1.0.0.jar` | Upstream | âœ…… **Alta** (BlockBreak decay) | Copiar directo a Staging. |
| `Hurricane.jar` | Upstream | âœ…… **Alta** (Clima custom) | Copiar directo a Staging. |
| `BreweryX-3.7.0.jar` | Repo `BreweryX-Drake` | âœ…… **Alta** (Tiene rama activa `port-26x`) | Compilar rama `port-26x` y desplegar a Staging. |

---

### E. Staff, ModeraciÃ³n, Seguridad y AdministraciÃ³n (P1)
| JAR en Dallas | Tipo / Origen | Compatibilidad Paper 26.2 | AcciÃ³n Requerida para Staging |
|:---|:---|:---:|:---|
| `TAB-6.0.2.jar` | Upstream | âœ…… **Media/Alta** (Packet injection) | Copiar y probar si los prefijos y el score se renderizan limpios. |
| `SkinsRestorer-15.12.6.jar` | Upstream | âœ…… **Alta** (Skin property injector) | Copiar a Staging. |
| `FastAsyncWorldEdit-Paper-2.16.1.jar` | Upstream FAWE | âš ï¸� **Baja** (Hardcoded NMS a 1.21) | En Staging se colocÃ³ `worldedit-bukkit-7.4.5.jar` como alternativa limpia para evitar crash NMS. Mantener WorldEdit o buscar build experimental FAWE 26.x. |
| `fastasyncvoxelsniper-3.2.4.jar` | Addon FAWE | âš ï¸� **Baja** (Ligado a FAWE) | Depende de la decisiÃ³n de FAWE vs WorldEdit standard. |
| `StaffPlusPlus.jar` | Upstream | âœ…… **Alta** (Staff mode) | Copiar directo a Staging. |
| `OpenInv.jar` & `InvSee++.jar` | Upstream | âš ï¸� **Media** (NMS container viewing) | Probar en Staging; si fallan, InvSwitcher de BentoBox cubre vaults/inventarios. |
| `Maintenance-Paper-5.1.0.jar` | Upstream | âœ…… **Alta** (Ping event interceptor) | Copiar directo a Staging. |
| `minimotd-paper-2.2.3.jar` | Upstream | âœ…… **Alta** (ServerListPingEvent) | Copiar directo a Staging. |
| `ConsoleSpamFixReborn-1.12.0.jar` | Upstream | âœ…… **Alta** (Log4j filter) | Copiar directo a Staging. |
| `ImageFrame-2026.1.4.1.jar` | Repo `ImageFrame` | âš ï¸� **Media** (Packet map rendering) | Copiar y validar renderizado de mapas en marcos. |
| `LibsDisguises-11.0.18-Premium.jar` | Upstream | âš ï¸� **Media** (ProtocolLib watcher) | Copiar y validar con ProtocolLib en 26.2. |
| `Denizen-1.3.2-b7282.jar` | Upstream | âš ï¸� **Media** (Scripting engine) | Copiar y revisar scripts activos. |
| `Skript-2.16.2.jar` | Upstream | âš ï¸� **Media** (Parser de triggers) | Validar si hay scripts activos en `/plugins/Skript/scripts`. |
| `FancyNpcs-2.9.2-java21.jar` | Upstream FancyPlugins | âœ…… **Alta** (Packet NPC engine moderno) | Copiar a Staging; ya estÃ¡ optimizado para Java 21+. |
| `ItemEdit-3.7.10.jar` & `ItemEditor.jar` | Upstream | âœ…… **Alta** (ItemStack lore/meta) | Copiar directo a Staging. |

---

### F. Addons y Plugins Propios DrakesCraft (P1)
| JAR en Dallas | Tipo / Origen | Compatibilidad Paper 26.2 | AcciÃ³n Requerida para Staging |
|:---|:---|:---:|:---|
| `DiosesDrakes.jar` | Repo `DiosesDrakes` | âœ…… **Alta** (MecÃ¡nica RPG pura) | Copiar a Staging y validar invocaciones divinas. |
| `DrakesArcana.jar` | Repo `ArcanaDrakes` | âœ…… **Alta** (Magia elemental) | Copiar a Staging. |
| `DrakesNanotech-0.4.0.jar` | Repo `DrakesNanotech` | âœ…… **Alta** (Tiene rama `port-26x`) | Desplegar build de `port-26x` a Staging. |
| `Bump-2.5.0-Drake-1.21.11.jar` | Repo `Bump` | âœ…… **Alta** (Recompensas de voto) | Copiar a Staging. |
| `IDreamOfEasy.jar` | Repo `IDreamOfEasy` | âœ…… **Alta** (JAR ya compilado en target/) | Copiar a Staging. |
| `nexcavate-1.0-SNAPSHOT.jar` | Repo `Nexcavate` | âœ…… **Alta** (Tiene rama `port-26x`) | Desplegar build de `port-26x` a Staging. |
| `sfadvancements.jar` | Slimefun Advancements | âœ…… **Alta** (Advancement toasts) | Copiar a Staging. |

---

### G. Addons Slimefun HuÃ©rfanos o No Portados en Staging (P2)
| JAR en Dallas | Tipo / Origen | Compatibilidad Paper 26.2 | AcciÃ³n Requerida para Staging |
|:---|:---|:---:|:---|
| `DyeBench-drake vUNOFFICIAL.jar` | Addon Slimefun | âš ï¸� Pendiente | Evaluar si se absorbe en Suite Utility o se copia. |
| `FNAmplifications vUnoffical-4.2.4.jar` | Addon Slimefun | âš ï¸� Pendiente | Evaluar compatibilidad con Slimefun Universal ABI. |
| `FastMachines-11.0-Drake-1.21.1-SNAPSHOT.jar` | Addon Slimefun | âš ï¸� En `FastMachines-drake` | Probar build en Staging o verificar absorciÃ³n en Tech. |
| `Netheopoiesis vMODIFIED.jar` | Addon Slimefun | âš ï¸� En `Netheopoiesis` | Copiar y probar si genera flora del Nether en 26.2. |

---

## 4. Plan de AcciÃ³n Inmediato para Staging

1. **Fase 1: InyecciÃ³n Inmediata de Plugins Seguros (Pure Bukkit / Sin NMS):**
   - Copiar de Dallas a Staging: `tebex-bukkit`, `UltimateShop`, `ExcellentCrates`, `AuraSkills`, `BetterTeams`, `Jobs-Reborn`, `Quests`, `GSit`, `WildRTP`, `MarriageMaster`, `VotifierPlus`, `40ServidoresMC`, `DiscordSRV`, `AutoMessage`, `ChatGames`, `SkinsRestorer`, `FancyNpcs`.
2. **Fase 2: Despliegue de Builds de Ramas `port-26x` Ya Listas:**
   - Desplegar jars compilados de `AxGraves-Drakes`, `DrakesNanotech`, `Nexcavate` y `BreweryX-Drake`.
3. **Fase 3: SincronizaciÃ³n del Ecosistema Multiverse:**
   - Actualizar `MultiverseCreatures` a la versiÃ³n `v4.9-RELEASE`.
   - Incorporar `MultiverseProgramming` (`v1.2.2`).
   - Confirmar si `MultiverseNets v6.3` opera mejor como mÃ³dulo dentro de `drakes-multiverse.jar` o como JAR desacoplado.
4. **Fase 4: Prueba de Red & Crossplay:**
   - Descargar e incorporar el build mÃ¡s reciente de `Geyser-Spigot` y `floodgate-spigot` en Staging.
5. **Fase 5: Ensayo General de Arranque en Staging:**
   - Reiniciar el servidor de Staging con la flota completa de ~180 plugins y verificar que el conteo de plugins cargados coincida con la paridad total de Dallas.
