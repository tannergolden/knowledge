<!--
title: "Recent Context"
description: "The context mid tier - recent session summaries one step back from the entry tier, reached on request and ranked by recency, importance, and relevance."
type: "index"
keywords: ["mid tier", "on request", "lookback", "summaries", "importance aware", "overflow"]
-->

# 🗂️ Recent Context

The mid tier of context memory: recent history one step back from the entry tier. It stays available without inflating what every session reads at its start, so it is reached on request rather than read at start.

## Cap and cascade

This tier holds at most 6 summaries, a larger lookback than Current's 3. When it overflows, `update-vault.py` moves the oldest to `Memory/Context/Archive/<year>/`, the year read from the start of its name, and lists the summaries currently here. Nothing is deleted (the root `README.md`, Ask First).

## Recall here is scored, not just listed

A look back beyond the two summaries every session reads does not read this tier top to bottom. It ranks the summaries by **recency + importance + relevance** to the current need (`Memory/README.md`, Operations), so a more relevant or more important older summary outranks a fresher trivial one. Tier membership sets what is cheap to reach; the score sets what actually surfaces.

## Summaries in this tier

<!-- brain:tier-summaries (drawn by .github/scripts/update-vault.py - do not edit by hand) -->
_No summaries in this tier right now._
<!-- /brain:tier-summaries -->

## Notes

- Files keep their `YYYYMMDD-HHMMSS.md` names so they remain sortable by time.
- A high-importance summary remains a retrieval candidate even after it cascades to Archive (`Memory/Context/README.md`).
