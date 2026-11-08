<!--
title: '🌿 DISTRIBUTION & WORKFLOW'
description: 'From a commit to a vault: how a change moves through the template and its releases into each vault, and any step a vault adds to the shared workflow. Read it before you cut a release or merge a sync pull request.'
type: index
-->

<div align="center">

# 🌿 DISTRIBUTION & WORKFLOW

<a name="top"></a>

**From a commit to a release, and from a release to each vault.**

_What the vault adds. The rest is in the standards._

</div>

---

## 💡 What This Folder Is For

How a change moves from its first commit to a release, and from a release into
each vault. Branching, commits, reviews, pipelines and versioning are written
down once, in the standards'
[Distribution & Workflow](https://github.com/tannergolden/standards/blob/Development/docs/distribution/README.md),
and followed here by link. This folder holds what the vault adds to them, or
does its own way.

- **How a change reaches a vault**: from the golden path template, through this
  template's releases, to each vault whose owner runs 🔄 Template Sync; which
  major a vault follows and how it takes a new one; and what a sync leaves
  alone, in [How A Change Reaches A Vault](How-A-Change-Reaches-A-Vault.md).
- **A step of your own**: anything you ask of every change to your vault that
  the standards do not ask everywhere.

How the checks are built, and where CI runs them, is technical, and lives in
[Vault Scripts](../technical/Vault-Scripts.md).

How A Change Reaches A Vault, like this README, is the template's, and
🔄 Template Sync keeps it current in a vault. A document you add here is
**yours from the first commit**: nothing upstream ever writes, moves or removes
it. The log below is redrawn from the files the folder holds.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                                                | Purpose                                                                                                                                                                                                                                                                                                                                                              |
| :------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`How-A-Change-Reaches-A-Vault.md`](How-A-Change-Reaches-A-Vault.md) | The path a change takes from tannergolden/path, the golden path template, through tannergolden/knowledge and its releases, into a vault whose owner runs &#x1F504; Template Sync, what each section of the sync list means for a vault, and what a sync leaves alone. Read it before you add a file the template ships, cut a release, or merge a sync pull request. |
| [`README.md`](README.md)                                             | This file.                                                                                                                                                                                                                                                                                                                                                           |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push to the default branch,
from each document's own frontmatter.

---

## 🔗 See also

- [Documentation index](../README.md) - every document the vault keeps in `.docs/`
- [Distribution & Workflow](https://github.com/tannergolden/standards/blob/Development/docs/distribution/README.md) - the shared workflow, from a branch to a release

---

<div align="center">

**Ship it the way it is written down.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
