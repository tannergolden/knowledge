<!--
title: "Inbox - Staging Area"
description: "Drop any unsorted file here. The AI analyzes, proposes a destination, enriches with frontmatter or macOS metadata, and asks for sorting confirmation. Held sub-homes (Reports, Visuals, and the standing teams) live here but are never sorted."
type: "index"
keywords: ["staging area", "drop files", "unsorted", "sorting protocol", "pdf cleanup", "file triage", "where to put files", "hold folder"]
-->

# 📥 Inbox/

## Rules

- **Check `Inbox/` at the start of every session**, even when nothing is likely to be there, and sort what waits before other work. If the check is slow, finish it quietly, then report.
- **Nothing leaves unenriched.** A note gets its frontmatter, and any file a clean name, before it moves. No exceptions.
- **Nothing moves without a yes.** Propose each file's destination and clean name, and wait for your user to confirm.
- **Never delete a file here without confirmation.** Leaving it at the `Inbox/` root is the safe default.
- **The held sub-homes are never sorted**: `Reports/`, `Visuals/`, `Ideas/`, `Faculties/` and `Backups/`.
- **A new folder only to fit a file.** During a sort, when no folder fits, you may propose one three or more levels down; one directly inside a top folder needs your user's explicit direction, and a top folder never.
- **Offer cleanup for outside PDFs first**, and copy the originals into `Inbox/Backups/` before changing anything.
- Follow the sorting protocol below, step by step.

A staging area for any file you want the AI to sort into the BRAIN. Drop files here freely. Any format, any topic, organized or not. The AI handles the rest.

## What `Inbox/` Is (a meta-zone, not just an inbox)

`Inbox/` is a small **meta-zone**, not a single pure inbox. It holds five things kept deliberately distinct - the pattern Johnny.Decimal uses for its `00-09` area, where an inbox and an archive coexist as siblings:

1. **The inbox proper** - loose files dropped at `Inbox/` root, plus the sort protocol below. This is the only transient part: it is processed to empty.
2. **`Reports/`** - the held reports library (`Inbox/Reports/Reports.md`): the finished research and discovery reports, fully indexed and **excluded from the sort sweep**; held here, not sorted into the BRAIN, and good for up to three months before they must be re-verified.
3. **`Visuals/`** - the held visuals library (`Inbox/Visuals/Visuals.md`): the finished charts, diagrams, dashboards, and illustrations from the visualize skill, fully indexed and **excluded from the sort sweep**; held here as archival artifacts, not sorted into the BRAIN, and kept until superseded.
4. **`Ideas/`** - the held idea pool (`Inbox/Ideas/Ideas.md`): the living library of idea records the Discovery team generates, dispatched by the discover skill, fully indexed and **excluded from the sort sweep**; held here by lifecycle status (raw, shortlisted, developed, promoted, parked, killed), not sorted into the BRAIN, with killed ideas kept so the team never re-treads a dead end.
5. **`Faculties/`** - the standing-teams home (`Inbox/Faculties/Faculties.md`): the four cognitive teams Research, Discovery, Editorial, and Design, and the Finance team, with their agents, fully indexed and **excluded from the sort sweep**; their finished work sorts outward to its real home.

`Reports/`, `Visuals/`, `Ideas/`, and `Faculties/` are therefore **distinct, held lists that live at the inbox path - not contents of the inbox.** "Process the inbox to empty," and any "is the inbox empty?" check, apply only to the loose files at the root; they never count `Reports/`, `Visuals/`, `Ideas/`, or `Faculties/`. This is a deliberate, documented exception to the inbox-is-transient rule.

## What Happens When You Drop a File Here

1. At the next session start, the AI detects new files in this folder
2. If any are PDFs, the AI asks whether to run cleanup (removes piracy watermarks, malicious links, shadow library branding) or trust the source
3. The AI analyzes each file and determines where it should go in the BRAIN
4. The AI proposes both a destination and (if needed) a clean filename, then asks you to confirm
5. After confirmation, the AI adds the required frontmatter to each text file (a binary file carries none) before moving anything

**Nothing gets moved without your approval.**

## What Belongs in the Inbox

The Inbox is designed for things that already have a place in the BRAIN but need to be filed:

- Documents, notes, articles you want to keep as reference
- Personal media, photos, audio, video that fits an existing folder
- Project files, drafts, exports
- Anything you'd otherwise have to manually categorize

## What Doesn't Belong

Some files are better deleted or kept somewhere else entirely:

- Random downloads, accidentally dropped files, temporary work files
- System junk (`.DS_Store`, `.cache`, etc.). The AI ignores these automatically.
- Executables, archives, or installers. Not reference material.
- Anything you wouldn't want a portable knowledge layer to carry around forever

If you drop one of these and the AI sees no good home, it'll ask whether to delete it or return it to a location of your choice.

## The `Reports/` Subfolder

`Inbox/Reports/` is the held library for finished research and discovery reports. The Research team and the Discovery team file their reports here. See [[Inbox/Reports/Reports|Reports.md]] for the held-not-sorted rule, the three-month freshness rule (a report older than three months must be verified before it is reused), and the index rule (`Reports.md` is the one hub that wikilinks every report; no other file links to one). Like the team homes, it is fully linted and cataloged, and excluded only from the session-start sort sweep.

## The `Visuals/` Subfolder

`Inbox/Visuals/` is the held library for finished visuals from the `visualize` skill: standalone charts, diagrams, dashboards, interactive widgets, and explanatory illustration filed by the Design team. See [[Inbox/Visuals/Visuals|Visuals.md]] for the held-not-sorted rule, the archival retention (a saved visual is a snapshot kept until superseded, carrying the date of its underlying data rather than a fixed expiry), and the index rule (`Visuals.md` is the one hub that wikilinks every held visual; no other file links to one). Like `Reports/`, it is fully linted and cataloged, and excluded only from the session-start sort sweep. Most visuals render inline and are never saved; only one the Founder asks to keep is filed here or in a named home.

## The `Ideas/` Subfolder

`Inbox/Ideas/` is the held idea pool for the `discover` skill: the living library of idea records the Discovery team generates and ranks. See [[Inbox/Ideas/Ideas|Ideas.md]] for the held-not-sorted rule, the living-pool retention (ideas persist by lifecycle status, and killed and parked ideas are kept so the team dedups against them and never re-treads a dead end), and the leaf rule (an idea record links to nothing; the pool is found by search and by status, not by an index of links). The idea schema and the ICE, Elo, RICE, lifecycle, and lineage rules are the Discovery team's method, in `Inbox/Faculties/Discovery/Discovery.md`. Like `Reports/`, it is fully linted and cataloged, and excluded only from the session-start sort sweep.

## The `Faculties/` Subfolder

`Inbox/Faculties/` is the home for the BRAIN's five standing functional teams, the **Faculties**: Research (evidence), Discovery (ideas), Editorial (writing), Design (visuals), and Finance (personal money). It is a multi-team home, the same shape Agent Resources (AR) uses, and the personal-work counterpart to AR's venture workforce. See [[Inbox/Faculties/Faculties|Faculties.md]] for the rosters, each team's standard, the skill that dispatches it, and the federation with AR. Like `Reports/`, it is a permanent home, fully linted and cataloged, and excluded only from the session-start sort sweep. The teams keep no library of their own here: a finished report, build, piece of writing, or financial plan sorts outward to its real home.

## Bulk Drops

You can drop dozens or hundreds of files at once. When more than 5 files are detected, the AI switches to a table-format confirmation so the proposed sort stays readable. You can approve all, approve some, or redirect individual files in your response.

## The Sorting Protocol (Canonical)

This is the complete sorting protocol; the Rules above are its always-on essentials.

The `Inbox/` folder is a staging area where the user can drop any file (organized or not, any format) for the AI to process and route into the correct part of the BRAIN.

### 1. Detection

At every session initialization, automatically check whether `Inbox/` contains any sortable files. If it does, proceed to analysis before doing anything else.

**What counts as a sortable file:**

Detection scans only files that are eligible for sorting. The following are excluded:

- [[Inbox/Inbox|Inbox/Inbox.md]] (permanent fixture, never sorted)
- Hidden files and directories (any name starting with `.`, including `.DS_Store`, `.gitkeep`, `.localized`)
- `Inbox/Backups/` and any timestamped backup subfolders inside it (pre-cleanup snapshots)
- The `Inbox/Reports/` subfolder and everything inside it (the held reports library; see "The `Reports/` Subfolder" above). It stays linted and cataloged; it is excluded from sort-detection only.
- The `Inbox/Visuals/` subfolder and everything inside it (the held visuals library; see "The `Visuals/` Subfolder" above). It stays linted and cataloged; it is excluded from sort-detection only.
- The `Inbox/Ideas/` subfolder and everything inside it (the held idea pool; see "The `Ideas/` Subfolder" above). It stays linted and cataloged; it is excluded from sort-detection only.
- The `Inbox/Faculties/` subfolder and everything inside it (the standing-teams home, holding Research, Discovery, Editorial, Design, and Finance; see "The `Faculties/` Subfolder" above). It stays linted and cataloged; it is excluded from sort-detection only.
- Files modified within the last 30 seconds (may still be syncing or copying; recheck after a short wait)

If no eligible files remain after these exclusions, treat the Inbox as empty and continue with the session.

### 2. The Held Sub-Homes (Not Sorted)

`Inbox/` holds four permanent sub-homes that are never sorted: `Reports/` (the held research and discovery reports), `Visuals/` (the held visuals from the visualize skill), `Ideas/` (the held idea pool from the discover skill), and `Faculties/` (the five standing teams, each its own roster of agents). The session-start card leaves all four out of sort-detection, so their contents are never scanned, surfaced, or proposed for routing at session start. They are not invisible: they stay fully linted and cataloged like any other vault content. Only the loose files at the `Inbox/` root are subject to the sorting protocol below.

### 3. PDF Pre-Processing

PDFs from external sources frequently contain piracy watermarks, shadow library branding (Z-Library, OceanofPDF, Anna's Archive), and malicious link annotations. These must be cleaned before the file enters the BRAIN.

**Before running cleanup, the AI asks the user:**

> *"I see [N] PDF(s) in the Inbox. Should I run cleanup (recommended for external downloads) or skip it (if these are from a trusted source like a publisher, personal scan, or official download)?"*

If the user confirms cleanup or doesn't answer clearly, proceed with cleanup. If the user explicitly trusts the source, skip directly to analysis (step 4).

**To run cleanup**, the AI performs it directly with whatever PDF tooling its environment provides (e.g., PyMuPDF via a short Python script, or the host platform's PDF tools). There is no bundled cleanup script. The rules below are the contract any cleanup must honor:

- **Back up first, always.** Before modifying anything, copy the original PDFs into a timestamped subfolder under `Inbox/Backups/` (a hyphenated timestamp, never underscores).
- Remove clickable link annotations pointing to shadow library domains (z-library, OceanofPDF, Anna's Archive, and the like)
- Erase watermark text baked into page content streams
- Delete an entire page only when it is clearly a shadow library advertisement and nothing else. Never touch pages with real content, blank pages, image-only pages, or internal PDF links.
- If the environment has no PDF tooling at all, skip cleanup, tell the user, and route the files unmodified or leave them at the `Inbox/` root at the user's choice.

After cleanup completes, proceed to step 4 to analyze and route the files.

### 4. User Confirmation

Analyze each eligible file and determine both its destination and (if appropriate) a cleaner filename. Then present the proposed sort to the user for confirmation. **Combine renaming and routing into one decision** so the user confirms both in a single response.

**Up to 5 files (inline format):**

> *"I found [N] file(s) in the Inbox. Here's where I'd route them:*
> *- `original-name.pdf` → rename to `Clean Name.pdf` → `Library/Life & Practice/Health & Wellness/`*
> *- `notes.md` → `Memory/Log.md` (append)*
>
> *Want me to sort them now?"*

**More than 5 files (table format):**

| Original Name | Proposed New Name | Destination |
|---|---|---|
| ... | ... | ... |

**Partial confirmation is supported.** The user may approve some files and decline or redirect others. Possible responses include:

- "Sort all of them"
- "Skip [filename(s)]"
- "Send [filename] to [different path] instead"
- "Sort everything except [filename(s)]"

Do not move any file without explicit approval for that file.

### 5. Pre-Sorting Enrichment

**No file may be moved from `Inbox/` to its destination in a raw, un-enriched state.** Before moving any file, apply the appropriate enrichment.

**Order of operations:**

1. Apply the rename (if a rename was approved in step 4)
2. For files destined for `Library/`, assess freshness lifespan by the Library's tiers (`Library/Library.md`, Rules). If ephemeral (<5 years), redirect to `Projects/`, `Ventures/`, `Memory/`, or deletion with user confirmation. Do not file ephemeral content in the Library.
3. Enrich with frontmatter (text/markdown); a binary carries none. For Library files, lead the keywords with the freshness token (`freshness/timeless`, `freshness/enduring` or `freshness/current`).
4. Move to destination

**Filename hygiene (check before enrichment):**

If the incoming filename is messy, hard to parse, uses underscores as word separators, or contains garbled characters or excessive punctuation, the rename should already have been proposed in the confirmation step (step 4). Underscores are never used as word separators. Use spaces or hyphens.

Examples: `my_report_v2_FINAL(1).pdf` → `My Report.pdf`, `export_2024_03_07.csv` → `Export 2024-03-07.csv`.

**Text / Markdown files:**

- Add the hidden frontmatter (`.docs/technical/vault/Note-Schema.md`) before moving
- Fill in `title`, `description` and `type`, with `keywords` where they help

**Binary / Non-Editable files (images, PDFs, audio, video, scripts, etc.):**

These cannot embed frontmatter, so they carry none (`.docs/technical/vault/Note-Schema.md`): the folder they are filed into places them, and that folder's note describes them. Give each a clean, descriptive name before it moves, so its subject is plain from the name, and keep anything sensitive out of the name.

### 6. Ambiguous File Handling

If a file's contents do not clearly match one specific folder, assign it to the closest, most appropriate existing folder based on subject matter. Then log the reasoning in `Memory/Log.md` so the user can review the decision later. Do not embed routing notes in the file's frontmatter.

**Log entry format:**

```markdown
### [Date] - Sort routing: [filename]

**Routed to:** [destination path]
**Why:** [brief explanation of the ambiguity and why this folder was chosen]
**Alternatives considered:** [folders that were close but not chosen]
```

These entries are governed by the `Memory/Log.md` retention policy under the "Inbox sort routing notes" row.

### 7. Duplicate Filename Handling

If a file being sorted from `Inbox/` would collide with an existing file at the destination, **stop and ask the user** before resolving. Present the options:

- **Rename the incoming file** (AI proposes a non-colliding name)
- **Overwrite the existing file** (destructive, confirm twice)
- **Skip this file** (leave it in `Inbox/` for later handling)
- **Keep both** (AI appends a suffix to one of them)

Do not silently pick an option. Wait for the user's choice.

### 8. Files That Don't Belong in BRAIN

Some files dropped into the Inbox don't belong anywhere in the BRAIN: random junk, accidental drops, screenshots from another context, temporary files.

When the AI's analysis finds no reasonable destination, ask the user:

> *"`[filename]` doesn't seem to fit anywhere in the BRAIN. Should I delete it, move it back out of the Inbox to a location you specify, or leave it at the `Inbox/` root for you to decide later?"*

Never delete a file from the Inbox without explicit user confirmation (`AGENTS.md`, Ask first). Leaving it at the `Inbox/` root is the safe default if the user doesn't respond.

### 9. Dynamic Subfolder Creation

If no existing folder is a reasonable fit for a file, you may request permission to create a new subfolder:

> *"I couldn't find a good match for [filename]. I'd suggest creating a new subfolder at [proposed path]. Is that okay?"*

**Strict constraint:** You may never create or propose a new folder at Layer 0 (root) or Layer 1. Layer 2 folders require explicit user confirmation before creation (`AGENTS.md`, Ask first). For the Inbox sorting protocol specifically, proposed new folders must be Layer 3 or deeper unless the user explicitly directs a Layer 2 creation.

### 10. Routing System Assets (Skills, Utilities)

Some Inbox items are system assets rather than personal content. Route them into the `System/` subfolders `System/System.md` describes:

- **Skill directories** (a folder containing `SKILL.md` and its supporting files) → `System/Skills/`, preserved as a folder, never flattened. Subagents live inside the skill's own `agents/` folder.
- **General prompt snippets, workflows, or loose templates** → `System/Utilities/`

Follow the standard sorting protocol: confirm the move, fully move the item out of `Inbox/` so no duplicate is left behind, and apply naming hygiene - strictly no underscores anywhere in the file or folder name (`AGENTS.md`, Conventions); use kebab-case, spaces, or PascalCase. Skill directories keep the external `SKILL.md` format and are exempt from BRAIN frontmatter (the note schema does not apply to them); utility `.md` files take standard BRAIN frontmatter.
