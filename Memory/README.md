<!--
title: "Memory - Folder Information"
description: "The continuity layer, organized by kind of memory: working (Log), context (session summaries and events), semantic (Entities), reflective (Decisions and Insights), and prospective (Dates). It records what happened and the owner's outside world, with capture-time importance, recency-importance-relevance retrieval, reflection, and bitemporal provenance. Who the owner IS lives in Profile, never here."
type: "index"
keywords: ["continuity layer", "memory types", "context semantic", "importance salience", "recency relevance retrieval", "reflection cadence", "bitemporal provenance", "supersede not rewrite"]
-->

# 🧠 Memory/

What happened, who is around the owner, what they decided and what is due, organized by kind of memory: `Log.md` for what just happened and what is still open, `Dates.md` for what is due, `Context/` for session summaries that age from Current to Recent to Archive, and `Events/`, `Entities/`, `Decisions/` and `Insights/` for what lasts. Who the owner is lives in `Profile/`, never here. Read this README before changing anything in this folder; its rules add to the root `README.md` and never loosen it.

## Rules

- **Only what `Profile/` cannot hold.** `Memory/` records what happened, who is around the owner, what they decided and what is due. Who the owner is (traits, values, habits, preferences, goals) belongs to `Profile/`: it is proposed there (`Profile/README.md`, Rules), never stored here.
- **`Log.md` is read at the start of every session**, and a premise is checked against Memory before it is acted on: when Memory disagrees, the conflict is named rather than either version adopted (the root `README.md`, Gotchas).
- **Nothing is deleted.** A fact that changes is superseded rather than overwritten, and summaries cascade into the archive. Removing an entry is a confirmed `git rm`.
- **A checkpoint at every task boundary.** After each finished task the running session summary is updated, and one is written before the context runs short (Session Summaries, below).
- **Each entry is written in its destination's format**, and a generated block is never edited by hand: `update-vault.py` redraws them.
- **No wikilinks in an entry.** An entry cross-references with a plain-path `Related:` line.

## What Belongs Here, And What Goes Elsewhere

`Memory/` is the continuity layer: the vault's persistent memory of what has happened, who and what is in the owner's world, what was decided, and what is due. Without it every session starts cold; with it, context accumulates.

| Content | Belongs in |
|---------|-----------|
| Recent notes, events, open threads | `Memory/Log.md` |
| Future dates, deadlines, anniversaries | `Memory/Dates.md` |
| Cross-session continuity (a whole session) | `Memory/Context/` (a session summary) |
| A discrete dated event or experience | `Memory/Events/` |
| A person, organization, or place in the owner's personal orbit | `Memory/Entities/...` |
| A decision in the owner's own life | `Memory/Decisions/` |
| A derived pattern about the owner's outside world | `Memory/Insights/` |
| A trait, habit, value, preference, or goal of the owner | `Profile/`, proposed first (`Profile/README.md`, Rules), never Memory |
| General or world knowledge | `Library/` (`Library/README.md`, Rules) |
| Business context, business contacts, and a venture's decisions | `Ventures/` |
| Project progress | `Projects/[project]/` |

Memory records the *events that evidence* a trait; Profile states the trait once and cites the event. The entities here are the owner's *personal* orbit: a contact known only through a venture lives in that venture.

Any work that learns what happened, who is around the owner, what they decided or what is due records it here, by the rules on this page, whichever skill does it: the decisions, dates and commitments the `administration` skill helps the owner make in their own life, the open loops and dates of a complaint or a return (`customer-experience`) or a dispute (`legal-and-compliance`), and the people, events, dates and decisions a profile interview learns.

## The Kinds Of Memory

| Memory type | Where | Holds | How it ages |
|-------------|-------|-------|-------------|
| **Working** | [[Memory/Log\|Log.md]] | the capture stream and open loops; the first place things land | promotes to a collection or ages out |
| **Context** | [[Memory/Context/README\|Context/]], [[Memory/Events/README\|Events/]] | what happened: session summaries (Context, tiered Current to Recent to Archive) and atomic dated events (Events) | summaries cascade; events persist; nothing is deleted |
| **Semantic** | [[Memory/Entities/README\|Entities/]] | durable facts about the people, organizations, and places in the owner's personal orbit | persists; superseded when a fact changes |
| **Reflective** | [[Memory/Decisions/README\|Decisions/]], [[Memory/Insights/README\|Insights/]] | choices and their outcomes; higher-order patterns distilled about the owner's outside world | persists; superseded |
| **Prospective** | [[Memory/Dates\|Dates.md]] | future-facing: dates, deadlines, anniversaries, intentions | kept; a person's dates also live in their entry |

Memory is organized the way long-term memory is organized in both cognitive science and modern AI memory systems, by kind of memory rather than by file kind. The classical **procedural** kind (skills, habits, how the owner likes things done) is deliberately absent: general how-to is `Library/`, and the owner's own habits and preferences are `Profile/`. This layer holds events and the outside world, not the self and not the world's knowledge.

Memory that grows without bound is split into **collections**: a lean, always-scannable index (the folder's `README.md`, whose list `update-vault.py` draws) plus one entry file per item, loaded only when relevant. This is parent-document retrieval, small to find and large to read, so a whole-collection scan never drags in years of irrelevant history. The per-entry collections are People, Organizations, Places, Events, Decisions, and Insights; the streaming or small files (`Log.md`, `Dates.md`) stay flat.

## Writing An Entry

Each entry is written in its destination's format:

- **A Log entry** goes at the top of `Log.md`'s Log Entries, in the format `Log.md` shows, with its importance (Operations, below). An open thread carries `**Status:** Open`, changed to `**Status:** Resolved (YYYY-MM-DD)` when it closes.
- **An entry file** is copied from `Memory/.template/` into its collection, with its instantiation note followed (`Memory/.template/README.md`).
- **A date** is a row in `Dates.md`.

`.github/scripts/update-vault.py` then redraws each collection's index, the Open Loops view and the tier lists, and cascades the context tiers. Removing an entry is a confirmed `git rm` that the history keeps (the root `README.md`, Ask First).

**Cross-referencing.** An entry names another file with a plain-path `Related:` line, since only a folder's README carries wikilinks (`.docs/technical/vault/Link-Topology.md`):

```txt
Related: Memory/Decisions/2026-05-switched-to-llc.md
Related: Memory/Entities/People/Jane Doe.md
```

**Provenance.** Memory records *when a fact was true* and *when it was learned* (bitemporal provenance), in the entry body, so no vault-wide frontmatter field is added:

```txt
As of: 2026-06        # when this became true in the world (valid-time)
Recorded: 2026-06-18  # when the BRAIN learned it (transaction-time)
```

**Supersession.** When a fact changes, it is **superseded, never silently rewritten**: the old entry is marked (a Decision's or an Insight's Status set to `Superseded`, or the file's `status: deprecated`), a plain-path pointer to its replacement is added, and the old `As of` is closed. The old record stays, demoted in retrieval and never deleted. A memory that preserves *when* facts changed cannot quietly contradict itself; one that rewrites in place can.

## Operations

The five operations of this memory, each with the rule that governs it:

- **Capture.** Every observation worth keeping enters `Log.md` as a new entry at the top of its Log Entries. Its **importance is rated 1 to 5 at write time** (1 routine, 3 significant, 5 pivotal), as an `Importance: N` line in the entry body. Importance is judged once, at capture, the way a person tags an experience by how much it mattered; it feeds both retrieval ranking and the reflection trigger.
- **Consolidate.** Qualified Log entries are promoted into a collection, entries that describe the same entity or event are merged, near-duplicate Log lines collapse into the canonical entry, and summaries are relocated, never compressed away, as a tier overflows. A summary always links to its sources and never replaces the raw record. The consolidation pass itself is defined in `System/Workflows.md`.
- **Retrieve.** Candidates are ranked by **recency + importance + relevance** (below); the two newest context summaries are read at the start of every session, and everything older is reached on demand by searching.
- **Reflect.** On the periodic consolidation pass, and whenever the summed importance of the memories captured since the last reflection crosses about 25, a few questions are posed over recent context and entity memory, and the `Insights/` that answer them are written, each citing its sources. Reflection about the owner themselves becomes a `Profile/` proposal, never an Insight.
- **Forget.** Nothing is ever deleted (Rules, above). Decay is a ranking term, not erasure; a fact that changes is superseded, not overwritten.

**Salience and retrieval.** Retrieval ranks candidates by the sum of three signals, each normalized to a 0-to-1 scale and weighted equally by default:

```txt
score = recency + importance + relevance
```

- **recency**: decays exponentially with time since the memory was last touched, so fresh context outranks old.
- **importance**: the 1-to-5 score captured at write time, normalized.
- **relevance**: keyword plus semantic match to the active query or context.

The newest, most important, most on-point memories surface first; superseded or deprecated entries remain searchable but sort last. An entry may also carry an explicit `Salience:` note when its importance is not obvious from age alone.

## Session Summaries

A session summary is written to `Context/Current/`, named `YYYYMMDD-HHMMSS.md` (the time of filing), from `.template/Session Summary.md`: it is updated after each finished task and written before the context runs short, and then `python3 .github/scripts/update-vault.py` enforces the tier caps. It is a **delta update**, separating:

- **Established foundations**: prior state still valid.
- **Active changes**: what this session modified, added, or decided.
- **Overrides**: with explicit "this supersedes any earlier statement about X" language, because a model otherwise fails to prefer the newer of two contradictory statements unless the newer one declares itself authoritative.

What must be recalled is captured first, and only then is the rest pruned: compaction loss is permanent, so a load-bearing detail is kept word for word rather than paraphrased. The exact section list and the summary's frontmatter live in `.template/Session Summary.md`, and a summary that overrides an earlier one marks the earlier one `status: deprecated` (`Context/Current/README.md`).

## Growth Protocol

An entry loads whole whenever it is relevant, so it has to stay small enough to read beside the task. When a permanent entry (a person, organization, place, decision or insight) passes about 300 lines, or sessions keep loading it for a small part of it, it is split the way the collections are split: the entry stays lean, and what only accumulates moves out. The split is proposed first, as a table of what moves where, and made only with a yes.

- **The entry keeps its path and its present.** Its name, every field that describes its subject now, its open threads, its important dates and its provenance stay where they are, so every reference to it still holds.
- **Its history becomes events.** Each dated item of its history that stands on its own, such as a shared milestone, a past role or a move, becomes an entry in `Memory/Events/`, written from `Memory/.template/Event.md`, with a plain-path `Related:` line each way. The entry keeps one `Related:` line per moved event, newest first.
- **Move, never compress.** Text moves word for word, and a superseded fact keeps its supersession marks: compaction loss is permanent.
- **The flat files stay flat.** `Log.md` shrinks by consolidation; `Dates.md`, past the same size, moves its one-time dates that have passed into `Memory/Events/`.
- **Finished mechanically:** `lint-notes.py` on every file written, then `update-vault.py` and `check-vault.py`, then a commit.

## File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                               | Purpose                                                                                                                                                                                                                |
| :---------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`.template/`](.template/README.md) | The entry scaffolds, one per kind of memory: a person, an organization, a place, a decision, an event, an insight, a session summary, and a new collection's README. Each is copied on its own, never edited in place. |
| [`Context/`](Context/README.md)     | Session context: the tiered cascade of session summaries (Current to Recent to Archive) that carries what happened across working sessions. The gist grain of context memory; recall is importance-aware.              |
| [`Decisions/`](Decisions/README.md) | Reflective record of significant decisions, one file per decision, with context, alternatives, outcomes, and lessons.                                                                                                  |
| [`Entities/`](Entities/README.md)   | Semantic memory: durable facts about the people, organizations, and places in the owner's personal world, kept as per-entry collections.                                                                               |
| [`Events/`](Events/README.md)       | The atomic grain of context memory: discrete, dated events and experiences worth remembering on their own, distinct from session context, decisions, and future dates.                                                 |
| [`Insights/`](Insights/README.md)   | Reflective synthesis of higher-order observations about the owner's outside world, distilled from context and entity memory.                                                                                           |
| [`Dates.md`](Dates.md)              | Prospective memory: important dates, deadlines, anniversaries, and recurring events. Future-facing reference, one table row per date.                                                                                  |
| [`Log.md`](Log.md)                  | Working memory: the chronological capture stream where observations, events, and open threads land first, before they promote to a collection or age out. Newest first; read at session start.                         |
| [`README.md`](README.md)            | This file.                                                                                                                                                                                                             |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push to the default branch.
