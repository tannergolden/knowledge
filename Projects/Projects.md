---
title: "Projects - Folder Information"
description: "Explains the purpose of the Projects/ folder: personal project tracking with AI-managed folder creation, standardized templates, and a master index."
status: "active"
tags: ["projects", "information", "timeless"]
aliases: []
keywords: ["personal initiatives", "side projects", "passion builds", "folder overview", "project templates", "creative work", "learning initiatives"]
created: 2026-05-18
updated: 2026-10-19
type: "information"
folder: "projects"
layer: 1
policy: false
author: "Tanner Golden"
path: "BRAIN/Projects/Projects.md"
id: "pr-projects"
---

# Projects/

## Purpose

`Projects/` tracks personal initiatives - things the user is building, creating, learning, or exploring independently. This is not for work tasks or organizational projects. It is for side projects, creative work, passion builds, learning initiatives, and anything else the user is personally driving.

---

## Structure

```
Projects/
├── Projects.md         ← this file (folder hub)
├── .template/           ← blueprint for new project folders
│   ├── Overview.md
│   ├── Log.md
│   ├── Notes.md
│   └── Resources.md
└── [Project-Name]/     ← one folder per project, AI-created
    ├── Overview.md     ← always at root
    ├── Log.md          ← always at root
    ├── Notes.md        ← always at root
    ├── Resources.md    ← always at root
    └── [Subfolder]/    ← AI-created for additional content as needed
```

---

## AI Instructions - Creating Project Folders

**The AI creates project folders. The user does not need to do this manually.**

When the user mentions working on, starting, or planning something that sounds like a personal project, the AI should ask:
> *"Want me to create a project folder for this?"*

If confirmed, the AI creates a new folder by copying the `.template/` structure and names it using short hyphenated format (e.g., `Personal-Site`, `Fishing-Journal`). The new folder is picked up automatically by the catalog (`System/Data/catalog.ndjson`, drawn by `update-vault.py`) - there is no hand-maintained index to update.

**Triggers for creating a project folder:**
- User explicitly starts a new personal project
- User repeatedly references something across sessions that doesn't have a folder yet
- A conversation reveals a sustained personal goal or build
- User asks to track or organize something new

---

## Template Files

Each project folder contains four standard files:

| File | Purpose | Retention |
|------|---------|-----------|
| `Projects/.template/Overview.md` | Goal, scope, status, key decisions - updated in place | Archive when project closes |
| `Projects/.template/Log.md` | Progress notes - chronological, staging-area model | Archive when project closes |
| `Projects/.template/Notes.md` | Freeform ideas, brainstorming, research - prune aggressively | Archive when project closes |
| `Projects/.template/Resources.md` | Tools, links, assets, people - keep current | Archive when project closes |

---

## AI Instructions - Subfolder Organization

**The four core files always stay at the root of the project folder - no exceptions.**

`Projects/.template/Overview.md`, `Projects/.template/Log.md`, `Projects/.template/Notes.md`, and `Projects/.template/Resources.md` are never moved into subfolders. They are always at `Projects/[Project-Name]/` regardless of how the project grows.

Subfolders are for additional content only - assets, code, drafts, research files, and other project materials that accumulate as the work progresses. The template is intentionally flat to start. But as a project grows, flat files are not always sufficient - and the AI is responsible for recognizing when they aren't and proposing the right structure.

**When to assess subfolder needs:**
- When creating a new project folder - if the project description makes it obvious the content will be varied (code + assets, writing + research, etc.), propose subfolders upfront
- When the user adds a new file to a project - assess whether it fits the existing structure or signals a need for a dedicated subfolder
- When a project folder accumulates more than 6–8 loose files - suggest consolidating into subfolders

**How to propose (always ask before creating):**
> *"This project looks like it'll have [code/assets/research/etc.]. Want me to add a [Code/Assets/Research/] subfolder to keep things organized?"*

**Never create subfolders silently.** Always propose first and wait for confirmation.

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

These are starting points - the actual subfolders should match what the project actually contains. Don't create a `Code/` folder for a project that has no code.

**Files placed inside a project folder should always be in the right place.** If the AI is saving or referencing a file for a project (a design mockup, a script, a draft document), it should check whether an appropriate subfolder exists and, if not, propose creating one rather than dropping everything at the root level.

---

## What Belongs Here vs. Elsewhere

| Content Type | Belongs In |
|-------------|-----------|
| A personal side project the user is building | `Projects/[Project-Name]/` |
| Work assigned by an employer or client | `Ventures/` |
| Reference material for a project topic | `Library/` |
| A pattern or trait observed about the user | `Profile/Personality.md` (propose via Constitution 4.2) |

---

## Listing projects

There is no hand-maintained index. Each project is a folder with an `Overview.md` whose frontmatter carries its status; the live list comes from the catalog: the `projects` records of the committed `System/Data/catalog.ndjson`. Keep each project's `Overview.md` status current as work progresses. If unsure whether something qualifies as a project, ask before creating anything.
