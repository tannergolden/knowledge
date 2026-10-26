<!--
title: "discover - Changelog"
description: "Change history for the discover skill."
type: "record"
keywords: ["version history", "release notes", "discover changes", "revision log"]
-->
# discover Changelog

## Current Version

**`1.1.0`**

The version is SemVer, per standards' [versioning policy](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Releases-&-Versioning.md#-versioning-policy-semver). It matches `metadata.version` in `SKILL.md`, and `check-skills.py` fails when they differ. Each section shows the 4 most recent entries; older entries age out. Newest on top.

---

## How This File Works

- **Tracks** changes to how the skill works: tiers, the team, references, templates, the output contract. Not below-PATCH tweaks.
- **Bump** the version by standards' [versioning policy](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Releases-&-Versioning.md#-versioning-policy-semver), and update the Current Version line with every entry.
- **4-entry cap** per section; a fifth drops the oldest.

---

## Major Updates

> Breaking changes, restructured pipeline, incompatible output. Most recent 4 entries.

### `1.0.0` - 2026-06-28

Initial build of the discover skill: the BRAIN's ideation skill, dispatching the standing Discovery team (Sebastian's crew) to generate ideas wide then converge to a ranked shortlist by pairwise Elo tournament, to the standard generate wide, select fair. Idea records file to the new held idea pool at Inbox/Ideas/. Grounded in a research pass on ideation method (Osborn, CPS, the Double Diamond, the Diehl and Stroebe productivity evidence, Bradley-Terry and Elo, ICE and RICE, the de Bono and SCAMPER lenses, and the how-might-we briefing craft).

## Minor Updates

> Backward-compatible additions. Most recent 4 entries.

### `1.1.0` - 2026-10-26

The Discovery team now ships inside the skill, in `agents/`, instead of living in `Inbox/Faculties/Discovery/`, and the skill source moved from `System/Skills/.unpackaged/` to `.agents/skills/`, where the agent apps read a repository's skills, so the vault's own sessions load it and tannergolden/intelligence's home kit can carry it to every repository. The Idea Curator reads the idea schema from the roster beside it. A new **Where it runs** rule: in a vault, the vault's own copy runs, so a home copy hands over to it; anywhere else the idea pool stays in the conversation. `allowed-tools` now pre-approves read-only tools only, and the frontmatter keeps one key to a line, as the home kit's reader requires. The description is now quoted: unquoted, its colon made the frontmatter invalid YAML, so a loader dropped the description and the skill could never trigger.

## Patch Updates

> Fixes and clarifications. Most recent 4 entries.

### `1.0.3` - 2026-10-19

- An idea record's stage is its `lifecycle` field, not `status`, which stays the standard frontmatter's (`references/brief.md`).

### `1.0.2` - 2026-10-19

- References point at `AGENTS.md`, the folder notes' Rules and `.docs/vault/` instead of the retired root rule files.
- The licence is MIT, and the versioning rules link to tannergolden/standards instead of restating them.
- Versions are plain SemVer: `01.00.01` is now `1.0.1`.

### `1.0.1` - 2026-10-19

Moved the preflight off the retired engine: an existing file's last state is committed before an edit, since git history is the backup. The archive now carries the Discovery team, vendored when it is built.

<!-- This is a BRAIN documentation node: it carries the vault's note schema above
     (.docs/technical/vault/Note-Schema.md), not the Agent Skills schema. -->
