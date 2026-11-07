<!--
title: "Projects - Folder Information"
description: "Explains the purpose of the Projects/ folder: personal project tracking, one folder per project copied whole from a standard template, created only with a yes, with each project's status in its own Overview.md."
type: "index"
keywords: ["personal initiatives", "side projects", "passion builds", "folder overview", "project templates", "creative work", "learning initiatives"]
-->

# 🛠️ Projects/

What the user builds, makes, learns or explores on their own: side projects, creative work, learning goals. Each project is a folder copied from `.template/`, with an `Overview.md` for its goal and status, a `Log.md` of progress, `Notes.md` and `Resources.md`. Work for an employer, a client or one of the user's companies belongs in `Ventures/`. Read this README before changing anything in this folder; its rules add to the root `README.md` and never loosen it.

## Rules

- `Projects/` holds the user's personal initiatives only. Work for an employer, a client or one of their companies goes to `Ventures/`.
- A project folder is created only with a yes, by copying `Projects/.template/` whole and giving the folder a short hyphenated name (`Personal-Site`). When it is unclear whether something is a project, ask first.
- Every copied file gets its real `title`, `description` and `type`, and `[Project Name]` its real name: the copied `README.md` becomes the project folder's note, typed `index`, so the template's placeholders never reach the catalog.
- A project's four core files, `Overview.md`, `Log.md`, `Notes.md` and `Resources.md`, always stay at its root, beside its `README.md`.
- A subfolder is proposed first and created only with a yes, never silently.
- When work happens on a project, its `Overview.md` status is updated and its `Log.md` gains an entry.

## Purpose

`Projects/` tracks personal initiatives: things the user is building, creating, learning, or exploring independently. It is not for work tasks or organizational projects. It is for side projects, creative work, passion builds, learning initiatives, and anything else the user is personally driving.

---

## Structure

```bash
Projects/
├── README.md           ← this file (folder hub)
├── .template/          ← blueprint for new project folders, copied whole
│   ├── README.md       ← becomes the project folder's README.md
│   ├── Overview.md
│   ├── Log.md
│   ├── Notes.md
│   └── Resources.md
└── [Project-Name]/     ← one folder per project
    ├── README.md       ← the project folder's note
    ├── Overview.md     ← always at root
    ├── Log.md          ← always at root
    ├── Notes.md        ← always at root
    ├── Resources.md    ← always at root
    └── [Subfolder]/    ← added for more content as needed, with a yes
```

---

## Creating A Project Folder

A project folder is made when the user starts something that sounds like a personal project, and only once they say yes to the question:

> _"Create a project folder for this?"_

It is made by copying `.template/` whole and naming the copy in short hyphenated form (for example `Personal-Site` or `Fishing-Journal`). Each copied file then gets its real title, description and type, and the copied `README.md` becomes the project's folder note. The new folder is picked up automatically by the catalog (`System/Data/catalog.ndjson`, drawn by `update-vault.py`): there is no hand-maintained index to update.

**Signs a project folder is needed:**

- The user explicitly starts a new personal project
- The user keeps referring, across sessions, to something that has no folder yet
- A conversation reveals a sustained personal goal or build
- The user asks to track or organize something new

---

## Template Files

Each project folder holds five standard files:

| File | Purpose | Retention |
|------|---------|-----------|
| `Projects/.template/README.md` | The project folder's note: what the folder holds and where its files go | Kept while the folder exists |
| `Projects/.template/Overview.md` | Goal, scope, status, key decisions, updated in place | Archive when project closes |
| `Projects/.template/Log.md` | Progress notes: chronological, staging-area model | Archive when project closes |
| `Projects/.template/Notes.md` | Freeform ideas, brainstorming, research, pruned aggressively | Archive when project closes |
| `Projects/.template/Resources.md` | Tools, links, assets, people, kept current | Archive when project closes |

---

## Subfolders

**The core files always stay at the root of the project folder, without exception.**

`Overview.md`, `Log.md`, `Notes.md` and `Resources.md` are never moved into subfolders. They always sit in `Projects/[Project-Name]/`, beside its `README.md`, however the project grows.

Subfolders are for additional content only: assets, code, drafts, research files, and other project materials that accumulate as the work progresses. The template is flat to start, but flat files are not always enough as a project grows, so the structure is reassessed as it does, and a fitting subfolder is proposed when one is needed.

**When to assess subfolder needs:**

- When a project folder is created: if the description makes it obvious the content will be varied (code and assets, writing and research), subfolders are proposed up front
- When a new file is added to a project: it either fits the existing structure or signals a need for a dedicated subfolder
- When a project folder gathers more than six to eight loose files: consolidating them into subfolders is suggested

**How a subfolder is proposed (always before it is created):**

> _"This project will hold [code/assets/research]. Add a [Code/Assets/Research] subfolder to keep it organized?"_

**No subfolder is created silently.** It is always proposed first, and made only after a yes.

**Common subfolder patterns by project type:**

| Project type | Common subfolders |
|---|---|
| Software / coding | `Code/`, `Assets/`, `Docs/` |
| Creative writing | `Drafts/`, `Research/`, `Assets/` |
| Design | `Assets/`, `Mockups/`, `Exports/` |
| Learning / research | `Sources/`, `Summaries/`, `Exercises/` |
| Media (video, audio, photo) | `Media/`, `Scripts/`, `Exports/` |
| Business / planning | `Plans/`, `Research/`, `Assets/` |
| Game development | `Code/`, `Assets/`, `Docs/`, `Builds/` |

These are starting points: a project's subfolders match what it actually contains, so a project with no code gets no `Code/` folder.

**A file saved for a project goes in the right place.** A design mockup, a script or a draft goes into a fitting subfolder; when none exists, one is proposed rather than everything dropped at the root.

---

## What Belongs Here vs. Elsewhere

| Content Type | Belongs In |
|-------------|-----------|
| A personal side project the user is building | `Projects/[Project-Name]/` |
| Work assigned by an employer or client | `Ventures/` |
| Reference material for a project topic | `Library/` |
| A pattern or trait observed about the user | `Profile/Personality.md`, proposed first (`Profile/README.md`, Rules) |

---

## Projects

Each project folder's README, listed by `update-vault.py` from the folders here:

<!-- brain:children (drawn by .github/scripts/update-vault.py - do not edit by hand) -->
_No subfolders yet._
<!-- /brain:children -->

## Listing Projects

There is no hand-maintained index. Each project is a folder with an `Overview.md` whose Status section says where it stands; the live list comes from the catalog: the `BRAIN/Projects/` records of the committed `System/Data/catalog.ndjson`. Each project's `Overview.md` status is kept current as work progresses. When it is unclear whether something qualifies as a project, ask before creating anything.

## File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                               | Purpose                                                                                                                                                                        |
| :---------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`.template/`](.template/README.md) | The blueprint every project folder is copied from, whole: this README becomes the project folder's own, with [Project Name] replaced and its real title, description and type. |
| [`README.md`](README.md)            | This file.                                                                                                                                                                     |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push.
