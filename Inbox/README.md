<!--
title: "Inbox - Staging Area"
description: "The staging area: drop any unsorted file here, and it is enriched and filed where it belongs, each move proposed and confirmed first. Held sub-homes (Reports, Visuals and Ideas) live here but are never sorted."
type: "index"
keywords: ["staging area", "drop files", "unsorted", "sorting protocol", "pdf cleanup", "file triage", "where to put files", "hold folder"]
-->

# 📥 Inbox/

Anything waiting to be filed lands here: a document, a PDF, a photo, an export, a note written in a hurry. Each loose file is given a home and a clean name, enriched, and moved only once the owner confirms the move. Read this README before changing anything in this folder; its rules add to the root `README.md` and never loosen it.

## Rules

- **Check `Inbox/` at the start of every session**, even when nothing is likely to be there, and sort what waits before other work. If the check is slow, finish it quietly, then report.
- **Nothing leaves unenriched.** A note gets its frontmatter, and any file a clean name, before it moves. No exceptions.
- **Nothing moves without a yes.** Each file's destination and clean name are proposed first, and the owner confirms them.
- **No file here is deleted without confirmation.** Leaving a file at the `Inbox/` root is the safe default.
- **The held sub-homes are never sorted**: `Reports/`, `Visuals/`, `Ideas/` and `Backups/`.
- **A new folder only to fit a file.** During a sort, when no folder fits, a new folder three or more levels down may be proposed; one directly inside a top folder needs the owner's explicit direction, and a top folder is never created.
- **Outside PDFs are offered cleanup first**, and their originals are copied into `Inbox/Backups/` before anything changes.
- The sort follows the protocol below, step by step.

## What `Inbox/` Is (a meta-zone, not just an inbox)

`Inbox/` is a small **meta-zone**, not a single pure inbox. It holds things kept deliberately distinct, the pattern Johnny.Decimal uses for its `00-09` area, where an inbox and an archive coexist as siblings:

1. **The inbox proper**: loose files dropped at the `Inbox/` root, plus the sort protocol below. This is the only transient part: it is processed to empty.
2. **`Reports/`**: the held reports library (`Inbox/Reports/README.md`), where finished research and discovery reports land. Fully indexed and **excluded from the sort sweep**; held here, not sorted into the BRAIN, and good for up to three months before a report must be re-verified.
3. **`Visuals/`**: the held visuals library (`Inbox/Visuals/README.md`), where finished charts, diagrams, dashboards and illustrations land. Fully indexed and **excluded from the sort sweep**; held as archival artifacts, not sorted into the BRAIN, and kept until superseded.
4. **`Ideas/`**: the held idea pool (`Inbox/Ideas/README.md`), where idea records land, one idea to a file. Fully indexed and **excluded from the sort sweep**; held by lifecycle status (raw, shortlisted, developed, promoted, parked, killed), not sorted into the BRAIN, with killed ideas kept so a dead end is never re-trodden.

`Reports/`, `Visuals/` and `Ideas/` are therefore **distinct, held lists that live at the inbox path, not contents of the inbox.** "Process the inbox to empty", and any "is the inbox empty?" check, apply only to the loose files at the root; they never count `Reports/`, `Visuals/` or `Ideas/`. This is a deliberate, documented exception to the inbox-is-transient rule.

## What Happens When A File Is Dropped Here

1. At the next session start, the file is detected (`session.py start` lists each loose file on an `INBOX` line).
2. If any are PDFs, the owner is asked whether to run cleanup (which removes piracy watermarks, malicious links and shadow-library branding) or to trust the source.
3. Each file is analyzed for where it belongs in the BRAIN.
4. A destination and, where needed, a clean file name are proposed together, and the owner confirms them.
5. After confirmation, each text file gets the required frontmatter (a binary file carries none) before anything moves.

**Nothing is moved without the owner's approval.**

## What Belongs In The Inbox

The Inbox is for things that already have a place in the BRAIN but need to be filed:

- Documents, notes and articles to keep as reference
- Personal media, photos, audio and video that fit an existing folder
- Project files, drafts and exports
- Anything that would otherwise have to be categorized by hand

## What Doesn't Belong

Some files are better deleted or kept somewhere else entirely:

- Random downloads, accidentally dropped files, temporary work files
- System junk (`.DS_Store`, `.cache` and the like), which the sort ignores
- Executables, archives or installers, which are not reference material
- Anything a portable knowledge layer should not carry around forever

When one of these is dropped and no good home exists, the owner is asked whether to delete it or return it to a location of their choice.

## The `Reports/` Subfolder

`Inbox/Reports/` is the held library for finished research and discovery reports. [[Inbox/Reports/README|Reports]] sets the held-not-sorted rule, the three-month freshness rule (a report older than three months is verified before it is reused) and the index rule (that README is the one hub that wikilinks every report; no other file links to one). Like the other sub-homes, it is fully linted and cataloged, and excluded only from the session-start sort sweep.

## The `Visuals/` Subfolder

`Inbox/Visuals/` is the held library for finished standalone visuals: charts, diagrams, dashboards, interactive widgets and explanatory illustration. [[Inbox/Visuals/README|Visuals]] sets the held-not-sorted rule, the archival retention (a saved visual is a snapshot kept until superseded, carrying the date of its underlying data rather than a fixed expiry) and the index rule (that README is the one hub that wikilinks every held visual; no other file links to one). Like `Reports/`, it is fully linted and cataloged, and excluded only from the session-start sort sweep. Most visuals are shown once and never saved; only one the owner asks to keep is filed here or in a named home.

## The `Ideas/` Subfolder

`Inbox/Ideas/` is the held idea pool: the living library of idea records, generated and ranked during discovery work. [[Inbox/Ideas/README|Ideas]] sets the held-not-sorted rule, the living-pool retention (ideas persist by lifecycle status, and killed and parked ideas are kept so every new idea is checked against them and no dead end is re-trodden) and the leaf rule (an idea record links to nothing; the pool is found by search and by status, not by an index of links). Like `Reports/`, it is fully linted and cataloged, and excluded only from the session-start sort sweep.

## Bulk Drops

Dozens or hundreds of files can be dropped at once. When more than five wait, the proposed sort comes as one table so it stays readable, and the owner can approve all, approve some, or redirect individual files.

## The Sorting Protocol (Canonical)

This is the complete sorting protocol; the Rules above are its always-on essentials. `Inbox/` is a staging area where the owner can drop any file (organized or not, any format) to be processed and routed into the right part of the BRAIN.

### 1. Detection

At the start of every session, `Inbox/` is checked for sortable files. If any wait, they are analyzed before anything else.

**What counts as a sortable file.** Detection scans only files that are eligible for sorting. These are excluded:

- This README (a permanent fixture, never sorted)
- Hidden files and folders (any name starting with `.`, including `.DS_Store`, `.gitkeep` and `.localized`)
- `Inbox/Backups/` and any timestamped backup subfolders inside it (pre-cleanup snapshots)
- The `Inbox/Reports/` subfolder and everything inside it (the held reports library). It stays linted and cataloged; it is excluded from sort detection only.
- The `Inbox/Visuals/` subfolder and everything inside it (the held visuals library). It stays linted and cataloged; it is excluded from sort detection only.
- The `Inbox/Ideas/` subfolder and everything inside it (the held idea pool). It stays linted and cataloged; it is excluded from sort detection only.
- Files modified within the last 30 seconds (they may still be syncing or copying; recheck after a short wait)

If no eligible files remain after these exclusions, the Inbox counts as empty and the session goes on.

### 2. The Held Sub-Homes (Not Sorted)

`Inbox/` holds three permanent sub-homes that are never sorted: `Reports/` (the held research and discovery reports), `Visuals/` (the held visuals) and `Ideas/` (the held idea pool). The session-start card leaves all three out of sort detection, so their contents are never scanned, surfaced or proposed for routing at session start. They are not invisible: they stay fully linted and cataloged like any other vault content. Only the loose files at the `Inbox/` root are subject to the sorting protocol below.

### 3. PDF Pre-Processing

PDFs from outside sources often carry piracy watermarks, shadow-library branding (Z-Library, OceanofPDF, Anna's Archive) and malicious link annotations. These are cleaned before the file enters the BRAIN.

**Before cleanup, the owner is asked:**

> _"[N] PDF(s) wait in the Inbox. Run cleanup (recommended for outside downloads), or skip it (for a trusted source such as a publisher, a personal scan or an official download)?"_

If the owner confirms cleanup, or does not answer clearly, cleanup runs. If the owner trusts the source, analysis (step 4) follows directly.

**Cleanup** is done with whatever PDF tooling is at hand (for example PyMuPDF in a short Python script, or the platform's own PDF tools). There is no bundled cleanup script. Any cleanup honors this contract:

- **Back up first, always.** Before anything is modified, the original PDFs are copied into a timestamped subfolder under `Inbox/Backups/` (a hyphenated timestamp, never underscores).
- Clickable link annotations pointing to shadow-library domains (Z-Library, OceanofPDF, Anna's Archive and the like) are removed.
- Watermark text baked into page content streams is erased.
- A whole page is deleted only when it is clearly a shadow-library advertisement and nothing else. Pages with real content, blank pages, image-only pages and internal PDF links are never touched.
- With no PDF tooling at all, cleanup is skipped, the owner is told, and the files are routed unmodified or left at the `Inbox/` root, at the owner's choice.

After cleanup, step 4 analyzes and routes the files.

### 4. Confirmation

Each eligible file is analyzed for both its destination and, where it helps, a cleaner file name. The proposed sort then goes to the owner for confirmation, **renaming and routing combined in one decision**, so both are confirmed in a single answer.

**Up to five files (inline):**

> _"[N] file(s) wait in the Inbox. Proposed routes:_
> _- `original-name.pdf` → rename to `Clean Name.pdf` → `Library/Life & Practice/Health & Wellness/`_
> _- `notes.md` → `Memory/Log.md` (append)_
>
> _Sort them now?"_

**More than five files (a table):**

| Original Name | Proposed New Name | Destination |
| ------------- | ----------------- | ----------- |
| ...           | ...               | ...         |

**Partial confirmation is supported.** The owner may approve some files and decline or redirect others, for example:

- "Sort all of them"
- "Skip [file name(s)]"
- "Send [file name] to [a different path] instead"
- "Sort everything except [file name(s)]"

No file moves without explicit approval for that file.

### 5. Pre-Sorting Enrichment

**No file moves from `Inbox/` to its destination in a raw, un-enriched state.** Each file gets its enrichment first.

**Order of operations:**

1. Apply the rename, if one was approved in step 4.
2. For a file bound for `Library/`, assess its freshness by the Library's tiers (`Library/README.md`, Rules). Ephemeral content (under five years) is redirected to `Projects/`, `Ventures/`, `Memory/` or a confirmed deletion: it is never filed in the Library.
3. Enrich it with frontmatter (text and Markdown); a binary carries none. A Library file leads its keywords with its freshness token (`freshness/timeless`, `freshness/enduring` or `freshness/current`).
4. Move it to its destination.

**File name hygiene (checked before enrichment).** A messy, hard-to-parse name, one using underscores as word separators, or one with garbled characters or excessive punctuation gets its rename proposed in the confirmation step (step 4). Underscores are never word separators: use spaces or hyphens. Examples: `my_report_v2_FINAL(1).pdf` → `My Report.pdf`, `export_2024_03_07.csv` → `Export 2024-03-07.csv`.

**Text and Markdown files:**

- Add the hidden frontmatter (`.docs/technical/vault/Note-Schema.md`) before moving.
- Fill in `title`, `description` and `type`, with `keywords` where they help.

**Binary and non-editable files (images, PDFs, audio, video, scripts and so on):** these cannot embed frontmatter, so they carry none (`.docs/technical/vault/Note-Schema.md`): the folder they are filed into places them, and that folder's README describes them. Each gets a clean, descriptive name before it moves, so its subject is plain from the name, with anything sensitive kept out of the name.

### 6. Ambiguous Files

When a file's contents do not clearly match one folder, it goes to the closest, most fitting existing folder by subject, and the reasoning is logged in `Memory/Log.md` so the owner can review the decision later. Routing notes never go in the file's own frontmatter.

**Log entry format:**

```markdown
### [Date] - Sort routing: [file name]

**Routed to:** [destination path]
**Why:** [brief explanation of the ambiguity and why this folder was chosen]
**Alternatives considered:** [folders that were close but not chosen]
```

These entries fall under the `Memory/Log.md` retention policy, in its "Inbox sort routing notes" row.

### 7. Duplicate File Names

When a file being sorted would collide with an existing file at its destination, the sort **stops and the owner chooses**:

- **Rename the incoming file** (a non-colliding name is proposed)
- **Overwrite the existing file** (destructive, so confirmed twice)
- **Skip this file** (it stays in `Inbox/` for later)
- **Keep both** (a suffix is added to one of them)

No option is picked silently.

### 8. Files That Don't Belong In The BRAIN

Some dropped files belong nowhere in the BRAIN: junk, accidental drops, screenshots from another context, temporary files. When analysis finds no reasonable destination, the owner is asked:

> _"`[file name]` does not fit anywhere in the BRAIN. Delete it, move it out of the Inbox to a location you name, or leave it at the `Inbox/` root to decide later?"_

No file is deleted from the Inbox without the owner's explicit confirmation (the root `README.md`, Ask First). Leaving it at the `Inbox/` root is the safe default when the owner does not answer.

### 9. New Subfolders

When no existing folder is a reasonable fit for a file, a new subfolder may be proposed:

> _"No folder fits [file name]. Create a new subfolder at [proposed path]?"_

**Strict constraint:** no new folder is ever created or proposed at Layer 0 (the root) or Layer 1. A Layer 2 folder needs the owner's explicit confirmation before it is created (the root `README.md`, Ask First). For the sort specifically, a proposed new folder sits at Layer 3 or deeper unless the owner explicitly directs a Layer 2 one.

### 10. System Assets (Utilities, Skills)

Some Inbox items are system assets rather than personal content. They go to the `System/` subfolders `System/README.md` describes:

- **A skill folder** (one holding a `SKILL.md` and its supporting files) is not vault content, and the vault has no place for it. It stays at the `Inbox/` root until the owner moves it out of the vault or confirms its deletion.
- **General prompt snippets, workflows or loose templates** go to `System/Utilities/`.

The standard protocol applies: the move is confirmed, the item leaves `Inbox/` completely so no duplicate is left behind, and naming hygiene holds: no underscores anywhere in a file or folder name (the root `README.md`, Conventions); use kebab-case, spaces or PascalCase. A utility `.md` file takes the standard frontmatter.

## File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                           | Purpose                                                                                                                                                                                                                                                                                                                                                         |
| :------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`Ideas/`](Ideas/README.md)     | The held idea pool: the living library of idea records that discovery work produces. Ideas persist here by lifecycle status (raw, shortlisted, developed, promoted, parked, killed), held and never sorted, so each new idea is checked against the whole pool, killed ideas included, and its lineage traced. The ideation counterpart to the Reports library. |
| [`Reports/`](Reports/README.md) | The held library for finished research and discovery reports: they are held, not sorted into the BRAIN, and every report is good for up to three months before it must be re-verified.                                                                                                                                                                          |
| [`Visuals/`](Visuals/README.md) | The held library for finished standalone visuals: charts, diagrams, dashboards and illustrations, held, not sorted into the BRAIN, and kept as archival artifacts that carry the date of their underlying data.                                                                                                                                                 |
| [`README.md`](README.md)        | This file.                                                                                                                                                                                                                                                                                                                                                      |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push.
