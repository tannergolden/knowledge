<!--
title: "Collection Index"
description: "Generic scaffold for a per-collection index doc - purpose, retention policy, and a generated entry list."
type: "template"
keywords: ["index template", "entry list", "per-collection scaffold", "registry", "namesake doc", "generated list"]
-->

<!--
INSTANTIATION (when scaffolding a new per-entry collection's index doc):
- Set type to "index", and give the copy its real title and description.
- Keep the emoji H1; replace [Collection] with the collection's name and pick a fitting emoji.
- Fill purpose and retention for the specific collection; never fabricate.
- Leave the Entries block to `.github/scripts/update-vault.py` - the AI never hand-edits it.
-->

# 🗂️ [Collection]

<!-- One or two sentences: what this collection holds and why it exists. -->

## Purpose

<!-- The scope of this collection: what earns an entry here and what does not. -->

## Retention

<!-- How entries age: persist, supersede on change, never delete (`AGENTS.md`, Ask first). -->

## How entries are made

Copy the entry template into this folder and follow its instantiation note; `update-vault.py` lists the entry below. The AI never hand-edits this index.

---

## Entries

<!-- Drawn by update-vault.py. One line per entry. -->

| Name | Notes | Updated |
|------|-------|---------|
|      |       |         |
