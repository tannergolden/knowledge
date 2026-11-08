<!--
title: '🧩 ENTITIES'
description: 'Semantic memory: durable facts about the people, organizations, and places in the owner''s personal world, kept as per-entry collections. Read it to decide whether a name earns an entry, and in which collection.'
type: 'index'
keywords: ["semantic memory", "people organizations places", "personal orbit", "durable facts", "index and entry", "who and what"]
-->

<div align="center">

# 🧩 ENTITIES

<a name="top"></a>

**The semantic memory of the people, organizations and places in the owner's world.**

_Who and what, recognized instead of met fresh._

</div>

---

## 💡 What This Folder Is For

Semantic memory: the durable, slowly changing facts about the **people, organizations, and places** in the owner's personal world. Where context memory remembers *what happened*, Entities remembers *who and what* the owner's life is populated by, so a name is recognized and the relationship recalled instead of everyone being met fresh each session.

---

## 🗂️ The three collections

Each is a **collection**: a lean index (the folder's `README.md`) plus one entry file per item, loaded only when relevant.

- [[Memory/Entities/People/README|People]]: the people in the owner's personal orbit, one Biography-depth file per person.
- [[Memory/Entities/Organizations/README|Organizations]]: the organizations in the owner's personal life that are not their own ventures (gym, clinic, school, club, a company they are a customer of).
- [[Memory/Entities/Places/README|Places]]: the places of personal significance (home, hometown, frequented or meaningful locations).

---

## ⚖️ What earns an entry

An entity earns a file when it has a **real relationship** or **recurs**. A name mentioned once in passing stays a line in `Memory/Log.md`; it graduates to an entry only when it proves durable. The collections keep the people, organizations, and places that actually matter, not every name the owner has ever mentioned.

---

## 🚧 Boundaries

- **Personal orbit only.** These are the owner's *personal* relationships. A person or organization that exists only in a business context, such as a client, a vendor, or a coworker known purely through work, lives in its venture in `Ventures/`, not here. Someone who is both a friend and a business contact gets the personal entry here, which names the venture by plain path.
- **Not the owner (`Profile/README.md`, Rules).** Nothing about who the owner is (their traits, values, habits, preferences, goals, biography) belongs here: that is the self, in `Profile/`. Something learned about the owner themselves is proposed as a `Profile/` edit, not an entry here.
- **Library.** General knowledge about a public figure or a famous place is reference material for `Library/`; an entry here is warranted only when the owner has a personal relationship to it.

---

## ✍️ Writing and keeping entries

The right template from `Memory/.template/` (Person, Organization or Place) is copied into the collection's folder as `<Name>.md`, and its instantiation note followed: the real `title`, `description` and `type`. `.github/scripts/update-vault.py` then lists it in the collection's README; an index block is never edited by hand.

Facts here change slowly, but they do change. Each fact carries bitemporal provenance in the entry body (`As of:` when it became true, `Recorded:` when the BRAIN learned it), and when a fact changes the entry is **superseded, not silently rewritten** (`Memory/README.md`). A person who moves keeps their old address as superseded history; the new one becomes current.

---

<div align="center">

**Known by name, remembered by relationship.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
