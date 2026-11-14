<!--
title: '🧩 MEMORY TEMPLATES'
description: 'The entry scaffolds, one per kind of memory: a person, an organization, a place, a decision, an event, an insight, a session summary, and a new collection''s README, each copied on its own and never edited in place. Read it before making a Memory entry from one of them.'
type: 'index'
keywords: ["entry templates", "memory scaffolds", "person", "decision", "event", "session summary", "copy to file"]
-->

<div align="center">

# 🧩 MEMORY TEMPLATES

<a name="top"></a>

**One scaffold per kind of memory, each copied to make one new entry.**

_Copy one, fill in what is known, leave the rest blank._

</div>

---

## 💡 What This Folder Is For

The scaffolds every Memory entry is made from, one per kind of memory. Each is copied on its own, to make one new entry, by the note at its top, a comment that opens `On copying:` and says where the copy goes and what it needs, and that is deleted from the copy. A scaffold is never edited in place. This README explains them and is never copied.

---

## 🗂️ The Templates

| Template | Makes | Copied to | The copy's type |
| -------- | ----- | --------- | --------------- |
| `Person.md` | A person in the owner's personal orbit | `Memory/Entities/People/<First Last>.md` | `record` |
| `Organization.md` | An organization in the owner's personal life that is not one of their ventures | `Memory/Entities/Organizations/<Name>.md` | `record` |
| `Place.md` | A place of personal significance | `Memory/Entities/Places/<Name>.md` | `record` |
| `Decision.md` | A significant decision: its context, the alternatives, the outcome and the lessons | `Memory/Decisions/<YYYY-MM-slug>.md` | `record` |
| `Event.md` | One atomic, dated event | `Memory/Events/<YYYY-MM-DD-slug>.md` | `record` |
| `Insight.md` | A synthesized insight about the owner's outside world, with its evidence | `Memory/Insights/<YYYY-MM-slug>.md` | `record` |
| `Session Summary.md` | The delta-update summary of one session | `Memory/Context/Current/<YYYYMMDD-HHMMSS>.md` | `record` |
| `Collection Index.md` | The README of a new per-entry collection | `README.md` in the new collection's folder | `index` |

---

## ✍️ How A Copy Is Made

- **One file at a time.** A template is copied, never moved or edited in place, and this folder is never copied whole.
- **By the note at its top.** Each scaffold opens with a comment that begins `On copying:`: where the copy goes, what its type becomes, what to replace, and what its folder's README asks of an entry. The note is deleted from the copy.
- **Every placeholder is replaced.** The copy gets its real `title`, the same text as its H1, its real `description`, and its `type`, never `template`, which `lint-notes.py` refuses outside a `.template/` folder. Its keywords become its own: lowercase, at most eight, each distinct, none already in the title, with `template` dropped (`.docs/technical/vault/Keywords.md`). Each `[bracketed]` prompt gets its real value or is deleted. Only what is known is filled in: a field nobody knows stays blank rather than guessed.
- **Dates are ISO 8601.** A date reads `YYYY-MM-DD`, or `YYYY-MM` when only the month is known, and a dated entry's file name starts with its date, so entries sort by time; an event known only to its month takes `00` for its day, `YYYY-MM-00-slug.md`, which sorts first in its month.
- **Provenance goes in the body.** `As of:` and `Recorded:` lines date each fact, and a fact that changes is superseded, never rewritten: a superseded decision or insight sets its Status and takes `status: deprecated` (`Memory/README.md`, Writing An Entry).
- **No wikilinks.** An entry cross-references with plain-path `Related:` lines; only a folder's README carries wikilinks (`.docs/technical/vault/Link-Topology.md`). A scaffold neither carries nor receives one, and the catalog leaves this folder out.
- **A collection's README is always `README.md`.** It is never named after its folder: a note named after its folder repeats the folder's README, and `lint-notes.py` flags it.
- **The lists draw themselves.** After an entry is written, `python3 .github/scripts/update-vault.py` lists it in its collection's README and moves session summaries down their tiers; a generated list is never edited by hand.
- **A new collection is registered.** A new collection's folder is created only with the owner's yes (the root `README.md`, Ask First). Its entries get a scaffold of their own here, proposed first, and its list is drawn only once the folder is added to `COLLECTIONS` in `.github/scripts/vault.py`.

---

<div align="center">

**Copy the scaffold, never the folder.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
