---
id: "sy-skill-discover-changelog"
title: "discover - Changelog"
description: "Change history for the discover skill."
aliases: []
keywords: ["version history", "release notes", "discover changes", "revision log"]
author: "Tanner Golden"
path: "BRAIN/System/Skills/.unpackaged/discover/Changelog.md"
layer: 4
folder: "system"
type: "log"
tags: ["system", "log"]
status: "active"
policy: false
created: 2026-06-28
updated: 2026-10-19
---
# discover Changelog

## Current Version

**`01.00.01`**

Semantic versioning, `MAJOR.MINOR.PATCH`, two-digit zero-padded segments. This value matches `metadata.version` in `SKILL.md`. Each section shows the 4 most recent entries; older entries age out. Newest on top.

---

## How This File Works

- **Tracks** changes to how the skill works: tiers, the team, references, templates, the output contract. Not below-PATCH tweaks.
- **Bump** PATCH for a fix, MINOR for a backward-compatible addition, MAJOR for a breaking change. Update the Current Version line with every entry.
- **4-entry cap** per section; a fifth drops the oldest.

---

## Major Updates

> Breaking changes, restructured pipeline, incompatible output. Most recent 4 entries.

### `01.00.00` - 2026-06-28

Initial build of the discover skill: the BRAIN's ideation skill, dispatching the standing Discovery team (Sebastian's crew) to generate ideas wide then converge to a ranked shortlist by pairwise Elo tournament, to the standard generate wide, select fair. Idea records file to the new held idea pool at Inbox/Ideas/. Grounded in a research pass on ideation method (Osborn, CPS, the Double Diamond, the Diehl and Stroebe productivity evidence, Bradley-Terry and Elo, ICE and RICE, the de Bono and SCAMPER lenses, and the how-might-we briefing craft).

## Minor Updates

> Backward-compatible additions. Most recent 4 entries.

_None yet._

## Patch Updates

> Fixes and clarifications. Most recent 4 entries.

### `01.00.01` - 2026-10-19

Moved the preflight off the retired engine: an existing file's last state is committed before an edit, since git history is the backup. The archive now carries the Discovery team, vendored when it is built.

<!-- This is a BRAIN documentation node: it carries the BRAIN global frontmatter schema
     above (Instructions Section 8), not the Agent Skills schema. -->
