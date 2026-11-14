<!--
title: '📌 EVENTS'
description: 'The atomic grain of context memory: discrete, dated events and experiences worth remembering on their own, distinct from session context, decisions, and future dates. Read it before recording an event, or to recall a specific moment.'
type: 'index'
keywords: ["atomic episode", "what happened", "dated experience", "milestone moment", "occurrence", "context detail"]
-->

<div align="center">

# 📌 EVENTS

<a name="top"></a>

**The atomic record of what happened: one dated event to each file.**

_One moment, recalled exactly._

</div>

---

## 💡 What This Folder Is For

The atomic grain of the record of what happened: discrete, dated happenings worth remembering precisely on their own, such as "got the job offer", "moved to Austin", "first met Dana" or "closed the house". Where session context (`Memory/Context/`) captures a whole session's gist, an event captures one occurrence exactly, so a specific moment can be recalled without depending on which session it was mentioned in.

---

## ⚖️ What belongs here

A specific, dated occurrence with continuity value earns an event: a milestone, a turning point, a first or a last. What lives nearby goes there instead:

- A whole session's running state: a session summary in `Memory/Context/`.
- A choice and the reasoning behind it: `Memory/Decisions/`.
- A future date, deadline, or recurring event: `Memory/Dates.md`.
- A durable fact about a person, organization, or place: `Memory/Entities/`.
- A pattern distilled across several events: `Memory/Insights/`.

---

## 🧾 Each entry

One file per event, named `YYYY-MM-DD-slug.md` so events sort chronologically (`YYYY-MM-00-slug.md` for one known only to its month), and atomic: one happening per file. Each carries:

- **What happened**: the occurrence, stated factually.
- **When**: `As of:` the event date, `Recorded:` when it was logged (bitemporal).
- **Importance**: 1 to 5, set at capture; it governs how long the event stays hot in recall.
- **Who and what**: plain-path `Related:` lines to the People, Organizations, and Places involved.
- **Why it matters**: the continuity significance for future sessions.
- **Related**: plain-path `Related:` lines to the decisions, session summaries or other events it ties to.

---

## ✍️ Writing an entry

`Memory/.template/Event.md` is copied into this folder as `YYYY-MM-DD-slug.md`, and the note at its top followed. `update-vault.py` lists it below; this index is never edited by hand.

---

## 🕰️ Provenance and superseding

Events are importance-weighted in recall (recency + importance + relevance, `Memory/README.md`): a high-importance event stays a retrieval candidate for the life of the BRAIN and never ages out of reach. A superseded event is marked, never rewritten or deleted: its frontmatter takes `status: deprecated`, and a plain-path `Related:` line points to the entry that replaces it (`Memory/README.md`).

---

## 🗂️ Entries

<!-- brain:collection-entries (drawn by .github/scripts/update-vault.py - do not edit by hand) -->
_No events recorded yet._
<!-- /brain:collection-entries -->

---

<div align="center">

**One happening, one file, one date.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
