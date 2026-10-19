---
title: "Faculties"
description: "The BRAIN's standing functional teams: the four cognitive teams the Founder dispatches directly (Research, Discovery, Editorial, Design), grouped as one home. The personal-work counterpart to the venture corporate workforce in Agent Resources (AR)."
status: "active"
tags: ["inbox", "information", "timeless"]
aliases: ["the Faculties", "standing teams", "cognitive teams", "the agent teams"]
keywords: ["standing teams", "functional teams", "research team", "discovery team", "editorial team", "design team", "agent teams", "cognitive faculties"]
created: 2026-06-23
updated: 2026-10-19
type: "information"
folder: "inbox"
layer: 2
policy: false
author: "Tanner Golden"
path: "BRAIN/Inbox/Faculties/Faculties.md"
id: "in-faculties"
---

# 👥 Faculties

The BRAIN's **Faculties** are its standing functional teams: the four cognitive teams the Founder dispatches directly to do the BRAIN's own thinking work. A faculty is both a body of experts and a mental capacity, which is exactly what each of these is, a standing group of specialist agents for one mode of work. They are the personal-work counterpart to Agent Resources (AR), the corporate workforce that serves the ventures: AR runs the companies, the Faculties serve the Founder's own research, ideation, writing, and visualization.

## The four teams

Each team is a standing roster of single-file agents with one star lead, dispatched to the smallest sufficient size for the job, and each holds one overriding standard. The lead orchestrates (frames the brief, dispatches the specialists, synthesizes their returns, and ships) and never does the hands-on labor itself; the making is the specialists' work. A solo home like the Library, one agent and no specialists, is the exception: it does the work itself.

- [[Inbox/Faculties/Research/Research|Research.md]] - gathers, verifies, and synthesizes evidence, to a **zero-bias** standard. Dispatched by the `research` skill.
- [[Inbox/Faculties/Discovery/Discovery|Discovery.md]] - generates ideas wide then converges to the strongest by tournament, to a **generate-wide, select-fair** standard. Dispatched by the `discover` skill.
- [[Inbox/Faculties/Editorial/Editorial|Editorial.md]] - drafts all of the Founder's prose, to a **clarity** standard with voice fidelity as its craft rule. Dispatched by the `editorial` skill.
- [[Inbox/Faculties/Design/Design|Design.md]] - turns data, structure, and ideas into honest visuals, to a **graphical-integrity** standard with legibility and accessibility as its craft rule. Dispatched by the `visualize` skill.

Building is no longer a faculty of this vault. The Development team, which designs, builds, and independently verifies whatever the Founder needs built, now ships inside `develop`, the one universal skill, which comes from tannergolden/intelligence with its home kit. So the team works here and in any other repository alike: dispatch it through `develop`, which follows this vault's rules when it works here.

## How it is organized

- **One folder per team.** Each team is a flat home: a folder of single-file agent specs plus a namesake roster that carries `members` and the star `lead`. The four together make `Inbox/Faculties/` a multi-team home, the same shape Agent Resources (AR) uses for its departments.
- **Each team owns its own standard and global rules.** Unlike AR, the Faculties share no workforce-wide rulebook: each is a distinct discipline with its own overriding standard, so the standard and the global rules live in each team's own roster, not here. This doc is the grouping and the map, not a rulebook.
- **Skills dispatch the teams.** A skill is the trigger that calls a faculty: `research` dispatches Research, `editorial` dispatches Editorial, `visualize` dispatches Design, and `discover` dispatches Discovery. All four faculties have a dispatching skill.
- **Sanctioned exception.** Only one agent in this vault holds labor tools: the Library's solo ★ Librarian (Write, Edit, Bash, Task), scope-bounded to `Library/` holdings as the documented solo steward. Every other agent composes and returns; the dispatching skill persists. The Development team's Full-Stack Engineer also holds them (Write, Edit, Bash), because the build seat cannot produce working code otherwise, and it moved with its team into `develop`.

## Federation: one logical library, two corners

The Faculties and Agent Resources (AR) are **one logical agent library** with one global namespace: no two agents anywhere share a spoken name or a role, and one catalog (`System/Data/agent-catalog.json`) indexes the whole library. The split is by who they serve: the Faculties (`Inbox/Faculties/`) serve the Founder's own work; AR (`Ventures/Agent Resources (AR)/`) serves the ventures. A skill or venture references any agent by name regardless of which corner holds it.

## Held, not sorted

`Inbox/Faculties/` is a permanent held sub-home of the Inbox, like `Inbox/Reports/`: fully linted, synced, and indexed, but never scanned or sorted by the session-start Inbox sweep. Only loose files at the `Inbox/` root are sorted. The teams' finished work, a report, a build, a piece of writing, is delivered to its real home elsewhere in the BRAIN, never kept here.
