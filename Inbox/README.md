<!--
title: '📥 INBOX'
description: 'The staging area: drop any unsorted file here, and it is enriched and filed where it belongs, each move proposed and confirmed first, while the held sub-homes (Research, Visuals, Ideas and Backups) live here but are never sorted. Read it before sorting the Inbox or changing anything in it.'
type: 'index'
keywords: ["staging area", "drop files", "unsorted", "sorting protocol", "pdf cleanup", "file triage", "where to put files", "hold folder"]
-->

<div align="center">

# 📥 INBOX

<a name="top"></a>

**The staging area where every unsorted file waits to be enriched and filed.**

_Proposed first, enriched always, moved only on a yes._

</div>

---

## 💡 What `Inbox/` Is (a meta-zone, not just an inbox)

Anything waiting to be filed lands here: a document, a PDF, a photo, an export, a note written in a hurry. Each loose file is given a home and a clean name, enriched, and moved only once the owner confirms the move. Read this README before changing anything in this folder; its rules add to the root `README.md` and never loosen it.

`Inbox/` is a small **meta-zone**, not a single pure inbox. It holds things kept deliberately distinct, the pattern Johnny.Decimal uses for its `00-09` area, where an inbox and an archive coexist as siblings:

1. **The inbox proper**: loose files dropped at the `Inbox/` root, and the sorting protocol below. This is the only transient part: it is processed to empty.
2. **[[Inbox/Research/README|Research]]**: the held library of finished research and discovery reports about anything but this vault itself. Each report is good for up to three months, then verified before it is used again, and that README is the one index that links every report. Research behind a change to the vault itself is a Research Log in `.docs/technical/research/` instead.
3. **[[Inbox/Visuals/README|Visuals]]**: the held library of finished standalone visuals (charts, diagrams, dashboards, interactive widgets and explanatory illustration). Each is an archival snapshot that carries the date of its underlying data and is kept until superseded, and that README is the one index that links every visual. Most visuals are shown once and never saved; only one the owner asks to keep is filed there or in a named home.
4. **[[Inbox/Ideas/README|Ideas]]**: the held idea pool, one idea record to a file. Ideas are held by lifecycle status (raw, shortlisted, developed, promoted, parked, killed), with killed and parked ideas kept so a dead end is never re-trodden; a record links to nothing, and the pool is found by search and by status, not by an index of links.
5. **`Backups/`**: the originals of outside PDFs, copied into a timestamped subfolder before a cleanup changes them (step 2 below). It appears once the first cleanup runs.

The three libraries stay inside the vault's checks like any other content: their notes are linted and cataloged, and a saved visual, which is not a note, is found through its index. `Backups/` holds raw copies, which the checks and the catalog never walk. All four are **held lists that live at the inbox path, not contents of the inbox.** "Process the inbox to empty", and any "is the inbox empty?" check, apply only to the loose files at the root; they never count a held sub-home. This is a deliberate, documented exception to the inbox-is-transient rule.

---

## 📜 Rules

- **The Inbox is checked at the start of every session**, even when nothing is likely to wait there, and what waits is sorted before other work.
- **Nothing leaves unenriched.** A note gets its frontmatter, and any file a clean name, before it moves. No exceptions.
- **Nothing moves without a yes.** Each file's destination and clean name are proposed first, and the owner confirms them.
- **No file here is deleted without confirmation.** Leaving a file at the `Inbox/` root is the safe default.
- **The held sub-homes are never sorted**: `Research/`, `Visuals/`, `Ideas/` and `Backups/`.
- **A new folder only to fit a file.** During a sort, when no folder fits, a new folder three or more levels down may be proposed; one directly inside a top folder needs the owner's explicit direction, and a top folder is never created.
- **Outside PDFs are offered cleanup first**, and their originals are copied into `Inbox/Backups/` before anything changes.
- The sort follows the protocol below, step by step.

---

## ⚖️ What Belongs In The Inbox

The Inbox is for things that already have a place in the BRAIN but need to be filed:

- Documents, notes and articles to keep as reference
- Personal media, photos, audio and video that fit an existing folder
- Project files, drafts and exports
- Anything that would otherwise have to be categorized by hand

---

## 🚫 What Doesn't Belong

Some files are better deleted or kept somewhere else entirely:

- Random downloads, accidentally dropped files, temporary work files
- Executables, archives or installers, which are not reference material
- Anything a portable knowledge layer should not carry around forever

When one of these is dropped and no good home exists, the owner is asked whether to delete it or move it to a location of their choice (step 7). System junk (`.DS_Store`, `.cache` and the like) is ignored by the sort, and `.DS_Store` is never deleted, moved or counted (the root `README.md`, Gotchas).

---

## 🗃️ The Sorting Protocol (Canonical)

This is the complete sorting protocol; the Rules above are its always-on essentials. In short: at the next session start, each loose file is detected; a PDF from outside is offered cleanup; each file is analyzed for where it belongs in the BRAIN; its destination and, where needed, a clean name are proposed together and confirmed; and only then is it enriched and moved. **Nothing is moved without the owner's approval.**

### 1. Detection

At the start of every session, `Inbox/` is checked for sortable files: `python3 .github/scripts/session.py start` lists each loose file on an `INBOX` line. If any wait, they are analyzed before anything else.

**What counts as a sortable file.** Only the loose files at the `Inbox/` root, and in folders dropped there, are sortable. Never sortable:

- This README (a permanent fixture, never sorted)
- Hidden files and folders (any name starting with `.`, including `.DS_Store`, `.gitkeep` and `.localized`)
- The held sub-homes, `Research/`, `Visuals/`, `Ideas/` and `Backups/`, and everything inside them: their contents are never scanned, surfaced or proposed for routing at session start

A file modified within the last 30 seconds may still be syncing or copying, so it is checked again after a short wait before it is sorted. If no sortable file remains, the Inbox counts as empty and the session goes on.

### 2. PDF Pre-Processing

PDFs from outside sources often carry piracy watermarks, shadow-library branding (Z-Library, OceanofPDF, Anna's Archive) and malicious link annotations. These are cleaned before the file enters the BRAIN.

**Before cleanup, the owner is asked:**

> _"[N] PDF(s) wait in the Inbox. Run cleanup (recommended for outside downloads), or skip it (for a trusted source such as a publisher, a personal scan or an official download)?"_

If the owner confirms cleanup, or does not answer clearly, cleanup runs. If the owner trusts the source, confirmation (step 3) follows directly.

**Cleanup** is done with whatever PDF tooling is at hand (for example PyMuPDF in a short Python script, or the platform's own PDF tools). There is no bundled cleanup script. Any cleanup honors this contract:

- **Back up first, always.** Before anything is modified, the original PDFs are copied into a timestamped subfolder under `Inbox/Backups/` (a hyphenated timestamp, never underscores).
- Clickable link annotations pointing to shadow-library domains (Z-Library, OceanofPDF, Anna's Archive and the like) are removed.
- Watermark text baked into page content streams is erased.
- A whole page is deleted only when it is clearly a shadow-library advertisement and nothing else. Pages with real content, blank pages, image-only pages and internal PDF links are never touched.
- With no PDF tooling at all, cleanup is skipped, the owner is told, and the files are routed unmodified or left at the `Inbox/` root, at the owner's choice.

After cleanup, step 3 analyzes and routes the files.

### 3. Confirmation

Each sortable file is analyzed for both its destination and, where it helps, a cleaner file name. The proposed sort then goes to the owner for confirmation, **renaming and routing combined in one decision**, so both are confirmed in a single answer. Dozens or hundreds of files can be dropped at once, so the proposal's form follows the count.

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

### 4. Pre-Sorting Enrichment

**No file moves from `Inbox/` to its destination in a raw, un-enriched state.** Each file gets its enrichment first.

**Order of operations:**

1. Apply the rename, if one was approved in step 3.
2. For a file bound for `Library/`, assess its freshness by the Library's tiers (`Library/README.md`, Rules). Ephemeral content (under five years) is redirected to `Projects/`, `Ventures/`, `Memory/` or a confirmed deletion: it is never filed in the Library.
3. Enrich it with frontmatter (text and Markdown); a binary carries none. A Library file leads its keywords with its freshness token (`freshness/timeless`, `freshness/enduring` or `freshness/current`).
4. Move it to its destination.

**File name hygiene (checked before enrichment).** A messy, hard-to-parse name, one using underscores as word separators, or one with garbled characters or excessive punctuation gets its rename proposed in the confirmation step (step 3). Underscores are never word separators: names use spaces or hyphens (the root `README.md`, Conventions). Examples: `my_report_v2_FINAL(1).pdf` → `My Report.pdf`, `export_2024_03_07.csv` → `Export 2024-03-07.csv`.

**Text and Markdown files:**

- Add the hidden frontmatter (`.docs/technical/vault/Note-Schema.md`) before moving.
- Fill in `title`, `description` and `type`, with `keywords` where they help.

**Binary and non-editable files (images, PDFs, audio, video, scripts and so on):** these cannot embed frontmatter, so they carry none (`.docs/technical/vault/Note-Schema.md`): the folder they are filed into places them, and that folder's README describes them. A binary source bound for `Library/`, such as a book or paper as a PDF, also gets the companion catalog card `Library/README.md` requires, made from `Library/.template/Source Catalog Card.md` and filed beside it. Each gets a clean, descriptive name before it moves, so its subject is plain from the name, with anything sensitive kept out of the name.

### 5. Ambiguous Files

When a file's contents do not clearly match one folder, it goes to the closest, most fitting existing folder by subject, and the reasoning is recorded so the owner can review the decision later: a row in the Sort Routing Notes table of `Memory/Log.md`, with the date, the file, its destination and the rationale, which names the folders that were close but not chosen. Routing notes never go in the file's own frontmatter, and they fall under the Log's retention: staging only (`Memory/Log.md`).

### 6. Duplicate File Names

When a file being sorted would collide with an existing file at its destination, the sort **stops and the owner chooses**:

- **Rename the incoming file** (a non-colliding name is proposed)
- **Overwrite the existing file** (destructive, so confirmed twice)
- **Skip this file** (it stays in `Inbox/` for later)
- **Keep both** (a suffix is added to one of them)

No option is picked silently.

### 7. Files That Don't Belong In The BRAIN

Some dropped files belong nowhere in the BRAIN: junk, accidental drops, screenshots from another context, temporary files. When analysis finds no reasonable destination, the owner is asked:

> _"`[file name]` does not fit anywhere in the BRAIN. Delete it, move it out of the Inbox to a location you name, or leave it at the `Inbox/` root to decide later?"_

No file is deleted from the Inbox without the owner's explicit confirmation (the root `README.md`, Ask First). Leaving it at the `Inbox/` root is the safe default when the owner does not answer.

### 8. New Subfolders

When no existing folder is a reasonable fit for a file, a new subfolder may be proposed:

> _"No folder fits [file name]. Create a new subfolder at [proposed path]?"_

**Strict constraint:** a sort never creates or proposes a top folder, and never a folder directly inside a top folder unless the owner explicitly directs it (the root `README.md`, Ask First). A folder a sort proposes sits three or more levels down, such as `Library/<Class>/<New Folder>/`, and is created only with a yes.

### 9. System Assets (Skills, Prompts, Settings)

Some Inbox items are not personal content but material for working in the vault:

- **A skill folder** (one holding a `SKILL.md` and its supporting files) is not vault content, and the vault has no place for it. It stays at the `Inbox/` root until the owner moves it out of the vault or confirms its deletion.
- **A prompt for working in this vault** goes to `.docs/Prompts.md`, under This Repository's Prompts, the section only the owner writes.
- **A standing setting** for how work here is done goes to a `System/` settings file, and a recurring workflow is mapped in `System/Workflows.md` (`System/README.md`).
- **A scaffold** for a folder's new notes goes to that folder's `.template/`, proposed first like any new file.

The standard protocol applies: the move is confirmed, the item leaves `Inbox/` completely so no duplicate is left behind, its name has no underscores (the root `README.md`, Conventions), and a `.md` file takes the standard frontmatter.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                             | Purpose                                                                                                                                                                                                                                                                                                                                                        |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`Ideas/`](Ideas/README.md)       | The held idea pool: the living library of idea records that discovery work produces, kept by lifecycle status (raw, shortlisted, developed, promoted, parked, killed) and never sorted, the ideation counterpart to the Research library. Read it to file an idea, or to check a new one against the whole pool, killed ideas included, and trace its lineage. |
| [`Research/`](Research/README.md) | The held library for finished research about anything but this vault itself: the world, the owner's life, a venture or a project. Reports are held, not sorted into the BRAIN, and each is good for up to three months before it must be re-verified. Read it to file, refresh or find a report.                                                               |
| [`Visuals/`](Visuals/README.md)   | The held library for finished standalone visuals: charts, diagrams, dashboards and illustrations, held, not sorted into the BRAIN, and kept as archival artifacts that carry the date of their underlying data. Read it to file, regenerate or find a visual.                                                                                                  |
| [`README.md`](README.md)          | This file.                                                                                                                                                                                                                                                                                                                                                     |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push to the default branch.

---

<div align="center">

**Sorted to empty, one confirmed move at a time.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
