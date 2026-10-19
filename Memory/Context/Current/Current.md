---
title: "Current Context"
description: "The context entry tier - the newest session summaries, the two newest of which load at session start."
status: "active"
tags: ["memory", "information", "timeless"]
aliases: []
keywords: ["current", "entry tier", "latest", "autoload", "session start", "freshest", "summaries"]
created: 2026-06-18
updated: 2026-10-19
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

## The two newest load at session start

The SessionStart hook (`session-hooks.py start`) lists the two newest summaries here for the AI to read, skipping any marked `deprecated` or `archived` (a later summary that overrides one marks it so). Keep each summary short: both are read in full at the start of every session, so a long one crowds out the fresh working context.

## Cap and cascade

This tier holds a small ceiling of the newest summaries (default 3) so the auto-load cost stays bounded. When a newer summary pushes the tier over its ceiling, the oldest overflows into `Memory/Context/Recent/` via `update-vault.py`, which also lists the summaries currently here.

## Summaries in this tier

<!-- brain:tier-summaries (drawn by .github/scripts/update-vault.py - do not edit by hand) -->
_No summaries in this tier right now._
<!-- /brain:tier-summaries -->

## Notes

- Files are named `YYYYMMDD-HHMMSS.md` so they sort newest-first by name.
- Nothing is deleted; overflow relocates to `Memory/Context/Recent/` (`AGENTS.md`, Ask first).
- A high-importance summary stays a retrieval candidate after it cascades out (see `Memory/Context/Context.md`).
- The session-summary format lives in `Memory/Memory.md` and `Memory/.template/Session Summary.md`.
