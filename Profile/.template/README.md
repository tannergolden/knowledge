<!--
title: '🧩 PROFILE TEMPLATES'
description: 'The Profile scaffolds: a flat facet, the README of a facet that is a folder, a generic entry, and the entries of the folder facets (a belief, a goal, a skill, a health condition, a life chapter). Read it before copying one to add a facet or an entry, each copied on its own and never edited in place.'
type: 'index'
keywords: ["profile scaffolds", "facet overview", "folder facet", "entry templates", "belief", "goal", "skill", "copy to file"]
-->

<div align="center">

# 🧩 PROFILE TEMPLATES

<a name="top"></a>

**The blank facet overview and entries every new Profile note is copied from.**

_Copied only on a yes, and never edited in place._

</div>

---

## 💡 What This Folder Is For

The scaffolds the Profile's facets and entries are made from. Each is copied on its own, to make one new note, by the note at its top, a comment that opens `On copying:` and says where the copy goes and what it needs, and that is deleted from the copy. A scaffold is never edited in place. This README explains them and is never copied, and `profile-coverage.py` leaves it out when it reads the scaffolds' lines.

---

## 🗂️ The Templates

| Template | Makes | Copied to | The copy's type |
| -------- | ----- | --------- | --------------- |
| `Facet Overview.md` | A flat facet: one file, read as a whole | `Profile/<Facet>.md` | `reference` |
| `Folder Facet.md` | The README of a facet that is a folder: its overview, a page, above the generated list of its entries | `Profile/<Facet>/README.md` | `reference` |
| `Entry.md` | A generic entry inside a folder facet, for an item no other scaffold here fits | `Profile/<Facet>/<Title>.md` | `reference` |
| `Belief.md` | One held belief, isolated for privacy | `Profile/Values/<Title>.md` | `reference` |
| `Goal.md` | One enduring goal | `Profile/Goals/<Title>.md` | `reference` |
| `Skill.md` | One area of genuine depth | `Profile/Skills/<Title>.md` | `reference` |
| `Health Condition.md` | One health attribute or accessibility need, isolated for privacy | `Profile/Health/<Title>.md` | `reference` |
| `Life Chapter.md` | One chapter of the owner's life story, once it outgrows the Biography overview | `Profile/Biography/<Title>.md`, once Biography is a folder facet (`Profile/README.md`, How The Facets Are Built) | `reference` |

A facet read as a whole is a flat file, made from `Facet Overview.md`; a facet that holds many separate items is a folder, whose `README.md` is made from `Folder Facet.md`. A new facet of either shape, or a flat facet that grows entries and becomes a folder, is a structural change made only with the owner's yes, and is registered in three places: `FACETS` in `.github/scripts/profile-coverage.py`, so it is scored; for a folder, `PROFILE_COLLECTIONS` in `.github/scripts/vault.py`, so `update-vault.py` lists its entries; and the facet table in `Profile/README.md`. A new facet, rather than a flat facet that becomes a folder, also changes every count of the facets: the twelve, and the eleven of the stable self, in `Profile/README.md`'s description and tagline; the twelve in `.docs/references/Glossary.md`, `.docs/introduction/Setting-Up-A-Vault.md` and `.github/scripts/profile-coverage.py`; and the count `.github/scripts/test_profile_coverage.py` checks, which CI runs.

---

## ✍️ How A Copy Is Made

- **Only with a yes.** `Profile/` is read-only unless the owner asks for a change or confirms one, so a new entry is proposed first (`Profile/README.md`, Rules).
- **One file at a time.** A template is copied, never moved or edited in place, and this folder is never copied whole.
- **By the note at its top.** Each scaffold opens with a comment that begins `On copying:`: where the copy goes, what its type becomes, what to replace, and what the Profile's rules ask of it. The note is deleted from the copy.
- **Every placeholder is replaced.** The copy gets its real `title`, the same text as its H1, its real `description`, and its `type`, never `template`, which `lint-notes.py` refuses outside a `.template/` folder. Its keywords become its own: lowercase, at most eight, each distinct, none already in the title, with `template` dropped (`.docs/technical/vault/Keywords.md`). Each `[bracketed]` prompt gets the owner's own words or is deleted.
- **Facts, not guesses.** Only what the owner said, or what was observed directly, is written. A stated fact carries no marker; an inference ends its line with the provenance marker, `<!-- observed YYYY-MM-DD · confidence: low|medium|high · unconfirmed -->`, and stays `unconfirmed` until the owner approves it (`Profile/README.md`, Provenance And Freshness). Each scaffold's note says this in words, since one comment cannot hold another.
- **Sensitive entries stay terse.** A belief and a health condition each get a file of their own, kept to the minimum needed to be considerate and surfaced only when the task needs it (`Profile/README.md`, Sensitivity); health is kept for awareness, never diagnosis (`Profile/Health/README.md`).
- **A folder facet's overview is its `README.md`.** It is never named after its folder: a note named after its folder repeats the folder's README, and `lint-notes.py` flags it.
- **The lists draw themselves.** After an entry is written, `python3 .github/scripts/update-vault.py` lists it in its facet's README.
- **No wikilinks.** An entry names other files by plain path, a scaffold neither carries nor receives a wikilink, and the catalog leaves this folder out.

---

<div align="center">

**One scaffold, one copy, one confirmed entry.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
