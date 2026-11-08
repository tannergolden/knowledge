<!--
title: '[emoji] [COLLECTION]'
description: "Generic scaffold for a per-entry collection's README.md - purpose, retention policy, and a generated entry list."
type: "template"
keywords: ["index template", "entry list", "per-collection scaffold", "registry", "folder readme", "generated list"]
-->

<!--
INSTANTIATION (when scaffolding a new per-entry collection: copy this file into the collection's folder as README.md, never as a note named after the folder):
- Set type to "index", and give the copy its real title and description.
- Keep the page format (.docs/technical/vault/Note-Schema.md): replace [emoji] and [COLLECTION] in the title and the H1 alike with a fitting emoji and the collection's name, fully capped, and write its one-line description, its tagline and its closing phrase, each its own.
- Fill purpose and retention for the specific collection; never fabricate.
- Leave the Entries block to `.github/scripts/update-vault.py`, which draws it once the collection's folder is added to COLLECTIONS in `.github/scripts/vault.py`; it is never edited by hand.
-->

<div align="center">

# [emoji] [COLLECTION]

<a name="top"></a>

**[One line: what this collection holds.]**

_[A principle of this collection's own, shorter than the line above.]_

</div>

---

## 💡 Purpose

<!-- One or two sentences: what this collection holds and why it exists. Then its scope: what earns an entry here and what does not. -->

---

## 🕰️ Retention

<!-- How entries age: persist, supersede on change, never delete (the root `README.md`, Ask First). -->

---

## ✍️ How entries are made

Copy the entry template into this folder and follow its instantiation note; `update-vault.py` lists the entry below. This index is never edited by hand.

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
