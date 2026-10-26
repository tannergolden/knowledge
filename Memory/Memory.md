<!--
title: "Memory - Folder Information"
description: "The continuity layer, organized by cognitive memory type: working (Log), context (the session timeline), semantic (Entities), reflective (Decisions and Insights), and prospective (Dates). It records what happened and the user's external world, with capture-time importance, recency-importance-relevance retrieval, reflection, and bitemporal provenance. Who the user IS lives in Profile, never here."
type: "index"
keywords: ["continuity layer", "memory types", "context semantic", "importance salience", "recency relevance retrieval", "reflection cadence", "bitemporal provenance", "supersede not rewrite"]
-->

# 🧠 Memory/

## Rules

- **Only what `Profile/` cannot hold.** `Memory/` records what happened, who is around your user, what they decided and what is due. Who your user is (traits, values, habits, preferences, goals) belongs to `Profile/`: propose it there (`Profile/Profile.md`, Rules), never store it here.
- **Read `Log.md` at the start of every session**, and check a premise against Memory before acting on it.
- **Nothing is deleted.** Supersede a fact that changes rather than overwrite it, and let summaries cascade into the archive. Removing an entry is a confirmed `git rm`.
- **Checkpoint at every task boundary.** After each finished task, update the running session summary, and write one before the context runs short (Session summaries, below).
- **Write each entry in its destination's format**, and never hand-edit a generated block: `update-vault.py` redraws them.
- **No wikilinks in an entry.** Cross-reference with a plain-path `Related:` field.

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

- **Identity (Rules, above).** Who the user *is* - traits, values, habits, preferences, goals, beliefs, biography - is the stable self and lives in `Profile/`, never here. Memory records the *events that evidence* a trait; Profile states the trait once and cites the event. When the AI learns something about the user themselves, it proposes an `Profile/` edit, it does not store it here.
- **Library (`Library/Library.md`, Rules).** General and world knowledge is reference material for `Library/`.
- **Ventures.** Business context and business contacts live in `Ventures/`; the entities here are the *personal* orbit.
- **Projects.** Project-specific progress lives in `Projects/[project]/`.

## Design: index + entry

Memory that grows without bound is split into **collections**: a lean, always-scannable index doc (the folder's namesake file) plus one entry file per item, loaded only when relevant. This is parent-document retrieval - small to find, large to read - so a whole-collection scan never drags in years of irrelevant history. The per-entry collections are People, Organizations, Places, Decisions, and Insights; the streaming or small files (`Log.md`, `Dates.md`) stay flat.

## Growth Protocol

An entry loads whole whenever it is relevant, so it has to stay small enough to read beside the task. When a permanent entry (a person, organization, place, decision or insight) passes about 300 lines, or sessions keep loading it for a small part of it, split it the way the collections are split: the entry stays lean, and what only accumulates moves out. Propose the split first, as a table of what moves where, and wait for a yes.

- **The entry keeps its path and its present.** Its name, every field that describes its subject now, its open threads, its important dates and its provenance stay where they are, so every link to it still holds.
- **Its history becomes events.** Each dated item of its history that stands on its own, such as a shared milestone, a past role or a move, becomes an entry in `Events/`, written from `.template/Event.md`, with a plain-path `Related:` line each way. The entry keeps one `Related:` line per moved event, newest first.
- **Move, never compress.** Text moves word for word, and a superseded fact keeps its supersession marks: compaction loss is permanent.
- **The flat files stay flat.** `Log.md` shrinks by consolidation; `Dates.md`, past the same size, moves its one-time dates that have passed into `Events/`.
- **Finish mechanically:** `lint-notes.py` on every file written, then `update-vault.py` and `check-vault.py`, then commit.

## Operations

The five operations of this memory, each with the rule that governs it:

- **Capture.** Every observation worth keeping enters `Log.md` as a new entry at the top of its Log Entries, in the format `Log.md` shows. Rate its **importance 1 to 5 at write time** (1 routine, 3 significant, 5 pivotal), recorded as an `Importance: N` line in the entry body. Importance is judged once, at capture, the way a person tags an experience by how much it mattered; it feeds both retrieval ranking and the reflection trigger.
- **Consolidate.** Promote qualified Log entries into a collection; merge entries that describe the same entity or event; collapse near-duplicate Log lines into the canonical entry; relocate (never compress away) summaries as a tier overflows. A summary always links to its sources and never replaces the raw record.
- **Retrieve.** Rank by **recency + importance + relevance** (see below); auto-load the newest context summaries each session; reach everything older on demand by searching.
- **Reflect.** On the periodic consolidation pass, and whenever the summed importance of memories captured since the last reflection crosses about 25, pose a few questions over recent context and entity memory and write the `Insights/` that answer them, each citing its sources. Reflection about the user themselves becomes an `Profile/` proposal, never an Insight.
- **Forget.** Nothing is ever deleted (Rules, above). Decay is a ranking term, not erasure; a fact that changes is superseded, not overwritten.

## Salience and retrieval

Retrieval ranks candidates by the sum of three signals, each normalized to a 0-to-1 scale and weighted equally by default:

```txt
score = recency + importance + relevance
```

- **recency** - decays exponentially with time since the memory was last touched, so fresh context outranks old.
- **importance** - the 1-to-5 score captured at write time, normalized.
- **relevance** - keyword plus semantic match to the active query or context.

The newest, most important, most on-point memories surface first; superseded or deprecated entries remain searchable but sort last. The two newest `Context/Current/` summaries load at the start of every session; everything older is reached on demand by searching, weighed by the same three signals. An entry may also carry an explicit `Salience:` note when its importance is not obvious from age alone.

## Provenance and supersession

Memory records *when a fact was true* and *when it was learned* (bitemporal provenance), kept in the entry body so no brain-wide frontmatter field is added:

```txt
As of: 2026-06        # when this became true in the world (valid-time)
Recorded: 2026-06-18  # when the BRAIN learned it (transaction-time)
```

When a fact changes, **supersede, do not silently rewrite**: mark the old entry (set a Decision's `**Status:**` line to `Superseded`, or the file's `status: deprecated`), add a plain-path `Superseded-by:` pointer, and close the old `As of`. The old record stays - demoted in retrieval, never deleted. A memory that preserves *when* facts changed cannot quietly contradict itself; one that rewrites in place can.

## Writing memory

The AI supplies content and judgment and writes each entry itself, in its destination's format: a Log entry at the top of `Log.md`'s Log Entries (with `**Status:** Open` for an open thread, flipped to `**Status:** Resolved (YYYY-MM-DD)` when it closes); an entry file copied from `Memory/.template/` into its collection (People, Organizations, Places, Decisions, Events, Insights) with its instantiation note followed; a row in `Dates.md`. It never hand-edits a generated block: `.github/scripts/update-vault.py` redraws each collection's index, the Open Loops view and the tier lists, and cascades the context tiers. Removing an entry is a confirmed `git rm` that the history keeps (`AGENTS.md`, Ask first).

## Session summaries

When a session nears its context limit, write one context summary to `Context/Current/`, named `YYYYMMDD-HHMMSS.md` (pure timestamp), then run `python3 .github/scripts/update-vault.py` to enforce the tier caps. Write it as a **delta update**, separating:

- **Established foundations** - prior state still valid.
- **Active changes** - what this session modified, added, or decided.
- **Overrides** - with explicit "this supersedes any earlier statement about X" language, because a model otherwise fails to prefer the newer of two contradictory statements unless the newer one declares itself authoritative.

Capture for recall first, then prune: compaction loss is permanent, so keep verbatim any load-bearing detail rather than paraphrasing it. The exact section list and the summary frontmatter live in `.template/Session Summary.md`.

## Two rules that keep memory trustworthy

- **Supersede, don't silently rewrite** (above). Editing a record in place lets stale state win; superseding keeps the timeline honest.
- **Check memory before accepting premises.** When a request embeds a factual assumption, verify it here first; if Memory disagrees, surface the conflict ("Memory says X as of [date]; you said Y - which is current?") rather than silently picking a side. A memory-equipped model accepts outdated premises more often than it retrieves wrongly, so this check is the main safeguard.

## Cross-referencing

Entries cross-reference with a plain-path `Related:` field (content files carry no wikilinks; `.docs/technical/vault/Link-Topology.md`):

```txt
Related: Memory/Decisions/2026-05-switched-to-llc.md
Related: Memory/Entities/People/Jane Doe.md
```

## What belongs here vs. elsewhere

| Content | Belongs in |
|---------|-----------|
| A person, organization, or place in the user's personal orbit | `Memory/Entities/...` |
| A decision the user made | `Memory/Decisions/` |
| A derived pattern about the user's external world | `Memory/Insights/` |
| A trait, habit, value, preference, or goal of the user | `Profile/`, proposed first (`Profile/Profile.md`, Rules), never Memory |
| Recent notes, events, open threads | `Memory/Log.md` |
| Future dates, deadlines, anniversaries | `Memory/Dates.md` |
| Cross-session continuity (a whole session) | `Memory/Context/` (a session summary) |
| A discrete dated event or experience | `Memory/Events/` |
| General or world knowledge | `Library/` |
| Business context or business contacts | `Ventures/` |
| Project progress | `Projects/[project]/` |
