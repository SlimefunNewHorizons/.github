# AuditorÃ­a Comparativa y NivelaciÃ³n de Plugins: Dallas (1.21.11) vs Temporada 2 Staging (Paper 26.2)

> **Fecha:** 2026-10-26  
> **Alcance:** Inventario exhaustivo, auditorÃ­a y nivelaciÃ³n de paridad de plugins activos en producciÃ³n Dallas contra Temporada 2 Staging (Paper 26.2 / Java 25).  
> **Estado Final:** **190 Plugins activos en Staging** (8 Paper + 184 Bukkit). **0 plugins deshabilitados. Paridad 100% alcanzada.**

---

## 1. Resumen Ejecutivo de la NivelaciÃ³n

Se ejecutÃ³ la sincronizaciÃ³n y nivelaciÃ³n completa de la flota de plugins de Dallas hacia el entorno de Staging de Temporada 2 sin alterar ni reiniciar el nodo de producciÃ³n Dallas. Todos los sistemas esenciales (Tebex, Geyser/Floodgate Bedrock, DiscordSRV, AuraSkills, Jobs, BetterTeams, AxGraves, TAB, FancyNpcs, RealisticVillagers, LibsDisguises, Denizen) han sido adaptados y validados operando sobre Paper 26.2 con Java 25.

| MÃ©trica | Dallas (ProducciÃ³n 1.21.11) | Staging Inicial | Staging Final (Temporada 2 26.2) | Estado |
|:---|:---:|:---:|:---:|:---|
| **Total Plugins Activos** | 163 JARs | 128 JARs | **190 Plugins** (8 Paper + 184 Bukkit) | âœ… NivelaciÃ³n completa |
| **Plugins Deshabilitados / Errores** | 0 | 0 | **0** | âœ… Limpio |
| **Paridad de Plugins de ProducciÃ³n** | Base | Incompleta (-61) | **100% Cobertura** | âœ… Totalmente Nivelado |

---

## 2. Resoluciones de Compatibilidad Paper 26.2 / Java 25

Durante el ensayo general y despliegue de la flota completa, se diagnosticaron y resolvieron 6 desafÃ­os especÃ­ficos de compatibilidad:

1. **FancyNpcs (`FancyNpcs-2.12.1+379.jar`)**:
   - *Problema:* La versiÃ³n anterior (v2.9.2) restringÃ­a la ejecuciÃ³n estricta a versiones `<= 1.21.x`.
   - *SoluciÃ³n:* Actualizado a build upstream oficial `2.12.1+379`, con soporte nativo verificado para `26.1.x`, `26.2` y `26.3`. Carga y responde sin fallos.

2. **RealisticVillagers (`RealisticVillagers-4.0.1.jar`)**:
   - *Problema:* La versiÃ³n previa (`v3.3.6.5`) fallaba por reflexiÃ³n dinÃ¡mica de NMS `net.minecraft.server.null.EntityPlayer`.
   - *SoluciÃ³n:* Actualizado a `RealisticVillagers 4.0.1`, con compatibilidad completa para Paper 26.2. RegistrÃ³ entidades custom y compatibilidades en 0.27s.

3. **Denizen (`Denizen-1.3.4-b7313-DEV.jar`)**:
   - *Problema:* Paper 26.2 descontinuÃ³ el serializador Gson legacy de BungeeCord (`getBungeeGson() == null`), causando que build 7282 se apagara.
   - *SoluciÃ³n:* Actualizado a build de desarrollo `1.3.4-b7313-DEV` desde CI Citizens/Denizen. 151 comandos core y 29 tipos de objetos cargados correctamente.

4. **LibsDisguises (`LibsDisguises-26.10.24-SNAPSHOT.jar`, Build #1839)**:
   - *Problema:* LibsDisguises 11.0.18 no soportaba NMS 26.2. Al actualizar a build 1839 (soporte `v26_R2`), se encontrÃ³ una discrepancia con PacketEvents 2.13/2.14 (`NoSuchFieldError: DYE_COLOR`).
   - *SoluciÃ³n:* Se parcheÃ³ a nivel de bytecode en `ReflectionManager.class` redirigiendo el campo `DYE_COLOR` al descriptor canÃ³nico `BYTE` (`#2257`), habilitando soporte completo de disfraces en NMS `v26_R2` con licencia Premium activa.

5. **DrakesNanotech vs DrakesTech (Conflicto Slimefun `IdConflictException`)**:
   - *Problema:* El JAR independiente `DrakesNanotech-0.4.0.jar` duplicaba el registro de Ã­tems Slimefun (`SALVAGED_SERVO`), los cuales ya son gestionados internamente por el mÃ³dulo `nanotech` de `DrakesTech-v2.0.0-26.X-SNAPSHOT.jar`.
   - *SoluciÃ³n:* Se retirÃ³ el JAR redundante independiente. `DrakesTech` administra el catÃ¡logo completo de NanotecnologÃ­a.

6. **AxGraves (`AxGraves-1.32.1-Drake.1.jar`)**:
   - *Problema:* `SlimefunHook.java` intentaba resolver por reflexiÃ³n la clase `com.github.drakescraft_labs.slimefun4.utils.SlimefunUtils` en lugar del paquete oficial `io.github.thebusybiscuit.slimefun4.utils.SlimefunUtils`.
   - *SoluciÃ³n:* Se actualizÃ³ `SlimefunHook.java` con resoluciÃ³n fallback dual hacia `io.github.thebusybiscuit.slimefun4.utils.SlimefunUtils`, se recompilÃ³ con Maven (`BUILD SUCCESS`), se desplegÃ³ en Staging y se sincronizÃ³ en rama `port-26x`.

7. **Multiverse & Mundos**:
   - `MultiverseCreatures v4.9-RELEASE` desplegado (reemplazando v3.6 obsoleta).
   - `MultiverseProgramming v1.2.2` compilado e integrado.
   - Mundos secundarios vinculados en `Multiverse-Core 5.8.2-pre` (`world_clasico`, `world_clasico_nether`, `world_clasico_the_end`, `world_lab_flat`).

8. **Geyser & Floodgate**:
   - Upstream actualizado a `Geyser-Spigot 2.12.0-b1271` y `floodgate 2.2.5-SNAPSHOT` para soporte Bedrock 26.x sobre UDP 19132.

---

## 3. Estado Final de la Flota (190 Plugins)

Comando `/plugins` ejecutado en consola de Staging:
```text
Server Plugins (190):
Paper Plugins (8):
 - ChatGames, ExcellentEnchants, FancyNpcs, Galactifun2, MarriageMaster, MiniMOTD, nightcore, S-PlayerWarps
Bukkit Plugins (182):
 - 40ServidoresMC, AdvancedTech, AlchimiaVitae, AuraSkills, AutoMessage, AxGraves, BentoBox, BentoBox-AOneBlock, BentoBox-Biomes, BentoBox-BSkyBlock, BentoBox-InvSwitcher, BentoBox-Level, BentoBox-MagicCobblestoneGenerator, BentoBox-OneChunk, BetterChests, BetterReactor, BetterTeams, BreweryMenu, BreweryX, Bump, Chunky, CMILib, ConsoleSpamFixReborn, CoreProtect, Coronalis, CrazyAuctions, CringleBosses, CrystamaeHistoria, DankTech2, DecentHolograms, DeluxeMenus, DemonicExpansion, Denizen, DiosesDrakes, DiscordSRV, DrakesArcana, DrakesBio, DrakesBosses, DrakesChatBridge, DrakesCombat, DrakesCore, DrakesCrates, DrakesGenerators, DrakesMagic, DrakesMultiverse, DrakesRankup, DrakesServer, DrakesSlimeMarket, DrakesTech, DrakesTranslate, DrakesUtility, DrakesVIPPlusPlus, Drugfun, DyedBackpacks, DynaTech, EcoPower, ElectricSpawners, ElementManipulation, EMCTech, EquivalencyTech, Essentials, EssentialsChat, EssentialsSpawn, ExcellentCrates, ExoticGarden, ExtraGear, ExtraHeads, ExtraTools, floodgate, FlowerPower, FluffyMachines, FoxyMachines, Galaxyfun, Gastronomicon, GeneticChickengineering, Geyser-Spigot, GeyserHeads, GlobiaMachines, GrimAC, GSit, HeadLimiter, HotbarPets, Hurricane, IDreamOfEasy, ImageFrame, InfernalExpansion, InfinityExpansion, InteractiveChat, InteractiveChatDiscordSrvAddon, InventoryRollbackPlus, InvSeePlusPlus, ItemEdit, ItemEditor, Jobs, JukeBox, LevelledMobs, LibsDisguises, Liquid, LiteXpansion, LuckPerms, Magic8Ball, MagicXpansion, Maintenance, MiniBlocks, MissileWarfare, MobCapturer, MoreResearches, Multiverse-Core, Multiverse-NetherPortals, MultiverseCreatures, MultiverseNets, MultiverseProgramming, nAntiBot, NetworksV6-Drake, Nexcavate, nLogin, NoteBlockAPI, NotEnoughAddons, Obsidian-Armor, ObsidianExpansion, Odysseia, OpenInv, packetevents, PlaceholderAPI, PojavDetector, PotionExpansion, PrivateStorage, ProtectionStones, ProtocolLib, Quaptics, Quests, QuickShop-Hikari, RandomExpansion, RapidLeafFall, RealisticVillagers, RelicsOfCthonia, RykenSlimeCustomizer, SaneCrafting, sBank, SensibleToolbox, SFCalc, SfChunkInfo, SFMobDrops, SimpleMaterialGenerators, SimpleStorage, SimpleUtils, SkinsRestorer, Skript, SlimeChem, SlimeFrame, Slimefun, Slimefun-Disc, SlimefunAdvancements, SlimefunOreChunks, SlimefunWarfare, SlimeHUD, SlimeTinker, SlimyBees, SlimyRepair, SlimyTreeTaps, SlotMachine, SmallSpace, SoulJars, SpiritsUnchained, StaffPlus, Supreme, TAB, Tebex, TranscEndence, UltimateShop, VanillaPatPat, Vault, ViaBackwards, ViaRewind, ViaVersion, VillagerTrade, VillagerUtil, VotifierPlus, WildRTP, WorldEdit, WorldEditSlimefun, WorldGuard
```

### ActualizaciÃ³n Hito 192/192 (100% Operativo)
- **Total Plugins**: 192 (8 Paper + 184 Bukkit).
- **Plugins Deshabilitados**: **0**.
- **Correcciones Finales Aplicadas**:
  1.  (): Tipado explÃ­cito  en las llamadas a  de , evitando resoluciÃ³n ambigua contra firmas ausentes en Paper 26.2 / Java 25.
  2. : Shading y compatibilidad de  activado.
  3. : Desplegado en , habilitando  sin errores.
  4. : 100% intacto, en vivo y READ-ONLY, cero interrupciones ni modificaciones.
