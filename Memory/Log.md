<!--
title: "Memory Log"
description: "Working memory: the chronological capture stream where observations, events, and open threads land first, before they promote to a collection or age out. Newest first; read at session start."
type: "record"
keywords: ["working memory", "memory buffer", "staging buffer", "capture stream", "open loops", "session start", "recent events", "quick capture"]
-->

# 📓 Log

Working memory: the first place new context lands. Observations, events, and open threads are captured here, then either **promote** to a permanent collection (Entities, Decisions, Insights, Dates, or a session summary in Context) or **age out**. Read this file at the start of every session.

**How to write here.** Add each entry at the top of Log Entries, just below the `brain:log-entries` marker, as `### YYYY-MM-DD - Title`, then the detail and an `Importance: N` line (1 routine to 5 pivotal). An open thread also carries `**Status:** Open`; when it closes, change that line to `**Status:** Resolved (YYYY-MM-DD)`, never delete the entry. Never edit the Open Loops block: `.github/scripts/update-vault.py` redraws it from the entries marked Open. A routing rationale from Inbox sorting is a row in the Sort Routing Notes table.

**Retention:** staging only. Entries that earn a permanent home are promoted into their collection; the rest age out. Nothing here is authoritative once it has been promoted and superseded.

---

## Log Entries

<!-- brain:log-entries -->

---

## Open Loops

<!-- brain:open-loops (drawn by .github/scripts/update-vault.py - do not edit by hand) -->
_No open loops._
<!-- /brain:open-loops -->

---

## Sort Routing Notes

Routing rationales staged during Inbox sorting - each row records what moved, where it went, and why, added as the file is sorted.

| Date | File | Destination | Rationale |
|------|------|-------------|-----------|
|      |      |             |           |
