---
title: "Skills - Folder Information"
description: "The System/Skills/ folder: hidden .unpackaged/ skill sources that compose teams from the federated agent library, packaged into .skill artifacts at the root. Skills carry no agents and no scripts of their own."
status: "active"
tags: ["system", "information", "timeless"]
aliases: []
keywords: ["skills folder", "unpackaged sources", "skill packaging", "compose teams", "metadata.team", "skill artifacts", "no scripts"]
created: 2026-06-08
updated: 2026-07-04
type: "information"
folder: "system"
layer: 2
policy: false
version: "01.01.03"
author: "Tanner Golden"
path: "BRAIN/System/Skills/Skills.md"
id: "sy-skills"
---

# 🛠️ Skills - the consumers

Each skill is a folder with a `SKILL.md` entrypoint. A skill does not own agents; it composes a team from the federated agent library, naming the team in `metadata.team`. Authored and packaged by `develop`.

## Sources live in `.unpackaged/`

Skill SOURCES live in `Skills/.unpackaged/<skill>/`, a hidden folder, so the everyday tree is not cluttered by working files. Packaging a skill produces a self-contained `<skill>.skill` artifact at the `Skills/` root. The source is what `develop` edits; the artifact is what installs and ships. Each packaged skill is the graph node linked here as a sibling file: currently [[develop.skill]], [[research.skill]], [[editorial.skill]], [[visualize.skill]], [[discover.skill]], [[identify.skill]], and [[board.skill]].

## Per-skill folder (the mandatory structure)

Every skill source carries exactly these files and folders:

```
.unpackaged/<skill-name>/
  SKILL.md          entrypoint: frontmatter + workflow; metadata.team names the roster
  License.txt       the license text
  Changelog.md      version history (BRAIN changelog format, ships at 01.00.00)
  <Skill-Name>.md   the namesake doc
  assets/           static files the skill ships
  references/       domain knowledge loaded on demand
  templates/        output scaffolds the skill fills in
```

No `agents/` folder in source. Agents are referenced from the federated agent library by name; only at export does `develop` vendor the referenced agents into a packaged copy's `agents/`.

No `scripts/` folder either. Every deterministic helper a skill needs (validation, packaging, catalog generation) lives in `brain.command` and is shared across all skills, invoked as a subcommand such as `brain.command skill validate`. Centralizing scripts there keeps one implementation and, because the engine already tracks the live BRAIN, makes the checks dynamic: a rule change in the BRAIN is picked up without editing any skill.

## How a skill names its team

- `SKILL.md` frontmatter carries `metadata.team: <team-name>`, a string naming a team in the federated agent library (a team in one of the agent homes: `Ventures/Agent Resources (AR)/`, `Inbox/Faculties/Research/`, `Inbox/Faculties/Discovery/`, or `Inbox/Faculties/Development/`). This is a portable annotation: the SKILL.md schema is closed, and `metadata` is the only spec-legal home for it. `brain.command skill validate` rejects a `metadata.team` that does not resolve to a staffed roster.
- The SKILL.md BODY carries the dispatch-scaling rule: which members of the team run at which task complexity. The body is the real behavior; the annotation is documentation.
- Agents are selected and invoked by their `description`. Where supported, a skill composes an agent at runtime via `context: fork` plus `agent: <name>`.

## Reference locally, vendor on export

Locally a skill references its team's agents by name and nothing is copied. When packaging a skill to distribute, `develop` vendors the referenced agents into the skill's `agents/` so the shipped `.skill` is self-contained. Vendoring is a packaging step, not the everyday state.

## How develop works here

`develop` authors each agent into its home team folder in the federated library (a domain home such as `Inbox/Faculties/Development/` or a `Ventures/Agent Resources (AR)/` department), writes or updates that team's namesake roster, and writes skills into this folder from the develop skill's `templates/`. It places each agent in its home professional team, marks the team lead with a star, and runs vendor-on-export only when packaging for distribution.
