<!--
title: "finance - Changelog"
description: "Change history for the finance skill."
type: "record"
keywords: ["version history", "release notes", "finance changes", "revision log"]
-->
# finance Changelog

## Current Version

**`1.0.0`**

The version is SemVer, per standards' [versioning policy](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Releases-&-Versioning.md#-versioning-policy-semver). It matches `metadata.version` in `SKILL.md`, and `check-skills.py` fails when they differ. Each section shows the 4 most recent entries; older entries age out. Newest on top.

---

## How This File Works

- **Tracks** changes to how the skill works: modes, tiers, the team, references, templates, the output contract. Not below-PATCH tweaks.
- **Bump** the version by standards' [versioning policy](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Releases-&-Versioning.md#-versioning-policy-semver), and update the Current Version line with every entry.
- **4-entry cap** per section; a fifth drops the oldest.

---

## Major Updates

> Breaking changes, restructured pipeline, incompatible output. Most recent 4 entries.

### `1.0.0` - 2026-10-22

Initial build of the finance skill: the BRAIN's personal and household finance skill, dispatching the new standing Finance team in `Inbox/Faculties/Finance/` (Theodore leads Lucille, Owen, Harriet, Graham, Clara, Elliot and Henry, with Ingrid as the independent Plan Reviewer) to the standard of the Founder's interest first, with show the math as its craft rule. Three modes (ask, plan, review) and three tiers (quick, standard, deep); a fact sheet compiled before dispatch; every load-bearing number reproduced by a script before review; a blind review gate on consequential advice; and a gate that never moves money and never records a secret. Five references (doctrine, dispatch, data and writes, cadence, life events), five templates (fact sheet, brief, plan, review, checkup), and two assets (trigger tests, official US sources).

## Minor Updates

> Backward-compatible additions. Most recent 4 entries.

## Patch Updates

> Fixes and clarifications. Most recent 4 entries.

<!-- This is a BRAIN documentation node: it carries the vault's note schema above
     (.docs/technical/vault/Note-Schema.md), not the Agent Skills schema. -->
