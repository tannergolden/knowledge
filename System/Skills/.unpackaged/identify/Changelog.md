---
title: "identify - Changelog"
description: "Change history for the identify skill, the BRAIN's coverage-driven Profile interviewer."
status: "active"
tags: ["system", "log"]
aliases: []
keywords: ["version history", "release notes", "identify changes", "revision log"]
created: 2026-07-03
updated: 2026-10-19
type: "log"
folder: "system"
layer: 4
policy: false
author: "Tanner Golden"
path: "BRAIN/System/Skills/.unpackaged/identify/Changelog.md"
id: "sy-skill-identify-changelog"
---
# identify Changelog

## Current Version

**`01.00.01`**

Semantic versioning, `MAJOR.MINOR.PATCH`, two-digit zero-padded segments. This value matches `metadata.version` in `SKILL.md`. Each section shows the 4 most recent entries; older entries age out. Newest on top.

---

## How This File Works

- **Tracks** changes to how the skill works: modes, the crew, references, templates, the output contract. Not below-PATCH tweaks.
- **Bump** PATCH for a fix, MINOR for a backward-compatible addition, MAJOR for a breaking change. Update the Current Version line with every entry.
- **4-entry cap** per section; a fifth drops the oldest.

---

## Major Updates

> Breaking changes, restructured pipeline, incompatible output. Most recent 4 entries.

### `01.00.00` - 2026-07-03

Initial build of the identify skill: coverage-driven Profile interviewing. The engine's read-only `profile coverage` subcommand picks the target facet; the skill embodies Adeline (UX and Design Research Lead) to run a mixed-delivery interview from validated frameworks, dispatches Calvin (Writer) to compose the provenance-marked proposal batch and Sterling (Standards Reviewer) to audit it blind against Article IV, and writes only what the user approves, line-item capable, through the engine write path.

## Minor Updates

> Backward-compatible additions. Most recent 4 entries.

_None yet._

## Patch Updates

> Fixes and clarifications. Most recent 4 entries.

### `01.00.01` - 2026-10-19

Rewired the pipeline to the vault's scripts: `.github/scripts/profile-coverage.py` picks the target facet, a new entry is copied from its `Profile/.template/` file, Memory promotions are written in their destination's format, and `update-vault.py` and `lint-notes.py` close every run. The archive now carries its team, vendored when it is built.

