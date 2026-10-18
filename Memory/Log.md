---
title: "Memory Log"
description: "Working memory: the chronological capture stream where observations, events, and open threads land first, before they promote to a collection or age out. Engine-owned; read at session start."
status: "active"
tags: ["memory", "log", "startup"]
aliases: ["Working Memory", "Memory Buffer"]
keywords: ["staging buffer", "capture stream", "open loops", "session start", "recent events", "remember", "working memory"]
created: 2026-06-18
updated: 2026-10-18
type: "log"
folder: "memory"
layer: 1
policy: false
author: "Tanner Golden"
path: "BRAIN/Memory/Log.md"
id: "me-log"
---

# 📓 Log

Working memory: the first place new context lands. Observations, events, and open threads are captured here, then either **promote** to a permanent collection (Entities, Decisions, Insights, Dates, or a session summary in Context) or **age out**. Read this file at the start of every session.

**Engine-owned - the AI never hand-edits it.** All writes go through the engine: `remember "Title: detail"` for a note, `remember "..." --loop` for an open thread (auto-listed under Open Loops until `remember close "..."`), and `remember route "<file>" "<dest>" "<why>"` for an Inbox routing rationale. The engine timestamps, places, and keeps the Open Loops view in sync.

**Retention:** staging only. Entries that earn a permanent home are promoted through the engine; the rest age out. Nothing here is authoritative once it has been promoted and superseded.

---

## Log Entries

<!-- brain:log-entries -->

---

## Open Loops

<!-- brain:open-loops (auto-maintained by brain.command from entries marked Status: Open - do not edit by hand) -->
_No open loops._
<!-- /brain:open-loops -->

---

## Sort Routing Notes

Routing rationales staged during Inbox sorting - each row records what moved, where it went, and why, written by the engine via `remember route`.

| Date | File | Destination | Rationale |
|------|------|-------------|-----------|
|      |      |             |           |
