<div align="center">

<img src="https://raw.githubusercontent.com/SlimefunNewHorizons/.github/main/profile/assets/new-horizons-banner.svg" alt="Slimefun: New Horizons — Modernizing Slimefun for the next generation of Minecraft" width="100%" />

# Slimefun: New Horizons

### Modernizing Slimefun for the next generation of Minecraft

[![Paper](https://img.shields.io/badge/Production-Paper_1.21.11-38BDF8?style=for-the-badge&logo=minecraft&logoColor=white)](https://papermc.io/)
[![26.2](https://img.shields.io/badge/StarSuites-compile_on_Paper_26.2-8B5CF6?style=for-the-badge&logo=github&logoColor=white)](https://github.com/SlimefunNewHorizons/Drakes-Suites)
[![Java](https://img.shields.io/badge/Java-21_·_25-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)](https://openjdk.org/)
[![Rust](https://img.shields.io/badge/Rust-Off--Heap_SIMD-DEA584?style=for-the-badge&logo=rust&logoColor=white)](https://github.com/SlimefunNewHorizons/Slimefun-Rust)
[![Discord](https://img.shields.io/badge/Discord-Community-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/rv3vtXZTk7)

[🌐 Website](https://web.drakescraft.cl) ·
[💬 Discord](https://discord.gg/rv3vtXZTk7) ·
[🌌 StarSuites](https://github.com/SlimefunNewHorizons/Drakes-Suites) ·
[🧭 All repositories](https://github.com/orgs/SlimefunNewHorizons/repositories) ·
[📊 Verified status](docs/status/ECOSYSTEM_STATUS_2026-10-02.md) ·
[⚖️ Rights & attribution](RIGHTS_AND_ATTRIBUTION.md) ·
[🇪🇸 Español](README_ES.md)

</div>

---

## What is this?

This organization is the home of an **ecosystem**, not a single plugin. It started as an effort to carry [Slimefun](https://github.com/Slimefun/Slimefun4) and its addons
into the next generation of Minecraft servers, and grew around a live production network — **DrakesCraft** (`mc.drakescraft.cl`, Java & Bedrock). Everything is tested there
before it is published.

| Line | In one sentence |
|---|---|
| 🧬 **Slimefun: New Horizons** | Ports, forks and fixes that keep Slimefun and its addons alive on current Paper. |
| 🌌 **StarSuites** | One monorepo that is absorbing the historical addon repositories into 8 mega-suites. |
| ⭐ **Star** | The platform around the game: Star Engine, autonomous operations, observability and backups. |
| 🏛️ **Odysseia** | The server engine: commerce, game modes, economy safeguards, events and bosses. |
| 🐉 **Drakes** | The original gameplay plugins of the DrakesCraft network. |
| 🌠 **Multiverse** | The independent plugin suite by **Chagui68**, interoperable with Slimefun but standalone. |

> ℹ️ **Credit and independence.** Slimefun is created by **TheBusyBiscuit** and the Slimefun community (GPL-3.0). We are **not** its original authors and are **not affiliated
> with or endorsed by** the official Slimefun team. We modernize and rescue; original licenses and credits are always preserved — see [Rights & attribution](RIGHTS_AND_ATTRIBUTION.md).

---

## 📊 Verified status (measured 2026-10-02)

Numbers below were **measured, not estimated**. Method and plugin lists: [`docs/status/ECOSYSTEM_STATUS_2026-10-02.md`](docs/status/ECOSYSTEM_STATUS_2026-10-02.md).

| Question | Answer | Evidence |
|---|---|---|
| Plugins running on the production network (Paper/Purpur **1.21.11**) | **169 loaded** | Live server log |
| …of which maintained or adapted by us | **≈ 64** (43 Drake-branded forks/originals + 21 adapted) | Version strings in the live plugin list |
| …third-party, unmodified | **105** | Same |
| Repositories in the organization | **189** (90 are maintained `-drake` ports/forks) | GitHub API |
| Repositories whose build targets the **1.21.11** API | **61** of 75 with a detectable target | Build files |
| Repositories already referencing **26.x** | **2** (+ the StarSuites below) | Build files |
| **StarSuites compile on Paper 26.2** (`26.2.build.129-stable`, JDK 25) | **9 / 9 modules ✅** | Maven reactor, `BUILD SUCCESS` |
| StarSuites validated **running** on a 26.x server | **Not yet** ⏳ | Staging currently runs 1.21.11 |

> ⚠️ **Compiling is not the same as running.** Season 2 on Paper 26.x ships only after runtime validation of each suite on a real 26.x server.

---

## ⭐ Star — the platform

**Star** is the umbrella for everything that runs *around* the game: the **Star Engine** (the evolution of Odysseia's server kernel, delivered through Suite 7), **SAORI** (autonomous operations:
Discord and WhatsApp assistants, ticket triage, incident handling), observability, automatic backups and a 24/7 cloud runtime. It is the reason a small team can operate a large modded network.

## 🏛️ Odysseia — the server engine

`Odysseia` is the engine that makes a network of **5 isolated game modes** behave like one product. Built on the Slimefun community addon template, it contains:

- **Purchase engine** — idempotent store-purchase delivery with an identity gate, refunds that can be revoked and manual-review paths.
- **Game-mode isolation** — travel between modes with separated inventories, vaults and economies.
- **Economy watchdog** — in-game safeguard against abnormal fast earnings.
- **Events, bosses, chat games, cosmetics, kits, cheques, rebirth system, restart coordination** and a **native Rust bridge** (`Odysseia-Rust`) for hot paths.

## 🐉 Drakes — the DrakesCraft gameplay plugins

| Plugin | What it does |
|---|---|
| `DrakesRankup` | 50 anime/shōnen ranks, transformations, auras, a rank-maintenance economy sink |
| `DrakesVIPPlusPlus` | 15 VIP tiers with unique active abilities, cosmetics and automatic weekend boosters |
| `DrakesBosses` | Arenas, adaptive bosses, rewards and entry economy (anti-AFK, adaptive true damage) |
| `DrakesCrates` | Virtual and physical crates with Slimefun support and a Classic-mode guard |
| `DrakesSlimeMarket` | Dynamic Slimefun material market with inflation control |
| `DrakesNanotech` | Ultra-endgame programmable matter and cosmic technology for Slimefun |
| `DiosesDrakes` · `ArcanaDrakes` | Divine/mythological progression and elemental magic |
| `DrakesTranslate` | Native real-time chat translation |

## 🌠 Multiverse — by [Chagui68](https://github.com/Chagui68)

An independent plugin suite that works **standalone** and also **interoperates** with Slimefun through optional bridges (no hard dependency):

| Plugin | What it is | In production |
|---|---|---|
| **MultiverseNets** | Digital logistics and massive storage, with a bridge to Slimefun Networks | ✅ v4.7 |
| **MultiverseTinker** | Modular metallurgy, 90 minerals, alloys, smeltery and forge; bridge to SlimeTinker | ⏳ release pending |
| **MultiverseCreatures** | Themed custom entities and bosses | ✅ v2.4 |
| **MultiverseProgramming** | Programmable turtles inside Minecraft | ✅ v1.1.6 |

---

## 🌌 StarSuites

The `Drakes-Suites` monorepo is **absorbing the 180+ historical addon repositories into 8 mega-suites plus Multiverse**, with a single ticker engine and one modular configuration system
(`modules/<module>.yml`, hot-reloadable). **Phase 1 is complete; Phase 2 (absorption) is in progress — 44 addon modules are inside so far.**

| Suite | Artifact | Modules absorbed | Focus |
|---|---|---:|---|
| 0 · Core | `drakes-core.jar` | 1 | Kernel, shaded Dough, centralized ticker, SQLite WAL, audit logs |
| 1 · Tech | `drakes-tech.jar` | 6 | Networks-style logistics, DynaTech, FoxyMachines, Supreme, FluffyMachines, InfinityExpansion |
| 2 · Bio | `drakes-bio.jar` | 7 | Cultivation, GeneticChickengineering, FlowerPower, TreeTaps, MobCapturer, ExoticGarden, SlimyBees |
| 3 · Magic | `drakes-magic.jar` | 4 | RelicsOfCthonia, Crystamae, AlchimiaVitae, SoulJars |
| 4 · Generators | `drakes-generators.jar` | 6 | LiteXpansion, reactors, SMG, EcoPower, ore chunks, ultimate generators |
| 5 · Utility | `drakes-utility.jar` | 13 | Backpacks, SlimeHUD, ChestTerminal, SFCalc, portal gun, sound muffler and more |
| 6 · Combat | `drakes-combat.jar` | 6 | Warfare, ObsidianExpansion, ExtraGear, mob drops, SlimeTinker |
| 7 · Server | `drakes-server.jar` | 1 | Star Engine, economy module |
| Multiverse | `drakes-multiverse.jar` | — | By Chagui68 (see above) |

Everything not yet absorbed keeps shipping as individual `-drake` ports, preserving every item ID so no player data is ever put at risk.

---

## 🧭 Roadmap (exploring)

- **Season 2 on Paper 26.x** — runtime validation of each suite on a real 26.x server, then an atomic rollout.
- **DrakesID** — our own account identity (one account, many Java/Bedrock identities, per-mode scoping) to simplify purchases, rollbacks and ranks.
- **Display-based 3D** — pipes and cables drawn with `ItemDisplay`/`BlockDisplay` entities, inspired by [PylonMC/Rebar](https://github.com/pylonmc/rebar) (LGPL-3.0, with attribution).
- **Rights & licensing rollout** — a license and credit block in every repository ([policy](RIGHTS_AND_ATTRIBUTION.md)).

## 🤝 Standing on the shoulders of

Non-exhaustive list of upstream authors and projects we build on (each repository carries its own credits and license):
**TheBusyBiscuit and the Slimefun community** (Slimefun 4) · **Sefiraat** (Networks, SlimeTinker and other addons) · **Seggan** · **balugaq** and **ytdd9527** (NetworksExpansion / JustEnoughGuide) ·
**J3fftw** (WorldEditSlimefun) · **tastybento and the BentoBox team** (BentoBox, InvSwitcher) · **Dominic Feliton** (WorldwideChat) · **Rugzy** (PlayerVaultZ) · **spearforge** (sBank) · **PylonMC** (inspiration).

## Contributing

1. Active development of consolidated plugins happens in [`Drakes-Suites`](https://github.com/SlimefunNewHorizons/Drakes-Suites).
2. **Never break player data**: no item, inventory or purchase history may be put at risk; PDC keys are preserved.
3. Forks and consolidations **keep their original licenses** and credit the original authors.
4. Public READMEs are written in English; Spanish documentation lives alongside as `README_ES.md`.

<div align="center">

**Slimefun: New Horizons** · built with ♥ by the DrakesCraft Labs community<br/>
[Website](https://web.drakescraft.cl) · [Discord](https://discord.gg/rv3vtXZTk7) · [StarSuites](https://github.com/SlimefunNewHorizons/Drakes-Suites)

</div>
