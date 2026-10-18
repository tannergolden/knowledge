---
title: BRAIN Changelog
description: Versioned change history for the BRAIN system. Semantic versioning (MAJOR.MINOR.PATCH). Each section caps at the most recent 4 entries.
status: active
tags:
  - system
  - log
aliases: []
keywords:
  - change history
  - semantic versioning
  - version history
  - release notes
  - what changed
  - system updates
  - revision log
created: 2026-05-19
updated: 2026-07-05
type: log
folder: system
layer: 1
policy: true
version: "01.00.19"
author: Tanner Golden
path: BRAIN/System/changelog.md
id: sy-changelog
---

# BRAIN Changelog

## Current Version

**`40.09.00`**

The version format is `MAJOR.MINOR.PATCH`, two-digit zero-padded segments.

---

## How the AI Works This File

> **This is your operating manual for `changelog.md`.** Read this section before logging any change. Misclassifying or skipping entries breaks the version history.

### What the Changelog Tracks

**The changelog records changes to how the BRAIN works, not changes to what's in it.**

Eligible changes are any **additions, modifications, deletions, renames, or restructures of core BRAIN files**. Adding content to the BRAIN - no matter how much - is never a changelog entry on its own.

**Core BRAIN files (eligible for logging - additions and edits both count):**

- `Constitution.md`, `Instructions.md`, root `Information.md`
- Any folder documentation file (the folder-named doc, e.g. `Memory.md`, `Library.md`; formerly `Information.md`) and the root `Information.md` - these define folder/system scope and rules
- All files in `System/` (`brain.command`, `clean-pdf.command`, `changelog.md`, scripts, configuration files)
- All files in any `.template/` folder (they define the shape of future content)
- The folder structure itself (creating, renaming, deleting, or restructuring folders)
- The tagging system, type enum, frontmatter schema, and any other system-level vocabulary

**Not eligible for logging (content, not system):**

- Files placed into `Library/` subfolders (a book, recipe, reference document)
- Entries added to `Memory/` files (Log entries, learned facts, decisions, observed patterns)
- New project folders inside `Projects/` instantiated from the template (creating a project from the template is content)
- New venture folders inside `Ventures/` instantiated from the template (same)
- Personal information filled into `Profile/` files (the user's actual biography, preferences, values)
- Inbox sorting (routing files is content management)

The distinguishing test: *"Did this change how the BRAIN works for any future content, or did it just add/edit content the BRAIN holds?"* Only the former is logged. Note that creating, editing, or restructuring a core file (including adding a brand-new core file like a new `Information.md`, a new template, or a new system script) is always eligible - that's a change to how the BRAIN works.

### When to Log an Entry

A change to a core BRAIN file is logged **only if it meets the PATCH threshold or larger**. Below-PATCH changes are not logged.

| Threshold | Examples (core files only) |
|-----------|----------|
| **Below PATCH (do NOT log)** | Typo fixes, whitespace cleanup, single-word adjustments, formatting tweaks with no semantic impact, `updated` field bumps with no other changes |
| **PATCH (log + bump patch)** | Core file content edits, tag-system migrations on existing files, scaffolding documentation tweaks, script bug fixes, retention table changes on core files, single core-folder rename, backup cleanup |
| **MINOR (log + bump minor, reset patch)** | New Layer 3+ structural folders (e.g., a new Library category), new content-tag families, new file roles within an existing dimension, significant additions to existing scaffolding documentation, new optional script command |
| **MAJOR (log + bump major, reset minor + patch)** | Constitution amendments, Layer 0/1 changes (any), file format breaking changes, removal of an entire category or dimension, fundamental tagging-system shifts, anything that requires migrating existing files |

If a change spans multiple thresholds, log it at the highest threshold reached.

### How to Classify Borderline Changes

When uncertain whether a change is PATCH vs. MINOR vs. MAJOR:

1. **Does it require migrating existing files to remain valid?** → MAJOR
2. **Does it add a new category, folder, dimension, or controlled-vocabulary value?** → MINOR
3. **Does it change behavior or content without forcing migration or adding new structure?** → PATCH
4. **None of the above** → don't log

### How to Bump the Version

From the current version, the next version is:

- **PATCH change**: `01.00.00` → `01.00.01` → `01.00.02` → ... → `01.00.04` → `01.00.05` (no rollover at the cap; the 4-entry limit applies to *displayed entries*, not the version number)
- **MINOR change**: bump minor, reset patch. `01.00.07` → `01.01.00`
- **MAJOR change**: bump major, reset minor and patch. `01.05.12` → `02.00.00`

Update the `Current Version` line at the top of this file with every entry.

### How to Format an Entry

Add the new entry at the **top** of its section (most recent first). Format:

```
### `XX.XX.XX` - YYYY-MM-DD

Short description of the change. One or two sentences. Reference the file(s) affected and the backup name if applicable.
```

Optional fields after the description (use sparingly):

- **Files affected:** comma-separated relative paths
- **Backup:** backup filename in `System/State/.backups/`
- **Refs:** Constitution articles, Instructions sections, or other anchor points

### The 4-Entry Cap (Per Section)

Each of the three sections (Major Updates, Minor Updates, Patch Updates) holds at most **the 4 most recent entries**. When adding entry #5 to a section, the oldest entry in that section is removed.

Do not migrate aged-out entries to an archive file. The cap is hard; aged-out entries are gone. If a deeper history is ever needed, the backups in `System/State/.backups/` and the git history (if the BRAIN is under version control) hold it.

### When the AI Updates This File

1. Recognize that a change has just been made that meets the PATCH threshold or larger
2. Classify the change (PATCH / MINOR / MAJOR)
3. Compute the new version number using the bumping rule
4. Update the `Current Version` line at the top
5. Add the new entry at the top of the appropriate section
6. If the section now has 5 entries, delete the bottom (oldest) entry
7. Update the file's `updated` frontmatter to today
8. Tell the user the version was bumped and what entry was added

### What This File Is Not

- Not a session log. Use `Memory/Log.md` for session-level observations.
- Not a backup or archive. Use `System/State/.backups/` for file snapshots.
- Not a project tracker. Use the `Projects/` folders for personal projects.
- Not a venture log. Use `Ventures/[Company]/Log.md` for venture history.

---

## Major Updates

> Breaking changes, Constitution amendments, Layer 0/1 restructures, dimension-level tagging shifts. Most recent 4 entries.

### `40.00.00` - 2026-06-29

Rebuilt the venture system end to end so a workforce of agents can found, operate, scale, and maintain real companies. (1) Expanded Agent Resources (AR) into a full Fortune 500 organization: 46 new agents (90 total) across 18 departments, splitting Sales & Revenue from Marketing under a new Chief Revenue Officer, adding the missing chiefs (CTO, CISO, Chief Risk Officer, Chief Audit Executive, Chief Data Officer, Chief Product Officer) and deeper specialist seats, retitling the department heads to the C-suite, and adding a board-and-committee governance layer; the charter now encodes the sole-writer model (no agent holds Write or Edit; the board skill persists), the independent verifier (Head of Quality), two-tier seniority, and a stage-gated scaling playbook. (2) Upgraded Ventures/.template/ with an Administration executive office (Strategy.md, Decisions.md, Cadence.md), a forward Financial-Model.md, and a Cap-Table.md, and documented the AR-composes/board-writes deliverable model and the id-rewrite-on-copy step (Ventures.md to 01.02.00). (3) Rebuilt the board skill from a decision-only tool into the BRAIN's venture operating system (to 02.00.00): five modes (found, strategize, decide, operate, review) over the AR workforce scaled to the venture's stage, with a venture-context preflight, write-back into the venture folder, a write-gate that gates money, contracts, external comms, deletes, and equity to the Founder, specialist dispatch, and independent verification; added 11 references, 6 templates, and 3 assets, repackaged. Grounded in a deep multi-agent research and audit pass (Fortune 500 structure, function deliverables, the company lifecycle, the operating model, strategy frameworks, metrics, venture creation, governance, AI-operating-system guardrails) and gated by independent QA, security, and integration review. Agent library, skill validator, and health all green.

**Files affected:** Ventures/Agent Resources (AR)/ (46 new agents, 6 new departments, 18 rosters, the charter), System/Data/agent-catalog.json, Ventures/.template/ (Administration/, Finance & Accounting (F&A)/Financial-Model.md and Cap-Table.md), Ventures/Ventures.md, System/Skills/.unpackaged/board/ (SKILL.md, Board.md, Changelog.md, references, templates, assets), System/Skills/board.skill
**Backup:** pre-edit snapshots in System/.backups/

### `39.00.00` - 2026-06-26

Dissolved the System/State/ wrapper at the user's direction: the changelog, the generated Data/ folder, and the backup folders (.backups/ and the ad-hoc Backups/) moved up to System/ directly, and State.md was removed. This reverses the changelog half of the sixteenth amendment and required amending the Constitution (3.6 now points the changelog at System/changelog.md, 3.7 points backups at System/.backups/; Constitution to 01.07.03). brain.command was rewired (the data dir, the changelog reader, the backups dir, the search globs, the help and output strings); Instructions (01.09.04), System.md (01.02.05, now linking changelog.md and Data/Data.md directly), and Data.md (01.00.02) were repathed. Health, lint, links, and selftest all green.

**Files affected:** Constitution.md, Instructions.md, System/System.md, System/changelog.md, System/Data/Data.md, System/brain.command

### `38.00.00` - 2026-06-19

Migrated the identity layer: replaced the flat Identity/ folder with the faceted Profile/ folder (AI-designed self-model: Biography, Personality, Values, Goals, Skills, Preferences, Working Style, Health, plus the dynamic Focus; 18 docs; a strict superset of the former Identity/ in both structure and research-grade scaffold detail - BFI-2 15-facet table, McAdams narrative themes, Schwartz values, per-domain expertise map, isolated sensitive entries, standardized provenance vocabulary). Identity/ was soft-removed to .trash (recoverable; full backup retained). brain.command: _top_folder now maps the Profile/ path segment to the identity Folder tag (tag unchanged, ids keep id-), STARTUP_PATHS loads Profile/Working Style.md, and the folder bundle, promotion hints, and menu point at Profile/. Constitution: Article IV (Delegated) now hosted in Profile/Profile.md, references in 2.7/4.4/5.x/7.5 repointed, and an Article VII amendment logged (folder renamed Identity->Profile, identity tag retained). Instructions and all cross-referencing folder docs (Memory, Library, Ventures, Projects, System, Information) updated. The /identify skill SOURCE rewired to the 9 facets (file-map, coverage-report.py nested facets, SKILL/Identify/agent paths); the packaged identify.skill needs a /develop repackage to activate at runtime. Backup: System/State/.backups/pre-profile-migration-20260619-143155.

**Files affected:** Profile/, Identity/ (trashed), System/brain.command, Constitution.md, Instructions.md, identify skill

### `37.00.00` - 2026-06-19

Replaced the Library/ and Memory/ Layer-1 folders with AI-designed versions and rewired the memory engine to match. Library/ is now a universal reference library on a 10-class Dewey/UDC-lineage scheme (Information & Computing, Philosophy & Mind, Religion & Spirituality, Society & Social Sciences, Science & Mathematics, Technology & Applied Science, Arts & Recreation, Language & Literature, History & Geography, Life & Practice), plain-name folders with a faceted slash-namespaced keyword catalog, boundary-rulings and worked-examples routing in Library.md, and a namesake doc in every one of its 92 division folders (107 docs total). Memory/ is now organized by cognitive memory type: Log (working), Context (episodic session summaries, tiered Current/Recent/Archive), Events (atomic dated events), Entities (semantic: People/Organizations/Places), Decisions and Insights (reflective), Dates (prospective), with capture-time importance 1-5, recency+importance+relevance retrieval scoring, reflection cadence, and bitemporal As-of/Recorded provenance (22 docs). Rewired brain.command memory engine: MEMORY_COLLECTIONS now covers People/Organizations/Places under Entities plus Events and Insights, with nested-folder layer/path computation and broadened memory add|rm kinds (person|organization|place|decision|event|insight); MEMORY_TIERS/Context kept compatible. Updated Instructions.md (structure tree, Layer-2/3 examples, Library catalog row, Entities/People paths, memory add kinds) and Constitution.md (Article 5.6 repo-docs path, Article VII path examples, 7.3 Entities/People example), preserving historical amendment entries verbatim. Added the startup tag to Memory/Log.md for Section 9 consistency. Full pre-migration tree and per-file backups under System/State/.backups/pre-ai-takeover-20260619-111823/.

**Files affected:** Library/, Memory/, System/brain.command, Instructions.md, Constitution.md

## Minor Updates

> New categories, new folders, new vocabulary values, significant documentation additions. Most recent 4 entries.

### `40.09.00` - 2026-07-05

Added GitHub community-health files, designed for the repo landing page: .github/README.md, CODE_OF_CONDUCT.md, CONTRIBUTING.md, SECURITY.md, and a root MIT LICENSE. Reconciled Constitution 2.6 (no-README rule) with Article 9.7 to carve them out as GitHub presentation infrastructure, exempt from the schema and linter; the engine skips .github/ (dot-dir) and now skips the root LICENSE via SKIP_FILES.

**Files affected:** Constitution.md, System/brain.command

### `40.08.00` - 2026-07-04

Adopt and enforce the AI-Driven Commit Process (Conventional Commits) for vault commits. New engine command commitcheck validates a commit header (<type>(<scope>): <emoji> <summary>, valid type, one emoji, 72 chars or fewer); a tracked System/git-hooks/commit-msg calls it so every commit is checked (install-hooks wires it alongside the pre-push secret guard). The required session trailers live in the body and are unaffected. Bypass a one-off with git commit --no-verify.

**Files affected:** System/brain.command, System/System.md, System/git-hooks/commit-msg

### `40.07.00` - 2026-07-04

Recovery layer now depends on the backup mode (owner direction). New engine detector _remote_backed (cached ls-remote probe, safe-bias to local on doubt): when a git remote is reachable, backup skips the .backups/ pre-edit snapshot (git history is the backstop; backup <path> local forces one) and trash deletes a tracked+clean item with git rm (recoverable via trash restore / git history), keeping the two-stage .trash/ only for what git cannot recover (untracked or uncommitted-modified files) and for local-only vaults. Governance updated: Constitution 3.1 + amendment, Instructions Section 10 + Critical Rules, AGENTS.md, System.md backup/trash rows.

**Files affected:** System/brain.command, Constitution.md, Instructions.md, System/System.md, AGENTS.md

### `40.06.00` - 2026-07-04

Rebuilt and packaged the identify skill (was pending across five passes). Authored its five missing doctrine files (references/question-maps, provenance, roster; templates/interview-plan, proposal-batch) plus assets/trigger-evals.json and regression-cases.jsonl; validates and packages to identify.skill (12 files). Flipped identify from pending to live in Skills.md and the three hook rosters (skill-router, startup-critical, prompt-reminder). All 7 BRAIN skills now packaged and valid.

**Files affected:** System/Skills/Skills.md

## Patch Updates

> File edits, tag migrations, doc tweaks, script bug fixes. Most recent 4 entries.

### `40.08.01` - 2026-07-04

Added the developer's GitHub profile link (github.com/tannergolden) to Information.md's Developer section.

**Files affected:** Information.md

### `40.06.01` - 2026-07-04

Unified the Session Summary template with the engine's summary scaffold: numbered sections 1-6 with Established Foundations / Active Changes / Overrides nested under 2. Current State (they were unnumbered top-level sections), so a hand-filed summary matches one scaffolded by 'summary new' and the real filed summaries.

**Files affected:** Memory/.template/Session Summary.md

### `40.04.01` - 2026-07-04

Reconciled the closed File Role and Folder vocabularies with the engine's authoritative sets: removed the retired 'index' role from Constitution 7.1 and three Instructions enums, added the 'agent' role to the two Instructions enums that omitted it, corrected the folder value 'identity' to 'profile' and the Library id-prefix 'kn-' to 'li-'. Doc-vs-code drift only; no rule change.

**Files affected:** Constitution.md, Instructions.md

### `40.02.05` - 2026-07-03

Tier B engine repairs: memory add/rm date now targets the live Dates.md sections with three-cell rows, section-bounded table writes, and a pre-edit backup; Log.md regains the Sort Routing Notes table remember route writes to; consolidate and folder memory derive their file sets from MEMORY_COLLECTIONS; gitkeep check exits nonzero on a missing infra dir; supersede also flips frontmatter status to deprecated with guarded atomic IO; sync tag entries carry a manual marker that routine syncs and verify respect; the Log placeholder drop is bounded to its section.

**Files affected:** System/brain.command, Memory/Log.md

