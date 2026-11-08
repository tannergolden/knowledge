<!--
title: '📜 [THE CHANGE, FULLY CAPPED]'
description: 'The form for planning a change to the vault''s own machinery in small, reviewable steps: its goal and scope, the changes in order, the risks, the checks that prove it and how to undo it. Copy it to .docs/technical/plans/ before the change is made.'
type: 'template'
keywords: ['[a search term not in the title]', '[another name for the change]', 'template']
-->

<!-- On copying: copy this file to .docs/technical/plans/[Short-Slug].md, naming it in Capitalized-Kebab, to plan a change to the vault's own machinery in small, reviewable steps, after its design in .docs/technical/designs/ where it has one. Set type to 'record'. Replace every [bracketed] placeholder: the title and the H1 alike, with the change fully capped, the description with one of the plan's own, the one-line summary, the tagline and the closing phrase; give it up to eight lowercase keywords not already in the title, without 'template'. Delete a section that does not apply. If .docs/technical/plans/ does not exist yet, make it with its own README.md, as .docs/technical/README.md says. Delete this note from the copy. -->

<div align="center">

# 📜 [THE CHANGE, FULLY CAPPED]

<a name="top"></a>

**[One line: the change this plan carries out, and in how many steps.]**

_[A principle of this plan's own, shorter than the line above.]_

</div>

---

## 🎯 Goal

[What the change achieves and the problem it solves, in one or two sentences.]

- **Design**: [The design it carries out, in `.docs/technical/designs/`, as a link, or N/A]

---

## 🗺️ Scope

- **In scope**: [What this plan delivers]
- **Out of scope**: [What waits, or is left out]

---

## 🏗️ Proposed Changes

### [The folder, script or workflow it touches]

- [ ] [The change]
- [ ] [The change]

### [The next folder, script or workflow]

- [ ] [The change]

### Notes Already Written

- [ ] [How the notes that already exist take the change, in the same commit]

---

## 📅 Milestones

1. [What lands first, and why it goes first]
2. [What lands next]

---

## ⚠️ Risks & Mitigations

| Risk   | Likelihood            | Mitigation            |
| :----- | :-------------------- | :-------------------- |
| [Risk] | [High / Medium / Low] | [How it is contained] |

---

## 🧪 Verification Plan

### The Checks

Each runs from the vault root, in this order, once the change is written, as the root
[`README.md`](/README.md) says under Commands:

```bash
python3 .github/scripts/lint-notes.py "[each note the change writes]"
python3 .github/scripts/update-vault.py
python3 .github/scripts/check-vault.py
python3 -m unittest discover -s .github/scripts -p 'test_*.py'
```

The change is done when `check-vault.py` passes and a second run of `update-vault.py` has nothing
left to redraw.

### By Hand

1. [A step a reviewer takes, and what they should see]
2. [The next step]

---

## ⏪ Rollback

- [How to undo it: revert the pull request, or restore the files it changed from git history]

### 🔗 See also

> [!TIP]
> A [Technical Design](/.docs/templates/Technical-Design.md) comes before a plan, and
> [Vault Scripts](/.docs/technical/Vault-Scripts.md) says what each check fails on. Every canonical
> guide is indexed in the
> [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md).

---

<div align="center">

**[A closing phrase of this plan's own.]**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
