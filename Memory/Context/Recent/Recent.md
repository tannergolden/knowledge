---
title: "Recent Context"
description: "The context mid tier - recent session summaries one step back from the entry tier, reached on request and ranked by recency, importance, and relevance."
status: "active"
tags: ["memory", "information", "timeless"]
aliases: []
keywords: ["recent", "mid tier", "on request", "lookback", "summaries", "importance aware", "overflow"]
created: 2026-06-18
updated: 2026-06-18
type: "information"
folder: "memory"
layer: 3
policy: false
author: "Tanner Golden"
path: "BRAIN/Memory/Context/Recent/Recent.md"
id: "me-recent"
---

# 🗂️ Recent Context

The mid tier of context memory: recent history one step back from the entry tier. It stays available without inflating every session's base context, so it is reached on request rather than auto-loaded.

## Cap and cascade

This tier holds a larger ceiling than Current (default a session-or-two's worth, about 6 summaries). When it overflows, the oldest relocates to `Memory/Context/Archive/<year>/` via `brain.command memory cascade`. Nothing is deleted (Constitution 3.1).

## Recall here is scored, not just listed

When the AI looks back beyond the auto-load set, it does not read this tier top to bottom. It ranks the summaries by **recency + importance + relevance** to the current need (the model in `Memory/Memory.md`), so a more relevant or more important older summary outranks a fresher trivial one. Tier membership sets what is cheap to reach; the score sets what actually surfaces.

## Summaries in this tier

<!-- brain:tier-summaries (auto-maintained by brain.command - do not edit by hand) -->
_No summaries in this tier right now._
<!-- /brain:tier-summaries -->

## Notes

- Files keep their `YYYYMMDD-HHMMSS.md` names so they remain sortable by time.
- A high-importance summary remains a retrieval candidate even after it cascades to Archive.
