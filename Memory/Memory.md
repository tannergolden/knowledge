---
title: "Memory - Folder Information"
description: "The continuity layer, organized by cognitive memory type: working (Log), context (the session timeline), semantic (Entities), reflective (Decisions and Insights), and prospective (Dates). It records what happened and the user's external world, with capture-time importance, recency-importance-relevance retrieval, reflection, and bitemporal provenance. Who the user IS lives in Profile, never here."
status: "active"
tags: ["memory", "information", "timeless"]
aliases: []
keywords: ["continuity layer", "memory types", "context semantic", "importance salience", "recency relevance retrieval", "reflection cadence", "bitemporal provenance", "supersede not rewrite"]
created: 2026-06-18
updated: 2026-06-18
type: "information"
folder: "memory"
layer: 1
policy: false
version: "01.00.00"
author: "Tanner Golden"
path: "BRAIN/Memory/Memory.md"
id: "me-memory"
---

# 🧠 Memory/

## Purpose

`Memory/` is the continuity layer: the AI's persistent memory of what has happened, who and what is in the user's world, what was decided, and what is due. Without it every session starts cold; with it, context accumulates. **Read [[Memory/Log|Log.md]] at the start of every session.**

It is organized the way long-term memory is organized in both cognitive science and modern agent-memory systems - **by memory type** - rather than by file kind. Who the user *is* lives in `Profile/`, never here (see Boundaries).

## The memory-type architecture

| Memory type | Where | Holds | How it ages |
|-------------|-------|-------|-------------|
| **Working** | [[Memory/Log\|Log.md]] | the capture stream and open loops; the first place things land | promotes to a collection or ages out |
| **Context** | [[Memory/Context/Context\|Context/]], [[Memory/Events/Events\|Events/]] | what happened: session context (Context, tiered Current to Recent to Archive) and atomic dated events (Events) | summaries cascade; events persist; nothing is deleted |
| **Semantic** | [[Memory/Entities/Entities\|Entities/]] | durable facts about the people, organizations, and places in the user's personal orbit | persists; superseded when a fact changes |
| **Reflective** | [[Memory/Decisions/Decisions\|Decisions/]], [[Memory/Insights/Insights\|Insights/]] | choices and their outcomes; higher-order patterns distilled about the user's external world | persists; superseded |
| **Prospective** | [[Memory/Dates\|Dates.md]] | future-facing: dates, deadlines, anniversaries, intentions | kept; a person's dates also live in their entry |

The fourth classical type, **procedural** (skills, habits, how the user likes things done), is deliberately absent: general how-to is `Library/`, and the user's own habits and preferences are `Profile/`. This layer holds events and the external world, not the self and not the world's knowledge.

## Boundaries

- **Identity (Constitution 2.7, 4.2).** Who the user *is* - traits, values, habits, preferences, goals, beliefs, biography - is the stable self and lives in `Profile/`, never here. Memory records the *events that evidence* a trait; Profile states the trait once and cites the event. When the AI learns something about the user themselves, it proposes an `Profile/` edit, it does not store it here.
- **Library (Article VI).** General and world knowledge is reference material for `Library/`.
- **Ventures.** Business context and business contacts live in `Ventures/`; the entities here are the *personal* orbit.
- **Projects.** Project-specific progress lives in `Projects/[project]/`.

## Design: index + entry

Memory that grows without bound is split into **collections**: a lean, always-scannable index doc (the folder's namesake file) plus one entry file per item, loaded only when relevant. This is parent-document retrieval - small to find, large to read - so a whole-collection scan never drags in years of irrelevant history. The per-entry collections are People, Organizations, Places, Decisions, and Insights; the streaming or small files (`Log.md`, `Dates.md`) stay flat.

## Operations

The five operations of this memory, each with the rule that governs it:

- **Capture.** Every observation worth keeping enters `Log.md` through `remember`. Rate its **importance 1 to 5 at write time** (1 routine, 3 notable, 5 pivotal), recorded as an `Importance: N` line in the entry body. Importance is judged once, at capture, the way a person tags an experience by how much it mattered; it feeds both retrieval ranking and the reflection trigger.
- **Consolidate.** Promote qualified Log entries into a collection; merge entries that describe the same entity or event; collapse near-duplicate Log lines into the canonical entry; relocate (never compress away) summaries as a tier overflows. A summary always links to its sources and never replaces the raw record.
- **Retrieve.** Rank by **recency + importance + relevance** (see below); auto-load the newest context summaries each session; reach everything older on demand by `search`.
- **Reflect.** On the periodic consolidation pass, and whenever the summed importance of memories captured since the last reflection crosses about 25, pose a few questions over recent context and entity memory and write the `Insights/` that answer them, each citing its sources. Reflection about the user themselves becomes an `Profile/` proposal, never an Insight.
- **Forget.** Nothing is ever deleted (Constitution 3.1). Decay is a ranking term, not erasure; a fact that changes is superseded, not overwritten.

## Salience and retrieval

Retrieval ranks candidates by the sum of three signals, each normalized to a 0-to-1 scale and weighted equally by default:

```
score = recency + importance + relevance
```

- **recency** - decays exponentially with time since the memory was last touched, so fresh context outranks old.
- **importance** - the 1-to-5 score captured at write time, normalized.
- **relevance** - keyword plus semantic match to the active query or context.

The newest, most important, most on-point memories surface first; superseded or deprecated entries remain searchable but sort last. The newest `Context/Current/` summaries load automatically at the start of every session, up to a small token budget; everything older is reached on demand, where `search` applies the same scoring. An entry may also carry an explicit `Salience:` note when its importance is not obvious from age alone.

## Provenance and supersession

Memory records *when a fact was true* and *when it was learned* (bitemporal provenance), kept in the entry body so no brain-wide frontmatter field is added:

```
As of: 2026-06        # when this became true in the world (valid-time)
Recorded: 2026-06-18  # when the BRAIN learned it (transaction-time)
```

When a fact changes, **supersede, do not silently rewrite**: mark the old entry (`memory supersede ...` sets a Decision's Status to `Superseded`; or set the file `status: deprecated`), add a plain-path `Superseded-by:` pointer, and close the old `As of`. The old record stays - demoted in retrieval, never deleted. A memory that preserves *when* facts changed cannot quietly contradict itself; one that rewrites in place can.

## Engine-owned writes

The AI supplies content and judgment; it never hand-edits an index table. Writes go through the engine: `remember "Title: detail"` (and `remember "..." --loop` for an open thread, `remember close "..."`) for the Log; `memory add person|organization|place|decision|insight "Name"` to scaffold an entry from its template and register it in the collection index; `memory add date <recurring|onetime|milestone> "When" "Event"`; `memory add event "When" "What"` to log a discrete dated event; `memory supersede ...`; `memory cascade` to enforce the context tier caps; `memory rm ...` to soft-remove an entry to `.trash/`.

## Session summaries

When a session nears its context limit, write one context summary to `Context/Current/`, named `YYYYMMDD-HHMMSS.md` (pure timestamp), then run `memory cascade`. Write it as a **delta update**, separating:

- **Established foundations** - prior state still valid.
- **Active changes** - what this session modified, added, or decided.
- **Overrides** - with explicit "this supersedes any earlier statement about X" language, because a model otherwise fails to prefer the newer of two contradictory statements unless the newer one declares itself authoritative.

Capture for recall first, then prune: compaction loss is permanent, so keep verbatim any load-bearing detail rather than paraphrasing it. The exact section list and the summary frontmatter live in `.template/Session Summary.md`.

## Two rules that keep memory trustworthy

- **Supersede, don't silently rewrite** (above). Editing a record in place lets stale state win; superseding keeps the timeline honest.
- **Check memory before accepting premises.** When a request embeds a factual assumption, verify it here first; if Memory disagrees, surface the conflict ("Memory says X as of [date]; you said Y - which is current?") rather than silently picking a side. A memory-equipped model accepts outdated premises more often than it retrieves wrongly, so this check is the main safeguard.

## Cross-referencing

Entries cross-reference with a plain-path `Related:` field (content files carry no wikilinks, Constitution 3.7):

```
Related: Memory/Decisions/2026-05-switched-to-llc.md
Related: Memory/Entities/People/Jane Doe.md
```

## What belongs here vs. elsewhere

| Content | Belongs in |
|---------|-----------|
| A person, organization, or place in the user's personal orbit | `Memory/Entities/...` |
| A decision the user made | `Memory/Decisions/` |
| A derived pattern about the user's external world | `Memory/Insights/` |
| A trait, habit, value, preference, or goal of the user | `Profile/` (propose via 4.2), never Memory |
| Recent notes, events, open threads | `Memory/Log.md` |
| Future dates, deadlines, anniversaries | `Memory/Dates.md` |
| Cross-session continuity (a whole session) | `Memory/Context/` (a session summary) |
| A discrete dated event or experience | `Memory/Events/` |
| General or world knowledge | `Library/` |
| Business context or business contacts | `Ventures/` |
| Project progress | `Projects/[project]/` |
