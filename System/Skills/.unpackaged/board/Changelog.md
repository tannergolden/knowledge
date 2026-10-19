---
id: "sy-skill-board-changelog"
title: "board - Changelog"
description: "Change history for the board skill."
aliases: []
keywords: ["version history", "release notes", "board changes", "revision log"]
author: "Tanner Golden"
path: "BRAIN/System/Skills/.unpackaged/board/Changelog.md"
layer: 4
folder: "system"
type: "log"
tags: ["system", "log"]
status: "active"
policy: false
created: 2026-06-29
updated: 2026-10-19
---
# board Changelog

## Current Version

**`02.01.01`**

Semantic versioning, `MAJOR.MINOR.PATCH`, two-digit zero-padded segments. This value matches `metadata.version` in `SKILL.md`. Each section shows the 4 most recent entries; older entries age out. Newest on top.

---

## How This File Works

- **Tracks** changes to how the skill works: tiers, the team, references, templates, the output contract. Not below-PATCH tweaks.
- **Bump** PATCH for a fix, MINOR for a backward-compatible addition, MAJOR for a breaking change. Update the Current Version line with every entry.
- **4-entry cap** per section; a fifth drops the oldest.

---

## Major Updates

> Breaking changes, restructured pipeline, incompatible output. Most recent 4 entries.

### `02.00.00` - 2026-06-29

Rebuilt board from a decision-only skill into the BRAIN's venture operating system: five modes (found, strategize, decide, operate, review) over the expanded Agent Resources (AR) Fortune 500 workforce, scaled to the venture's stage. The decision engine is preserved as the decide mode. New: a venture-context preflight (read Overview/Goals/Strategy/Log, detect the stage) and write-back into the venture folder; the sole-writer model (no AR agent holds Write/Edit; the skill persists, behind a write-gate that gates money, contracts, external comms, deletes, and equity to the Founder); specialist dispatch (a lead frames, specialists produce) and the Head of Quality as the independent verifier of consequential output. Added ten references (modes-router, lifecycle, founding-playbook, strategy-toolkit, metrics-and-kpis, operating-cadence, write-gate, verification, specialist-dispatch, department-deliverable-catalog), six templates (founding-checklist, okr-cycle, deliverable-contract, venture-scorecard, qbr-sixpager, venture-health-check), and three assets (expanded trigger-evals, delegation-of-authority, stage-machine). Built alongside the AR expansion (90 agents, 18 departments, board and committees) and the Ventures template upgrade (an Administration strategic core, a financial model, and a cap table). Grounded in a deep research and audit pass on Fortune 500 structure, function deliverables, the company lifecycle, the operating model, strategy frameworks, metrics, venture creation, governance, and AI-operating-system guardrails.

### `01.00.00` - 2026-06-29

Initial build of the board skill: the BRAIN's decision skill, convening the Agent Resources (AR) corporate workforce as a board (the CEO chairs from Administration, the department leads give independent functional views, a dissent pass beats groupthink, and the chair synthesizes by RAPID to one recommendation with one accountable owner), to the standard every angle heard, one owner accountable. It decides and names the owner; irreversible or major calls escalate to the Founder. Replaces the archived company skill. Grounded in a research pass on executive deliberation (the chair's role and governance basics, the multi-perspective decision-framework toolkit, orchestrating functional heads without groupthink or the highest-paid opinion, and the board-style decision-memo format).

## Minor Updates
### `02.01.00` - 2026-07-02

Aligned the skill to the 2026-07-02 workforce lean build. Four AR departments dissolved (Sales & Marketing, Strategy & Corporate Development, Enterprise Risk, Internal Audit): the marketing seats (Product Marketing Manager Felix, Demand Generation Manager Derek) moved under the Chief Revenue Officer in Sales & Revenue and every CMO reference repointed there; strategy framing absorbed by the CEO (options, reversibility flags, recommend-not-decide) and every CSO reference repointed; the Risk/Audit scorecard row and lifecycle committee layer re-mechanized onto the write-gate, health, changelog, and backups, with the CISO holding security residuals. Retired specialist references repointed to their named survivors, the five nonexistent "Head of" titles corrected to the real chief titles, the crisis-communications plan reassigned to its actual producer (Nathaniel), and the functional-lead count fixed. Venture-folder paths (the Sales & Marketing (S&M)/ files) are unchanged.


> Backward-compatible additions. Most recent 4 entries.

_None yet._

## Patch Updates

> Fixes and clarifications. Most recent 4 entries.

### `02.01.01` - 2026-10-19

Moved the write gate and the preflight off the retired engine: an existing file's last state is committed before an edit (git history is the backup, so the snapshot step is gone), the dedup check is a vault search, and every write ends with `.github/scripts/update-vault.py` and `check-vault.py` instead of `sync` and `health`. The archive now carries the Administration team, vendored when it is built.

<!-- This is a BRAIN documentation node: it carries the BRAIN global frontmatter schema
     above (Instructions Section 8), not the Agent Skills schema. -->
