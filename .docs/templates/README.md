<!--
title: '📋 DOCUMENT TEMPLATES'
description: 'The forms for the documents a vault keeps about itself in .docs/: a decision record, a design, a plan, a research log, a runbook and a post-mortem, with a user story and the formats for notes that go into issues. Read it before writing one, to see what each form is for and where its copy goes.'
type: index
keywords: [work-product forms, decision record, design, plan, research log, runbook, post-mortem, user story]
-->

<div align="center">

# 📋 DOCUMENT TEMPLATES

<a name="top"></a>

**The forms for the documents a vault keeps about itself, and where each copy goes.**

_A form for each kind of document, and only those._

</div>

---

## 💡 What This Folder Is For

The forms here are for the documents a vault keeps about itself, in `.docs/`: a decision about its
layout, its rules, its scripts or its automation; the design and the plan for a change to them; the
research behind one; the steps for a routine task or a known failure; and what was learned when
something went wrong. Each such copy is a page, so its form carries the page format with
placeholders, and the copy keeps it ([Note Schema](../technical/vault/Note-Schema.md)).

They are not for the vault's notes. A note is made from the scaffold in its folder's `.template/`,
as that folder's README says: a decision in the owner's own life is a record in `Memory/Decisions/`,
made from `Memory/.template/Decision.md`, a venture's decision goes in its
`Administration/Decisions.md`, and research about anything but the vault itself, such as the owner's life, a
venture or the world, is a report held in `Inbox/Research/`. No rule makes a form here binding: each is used when it helps, research before
direction, a design before the build, a post-mortem after a failure.

---

## 📋 The Templates

| Template                                         | What it is for                                                                   | Its copy goes to                                                | The copy's type              |
| :----------------------------------------------- | :------------------------------------------------------------------------------- | :-------------------------------------------------------------- | :--------------------------- |
| [🧭 ADR](ADR.md)                                 | One decision about the vault itself: its layout, rules, scripts or automation    | `.docs/adrs/ADR-[NNNN]-[Short-Slug].md`, taking the next number | `record`                     |
| [📐 Technical Design](Technical-Design.md)       | A change to the vault's machinery, designed before it is built                   | `.docs/technical/designs/[Short-Slug].md`                       | `record`                     |
| [📜 Implementation Plan](Implementation-Plan.md) | The steps that carry a change out, their order and the checks that prove them    | `.docs/technical/plans/[Short-Slug].md`                         | `record`                     |
| [🔎 Research Log](Research-Log.md)               | The sourced research behind a change to the vault                                | `.docs/technical/research/[Topic].md`                           | `record`                     |
| [📒 Runbook](Runbook.md)                         | The steps for one routine task or one known failure in the vault's machinery     | `.docs/operations/runbooks/[Short-Slug].md`                     | `guide`                      |
| [📉 Post-Mortem](Post-Mortem.md)                 | What went wrong, such as a leak or a lost change, and what changes because of it | `.docs/operations/post-mortems/[YYYY-MM-DD]-[Short-Slug].md`    | `record`                     |
| [👤 User Story](User-Story.md)                   | A need a change to the vault must meet, with the criteria that show it is met    | An issue opened from ✨ Feature Request                         | None: the issue is the story |
| [💬 Communication](Communication.md)             | Meeting notes and status updates                                                 | Pasted into an issue, a discussion or a pull request            | None: never a file           |

Each form opens with a note, which starts "On copying", saying where its copy goes and what the copy
needs. Every decision record is listed in the [ADR index](../adrs/README.md), which draws each row
from the record's own frontmatter.

---

## 🚫 What Is Not Here

The golden path template, tannergolden/path, ships more under its `docs/templates/`: fill-in
standards for a software repository, covering its architecture, stack and source, its API, data
model and interface, its tests, pipelines and deployment, its incidents, threats and dependencies,
its releases and its glossary, and a seed for a project's front page. A vault is a personal
knowledge base, not a software project, so none of them can apply to it, and a vault's front page
is its own.

The template every vault is made from, tannergolden/knowledge, keeps none of them, and takes
nothing from the golden path's `docs/templates/`: the forms here are its own, written for a vault,
and no sync brings the others back
([ADR-0007](https://github.com/tannergolden/knowledge/blob/Development/.docs/adrs/ADR-0007-The-Vault-Keeps-Only-The-Templates-It-Uses.md),
kept in the template). A software repository the owner builds is generated from tannergolden/path,
which ships them.

---

## ✍️ How A Copy Is Made

1. **Copy** the form to the place its row names, and never fill in the form itself. The note at its
   top says what the copy needs, and is deleted from the copy.
2. **Replace every `[bracketed]` placeholder**: the title and the H1 alike, with the form's emoji
   and the copy's own title, fully capped; the one-line description, the tagline and the closing
   phrase, each the copy's own; and a description and keywords of the copy's own, without
   `template`. The `type` becomes the one its row names, and a choice such as `[a / b / c]` becomes
   the one that holds.
3. **Delete a section that does not apply**, rather than leave it empty.
4. **Link the copy from the pull request** that carries the change it records, so the reasoning
   stays traceable. A folder under `.docs/` that does not exist yet, such as `runbooks/`, is made
   with its own `README.md` when its first document arrives.

---

## 🔄 Kept Current

These forms are written for a vault by the template every vault is made from,
tannergolden/knowledge, which no longer takes them from the golden path. Every vault keeps them,
and this README, current from it through 🔄 Template Sync, merged with anything its owner changed;
a `#` in front of a form's line in `.github/template-sync` keeps that form as its owner's. A copy
made from a form is its owner's from the moment it is made, and no sync ever touches it.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                              | Purpose                                                                                                                                                                                                                                                                                                          |
| :------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`ADR.md`](ADR.md)                                 | The form for one decision about the vault itself, such as its layout, its rules, its scripts or its automation: the context, the options weighed, the outcome and its consequences. Copy it to .docs/adrs/ when such a decision is made.                                                                         |
| [`Communication.md`](Communication.md)             | The formats for meeting notes and status updates written in this repository's issues, discussions and pull requests, and where each kind of message goes. A meeting in the owner's own life is a Memory event, and a project's progress goes in its Log, never these.                                            |
| [`Implementation-Plan.md`](Implementation-Plan.md) | The form for planning a change to the vault's own machinery in small, reviewable steps: its goal and scope, the changes in order, the risks, the checks that prove it and how to undo it. Copy it to .docs/technical/plans/ before the change is made.                                                           |
| [`Post-Mortem.md`](Post-Mortem.md)                 | The form for a blameless account of something that went wrong in the vault or its machinery, such as a leak, a lost change or a sync that overwrote work: what happened, why, and the actions that stop a repeat. Copy it to .docs/operations/post-mortems/.                                                     |
| [`README.md`](README.md)                           | This file.                                                                                                                                                                                                                                                                                                       |
| [`Research-Log.md`](Research-Log.md)               | The form for the research behind a change to the vault itself: a dated, sourced, claim-by-claim investigation, kept honest by its verification window. Copy it to .docs/technical/research/; research about anything else, such as the owner's life, a venture or the world, is held in Inbox/Research/ instead. |
| [`Runbook.md`](Runbook.md)                         | The form for the exact steps of one routine task or one known failure in the vault's machinery, such as restoring a note from git or renewing an expired token, written to be followed under pressure. Copy it to .docs/operations/runbooks/, once for each task or failure.                                     |
| [`Technical-Design.md`](Technical-Design.md)       | The form for designing a change to the vault's own machinery before it is built, such as a new folder, rule, script or workflow: its parts, the notes and fields it changes, its privacy, its checks and how existing notes and vaults take it. Copy it to .docs/technical/designs/.                             |
| [`User-Story.md`](User-Story.md)                   | The form for a need a change to the vault must meet, written from the side of whoever it serves, with the criteria that show it is met. Its copy is an issue opened from the Feature Request form, never a file: read it before opening one.                                                                     |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push to the default branch,
from each template's own frontmatter.

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**The forms a vault can fill in, and no others.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
