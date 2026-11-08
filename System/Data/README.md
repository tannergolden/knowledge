<!--
title: '💾 DATA'
description: 'The generated catalog of every note, drawn by update-vault.py and committed: machine-written, never hand-edited. Read it to learn what the catalog holds and how it stays current, never for rules.'
type: 'index'
keywords: ["generated artifacts", "note catalog", "ndjson", "machine-written", "never hand-edit"]
-->

<div align="center">

# 💾 DATA

<a name="top"></a>

**The generated catalog of every note, drawn by a script and never edited by hand.**

_A map of the notes, never a source of rules._

</div>

---

## 💡 Purpose

`System/Data/` holds the vault's **generated catalog**: one file `.github/scripts/update-vault.py` draws from the notes and commits. Nothing here is human-authored; nothing here is ever edited by hand. This README is the folder's one human-readable file; the catalog is its other file, linked from here.

---

## 📦 Contents

| File | Drawn from | Holds |
|------|-----------|-------|
| [[catalog.ndjson]] | Every note's frontmatter | One JSON record per note, one per line for clean diffs, sorted by path: path (from `BRAIN/`, the vault root), title, type, keywords, description and status. `.template/` scaffolds are left out. The live listing of what exists, which the Projects and Ventures hubs and the Library point to, and which any tool can read instead of walking the tree. |

---

## 📜 Rules

- **Never edit by hand.** `update-vault.py` redraws the file from the notes; a hand edit is overwritten on its next run, and until then the catalog lies to everything that reads it (the root `README.md`, Conventions: accurate over complete).
- **It stays current by check, not by habit.** `update-vault.py` redraws it after a change, and CI runs `update-vault.py --check`, which fails when the catalog differs from the notes.
- **Never read it for rules.** It is for finding notes; the rules are in the root `README.md` and each folder's README (`System/README.md`, Rules).
- **It is deterministic.** No timestamps and a fixed order, so the catalog changes only when a note does.

---

<div align="center">

**Drawn, checked, never touched.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
