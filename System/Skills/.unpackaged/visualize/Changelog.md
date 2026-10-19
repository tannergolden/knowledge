---
id: "sy-skill-visualize-changelog"
title: "visualize - Changelog"
description: "Change history for the visualize skill."
aliases: []
keywords: ["version history", "release notes", "visualize changes", "revision log"]
author: "Tanner Golden"
path: "BRAIN/System/Skills/.unpackaged/visualize/Changelog.md"
layer: 4
folder: "system"
type: "log"
tags: ["system", "log"]
status: "active"
policy: false
created: 2026-06-28
updated: 2026-10-19
---
# visualize Changelog

## Current Version

**`01.04.01`**

Semantic versioning, `MAJOR.MINOR.PATCH`, two-digit zero-padded segments. This value matches `metadata.version` in `SKILL.md`. Each section shows the 4 most recent entries; older entries age out. Newest on top.

---

## How This File Works

- **Tracks** changes to how the skill works: tiers, the team, references, templates, the output contract. Not below-PATCH tweaks.
- **Bump** PATCH for a fix, MINOR for a backward-compatible addition, MAJOR for a breaking change. Update the Current Version line with every entry.
- **4-entry cap** per section; a fifth drops the oldest.

---

## Major Updates

> Breaking changes, restructured pipeline, incompatible output. Most recent 4 entries.

### `01.00.00` - 2026-06-28

Initial build of the visualize skill. Rebuilt fresh on the federated-team architecture as the BRAIN's fifth faculty ("show"), dispatching the new standing Design team (Margot, Otto, Vera) to a standard of graphical integrity. Grounded in a research pass (Tufte, Cleveland and McGill, Munzner, Few, WCAG) and an adversarial design review that collapsed an initial six-role roster to a lead plus two.

## Minor Updates

> Backward-compatible additions. Most recent 4 entries.

### `01.04.00` - 2026-06-28

Added a curated color-palette library: assets/palettes.json (about 87 established data-visualization palettes across categorical, sequential, and diverging, hex copied verbatim from ColorBrewer, the viridis family, Tableau, d3, Plotly, CARTOColors, Paul Tol, and Okabe-Ito, with colorblind-safe defaults) and references/palette.md (how to pick a palette by data type and apply it). The Visualization Designer now chooses a palette at creation; the Critic still gates accessibility. From a deep research run that computed hex from canonical source files.

### `01.03.00` - 2026-06-28

Added four format and inline-craft references from a deep research run: formats.md (choosing the inline format, with a per-format decision guide and the clean-Mermaid checklist), svg-craft.md (theme-reactive hand-authored SVG: viewBox, currentColor, markers, text-fitting, accessibility), interactive.md (self-contained HTML widgets and the charting-library decision matrix, canvas vs SVG, responsive sizing, interaction), and inline-aesthetics.md (typography, color and theming, data-ink, motion, native feel). Grounded in W3C and MDN, the chart-library and Mermaid official docs, and Tufte and Few, and fact-checked.

### `01.02.00` - 2026-06-28

Proactive use: the skill now fires on its own, not only on request. It defaults to producing a visual whenever a substantive response carries data or structure (comparison, process, timeline, hierarchy, tradeoff, relationship, system), skipping trivial or conversational replies. The description and a new Proactive use section carry the lowered-but-earned threshold; graphical integrity still governs. Standing rules were added to the skill-router and per-turn hooks.

### `01.01.00` - 2026-06-28

Saved visuals now file to the held visuals library at `Inbox/Visuals/` by default (a named home still wins when one fits), with the artifact's entry added to the `Visuals.md` index. The skill output contract, the Design roster's delivery rule, the engine sweep-exclusion, and Inbox.md were updated together.

## Patch Updates

> Fixes and clarifications. Most recent 4 entries.

### `01.04.01` - 2026-10-19

Moved the preflight off the retired engine: an existing file's last state is committed before an edit, and `.github/scripts/lint-notes.py` is the exit gate. The archive now carries the Design team, vendored when it is built.

### `01.03.01` - 2026-06-28

Audit fixes to the format references found by a fresh-context review: corrected the Chart.js bundle figure in interactive.md (full bundle is comparable to D3, not markedly smaller), added a browser-support caveat and a `currentColor` fallback for `context-stroke` markers in svg-craft.md, and clarified that `orient=auto-start-reverse` needs the marker referenced on both ends.

<!-- This is a BRAIN documentation node: it carries the BRAIN global frontmatter schema
     above (Instructions Section 8), not the Agent Skills schema. -->
