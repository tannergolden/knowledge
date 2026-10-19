---
title: "editorial - Changelog"
description: "Change history for the editorial skill, the BRAIN's writing, editing, and formatting orchestrator."
status: "active"
tags: ["system", "log"]
aliases: []
keywords: ["version history", "release notes", "editorial skill changes", "revision log"]
created: 2026-06-23
updated: 2026-10-19
type: "log"
folder: "system"
layer: 4
policy: false
author: "Tanner Golden"
path: "BRAIN/System/Skills/.unpackaged/editorial/Changelog.md"
id: "sy-skill-editorial-changelog"
---

# 📋 editorial Changelog

## Current Version

**`01.05.01`**

Semantic versioning, `MAJOR.MINOR.PATCH`, two-digit zero-padded segments. This value matches `metadata.version` in `SKILL.md`. Each section shows the 4 most recent entries; older entries age out. Newest on top.

---

## How This File Works

- **Tracks** changes to how editorial works: tiers, the dispatch wiring, references, templates, assets, the formatting and voice doctrine, the quality gate. Not below-PATCH tweaks.
- **Bump** PATCH for a fix, MINOR for a backward-compatible addition, MAJOR for a breaking change. Update the Current Version line with every entry.
- **4-entry cap** per section; a fifth drops the oldest.

---

## Major Updates

> Breaking changes, restructured tiers, incompatible output. Most recent 4 entries.

_None yet._

---

## Minor Updates

> New tier behavior, new references, new templates or assets. Most recent 4 entries.

### `01.05.00` - 2026-06-28

Restructured `SKILL.md` to develop's canonical skeleton, the standard every skill now mirrors (`develop` `references/architecture.md`): the operational table first (Tiers), then the team it dispatches, how a piece is made (intake Phase 0, the destination rule, the Line Editor gate, editing in place), dispatch scaling, formatting and beauty, voice, conformance with the live BRAIN, quality bars, and boundaries. No behavior change: every prior rule is preserved and reordered, the granular sections (the beauty principle, voice, the structural trigger scope, editing essentials, the BRAIN-aware contract) are folded into the spine, and the quality non-negotiables are consolidated into a Quality bars list. The 986-character description, the tier table, and every reference pointer are unchanged.

### `01.04.00` - 2026-06-25

External writing help (a piece the user will send or use outside the vault: write me an email, rewrite this, proofread this, reply to this, soften this) is now **first-class**, and an **understand-the-situation intake phase** runs before drafting. New `references/intake.md` is the understand-first method: the **situation read** (the rhetorical checks of goal, audience and relationship and power, the one key message, and constraints, plus a sentiment read of the clustered tone cues), the **sentiment-and-tone calibration** rule (mirror the register, never the emotion: converge on warmth and formality, diverge from anger and panic, hold calm-warm-firm, with the NVC frame for charged replies), the **elicitation rule** (ask at most 1 to 3 questions, only when a different answer would change the draft and a wrong guess is costly to undo, else draft on stated assumptions; batch once; check Profile and memory first), and the **situation-brief spine** (the fields the lead captures, each with a default). The lead runs this as Phase 0 and threads a **situation brief** into every dispatch so the Writer drafts to it and the Line Editor gates against it. Added `references/difficult-messages.md` (the bad-news, apology, refusal, complaint and recovery, and de-escalation playbook) and `templates/situation-brief.md` (the scaffold the lead fills). Clarified in `SKILL.md` that a leaving piece goes to the user and is governed by the destination's own format, so the vault preflight and lint exit gate do not apply to it, though clarity and the slop rubric still do. Made intake Phase 0 in `references/tiers-and-dispatch.md` and updated the self-contained-brief contract to carry the situation brief. Intake is a **formalized lead responsibility, not a new team seat** (no roster change). Built from a deep four-lane research run: the rhetorical situation, sentiment and communication-accommodation theory, difficult-message frameworks, and intake-brief practice.

### `01.03.00` - 2026-06-25

Split the combined correspondence reference into two by medium. The former `references/email-and-messages.md` became `references/email.md` (the furniture-bearing genres: the medium-branch table, bottom-line-up-front email, the Field/Tenor/Mode register theory and Joos's five-rung ladder, the greeting-and-sign-off map, formal letters, and the Writing-for-HTML-email section) and `references/messages.md` (the no-furniture chat genre: one thought delivered plain, no subject or salutation or sign-off, the keep-it-light register rule, and a pointer to `references/messaging-formats.md` for the per-platform syntax). Repointed the three referencing files to the new names (`references/voice.md`, `templates/email.md`, `templates/message.md`); each new reference keeps the plain-H1, no-frontmatter shape.

### `01.02.00` - 2026-06-24

Added two on-demand format references for non-Markdown destinations, both built from primary-source-verified research (RFCs 5322/3676/1849 and each platform's own docs). New `references/plain-text.md` covers true plain text (`.txt`, plain-text email or messages): the no-Markdown-into-raw-text footgun and bare URLs, line wrapping near 72 with the 998 SMTP hard limit, format=flowed soft breaks and space-stuffing (MIME-email-scoped), the `-- ` signature delimiter with its load-bearing trailing space, structure without markup, the ambiguous asterisk/underscore emphasis caveat, and `>` reply quoting. New `references/messaging-formats.md` is the per-platform chat-dialect matrix (Slack, Discord, WhatsApp, Telegram, Teams, iMessage/SMS/RCS, Reddit) leading with a side-by-side table, then the footguns: single-versus-double emphasis chars, the link-form split, Telegram MarkdownV2 escaping, heading and strikethrough variance, and the plain-text-only messaging platforms; scoped to text markup, not Block Kit / Adaptive Cards / bot payloads. Folded a "Writing for HTML email" section into `references/email-and-messages.md` (the mandatory plain-text twin, image-blocking-aware copy, the markdown-paste caveat, and a refer-out pointer for hand-built HTML). Added an other-markup pointer to `references/formatting.md` (match the target's native syntax; the glyphs collide; verify at the source). Added both new references to the `SKILL.md` pointer line and bumped `metadata.version` to match. Evaluated and excluded the out-of-scope formats: Word, PDF, PowerPoint, and Excel (their own BRAIN skills), structured data, code, full LaTeX and Typst, and subtitles.

---

## Patch Updates

> Fixes, wording, reference tweaks. Most recent 4 entries.

### `01.05.01` - 2026-10-19

Moved the preflight and the exit gate off the retired engine: an edit in place starts from a committed state, `.github/scripts/lint-notes.py` is the exit gate, and `update-vault.py` and `check-vault.py` replace `sync` and `health`. The archive now carries the Editorial team, vendored when it is built.

### `01.04.02` - 2026-06-27

Expanded the 9.7 alignment to name GitHub's full set of recognized markdown files, not only README. `references/formatting.md` and `SKILL.md` now list the repository and community-health files GitHub renders in its web interface, `README.md`, `LICENSE.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SECURITY.md`, `SUPPORT.md`, `GOVERNANCE.md`, and the issue and pull-request templates, as the only place GitHub-Flavored Markdown is in bounds. Verified against GitHub's community-health-files documentation.

### `01.04.01` - 2026-06-27

Aligned the formatting doctrine to new Constitution rule 9.7 (Obsidian-Compatible Markdown by Default). `references/formatting.md` and `SKILL.md` now state it explicitly: markdown is Obsidian-compatible by default (CommonMark plus Obsidian-Flavored Markdown), and GitHub-Flavored Markdown, including the five uppercase NOTE/TIP/IMPORTANT/WARNING/CAUTION alerts, is reserved for a primary repository file that renders on GitHub (a README and its kind), not for ordinary leaving-the-vault markdown. The precedence callout and the GitHub-five note cite 9.7.

### `01.01.01` - 2026-06-24

Verified the markdown and admonition references against primary sources (CommonMark 0.31.2, the frozen GFM spec, the GitHub alerts doc, and the Obsidian Help Callouts and Advanced-formatting pages) with a deep research run: five analysts, a fact-checker, and a devil's advocate. The callout type and alias set matched the live Obsidian doc exactly, and no factual error was found in any Obsidian or portability claim. Applied a small set of anti-footgun corrections rather than spec-completeness padding: in `references/markdown-reference.md`, named the backslash CommonMark hard break and corrected the hard-break portability note, flagged that MathJax renders a LaTeX subset (not full LaTeX), that a table cell takes no line break (use a break tag), and that Obsidian has no native code line-highlighting; in `references/admonitions.md`, that every callout body line needs its own quote marker and a pipe still escapes inside a callout table; in `references/formatting.md`, that vault frontmatter and tags follow the Instructions Section 8 schema and the Article VII vocabulary, not freeform Obsidian properties. Held the signal-scarcity doctrine: deferred the spec-coverage gaps (Setext and indented code, reference-link variants, properties and block-id syntax, wikilink and embed sub-forms) to the vault Markdown Style Guide rather than bloat the references.

