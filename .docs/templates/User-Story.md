<!--
title: '👤 USER STORY'
description: 'The form for a need a change to the vault must meet, written from the side of whoever it serves, with the criteria that show it is met. Its copy is an issue opened from the Feature Request form, never a file: read it before opening one.'
type: 'template'
keywords: ['requirement', 'acceptance criteria', 'feature request', 'issue', 'template']
-->

<!-- On copying: open an issue from the ✨ Feature Request form and carry this story into its fields: the story line into Summary, whoever it serves into Who is affected, the need into Problem / motivation, the acceptance criteria into Acceptance criteria, what it leaves out into Scope / out of scope, what it waits on into Dependencies / risks, and what it touches into Additional context / links. There is no stories folder: the issue is the story, and the pull request that meets it closes it. Replace every [bracketed] placeholder, and keep the owner's personal context out of an issue on a public repository. Delete this note from the copy. -->

<div align="center">

# 👤 USER STORY

<a name="top"></a>

**A need a change to the vault must meet, and the criteria that show it is met.**

_The need first, then the change._

</div>

---

## 👤 The Story

**As** [the owner / an AI working in the vault / someone generating a vault from the template],
**I want** [to do something],
**so that** [the goal it serves].

---

## ✅ Acceptance Criteria

Each is an outcome that can be checked, never a detail of how it is built:

- [ ] Given [the state of the vault], when [the action], then [the result].
- [ ] Given [the state of the vault], when [the action], then [the result].
- [ ] [A note, a field or a file that is missing or wrong] is reported, never passed in silence.

---

## 🚫 Out Of Scope

- [What this story leaves out, so it stays one story]

---

## 🔗 Dependencies

- [The stories, changes or decisions it waits on]

---

## 🗂️ What It Touches

- **Folders and notes**: [The folders and notes it changes]
- **Frontmatter and generated parts**: [The fields, the generated blocks or the catalog records it
  adds or changes]
- **Scripts and workflows**: [The scripts, checks and workflows it changes]

---

## 🏁 Definition Of Done

- [ ] Every acceptance criterion holds, checked by a test where one can be written
- [ ] `python3 .github/scripts/check-vault.py` passes, and `update-vault.py` has nothing left to
      redraw
- [ ] The README of each folder it changes says what changed
- [ ] Merged through a pull request that closes the issue

### 🔗 See also

> [!TIP]
> The [✨ Feature Request form](/.github/ISSUE_TEMPLATE/Feature-Request.yaml) is where a story goes,
> and a [Technical Design](/.docs/templates/Technical-Design.md) works out how to meet it. Every
> canonical guide is indexed in the
> [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md).

---

<div align="center">

**A need is met when its criteria hold.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
