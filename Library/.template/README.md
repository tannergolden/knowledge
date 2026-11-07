<!--
title: "Library Templates"
description: "The cataloging scaffolds: a reference note, a source catalog card and a division README. Each is copied on its own to make one new note, and never edited in place."
type: "index"
keywords: ["cataloging templates", "reference note", "catalog card", "division readme", "scaffolds", "copy to file"]
-->

# 🧩 Library Templates

The scaffolds the Library's notes are made from. Each is copied on its own, to make one new note, and is never edited in place. This README explains them and is never copied.

## The Templates

| Template | Makes | Copied to | The copy's type |
| -------- | ----- | --------- | --------------- |
| `Reference Note.md` | A synthesized reference note, the common Library holding | Its one class and division: `Library/<Class>/<Division>/<Title>.md` | `reference` |
| `Source Catalog Card.md` | The catalog card of an outside source: a book, paper, article, report or media | Its one class and division, beside any held copy of the work | `reference` |
| `Division.md` | A division folder's README, added under literary warrant once the division needs a finding aid | `Library/<Class>/<Division>/README.md` | `index` |

## How A Copy Is Made

- **One file at a time.** A template is copied, never moved or edited in place, and this folder is never copied whole.
- **Every placeholder is replaced.** The copy gets its real `title`, `description` and `type`, never `template`, which `lint-notes.py` refuses outside a `.template/` folder, and each `[bracketed]` placeholder gets its real value, so no placeholder reaches the catalog.
- **A holding carries one freshness token.** A reference note or a catalog card leads its keywords with `freshness/timeless`, `freshness/enduring` or `freshness/current` (`Library/README.md`, Rules); a division's README carries none.
- **A division's README is always `README.md`.** It is never named after its folder: a note named after its folder repeats the folder's README, and `lint-notes.py` flags it.
- **It is classified first.** The class and division come from the classification rules, boundary rulings and worked examples in `Library/README.md`.
- **No wikilinks.** A scaffold neither carries nor receives a wikilink (`.docs/technical/vault/Link-Topology.md`), and the catalog leaves this folder out.
