---
title: "BRAIN System Instructions"
description: "Master operating manual for any AI accessing this BRAIN. Covers navigation, folder purposes, Profile documentation, Inbox sorting protocol, and frontmatter standards."
status: "active"
tags: ["root", "guide", "startup", "timeless"]
aliases: []
keywords: ["operating manual", "navigation", "folder purposes", "frontmatter schema", "inbox sorting protocol", "startup checklist", "how to use brain"]
created: 2026-05-18
updated: 2026-07-04
type: "guide"
folder: "root"
layer: 0
policy: false
version: "01.12.00"
author: "Tanner Golden"
path: "BRAIN/Instructions.md"
id: "ro-instructions"
---

# BRAIN System Instructions

> **This is your operating manual.** Read this file at the start of every session before accessing any other part of the BRAIN. It tells you how this system is structured, what each folder contains, how to handle files, and what rules govern your behavior. For governance rules specifically, refer to `Constitution.md` in this same root directory.

---

## Critical Rules at a Glance

> Read this box first. It is the **primacy anchor** for this file: the rules most costly to miss, surfaced at the top where attention is highest. Full detail lives in the sections and files it points to. The companion rule that prevents these from being "lost in the middle" of a long context is Section 14.

- **The Constitution governs.** [[Constitution|Constitution.md]] is non-negotiable and wins every conflict. When unsure, consult it.
- **Initialize every session.** Run the Section 9 checklist: load the four `startup` files (Constitution, Instructions, Working Style, Memory/Log), check `Inbox/`, and load the 2 most recent `Memory/Context/Current/` summaries.
- **Back up before editing** any existing file (Section 10): a `.backups/` snapshot in a local-only vault, a commit in a remote-backed one (the engine skips the snapshot when a git remote is reachable). **Log core-file changes** to `System/changelog.md` (Constitution 3.6).
- **Never delete or restructure** Layer 0/1, and never delete any file, without explicit user confirmation (Constitution 2.1, 3.1).
- **Load lean.** Retrieve the minimal relevant set, never the whole vault for routine work. This is the BRAIN's primary defense against context-recall failure (Section 14).
- **Retrieval order.** Ground answers vault first (`search` / `load`), then the offline knowledge bases (`kb search`), then the live web; prefer the closest tier that answers, skip to the web for anything current, and never leave the vault for anything about the user (Section 4.5).
- **Output quality.** No em dashes, no AI-slop vocabulary, answer directly (Constitution Articles IX–X).
- **Invoke matching skills directly.** When a message matches a skill's description (by trigger phrase or context), fire the skill without asking. Skill selection is not a structural action and is exempt from confirm-first; the gate covers vault writes, which skills handle via their own preflight (`System/Skills/Skills.md`).

---

## 1. What This BRAIN Is

See [[Information|Information.md]] in this root directory for the full explanation of what the BRAIN is, its design principles, and how portability works.

**Short version:** A portable, personal user data layer that gives any AI model persistent, structured access to information about the user. Model agnostic, embedding agnostic, location-independent. It is a living system - the AI maintains it, not the user.

---

## 2. Directory Structure

```
BRAIN/
├── Instructions.md       ← You are here. Read first, every session.
├── Constitution.md       ← Governance rules. Non-negotiable.
├── Information.md        ← What the BRAIN is - purpose, design principles, portability.
├── AGENTS.md             ← Interop pointer for third-party agents (AGENTS.md standard). Points here.
├── CLAUDE.md             ← Claude Code shim: imports AGENTS.md (Claude Code doesn't read it natively).
├── Inbox/                ← Staging area for unsorted user files
├── Library/              ← Universal reference library (10 discipline classes)
├── Profile/             ← Who the user is (Profile/Profile.md)
├── Memory/               ← Continuity across sessions (by memory type)
│   ├── Log.md            ← Working: capture stream + open loops
│   ├── Dates.md          ← Prospective: dates, deadlines, anniversaries
│   ├── Context/          ← Episodic: tiered session summaries
│   │   ├── Current/      ← Active (max 3, auto-loaded at session start)
│   │   ├── Recent/       ← Recent history (max 6)
│   │   └── Archive/      ← Lifetime cold storage, by year (search-only)
│   ├── Events/           ← Episodic: atomic dated events
│   ├── Entities/         ← Semantic: People / Organizations / Places
│   ├── Decisions/        ← Reflective: decisions and outcomes
│   ├── Insights/         ← Reflective: derived patterns about the world
│   └── .template/        ← Entry scaffolds
├── Ventures/             ← Business context for each company the user owns/operates
├── Projects/             ← Personal projects and initiatives
└── System/               ← AI behavior configuration and workflows
```

Every folder contains a documentation file named after the folder itself - `Memory/Memory.md`, `System/System.md`, `Profile/Profile.md` - that explains its purpose and carries its canonical rules. (Only the BRAIN root's definition file keeps the name `Information.md`.) Read those files when entering a folder for the first time or when context about that folder would be useful.

---

## 3. Layer Structure & Navigation Rules

This BRAIN uses a strict layered hierarchy:

| Layer | Description | Examples |
|-------|-------------|---------|
| **Layer 0 (Root)** | Core system files only | `Instructions.md`, `Constitution.md` |
| **Layer 1** | Primary domain folders | `Library/`, `Memory/`, `Projects/`, `Inbox/` |
| **Layer 2** | Subfolders within Layer 1 | `Library/Science & Mathematics/`, `Memory/Entities/` |
| **Layer 3+** | Specific topic subfolders | `Library/Science & Mathematics/Physics/`, `Memory/Entities/People/` |

**Navigation rules:**
- Always read the folder's namesake doc (`[Folder].md`) before assuming you understand its contents
- When looking for something, traverse from general to specific - start at Layer 1, then narrow down
- If a file could logically belong in two places, prefer the folder that is more specific to the user's context over the more general one

---

## 4. Finding Files Quickly

Use the lookup table below to go directly to the right file without traversing the tree. For task-based loading, use `brain.command load "task description"` - it returns the minimal file set with token estimates. For keyword search, use `brain.command search "term"`.

### 4.1 Direct Lookup

| What you need                                 | Link                                   | Path                                                            |
| --------------------------------------------- | -------------------------------------- | --------------------------------------------------------------- |
| How to behave, governance rules               | `Constitution.md`                       | `Constitution.md`                                               |
| How this BRAIN is structured                  | `Instructions.md`                       | `Instructions.md` (this file)                                   |
| User's preferences and AI interaction rules   | `Profile/Working Style.md`               | `Profile/Working Style.md`                                       |
| Who the user is - background, history, career | `Profile/Biography.md`                 | `Profile/Biography.md`                                         |
| How the user thinks and communicates          | `Profile/Personality.md`               | `Profile/Personality.md`                                       |
| What the user values and believes             | `Profile/Values/Values.md`                    | `Profile/Values/Values.md`                                            |
| What happened recently, open loops            | `Memory/Log.md`                         | `Memory/Log.md`                                                 |
| Major past decisions and outcomes             | `Memory/Decisions/Decisions.md`         | `Memory/Decisions/<entry>.md` (index: `Decisions/Decisions.md`) |
| Facts, traits, or patterns about the user     | `Profile/`                             | `Profile/` (its facets) - never Memory |
| Important dates, deadlines, anniversaries     | `Memory/Dates.md`                       | `Memory/Dates.md`                                               |
| People referenced across conversations        | `Memory/Entities/People/People.md`      | `Memory/Entities/People/First Last.md` (index: `Entities/People/People.md`) |
| What projects are active right now            | `Projects/` folders                     | `db search folder=projects` (or list `Projects/`)              |
| Status and details on a specific project      | `Overview.md`                          | `Projects/[Name]/Overview.md`                                   |
| What ventures the user owns or operates       | `Ventures/` folders                     | `db search folder=ventures` (or list `Ventures/`)              |
| A venture's company profile                   | `Overview.md`                          | `Ventures/[Company]/Overview.md`                                |
| A venture's current goals and OKRs            | `Ventures/.template/Goals.md`                              | `Ventures/[Company]/Goals.md`                                   |
| Recent venture history and decisions          | `Log.md`                               | `Ventures/[Company]/Log.md`                                     |
| A venture's team and org structure            | `Ventures/.template/Human Resources (HR)/Hierarchy.md`                          | `Ventures/[Company]/Human Resources (HR)/Hierarchy.md`          |
| A venture's brand and messaging               | `Ventures/.template/Sales & Marketing (S&M)/Brand.md`                              | `Ventures/[Company]/Sales & Marketing (S&M)/Brand.md`           |
| A venture's clients and accounts              | `Ventures/.template/Client Experience (CX)/Clients.md`                            | `Ventures/[Company]/Client Experience (CX)/Clients.md`          |
| A venture's financials and runway             | `Ventures/.template/Finance & Accounting (F&A)/Financials.md`                         | `Ventures/[Company]/Finance & Accounting (F&A)/Financials.md`   |
| A venture's tech stack and tools              | `Ventures/.template/Information Technology (IT)/Stack.md`                              | `Ventures/[Company]/Information Technology (IT)/Stack.md`       |
| A venture's KPIs and dashboards               | `Ventures/.template/Business Intelligence (BI)/Metrics.md`                            | `Ventures/[Company]/Business Intelligence (BI)/Metrics.md`      |
| A venture's product roadmap                   | `Ventures/.template/Research & Development (R&D)/Roadmap.md`                            | `Ventures/[Company]/Research & Development (R&D)/Roadmap.md`    |
| A venture's legal structure and contracts     | `Ventures/.template/Legal & Compliance (L&C)/Compliance.md`                         | `Ventures/[Company]/Legal & Compliance (L&C)/Compliance.md`     |
| A venture's core processes and vendors        | `Ventures/.template/Operations & Logistics (O&L)/Operations.md`                         | `Ventures/[Company]/Operations & Logistics (O&L)/Operations.md` |
| Purpose of any folder                         | `[Folder]/[Folder].md`                 |                                                                 |
| Version history of the BRAIN system itself    | `System/changelog.md`                   | `System/changelog.md`                                           |
| Formalized AI workflows and strategy loops    | `System/Workflows.md`                          | `System/Workflows.md`                                           |
| Unpackaged skill directories (subagents live inside each skill) | `System/Skills/Skills.md`       | `System/Skills/Skills.md`                               |

### 4.2 Using Frontmatter to Filter

Every file has structured fields that narrow scope without reading content:

- **`folder`** - the owning section (`memory`, `projects`, `ventures`, etc.). Use this to limit a search to the relevant part of the BRAIN.
- **`layer`** - read lower numbers first. Layer 0 files are always most important; layer 2+ are content.
- **`type`** - tells you what kind of file it is before you open it. Same values as the File Role tag dimension (`guide`, `constitution`, `information`, `template`, `log`, `record`, `self`, `reference`, `script`, `agent`).
- **`tags`** - the closed-vocabulary tagging system defined in Constitution Article VII. Every file carries: a Folder tag, a File Role tag, optional `startup`, optional `sensitive`, and an optional Freshness tag (`timeless`/`enduring`/`current`). There are no free-form content tags. See Constitution Article VII for the full vocabulary.
- **`policy`** - boolean flag (frontmatter field, not a tag), present on every file. `true` when the file contains an embedded policy such as a retention policy, otherwise `false`. Filter `policy: true` to find every file carrying policy text.

**Common retrieval filters:**

| Filter | Meaning |
|--------|---------|
| `startup` | Files the AI loads at the beginning of every session |
| `sensitive` | Personal/private data, surface with discretion |
| `policy: true` (frontmatter field) | File contains an embedded policy such as a retention policy |
| Freshness tags (`timeless`, `enduring`, `current`) | Library files classified by estimated useful lifespan (see Article 6.2) |

### 4.3 Minimum Load for Any Task

If you are uncertain what to load, the four `startup` files cover the essential context for almost any task:

1. `Constitution.md` - rules
2. `Instructions.md` - structure
3. `Profile/Working Style.md` - how to behave
4. `Memory/Log.md` - recent context

For what currently exists (active projects, ventures, knowledge domains), query the catalog on demand - `db search folder=projects` / `folder=ventures`, or open the folder's hub doc (`Projects/Projects.md`, `Ventures/Ventures.md`, `Library/Library.md`).

Plus the namesake doc (`[Folder].md`) for any folder directly relevant to the task. `brain.command load "task"` assembles exactly this startup spine and then adds the most relevant files within a token budget.

### 4.4 Operating the Engine (`brain.command`)

`System/brain.command` is how you operate this BRAIN at scale: it does deterministically, in one call, what would otherwise take you many error-prone steps. Run it as `python3 System/brain.command <command>`. Add `--yes` to auto-confirm, `--json` on `load` for machine-readable output. `lint`, `stale`, and `diff` exit non-zero on findings, so you can branch on exit codes.

**Reach for it by situation - this is the power-user loop:**

| When | Run |
|------|-----|
| Starting any session | `startup` - the whole Section 9 bundle in one call (`--json` to budget it first; `--manifest` for the hook-safe orientation card) |
| Starting work on any task | `load "task description"` - ranked, budgeted context instead of guessing what to read |
| Needing part of a file, not all of it | `read <path> "<section>"` (or `--toc`, `--fm`) - Article 10.4 made mechanical |
| Finding anything by content | `search "term"` (add `folder=` / `type=` to narrow) - including the Memory archive |
| Looking up world knowledge the vault lacks | `kb search "term"` - the offline knowledge bases (Wikipedia and more) in `Library/Reference & Encyclopedia/`; after the vault, before the web (Section 4.5) |
| **Before editing any existing file** | `backup <path>` - the Section 10 protocol in one step (skipped in a remote-backed vault: commit instead; `backup <path> local` forces a snapshot) |
| After creating, moving, or editing files | `sync`, then `health` - tags pushed, system verified, index fresh |
| After saving a session summary | `memory cascade` - enforce the tier caps (Section 13.2) |
| Scaffolding new work | `new project "Name" --yes` / `new venture "Name" --yes` |
| Shipping a skill from `System/Skills/` | `skill package <name>` - validate + zip to an installable `.skill` (or `skill package all`) |
| After editing wikilinks, or any rename/move | `links check` - broken links are lies in the graph; exit 1 catches them |
| Renaming any file | `rename <path> <new-name>` - rewrites every backlink, backups first |
| After creating or closing a project/venture | `index verify` - the registries must match the tree |
| Compiling a session summary (Section 13) | `summary new` - canonical scaffold + cascade in one step |
| Running the Memory Consolidation Loop | `consolidate` - the ADD/UPDATE/SUPERSEDE/NOOP worksheet, read-only |
| Logging a core-file change (Article 3.6) | `changelog add <level> "description"` - version math and the 4-cap handled |
| Before any multi-file maintenance pass | `git snapshot "msg"` - a whole-vault restore point Backups/ can't give |
| Deleting anything (after user approval) | `trash <path>` - soft removal to `.trash/`; later, `trash empty` hands items to the computer's Trash (the OS finishes the job) |
| Capturing a quick fact or event | `remember "Title: detail"` - formatted Log entry, `updated` bumped |
| Wondering what changed since last verified | `diff` - hash-confirmed, exits 1 on drift |
| Refreshing who the user is, or their life state | `folder profile` / `folder memory` - the whole area in one call |
| Scanning the portfolio, or loading one venture/project deep | `folder ventures [Name]` / `folder projects [Name]`; `folder library` for the catalog |
| Budgeting context for a heavy session | `tokens` |

The full command reference lives in [[System/System|System/System.md]]. The rule of thumb: if you are about to do something file-mechanical by hand - assemble context, name a backup, enforce a cap, push tags, validate the tree - check this table first, because the engine almost certainly does it better.

### 4.5 Retrieval Order (vault -> knowledge bases -> web)

When you need a fact, ground it in the closest, most authoritative tier first, and fall outward only when that tier cannot answer. The order is owned-and-specific, then established, then current:

1. **The vault** (`search` / `load` / `db search`). Everything the user has recorded: Memory and Profile (about them), Projects and Ventures (their work), and the curated `Library/` notes (their own writing on a topic). Authoritative for anything about the user or their domains, and it carries their framing. For anything about the user, stop here.
2. **The knowledge bases** (`kb search`), in `Library/Reference & Encyclopedia/`. The offline world-knowledge layer (Wikipedia, Wiktionary, and the rest): what humanity has established. The grounding tier for what-is, who-was, define, explain. A user's own `Library/` note outranks it on framing; the knowledge bases fill in the established background.
3. **The live web** (research / web search). Current events, post-snapshot facts, prices, niche or specialized or proprietary topics, and verification of time-sensitive claims.

Two exceptions to strict top-down:
- **Time-sensitive or "latest" questions skip to the web.** The knowledge bases are monthly snapshots (some sources older); do not search them for breaking news, prices, or "now."
- **Questions about the user stop at the vault.** Do not escalate to the knowledge bases or the web for the user's own projects, people, or preferences.

The ladder sets grounding priority, not where to stop: when a question spans tiers, combine them - the user's note, plus established background, plus what changed recently - rather than halting at the first hit.

---

## 5. Folder Purposes

Each folder's canonical rules live in its own namesake doc - **read that doc before working in the folder.** What stays always-on here is one line of purpose and the rules you need before you ever open the folder:

| Folder | Purpose | Canonical rules |
|--------|---------|-----------------|
| Library/ | Universal reference library: 10 discipline classes, freshness-gated, never personal data | [[Library/Library\|Library.md]] |
| Memory/ | Continuity: staging Log, permanent records, tiered session summaries + lifetime archive | [[Memory/Memory\|Memory.md]] |
| Ventures/ | One folder per company the user owns/operates. **Check `Ventures/` (or `db search folder=ventures`) first** before offering to create one; scaffold via `new venture` | [[Ventures/Ventures\|Ventures.md]] |
| Projects/ | Personal initiatives only. Ask before creating; scaffold via `new project` | [[Projects/Projects\|Projects.md]] |
| System/ | The engine, workflows, Skills/, State/ (Data, Backups) | [[System/System\|System.md]] |
| Inbox/ | Sorting staging area - essentials in Section 7 | [[Inbox/Inbox\|Inbox.md]] |
| Profile/ | Who the user is - Section 6 | [[Profile/Profile\|Profile.md]] |

---

## 6. Profile/ Folder

Who the user is: `Profile/Biography.md` (life history), `Profile/Personality.md` (how they think), `Profile/Values/Values.md` (what matters to them), `Profile/Working Style.md` (how the AI should behave - startup-tagged, read every session). These files are a personal profile, not reference material: absorb them as context, never quote them back, and apply the delegated Article IV rules hosted there (read-only by default, flag inferences, no speculation) plus the universal 4.4 sensitivity law. Full guidance: [[Profile/Profile|Profile/Profile.md]].

---

## 7. Inbox Protocol (Essentials)

The always-on rules - these you must never get wrong, even without reading further:

- **Check `Inbox/` at every session start** (Constitution 5.2). If sortable files are present, handle them before anything else.
- **The held sub-homes are never sorted.** `Inbox/Reports/` and `Inbox/Faculties/` (the standing-teams home) are excluded from the sort sweep; they stay linted, synced, and indexed but are never scanned, surfaced, or proposed for routing.
- **Nothing moves un-enriched or unconfirmed** (Constitution 5.3). Propose destination + clean rename per file, get explicit approval, apply frontmatter or xattr tags, then move.
- **Never delete an Inbox file without confirmation**; leaving it at the `Inbox/` root is the safe default.
- **External PDFs get a cleanup offer first** (shadow-library watermarks/links), with originals backed up to `Inbox/Backups/` before any modification.

The full canonical protocol - detection exclusions, PDF cleanup contract, confirmation formats, enrichment order and the Library freshness gate, ambiguous-file logging, filename collisions, dynamic subfolder creation, and system-asset routing - lives in [[Inbox/Inbox|Inbox/Inbox.md]]. **Read it before sorting anything.**

---

## 8. Frontmatter Standards

Every markdown file in this BRAIN must include a YAML frontmatter block at the very top of the file. This enables consistent parsing across AI models and indexing environments.

### 8.1 Standard Frontmatter Schema

Fields are ordered in two bands (see 8.8): a human-facing band shown in Obsidian, then a system band hidden by a CSS snippet. The band-header comments below are illustrative; real files carry no comments.

```yaml
---
# Human band - shown in Obsidian (the fields you read and edit)
title: ""              # Human-readable file title
description: ""        # One or two specific, task-shaped sentences describing what this file is and when to use it. Do not echo the title; do not keyword-stuff.
status: ""             # Lifecycle: draft | active | deprecated | archived. Distinct from the Library freshness tag (content time-sensitivity vs file state). Retrieval treats deprecated/archived as stale: demoted (sorted last, flagged) in search, skipped by load and the startup auto-load. Retained and searchable, never deleted.
tags: []               # Closed vocabulary per Article VII: Folder + File Role + optional startup / sensitive / freshness. No content tags.
aliases: []            # Alternate names the file is known by (acronyms, former names, misspellings). Free text. Substitutable for the title. May be empty.
keywords: []           # 4-8 free-text search synonyms a user would type that are NOT already in the title. Distinctive, lowercase, deduped against the title. May be empty.
created: YYYY-MM-DD     # Unquoted ISO date (YYYY-MM-DD) so Obsidian types it as Date, not Text. Date file was first created.
updated: 2026-06-26
# System band - hidden in Obsidian via .obsidian/snippets/brain-hide-system.css (engine-managed; rarely hand-edited)
type: ""               # File Role tag value: guide | constitution | information | template | log | record | self | reference | script | agent
folder: ""             # Folder tag value: library | profile | memory | projects | ventures | system | inbox | root
layer: 0               # 0 = root, 1 = layer 1 folder file, 2 = layer 2 subfolder file, etc.
policy: false          # Required on every file. true if the file contains an embedded policy (e.g. a retention policy), else false.
version: "01.00.00"    # CORE/CONTRACT FILES ONLY (see 8.6). Per-file MAJOR.MINOR.PATCH, two-digit zero-padded. Content files omit this line.
author: ""             # The file's author. Defaults to the BRAIN owner.
path: ""               # Full path from BRAIN root (e.g. "BRAIN/Memory/Log.md")
id: ""                 # Stable slug, two-letter folder prefix + hyphenated name (e.g. "li-spaced-repetition"). Generated once at creation; NEVER regenerated. Survives renames/moves.
---
```

**Example complete frontmatter** (for the Constitution itself):

```yaml
tags: ["root", "constitution", "startup", "timeless"]
```

The schema is flat (no nested keys: the engine and Obsidian both require flat properties). Every file carries these fields in the two-band order shown above: a human-facing band (`title` through `updated`) followed by a system band (`type` through `id`), with `version` present only on core/contract files. The order is for human and Obsidian readability only; `brain.command` parses and lints fields order-independently. `aliases`, `keywords`, and `tags` are lists; `id`, `aliases`, and `keywords` directly improve retrieval (`id` is a stable link target; `aliases`/`keywords` are added to the strong-match surface in `brain.command load`/`search`, countering the vocabulary-mismatch weakness of keyword ranking). Tag order remains: Folder, File Role, AI Signal, Sensitivity, Freshness. The `policy`, `status`, and `version` flags are separate frontmatter fields, not tags. See 8.8 for the shown/hidden band split and the Obsidian display convention.

### 8.2 Binary / Non-Editable Files

For files that cannot contain embedded frontmatter (images, PDFs, scripts, audio, video, `.zip`, etc.), tags are written directly to the file's macOS metadata via xattr.

Determine appropriate tags based on the file's content and its destination folder, then apply them via `com.apple.metadata:_kMDItemUserTags` using the same xattr method `brain.command` uses for `.md` files.

### 8.3 Update Policy

Update `updated` whenever a file's content changes meaningfully. Do not update it for minor formatting fixes or whitespace changes. The date should reflect when the information itself last changed.

### 8.4 macOS File Metadata Sync (Mandatory)

**Tags in the YAML frontmatter must also be written to the file's macOS Finder metadata.** This is not optional. Every file that has a `tags:` field must have those same tags applied as macOS extended attributes (`com.apple.metadata:_kMDItemUserTags`) so they appear in the Finder "Tags" field, are searchable via Spotlight, and can be filtered in the sidebar.

**When this must happen:**
- After creating any new `.md` file
- After sorting any file from `Inbox/` to its destination
- After updating `tags:` in any file's frontmatter
- After creating a new project folder (all template files get tagged)

**How to do it:**
The AI runs the sync directly via bash:

```bash
python3 "/path/to/BRAIN/System/brain.command" sync
```

Resolve the path at runtime from the BRAIN root. This applies tags across all files in the BRAIN at once.

### 8.5 Tagging Rules

Tags follow the closed vocabulary defined in Constitution Article VII. There are no free-form content tags. Every file carries (in canonical order):

1. **Folder tag** (required) - `root`, `library`, `profile`, `memory`, `projects`, `ventures`, `system`, or `inbox`. Matches the `folder` field.
2. **File Role tag** (required) - `guide`, `constitution`, `information`, `template`, `log`, `record`, `self`, `reference`, `script`, or `agent`. Matches the `type` field. Library content files use `reference`; `information` is reserved for folder documentation.
3. **AI Signal** (when true) - `startup`
4. **Sensitivity** (when true) - `sensitive`
5. **Freshness** (when meaningful) - `timeless`, `enduring`, or `current` (Library files always carry one; see Article 6.2)

Any tag outside this vocabulary is invalid and is rejected by `brain.command lint`. Subject-matter search is handled by the folder taxonomy and `brain.command search`, not by tags.

Whether a file contains an embedded policy (e.g. a retention policy) is recorded by the boolean `policy` frontmatter field (Section 8.1), which is present on every file (`true` or `false`), not by a tag.

See Constitution Article VII for the complete tagging laws including format rules, valid values, and prohibited patterns. Run `python3 System/brain.command sync` after any tag change.

### 8.6 Versioning (Core/Contract Files)

A per-file `version` is carried only by **core/contract files**: those whose shape or rules other content depends on. Membership is decided by **location, not file type** (because `type: information` covers both governance folder docs and Library content-area docs, and only location tells them apart). A file is core, and carries `version`, when it is any of:

- a root governance file: `Constitution.md`, `Instructions.md`, `Information.md`, `AGENTS.md`, `CLAUDE.md`;
- anything under `System/`;
- any file inside a `.template/` folder;
- a Layer-1 folder documentation file (the folder-named doc directly inside a Layer-1 folder, e.g. `Memory/Memory.md`, `Library/Library.md`, `Profile/Profile.md`).

Everything else carries **no** `version` and relies on `updated` plus backup/history: all Library content and its subfolder docs (e.g. `GitHub.md`, `Backend.md`), and all Memory, Profile, Projects, and Ventures content. `brain.command` enforces this both ways in `lint` (the test is `_is_core_file`): a core file missing `version` fails, and a content file carrying `version` fails.

Format is `MAJOR.MINOR.PATCH`, two-digit zero-padded (e.g. `02.01.00`), matching `changelog.md`. Every file is created at `01.00.00`. The segment is chosen by the nature of the change, never by default:

- **MAJOR** - a breaking change to the file's rules or shape that existing content must conform to (a template restructure, a new mandatory field, a skill changing its interface).
- **MINOR** - a backward-compatible addition (a new optional field, a new section, a new capability).
- **PATCH** - a fix or clarification with no behavior change (a typo, a reworded rule, a refactor).

Do not edit the number by hand. Bump it with the engine, which does the arithmetic, stamps `updated`, and backs the file up first:

```bash
python3 System/brain.command bump "System/Workflows.md" minor
```

`brain.command health` includes a **version-drift** check: it flags any core file whose content changed since the last index build without a matching version bump, and prints the exact `bump` command to run. It never guesses the segment for you. After bumping, run `manifest` to refresh the index.

**A per-file `version` lives only in the frontmatter, never in body text.** The single exception is `System/changelog.md`, whose body carries a `Current Version` heading: that is the *system* version registry (the BRAIN-wide MAJOR.MINOR.PATCH tracked by `changelog add`), which is a different thing from the file's own frontmatter `version`. Both legitimately coexist on `changelog.md` (its frontmatter `version` is its per-file version; its body `Current Version` is the system version). Nowhere else should a version string appear in a file body.

### 8.7 Identity and Discovery Fields

- **`id`** is the file's durable identity. It is a lowercase, hyphenated slug with a two-letter folder prefix (`li-`, `me-`, `pr-`, `ve-`, `sy-`, `id-`, `in-`, `ro-`), generated once by `brain.command` when the file is created and never regenerated, so links and references survive renames and moves (which change `path`). Ids must be unique across the BRAIN; `lint` enforces both the format and uniqueness.
- **`aliases`** are alternate names the file is known by - acronyms, expansions, former titles, common misspellings. An alias must be substitutable for the title; topics and related concepts belong in `keywords`, not here. On rename, add the old title as an alias.
- **`keywords`** are free-text search synonyms: 4-8 distinctive, lowercase terms a person would actually search that are not already in the title. Prefer terms specific to this file over generic words every file shares, and include the problem phrasing people type. This is the deliberate free-text exception to the closed-vocabulary tag rule (Constitution Article VII): subject matter lives here, never in `tags`.

### 8.8 Field Bands and Obsidian Display

The fields are grouped into two bands by who uses them, and emitted in this order in every file:

- **Human band (shown):** `title`, `description`, `status`, `tags`, `aliases`, `keywords`, `created`, `updated`. The fields a person reads or edits.
- **System band (hidden):** `type`, `folder`, `layer`, `policy`, `version`, `author`, `path`, `id`. Engine-managed, derived from location, or constant in a personal vault. They stay in the file and are fully used by `brain.command`; they are only hidden from the Obsidian editor to cut clutter.

Hiding is done with a CSS snippet at `.obsidian/snippets/brain-hide-system.css` (enable under Settings -> Appearance -> CSS snippets), which targets each system key by name. It is display-only: every field remains present in the YAML and required exactly as before. The dates are unquoted ISO so Obsidian types them as Date (8.1).

When creating or rewriting any file, emit fields in the two-band order above so the property panel reads cleanly on devices both with and without the snippet. The order is a readability convention, not a parser requirement: `brain.command` reads and lints fields order-independently, so a file is never wrong for ordering alone, but new and edited files should follow it.

### 8.9 Schema Changes Propagate to Every File

**The standard frontmatter schema is vault-wide: when it changes, every existing file adopts the change in the same edit, not lazily as files happen to be touched.** A schema change that lands on new files only, leaving old files on the prior shape, is an incomplete change and a lint failure, never an acceptable end state. The schema is a contract every BRAIN document honors at once.

**What "standard frontmatter" means here:** the universal field set defined in 8.1 (the two-band schema every markdown file carries: `title` through `id`, with `version` scoped to core/contract files per 8.6). Adding a universal field, removing one, renaming one, or changing its required form or allowed values is a standard-schema change and triggers this rule.

**The migration is part of the change (do all of it, in order):**

1. Update the schema definition in 8.1 (and 8.7/8.8 if bands or discovery fields shift).
2. Update the engine: the scaffolders/templates in `brain.command` that emit frontmatter, plus `REQUIRED_FIELDS` and any validator in `cmd_lint`.
3. Back up, then backfill every existing markdown file to the new shape (`backup` first, Section 10).
4. Run `lint` (and `health`): the change is done only when zero files report a schema error. `lint` checks `REQUIRED_FIELDS` presence on every file, so a newly required field surfaces as an error on each non-conformant file until backfilled. The rule is machine-checked, not merely policy.
5. Bump the affected core files (8.6) and log the change to `System/changelog.md` (Article 3.6).

**Scope boundary (do not over-apply this rule):** it governs the *standard, universal* schema only. A field deliberately scoped to one class of file is **not** part of the standard frontmatter, is **not** added to 8.1, and is **not** backfilled across the vault: it lives only on the files it applies to. The built-in example is `version` (8.6): it is carried only by core/contract files and is forbidden on content files, so a change to how `version` works touches that class alone, never the whole vault. If a future field is added for one file type (documented where that type is defined, such as `Memory/Memory.md` for session summaries), introduce it by documenting its scope there, never by amending 8.1. The corollary: reach for a scoped field only when no universal field already carries the meaning. Staleness, for instance, is not a scoped field, it is the universal `status` (deprecated/archived), so retrieval honors it everywhere rather than duplicating it per file type.

---

## 9. Session Initialization Checklist

At the start of every session, in this order:

1. **Read the governance pair** - this file (`Instructions.md`) and `Constitution.md`, or confirm both have been read this session
2. **Check `Inbox/`** - if files are present, analyze and prompt the user per Section 7
3. **Read `Memory/Log.md`** - restore recent context and check for open loops
4. **Load `Memory/Context/Current/`** - auto-load the **2 most recent completed** session summary files to restore immediate continuity (see Section 13)
5. **Read `Profile/Working Style.md`** - confirm operating style for this session
6. **Orient on what exists** - skim the folder hub docs (`Projects/Projects.md`, `Ventures/Ventures.md`, `Library/Library.md`) or query the catalog (`db search folder=<name>`) for current projects, ventures, and knowledge domains
7. **Read any project, venture, or library files** relevant to what the user is working on

The `startup` command emits steps 1–6 (and the step-2 Inbox check) in one call, in cache-optimal order - prefer it over assembling the bundle by hand. In a channel that truncates large output (a session-start hook), `startup --manifest` emits a compact card naming the startup set instead of inlining it; Reading every listed file completes the same checklist. The Claude Code SessionStart hook uses the manifest form for exactly this reason: the full bundle is ~30k tokens and never survives the hook channel intact.

Do not skip steps 1–6. They are the minimum required to operate with full context: they load exactly the four files tagged `startup` (Constitution, Instructions, Working Style, Memory/Log) plus the Inbox check and the latest `Memory/Context/Current/` summaries, and step 6 orients on what exists via the folder hubs or the `db` catalog. The tag and this checklist are kept in agreement.

> **Before searching the web for any factual question, search the BRAIN first.** Use `brain.command search` or check the relevant folder directly. Only reach for external sources if the BRAIN has no answer or the information needs to be verified for currency.

---

## 10. File Backup Protocol

**Before making any change to an existing BRAIN file - major or minor - create a backup copy first.** Run `backup <path>`; it is the standard pre-edit safeguard and applies to every file edit: updating a single line, restructuring a section, adding a new field, or rewriting an entire document.

**The safeguard depends on the backup mode.** In a **local-only vault** - one with no reachable git remote - the pre-edit `.backups/` snapshot is the only way back, so it is taken before every edit, no exceptions. In a **remote-backed vault** - a reachable git remote, which `brain.command` detects automatically (Constitution 3.1) - git history is the pre-edit backstop instead: `backup` reports the snapshot as skipped, and you preserve a state by committing it. So **commit meaningful states often** in a remote-backed vault. Force a local snapshot anyway with `backup <path> local` when you want belt-and-suspenders before a risky, uncommitted edit. The rest of this section describes the local-mode `.backups/` mechanism.

### 10.1 How to Back Up

Run `python3 System/brain.command backup <path>` - it copies the file to `System/.backups/` with the correct name in one step and refuses files that are already backups. Manual fallback: copy the original yourself using this format:

```
[folder]-[parent dirs]-[filename]-YYYYMMDD-HHMMSS.ext
```

Parent directories (sanitized to letters, digits, and hyphens) appear for nested files so that same-named files never share a name: `Ventures/Acme/Log.md` → `ventures-Acme-Log-…`, while `Memory/Log.md` stays `memory-Log-…`.

Examples:
- `root-Instructions.md` → `root-Instructions-20260519-143022.md`
- `Ventures/Ventures.md` → `ventures-Information-20260519-143022.md`
- `Memory/Log.md` → `memory-Log-20260519-143022.md`

Use the `folder` frontmatter value as the prefix (e.g., `memory`, `ventures`, `projects`, `root`); files without frontmatter use their Layer-1 folder. Include both date and time so multiple backups of the same file in one day don't collide.

**Rotation (standing policy).** `.backups/` keeps the newest **5 versions per source file**; when a 6th is written, the oldest is automatically soft-removed to `.trash/` - stage 1 of the two-level deletion law, recoverable until you run `trash empty`. The folder's advisory ceiling is **1000 snapshots** (`stale`/`health` warn past it; backups are never blocked - rotation keeps real counts far below the ceiling). The engine runs rotation after every backup; never prune by hand.

**Backups preserve the original file verbatim, including its wikilinks** (Constitution Article 3.7). A backup is a faithful snapshot for exact restoration, so copy the file as-is and never edit the backup afterward. A backup adds nothing to the live knowledge graph because of where it lives, not because it was altered: the linter never walks `System/.backups/`, so a backup is never validated or treated as a live node no matter what it contains.

### 10.2 After Making Changes

Tell the user which file was changed and confirm a backup was created:

> *"Updated `[file path]`. Backup saved to `System/.backups/[backup filename]`."*

### 10.3 Deleting Backups

**Do not delete backups silently or proactively.** When the user indicates they are done working on a file - phrases like "that's good", "we're done with this", "looks good", "ship it", or otherwise signals the work on that file is complete - ask whether the backup is still needed:

> *"Looks like we're done with `[file path]`. Do you still need the backup at `System/.backups/[backup filename]`, or is it safe to delete?"*

**If the user confirms deletion, do not delete immediately.** First re-read each modified file and verify it looks correct - frontmatter is valid, content is complete, nothing was accidentally truncated or misformatted. Only after that verification passes should the backup be removed - and removal means **soft removal** (`backup clear` moves snapshots to `.trash/`; Constitution 3.1's two-level law). Hard removal happens later, from `.trash/`, via `trash empty` with its own confirmation - and even that only hands items to the computer's own Trash for the OS's 30-day retention (Constitution 3.1).

If the verification reveals a problem, do not restore automatically and do not delete the backup. Inform the user of exactly what the issue is and wait for them to decide next steps. Once the issue is resolved, ask again whether the backup can be cleared before deleting it.

Once verified, delete the backup and confirm:

> *"Verified `[file path]` - looks good. Backup `[backup filename]` deleted."*

If they want to keep it, leave it alone without further comment. If multiple backups accumulate across sessions, list them for the user when asked and offer to clean them up.

---

## 11. Maintaining This BRAIN

You are expected to keep this system current. Specific responsibilities:

- **Update Memory files** after sessions where events occurred, decisions were made, or new people or dates surfaced (facts/traits about the user go to `Profile/`, not Memory)
- **Update Project files** when work is done on a project - update `Overview.md` status, add to `Log.md`
- **Promote `Memory/Log.md` entries** when they qualify: `memory add person|organization|place|decision|event|insight` for the Entities, Decisions, Events, and Insights collections, `memory add date` for Dates. Anything learned about *who the user is* is proposed into `Profile/` (Constitution 4.2), never stored in Memory (see `Memory/Memory.md`)
- **Run the Memory Consolidation Loop** (`System/Workflows.md`) periodically: deduplicate, merge, and supersede Memory entries so the memory layer stays lean and contradiction-free
- **Check memory before accepting premises.** When a user request embeds a factual assumption (a job, a location, a project state), verify it against current Memory before acting on it. If Memory contradicts the premise, surface the conflict instead of silently adopting either version - stale-memory conflicts are a documented failure mode of AI memory systems
- **Suggest file additions** when a conversation reveals a knowledge gap that a new source would fill
- **Never silently rename, delete, or restructure folders at Layer 0 or Layer 1** without explicit user confirmation
- **Hidden folders are infrastructure, not junk.** `.obsidian/` (vault config), `.trash/` (the soft-removal stage of the two-level deletion law, Constitution 3.1 - also Obsidian's deleted-notes folder), `.git/` (if present), and `.claude/` (Claude Code harness config: `settings.json` defines the hooks that force the Section 9 startup checklist to run on every session and after `/clear`, and `hooks/` holds the injected skill-router and per-prompt reminder notes that reinforce skill auto-triggering; the engine ignores `.claude/` like any dot-prefixed folder, so it stays out of lint, sync, and the link graph) are intentional and must never be deleted, even during cleanup - empty or not. Only transient artifacts are clearable junk: `__pycache__/`, `*.pyc`, `._*` AppleDouble files. **`.DS_Store` is neither junk nor content - ignore it completely.** Never delete, move, report, or count it, anywhere in the BRAIN; macOS owns and regenerates it, and `.gitignore` keeps it out of version control. When in doubt, ask.
- **Empty folders carry a `.gitkeep` - mandatory.** Every empty folder in the BRAIN holds a `.gitkeep` so the structure survives git, zips, and sync tools; the moment a folder gains real files, its `.gitkeep` is removed. Both directions are standing policy: `brain.command gitkeep` enforces them (and runs inside `health`), so never hand-manage these files. `.gitkeep` is infrastructure - it is not content and never gets frontmatter or tags. One scoped exception to shipping: inside a skill package, each unused mandatory folder carries a `.gitkeep` (the develop skill's v1.5.0 convention), so those markers do ship in `.skill` archives.
- **Log to `System/changelog.md`** after any change to a core BRAIN file (governance, scaffolding, scripts, templates, folder structure) that meets the PATCH threshold or larger. The changelog enforces its own classification rules, version bumping, and 4-entry cap per section. See Constitution Article 3.6 for the governing rule. Content additions (Library files, Memory entries, Project/Venture instances, Profile fills, Inbox sorting) are never logged.

**Prefer BRAIN over web search.** When a question can be answered from existing BRAIN content, do not reach for external sources. The BRAIN is the primary knowledge layer. Web search supplements it - it does not replace it.

For all governance rules, prohibited actions, and conflict resolution - see `Constitution.md`.

---

## 12. Linking & Graph Structure

This BRAIN functions as an interconnected knowledge graph. To maintain this structure, you must explicitly link related concepts using Obsidian wikilink syntax.

### 12.1 Syntax Rules
- **Use Wikilinks**: Wrap the name of any known entity (project, venture, person, concept) in double brackets: `[[Filename]]`.
- **Omit Extensions**: Do not include `.md` in the link. Use `[[Log]]`, not `[[Log.md]]`.
- **Disambiguate Paths**: If a filename is common (e.g., `Log.md`, `Overview.md`), include the parent folder to disambiguate: `[[Memory/Log|Log]]` or `[[Ventures/Company/Log|Company Log]]`.
- **Use Aliases**: For readability in sentences, use the pipe `|` character to alias a link. Example: `"We updated the [[Profile/Working Style|user preferences]]."`

These are syntax illustrations inside code spans - they render as text, create no graph edges, and the link checker ignores them. Live links still obey the topology (12.2) and cascade (12.3) rules.

### 12.2 Tree Topology - Hub-Only (Constitution 3.7)

The graph mirrors the file tree and only hubs carry edges. Before writing any wikilink, check the boundary:

| From | May wikilink |
|------|--------------|
| A folder doc (`Memory/Memory.md`) | The files in its own folder, plus the namesake docs of its immediate subfolders (one level, docs only) |
| `CLAUDE.md` | `AGENTS.md` only |
| `AGENTS.md` | `Instructions.md` only |
| `Instructions.md` (the vault root's folder doc) | `Constitution.md`, `Information.md`, plus the Layer-1 namesake docs |
| `Constitution.md` | Nothing - the graph's terminal node |
| **Any other content file** (not a folder doc) | **Nothing** - every reference is a plain code-style path |

Related folders connect through their common parent, never laterally. `.template/` folders and skill sources stay out of the graph entirely; each skill's graph node is its packaged `.skill` artifact, linked from `Skills.md` as a sibling file. `brain.command links` rejects violations, including any link from a content file. The Memory tier docs under `Memory/Context/` are ordinary hub-and-spoke: `Memory.md` links `Context.md`, and `Context.md` links the tier docs (`Current`/`Recent`/`Archive`); the tier docs do not link each other (Constitution 3.7 rule 7). There are no sanctioned lateral folder-doc links anywhere in the BRAIN.

### 12.3 Leverage Backlinks - Never Link Back
Because you are explicitly linking files, Obsidian automatically generates **Backlinks** (showing what files link to the current one). This is why the cascade rule exists (Constitution 3.7): a file never wikilinks back to a file that links to it - the reverse relationship is already visible in the backlink pane, so a return link is duplication, not connection. Links flow downhill (root → namesake docs → folder files); upward references are plain code-style paths. `brain.command links` rejects reciprocal pairs.

### 12.4 Where Wikilinks Are Forbidden
Any `.template/` folder must **never** contain wikilinks (Constitution Article 3.7). Templates hold blank scaffolds, not knowledge-graph nodes. Reference other files by plain text or plain path there, and the linter rejects wikilinks. The prohibition runs both directions: templates contain no wikilinks and nothing links *to* a template (reference scaffolds by plain path - a template link invites Obsidian to create stray notes and drags scaffolds into the graph).

Backups in `System/.backups/` are deliberately not on this list. A backup is a verbatim restore copy, so it keeps the original's wikilinks and is never edited after it is written. Backups stay out of the live graph by location, since the linter never walks `System/.backups/`, not by altering their contents.

---

## 13. Context Handoff & Tiered Memory

### 13.1 Summary Triggers (Layered - never wait for a threshold)

You cannot read your own context meter, so the system layers four triggers, strongest first:

1. **The engine's context gauge.** Every CLI command ends with `[ctx ~N tokens served]` - an exact ledger of what the engine has put into your context this session (`startup` resets it; it is a *lower bound* on total use). At **60k+**, update the running summary at the next task boundary. At **90k+**, the gauge itself instructs you: write the summary, cascade, and show the user the handoff notice.
2. **Host warnings.** If the platform you run on surfaces a context or compaction warning, treat it as authoritative and act immediately.
3. **Task-boundary checkpointing - the primary habit.** After every completed major task or milestone, update the running session summary (same-session overwrite, see [[Memory/Memory|Memory/Memory.md]]). Research is unambiguous: mandated checkpoints at task boundaries preserve continuity; waiting for pressure thresholds loses detail, and passive "summarize when needed" intentions barely work at all.
4. **The saturation heuristic (floor).** Long conversation, topic cycling, earlier context fading - if you notice these, checkpoint now regardless of the gauge.

A summary that exists *before* pressure hits is the whole point: if context resets unexpectedly, the checkpoint is already on disk.

### 13.2 The Pipeline

Summaries are timestamped files (`YYYYMMDD-HHMMSS.md`) that cascade through capped tiers:

| Tier | Directory | Max | Purpose |
|------|-----------|-----|---------|
| 1 | `Memory/Context/Current/` | **3** | Active session summaries (2 historical + 1 running) |
| 2 | `Memory/Context/Recent/` | **6** | Recent historical summaries |
| 3 | `Memory/Context/Archive/<year>/` | **unbounded** | Lifetime cold storage - nothing is ever deleted |

After saving a summary, run `python3 System/brain.command memory cascade` to enforce the caps; Recent overflow archives by year. The archive is search-only: never loaded at session start, never in `load` - reach it via `search` on explicit request.

### 13.3 The Canonical Detail

The summary compilation format (delta updates with explicit supersession), mandatory sections, file naming and frontmatter, the same-session overwrite exception, the handoff notice, and the natural-language recall mapping ("check your recent memory…") all live in [[Memory/Memory|Memory/Memory.md]]. **Read it before compiling a summary.**

---

## 14. Context Assembly & the Lost-in-the-Middle Rule

Language models reliably attend to the **beginning** and the **end** of a long context, but under-weight material in the **middle** - the "Lost-in-the-Middle" effect. A fact buried mid-context is frequently missed even though it is present. This section governs how to assemble context so the BRAIN never depends on the model recalling something from a low-attention position.

### 14.1 Primary Defense: Retrieve Lean, Not Whole

The BRAIN is a structured retrieval system, and that structure is itself the main protection against Lost-in-the-Middle. A short, targeted context has no vulnerable middle.

- **Load the minimal relevant set, never the entire vault, for routine work.** Use the Section 4.1 lookup table, `brain.command load "task"`, and frontmatter filters to pull only what the task needs.
- **Prefer many small, surgical reads over one giant read** (reinforces Constitution Article 10.4). Read the section you need, not the whole file.
- Never assemble a full-vault context, even for a fresh AI. Orientation comes from `AGENTS.md` and the Section 9 startup checklist; everything else is loaded on demand. (The old `export` command was removed in `11.01.00` - every supported AI connects to the files directly.)

### 14.2 When a Long Context Is Unavoidable, Bookend by Criticality

When you must assemble a large context (a wide multi-file task), place information by attention position, not by convenience:

- **Front (primacy):** governance and the active task's key files - `Constitution.md`, this file, `Profile/Working Style.md`, and the specific files the task turns on.
- **Middle:** bulk reference material (`Library/`), whose exact wording you are least likely to need recalled verbatim.
- **End (recency):** the single most important constraint, open loop, or immediate next step. Restate it last so it lands in the high-recall tail.

### 14.3 Never Bury a Must-Not-Miss Item

If an instruction, deadline, or constraint is critical to the current task, it belongs at the **start or end** of the assembled context, never in the middle of a long block. When compiling a session summary or handoff (Section 13), keep the **Active Changes** and **Immediate Next Steps** at the top or bottom of the summary, not sandwiched between long Established-Foundations sections.

When a recap or end-of-context anchor restates rules that also appear earlier (a session summary's Overrides section, a handoff's closing constraints), it must declare precedence explicitly: state that the recap version supersedes any earlier or conflicting statement. Without that declaration, a model facing two versions of a rule picks unpredictably; with it, the conflict resolves in the recap's favor.

### 14.4 Built-In Supports

- The top-of-file **Critical Rules at a Glance** box is this file's primacy anchor.
- `brain.command load` and the Section 4.1 lookup table exist so you rarely need a long context at all - use them first.

### 14.5 Token-Format Economy

Measured tokenizer facts that govern how content is written and assembled here:

- **Stable content first, volatile content last.** The Section 14.2 ordering (governance → reference → current context) is also the cache-optimal ordering: every major provider's prompt caching rewards an identical stable prefix, and a timestamp or session-specific value placed early breaks it. Never lead an assembled context, or a frequently loaded file, with anything that changes per session.
- **ASCII over decoration in anything an AI ingests.** Box-drawing characters cost 3–10x their ASCII equivalents in common tokenizers (`═` is the worst offender). The engine's output is ASCII-separated for this reason; follow the same rule in generated reports and tool output.
- **Pick the cheap format for the data's shape.** For bulk tabular data, CSV/TSV costs roughly a third of JSON; minified JSON beats pretty-printed by ~40%; XML is always the most expensive. Markdown tables cost more than prose for simple facts - use tables where scanning matters, prose where it doesn't. Frontmatter arrays stay inline (`["a", "b"]`), which is ~30% cheaper than block lists and is already the schema standard.
- **Compression is the wrong tool here.** Summarizing or compressing vault files to save tokens trades away exact wording, which Memory and Library depend on. The BRAIN's economy comes from loading less, not from degrading what's loaded.
