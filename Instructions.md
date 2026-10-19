---
title: "BRAIN System Instructions"
description: "Master operating manual for any AI accessing this BRAIN. Covers navigation, folder purposes, Profile documentation, Inbox sorting protocol, and frontmatter standards."
status: "active"
tags: ["root", "guide", "startup", "timeless"]
aliases: []
keywords: ["operating manual", "navigation", "folder purposes", "frontmatter schema", "inbox sorting protocol", "startup checklist", "how to use brain"]
created: 2026-05-18
updated: 2026-10-19
type: "guide"
folder: "root"
layer: 0
policy: false
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
- **Changes are commits.** The vault is a git repository: its history is the backup and the change record (Section 10, Constitution 3.1 and 3.6). Commit a meaningful state before a risky edit, and never leave uncommitted work where a deletion could take it.
- **Never delete or restructure** Layer 0/1, and never delete any file, without explicit user confirmation (Constitution 2.1, 3.1).
- **Load lean.** Retrieve the minimal relevant set, never the whole vault for routine work. This is the BRAIN's primary defense against context-recall failure (Section 14).
- **Retrieval order.** Ground answers vault first (search the notes and the catalog), then an offline knowledge base when one is installed (`knowledge-base.py search`), then the live web; prefer the closest tier that answers, skip to the web for anything current, and never leave the vault for anything about the user (Section 4.5).
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

Use the lookup table below to go directly to the right file without traversing the tree. To find anything by content, search the notes (your own search tools, or Obsidian's); `System/Data/catalog.ndjson` holds every note's title, description, tags and keywords on one line each.

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
| What projects are active right now            | `Projects/` folders                     | `Projects/` (or the catalog's `projects` records)              |
| Status and details on a specific project      | `Overview.md`                          | `Projects/[Name]/Overview.md`                                   |
| What ventures the user owns or operates       | `Ventures/` folders                     | `Ventures/` (or the catalog's `ventures` records)              |
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
| Version history of the BRAIN system itself    | the git history and release notes       | `git log`                                                       |
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

For what currently exists (active projects, ventures, knowledge domains), read the catalog (`System/Data/catalog.ndjson`, filtered by `folder`) or open the folder's hub doc (`Projects/Projects.md`, `Ventures/Ventures.md`, `Library/Library.md`).

Plus the namesake doc (`[Folder].md`) for any folder directly relevant to the task.

### 4.4 The Vault's Scripts (`.github/scripts/`)

The vault's checks and generators are scripts in `.github/scripts/`, each run as `python3 .github/scripts/<script>` from the vault root. Every check exits non-zero on a finding, so you can branch on exit codes, and CI runs them all (`.github/workflows/vault.yml`).

| When | Run |
|------|-----|
| Starting any session | Nothing: the SessionStart hook runs `session-hooks.py start`, which lists the Section 9 set to Read |
| After writing a note | Nothing: the PostToolUse hook runs `lint-notes.py` on it, and `check-skills.py` on a skill source, and hands any problem back |
| After a change a generated part lists: a summary, an entry, a skill, an agent, a new note | `update-vault.py`: cascades the memory tiers, redraws every generated block, rebuilds the catalogs and the skill archives, and fixes `.gitkeep` markers (the Stop hook runs it too) |
| Before committing, or after any multi-file change | `check-vault.py`: every check CI runs |
| Checking one part | `lint-notes.py [notes]`, `check-links.py`, `check-skills.py [names]`, `check-agents.py [names]`, `scan-pii.py` |
| Choosing the next Profile interview | `profile-coverage.py --json` (the identify skill reads it) |
| Looking up world knowledge the vault lacks | `knowledge-base.py search "terms"` and `read "title"`, once a source is turned on and fetched (`list`, `enable <name>`, `refresh`); after the vault, before the web (Section 4.5) |

Everything else you do directly, with your own tools, in the format the destination folder's note documents: a Log entry, a session summary, a Memory or Profile entry, a new project or venture copied from its `.template/` (give each copied file its real `type`, `path`, `id` and dates), a rename (update every wikilink to the old name, then run `check-links.py`), and a deletion (confirmed, then `git rm`, Constitution 3.1). The scripts check the result and redraw what is derived from it. Each script's purpose is listed in `.github/scripts/README.md`.

### 4.5 Retrieval Order (vault -> knowledge bases -> web)

When you need a fact, ground it in the closest, most authoritative tier first, and fall outward only when that tier cannot answer. The order is owned-and-specific, then established, then current:

1. **The vault** (search the notes and `System/Data/catalog.ndjson`). Everything the user has recorded: Memory and Profile (about them), Projects and Ventures (their work), and the curated `Library/` notes (their own writing on a topic). Authoritative for anything about the user or their domains, and it carries their framing. For anything about the user, stop here.
2. **The knowledge bases** (`python3 .github/scripts/knowledge-base.py search`), in `Library/Reference & Encyclopedia/`, when a source is installed; a fresh vault has none, so skip to the web. The offline world-knowledge layer (Wikipedia, Wiktionary, and the rest): what humanity has established. The grounding tier for what-is, who-was, define, explain. A user's own `Library/` note outranks it on framing; the knowledge bases fill in the established background.
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
| Ventures/ | One folder per company the user owns/operates. **Check `Ventures/` first** before offering to create one; scaffold by copying `Ventures/.template/` | [[Ventures/Ventures\|Ventures.md]] |
| Projects/ | Personal initiatives only. Ask before creating; scaffold by copying `Projects/.template/` | [[Projects/Projects\|Projects.md]] |
| System/ | Workflows, the skill library (Skills/), and the generated catalogs (Data/); the scripts live in `.github/scripts/` | [[System/System\|System.md]] |
| Inbox/ | Sorting staging area - essentials in Section 7 | [[Inbox/Inbox\|Inbox.md]] |
| Profile/ | Who the user is - Section 6 | [[Profile/Profile\|Profile.md]] |

---

## 6. Profile/ Folder

Who the user is: `Profile/Biography.md` (life history), `Profile/Personality.md` (how they think), `Profile/Values/Values.md` (what matters to them), `Profile/Working Style.md` (how the AI should behave - startup-tagged, read every session). These files are a personal profile, not reference material: absorb them as context, never quote them back, and apply the delegated Article IV rules hosted there (read-only by default, flag inferences, no speculation) plus the universal 4.4 sensitivity law. Full guidance: [[Profile/Profile|Profile/Profile.md]].

---

## 7. Inbox Protocol (Essentials)

The always-on rules - these you must never get wrong, even without reading further:

- **Check `Inbox/` at every session start** (Constitution 5.2). If sortable files are present, handle them before anything else.
- **The held sub-homes are never sorted.** `Inbox/Reports/` and `Inbox/Faculties/` (the standing-teams home) are excluded from the sort sweep; they stay linted and cataloged but are never scanned, surfaced, or proposed for routing.
- **Nothing moves un-enriched or unconfirmed** (Constitution 5.3). Propose destination + clean rename per file, get explicit approval, apply frontmatter to a note, then move.
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
status: ""             # Lifecycle: draft | active | deprecated | archived. Distinct from the Library freshness tag (content time-sensitivity vs file state). Retrieval treats deprecated/archived as stale: skipped by the session-start card and read last when searching. Retained and searchable, never deleted.
tags: []               # Closed vocabulary per Article VII: Folder + File Role + optional startup / sensitive / freshness. No content tags.
aliases: []            # Alternate names the file is known by (acronyms, former names, misspellings). Free text. Substitutable for the title. May be empty.
keywords: []           # 4-8 free-text search synonyms a user would type that are NOT already in the title. Distinctive, lowercase, deduped against the title. May be empty.
created: YYYY-MM-DD     # Unquoted ISO date (YYYY-MM-DD) so Obsidian types it as Date, not Text. Date file was first created.
updated: YYYY-MM-DD     # Unquoted ISO date. Date the content last changed meaningfully (8.3).
# System band - hidden in Obsidian via .obsidian/snippets/brain-hide-system.css (derived from location; rarely hand-edited)
type: ""               # File Role tag value: guide | constitution | information | template | log | record | self | reference | script | agent
folder: ""             # Folder tag value: library | profile | memory | projects | ventures | system | inbox | root
layer: 0               # 0 = root, 1 = layer 1 folder file, 2 = layer 2 subfolder file, etc.
policy: false          # Required on every file. true if the file contains an embedded policy (e.g. a retention policy), else false.
author: ""             # The file's author. Defaults to the BRAIN owner.
path: ""               # Full path from BRAIN root (e.g. "BRAIN/Memory/Log.md")
id: ""                 # Stable slug, two-letter folder prefix + hyphenated name (e.g. "li-spaced-repetition"). Generated once at creation; NEVER regenerated. Survives renames/moves.
---
```

**Example complete frontmatter** (for the Constitution itself):

```yaml
tags: ["root", "constitution", "startup", "timeless"]
```

The schema is flat (no nested keys: the scripts and Obsidian both read flat properties). Every file carries these fields in the two-band order shown above: a human-facing band (`title` through `updated`) followed by a system band (`type` through `id`). The order is for human and Obsidian readability only; `lint-notes.py` reads fields order-independently. `aliases`, `keywords`, and `tags` are lists; `id`, `aliases`, and `keywords` directly improve retrieval (`id` is a stable link target; `aliases`/`keywords` land in the catalog beside the title, countering the vocabulary-mismatch weakness of keyword search). Tag order remains: Folder, File Role, AI Signal, Sensitivity, Freshness. The `policy` and `status` flags are separate frontmatter fields, not tags. See 8.8 for the shown/hidden band split and the Obsidian display convention.

### 8.2 Binary / Non-Editable Files

A file that cannot contain frontmatter (an image, a PDF, a script, audio, video, a `.zip`) carries no tags of its own (Constitution 3.5). Its folder places it, and the folder's note describes it; name it so its subject is plain from the name.

### 8.3 Update Policy

Update `updated` whenever a file's content changes meaningfully. Do not update it for minor formatting fixes or whitespace changes. The date should reflect when the information itself last changed.

### 8.4 Checking Frontmatter

The frontmatter is checked, never trusted. In Claude Code, the PostToolUse hook runs `.github/scripts/lint-notes.py` on every note you write and hands any problem back in the same turn; CI runs it on every note. Run it yourself on a note you changed outside Claude Code: `python3 .github/scripts/lint-notes.py "<path>"`.

### 8.5 Tagging Rules

Tags follow the closed vocabulary defined in Constitution Article VII. There are no free-form content tags. Every file carries (in canonical order):

1. **Folder tag** (required) - `root`, `library`, `profile`, `memory`, `projects`, `ventures`, `system`, or `inbox`. Matches the `folder` field.
2. **File Role tag** (required) - `guide`, `constitution`, `information`, `template`, `log`, `record`, `self`, `reference`, `script`, or `agent`. Matches the `type` field. Library content files use `reference`; `information` is reserved for folder documentation.
3. **AI Signal** (when true) - `startup`
4. **Sensitivity** (when true) - `sensitive`
5. **Freshness** (when meaningful) - `timeless`, `enduring`, or `current` (Library files always carry one; see Article 6.2)

Any tag outside this vocabulary is invalid and is rejected by `lint-notes.py`. Subject-matter search is handled by the folder taxonomy and full-text search, not by tags.

Whether a file contains an embedded policy (e.g. a retention policy) is recorded by the boolean `policy` frontmatter field (Section 8.1), which is present on every file (`true` or `false`), not by a tag.

See Constitution Article VII for the complete tagging laws including format rules, valid values, and prohibited patterns.

### 8.6 No Per-File Versions

No note carries a `version` field, and `lint-notes.py` rejects one (Constitution 3.6). The BRAIN's change history is its git history: every change is a commit, and the release notes drawn from those commits are the version record. `updated` (8.3) still says when a note's content last changed. A skill keeps its own version, in its `SKILL.md` metadata and its `Changelog.md`, because the skill ships outside the vault (`System/Skills/Skills.md`).

### 8.7 Identity and Discovery Fields

- **`id`** is the file's durable identity. It is a lowercase, hyphenated slug with a two-letter folder prefix (`li-`, `me-`, `pr-`, `ve-`, `sy-`, `id-`, `in-`, `ro-`), chosen once when the file is created (the prefix, then the file's name as a slug, with `-2`, `-3` on a clash) and never regenerated, so links and references survive renames and moves (which change `path`). Ids must be unique across the BRAIN; `lint-notes.py` enforces both the format and uniqueness.
- **`aliases`** are alternate names the file is known by - acronyms, expansions, former titles, common misspellings. An alias must be substitutable for the title; topics and related concepts belong in `keywords`, not here. On rename, add the old title as an alias.
- **`keywords`** are free-text search synonyms: 4-8 distinctive, lowercase terms a person would actually search that are not already in the title. Prefer terms specific to this file over generic words every file shares, and include the problem phrasing people type. This is the deliberate free-text exception to the closed-vocabulary tag rule (Constitution Article VII): subject matter lives here, never in `tags`.

### 8.8 Field Bands and Obsidian Display

The fields are grouped into two bands by who uses them, and emitted in this order in every file:

- **Human band (shown):** `title`, `description`, `status`, `tags`, `aliases`, `keywords`, `created`, `updated`. The fields a person reads or edits.
- **System band (hidden):** `type`, `folder`, `layer`, `policy`, `author`, `path`, `id`. Derived from location, or constant in a personal vault. They stay in the file and the vault's scripts read them; they are only hidden from the Obsidian editor to cut clutter.

Hiding is done with a CSS snippet at `.obsidian/snippets/brain-hide-system.css` (enable under Settings -> Appearance -> CSS snippets), which targets each system key by name. It is display-only: every field remains present in the YAML and required exactly as before. The dates are unquoted ISO so Obsidian types them as Date (8.1).

When creating or rewriting any file, emit fields in the two-band order above so the property panel reads cleanly on devices both with and without the snippet. The order is a readability convention, not a parser requirement: the scripts read fields order-independently, so a file is never wrong for ordering alone, but new and edited files should follow it.

### 8.9 Schema Changes Propagate to Every File

**The standard frontmatter schema is vault-wide: when it changes, every existing file adopts the change in the same edit, not lazily as files happen to be touched.** A schema change that lands on new files only, leaving old files on the prior shape, is an incomplete change and a lint failure, never an acceptable end state. The schema is a contract every BRAIN document honors at once.

**What "standard frontmatter" means here:** the universal field set defined in 8.1 (the two-band schema every markdown file carries: `title` through `id`). Adding a universal field, removing one, renaming one, or changing its required form or allowed values is a standard-schema change and triggers this rule.

**The migration is part of the change (do all of it, in order):**

1. Update the schema definition in 8.1 (and 8.7/8.8 if bands or discovery fields shift).
2. Update the scripts and scaffolds: `REQUIRED_FIELDS` and the vocabulary in `.github/scripts/vault.py`, any rule in `lint-notes.py`, and every `.template/` file that carries frontmatter.
3. Backfill every existing markdown file to the new shape, in the same commit.
4. Run `check-vault.py`: the change is done only when zero files report a schema error. `lint-notes.py` checks `REQUIRED_FIELDS` presence on every file, so a newly required field surfaces as an error on each non-conformant file until backfilled. The rule is machine-checked, not merely policy.

**Scope boundary (do not over-apply this rule):** it governs the *standard, universal* schema only. A field deliberately scoped to one class of file is **not** part of the standard frontmatter, is **not** added to 8.1, and is **not** backfilled across the vault: it lives only on the files it applies to. The built-in example is a team roster's `members` and `lead`: only rosters carry them, so a change to how they work touches the rosters alone, never the whole vault. If a future field is added for one file type (documented where that type is defined, such as `Memory/Memory.md` for session summaries), introduce it by documenting its scope there, never by amending 8.1. The corollary: reach for a scoped field only when no universal field already carries the meaning. Staleness, for instance, is not a scoped field, it is the universal `status` (deprecated/archived), so retrieval honors it everywhere rather than duplicating it per file type.

---

## 9. Session Initialization Checklist

At the start of every session, in this order:

1. **Read the governance pair** - this file (`Instructions.md`) and `Constitution.md`, or confirm both have been read this session
2. **Check `Inbox/`** - if files are present, analyze and prompt the user per Section 7
3. **Read `Memory/Log.md`** - restore recent context and check for open loops
4. **Load `Memory/Context/Current/`** - auto-load the **2 most recent completed** session summary files to restore immediate continuity (see Section 13)
5. **Read `Profile/Working Style.md`** - confirm operating style for this session
6. **Orient on what exists** - skim the folder hub docs (`Projects/Projects.md`, `Ventures/Ventures.md`, `Library/Library.md`) or read the catalog (`System/Data/catalog.ndjson`) for current projects, ventures, and knowledge domains
7. **Read any project, venture, or library files** relevant to what the user is working on

In Claude Code, the SessionStart hook runs `.github/scripts/session-hooks.py start`, which prints a compact card naming the startup set, the newest live session summaries and anything waiting at the Inbox, as paths rather than whole files, since a hook's output is cut short; Reading every listed file completes steps 1 to 6. Elsewhere, read them yourself in the order above.

Do not skip steps 1-6. They are the minimum required to operate with full context: they load exactly the four files tagged `startup` (Constitution, Instructions, Working Style, Memory/Log) plus the Inbox check and the latest `Memory/Context/Current/` summaries, and step 6 orients on what exists via the folder hubs or the catalog. The hook reads the `startup` tag, so the tag alone decides the set.

> **Before searching the web for any factual question, search the BRAIN first.** Search the notes, or check the relevant folder directly. Only reach for external sources if the BRAIN has no answer or the information needs to be verified for currency.

---

## 10. Changes Are Commits

**The vault is a git repository, and its history is the backup.** Every committed state of every file can be restored (`git restore <path>`, or `git checkout <commit> -- <path>`), so there are no snapshot copies to take before an edit and none to clear afterwards (Constitution 3.1).

### 10.1 Keeping a State

Commit meaningful states often, and always before a risky or wide edit, so the state you might want back is in the history. A Conventional Commits message says what changed and why; together the messages are the BRAIN's change record (Constitution 3.6). Never delete, or overwrite wholesale, a file that holds uncommitted work.

### 10.2 After Making Changes

Tell the user which files changed and what is not yet committed. Before committing, run `python3 .github/scripts/check-vault.py` and fix what it finds; `update-vault.py` redraws anything generated that it reports as stale.

### 10.3 Undoing a Change

To undo an uncommitted edit, restore the file from the last commit (`git restore <path>`); to undo a committed one, revert the commit or check the older version out. Confirm with the user before discarding any work they have not seen.

---

## 11. Maintaining This BRAIN

You are expected to keep this system current. Specific responsibilities:

- **Update Memory files** after sessions where events occurred, decisions were made, or new people or dates surfaced (facts/traits about the user go to `Profile/`, not Memory)
- **Update Project files** when work is done on a project - update `Overview.md` status, add to `Log.md`
- **Promote `Memory/Log.md` entries** when they qualify: write the entry file into its collection (Entities, Decisions, Events, Insights) in the format the collection's note shows, or a row into `Memory/Dates.md`, and let `update-vault.py` redraw the collection's index. Anything learned about *who the user is* is proposed into `Profile/` (Constitution 4.2), never stored in Memory (see `Memory/Memory.md`)
- **Run the Memory Consolidation Loop** (`System/Workflows.md`) periodically: deduplicate, merge, and supersede Memory entries so the memory layer stays lean and contradiction-free
- **Check memory before accepting premises.** When a user request embeds a factual assumption (a job, a location, a project state), verify it against current Memory before acting on it. If Memory contradicts the premise, surface the conflict instead of silently adopting either version - stale-memory conflicts are a documented failure mode of AI memory systems
- **Suggest file additions** when a conversation reveals a knowledge gap that a new source would fill
- **Never silently rename, delete, or restructure folders at Layer 0 or Layer 1** without explicit user confirmation
- **Hidden folders are infrastructure, not junk.** `.obsidian/` (vault config), `.git/` (the history every recovery rests on, Constitution 3.1), `.github/` (the vault's scripts, CI and repository files), and `.claude/` (Claude Code harness config: `settings.json` defines the hooks that force the Section 9 startup checklist to run on every session and after `/clear`, and `hooks/` holds the injected skill-router and per-prompt reminder notes that reinforce skill auto-triggering; the scripts skip `.claude/` like any dot-prefixed folder, so it stays out of lint and the link graph) are intentional and must never be deleted, even during cleanup - empty or not. Only transient artifacts are clearable junk: `__pycache__/`, `*.pyc`, `._*` AppleDouble files. **`.DS_Store` is neither junk nor content - ignore it completely.** Never delete, move, report, or count it, anywhere in the BRAIN; macOS owns and regenerates it, and `.gitignore` keeps it out of version control. When in doubt, ask.
- **Empty folders carry a `.gitkeep` - mandatory.** Every empty folder in the BRAIN holds a `.gitkeep` so the structure survives git, zips, and sync tools; the moment a folder gains real files, its `.gitkeep` is removed. Both directions are standing policy: `update-vault.py` adds and removes them, and `check-vault.py` fails on a missing or stale one, so never hand-manage these files. `.gitkeep` is infrastructure - it is not content and never gets frontmatter or tags. One scoped exception to shipping: inside a skill package, each unused mandatory folder carries a `.gitkeep` (the develop skill's v1.5.0 convention), so those markers do ship in `.skill` archives.
- **Commit each change with a Conventional Commits message.** The history is the changelog (Constitution 3.6); there is no changelog file to update and no version to bump.

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

Related folders connect through their common parent, never laterally. `.template/` folders and skill sources stay out of the graph entirely; each skill's graph node is its packaged `.skill` artifact, linked from `Skills.md` as a sibling file. `check-links.py` rejects violations, including any link from a content file. The Memory tier docs under `Memory/Context/` are ordinary hub-and-spoke: `Memory.md` links `Context.md`, and `Context.md` links the tier docs (`Current`/`Recent`/`Archive`); the tier docs do not link each other (Constitution 3.7 rule 7). There are no sanctioned lateral folder-doc links anywhere in the BRAIN.

### 12.3 Leverage Backlinks - Never Link Back
Because you are explicitly linking files, Obsidian automatically generates **Backlinks** (showing what files link to the current one). This is why the cascade rule exists (Constitution 3.7): a file never wikilinks back to a file that links to it - the reverse relationship is already visible in the backlink pane, so a return link is duplication, not connection. Links flow downhill (root → namesake docs → folder files); upward references are plain code-style paths. `check-links.py` rejects reciprocal pairs.

### 12.4 Where Wikilinks Are Forbidden
Any `.template/` folder must **never** contain wikilinks (Constitution Article 3.7). Templates hold blank scaffolds, not knowledge-graph nodes. Reference other files by plain text or plain path there, and the linter rejects wikilinks. The prohibition runs both directions: templates contain no wikilinks and nothing links *to* a template (reference scaffolds by plain path - a template link invites Obsidian to create stray notes and drags scaffolds into the graph).

---

## 13. Context Handoff & Tiered Memory

### 13.1 Summary Triggers (Layered - never wait for a threshold)

You cannot read your own context meter, so the system layers three triggers, strongest first:

1. **Host warnings.** If the platform you run on surfaces a context or compaction warning, treat it as authoritative and act immediately.
2. **Task-boundary checkpointing - the primary habit.** After every completed major task or milestone, update the running session summary (same-session overwrite, see [[Memory/Memory|Memory/Memory.md]]). Research is unambiguous: mandated checkpoints at task boundaries preserve continuity; waiting for pressure thresholds loses detail, and passive "summarize when needed" intentions barely work at all.
3. **The saturation heuristic (floor).** Long conversation, topic cycling, earlier context fading - if you notice these, checkpoint now.

A summary that exists *before* pressure hits is the whole point: if context resets unexpectedly, the checkpoint is already on disk.

### 13.2 The Pipeline

Summaries are timestamped files (`YYYYMMDD-HHMMSS.md`) that cascade through capped tiers:

| Tier | Directory | Max | Purpose |
|------|-----------|-----|---------|
| 1 | `Memory/Context/Current/` | **3** | Active session summaries (2 historical + 1 running) |
| 2 | `Memory/Context/Recent/` | **6** | Recent historical summaries |
| 3 | `Memory/Context/Archive/<year>/` | **unbounded** | Lifetime cold storage - nothing is ever deleted |

After saving a summary, run `python3 .github/scripts/update-vault.py` to enforce the caps (the Stop hook runs it too); Recent overflow archives by year. The archive is never loaded at session start; reach it by searching it on explicit request.

### 13.3 The Canonical Detail

The summary compilation format (delta updates with explicit supersession), mandatory sections, file naming and frontmatter, the same-session overwrite exception, the handoff notice, and the natural-language recall mapping ("check your recent memory…") all live in [[Memory/Memory|Memory/Memory.md]]. **Read it before compiling a summary.**

---

## 14. Context Assembly & the Lost-in-the-Middle Rule

Language models reliably attend to the **beginning** and the **end** of a long context, but under-weight material in the **middle** - the "Lost-in-the-Middle" effect. A fact buried mid-context is frequently missed even though it is present. This section governs how to assemble context so the BRAIN never depends on the model recalling something from a low-attention position.

### 14.1 Primary Defense: Retrieve Lean, Not Whole

The BRAIN is a structured retrieval system, and that structure is itself the main protection against Lost-in-the-Middle. A short, targeted context has no vulnerable middle.

- **Load the minimal relevant set, never the entire vault, for routine work.** Use the Section 4.1 lookup table, the catalog, and frontmatter filters to pull only what the task needs.
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
- The Section 4.1 lookup table and the catalog exist so you rarely need a long context at all - use them first.

### 14.5 Token-Format Economy

Measured tokenizer facts that govern how content is written and assembled here:

- **Stable content first, volatile content last.** The Section 14.2 ordering (governance → reference → current context) is also the cache-optimal ordering: every major provider's prompt caching rewards an identical stable prefix, and a timestamp or session-specific value placed early breaks it. Never lead an assembled context, or a frequently loaded file, with anything that changes per session.
- **ASCII over decoration in anything an AI ingests.** Box-drawing characters cost 3-10x their ASCII equivalents in common tokenizers (`═` is the worst offender). The vault's scripts print plain ASCII for this reason; follow the same rule in generated reports and tool output.
- **Pick the cheap format for the data's shape.** For bulk tabular data, CSV/TSV costs roughly a third of JSON; minified JSON beats pretty-printed by ~40%; XML is always the most expensive. Markdown tables cost more than prose for simple facts - use tables where scanning matters, prose where it doesn't. Frontmatter arrays stay inline (`["a", "b"]`), which is ~30% cheaper than block lists and is already the schema standard.
- **Compression is the wrong tool here.** Summarizing or compressing vault files to save tokens trades away exact wording, which Memory and Library depend on. The BRAIN's economy comes from loading less, not from degrading what's loaded.
