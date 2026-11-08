<!--
title: '🗓️ CONTEXT'
description: 'Session context: the tiered cascade of session summaries (Current to Recent to Archive) that carries what happened across working sessions, the gist grain of context memory, with importance-aware recall. Read it to see how a summary ages through the tiers and how an older one is recalled.'
type: 'index'
keywords: ["session context", "session summaries", "tiered cascade", "current recent archive", "importance aware recall", "period digest", "continuity"]
-->

<div align="center">

# 🗓️ CONTEXT

<a name="top"></a>

**The tiered cascade of session summaries that carries context across sessions.**

_Aged by tier, recalled by importance._

</div>

---

## 💡 What This Folder Is For

Session context: the running record of what happened across working sessions, kept as session summaries that age through a three-tier cascade. A summary is updated after each finished task and written before the context runs short (`Memory/README.md`, Session Summaries). This is the **gist grain** of the record of what happened; the **atomic grain**, discrete dated events, lives alongside it in `Memory/Events/`.

---

## 🗂️ The tiers

- [[Memory/Context/Current/README|Current]]: the entry tier, up to 3 summaries, the two newest of which are read at the start of every session.
- [[Memory/Context/Recent/README|Recent]]: recent history, up to 6 summaries, reached on request.
- [[Memory/Context/Archive/README|Archive]]: lifetime cold storage by year, with no cap, reached by search, with optional period digests.

---

## 📐 Why the tiers are sized the way they are

The tiers are sized by the cost of recall, not chosen as round numbers. The entry tier is kept small so the start of every session stays cheap; the mid tier is a larger on-request lookback; the archive is unbounded. The caps are **ceilings on what every session reads and on what is cheap to reach**, tunable rather than magic constants: they are `TIERS` in `.github/scripts/vault.py`, and the tier READMEs state them, so a change to one changes both. `update-vault.py` enforces them by moving the oldest summary down a tier, never deleting one (the root `README.md`, Ask First).

---

## 🎯 Recall is importance-aware, not pure recency

Tiers order summaries by age, but recall does not stop at age. On-demand retrieval over Recent and Archive ranks by **recency + importance + relevance** (`Memory/README.md`, Operations), not by folder order. A high-importance summary stays a live retrieval candidate no matter how deep in the archive it has cascaded: importance keeps it **hot**, so a pivotal session surfaces even years later while the routine sinks quietly into cold storage.

---

## 🧾 Format

Session summaries use the delta-update ledger in `Memory/.template/Session Summary.md`. Discrete events that are not session context are filed atomically in `Memory/Events/`.

---

<div align="center">

**The gist of every session, never lost to age.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
