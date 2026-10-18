---
title: "research - Changelog"
description: "Change history for the research skill, the BRAIN's depth-scaled multi-source research orchestrator."
status: "active"
tags: ["system", "log"]
aliases: []
keywords: ["version history", "release notes", "research skill changes", "revision log"]
created: 2026-06-22
updated: 2026-06-28
type: "log"
folder: "system"
layer: 4
policy: false
version: "01.05.00"
author: "Tanner Golden"
path: "BRAIN/System/Skills/.unpackaged/research/Changelog.md"
id: "sy-skill-research-changelog"
---

# research Changelog

## Current Version

**`01.05.00`**

Semantic versioning, `MAJOR.MINOR.PATCH`, two-digit zero-padded segments. This value matches `metadata.version` in `SKILL.md`. Each section shows the 4 most recent entries; older entries age out. Newest on top.

---

## How This File Works

- **Tracks** changes to how research works: tiers, the dispatch wiring, references, templates, the output and freshness contract. Not below-PATCH tweaks.
- **Bump** PATCH for a fix, MINOR for a backward-compatible addition, MAJOR for a breaking change. Update the Current Version line with every entry.
- **4-entry cap** per section; a fifth drops the oldest.

---

## Major Updates

> Breaking changes, restructured tiers, incompatible output. Most recent 4 entries.

_None yet._

---

## Minor Updates

> New tier behavior, new references, new by-demand seats. Most recent 4 entries.

### `01.05.00` - 2026-06-28

Added the `kb read` step to local grounding and tightened the knowledge-base doctrine. `brain.command` gained a `kb read "article"` command (full article text by title or path, with a citation line) and now rejects unknown flags on `kb search`; the grounding step and the Librarian use `kb search` to find an article then `kb read` to fetch and read its body, so a knowledge-base finding is fetched and read, not snippet-guessed. `references/methodology.md` adds: single-source grounding downgrades confidence and corroborates; the web-escalation triggers (current events, post-snapshot facts, primary research, non-English, specialized depth); and intra-source contradictions are surfaced like cross-source ones. Output gains a learn-loop: when grounding finds no curated `Library/` note on a durable topic, offer to promote the synthesis for the Librarian to catalog.

### `01.04.00` - 2026-06-28

Wired the Section 4.5 retrieval order (vault, then knowledge bases, then the web) into the pipeline. A new local-grounding step dispatches the **Librarian** (Marian, homed in `Library/`) to search the curated `Library/` notes and the offline knowledge bases (`brain.command kb search` across `Library/Reference & Encyclopedia/`) before any web fan-out; a question the Library and the knowledge bases fully answer is synthesized with no web run, and the fan-out covers only the gaps and currency. `SKILL.md` gains the grounding step, the Librarian as a cross-home dispatch seat, and a ground-locally-before-the-web doctrine bullet; `references/methodology.md` gains the retrieval-order section. The Librarian agent (`Library/★ Librarian.md`) now understands the whole Library, the Reference & Encyclopedia knowledge bases, and the reverse handoff: Research dispatches it to ground a run, and it returns findings and gaps, never conclusions.

### `01.03.00` - 2026-06-28

Restructured `SKILL.md` to develop's canonical skeleton, the standard every skill mirrors (`develop` `references/architecture.md`): Tiers, the team it dispatches, a new **How a run works** pipeline section (the frame, Step-0, lanes, fan-out, blind-verify, synthesize flow that was previously implicit across the tier table and the doctrine), dispatch scaling, output and freshness, the BRAIN preflight conformance, the doctrine that never bends (the quality bars), and boundaries. The reorder puts conformance before the quality doctrine to match the spine. No rule changed: every prior section is preserved, only reordered, plus the added pipeline overview. Also aligned the version sites, which had drifted: the namesake (01.01.02) and this Changelog's frontmatter (01.00.00) now version with the skill at 01.03.00.

### `01.02.00` - 2026-06-25

Reversed the reports-are-never-referenced rule: `Inbox/Reports/Reports.md` is now the single index that wikilinks every held report, and filing a report adds its entry to that index in the same edit (refresh updates it, clear removes it). No other file links to a report, so the wider graph stays free of disposable nodes, and durable findings are still promoted out. Updated `references/reporting.md` (the index rule plus the filing step), `SKILL.md` (the output contract and the one wikilink exception), and `templates/report.md` (the body still carries no inline wikilinks; the index entry is the only link). The team doc `Inbox/Faculties/Research/Research.md`, the namesake `Inbox/Reports/Reports.md`, and `Inbox/Inbox.md` were updated to match, and the five existing reports were backfilled into the index.

---

## Patch Updates

> Fixes, wording, reference tweaks. Most recent 4 entries.

### `01.01.03` - 2026-06-24

Dropped the "Research - " prefix from filed-report naming. A report is now named for its topic alone (`<Topic Title>.md`) and filed in `Inbox/Reports/`; its location, not a prefix, marks it as a report. Updated `references/reporting.md` (the naming rule) and `templates/report.md` (title, path, H1, and the id pattern, now `in-<slug>`). The three existing reports were renamed to match.

### `01.01.02` - 2026-06-23

Fixed the filed-report template (`templates/report.md`) to match the live BRAIN reports convention proven by the held reports in `Inbox/Reports/`: `type` is now `reference` (the prior `report` is outside the closed File Role vocabulary in Constitution Article VII and would fail `lint`), `tags` are `["inbox", "reference", "current"]`, and the `id` pattern is `in-research-<slug>` to match filed reports. No change to the research flow; a report filed from this template now lints clean.

### `01.01.01` - 2026-06-22

Audit-and-fix pass: four independent reviewers (consistency, skill-to-team fidelity, executability, leanness and SOTA) found, and this fixed, every real gap. Removed the last write-not-return contradiction (the lane-brief template said the Analyst writes a file) and the stale "filesystem is the artifact bus" line in SKILL.md; corrected the Information Specialist's tier (deep only) and the Editor's return contract in `roster.md`; reconciled the two-axis model to likelihood-and-confidence throughout, and gave the Bottom Line its second axis and `source-strategy.md` its missing ladder tiers. Executability: defined the workspace-create step and slug, the `draft.md` shape (the report sections), the REVISE loop, the Statistician joining the blind message, a blind-reviewer brief example, and a context-compaction rule. SOTA: added the CONTRADICTED Fact-Checker verdict and claim-to-passage logging (mirrored into the Search Peer-Reviewer and Fact-Checker agent specs), and made the URL-resolve a hard stop step. Trimmed duplicated 15x-cost, zero-bias, blind-review, and Step-0 statements to single sources, and refreshed the namesake. Re-verified by the validator, a scoped QA re-audit, and health.

### `01.00.01` - 2026-06-22

Hardening pass, proven by a real test-drive and an adversarial SOTA red-team. Fixed the stale "13-agent" count (the team is 10). Closed the executability gaps the test-drive hit: defined the run workspace path and the lane -> draft -> blind-review artifact flow in `dispatch.md` (resolving the persists-nothing vs artifact-bus contradiction), added the Search Peer-Reviewer sentinel check and PASS/REVISE routing, the lead-filename and apostrophe caveats, the untrusted-input boundary in the brief, and the verbatim-question handoff. Propagated worker-facing SOTA the red-team found stranded in `methodology.md`: saturation, the echo/independence rule, and source-tier tagging now live in `lane-brief.md`; added PRISMA-S negative-result recording, breadth-vs-depth search guidance, a two-axis render example, and the name-the-falsifier rule. Made the URL-resolve check a shipping step and added the fixed chat-synthesis shape to `reporting.md`, defined topic canonicalization, and stated the fan-out's defended boundary (the data-processing-inequality result) in `tiers.md`. Softened the ask-tool phrasing to "structured ask tool when available, otherwise in chat".
