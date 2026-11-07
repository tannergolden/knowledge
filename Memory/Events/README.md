<!--
title: "Events"
description: "The atomic grain of context memory: discrete, dated events and experiences worth remembering on their own, distinct from session context, decisions, and future dates."
type: "index"
keywords: ["atomic episode", "what happened", "dated experience", "milestone moment", "occurrence", "context detail"]
-->

# 📌 Events

The atomic grain of the record of what happened: discrete, dated happenings worth remembering precisely on their own, such as "got the job offer", "moved to Austin", "first met Dana" or "closed the house". Where session context (`Memory/Context/`) captures a whole session's gist, an event captures one occurrence exactly, so a specific moment can be recalled without depending on which session it was mentioned in.

## What belongs here

A specific, dated occurrence with continuity value earns an event: a milestone, a turning point, a first or a last. What lives nearby goes there instead:

- A whole session's running state: a session summary in `Memory/Context/`.
- A choice and the reasoning behind it: `Memory/Decisions/`.
- A future date, deadline, or recurring event: `Memory/Dates.md`.
- A durable fact about a person, organization, or place: `Memory/Entities/`.
- A pattern distilled across several events: `Memory/Insights/`.

## Each entry

One file per event, named `YYYY-MM-DD-slug.md` so events sort chronologically, and atomic: one happening per file. Each carries:

- **What happened**: the occurrence, stated factually.
- **When**: `As of:` the event date, `Recorded:` when it was logged (bitemporal).
- **Importance**: 1 to 5, set at capture; it governs how long the event stays hot in recall.
- **Who and what**: plain-path `Related:` lines to the People, Organizations, and Places involved.
- **Why it matters**: the continuity significance for future sessions.

## Writing an entry

`Memory/.template/Event.md` is copied into this folder and its instantiation note followed. `update-vault.py` lists it below; this index is never edited by hand.

## Provenance and superseding

Events are importance-weighted in recall (recency + importance + relevance, `Memory/README.md`): a high-importance event stays a retrieval candidate for the life of the BRAIN and never ages out of reach. A superseded event is marked, never rewritten or deleted (`Memory/README.md`).

## Entries

<!-- brain:collection-entries (drawn by .github/scripts/update-vault.py - do not edit by hand) -->
_No events recorded yet._
<!-- /brain:collection-entries -->
