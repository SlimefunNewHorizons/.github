# Contributing Guidelines & Engineering Standards

Welcome to **SlimefunNewHorizons**! We build, maintain, and optimize mission-critical Minecraft server software, Slimefun addons, paper/purpur forks, and server-side utilities running in production under high concurrency.

To maintain rock-solid stability and zero player data corruption, we enforce strict engineering standards across all repositories.

---

## 🏛️ 1. Code of Conduct & Respect

All participants are required to adhere to our [Code of Conduct](CODE_OF_CONDUCT.md). 
We expect all interactions in issues, pull requests, and discussions to remain professional, constructive, and technically grounded. 
**Insults, demanding language, ad-hominem attacks, or toxic entitlement will result in immediate thread locking and account blocking.**

---

## 📋 2. Issue-First Workflow (Mandatory)

Before writing code or opening a Pull Request:

1. **Check Existing Issues**: Make sure the bug or feature hasn't already been reported or solved.
2. **Open an Issue First**:
   - For **Bug Reports**: Provide complete reproduction steps, exact server software version (e.g., Paper/Purpur 1.21.11, build #), clean stack traces/logs, and list of active plugins.
   - For **Feature Requests / Architectural Changes**: Clearly articulate the problem and design before implementing anything.
3. **Wait for Maintainer Approval**: Do not open unsolicited PRs rewriting core mechanics, item storage engines, or data models. **Unsolicited massive PRs will be closed without review.**

---

## 🛡️ 3. SRE Golden Rule: Zero Production Disruption

Our code runs on live production networks with hundreds of active players:
* **Zero Item Loss & Zero BlockStorage Corruption**: Any PR touching persistent data (`BlockStorage`, `NamespacedKey`, PDC, SQLite databases, player vaults, island data) must guarantee zero data loss, backwards compatibility, and anti-dupe safety.
* **No Spigot Main Thread Blocking**: Database operations, network I/O, heavy file reads, and web calls must execute asynchronously (`runTaskAsynchronously`). Never block the primary server tick thread.
* **No Memory Leaks**: Clean up listeners, static collections, player references, and tasks on `onDisable` or player quit.

---

## 🛠️ 4. Pull Request Requirements

* **Target Branch**: Default target is `main` (for production/1.21.11 fixes) or `port-26x` / `26.x` (for 26.x development). Follow branch guidelines in [AGENTS.md](AGENTS.md).
* **Language & GUI Standards**: All player-facing GUI titles, item names, lore, and chat messages MUST be in **English**. Internal code and documentation may be in English or Spanish.
* **Pass All Quality Gates**:
  - Code must compile with Maven (`mvn clean package`) or Cargo with zero errors and zero warnings.
  - Tests must pass.
  - Clean commit history with descriptive messages.

---

## 🤖 5. AI-Assisted and Agent Contributions

We enforce a strict **Zero-Slop Policy**:
* If an AI was used, disclose it in the PR description.
* The human contributor assumes **100% engineering responsibility** for every line.
* Fabricated Bukkit/Spigot/Paper methods, hallucinated Slimefun APIs, non-compiling boilerplate, or unchecked AI diffs will be closed immediately as spam.
* See [AGENTS.md](AGENTS.md) for full automated contributor specifications.

## Attribution / Atribución

Every repository must keep the credits block (`<!-- credits:start -->`) at the top of its README and `docs/UPSTREAM_ATTRIBUTION.md` with the original authors linked, plus the upstream LICENSE unchanged. Never invent authors: if unknown, write "in verification". Index: [CREDITS.md](CREDITS.md). Policy: [RIGHTS_AND_ATTRIBUTION.md](RIGHTS_AND_ATTRIBUTION.md).
