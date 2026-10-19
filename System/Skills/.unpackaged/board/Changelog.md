<!--
title: "board - Changelog"
description: "Change history for the board skill."
type: "record"
keywords: ["version history", "release notes", "board changes", "revision log"]
-->
# board Changelog

## Current Version

**`2.1.3`**

The version is SemVer, per standards' [versioning policy](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Releases-&-Versioning.md#-versioning-policy-semver). It matches `metadata.version` in `SKILL.md`, and `check-skills.py` fails when they differ. Each section shows the 4 most recent entries; older entries age out. Newest on top.

---

## How This File Works

- **Tracks** changes to how the skill works: tiers, the team, references, templates, the output contract. Not below-PATCH tweaks.
- **Bump** the version by standards' [versioning policy](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Releases-&-Versioning.md#-versioning-policy-semver), and update the Current Version line with every entry.
- **4-entry cap** per section; a fifth drops the oldest.

---

## Major Updates

> Breaking changes, restructured pipeline, incompatible output. Most recent 4 entries.

### `2.0.0` - 2026-06-29

Rebuilt board from a decision-only skill into the BRAIN's venture operating system: five modes (found, strategize, decide, operate, review) over the expanded Agent Resources (AR) Fortune 500 workforce, scaled to the venture's stage. The decision engine is preserved as the decide mode. New: a venture-context preflight (read Overview/Goals/Strategy/Log, detect the stage) and write-back into the venture folder; the sole-writer model (no AR agent holds Write/Edit; the skill persists, behind a write-gate that gates money, contracts, external comms, deletes, and equity to the Founder); specialist dispatch (a lead frames, specialists produce) and the Head of Quality as the independent verifier of consequential output. Added ten references (modes-router, lifecycle, founding-playbook, strategy-toolkit, metrics-and-kpis, operating-cadence, write-gate, verification, specialist-dispatch, department-deliverable-catalog), six templates (founding-checklist, okr-cycle, deliverable-contract, venture-scorecard, qbr-sixpager, venture-health-check), and three assets (expanded trigger-evals, delegation-of-authority, stage-machine). Built alongside the AR expansion (90 agents, 18 departments, board and committees) and the Ventures template upgrade (an Administration strategic core, a financial model, and a cap table). Grounded in a deep research and audit pass on Fortune 500 structure, function deliverables, the company lifecycle, the operating model, strategy frameworks, metrics, venture creation, governance, and AI-operating-system guardrails.

### `1.0.0` - 2026-06-29

Initial build of the board skill: the BRAIN's decision skill, convening the Agent Resources (AR) corporate workforce as a board (the CEO chairs from Administration, the department leads give independent functional views, a dissent pass beats groupthink, and the chair synthesizes by RAPID to one recommendation with one accountable owner), to the standard every angle heard, one owner accountable. It decides and names the owner; irreversible or major calls escalate to the Founder. Replaces the archived company skill. Grounded in a research pass on executive deliberation (the chair's role and governance basics, the multi-perspective decision-framework toolkit, orchestrating functional heads without groupthink or the highest-paid opinion, and the board-style decision-memo format).

## Minor Updates

> Backward-compatible additions. Most recent 4 entries.

### `2.1.0` - 2026-07-02

Aligned the skill to the 2026-07-02 workforce lean build. Four AR departments dissolved (Sales & Marketing, Strategy & Corporate Development, Enterprise Risk, Internal Audit): the marketing seats (Product Marketing Manager Felix, Demand Generation Manager Derek) moved under the Chief Revenue Officer in Sales & Revenue and every CMO reference repointed there; strategy framing absorbed by the CEO (options, reversibility flags, recommend-not-decide) and every CSO reference repointed; the Risk/Audit scorecard row and lifecycle committee layer re-mechanized onto the write-gate, health, changelog, and backups, with the CISO holding security residuals. Retired specialist references repointed to their named survivors, the five nonexistent "Head of" titles corrected to the real chief titles, the crisis-communications plan reassigned to its actual producer (Nathaniel), and the functional-lead count fixed. Venture-folder paths (the Sales & Marketing (S&M)/ files) are unchanged.

## Patch Updates

> Fixes and clarifications. Most recent 4 entries.

### `2.1.3` - 2026-10-19

- Founding gives each copied venture file its real `title`, `description` and `type`, the vault's hidden frontmatter, in place of rewriting the retired `id` and `path` (`SKILL.md`, `references/modes-router.md`, `references/write-gate.md`).
- The callouts in `references/metrics-and-kpis.md` and `templates/qbr-sixpager.md` are GitHub alerts.

### `2.1.2` - 2026-10-19

- References point at `AGENTS.md`, the folder notes' Rules and `.docs/vault/` instead of the retired root rule files.
- The licence is MIT, and the versioning rules link to tannergolden/standards instead of restating them.
- Versions are plain SemVer: `02.01.01` is now `2.1.1`.

### `2.1.1` - 2026-10-19

Moved the write gate and the preflight off the retired engine: an existing file's last state is committed before an edit (git history is the backup, so the snapshot step is gone), the dedup check is a vault search, and every write ends with `.github/scripts/update-vault.py` and `check-vault.py` instead of `sync` and `health`. The archive now carries the Administration team, vendored when it is built.

<!-- This is a BRAIN documentation node: it carries the vault's note schema above
     (.docs/vault/Note-Schema.md), not the Agent Skills schema. -->
