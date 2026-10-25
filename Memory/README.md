<!--
title: '🧠 MEMORY'
description: 'The continuity layer: what happened, who is around you, what you decided and what is due.'
type: index
keywords: [continuity, vault]
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🧠 MEMORY

<a name="top"></a>

**What happened, who is around you, what you decided, and what is due.**

_Every session starts where the last one ended._

</div>

---

## 💡 What This Folder Is For

`Memory/` is the AI's lasting memory, organised by kind of memory: `Log.md` for what just
happened and what is still open, `Dates.md` for what is due, `Context/` for session summaries that
age from Current to Recent to Archive, and `Events/`, `Entities/`, `Decisions/` and `Insights/` for
what lasts. Who you are is not here: that is `Profile/`.

---

## 🚀 How To Use It

- **Read the Log** to see what the AI has recorded and what is still open.
- **Let the AI write it.** It adds entries and session summaries as you work, in each folder's
  format, and `update-vault.py` keeps the indexes and the summary tiers current.
- **Nothing is deleted.** A fact that changes is superseded, and old summaries move to
  `Context/Archive/`, searchable for good.

The AI reads this folder's note, [`Memory.md`](Memory.md), before it works here: its
rules come first, then how the folder works.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                      | Purpose                                                                                                                                                                                                                                                                                                                                                                                                        |
| :------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`.template/`](.template/) | The entry scaffolds, one per kind of memory: a person, a decision, an event, an insight, a session summary and more. Copied, never edited in place.                                                                                                                                                                                                                                                            |
| [`Context/`](Context/)     | Session context: the tiered cascade of session summaries (Current to Recent to Archive) that carries what happened across working sessions. The gist grain of context memory; recall is importance-aware.                                                                                                                                                                                                      |
| [`Decisions/`](Decisions/) | Reflective record of significant decisions, one file per decision, with context, alternatives, outcomes, and lessons.                                                                                                                                                                                                                                                                                          |
| [`Entities/`](Entities/)   | Semantic memory: durable facts about the people, organizations, and places in the user's personal world, kept as per-entry collections.                                                                                                                                                                                                                                                                        |
| [`Events/`](Events/)       | The atomic grain of context memory: discrete, dated events and experiences worth remembering on their own, distinct from session context, decisions, and future dates.                                                                                                                                                                                                                                         |
| [`Insights/`](Insights/)   | Reflective synthesis of higher-order observations about the user's external world, distilled from context and entity memory.                                                                                                                                                                                                                                                                                   |
| [`Dates.md`](Dates.md)     | Prospective memory: important dates, deadlines, anniversaries, and recurring events. Future-facing reference, one table row per date.                                                                                                                                                                                                                                                                          |
| [`Log.md`](Log.md)         | Working memory: the chronological capture stream where observations, events, and open threads land first, before they promote to a collection or age out. Newest first; read at session start.                                                                                                                                                                                                                 |
| [`Memory.md`](Memory.md)   | The continuity layer, organized by cognitive memory type: working (Log), context (the session timeline), semantic (Entities), reflective (Decisions and Insights), and prospective (Dates). It records what happened and the user's external world, with capture-time importance, recency-importance-relevance retrieval, reflection, and bitemporal provenance. Who the user IS lives in Profile, never here. |
| [`README.md`](README.md)   | This file.                                                                                                                                                                                                                                                                                                                                                                                                     |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push.

---

<div align="center">

**Recorded once, superseded never erased.**

[↑ Back to Top](#top)

</div>
