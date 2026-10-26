<!--
title: "visualize - Changelog"
description: "Change history for the visualize skill."
type: "record"
keywords: ["version history", "release notes", "visualize changes", "revision log"]
-->
# visualize Changelog

## Current Version

**`1.5.0`**

The version is SemVer, per standards' [versioning policy](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Releases-&-Versioning.md#-versioning-policy-semver). It matches `metadata.version` in `SKILL.md`, and `check-skills.py` fails when they differ. Each section shows the 4 most recent entries; older entries age out. Newest on top.

---

## How This File Works

- **Tracks** changes to how the skill works: tiers, the team, references, templates, the output contract. Not below-PATCH tweaks.
- **Bump** the version by standards' [versioning policy](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Releases-&-Versioning.md#-versioning-policy-semver), and update the Current Version line with every entry.
- **4-entry cap** per section; a fifth drops the oldest.

---

## Major Updates

> Breaking changes, restructured pipeline, incompatible output. Most recent 4 entries.

### `1.0.0` - 2026-06-28

Initial build of the visualize skill. Rebuilt fresh on the federated-team architecture as the BRAIN's fifth faculty ("show"), dispatching the new standing Design team (Margot, Otto, Vera) to a standard of graphical integrity. Grounded in a research pass (Tufte, Cleveland and McGill, Munzner, Few, WCAG) and an adversarial design review that collapsed an initial six-role roster to a lead plus two.

## Minor Updates

> Backward-compatible additions. Most recent 4 entries.

### `1.5.0` - 2026-10-26

The Design team now ships inside the skill, in `agents/`, instead of living in `Inbox/Faculties/Design/`, and the skill source moved from `System/Skills/.unpackaged/` to `.agents/skills/`, where the agent apps read a repository's skills, so the vault's own sessions load it and tannergolden/intelligence's home kit can carry it to every repository. A new **Where it runs** rule: in a vault, the vault's own copy runs, so a home copy hands over to it; anywhere else a visual renders in chat and is saved only where the user says. `allowed-tools` now pre-approves read-only tools only, and the frontmatter keeps one key to a line, as the home kit's reader requires. The description is now quoted: unquoted, its colon made the frontmatter invalid YAML, so a loader dropped the description and the skill could never trigger.

### `1.4.0` - 2026-06-28

Added a curated color-palette library: assets/palettes.json (about 87 established data-visualization palettes across categorical, sequential, and diverging, hex copied verbatim from ColorBrewer, the viridis family, Tableau, d3, Plotly, CARTOColors, Paul Tol, and Okabe-Ito, with colorblind-safe defaults) and references/palette.md (how to pick a palette by data type and apply it). The Visualization Designer now chooses a palette at creation; the Critic still gates accessibility. From a deep research run that computed hex from canonical source files.

### `1.3.0` - 2026-06-28

Added four format and inline-craft references from a deep research run: formats.md (choosing the inline format, with a per-format decision guide and the clean-Mermaid checklist), svg-craft.md (theme-reactive hand-authored SVG: viewBox, currentColor, markers, text-fitting, accessibility), interactive.md (self-contained HTML widgets and the charting-library decision matrix, canvas vs SVG, responsive sizing, interaction), and inline-aesthetics.md (typography, color and theming, data-ink, motion, native feel). Grounded in W3C and MDN, the chart-library and Mermaid official docs, and Tufte and Few, and fact-checked.

### `1.2.0` - 2026-06-28

Proactive use: the skill now fires on its own, not only on request. It defaults to producing a visual whenever a substantive response carries data or structure (comparison, process, timeline, hierarchy, tradeoff, relationship, system), skipping trivial or conversational replies. The description and a new Proactive use section carry the lowered-but-earned threshold; graphical integrity still governs. Standing rules were added to the skill-router and per-turn hooks.

## Patch Updates

> Fixes and clarifications. Most recent 4 entries.

### `1.4.2` - 2026-10-19

- References point at `AGENTS.md`, the folder notes' Rules and `.docs/vault/` instead of the retired root rule files. The description no longer names one owner's taste for visuals; how often to offer one beyond the skill's default is the user's call, in `Profile/Working Style.md`.
- The licence is MIT, and the versioning rules link to tannergolden/standards instead of restating them.
- Versions are plain SemVer: `01.04.01` is now `1.4.1`.

### `1.4.1` - 2026-10-19

Moved the preflight off the retired engine: an existing file's last state is committed before an edit, and `.github/scripts/lint-notes.py` is the exit gate. The archive now carries the Design team, vendored when it is built.

### `1.3.1` - 2026-06-28

Audit fixes to the format references found by a fresh-context review: corrected the Chart.js bundle figure in interactive.md (full bundle is comparable to D3, not markedly smaller), added a browser-support caveat and a `currentColor` fallback for `context-stroke` markers in svg-craft.md, and clarified that `orient=auto-start-reverse` needs the marker referenced on both ends.

<!-- This is a BRAIN documentation node: it carries the vault's note schema above
     (.docs/technical/vault/Note-Schema.md), not the Agent Skills schema. -->
