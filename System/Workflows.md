<!--
title: "System Workflows"
description: "The map of the vault's recurring workflows: the strategy, capture and consolidation loops, and where every other recurring procedure is defined."
type: "guide"
keywords: ["procedures", "strategy loop", "capture loop", "consolidation loop", "recurring behaviors", "operating procedures", "workflow map"]
-->

# 🔄 System Workflows

This document is the BRAIN's complete workflow map. It plays two roles: it **owns** (defines in full) the strategy, capture, and consolidation loops that have no other home, and it **indexes** every other recurring procedure with a pointer to its canonical definition and how it runs. Procedures defined elsewhere are not re-specified here (the root `README.md`, Conventions: one home for each thing); this file stays the one place to see the whole operating-procedure map. For the situation-to-script table, see the root `README.md`, Commands.

## The Complete Workflow Map

Workflows marked *owned here* are specified in full lower in this file; all others link to their canonical home.

### Session lifecycle

| Workflow | When it runs | Canonical home · how it runs |
|----------|--------------|--------------------------|
| Session startup / initialization | Start of every session | The root `README.md`, How A Session Goes · `session.py start` |
| Context handoff & session summary | Task boundaries, host context warnings, session end | `Memory/README.md` · write it from `Memory/.template/Session Summary.md` |
| Tiered-memory cascade | After saving a summary | `Memory/README.md`, Rules · `update-vault.py` |

### Capture & filing

| Workflow | When it runs | Canonical home · how it runs |
|----------|--------------|--------------------------|
| Inbox sorting protocol | Sortable files present in `Inbox/` | `Inbox/README.md` · the session-start card lists them |
| Library filing + freshness gate | Filing reference material into `Library/` | `Inbox/README.md` (enrichment) + `Library/README.md` (Rules) |
| Quick memory capture | A fact or event worth logging | `Memory/README.md` · a new entry at the top of `Memory/Log.md`'s Log Entries |

### Memory upkeep

| Workflow | When it runs | Canonical home · how it runs |
|----------|--------------|--------------------------|
| Memory consolidation loop | ~10+ unpromoted Log entries / monthly / on request | *owned here* |
| Log → permanent promotion | A Log entry qualifies for People/Decisions/Dates (facts about the owner go to Profile) | *owned here* (consolidation) + `Memory/README.md`, Writing An Entry |
| Memory entry growth (lifetime) | A permanent Memory entry file grows too long to load whole | `Memory/README.md` "Growth Protocol" · the entry keeps its present, and its history moves into `Memory/Events/` |

### Integrity & maintenance

| Workflow | When it runs | Canonical home · how it runs |
|----------|--------------|--------------------------|
| Keeping a state | Before a risky or wide edit | The root `README.md`, Gotchas · a git commit |
| Integrity pass | After any major session or change set, and before a commit | `System/README.md` · `check-vault.py` (notes, links, personal data, ignored files, generated parts) |
| Change record | Every change | [Conventional Commits](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Conventional-Commits.md) · the release notes are the history |
| Deletion | Removing anything (after the owner's approval) | The root `README.md`, Ask First · `git rm`, recoverable from history |
| Backlink-safe rename | Renaming any file | `.docs/technical/vault/Link-Topology.md` · update every wikilink to it, then `check-links.py` |

### Creation & scaffolding

| Workflow | When it runs | Canonical home · how it runs |
|----------|--------------|--------------------------|
| New project | A personal initiative begins (ask first) | `Projects/README.md` · copy `Projects/.template/` |
| New venture | A company the owner owns or operates | `Ventures/README.md` · copy `Ventures/.template/` |
| Profile interview | Filling or deepening the `Profile/` files | `Profile/README.md` · a profile interview, such as the one the `human-resources` skill runs |

### Reporting

| Workflow | When it runs | Canonical home · how it runs |
|----------|--------------|--------------------------|
| BRAIN-work report fix prompt | Ending any report about developing the BRAIN | `System/README.md`, Reports On The Vault |

When a new workflow is added anywhere in the BRAIN, add a row here so this map stays complete.

---

## Loops Defined in Full Here

The procedure the map marks *owned here* is specified below.

## The Memory Consolidation Loop

Memory quality decays through accumulation, not deletion: duplicates pile up, facts go stale, and contradictions creep in between files. This loop is the BRAIN's equivalent of "sleep-time" memory maintenance (the pattern used by Letta/MemGPT and Mem0-style systems, adapted to plain markdown).

**When to run:** Periodically, at natural low-stakes moments. Triggers: `Memory/Log.md` accumulating more than ~10 unpromoted entries, a month since the last consolidation, or the owner asking to "clean up memory."

**The pass, across the memory layer (`Log.md`, the People and Decisions collections, and `Dates.md`):**

1. **Classify each entry** against the rest of the memory layer using four operations. Write each change in the destination's own format (the collection's note shows it); `update-vault.py` redraws the collection's index, so never hand-edit an index block. If an entry is really about *who the owner is* (a trait, fact, belief, preference, goal), it does not belong in Memory at all: propose it into `Profile/` (`Profile/README.md`, Rules):
   - **ADD** - genuinely new; promote Log entries into their collection (a new entry file for a person, decision, event or insight, a row in `Dates.md`).
   - **UPDATE** - complements or refines an existing entry; merge into it.
   - **SUPERSEDE** - contradicts an existing entry; the old entry is not silently rewritten. Mark it superseded (its Status line becomes Superseded, with a pointer to the new entry), then record the new version. Preserving the dated old version is deliberate: it lets any future session see *when* a fact changed instead of inheriting a silent edit.
   - **NOOP** - duplicate or trivial; flag per retention policy.
2. **Flag, never delete.** Removals surface to the owner for confirmation (the root `README.md`, Ask First); an approved removal is a `git rm`, so it stays recoverable from history. No automated deletion exists anywhere in the system: even Recent-tier cascade overflow is archived to `Memory/Context/Archive/`, not deleted (`Memory/README.md`).
3. **Check cross-file consistency.** A superseded decision may invalidate a person's status in `People/` or a routing note in `Log.md`; propagate the change rather than leaving siblings stale.
4. **Finish mechanically:** run `update-vault.py`, then `check-vault.py`, then commit.
