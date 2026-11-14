<!--
title: '🧩 LIBRARY TEMPLATES'
description: 'The cataloging scaffolds: a reference note, a source catalog card and a division README. Read it before copying one to make a new Library note; each is copied on its own and never edited in place.'
type: 'index'
keywords: ["cataloging templates", "reference note", "catalog card", "division readme", "scaffolds", "copy to file"]
-->

<div align="center">

# 🧩 LIBRARY TEMPLATES

<a name="top"></a>

**The scaffolds the Library's notes are copied from, one file at a time.**

_Copied, filled and filed, never edited in place._

</div>

---

## 💡 What This Folder Is For

The scaffolds the Library's notes are made from. Each is copied on its own, to make one new note, by the note at its top, a comment that opens `On copying:` and says where the copy goes and what it needs, and that is deleted from the copy. A scaffold is never edited in place. This README explains them and is never copied.

---

## 🗂️ The Templates

| Template | Makes | Copied to | The copy's type |
| -------- | ----- | --------- | --------------- |
| `Reference Note.md` | A synthesized reference note, the common Library holding | Its one class and division: `Library/<Class>/<Division>/<Note Title>.md` | `reference` |
| `Source Catalog Card.md` | The catalog card of an outside source: a book, paper, article, report, video or dataset | Its one class and division, beside any held copy of the work: `Library/<Class>/<Division>/<Work Title>.md` | `reference` |
| `Division.md` | The README of a new division, written when the division is added, with the owner's yes | `Library/<Class>/<Division>/README.md` | `index` |

---

## ✍️ How A Copy Is Made

- **It is classified first.** A holding's freshness tier comes from the Rules in `Library/README.md`, and nothing with under five years of useful life is copied in at all; its class and division come from the classification rules, boundary rulings and worked examples there.
- **One file at a time.** A template is copied, never moved or edited in place, and this folder is never copied whole.
- **By the note at its top.** Each scaffold opens with a comment that begins `On copying:`: where the copy goes, what its type becomes, what to replace, and what `Library/README.md` asks of it. The note is deleted from the copy.
- **Every placeholder is replaced.** The copy gets its real `title`, the same text as its H1, its real `description`, and its `type`, never `template`, which `lint-notes.py` refuses outside a `.template/` folder. Its keywords become its own: lowercase, at most eight, each distinct, none already in the title, with `template` dropped (`.docs/technical/vault/Keywords.md`). Each `[bracketed]` placeholder gets its real value, so no placeholder reaches the catalog. An outside source is cited with its date as precise as the source gives it: its year, `YYYY`, for a book, and for a web source the day it was read, `YYYY-MM-DD`.
- **A holding carries one freshness token.** A reference note or a catalog card leads its keywords with `freshness/timeless`, `freshness/enduring` or `freshness/current` (`Library/README.md`, Rules), in place of the scaffold's `freshness/[tier]`, and `lint-notes.py` refuses a holding without one; a division's README carries none.
- **A division's README is always `README.md`, and a page.** It keeps the scaffold's page format, the centered header and the footer, with its emoji, its fully capped name, its one-line description, its tagline and its closing phrase filled in (`.docs/technical/vault/Note-Schema.md`). It is never named after its folder: a note named after its folder repeats the folder's README, and `lint-notes.py` flags it. The class's Divisions table gains a row for the new division, and `update-vault.py` adds it to the class's list of subfolders.
- **No wikilinks.** A scaffold neither carries nor receives a wikilink (`.docs/technical/vault/Link-Topology.md`), and the catalog leaves this folder out.

---

<div align="center">

**Every new holding starts from a clean blank.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
