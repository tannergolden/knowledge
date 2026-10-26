<!--
title: "research - Changelog"
description: "Change history for the research skill, the BRAIN's depth-scaled multi-source research orchestrator."
type: "record"
keywords: ["version history", "release notes", "research skill changes", "revision log"]
-->

# research Changelog

## Current Version

**`1.6.0`**

The version is SemVer, per standards' [versioning policy](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Releases-&-Versioning.md#-versioning-policy-semver). It matches `metadata.version` in `SKILL.md`, and `check-skills.py` fails when they differ. Each section shows the 4 most recent entries; older entries age out. Newest on top.

---

## How This File Works

- **Tracks** changes to how research works: tiers, the dispatch wiring, references, templates, the output and freshness contract. Not below-PATCH tweaks.
- **Bump** the version by standards' [versioning policy](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Releases-&-Versioning.md#-versioning-policy-semver), and update the Current Version line with every entry.
- **4-entry cap** per section; a fifth drops the oldest.

---

## Major Updates

> Breaking changes, restructured tiers, incompatible output. Most recent 4 entries.

_None yet._

---

## Minor Updates

> New tier behavior, new references, new by-demand seats. Most recent 4 entries.

### `1.6.0` - 2026-10-26

The Research team now ships inside the skill, in `agents/`, instead of living in `Inbox/Faculties/Research/`, and the skill source moved from `System/Skills/.unpackaged/` to `.agents/skills/`, where the agent apps read a repository's skills, so the vault's own sessions finally load it and tannergolden/intelligence's home kit can carry it to every repository. Briefs read each spec from `<skill>/agents/`. A new **Where it runs** rule: in a vault, the vault's own copy runs, so a home copy hands over to it; anywhere else the run skips the Step-0 dedup and the Librarian and delivers in chat. `allowed-tools` now pre-approves read-only tools only, and the frontmatter keeps one key to a line, as the home kit's reader requires.

### `1.5.0` - 2026-06-28

Added the `kb read` step to local grounding and tightened the knowledge-base doctrine. `brain.command` gained a `kb read "article"` command (full article text by title or path, with a citation line) and now rejects unknown flags on `kb search`; the grounding step and the Librarian use `kb search` to find an article then `kb read` to fetch and read its body, so a knowledge-base finding is fetched and read, not snippet-guessed. `references/methodology.md` adds: single-source grounding downgrades confidence and corroborates; the web-escalation triggers (current events, post-snapshot facts, primary research, non-English, specialized depth); and intra-source contradictions are surfaced like cross-source ones. Output gains a learn-loop: when grounding finds no curated `Library/` note on a durable topic, offer to promote the synthesis for the Librarian to catalog.

### `1.4.0` - 2026-06-28

Wired the Section 4.5 retrieval order (vault, then knowledge bases, then the web) into the pipeline. A new local-grounding step dispatches the **Librarian** (Marian, homed in `Library/`) to search the curated `Library/` notes and the offline knowledge bases (`brain.command kb search` across `Library/Reference & Encyclopedia/`) before any web fan-out; a question the Library and the knowledge bases fully answer is synthesized with no web run, and the fan-out covers only the gaps and currency. `SKILL.md` gains the grounding step, the Librarian as a cross-home dispatch seat, and a ground-locally-before-the-web doctrine bullet; `references/methodology.md` gains the retrieval-order section. The Librarian agent (`Library/★ Librarian.md`) now understands the whole Library, the Reference & Encyclopedia knowledge bases, and the reverse handoff: Research dispatches it to ground a run, and it returns findings and gaps, never conclusions.

### `1.3.0` - 2026-06-28

Restructured `SKILL.md` to develop's canonical skeleton, the standard every skill mirrors (`develop` `references/architecture.md`): Tiers, the team it dispatches, a new **How a run works** pipeline section (the frame, Step-0, lanes, fan-out, blind-verify, synthesize flow that was previously implicit across the tier table and the doctrine), dispatch scaling, output and freshness, the BRAIN preflight conformance, the doctrine that never bends (the quality bars), and boundaries. The reorder puts conformance before the quality doctrine to match the spine. No rule changed: every prior section is preserved, only reordered, plus the added pipeline overview. Also aligned the version sites, which had drifted: the namesake (01.01.02) and this Changelog's frontmatter (01.00.00) now version with the skill at 01.03.00.

---

## Patch Updates

> Fixes, wording, reference tweaks. Most recent 4 entries.

### `1.5.3` - 2026-10-19

- A report's three-month window ends on its `review_by` date, since the hidden frontmatter retired `updated` (`references/reporting.md`, `templates/report.md`).

### `1.5.2` - 2026-10-19

- References point at `AGENTS.md` (Start here holds the retrieval order) and the folder notes' Rules instead of the retired root rule files.
- The licence is MIT, and the versioning rules link to tannergolden/standards instead of restating them.
- Versions are plain SemVer: `01.05.01` is now `1.5.1`.

### `1.5.1` - 2026-10-19

Moved local grounding and the preflight off the retired engine: the offline knowledge bases are searched with `.github/scripts/knowledge-base.py` when one is installed, a report overwrite starts from a committed state, and `update-vault.py` and `check-vault.py` replace `sync` and `health`. The archive now carries the Research team, vendored when it is built.

### `1.1.3` - 2026-06-24

Dropped the "Research - " prefix from filed-report naming. A report is now named for its topic alone (`<Topic Title>.md`) and filed in `Inbox/Reports/`; its location, not a prefix, marks it as a report. Updated `references/reporting.md` (the naming rule) and `templates/report.md` (title, path, H1, and the id pattern, now `in-<slug>`). The three existing reports were renamed to match.
