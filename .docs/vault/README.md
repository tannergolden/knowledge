<!--
title: '🧠 VAULT REFERENCE'
description: 'The reference pages behind the vault''s rules: its note schema, keywords, link topology and context assembly.'
type: index
keywords: [schema]
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🧠 VAULT REFERENCE

<a name="top"></a>

**The reference pages behind the vault's rules, kept out of every session's context.**

_The rules say what to do. These pages say exactly how._

</div>

---

## 💡 What This Folder Is For

[`AGENTS.md`](../../AGENTS.md) holds the vault's rules in one line each, and each folder note holds
its folder's. The long reference parts those lines point to live here, so an agent reads them when
a task needs them rather than at the start of every session. They are pages, not notes: the vault's
walk skips this folder, and the vault's checks read the same rules from `.github/scripts/vault.py`.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                        | Purpose                                                                                                                     |
| :------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------- |
| [`Context-Assembly.md`](Context-Assembly.md) | How an agent assembles context from the vault so nothing it must remember sits where models forget.                         |
| [`Keywords.md`](Keywords.md)                 | How a note is found without tags: its path, its title and a few keywords, and the controlled tokens the Library filters on. |
| [`Link-Topology.md`](Link-Topology.md)       | Which notes may wikilink which, so the vault's graph mirrors its folder tree and never loops.                               |
| [`Note-Schema.md`](Note-Schema.md)           | The frontmatter every note in the vault carries, field by field, and how a change to it reaches every note.                 |
| [`README.md`](README.md)                     | This file.                                                                                                                  |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push.

---

<div align="center">

**One line in the rules, the whole of it here.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
