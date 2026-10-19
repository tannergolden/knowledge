<!--
title: '🏷️ TAG VOCABULARY'
description: 'The closed set of tags a note may carry, what each one means, and the order they are written in.'
tags: [tags, vocabulary, obsidian-vault, search]
category: docs
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🏷️ TAG VOCABULARY

<a name="top"></a>

**The closed set of tags a note may carry, and what each one means.**

_A tag shared by many notes finds them; a tag on one note finds nothing._

</div>

---

## 🎯 The Rule

Every note is tagged from one **fixed, closed vocabulary**. Tags exist for one purpose: fast,
reliable filtering, in an agent's retrieval, in Obsidian and in the vault's catalog. To stay useful,
every tag is shared across many notes and drawn only from the lists below.

**There are no free-form "content" tags.** A tag that lands on a single note is noise. Subject
matter is found by the folder a note sits in (the path is the subject:
`Library/Society & Social Sciences/Economics/`), by full-text search, and by the `keywords` field,
never by tags.

`.github/scripts/lint-notes.py` rejects any tag outside this vocabulary, on every edit an agent
makes and in CI. A note whose tags break it is broken; never leave one that way.

---

## 🧾 The Five Dimensions

Apply tags in this order:

| #   | Dimension       | Required?         | Values                                                                              |
| :-- | :-------------- | :---------------- | :---------------------------------------------------------------------------------- |
| 1   | **Folder**      | Always, exactly 1 | `library` `profile` `memory` `ventures` `projects` `system` `inbox`                 |
| 2   | **File Role**   | Always, exactly 1 | `guide` `information` `template` `log` `record` `self` `reference` `script` `agent` |
| 3   | **AI Signal**   | When true         | `startup`                                                                           |
| 4   | **Sensitivity** | When true         | `sensitive`                                                                         |
| 5   | **Freshness**   | When meaningful   | `timeless` `enduring` `current`                                                     |

A note carries exactly one Folder tag and one File Role tag; the rest apply only when true, so
most notes carry two to four. Whether a note holds an embedded policy is the `policy` field, not a
tag ([Note Schema](Note-Schema.md)).

### Folder

The top folder the note sits in. It matches the note's `folder` field.

```txt
Memory/Log.md                  → memory
Profile/Personality.md         → profile
System/Skills/Skills.md        → system
```

### File Role

The one kind of note this is. It matches the note's `type` field.

| Tag           | For                                                                                                                             |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------ |
| `guide`       | Operating manuals and how-to notes                                                                                              |
| `information` | A folder's own note, named after the folder (`Memory/Memory.md`)                                                                |
| `template`    | A blank scaffold inside a `.template/` folder                                                                                   |
| `log`         | A chronological log of progress or events (`Log.md`)                                                                            |
| `record`      | A curated record that is not a strict event log: a decision, a person's entry, `Memory/Dates.md`                                |
| `self`        | A profile note describing the vault's owner, in `Profile/` (`Biography.md`, `Personality.md`)                                   |
| `reference`   | Library source material: books, primers, articles. `information` stays for folder notes                                         |
| `script`      | Executable code                                                                                                                 |
| `agent`       | An agent spec in the workforce (`Ventures/Agent Resources (AR)/<department>/<Role>.md`) or a standing team (`Inbox/Faculties/`) |

An `agent` note's role is its `title`, equal to its file name; its spoken name is `name`, and
`tools` lists what it may use. Workforce-wide rules live in `Agent Resources (AR).md`.

### AI Signal

`startup` marks a note an agent reads at the start of every session. It decides the startup set by
itself: the session-start hook reads the tag. There is no `ai-managed` tag; the whole vault is
maintained by its agents, so it would tell nothing apart.

### Sensitivity

`sensitive` marks a note holding personal, private or identifying information: biography, health,
finances, relationships, beliefs. Every note in `Profile/` is sensitive by default.

### Freshness

One of `timeless`, `enduring` or `current`, by the Library's freshness tiers (`Library/Library.md`,
Rules). Library holdings always carry one; other notes carry one where freshness means something,
and a system note is usually `timeless`. Templates, folder notes and logs leave it off.

---

## ✍️ How Tags Are Written

- Lowercase, copied exactly from the vocabulary.
- A multi-word tag uses hyphens, and no other special character.
- No trailing spaces or punctuation inside a tag.
- An inline array: `tags: ["memory", "log", "startup"]`.

---

## 🔍 Discovery Fields Are Not Tags

The closed vocabulary governs `tags` alone. Two fields are free text on purpose, to carry the
subject terms and synonyms tags may not: `keywords`, 4-8 distinctive search terms a person would
type that the title lacks, and `aliases`, other names that can stand in for the title. They carry
no policy meaning. [Note Schema](Note-Schema.md) defines both.

---

<div align="center">

**Shared tags find notes. Subject lives in the path.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
