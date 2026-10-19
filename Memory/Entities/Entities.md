---
title: "Memory / Entities"
description: "Semantic memory: durable facts about the people, organizations, and places in the user's personal world, kept as per-entry collections."
status: "active"
tags: ["memory", "information", "timeless"]
aliases: []
keywords: ["semantic memory", "entities", "people organizations places", "personal orbit", "durable facts", "index and entry", "who and what"]
created: 2026-06-18
updated: 2026-10-19
type: "information"
folder: "memory"
layer: 2
policy: false
author: "Tanner Golden"
path: "BRAIN/Memory/Entities/Entities.md"
id: "me-entities"
---

# 🧩 Memory / Entities /

Semantic memory: the durable, slowly-changing facts about the **people, organizations, and places** in the user's personal world. Where context memory remembers *what happened*, Entities remembers *who and what* the user's life is populated by, so the AI can recognize a name and recall the relationship instead of meeting everyone fresh each session.

## The three sub-collections

Each is a **collection**: a lean index doc (the namesake file) plus one entry file per item, loaded only when relevant.

- [[Memory/Entities/People/People|People]] - the people in the user's personal orbit, one Biography-depth file per person.
- [[Memory/Entities/Organizations/Organizations|Organizations]] - the organizations in the user's personal life that are not their own ventures (gym, clinic, school, club, a company they are a customer of).
- [[Memory/Entities/Places/Places|Places]] - the places of personal significance (home, hometown, frequented or meaningful locations).

## What earns an entry

An entity earns a file when it has a **real relationship** or **recurs**. A name mentioned once in passing stays a line in `Log.md`; it graduates to an entry only when it proves durable. Keep the collections about the people, organizations, and places that actually matter, not every name the user has ever uttered.

## Boundaries

- **Personal orbit only.** These are the user's *personal* relationships. A person or organization that exists only in a business context - a client, a vendor, a coworker known purely through work - lives in `Ventures/`, not here. If someone is both a friend and a business contact, the personal entry lives here and cross-references the venture.
- **Not the user (`Profile/Profile.md`, Rules).** Nothing about who the *user* is - their traits, values, habits, preferences, goals, biography - belongs here; that is the self-schema in `Profile/`. Entities is the user's external world, never the self. When the AI learns something about the user themselves, it proposes an `Profile/` edit, not an entry here.
- **Library.** General knowledge about a public figure or a famous place is reference material for `Library/`; an Entities file is warranted only when the user has a personal relationship to it.

## Provenance and supersession

Facts here change slowly but they do change. Each fact carries bitemporal provenance in the entry body (`As of:` when it became true, `Recorded:` when the BRAIN learned it), and when a fact changes the entry is **superseded, not silently rewritten** (Memory.md). A person who moves keeps their old address as superseded history; the new one becomes current.

## Writing entries

Copy the right template from `Memory/.template/` (Person, Organization or Place) into the collection's folder as `<Name>.md`, and follow its instantiation note: the real `type`, `path`, `id` and dates. `.github/scripts/update-vault.py` then lists it in the collection's index; the AI never hand-edits an index block.
