<!--
title: '🗂️ NOTE SCHEMA'
description: 'The frontmatter every note in the vault carries, field by field, and how a change to it reaches every note.'
type: standard
keywords: [frontmatter, notes]
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🗂️ NOTE SCHEMA

<a name="top"></a>

**The frontmatter every note in the vault carries, and what each field is for.**

_One hidden block, every note, checked on every edit._

</div>

---

## 🎯 The Rule

Every note in the vault opens with hidden frontmatter: an HTML comment holding a few flat fields
that tell a reader, or any tool, what the note is before the body is read. The fields are the account's own
standard,
[Frontmatter Metadata](https://github.com/tannergolden/standards/blob/Development/docs/technical/interface/Document-Styling-&-Formatting.md#-frontmatter-metadata)
in the Document Styling guide, so a note reads the same way as every document in every repository.

A note is any `.md` file in the seven top folders, their `.template/` scaffolds included. Each
folder's `README.md` is that folder's note, and carries this schema like any other. The `README.md`
at the vault root and everything under a hidden folder are not notes but pages: they carry the same
hidden block, as the styling guide asks of every page, and keep the rules they follow as pages.

`.github/scripts/lint-notes.py` checks every note against this page. Run it on a note after
changing it; CI runs it on every note, beside the account's frontmatter check over every document.
A note found without frontmatter is flagged and given one before it moves anywhere.

---

## 🧾 The Fields

```markdown
<!--
title: "Memory Log"
description: "Working memory: the capture stream where observations, events, and open threads land first. Read at session start."
type: "record"
keywords: ["working memory", "capture stream", "open loops", "quick capture"]
-->
```

| Field         | Required | Rule                                                                                                                                                                              |
| :------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `title`       | Yes      | The plain title, with no emoji: the note's H1 carries the emoji                                                                                                                   |
| `description` | Yes      | One or two specific, task-shaped sentences: what the note is and when to use it. Do not echo the title or stuff keywords                                                          |
| `type`        | Yes      | One of the six types below                                                                                                                                                        |
| `keywords`    | No       | Up to eight distinct, lowercase search terms that are not already in the title ([Keywords](Keywords.md))                                                                          |
| `status`      | No       | `draft`, `deprecated` or `archived`; left out while the note is current. Retrieval reads `deprecated` and `archived` notes last, and they stay kept and searchable, never deleted |

The block opens the file with `<!--` alone on the first line and closes with `-->` alone on its own
line. It is never fenced with `---`, which GitHub shows as a table at the top of the page. One field
to a line, flat, with a list written inline (`["a", "b"]`).

Nothing else is written. The folder, the author and the dates are what the path and git already
say, and a field that only repeats them drifts. A note's subject is its path, never a tag.

### Types

| Type        | Use for                                                                                     |
| :---------- | :------------------------------------------------------------------------------------------ |
| `index`     | A folder's own note, its `README.md` (`Memory/README.md`)                                   |
| `guide`     | An operating manual or a how-to                                                             |
| `standard`  | Rules a reader must obey                                                                    |
| `reference` | Material to look up: Library holdings, and the Profile's facts about the owner              |
| `record`    | A dated account: the Log, session summaries, decisions, entities, events, reports and ideas |
| `template`  | A scaffold inside a `.template/` folder; the copy takes its own type                        |

A `.template/` folder's own `README.md` is `index` when it explains a folder of scaffolds and is
never copied, such as `Memory/.template/README.md`, and `template` when its folder is copied whole,
such as a venture's or a project's, whose copy becomes that folder's `index`. A Profile folder facet's
`README.md` holds the facet itself, so it is `reference`.

### Fields Of A Kind

A record or a template may add the fields its own kind needs, defined once in its template and
documented where that kind is defined: an idea record's lineage `id`, `lifecycle` and scores, or a
research report's `review_by` date, both the `research-and-development` skill's. Such a field lives
only on its kind and is never added to this page.

### No Per-File Versions

No note carries a `version` field, and the linter rejects one. The vault's history is its git
history: `git log -- <path>` says when a note last changed.

---

## 🖼️ Files That Cannot Carry Frontmatter

An image, a PDF, a script, audio, video or an archive carries none of its own. Its folder places
it, and the folder's `README.md` describes it, so name it so its subject is plain from the name.

---

## 🔍 Filtering By Frontmatter

The fields narrow a search before any note is opened:

| Field or path                      | Narrows to                                                           |
| :--------------------------------- | :------------------------------------------------------------------- |
| The path                           | One top folder, then one subject                                     |
| `type`                             | The kind of note, before you open it                                 |
| `keywords`                         | Other names and the words a person types; in the Library, its facets |
| `status: deprecated` or `archived` | Superseded notes, which retrieval reads last                         |
| Anything under `Profile/`          | Personal data about the owner: surfaced with discretion              |

The files every session reads first are `STARTUP` in `.github/scripts/vault.py`, listed in the root
[`README.md`](../../../README.md), How A Session Goes. `System/Data/catalog.ndjson` holds every
note's path, title, type, keywords, description and status, one line each, for a search that reads
no note at all.

---

## 🔁 A Schema Change Reaches Every Note

The schema is vault-wide. When it changes, every existing note takes the change in the same
commit, never lazily as notes happen to be edited: a change that reaches new notes only is
unfinished, and a lint failure.

A change to the schema means adding, removing or renaming one of the fields above, or changing
its form or allowed values. Make all of it, in order:

1. Change this page.
2. Change the scripts and the scaffolds: `REQUIRED_FIELDS`, `TYPES` and the rest of the schema in
   `.github/scripts/vault.py`, any rule in `lint-notes.py`, and every `.template/` file.
3. Bring every existing note to the new shape, in the same commit.
4. Run `check-vault.py`. The change is done only when no note reports a schema error.

**Do not over-apply this.** A field of a kind is not part of the schema, is not added here, and is
not backfilled across the vault: a change to it touches only the notes of its kind. Reach for one
only when no field here already carries the meaning: staleness, for instance, is `status`, not a
field of its own.

---

<div align="center">

**One hidden block, five fields, every note the same.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
