<!--
title: '[emoji] [COLLECTION]'
description: '[What this collection records, one file per entry.] Read it before adding or updating [an entry], or to tell [an entry] from [what the nearest folder holds].'
type: 'template'
keywords: ["[what the entries are]", "[another name for them]", "template"]
-->

<!-- On copying: a new per-entry collection is a new folder in Memory/, made only with the owner's yes (the root README.md, Ask First). Save this in it as README.md, never as a note named after the folder. Then:
- Set type to "index". Replace [emoji] and [COLLECTION] in the title and the H1 alike with a fitting emoji and the collection's name, fully capped, and give the copy its real description and keywords: lowercase, at most eight, each distinct, none already in the title, with "template" dropped.
- Replace every [bracketed] placeholder with what has been decided, nothing invented: the one-line description and the tagline under the H1, each section, and the closing phrase, each the collection's own, as the README of Memory/Entities/People/ shows.
- Its entries need a scaffold of their own in Memory/.template/, proposed first like any new file and listed in Memory/.template/README.md.
- The folder is added to COLLECTIONS in .github/scripts/vault.py, so update-vault.py draws the Entries block, which is never edited by hand. The README of the folder above names the new collection.
- Once filed, lint-notes.py checks it.
- Delete this note from the copy.
-->

<div align="center">

# [emoji] [COLLECTION]

<a name="top"></a>

**[One line: what this collection holds, one file per entry.]**

_[A principle of this collection's own, shorter than the line above.]_

</div>

---

## 💡 What This Folder Is For

[What this collection records, and why each item gets a file of its own rather than a line in `Memory/Log.md`.]

---

## ⚖️ What belongs here

- **[What earns an entry.]** [The test an entry passes, such as a relationship that is real or recurring.]
- **[What goes elsewhere.]** [The nearest things that belong in another folder, each named by path.]

---

## 🧾 Each entry

[One file per entry, named `[naming pattern]`, holding each section of its scaffold, in order.]

---

## ✍️ Writing an entry

`Memory/.template/[Scaffold].md` is copied into this folder as `[naming pattern]`, and the note at its top followed. `update-vault.py` lists it below; this index is never edited by hand.

---

## 🕰️ Provenance and superseding

Each entry carries `As of:` and `Recorded:` provenance in its body, and a fact that changes is superseded rather than overwritten (`Memory/README.md`). Cross-references use plain-path `Related:` lines.

---

## 🗂️ Entries

<!-- brain:collection-entries (drawn by .github/scripts/update-vault.py - do not edit by hand) -->
_No entries recorded yet._
<!-- /brain:collection-entries -->

---

<div align="center">

**[A closing phrase of this collection's own.]**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
