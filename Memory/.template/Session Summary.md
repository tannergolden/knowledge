<!--
title: "Session Summary"
description: "Delta-update ledger scaffold for filing a single session into context memory."
type: "template"
keywords: ["ledger", "delta", "record", "scaffold", "context"]
-->

# 🧾 Session Summary - [YYYY-MM-DD]

<!--
FILING INSTRUCTIONS (do this when you save the summary):
- Save into Memory/Context/Current/ named YYYYMMDD-HHMMSS.md (timestamp of filing).
- In frontmatter: set type "record", and give the copy its real title and description.
- Give the H1 a fitting emoji for the session and replace [YYYY-MM-DD] with the real date.
- Then run: python3 .github/scripts/update-vault.py
NO wikilinks anywhere in this file (`.docs/technical/vault/Link-Topology.md`). Reference files by plain path.
-->

## 1. Session Metadata

- Date:
- Duration:
- Model:
- Primary topics:

## 2. Current State

The accurate snapshot as of the end of this session. If something here conflicts with an
earlier summary, this entry wins. Separate what stands, what changed, and what is overridden.

### Established Foundations

What was already true and confirmed this session. Stable context carried in, not new.

### Active Changes

What changed this session - new decisions, edits, additions, or shifts in direction.

### Overrides

What this session supersedes. Be explicit: "this supersedes any earlier statement about X."
List each override on its own line so a later reader cannot miss it.

## 3. Critical Decisions Made

Decisions that should bind future sessions, with a one-line rationale for each.

## 4. Unresolved Questions

Open threads, ambiguities, and things deferred for a later session.

## 5. Immediate Next Steps

The concrete actions queued for next time, in priority order.

## 6. Verbatim Preservation

Exact quotes, names, numbers, paths, or wording that must be preserved word-for-word.
Anything that would lose meaning if paraphrased goes here.
