<!--
title: "Insights"
description: "Reflective synthesis of higher-order observations about the user's external world, distilled from context and entity memory."
type: "index"
keywords: ["insight", "synthesis", "pattern", "observation", "reflection", "dynamic", "tendency"]
-->

# 💡 Insights

Reflective synthesis: higher-order observations distilled from context and entity memory about the user's **external world**. Where context memory records what happened and entities record who and what, Insights record the patterns that emerge across them - recurring situations, relationship dynamics, and the ways things tend to go. This is the reflection operation from agent-memory research, scoped to stay firmly on the Memory side of the Profile boundary.

## The boundary - read this first

> An Insight is **never** about who the USER is.

Any observation about the user's own traits, values, habits, preferences, or goals does **not** belong here. It belongs in Profile/ and must be proposed there (`Profile/Profile.md`, Rules), never stored as an Insight. Insights are about the world **around** the user, not the self.

- "Conversations with Dana tend to go better in the morning than late at night." - Insight (a relationship dynamic in the external world).
- "The hiring process at mid-size firms in this market drags for months." - Insight (a pattern in how things go).
- "The user is impatient with slow processes." - NOT an Insight. That is a claim about the user and belongs in Profile/.
- "The user values mornings for hard conversations." - NOT an Insight. Propose to Profile/.

When in doubt, ask whether the observation describes the user or the user's surroundings. If it describes the user, it is Profile, not Memory.

## What lives here

One file per insight, named `YYYY-MM-slug.md` so insights sort chronologically. Each insight is a single synthesized observation about the external world, and it carries:

- **Statement** - the observation itself, about the external world only.
- **Evidence** - plain-path citations to the source memories it was distilled from, so the synthesis is traceable back to the context records and entities that produced it.
- **Confidence** - how strongly it holds, and why.
- **Provenance** - bitemporal: `As of` (when the pattern holds in the world) and `Recorded` (when it was written down).
- **Status** - `Active` or `Superseded`.

## Sourcing

Every insight cites the source memories it was derived from, by plain path (`.docs/vault/Link-Topology.md`). An insight with no evidence is not an insight - it is a guess, and does not belong here.

## Superseding

An insight is superseded when it no longer holds - when the pattern breaks or the dynamic changes. Set its Status to `Superseded` and link it forward to the insight that replaces it. Insights are not rewritten in place.

## When insights are written

Reflection runs on the periodic consolidation pass, and whenever the summed importance of the memories captured since the last reflection crosses about 25 (see `Memory/Memory.md`). Each pass poses a few questions over recent context and entity memory and writes the insights that answer them, every one citing the memories it was drawn from.

## Entries

<!-- brain:collection-entries (drawn by .github/scripts/update-vault.py - do not edit by hand) -->
_No insights recorded yet._
<!-- /brain:collection-entries -->
