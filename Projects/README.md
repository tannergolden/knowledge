<!--
title: '🛠️ PROJECTS'
description: 'Explains the purpose of the Projects/ folder: personal project tracking, one folder per project copied whole from a standard template, created only with a yes, with each project''s status in its own Overview.md. Read it before starting, filing or updating a personal project.'
type: 'index'
keywords: ["personal initiatives", "side projects", "passion builds", "folder overview", "project templates", "creative work", "learning initiatives"]
-->

<div align="center">

# 🛠️ PROJECTS

<a name="top"></a>

**Side projects, creative work and learning, each in a folder of its own.**

_Never an employer's work, and never a folder without a yes._

</div>

---

## ⚖️ What Belongs Here

`Projects/` tracks personal initiatives: what the owner builds, makes, learns or explores on their own, such as side projects, creative work, passion builds and learning initiatives. Each project is a folder copied from `.template/`, with an `Overview.md` for its goal and status, a `Log.md` of progress, `Notes.md` and `Resources.md`. It is not for work tasks or organizational projects: work for an employer, a client or one of the owner's companies belongs in `Ventures/`. Read this README before changing anything in this folder; its rules add to the root `README.md` and never loosen it.

Any skill's work in the owner's own life lands here once it is an initiative of its own, each project created only with a yes (Rules, below):

- a side project or a learning plan, from the `research-and-development` skill;
- a household plan, a trip or a move, from `operations-and-logistics`;
- a job search or a personal brand, from `sales-and-marketing`;
- a body of the owner's own writing, from `public-relations`;
- a habit or a metric the owner tracks, from `business-intelligence`.

A check of a project's work, such as the `quality-assurance` skill's, is logged in that project's `Log.md`.

| Content Type | Belongs In |
|-------------|-----------|
| A personal side project the owner is building | `Projects/[Project-Name]/` |
| Work assigned by an employer or client | `Ventures/` |
| An event or decision worth remembering | `Memory/` (`Memory/README.md`) |
| Reference material for a project topic | `Library/` |
| A pattern or trait observed about the owner | `Profile/Personality.md`, proposed first (`Profile/README.md`, Rules) |

---

## 📏 Rules

- `Projects/` holds the owner's personal initiatives only. Work for an employer, a client or one of their companies goes to `Ventures/`.
- A project folder is created only with a yes, by copying `Projects/.template/` whole and giving the folder a short hyphenated name (`Personal-Site`). When it is unclear whether something is a project, the owner is asked first.
- Every copied file gets its real `title`, `description` and `type`, its keywords lose `template`, and `[Project Name]` becomes the project's name: the copied `README.md` becomes the project folder's note, typed `index`, so the template's placeholders never reach the catalog.
- A project's four core files, `Overview.md`, `Log.md`, `Notes.md` and `Resources.md`, always stay at its root, beside its `README.md`.
- A subfolder is proposed first and created only with a yes, never silently.
- When work happens on a project, its `Overview.md` status is updated and its `Log.md` gains an entry.

---

## 🏗️ Structure

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

## 🌱 Creating A Project Folder

A project folder is made when the owner starts something that sounds like a personal project, and only once they say yes to the question:

> _"Create a project folder for this?"_

It is made by copying `.template/` whole and naming the copy in short hyphenated form (for example `Personal-Site` or `Fishing-Journal`), and each copied file is given its real frontmatter (Rules, above). `update-vault.py` lists the new folder under Projects, below, and the catalog (`System/Data/catalog.ndjson`) picks up its notes: there is no hand-maintained index to update.

**Signs a project folder is needed:**

- The owner explicitly starts a new personal project
- The owner keeps referring, across sessions, to something that has no folder yet
- A conversation reveals a sustained personal goal or build
- The owner asks to track or organize something new

---

## 📄 The Project Files

Each project folder holds the five files the template gives it:

| File | Holds | Kept |
|------|-------|------|
| `README.md` | The project folder's note: what the folder holds and where its files go | While the folder exists |
| `Overview.md` | Goal, scope, status, blockers and key decisions, updated in place | Current while the project runs; its status says when it closes |
| `Log.md` | Progress notes, newest first, with key decisions promoted to `Overview.md` | While the project runs, then kept with the folder |
| `Notes.md` | Freeform ideas, brainstorming and research, pruned once acted on | Pruned as it goes, then kept with the folder |
| `Resources.md` | Tools, links, books, assets and contacts, kept current | While the project runs, then kept with the folder |

When a project closes, its `Overview.md` says so and the folder is kept as the record: archiving or removing anything in it takes a yes (the root `README.md`, Ask First).

---

## 📁 Subfolders

**The core files always stay at the root of the project folder, without exception.** `Overview.md`, `Log.md`, `Notes.md` and `Resources.md` are never moved into subfolders: they always sit in `Projects/[Project-Name]/`, beside its `README.md`, however the project grows.

Subfolders are for additional content only: assets, code, drafts, research files, and other project materials that accumulate as the work progresses. The template is flat to start, but flat files are not always enough as a project grows, so the structure is reassessed as it does, and a fitting subfolder is proposed when one is needed:

- **When a project folder is created:** if its description makes it obvious the content will be varied (code and assets, writing and research), subfolders are proposed up front.
- **When a new file is added to a project:** it either fits the existing structure or signals a need for a dedicated subfolder.
- **When a project folder gathers more than six to eight loose files:** consolidating them into subfolders is suggested.

A subfolder is always proposed before it is created, and made only after a yes:

> _"This project will hold [code/assets/research]. Add a [Code/Assets/Research] subfolder to keep it organized?"_

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

These are starting points: a project's subfolders match what it actually contains, so a project with no code gets no `Code/` folder. A file saved for a project goes in the right place: a design mockup, a script or a draft goes into a fitting subfolder, and when none exists, one is proposed rather than everything dropped at the root.

---

## 🗂️ Projects

Each project folder's README, listed by `update-vault.py` from the folders here; the catalog's `BRAIN/Projects/` records list every note inside them, and each project's `Overview.md` says where it stands.

<!-- brain:children (drawn by .github/scripts/update-vault.py - do not edit by hand) -->
_No subfolders yet._
<!-- /brain:children -->

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                               | Purpose                                                                                                                                                                                                                                                                     |
| :---------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`.template/`](.template/README.md) | The blueprint every project folder is copied from, whole: this README becomes the project folder's own, with [Project Name] replaced and its real title, description and type. Read it before starting a project, to see what each project folder holds and how it is kept. |
| [`README.md`](README.md)            | This file.                                                                                                                                                                                                                                                                  |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push to the default branch.

---

<div align="center">

**Start on a yes, log each step, keep the core files at the root.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
