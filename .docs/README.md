<!--
title: '📚 DOCUMENTATION'
description: 'Where this repository keeps its documents about the vault and its machinery, the forms those documents are copied from, and where the engineering standards it follows live. Read it before adding a document to .docs/.'
type: index
-->

<div align="center">

# 📚 DOCUMENTATION

<a name="top"></a>

**Two kinds of document, kept deliberately apart.**

_Standards are followed. Templates are filled in._

</div>

---

## 🧭 The Split

| Kind          | Where it lives                                                                                        | What you do with it        |
| :------------ | :---------------------------------------------------------------------------------------------------- | :------------------------- |
| **Standards** | [`tannergolden/standards`](https://github.com/tannergolden/standards/blob/Development/docs/README.md) | Follow by link, never copy |
| **Templates** | [`.docs/templates/`](templates/README.md)                                                             | Copy out, fill in, own     |

A standard describes how every repository works: branching, reviews, releases,
secrets, hygiene. It is shared, it changes centrally, and copying it here would
only produce a stale second copy.

A template is a form for a document the vault keeps about itself: a decision
record, a design, a plan, a research log, a runbook or a post-mortem. Nobody
else can write those for the vault, which is why the forms ship blank rather
than as law.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                     | Purpose                                                                                                                                                                                                                                                                                                |
| :---------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`adrs/`](adrs/README.md)                 | Architecture decision records, one file per decision, each logged with its status, date and evidence.                                                                                                                                                                                                  |
| [`distribution/`](distribution/README.md) | From a commit to a vault: how a change moves through the template and its releases into each vault, and any step a vault adds to the shared workflow. Read it before you cut a release or merge a sync pull request.                                                                                   |
| [`introduction/`](introduction/README.md) | Where to start: how the vault works, how to set one up, and how to change it without breaking what it promises. Read it before any other page in .docs/.                                                                                                                                               |
| [`library/`](library/README.md)           | What to learn, and where: guides, background and further reading for anyone new to the vault or the tools it runs on. Not the vault's Library/, which holds reference knowledge about the world.                                                                                                       |
| [`operations/`](operations/README.md)     | Keeping the vault healthy and safe: why it stays private, how a secret is kept out of it, and the runbooks and post-mortems written for it. Read it before you touch anything sensitive, or after something goes wrong.                                                                                |
| [`references/`](references/README.md)     | Things to look up about the vault: its glossary, and any catalogue or format its owner adds, the pages consulted rather than read through.                                                                                                                                                             |
| [`technical/`](technical/README.md)       | How the vault is built: how its scripts fit together, the reference pages behind its rules, and the designs, plans and research behind a change to the vault itself. Read it before you change a script, a rule or the layout.                                                                         |
| [`templates/`](templates/README.md)       | The forms for the documents a vault keeps about itself in .docs/: a decision record, a design, a plan, a research log, a runbook and a post-mortem, with a user story and the formats for notes that go into issues. Read it before writing one, to see what each form is for and where its copy goes. |
| [`Prompts.md`](Prompts.md)                | Ready-made prompts for working in this repository with an AI agent, in two sections kept apart: the Golden Path's own, and this repository's, which opens with the prompts for using and keeping a vault. &#x1F504; Template Sync keeps both current in a vault.                                       |
| [`README.md`](README.md)                  | This file.                                                                                                                                                                                                                                                                                             |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push to the default branch.
Every folder below this one carries a `README.md` that logs the files inside it,
so the tree reads one level at a time.

---

## 🌱 Using A Template

Copy a form out of `.docs/templates/` to the folder its row in the
[template catalogue](templates/README.md) names, then fill it in:

```txt
.docs/templates/Runbook.md
        ↓
.docs/operations/runbooks/[Short-Slug].md
```

**Anything in `[square brackets]` is yours to replace**: a prompt like `[why]`,
or a choice like `[High / Medium / Low]`, which becomes the one that holds. The
note at the top of each form, which opens "On copying", says where the copy
goes and what it needs, and is deleted from the copy. A file still carrying
brackets has not been filled in yet.

Whenever you run 🔄 Template Sync, it brings the forms themselves up to date:
each improvement arrives as a pull request that overwrites a form you had not
changed with the template's version, and merges one you had with your changes.
It never touches a document you copied out: from the moment you make it, that
copy is an ordinary file in your tree. Put a `#` in front of a form's line in
`.github/template-sync` to keep that form exactly as it is.

---

## 📁 The Seven Folders

`.docs/` is where the documents about the vault go: the pages this template
ships, and the ones you write or copy out of a form, not the folder the forms
sit in. It arrives in the same seven folders as the standards' own
documentation, so every repository on the standards reads the same way:

```bash
.docs/
├── introduction/        # how the vault works, setting up, changing it
├── distribution/        # how a change reaches a vault
├── technical/           # the machinery, designs, plans, research
├── operations/          # privacy and secrets, runbooks, post-mortems
├── references/          # the glossary
├── library/             # what to learn: guides, background, further reading
├── adrs/                # architecture decision records
└── templates/           # the forms, copied out into the folders above
```

Beside the seven folders sits [`Prompts.md`](Prompts.md): ready-made prompts for
working here with an AI agent, in two sections kept apart: the Golden Path's,
which tannergolden/path writes, and this repository's, which opens with this
template's prompts for using and keeping a vault. 🔄 Template Sync keeps the
whole page current in a vault, merged with any prompt its owner adds.

Each folder arrives with a `README.md` that says what belongs in it and logs its
files, beside any page this template ships there. Put each document you write in
the folder its kind names, and add folders below them as you grow: give each one
a `README.md` with a folder log between `AUTO-INDEX` markers, the way every
folder here does, and 🗂️ Machined Indexes keeps the log current. `templates/`
is not copied across: the forms stay where they are and you copy what you need.

**Use these folders unless your project needs its own.** They fit any project,
which is why the standards use the same seven. A vault keeps its notes in its
seven top folders, each explained by its own README, and keeps `.docs/` for the
pages about the vault and its machinery, which 🔄 Template Sync keeps current
with every README here. Put a `#` in front of a README's line in
`.github/template-sync` before you put its folder to another use, or the next
sync overwrites it.

---

## 🔗 See also

- [Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md) - every canonical guide
- [Template catalogue](templates/README.md) - what each form is for, and where its copy goes
- [Prompts](Prompts.md) - the Golden Path's prompts, and this repository's own
- [Repository README](../.github/README.md) - what this vault is and how it is governed

---

<div align="center">

**Follow the standards. Fill in the templates.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
