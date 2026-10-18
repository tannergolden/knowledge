---
title: "System Workflows"
description: "Formalized workflows for the AI to follow, defining strategy loops, automated captures, and recurring behaviors."
status: "active"
tags: ["system", "guide"]
aliases: []
keywords: ["procedures", "strategy loop", "capture loop", "consolidation loop", "recurring behaviors", "operating procedures", "workflow map"]
created: 2026-06-01
updated: 2026-06-26
type: "guide"
folder: "system"
layer: 1
policy: false
version: "01.00.05"
author: "Tanner Golden"
path: "BRAIN/System/Workflows.md"
id: "sy-workflows"
---

# System Workflows

This document is the BRAIN's complete workflow map. It plays two roles: it **owns** (defines in full) the strategy, capture, and consolidation loops that have no other home, and it **indexes** every other recurring procedure with a pointer to its canonical definition and the engine command that runs it. Procedures defined elsewhere are not re-specified here (Constitution 2.4, no duplicate structures); this file stays the one place to see the whole operating-procedure map. For the command-by-situation quick table, see `Instructions.md` Section 4.4.

## The Complete Workflow Map

Workflows marked *owned here* are specified in full lower in this file; all others link to their canonical home.

### Session lifecycle

| Workflow | When it runs | Canonical home · command |
|----------|--------------|--------------------------|
| Session startup / initialization | Start of every session | `Instructions.md` §9 · `brain.command startup` |
| Context handoff & session summary | Task boundaries, 60k/90k context, session end | `Instructions.md` §13 + `Memory/Memory.md` · `brain.command summary new` |
| Tiered-memory cascade | After saving a summary | `Instructions.md` §13.2 · `brain.command memory cascade` |

### Capture & filing

| Workflow | When it runs | Canonical home · command |
|----------|--------------|--------------------------|
| Inbox sorting protocol | Sortable files present in `Inbox/` | `Instructions.md` §7 + `Inbox/Inbox.md` · `brain.command inbox` |
| Library filing + freshness gate | Filing reference material into `Library/` | `Inbox/Inbox.md` (enrichment) + `Library/Library.md` (Article 6.2) |
| Quick memory capture | A fact or event worth logging | `Memory/Memory.md` · `brain.command remember` |

### Memory upkeep

| Workflow | When it runs | Canonical home · command |
|----------|--------------|--------------------------|
| Memory consolidation loop | ~10+ unpromoted Log entries / monthly / on request | *owned here* · `brain.command consolidate` |
| Log → permanent promotion | A Log entry qualifies for People/Decisions/Dates (user-facts go to Profile) | *owned here* (consolidation) + `Memory/Memory.md` retention tables |
| Memory entry growth (lifetime) | A permanent Memory entry file exceeds the size threshold | `Memory/Memory.md` "Growth Protocol" · `brain.command stale` flags |

### Integrity & maintenance

| Workflow | When it runs | Canonical home · command |
|----------|--------------|--------------------------|
| File backup before edit | Before editing any existing file | `Instructions.md` §10 · `brain.command backup` |
| Tag sync to Finder | After any create / move / tag change | Constitution Article VII + `Instructions.md` §8.4 · `brain.command sync` |
| Health / integrity pass | After any major session or change set | `System/System.md` · `brain.command health` (lint·links·stale·index·gitkeep·errors) |
| Changelog discipline | After a PATCH-or-larger change to a core file | Constitution 3.6 + `System/changelog.md` · `brain.command changelog add` |
| Two-level deletion | Removing anything (after user approval) | Constitution 3.1 · `brain.command trash` → `trash empty` |
| Backlink-safe rename | Renaming any file | Constitution 2.6 / 3.7 · `brain.command rename` |
| Whole-vault snapshot | Before a multi-file maintenance pass | `System/System.md` · `brain.command git snapshot` |
| Activity logging | Automatic on every state-changing command | `System/Data/Data.md` (`reports.log`) |
| Friction capture | The AI is corrected, misses a step, a skill mis-fires, or a rule proves ambiguous | `System/Data/Data.md` (`friction.jsonl`) · `brain.command friction` |

### Creation & scaffolding

| Workflow | When it runs | Canonical home · command |
|----------|--------------|--------------------------|
| New project | A personal initiative begins (ask first) | `Projects/Projects.md` · `brain.command new project` |
| New venture | A company the user owns or operates | `Ventures/Ventures.md` · `brain.command new venture` |
| Identity interview | Filling or deepening the `Profile/` files | `Profile/Profile.md` · the `identify` skill (`/identify`) |

### Skills

| Workflow | When it runs | Canonical home · command |
|----------|--------------|--------------------------|
| Skill development | Build / update / optimize a skill | the `develop` skill (`/develop`) |
| Skill packaging | Ship a `.skill` from a source folder | `System/Skills/Skills.md` · `brain.command skill package` |
| BRAIN-work report fix prompt | Ending any report about developing the BRAIN | Constitution Article 9.4 |

When a new workflow is added anywhere in the BRAIN, add a row here so this map stays complete.

---

## Loops Defined in Full Here

The procedure the map marks *owned here* is specified below.

## The Memory Consolidation Loop

Memory quality decays through accumulation, not deletion: duplicates pile up, facts go stale, and contradictions creep in between files. This loop is the BRAIN's equivalent of "sleep-time" memory maintenance (the pattern used by Letta/MemGPT and Mem0-style systems, adapted to plain markdown).

**When to run:** Periodically, at natural low-stakes moments. Triggers: `Memory/Log.md` accumulating more than ~10 unpromoted entries, a month since the last consolidation, or the user asking to "clean up memory."

**The pass, across the memory layer (`Log.md`, the People and Decisions collections, and `Dates.md`):**

1. **Classify each entry** against the rest of the memory layer using four operations. Every write goes through the engine (`memory add|rm|supersede`), never a hand-edited table. If an entry is really about *who the user is* (a trait, fact, belief, preference, goal), it does not belong in Memory at all: propose it into `Profile/` (Constitution 4.2):
   - **ADD** - genuinely new; promote Log entries with `memory add person|decision|date` per the retention tables.
   - **UPDATE** - complements or refines an existing entry; merge into it.
   - **SUPERSEDE** - contradicts an existing entry; the old entry is not silently rewritten. Mark it with `memory supersede decision` (Status -> Superseded), then record the new version. Preserving the dated old version is deliberate: it lets any future session see *when* a fact changed instead of inheriting a silent edit.
   - **NOOP** - duplicate or trivial; flag per retention policy.
2. **Flag, never delete.** Removals surface to the user for confirmation (Constitution 3.1/3.4); use `memory rm` so removal is recoverable (`.trash/` or a backup). No automated deletion exists anywhere in the system: even Recent-tier cascade overflow is archived to `Memory/Context/Archive/`, not deleted (Instructions 13.2).
3. **Check cross-file consistency.** A superseded decision may invalidate a person's status in `People/` or a routing note in `Log.md`; propagate the change rather than leaving siblings stale.
4. **Finish mechanically:** update `updated` frontmatter on touched files, run `brain.command sync`, then `health`.
