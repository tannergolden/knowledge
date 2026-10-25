<!--
title: "Memory / Context"
description: "Session context: the tiered cascade of session summaries (Current to Recent to Archive) that carries what happened across working sessions. The gist grain of context memory; recall is importance-aware."
type: "index"
keywords: ["session context", "session summaries", "tiered cascade", "current recent archive", "importance aware recall", "period digest", "continuity"]
-->

# 🗓️ Memory / Context /

Session context: the running record of what happened across working sessions, kept as session summaries that consolidate when a session nears its context limit and age through a three-tier cascade. This is the **gist grain** of the record of what happened; the **atomic grain** - discrete dated events - lives alongside it in `Memory/Events/`.

## The tiers

- [[Memory/Context/Current/Current|Current]] - the entry tier; the newest summaries, auto-loaded at session start.
- [[Memory/Context/Recent/Recent|Recent]] - recent history, reached on request.
- [[Memory/Context/Archive/Archive|Archive]] - lifetime cold storage by year, search-only, with optional period digests.

## Why the tiers are sized the way they are

The tiers are derived from the cost of recall, not chosen as round numbers. The entry tier is kept small so the session-start auto-load stays cheap (the two newest summaries load at session start); the mid tier is a larger on-request lookback; the archive is unbounded. The per-tier caps are **ceilings on auto-load and working cost** (sensible defaults: a few in Current, a session-or-two's worth in Recent), tunable, not magic constants. `.github/scripts/update-vault.py` enforces them by relocating the oldest outward, never deleting (`AGENTS.md`, Ask first).

## Recall is importance-aware, not pure recency

Tiers order summaries by age, but recall does not stop at age. On-demand retrieval over Recent and Archive ranks by **recency + importance + relevance** (the model in `Memory/Memory.md`), not by folder order. A high-importance summary stays a live retrieval candidate no matter how deep in the archive it has cascaded - importance keeps it **hot**, so a pivotal session surfaces even years later while the routine sinks quietly into cold storage.

## Format

Session summaries use the delta-update ledger in `Memory/.template/Session Summary.md`. Discrete events that are not session context are filed atomically in `Memory/Events/`.
