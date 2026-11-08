<!--
title: '🛠️ TECHNICAL'
description: 'How the vault is built: how its scripts fit together, the reference pages behind its rules, and the designs, plans and research behind a change to the vault itself. Read it before you change a script, a rule or the layout.'
type: index
-->

<div align="center">

# 🛠️ TECHNICAL

<a name="top"></a>

**How the vault is built, and the thinking behind each change to it.**

_Written down where the scripts cannot say it._

</div>

---

## 💡 What This Folder Is For

How the vault is built, written down where its scripts and its folders cannot
say it themselves.

- **The machinery**: how the scripts in `.github/scripts/` fit together, what
  each check fails on, and what to do when one fails, in
  [Vault Scripts](Vault-Scripts.md).
- **The reference pages behind the rules**: the note schema, the keywords, the
  link topology, how context is assembled and how a session runs, in
  [`vault/`](vault/README.md).
- **Designs, plans and research** behind a change to the vault itself, such as
  a new folder, rule or script: one document each in `designs/`, `plans/` and
  `research/`, copied from the [Technical Design](../templates/Technical-Design.md),
  [Implementation Plan](../templates/Implementation-Plan.md) and
  [Research Log](../templates/Research-Log.md) templates. Each of those folders
  is made, with its own `README.md`, when its first document arrives. Research
  for the owner's own life or a venture is a held report in `Inbox/Reports/`,
  never a page here.

Vault Scripts and the pages in `vault/`, like this README, are the template's,
and 🔄 Template Sync keeps them current in a vault. A document you add here is
**yours from the first commit**: nothing upstream ever writes, moves or removes
it. The log below is redrawn from the files the folder holds.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                  | Purpose                                                                                                                                                                                                                                                                                                      |
| :------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`vault/`](vault/README.md)            | The reference pages behind the vault's rules: its note schema, keywords and link topology, how context is assembled, and how a session runs and its summaries age.                                                                                                                                           |
| [`README.md`](README.md)               | This file.                                                                                                                                                                                                                                                                                                   |
| [`Vault-Scripts.md`](Vault-Scripts.md) | How the scripts in .github/scripts/ fit together: the library they share, the contract each one keeps, what each check fails on, what update-vault.py draws and where, how they are tested and where CI runs them, and what to do when one fails. Read it before you change a script, or when a check fails. |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push to the default branch,
from each document's own frontmatter.

---

## 🔗 See also

- [Documentation index](../README.md) - every document the vault keeps in `.docs/`
- [Template catalogue](../templates/README.md) - every seed, and where each one is copied to

---

<div align="center">

**Write down what the code cannot say.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
