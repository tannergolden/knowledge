<!--
title: '🗂️ NOTE SCHEMA'
description: 'The frontmatter every note in the vault carries, field by field, and how a change to it reaches every note.'
tags: [frontmatter, schema, obsidian-vault, notes]
category: docs
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🗂️ NOTE SCHEMA

<a name="top"></a>

**The frontmatter every note in the vault carries, and what each field is for.**

_One schema, every note, checked on every edit._

</div>

---

## 🎯 The Rule

Every note in the vault opens with a YAML frontmatter block in the schema below. A note is any
`.md` file in the seven top folders, their `.template/` scaffolds included. The `README.md`
pages, [`AGENTS.md`](../../AGENTS.md) and everything under a hidden folder are not notes.

The block is a `---` fence, not the hidden comment the
[Document Styling guide](https://github.com/tannergolden/standards/blob/Development/docs/technical/interface/Document-Styling-&-Formatting.md#-frontmatter-metadata)
asks of other documents: Obsidian reads a note's properties only from that fence, and the guide
exempts a vault's notes for that reason.

`.github/scripts/lint-notes.py` checks every note against the schema. The Claude Code hook runs it
on each note an agent writes, and CI runs it on every note. A note found without frontmatter is
flagged and given one before it moves anywhere.

---

## 🧾 The Fields

Fields come in two bands: a human band shown in Obsidian, then a system band hidden by a CSS
snippet. The band comments below are illustrative; real notes carry no comments.

<details>
<summary>The full schema, field by field</summary>

```yaml
---
# Human band - shown in Obsidian (the fields you read and edit)
title: '' # Human-readable title
description: '' # One or two specific sentences saying what the note is and when to use it. Do not echo the title or stuff keywords.
status: '' # draft | active | deprecated | archived. Retrieval reads deprecated and archived last. Kept and searchable, never deleted.
tags: [] # The closed vocabulary only (Tag-Vocabulary.md): Folder + File Role + optional startup / sensitive / freshness
aliases: [] # Other names the note goes by: acronyms, former titles, misspellings. Substitutable for the title. May be empty.
keywords: [] # 4-8 lowercase search terms a person would type that the title lacks. May be empty.
created: YYYY-MM-DD # Unquoted ISO date, so Obsidian types it as a Date. When the note was created.
updated: YYYY-MM-DD # Unquoted ISO date. When the content last changed meaningfully.
# System band - hidden in Obsidian by .obsidian/snippets/brain-hide-system.css (derived from location)
type: '' # The File Role tag: guide | information | template | log | record | self | reference | script | agent
folder: '' # The Folder tag: library | profile | memory | projects | ventures | system | inbox
layer: 0 # 1 = a file in a top folder, 2 = one folder deeper, and so on
policy: false # true if the note carries an embedded policy, such as a retention policy
author: '' # Who the note belongs to: the vault's owner
path: '' # The path from the vault root, as "BRAIN/Memory/Log.md"
id: '' # A stable slug: a two-letter folder prefix and the hyphenated name. Chosen once, never regenerated.
---
```

</details>

The schema is flat, with no nested keys, because the scripts and Obsidian both read flat
properties. `aliases`, `keywords` and `tags` are lists, written inline (`["a", "b"]`). The
`policy` and `status` flags are fields, not tags.

### Bands In Obsidian

- **Human band (shown):** `title`, `description`, `status`, `tags`, `aliases`, `keywords`,
  `created`, `updated`. The fields a person reads or edits.
- **System band (hidden):** `type`, `folder`, `layer`, `policy`, `author`, `path`, `id`. Derived
  from where the note sits, or constant in a personal vault.

`.obsidian/snippets/brain-hide-system.css` hides the system band from the property panel (enable
it under Settings → Appearance → CSS snippets). It hides them only from view: every field stays in
the YAML, required as before. Write the fields in the order above, so the panel reads cleanly with
or without the snippet; the scripts read them in any order.

### Identity And Discovery

- **`id`** is the note's lasting identity: a lowercase, hyphenated slug with a two-letter folder
  prefix (`li-`, `me-`, `pr-`, `ve-`, `sy-`, `id-`, `in-`), chosen once when the note is created
  (the prefix, then the name as a slug, with `-2`, `-3` on a clash) and never regenerated, so links
  and references survive renames and moves. Ids are unique across the vault, and the linter checks
  both the form and the uniqueness.
- **`aliases`** are other names the note goes by. An alias must be able to stand in for the title;
  related topics belong in `keywords`. On a rename, add the old title as an alias.
- **`keywords`** are free-text search terms: 4-8 distinctive, lowercase words a person would type
  that are not already in the title, including how they would phrase the problem. They are the
  deliberate exception to the closed tag vocabulary: subject matter lives here, never in `tags`.

### Dates

Change `updated` whenever a note's content changes meaningfully, and not for formatting or
whitespace. The date says when the information itself last changed.

### No Per-File Versions

No note carries a `version` field, and the linter rejects one. The vault's history is its git
history. A skill keeps its own version, in its `SKILL.md` and its `Changelog.md`, because a skill
ships outside the vault (`System/Skills/Skills.md`).

---

## 🖼️ Files That Cannot Carry Frontmatter

An image, a PDF, a script, audio, video or an archive carries no tags of its own. Its folder places
it, and the folder's note describes it, so name it so its subject is plain from the name.

---

## 🔍 Filtering By Frontmatter

The fields narrow a search before any note is opened:

| Field or tag                       | Narrows to                                                             |
| :--------------------------------- | :--------------------------------------------------------------------- |
| `folder`                           | One top folder                                                         |
| `layer`                            | Lower numbers first: layer 1 is a top folder's own files               |
| `type`                             | The kind of note, before you open it                                   |
| `startup`                          | The notes an agent reads at the start of every session                 |
| `sensitive`                        | Personal or private data: surface it with discretion                   |
| `policy: true`                     | Notes that carry an embedded policy, such as a retention policy        |
| `timeless`, `enduring`, `current`  | Library notes by how long they stay true (`Library/Library.md`, Rules) |
| `status: deprecated` or `archived` | Superseded notes, which retrieval reads last                           |

`System/Data/catalog.ndjson` holds every note's title, description, tags and keywords, one line
each, for a search that reads no note at all.

---

## 🔁 A Schema Change Reaches Every Note

The schema is vault-wide. When it changes, every existing note takes the change in the same
commit, never lazily as notes happen to be edited: a change that reaches new notes only is
unfinished, and a lint failure.

A change to the schema means adding, removing or renaming one of the fields above, or changing
its form or allowed values. Make all of it, in order:

1. Change this page.
2. Change the scripts and the scaffolds: `REQUIRED_FIELDS` and the vocabulary in
   `.github/scripts/vault.py`, any rule in `lint-notes.py`, and every `.template/` file.
3. Bring every existing note to the new shape, in the same commit.
4. Run `check-vault.py`. The change is done only when no note reports a schema error; the linter
   checks every required field on every note, so a newly required field shows up on each note that
   lacks it.

**Do not over-apply this.** A field meant for one kind of note is not part of the schema, is not
added here, and is not backfilled across the vault. It is documented where that kind is defined,
as a team roster's `members` and `lead` are, and lives only on those notes. Reach for one only
when no field here already carries the meaning: staleness, for instance, is `status`, not a field
of its own.

---

<div align="center">

**One fence, fifteen fields, every note the same.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
