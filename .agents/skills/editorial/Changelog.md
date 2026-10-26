<!--
title: "editorial - Changelog"
description: "Change history for the editorial skill, the BRAIN's writing, editing, and formatting orchestrator."
type: "record"
keywords: ["version history", "release notes", "editorial skill changes", "revision log"]
-->

# 📋 editorial Changelog

## Current Version

**`1.7.0`**

The version is SemVer, per standards' [versioning policy](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Releases-&-Versioning.md#-versioning-policy-semver). It matches `metadata.version` in `SKILL.md`, and `check-skills.py` fails when they differ. Each section shows the 4 most recent entries; older entries age out. Newest on top.

---

## How This File Works

- **Tracks** changes to how editorial works: tiers, the dispatch wiring, references, templates, assets, the formatting and voice doctrine, the quality gate. Not below-PATCH tweaks.
- **Bump** the version by standards' [versioning policy](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Releases-&-Versioning.md#-versioning-policy-semver), and update the Current Version line with every entry.
- **4-entry cap** per section; a fifth drops the oldest.

---

## Major Updates

> Breaking changes, restructured tiers, incompatible output. Most recent 4 entries.

_None yet._

---

## Minor Updates

> New tier behavior, new references, new templates or assets. Most recent 4 entries.

### `1.7.0` - 2026-10-26

The Editorial team now ships inside the skill, in `agents/`, instead of living in `Inbox/Faculties/Editorial/`, and the skill source moved from `System/Skills/.unpackaged/` to `.agents/skills/`, where the agent apps read a repository's skills, so the vault's own sessions load it and tannergolden/intelligence's home kit can carry it to every repository. Briefs read each spec from `<skill>/agents/`, and every reference to the team's old folder points at `agents/`, which holds the team alone. A new **Where it runs** rule: in a vault, the vault's own copy runs, so a home copy hands over to it; anywhere else the voice comes from the user's own writing at hand. `allowed-tools` now pre-approves read-only tools only, and the frontmatter keeps one key to a line, as the home kit's reader requires. The description is now quoted: unquoted, its colon made the frontmatter invalid YAML, so a loader dropped the description and the skill could never trigger.

### `1.6.0` - 2026-10-19

- Vault notes are GitHub-Flavored Markdown with wikilinks, the vault's move off Obsidian: `references/formatting.md` and `SKILL.md` make it the default for every vault file and for a markdown target leaving the vault, and wikilinks never leave the notes.
- Callouts are GitHub's five uppercase alerts, titled by a bold lead-in, and a collapsible `<details>` block replaces folding as the density tool. `references/admonitions.md` and `assets/callout-types.json` keep Obsidian's full set for a target that renders it.
- The precedence and the exit gate name the hidden frontmatter in `.docs/vault/Note-Schema.md`, and every callout in the skill's references and templates is one of the five.

### `1.5.0` - 2026-06-28

Restructured `SKILL.md` to develop's canonical skeleton, the standard every skill now mirrors (`develop` `references/architecture.md`): the operational table first (Tiers), then the team it dispatches, how a piece is made (intake Phase 0, the destination rule, the Line Editor gate, editing in place), dispatch scaling, formatting and beauty, voice, conformance with the live BRAIN, quality bars, and boundaries. No behavior change: every prior rule is preserved and reordered, the granular sections (the beauty principle, voice, the structural trigger scope, editing essentials, the BRAIN-aware contract) are folded into the spine, and the quality non-negotiables are consolidated into a Quality bars list. The 986-character description, the tier table, and every reference pointer are unchanged.

### `1.4.0` - 2026-06-25

External writing help (a piece the user will send or use outside the vault: write me an email, rewrite this, proofread this, reply to this, soften this) is now **first-class**, and an **understand-the-situation intake phase** runs before drafting. New `references/intake.md` is the understand-first method: the **situation read** (the rhetorical checks of goal, audience and relationship and power, the one key message, and constraints, plus a sentiment read of the clustered tone cues), the **sentiment-and-tone calibration** rule (mirror the register, never the emotion: converge on warmth and formality, diverge from anger and panic, hold calm-warm-firm, with the NVC frame for charged replies), the **elicitation rule** (ask at most 1 to 3 questions, only when a different answer would change the draft and a wrong guess is costly to undo, else draft on stated assumptions; batch once; check Profile and memory first), and the **situation-brief spine** (the fields the lead captures, each with a default). The lead runs this as Phase 0 and threads a **situation brief** into every dispatch so the Writer drafts to it and the Line Editor gates against it. Added `references/difficult-messages.md` (the bad-news, apology, refusal, complaint and recovery, and de-escalation playbook) and `templates/situation-brief.md` (the scaffold the lead fills). Clarified in `SKILL.md` that a leaving piece goes to the user and is governed by the destination's own format, so the vault preflight and lint exit gate do not apply to it, though clarity and the slop rubric still do. Made intake Phase 0 in `references/tiers-and-dispatch.md` and updated the self-contained-brief contract to carry the situation brief. Intake is a **formalized lead responsibility, not a new team seat** (no roster change). Built from a deep four-lane research run: the rhetorical situation, sentiment and communication-accommodation theory, difficult-message frameworks, and intake-brief practice.

---

## Patch Updates

> Fixes, wording, reference tweaks. Most recent 4 entries.

### `1.5.2` - 2026-10-19

- References point at `AGENTS.md`, the folder notes' Rules and `.docs/vault/` instead of the retired root rule files.
- The licence is MIT. The slop rubric points at standards' Plain Words list instead of copying it, and WebFetch joins the tools so the lead can read the list at its link; a page GitHub renders follows standards' Document Styling guide while a vault note keeps `AGENTS.md`, and the versioning rules link to standards.
- Versions are plain SemVer: `01.05.01` is now `1.5.1`.

### `1.5.1` - 2026-10-19

Moved the preflight and the exit gate off the retired engine: an edit in place starts from a committed state, `.github/scripts/lint-notes.py` is the exit gate, and `update-vault.py` and `check-vault.py` replace `sync` and `health`. The archive now carries the Editorial team, vendored when it is built.

### `1.4.2` - 2026-06-27

Expanded the 9.7 alignment to name GitHub's full set of recognized markdown files, not only README. `references/formatting.md` and `SKILL.md` now list the repository and community-health files GitHub renders in its web interface, `README.md`, `LICENSE.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SECURITY.md`, `SUPPORT.md`, `GOVERNANCE.md`, and the issue and pull-request templates, as the only place GitHub-Flavored Markdown is in bounds. Verified against GitHub's community-health-files documentation.

### `1.4.1` - 2026-06-27

Aligned the formatting doctrine to new Constitution rule 9.7 (Obsidian-Compatible Markdown by Default). `references/formatting.md` and `SKILL.md` now state it explicitly: markdown is Obsidian-compatible by default (CommonMark plus Obsidian-Flavored Markdown), and GitHub-Flavored Markdown, including the five uppercase NOTE/TIP/IMPORTANT/WARNING/CAUTION alerts, is reserved for a primary repository file that renders on GitHub (a README and its kind), not for ordinary leaving-the-vault markdown. The precedence callout and the GitHub-five note cite 9.7.
