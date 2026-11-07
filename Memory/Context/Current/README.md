<!--
title: "Current Context"
description: "The context entry tier - the newest session summaries, the two newest of which load at session start."
type: "index"
keywords: ["entry tier", "latest", "autoload", "session start", "freshest", "summaries"]
-->

# 📥 Current Context

The entry tier of context memory. Every new session summary is filed here first, as a timestamped `YYYYMMDD-HHMMSS.md` record, and the freshest context is read at the start of the next session.

## The two newest are read at session start

`session.py start` lists the two newest summaries here to be read, skipping any marked `deprecated` or `archived` (a later summary that overrides one marks it so). Each summary is kept short: both are read in full at the start of every session, so a long one crowds out the fresh working context.

## Cap and cascade

This tier holds at most 3 summaries, so what every session reads stays bounded. When a newer summary pushes the tier over its cap, `update-vault.py` moves the oldest into `Memory/Context/Recent/`, and lists the summaries currently here.

## Summaries in this tier

<!-- brain:tier-summaries (drawn by .github/scripts/update-vault.py - do not edit by hand) -->
_No summaries in this tier right now._
<!-- /brain:tier-summaries -->

## Notes

- Files are named `YYYYMMDD-HHMMSS.md` so they sort by time.
- Nothing is deleted; overflow moves to `Memory/Context/Recent/` (the root `README.md`, Ask First).
- A high-importance summary stays a retrieval candidate after it cascades out (`Memory/Context/README.md`).
- The session-summary format lives in `Memory/README.md` and `Memory/.template/Session Summary.md`.
