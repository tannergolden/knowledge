---
title: "System - Folder Information"
description: "Explains the purpose of the System/ folder: AI behavior configuration, persona settings, workflow loops, the skill library, and the generated catalogs. The vault's scripts live in .github/scripts/."
status: "active"
tags: ["system", "information", "timeless"]
aliases: []
keywords: ["ai configuration", "persona settings", "operating context", "control panel", "vault scripts", "behavior config", "folder overview"]
created: 2026-05-18
updated: 2026-10-19
type: "information"
folder: "system"
layer: 1
policy: false
author: "Tanner Golden"
path: "BRAIN/System/System.md"
id: "sy-system"
---

# System/

## Purpose

`System/` is the AI configuration layer of this BRAIN. It contains files that define how the AI should behave, what workflows it should follow, what persona it should adopt, and what operating context applies to this specific user's environment. Files here take precedence over general AI defaults where they overlap.

Think of this folder as the control panel - if `Instructions.md` is the operating manual and `Constitution.md` is the rulebook, `System/` is where the specific dials and settings live.

---

## Folder Structure

`System/` is a flat **operating surface** at the root (the docs you read), the `Skills/` library of installable capabilities, and the generated `Data/` folder. The vault's scripts are not here: they live in `.github/scripts/`, beside the CI that runs them, so `System/` holds only what the vault reads.

### Operating surface (`System/` root)

| Path | Purpose |
|------|---------|
| `System.md` | This file. |
| [[System/Workflows\|Workflows.md]] | Strategy and capture loops the AI follows. |
| `Persona.md` · `Context.md` · `Integrations.md` | Optional config files *(create as needed)*. |

### `Skills/` - installable capabilities

| Path | Purpose |
|------|---------|
| [[System/Skills/Skills\|Skills/Skills.md]] | Packaged `.skill` artifacts at the root; skill sources hidden in `.unpackaged/` (external format, no wikilinks, not walked as notes). A skill composes a team from the federated agent library and carries no agents of its own; its archive carries the team, vendored when it is built. |

### `Data/` - generated files

Machine-written and never hand-edited; `.github/scripts/update-vault.py` draws both, and CI fails when either is out of date. Group overview: [[System/Data/Data|Data/Data.md]].

| Path | Purpose |
|------|---------|
| `Data/catalog.ndjson` | One JSON record per note (`.template/` scaffolds excluded): path, title, type, folder, layer, tags, keywords, description, status and updated. The vault's live listing of what exists, readable by any AI or tool. |
| `Data/agent-catalog.json` | Every agent (spoken name, role, home, team, description) and every team roster in the federated agent library. The agents themselves are the source of truth; skills check a name against this before dispatching it. |

---

## Tooling

The vault's checks and generators are scripts in `.github/scripts/`, run from the vault root as `python3 .github/scripts/<script>`. Each one finds the vault from its own location (Constitution 2.5), needs only Python 3's standard library, and exits non-zero on a finding. `.github/workflows/vault.yml` runs every check, through the action in `.github/actions/vault/`, on each pull request and each push to the default branch.

| Script | What it does |
|--------|--------------|
| `check-vault.py` | Runs every check below, as CI does. The one command to run before a commit. |
| `lint-notes.py` | Every note's frontmatter, tags and naming against the schema (Instructions Section 8, Constitution Article VII). |
| `check-links.py` | The wikilink graph: every link resolves and follows the hub topology (Constitution 3.7). |
| `check-skills.py` | Each skill source against the Agent Skills format and the layout in `Skills/Skills.md`. |
| `check-agents.py` | Each agent spec and team roster, and one namespace across every home. |
| `scan-pii.py` | Social Security and card numbers in tracked files. Keys and tokens are the gitleaks scan's job in `checks.yml`. |
| `update-vault.py` | Draws everything generated: the memory cascade, every `brain:` block, both catalogs, the skill archives and the `.gitkeep` markers. `--check` writes nothing and fails when anything is stale. |
| `session-hooks.py` | The Claude Code hooks in `.claude/settings.json`: the session-start card, the check after every note written, and the end-of-turn redraw. |
| `profile-coverage.py` | How filled in each Profile facet is; the identify skill reads its `--json`. |
| `knowledge-base.py` | Offline reference works (Wikipedia and more) in `Library/Reference & Encyclopedia/`: `list`, `enable`, `refresh`, `search`, `read`. Every source ships off. |

Each script is tested by the `test_*.py` file beside it, and `.github/scripts/README.md` lists them all. The writes the retired engine once made for the AI, such as a memory entry, a session summary or a new note, the AI now makes with its own tools in the documented formats (Instructions Section 4.4).

---

## AI Instructions

- Read relevant `System/` files before beginning any session where behavior customization matters
- Files here override default AI behavior - if `System/Persona.md` says to avoid bullet points, avoid them even if it would otherwise be natural
- Do not modify `System/` files without explicit user direction - these represent deliberate configuration choices
- If no `System/` files exist yet, operate on defaults from `Instructions.md` and `Profile/Working Style.md`
- `System/Data/` files are generated artifacts - never read them for behavioral context; read `catalog.ndjson` when you need to know what notes exist without walking the tree

---

## AI Instructions - Writing Scripts

A new vault script goes in `.github/scripts/`, beside the others, and follows them:

- One job per script, named verb-noun with hyphens (`check-links.py`); its tests go in `test_<name>.py` beside it, which CI discovers on its own.
- Standard library only, and runnable on Python 3.9 (`from __future__ import annotations`), because the hooks run on whatever `python3` the machine has.
- The module docstring's first line is the script's purpose, since the folder's File Log reads it; the rest says why it exists and how to run it.
- Self-locating: import `vault.py` from the script's own folder, take the vault root from `--root` (the repository by default), and never hardcode a path (Constitution 2.5).
- Exit 0 when clean, 1 on findings, 2 on misuse, and print one finding per line; `vault.Report` does both, with GitHub annotations under Actions.
- Generated output is deterministic (sorted, no timestamps), so CI can tell a stale file from a fresh one.

---

## Priority Order

When `System/` files conflict with other parts of the BRAIN:
1. `Constitution.md` - always wins
2. `Instructions.md` - wins over System files on structural matters
3. `System/` files - win over Profile and general defaults on behavioral configuration
4. `Profile/Working Style.md` - applies when no System override exists

---

## What Belongs Here vs. Elsewhere

| Content Type | Belongs In |
|-------------|-----------|
| How this AI should communicate with this user | `System/Persona.md` *(create as needed)* |
| The user's natural communication preferences | `Profile/Working Style.md` |
| Governance rules for AI behavior | `Constitution.md` |
| Navigation and operational instructions | `Instructions.md` |
| Project-specific workflows | `Projects/[project]/` |
