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

The scaffolds every Memory entry is made from, one per kind of memory. Each is copied on its own, to make one new entry, by the instantiation note at its top (the comment that says where the copy goes and what it needs), and is never edited in place. This README explains them and is never copied.

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
| `Collection-Index.md` | The README of a new per-entry collection | The new collection's folder, as `README.md` | `index` |

---

## ✍️ How A Copy Is Made

- **One file at a time.** A template is copied, never moved or edited in place, and this folder is never copied whole.
- **Every placeholder is replaced.** The copy gets its real `title`, `description` and `type`, never `template`, which `lint-notes.py` refuses outside a `.template/` folder, and its keywords lose `template`. Only what is known is filled in: a field nobody knows stays blank rather than guessed.
- **Provenance goes in the body.** `As of:` and `Recorded:` lines date each fact, and a fact that changes is superseded, never rewritten (`Memory/README.md`).
- **No wikilinks in an entry.** An entry cross-references with plain-path `Related:` lines; only a folder's README carries wikilinks (`.docs/technical/vault/Link-Topology.md`).
- **A collection's README is always `README.md`.** It is never named after its folder: a note named after its folder repeats the folder's README, and `lint-notes.py` flags it.
- **The lists draw themselves.** After an entry is written, `python3 .github/scripts/update-vault.py` lists it in its collection's README and moves session summaries down their tiers; a generated list is never edited by hand.
- **A new collection is registered.** A new collection's folder is created only with the owner's yes (the root `README.md`, Ask First), and its list is drawn only once the folder is added to `COLLECTIONS` in `.github/scripts/vault.py`.
- A scaffold neither carries nor receives a wikilink, and the catalog leaves this folder out.

---

<div align="center">

**Copy the scaffold, never the folder.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
