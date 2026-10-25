<!--
title: "Data - Folder Information"
description: "Explains the System/Data/ folder: the two generated catalogs, one of every note and one of every agent, drawn by update-vault.py and committed. Machine-written; never hand-edit."
type: "index"
keywords: ["generated artifacts", "note catalog", "agent catalog", "ndjson", "machine-written", "never hand-edit"]
-->

# 💾 System/Data/

## Purpose

`System/Data/` holds the vault's **generated catalogs**: two files `.github/scripts/update-vault.py` draws from the notes and commits. Nothing here is human-authored; nothing here is ever edited by hand. This doc is the folder's one human-readable file; the catalogs are its other two files, linked from here.

---

## Contents

| File | Drawn from | Holds |
|------|-----------|-------|
| [[catalog.ndjson]] | Every note's frontmatter | One JSON record per note, one per line for clean diffs, sorted by path: path, title, type, keywords, description and status. `.template/` scaffolds are left out. The live listing of what exists: the Projects and Ventures hubs, the Library's finding aids and any AI or tool read it instead of walking the tree. |
| [[agent-catalog.json]] | The agent homes (`Ventures/Agent Resources (AR)/`, `Inbox/Faculties/`, `Library/`) | Every agent (spoken name, role, home, team, description, path) and every team roster (team, home, lead, members, description, path), with counts. Skills check a specialist's name against it before dispatching it, so a renamed or retired agent fails loudly. |

---

## Rules

- **Never edit by hand.** `update-vault.py` redraws both files from the notes; a hand edit is overwritten on its next run, and until then the catalog lies to everything that reads it (`AGENTS.md`, Conventions: accurate over complete).
- **They stay current by check, not by habit.** `update-vault.py` redraws them after a change, and CI runs `update-vault.py --check`, which fails when either catalog differs from the notes.
- **Never read these for behavioral context.** They are for finding notes and agents, not for rules (`System/System.md`, AI Instructions).
- **They are deterministic.** No timestamps and a fixed order, so a catalog changes only when a note or an agent does.
