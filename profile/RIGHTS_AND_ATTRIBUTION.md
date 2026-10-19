# Rights, Licensing & Attribution Policy

> **Status: DRAFT for owner review.** This is an engineering policy, **not legal advice**. Before enforcing it against third parties or changing
> any license in a published repository, have it reviewed by a qualified lawyer. 🇪🇸 [Versión en español](RIGHTS_AND_ATTRIBUTION_ES.md)

Applies to every repository in the **SlimefunNewHorizons** organization (Slimefun: New Horizons / StarSuites / DrakesCraft) and to anything published from it
(GitHub, Modrinth, Maven, releases).

## 1. Principles

1. **Our original work is © JackStar6677-1 and DrakesCraft Labs contributors — ALL RIGHTS RESERVED**, unless a repository contains an explicit `LICENSE` file that says otherwise.
2. **Original authors always get credit, and their licenses always stay.** We never remove, replace, shorten or contradict an upstream copyright notice or license.
3. **The creators of Slimefun keep every right they have.** Slimefun 4 is created by **TheBusyBiscuit and the Slimefun community** and is licensed under **GPL-3.0**.
   Nothing in this policy licenses, restricts or "reserves" their work or any modification of it.
4. **Copyleft is not optional.** A work derived from GPL-3.0 code must itself be distributed under GPL-3.0. "All rights reserved" **cannot** be applied to it.
   This is why "all rights reserved" applies only to code that is genuinely ours (see §2).

## 2. Repository classes

Every repository belongs to exactly one class, recorded in [`docs/rights/repo-rights-manifest.csv`](docs/rights/repo-rights-manifest.csv).

| Class | What it is | License | Credits required |
|---|---|---|---|
| **A · ORIGINAL** | 100 % written by us; does **not** derive from third-party code and is not a derivative of a copyleft library. | **All Rights Reserved** (`templates/rights/LICENSE-ARR.txt`). | Our copyright line; list third-party *dependencies* in `NOTICE`. |
| **B · OPEN-DERIVATIVE** | Fork, port, rewrite or consolidation of someone else's project (e.g. Slimefun and its addons), including original code that links to Slimefun's API. | **Keep the upstream license** (GPL-3.0 / LGPL-3.0 / MIT / Apache-2.0 …). Slimefun-linked modules default to **GPL-3.0**. | Upstream copyright + `NOTICE` + README credit block (§4). |
| **C · THIRD-PARTY AUTHORED, HOSTED HERE** | Written by another person who hosts or develops it in this org (e.g. **Chagui68**'s MultiverseNets / MultiverseTinker / MultiverseCreatures / MultiverseProgramming). | **The author's choice**, recorded in the file. Never ours to relicense. | Author named in README and `NOTICE`. |
| **D · UNKNOWN UPSTREAM** | Derived from third-party code whose license we have **not** verified. | **Unresolved — treat as the strictest possible** (no copying, no new releases) until verified. | `NOTICE` naming the original author immediately. |

> **Mixed repositories** (e.g. the `Drakes-Suites` monorepo) are classified by their *most restrictive* component: if any module is derived from GPL code, the
> combined distributable is GPL-3.0. Original modules should live in their own class-A repository whenever practical.

## 3. What each class must contain

* **A:** `LICENSE` (ARR text), copyright header (optional per file), README footer.
* **B / C / D:** the upstream `LICENSE` file **unchanged**, a `NOTICE` (template: `templates/rights/NOTICE-UPSTREAM.md`) and the README credit block.
* **All:** never delete `LICENSE`, `NOTICE`, `AUTHORS` or copyright headers inherited from upstream.

## 4. Mandatory credit block for anything Slimefun-related

Put this in the README of every class B/C/D repository that extends or derives from Slimefun (adapt the second line to the real upstream addon):

```markdown
## Credits & License
This project is based on / extends **[Slimefun 4](https://github.com/Slimefun/Slimefun4)** by **TheBusyBiscuit** and the Slimefun community (GPL-3.0).
Derived from **<Addon name>** by **<original author>** (<upstream URL>, <upstream license>).
It is an independent community project and is **not affiliated with or endorsed by** the official Slimefun team.
Modifications © DrakesCraft Labs contributors, distributed under the same license as the original.
```

## 5. Distribution rules

* GPL obligations are triggered by **distribution** (publishing a jar on Modrinth/GitHub Releases/Maven counts). A GPL-derived jar may only be published together with its
  corresponding source and the `LICENSE` file. **Repositories with no `LICENSE` that publish builds are out of compliance today** — see §7.
* **Class D repositories publish nothing** (no releases, no Modrinth project) until the upstream license is verified or permission is obtained.
* Running software privately on our own server is not distribution; publishing a download is.

## 6. Contributions

Contributions to class-A repositories are accepted only if the contributor agrees, in the pull request, that their contribution may be used under the repository's
license and that they have the right to submit it. Contributions to B/C/D repositories are accepted under the repository's existing license.

## 7. Current state (audit of 2026-10-02) and rollout

The audit of 179 local clones found: **75 repositories with no license file**, 66 GPL-3.0, 29 MIT, 4 LGPL-3.0, 1 Apache-2.0, 100 repositories that depend on Slimefun
(17 of them with no license file; 15 with no credits in the README). Only **5 repositories are confidently class A**; 42 cannot be classified without the owner's input.
Full per-repository table and proposed action: [`docs/rights/repo-rights-manifest.csv`](docs/rights/repo-rights-manifest.csv).

Rollout order (do not apply blindly — each license choice needs the owner's confirmation):

1. **Stop the bleeding:** for class-D repositories, pause releases/Modrinth publication; add `NOTICE` naming the original author.
2. **Add missing license files**, starting with the 17 Slimefun-linked repositories with none (GPL-3.0) and the confirmed class-A repositories (ARR).
3. **Add the credit block (§4)** to the 15 Slimefun-related READMEs that lack credits.
4. Resolve class D by obtaining the upstream license text, a written permission, or removing/rewriting the code.
5. Review quarterly; keep the manifest in sync (a CI check for `LICENSE`/`NOTICE` presence is recommended).

## 8. GitHub organization settings that support this policy

The *Repository policies* page (organization rulesets) is **not enforced on the Free plan** — GitHub states it applies only after upgrading to **GitHub Team**.
Equivalent free controls: **Organization → Settings → Member privileges**:

| Control | Recommended |
|---|---|
| Repository creation | Owners only (or disable public creation) |
| Repository deletion and transfer | **Disallow members** |
| Base permissions | *Read* |
| Two-factor authentication requirement | **Enable** (currently disabled) |

If the organization later moves to GitHub Team, create one repository policy with: **Restrict deletions** and **Restrict transfers** (allow list = owners),
**Restrict creations** (allow list = owners), and **Restrict visibility** only if private-by-default is desired.
