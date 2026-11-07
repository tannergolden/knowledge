<!--
title: '⚙️ SYSTEM'
description: 'How the AI works in the vault: its workflows and the catalog it generates.'
type: index
keywords: [configuration, vault]
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# ⚙️ SYSTEM

<a name="top"></a>

**How the AI works here: workflows and the generated catalog.**

_The dials and settings behind every session._

</div>

---

## 💡 What This Folder Is For

`System/` is the vault's control panel. `Workflows.md` holds the loops the AI follows, and `Data/`
holds the catalog `update-vault.py` generates. The vault's checks and generators live in
`.github/scripts/`, beside the CI that runs them. The skills the AI uses (board, discover, editorial,
finance, identify, research and visualize) are not kept here: the home kit installs them from
tannergolden/intelligence.

---

## 🚀 How To Use It

- **Add a setting** as a note here, such as `Persona.md`, and the AI follows it over its own
  defaults.
- **Use a skill** by asking for what it does; the AI fires the matching one from the home kit.
- **Never edit `Data/` by hand.** It is redrawn from the notes.

The AI reads this folder's note, [`System.md`](System.md), before it works here: its
rules come first, then how the folder works.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                          | Purpose                                                                                                                                                                                                                  |
| :----------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`Data/`](Data/)               | Explains the System/Data/ folder: the generated catalog of every note, drawn by update-vault.py and committed. Machine-written; never hand-edit.                                                                         |
| [`README.md`](README.md)       | This file.                                                                                                                                                                                                               |
| [`System.md`](System.md)       | Explains the purpose of the System/ folder: AI behavior configuration, persona settings, workflow loops, and the generated catalog. The vault's scripts live in .github/scripts/, and its skills come from the home kit. |
| [`Workflows.md`](Workflows.md) | Formalized workflows for the AI to follow, defining strategy loops, automated captures, and recurring behaviors.                                                                                                         |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push.

---

<div align="center">

**Settings here, rules in AGENTS.md, notes everywhere else.**

[↑ Back to Top](#top)

</div>
