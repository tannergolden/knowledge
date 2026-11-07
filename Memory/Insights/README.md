<!--
title: "Insights"
description: "Reflective synthesis of higher-order observations about the owner's outside world, distilled from context and entity memory."
type: "index"
keywords: ["insight", "synthesis", "pattern", "observation", "reflection", "dynamic", "tendency"]
-->

# 💡 Insights

Reflective synthesis: higher-order observations distilled from context and entity memory about the owner's **outside world**. Where context memory records what happened and entities record who and what, Insights record the patterns that emerge across them: recurring situations, relationship dynamics, and the ways things tend to go. This is the reflection operation from agent-memory research, scoped to stay firmly on the Memory side of the Profile boundary.

## What belongs here

> An Insight is **never** about who the OWNER is.

Any observation about the owner's own traits, values, habits, preferences, or goals does **not** belong here. It belongs in `Profile/` and is proposed there (`Profile/README.md`, Rules), never stored as an Insight. Insights are about the world **around** the owner, not the self.

- "Conversations with Dana tend to go better in the morning than late at night." - an Insight (a relationship dynamic in the outside world).
- "The hiring process at mid-size firms in this market drags for months." - an Insight (a pattern in how things go).
- "The owner is impatient with slow processes." - NOT an Insight. That is a claim about the owner and belongs in `Profile/`.
- "The owner values mornings for hard conversations." - NOT an Insight. It is proposed to `Profile/`.

When in doubt, the test is whether the observation describes the owner or the owner's surroundings. If it describes the owner, it is Profile, not Memory.

## Each entry

One file per insight, named `YYYY-MM-slug.md` so insights sort chronologically. Each insight is a single synthesized observation about the outside world, and it carries:

- **Statement**: the observation itself, about the outside world only.
- **Evidence**: plain-path citations to the source memories it was distilled from, so the synthesis is traceable back to the context records and entities that produced it.
- **Confidence**: how strongly it holds, and why.
- **Provenance**: bitemporal, `As of` (when the pattern holds in the world) and `Recorded` (when it was written down).
- **Status**: `Active` or `Superseded`.

Every insight cites the source memories it was derived from, by plain path (`.docs/technical/vault/Link-Topology.md`). An insight with no evidence is not an insight: it is a guess, and does not belong here.

## Writing an entry

Insights are written by reflection, on the periodic consolidation pass and whenever the summed importance of the memories captured since the last reflection crosses about 25 (`Memory/README.md`, Operations). Each pass poses a few questions over recent context and entity memory and writes the insights that answer them, every one citing the memories it was drawn from. `Memory/.template/Insight.md` is copied into this folder for each and its instantiation note followed; `update-vault.py` lists it below, and this index is never edited by hand.

## Provenance and superseding

An insight is superseded when it no longer holds, when the pattern breaks or the dynamic changes: its Status becomes `Superseded`, with a plain-path pointer to the insight that replaces it. Insights are not rewritten in place (`Memory/README.md`).

## Entries

<!-- brain:collection-entries (drawn by .github/scripts/update-vault.py - do not edit by hand) -->
_No insights recorded yet._
<!-- /brain:collection-entries -->
