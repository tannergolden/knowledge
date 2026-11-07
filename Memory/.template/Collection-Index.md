<!--
title: "Collection Index"
description: "Generic scaffold for a per-entry collection's README.md - purpose, retention policy, and a generated entry list."
type: "template"
keywords: ["index template", "entry list", "per-collection scaffold", "registry", "folder readme", "generated list"]
-->

<!--
INSTANTIATION (when scaffolding a new per-entry collection: copy this file into the collection's folder as README.md, never as a note named after the folder):
- Set type to "index", and give the copy its real title and description.
- Keep the emoji H1; replace [Collection] with the collection's name and pick a fitting emoji.
- Fill purpose and retention for the specific collection; never fabricate.
- Leave the Entries block to `.github/scripts/update-vault.py`, which draws it once the collection's folder is added to COLLECTIONS in `.github/scripts/vault.py`; it is never edited by hand.
-->

# 🗂️ [Collection]

<!-- One or two sentences: what this collection holds and why it exists. -->

## Purpose

<!-- The scope of this collection: what earns an entry here and what does not. -->

## Retention

<!-- How entries age: persist, supersede on change, never delete (the root `README.md`, Ask First). -->

## How entries are made

Copy the entry template into this folder and follow its instantiation note; `update-vault.py` lists the entry below. This index is never edited by hand.

---

## Entries

<!-- brain:collection-entries (drawn by .github/scripts/update-vault.py - do not edit by hand) -->
_No entries recorded yet._
<!-- /brain:collection-entries -->
