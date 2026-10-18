---
title: "Data - Folder Information"
description: "Explains the System/Data/ folder: the engine's generated artifacts - error log, activity log, file index, tag-sync state, and session token ledger. Machine-written; never hand-edit."
status: "active"
tags: ["system", "information", "timeless"]
aliases: []
keywords: ["generated artifacts", "error log", "activity log", "file index", "tag sync", "token ledger", "machine-written", "never hand-edit"]
created: 2026-06-12
updated: 2026-06-26
type: "information"
folder: "system"
layer: 2
policy: false
version: "01.00.02"
author: "Tanner Golden"
path: "BRAIN/System/Data/Data.md"
id: "sy-data"
---

# System/Data/

## Purpose

`System/Data/` holds the engine's **generated artifacts** - files `brain.command` writes and rebuilds as it operates. Nothing here is human-authored; nothing here is ever edited by hand. This doc is the folder's one human-readable file and its only graph node: the artifacts are deliberately excluded from the index (the index would churn on its own output), so they are never linted, indexed, or searched - only linked from here.

---

## Contents

| File | Written by | Holds |
|------|-----------|-------|
| [[errors.log]] | Every command and script (shared convention, `System/System.md`) | One line per error: timestamp, script/component, level, message. Reviewed by `health`. |
| [[reports.log]] | Every state-changing command (centralized in `_finish_ledger`, gated by `_is_mutating`) | Activity log, the success-side companion to `errors.log`: one line per mutating command (sync, manifest, cascade, backup, trash, rename, new, changelog, gitkeep, skill package, git init/snapshot). Read-only commands and read-only subcommands stay silent. Auto-trims to the most recent 1000 lines. |
| [[manifest.json]] | `manifest` (incremental; `manifest full` rebuilds) | The scale-ready file index, schema v2: every markdown and binary file with frontmatter, token count, and SHA-256 hash. Powers `load`, `diff`, and `search` filtering. |
| [[catalog.ndjson]] | `save_index` (so any index rebuild: `manifest`, `sync`, `health`, `db build`/`db rollup`) | The lean, committed content roll-up: one JSON record per CONTENT markdown file (path, title, type, folder, layer, tags, keywords, description, status, updated), one record per line for clean diffs. `.template/` scaffolding and binaries are excluded, so it is a clean content database. Written in lockstep with `manifest.json` by `save_index` (idempotent - no rewrite when unchanged), so it can never be committed stale. The portable, dual-readable "database" that ships with the vault; the heavy SQLite FTS5 query index (`db search`) lives outside the iCloud tree and is rebuilt on demand. |
| [[agent-catalog.json]] | `save_index` (so any index rebuild: `manifest`, `sync`, `health`, `db build`/`db rollup`) plus `agents catalog` on demand | The derived roll-up of the federated agent library: one record per agent (spoken name, role key, home, team, description, path) and one per team roster (name, home, lead, members, description), with a `generated` stamp and the BRAIN version like `manifest.json`. Refreshed in lockstep with the manifest by `save_index`, so it can never drift from the live homes. Machine-managed and regenerable; the agent files are the source of truth. |
| [[sync-state.json]] | `sync` | Last-synced Finder tags per file, so `sync` re-tags only what changed. |
| [[session-ledger.json]] | Every command (the `[ctx ~N tokens served]` gauge) | Running ledger of tokens the engine has served into the AI's context this session; `startup` resets it. |
| [[friction.jsonl]] | `friction` (the read-only `friction list` review stays silent) | Append-only operating-failure signal, the success-side `reports.log`'s counterpart: one JSON line per event (`date`, `ts`, `kind`, `what`, `target`, `severity`) when the AI is corrected, misses a step, mis-fires a skill, or hits an ambiguous rule. The BRAIN-wide companion to each skill's `regression-cases.jsonl`; the reflection loop reads it. |

---

## Lifecycles

These artifacts share one folder but fall into three distinct lifecycles - the canonical cache vs logs vs state distinction (XDG Base Directory Spec). They are documented here rather than split into subfolders: at this file count, the clarity is worth more than the folders, and the lifecycle *operations* already exist as commands.

| Lifecycle | Files | Behavior |
|-----------|-------|----------|
| **Cache** - regenerable, safe to wipe | `manifest.json`, `catalog.ndjson`, `agent-catalog.json` | Derived from the notes; a `manifest` / `db build` rebuild reconstructs them with zero data loss. `catalog.ndjson` is a committed warm roll-up that ships with the vault; `manifest.json` is the operational index; `agent-catalog.json` is the agent-library roll-up, rebuilt from the homes on any index refresh. |
| **Logs** - append-only history | `errors.log`, `reports.log`, `friction.jsonl` | Written as events happen; `reports.log` auto-trims to 1000 lines; `logs clear` snapshots then truncates. Never read for behavioral context. |
| **Runtime state** | `session-ledger.json` (ephemeral - reset every `startup`); `sync-state.json` (persists - the incremental-sync cursor) | The engine's working state carried between runs. |

Backups live separately in `System/.backups/` (recovery artifacts, hidden from the graph), not here.

---

## Rules

- **Never edit by hand.** Each file is rebuilt by its owning command; manual edits are overwritten or, worse, poison the index (`Constitution.md` Article 1.2 favors accuracy - a corrupted manifest lies to every command that reads it).
- **Never read these for behavioral context.** `manifest.json` is for fast file discovery only (`System/System.md`, AI Instructions).
- **Deleting them is safe but pointless** - each regenerates on the next run of its command. They are exempt from the backup protocol for the same reason.
