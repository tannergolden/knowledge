<!--
title: '🛠️ [PROJECT NAME]'
description: 'The blueprint every project folder is copied from, whole: this README becomes the project folder''s own, with [Project Name] replaced and its real title, description and type. Read it before starting a project, to see what each project folder holds and how it is kept.'
type: 'template'
keywords: ["[other name for the project]", "[what it is about]", "template"]
-->

<!-- On copying: this README comes with the project's folder, Projects/<Project-Name>/, made by copying Projects/.template/ whole, only with the owner's yes (Projects/README.md, Rules). Then:
- Set type to "index". Replace [PROJECT NAME] in the title and the H1 alike with the folder's name in capitals, and [Project Name] everywhere else with the project's name. Give the copy its real description, of what the project is and when to read this README, and keywords a search would use: lowercase, at most eight, each distinct, none already in the title, with "template" dropped.
- Each file copied with it has a note of its own at its top: Overview.md and Resources.md become reference, and Log.md and Notes.md become record.
- Write only what the owner says or confirms; nothing is guessed.
- Once filed, lint-notes.py checks each copied file, and update-vault.py lists the project in Projects/README.md.
- Delete this note from the copy.
-->

<div align="center">

# 🛠️ [PROJECT NAME]

<a name="top"></a>

**[Project Name]'s home: its four core files and everything the project gathers.**

_[Project Name]'s status in its Overview, its progress in its Log._

</div>

---

## 📂 What Goes Here

The folder of [Project Name], a personal project. Read this README before changing anything in this folder; its rules add to `Projects/README.md` and the root `README.md`, and never loosen them.

| File | Holds |
| ---- | ----- |
| `Overview.md` | The goal, scope, current status, blockers and key decisions, updated in place: read it first |
| `Log.md` | Progress notes, newest first; key decisions are promoted to `Overview.md` |
| `Notes.md` | Freeform ideas, brainstorming and research findings, pruned once acted on |
| `Resources.md` | The tools, links, books, assets and contacts the project uses, kept current |

These four always stay at the root of this folder, beside this README. Everything else the project gathers, such as code, assets, drafts or research, goes in a subfolder named for what it holds (`Code/`, `Assets/`, `Drafts/`), proposed first and created only with a yes (`Projects/README.md`, Subfolders).

---

## 📏 Rules

- Only what the owner says or confirms is written here; nothing is guessed or invented.
- When work happens on the project, `Overview.md` takes its current status and `Log.md` gains an entry.
- A fact about the owner goes to `Profile/`, an event or decision worth remembering to `Memory/`, and reference knowledge to `Library/`, never here.
- When the project closes, `Overview.md` says so. The folder is kept, and archiving or removing anything in it takes a yes.

---

<div align="center">

**[Project Name], one log entry at a time.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
