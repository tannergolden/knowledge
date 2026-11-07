<!--
title: "Profile Templates"
description: "The Profile scaffolds: a facet overview, a generic entry, and the entries of the folder facets (a belief, a goal, a skill, a health condition, a life chapter). Each is copied on its own, never edited in place."
type: "index"
keywords: ["profile scaffolds", "facet overview", "entry templates", "belief", "goal", "skill", "copy to file"]
-->

# 🧩 Profile Templates

The scaffolds the Profile's facets and entries are made from. Each is copied on its own, to make one new note, by the instantiation note at its top (its filing instructions), and is never edited in place. This README explains them and is never copied, and `profile-coverage.py` leaves it out when it reads the scaffolds' lines.

## The Templates

| Template | Makes | Copied to | The copy's type |
| -------- | ----- | --------- | --------------- |
| `Facet Overview.md` | A facet's overview | A flat facet's `Profile/<Facet>.md`, or a folder facet's `Profile/<Facet>/README.md` | `reference` |
| `Entry.md` | A generic entry inside a folder facet | `Profile/<Facet>/<Entry Title>.md` | `reference` |
| `Belief.md` | One held belief, isolated for privacy | `Profile/Values/<Title>.md` | `reference` |
| `Goal.md` | One enduring goal | `Profile/Goals/<Title>.md` | `reference` |
| `Skill.md` | One area of genuine depth | `Profile/Skills/<Title>.md` | `reference` |
| `Health Condition.md` | One health attribute or accessibility need, isolated for privacy | `Profile/Health/<Title>.md` | `reference` |
| `Life Chapter.md` | One chapter of the owner's life story, once it outgrows the Biography overview | `Profile/Biography/<Life Chapter>.md`, once Biography is a folder facet (`Profile/README.md`, How The Facets Are Built) | `reference` |

## How A Copy Is Made

- **Only with a yes.** `Profile/` is read-only unless the owner asks for a change or confirms one, so a new entry is proposed first (`Profile/README.md`, Rules).
- **One file at a time.** A template is copied, never moved or edited in place, and this folder is never copied whole.
- **Every placeholder is replaced.** The copy gets its real `title`, `description` and `type`, never `template`, its keywords lose `template`, and each `[bracketed]` placeholder gets its real value. Only what the owner said, or what was observed directly, is written; an inference carries its provenance marker and stays `unconfirmed` until approved (`Profile/README.md`, Provenance And Freshness).
- **A folder facet's overview is its `README.md`.** It is never named after its folder: a note named after its folder repeats the folder's README, and `lint-notes.py` flags it.
- **The lists draw themselves.** After an entry is written, `python3 .github/scripts/update-vault.py` lists it in its facet's README.
- **No wikilinks.** An entry names other files by plain path, a scaffold neither carries nor receives a wikilink, and the catalog leaves this folder out.
