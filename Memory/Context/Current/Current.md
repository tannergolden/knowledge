---
title: "Current Context"
description: "The context entry tier - the newest session summaries, auto-loaded at session start under a small token budget."
status: "active"
tags: ["memory", "information", "timeless"]
aliases: []
keywords: ["current", "entry tier", "latest", "autoload", "token budget", "freshest", "summaries"]
created: 2026-06-18
updated: 2026-06-18
type: "information"
folder: "memory"
layer: 3
policy: false
author: "Tanner Golden"
path: "BRAIN/Memory/Context/Current/Current.md"
id: "me-current"
---

# 📥 Current Context

The entry tier of context memory. Every new session summary is filed here first as a timestamped `YYYYMMDD-HHMMSS.md` record, and the freshest context loads automatically at the start of the next session.

## Auto-load is token-budgeted, not a fixed count

The newest summary always loads at session start. Additional newer summaries load only while they fit a small session-start token budget, so one long summary does not crowd out the fresh working context. Loading the freshest one or two is the usual result; the point is the budget, not the number.

## Cap and cascade

This tier holds a small ceiling of the newest summaries (default 3) so the auto-load cost stays bounded. When a newer summary pushes the tier over its ceiling, the oldest overflows into `Memory/Context/Recent/` via `brain.command memory cascade`. The engine auto-lists the summaries currently here.

## Summaries in this tier

<!-- brain:tier-summaries (auto-maintained by brain.command - do not edit by hand) -->
_No summaries in this tier right now._
<!-- /brain:tier-summaries -->

## Notes

- Files are named `YYYYMMDD-HHMMSS.md` so they sort newest-first by name.
- Nothing is deleted; overflow relocates to `Memory/Context/Recent/` (Constitution 3.1).
- A high-importance summary stays a retrieval candidate after it cascades out (see `Memory/Context/Context.md`).
- The session-summary format lives in `Memory/Memory.md` and `Memory/.template/Session Summary.md`.
