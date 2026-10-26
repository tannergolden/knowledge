<!--
title: "System Workflows"
description: "Formalized workflows for the AI to follow, defining strategy loops, automated captures, and recurring behaviors."
type: "guide"
keywords: ["procedures", "strategy loop", "capture loop", "consolidation loop", "recurring behaviors", "operating procedures", "workflow map"]
-->

# 🔄 System Workflows

This document is the BRAIN's complete workflow map. It plays two roles: it **owns** (defines in full) the strategy, capture, and consolidation loops that have no other home, and it **indexes** every other recurring procedure with a pointer to its canonical definition and how it runs. Procedures defined elsewhere are not re-specified here (`AGENTS.md`, Conventions: one home for each thing); this file stays the one place to see the whole operating-procedure map. For the situation-to-script table, see `AGENTS.md`, Commands.

## The Complete Workflow Map

Workflows marked *owned here* are specified in full lower in this file; all others link to their canonical home.

### Session lifecycle

| Workflow | When it runs | Canonical home · how it runs |
|----------|--------------|--------------------------|
| Session startup / initialization | Start of every session | `AGENTS.md`, Start here · `session.py start` |
| Context handoff & session summary | Task boundaries, host context warnings, session end | `Memory/Memory.md` · write it from `Memory/.template/Session Summary.md` |
| Tiered-memory cascade | After saving a summary | `Memory/Memory.md`, Rules · `update-vault.py` |

### Capture & filing

| Workflow | When it runs | Canonical home · how it runs |
|----------|--------------|--------------------------|
| Inbox sorting protocol | Sortable files present in `Inbox/` | `Inbox/Inbox.md` · the session-start card lists them |
| Library filing + freshness gate | Filing reference material into `Library/` | `Inbox/Inbox.md` (enrichment) + `Library/Library.md` (Rules) |
| Quick memory capture | A fact or event worth logging | `Memory/Memory.md` · a new entry at the top of `Memory/Log.md`'s Log Entries |

### Memory upkeep

| Workflow | When it runs | Canonical home · how it runs |
|----------|--------------|--------------------------|
| Memory consolidation loop | ~10+ unpromoted Log entries / monthly / on request | *owned here* |
| Log → permanent promotion | A Log entry qualifies for People/Decisions/Dates (user-facts go to Profile) | *owned here* (consolidation) + `Memory/Memory.md` retention tables |
| Memory entry growth (lifetime) | A permanent Memory entry file grows too long to load whole | `Memory/Memory.md` "Growth Protocol" · the entry keeps its present, and its history moves into `Memory/Events/` |

### Integrity & maintenance

| Workflow | When it runs | Canonical home · how it runs |
|----------|--------------|--------------------------|
| Keeping a state | Before a risky or wide edit | `AGENTS.md`, Gotchas · a git commit |
| Integrity pass | After any major session or change set, and before a commit | `System/System.md` · `check-vault.py` (notes, links, skills, agents, personal data, generated parts) |
| Change record | Every change | [Conventional Commits](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Conventional-Commits.md) · the release notes are the history |
| Deletion | Removing anything (after user approval) | `AGENTS.md`, Ask first · `git rm`, recoverable from history |
| Backlink-safe rename | Renaming any file | `.docs/technical/vault/Link-Topology.md` · update every wikilink to it, then `check-links.py` |

### Creation & scaffolding

| Workflow | When it runs | Canonical home · how it runs |
|----------|--------------|--------------------------|
| New project | A personal initiative begins (ask first) | `Projects/Projects.md` · copy `Projects/.template/` |
| New venture | A company the user owns or operates | `Ventures/Ventures.md` · copy `Ventures/.template/` |
| Identity interview | Filling or deepening the `Profile/` files | `Profile/Profile.md` · the `identify` skill (`/identify`) |

### Skills

| Workflow | When it runs | Canonical home · how it runs |
|----------|--------------|--------------------------|
| Skill development | Build / update / optimize a skill | the universal `develop` skill (`/develop`) |
| Skill packaging | Ship a `.skill` from a source folder | `System/Skills/Skills.md` · `update-vault.py` builds every archive, team included |
| BRAIN-work report fix prompt | Ending any report about developing the BRAIN | `System/System.md`, Reports On The Vault |

When a new workflow is added anywhere in the BRAIN, add a row here so this map stays complete.

---

## Loops Defined in Full Here

The procedure the map marks *owned here* is specified below.

## The Memory Consolidation Loop

Memory quality decays through accumulation, not deletion: duplicates pile up, facts go stale, and contradictions creep in between files. This loop is the BRAIN's equivalent of "sleep-time" memory maintenance (the pattern used by Letta/MemGPT and Mem0-style systems, adapted to plain markdown).

**When to run:** Periodically, at natural low-stakes moments. Triggers: `Memory/Log.md` accumulating more than ~10 unpromoted entries, a month since the last consolidation, or the user asking to "clean up memory."

**The pass, across the memory layer (`Log.md`, the People and Decisions collections, and `Dates.md`):**

1. **Classify each entry** against the rest of the memory layer using four operations. Write each change in the destination's own format (the collection's note shows it); `update-vault.py` redraws the collection's index, so never hand-edit an index block. If an entry is really about *who the user is* (a trait, fact, belief, preference, goal), it does not belong in Memory at all: propose it into `Profile/` (`Profile/Profile.md`, Rules):
   - **ADD** - genuinely new; promote Log entries into their collection (a new entry file for a person, decision, event or insight, a row in `Dates.md`) per the retention tables.
   - **UPDATE** - complements or refines an existing entry; merge into it.
   - **SUPERSEDE** - contradicts an existing entry; the old entry is not silently rewritten. Mark it superseded (its Status line becomes Superseded, with a pointer to the new entry), then record the new version. Preserving the dated old version is deliberate: it lets any future session see *when* a fact changed instead of inheriting a silent edit.
   - **NOOP** - duplicate or trivial; flag per retention policy.
2. **Flag, never delete.** Removals surface to the user for confirmation (`AGENTS.md`, Ask first); an approved removal is a `git rm`, so it stays recoverable from history. No automated deletion exists anywhere in the system: even Recent-tier cascade overflow is archived to `Memory/Context/Archive/`, not deleted (`Memory/Memory.md`).
3. **Check cross-file consistency.** A superseded decision may invalidate a person's status in `People/` or a routing note in `Log.md`; propagate the change rather than leaving siblings stale.
4. **Finish mechanically:** run `update-vault.py`, then `check-vault.py`, then commit.
