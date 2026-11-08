<!--
title: '🔗 LINK TOPOLOGY'
description: 'Which notes may wikilink which, so the vault''s graph mirrors its folder tree and never loops.'
type: standard
keywords: [wikilinks, graph]
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🔗 LINK TOPOLOGY

<a name="top"></a>

**Which notes may wikilink which, so the graph mirrors the folder tree.**

_Links flow downhill. Backlinks carry the way back._

</div>

---

## 🎯 The Rule

Whenever a note names an entity the vault has a file for (a project, a venture, a person, a
concept), it uses a wikilink, `[[Filename]]`, wherever the topology below allows the edge, and a
plain code-style path where it does not. The links make the vault a knowledge graph that a reader,
Obsidian and `check-links.py` can walk.

`.github/scripts/check-links.py` enforces the topology: it fails on a link to nothing, a link the
topology does not allow, a link into a scaffold and two notes that link each other, and warns on a
link that matches several files and on longer cycles. Links inside code, or inside a `%%`
comment, are not links.

---

## 🌳 Hub-Only Tree

The graph mirrors the file tree, and only a folder's `README.md`, its note, carries edges:

| From                                   | May wikilink                                                                                                                 |
| :------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------- |
| A folder's README (`Memory/README.md`) | The files in its own folder, and the `README.md` of each immediate subfolder, one level down                                 |
| Any other note                         | **Nothing.** Every reference is a plain code-style path; its hub's link already leads to it                                  |
| A file at the vault root               | Nothing. The root holds no notes: its `README.md` and `AGENTS.md` are pages, which name files by Markdown link or plain path |

- **Links cascade, never reciprocate.** Links run from the top folders down to their files, from
  the general to the specific. A note never links back to a note that links to it: the
  forward link already records the edge. Where two notes both want the edge, the one nearer the root carries
  it, and the graph stays acyclic.
- **Related folders connect through their common parent**, never sideways.
- **The memory tiers are ordinary.** `Memory/README.md` links `Context/README.md`, which links the
  tiers' READMEs (`Current`, `Recent`, `Archive`); the tiers do not link each other, and the cascade
  between them is described in prose. Each tier's README links the summaries in its own folder, and
  `update-vault.py` keeps those links current as summaries move.

---

## 🚫 Where Wikilinks Never Go

- **A `.template/` folder** neither contains wikilinks nor receives them, its own `README.md`
  included. A scaffold is not a graph node, and a link to one drags it into the graph. Name a
  scaffold by plain path. A venture's or a project's README, copied from a scaffold, may link once it
  is copied, as any folder's README does, and a venture's carries the block in which
  `update-vault.py` draws its list of subfolders.

---

## ✍️ Writing A Link

- **Leave off the extension:** `[[Log]]`, not `[[Log.md]]`.
- **Name a folder by its README:** a folder's note is its `README.md`, and every folder has one, so a
  link to a folder gives the README's path and the folder's name as the alias:
  `[[Library/README|Library]]`, `[[Memory/Entities/People/README|People]]`. A bare `[[README]]`
  matches every folder's README, and the checker warns that it needs a path.
- **Give a common name its folder:** `[[Memory/Log|Log]]` or `[[Ventures/Company/Log|Company Log]]`
  for names such as `Log.md` and `Overview.md` that many folders share.
- **Alias for reading:** `the [[Profile/Working Style|owner's preferences]]`.

Examples inside code spans, like these, are text: they create no edge, and the checker skips them.

---

<div align="center">

**The tree is the graph. Nothing links back up it.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
