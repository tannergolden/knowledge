---
title: "Events"
description: "The atomic grain of context memory: discrete, dated events and experiences worth remembering on their own, distinct from session context, decisions, and future dates."
status: "active"
tags: ["memory", "information", "timeless"]
aliases: []
keywords: ["events", "atomic episode", "what happened", "dated experience", "milestone moment", "occurrence", "context detail"]
created: 2026-06-18
updated: 2026-10-19
type: "information"
folder: "memory"
layer: 2
policy: false
author: "Tanner Golden"
path: "BRAIN/Memory/Events/Events.md"
id: "me-events"
---

# 📌 Events

The atomic grain of the record of what happened: discrete, dated happenings worth remembering precisely on their own - "got the job offer," "moved to Austin," "first met Dana," "closed the house." Where session context (`Memory/Context/`) captures a whole session's gist, an event captures one occurrence exactly, so a specific moment can be recalled without depending on which session it was mentioned in.

## What earns an event

A specific, dated occurrence with continuity value: a milestone, a turning point, a first or a last. One file per event, named `YYYY-MM-DD-slug.md` so events sort chronologically. Keep them atomic - one happening per file.

## What lives here vs. nearby

- A discrete dated happening -> here.
- A whole session's running state -> a session summary in `Memory/Context/`.
- A choice and the reasoning behind it -> `Memory/Decisions/`.
- A future date, deadline, or recurring event -> `Memory/Dates.md`.
- A durable fact about a person, organization, or place -> `Memory/Entities/`.
- A pattern distilled across several events -> `Memory/Insights/`.

## Each event carries

- **What happened** - the occurrence, stated factually.
- **When** - `As of:` the event date, `Recorded:` when it was logged (bitemporal).
- **Importance** - 1 to 5, set at capture; it governs how long the event stays hot in recall.
- **Who and what** - plain-path `Related:` links to the People, Organizations, and Places involved.
- **Why it matters** - the continuity significance for future sessions.

## Creating and keeping

Copy `Memory/.template/Event.md` to this folder and follow its instantiation note; `update-vault.py` lists it here. Events are importance-weighted in recall (recency + importance + relevance, see `Memory/Memory.md`): a high-importance event stays a retrieval candidate for the life of the BRAIN and never ages out of reach. A superseded event is marked, not rewritten (Constitution 3.1).

## Entries

<!-- brain:collection-entries (drawn by .github/scripts/update-vault.py - do not edit by hand) -->
_No events recorded yet._
<!-- /brain:collection-entries -->
