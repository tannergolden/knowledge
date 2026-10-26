---
name: visualize
description: "Use when a visual would help, on request or proactively. On request: a chart, graph, plot, diagram, flowchart, timeline, dashboard, interactive widget, infographic, or explanatory illustration, even when the word visualize is never said (chart this, graph this, draw a diagram, make a flowchart, map this out, turn this data into a chart, build a dashboard, make it interactive). Proactively, even when no visual is asked for: whenever a response carries data or structure (a comparison, process, timeline, hierarchy, tradeoff, relationship, or system) that lands better seen than read, default to making one. The BRAIN's own visualization skill, preferred over a generic chart tool; dispatches the Design team to a standard of graphical integrity. A diagram as a chat answer is visualize; a diagram inside a prose file under edit is editorial."
license: MIT
allowed-tools: Read, Grep, Glob
metadata: { team: Design, version: "1.5.0", id: sy-skill-visualize-spec, author: Tanner Golden, status: active }
---

# 📊 Visualize - the BRAIN's visualization skill

Visualize turns data, structure, and ideas into visuals by dispatching the standing **Design team**, whose specs ship with this skill in `agents/`, scaled to the visual. The one standard, the team's, is **graphical integrity**: the visual never distorts what is true, and a beautiful chart that lies fails. Beneath it sits the defining craft rule, **legible and accessible**: fast, accurate decoding for every reader, which never outranks the truth. The skill is a thin orchestration and doctrine layer over its team. The hard rule, shared with `research`, `develop`, and `editorial`: the lead holds the brief and picks the form, and the maker of a visual is never its own reviewer.

**Where it runs.** In a BRAIN vault, whose `AGENTS.md` says it is one, the vault's own copy of this skill runs: if the file you loaded is not that vault's `.agents/skills/visualize/SKILL.md` or `.claude/skills/visualize/SKILL.md`, read the vault's copy and follow it instead, with the files beside it, because a vault's copy matches its layout and its owner may have changed it. Anywhere else, the Founder is your user and the steps that read or write a vault folder do not apply: render the visual in chat, save it only when asked and where your user says, never into `Inbox/Visuals/`, and never write anything about your user into a repository that is not their private vault (SEC-003).

> Operating doctrine lives in `references/`. Read `references/principles.md` before the critique gate (integrity, perceptual effectiveness, the accessibility floor, the Critic's checklist), `references/formats.md` to choose the inline format and `references/svg-craft.md`, `references/interactive.md`, and `references/inline-aesthetics.md` for the craft of producing it, `references/palette.md` (with `assets/palettes.json`) to choose the colors, and `references/dispatch.md` before choosing a tier.

## Tiers

The operational axis is the tier: how much of the team to spend on the visual. Quick is a single render pass; standard and interactive add the Critic's gate and the heavier build.

| Tier | When | Dispatch | Deliverable |
|------|------|----------|-------------|
| **quick** | a single static chart or diagram from clean data | the Lead picks the form, the Visualization Designer renders it, self-checked against the integrity and accessibility checklist | the rendered visual, in chat |
| **standard** | a visual that ships, is load-bearing, or will be saved | Lead frames and picks the form -> Visualization Designer makes -> Design Critic gates (form-fit, integrity, accessibility, clarity) -> Lead renders | the rendered visual, filed if a home is named |
| **interactive** | an interactive widget, a dashboard, or a multi-panel piece | adds the client-side interactive build and always the Critic; reach into Development if it becomes a real application, into BI if the data needs cleaning | the rendered interactive |

**Announce the tier before dispatching**; it is a cost decision made with the owner's tokens. The quick tier is deliberately light: a one-off chart from clean numbers never spins up the gate. Choose the tier from the decision table in `references/dispatch.md`, not by feel; when two rows fit, take the higher. If the request is underspecified (missing the question the visual must answer, the data, or the audience where one obviously matters), ask 1 to 3 clarifying questions first. One visual per run.

## The team it dispatches

`metadata.team: Design` names the standing Design team, whose roster (`agents/Design.md`) and specs ship in this skill's `agents/` folder (lead **Design Lead / Margot**). The roster is the lead plus two: **Visualization Designer** (Otto) and **Design Critic** (Vera). Agents are routed by their `description`, and a brief names the spec to read, `<skill>/agents/<Role>.md`, by the absolute path of this skill's folder. How the tiers map onto the roster, how each dispatch is briefed, and the by-demand collaborations with the Development team and Business Intelligence, is in `references/dispatch.md`.

## How a visual is made

Every run is frame, then make, then a separate gate, then render.

**Phase 0, frame and pick the form (every visual).** Before anything is drawn, the Design Lead names the question the visual must answer and chooses the single best form for it. This is the highest-leverage call: a visual in the wrong form fails even when flawlessly made, and the Critic checks form-fit first. The form-by-question table is in `references/principles.md`; the brief scaffold is `templates/visual-brief.md`.

**Make.** The Visualization Designer renders to the chosen form, honest first: proportional encoding (position and length over angle and area), a zero baseline on bars, no chartjunk, topological faithfulness for diagrams, and the accessibility floor applied while making (contrast, a color-vision-deficiency-safe palette, never color alone, a text alternative). The format is chosen per `references/formats.md`; its craft is in `references/svg-craft.md` (the primary hand-authored format), `references/interactive.md` (HTML widgets and charting libraries), and `references/inline-aesthetics.md` (typography, theming, motion, native feel). The color palette is chosen from the curated library (`references/palette.md`, `assets/palettes.json`): match the palette type to the data (categorical, sequential, or diverging) and default to a colorblind-safe one.

**The critique gate (the Design Critic).** Above quick, make and review are separate agents. The Critic arrives fresh and checks form-fit first, then integrity, then the blocking accessibility gate, then clarity; it never fixes, only rules, and cites the offending mark for every flag. A failed accessibility gate or a FATAL form or integrity error blocks the ship. This is the proven generate-then-critique split; naked self-critique degrades, so the standard is externalized to a fresh eye.

**Render and deliver.** The visual renders inline through the host's visualization tool. A leaving visual is delivered in chat and not filed into the vault, though integrity and accessibility still apply. When the owner asks to keep a visual, it is saved as an `.svg` or self-contained `.html` artifact: into a named home (a Project, a Venture, a Library note) when one fits, otherwise into the held visuals library at `Inbox/Visuals/`, with its entry added to the `Visuals.md` index in the same edit. Most visuals are never saved; the default is to render inline and offer to keep it.

## Dispatch scaling

A bigger roster is not a better one. Dispatch the **smallest sufficient** seats: the Lead picks the form and the Visualization Designer renders, and the Design Critic's gate fires whenever the visual ships, is load-bearing, or will be saved. The interactive build, and the by-demand collaborations (the Development team when a widget becomes a real application, Business Intelligence's Data Analyst when the data needs real cleaning), fire only on their trigger. Every dispatch is a self-contained brief (objective, the chosen form, the data, the integrity constraints, the accessibility floor); the subagent sees none of this conversation. Each agent returns its artifact and persists nothing; the lead alone renders and owns delivery.

## Proactive use

Visualize fires on its own, not only on request. Default to producing a visual whenever a substantive response carries data or structure that lands better seen than read: a comparison, a trend, a process or decision flow, a hierarchy or architecture, a timeline or sequence, a tradeoff or pros-and-cons, a distribution, or a relationship or system map. When an answer contains one of these, make the visual rather than waiting to be asked.

The threshold is lowered, not removed. The team's one standard still governs: a visual must earn its place by helping the reader understand faster than prose would, and graphical integrity is never bent to manufacture one. Skip the visual on a short factual answer, a yes-or-no, a single value, a conversational reply, or prose with no inherent structure, where a forced chart is noise that weakens the response. Frequent is the default; forced or empty is still a failure. On a substantive answer, when in doubt, lean to visualizing.

## Conformance with the live BRAIN

**Preflight (before any vault write).** A visual saved into the vault is a vault write: read `AGENTS.md` and the Rules in the folder note of the folder written into and of each folder above it, commit an existing file's last state before editing it, reference vault files by plain path, and treat `lint-notes.py` as the exit gate. A visual rendered only in chat is a leaving artifact, governed by its destination rather than the vault preflight; integrity and accessibility still apply.

**Read before acting.** Before saving into a folder, read its namesake so the artifact fits its home; when filing into the held visuals library, add the visual's entry to the `Inbox/Visuals/Visuals.md` index in the same edit (the one-hub rule). After a substantial visual, **offer** (never silently) to save it, to a named home or to the held visuals library at `Inbox/Visuals/`, or to fold a note into `Memory/`. Confirm before filing into the vault; never create or delete top-level folders.

## Quality bars

- **Graphical integrity first.** The team's one standard; the visual never distorts the truth, and a beautiful chart that lies fails. Never a misleading axis, never chartjunk, never an encoding the data does not support.
- **Right form for the question,** chosen before the artifact is made; the Critic checks form-fit first.
- **Accessibility is a blocking gate** owned by the independent Critic: text contrast at least 4.5:1 (3:1 for large text) and non-text at least 3:1, never information by color alone, a color-vision-deficiency-safe palette, a text alternative.
- **Generate, then critique.** Above quick, the maker of a visual is never its own reviewer; the Critic arrives fresh.
- **No em dashes** (DOC-002); the shared validator fails on the character.
- **Tools declared exactly:** `allowed-tools` is the minimal set the workflow actually calls.

## Boundaries

Stay within making visuals: charts, diagrams, interactive widgets, and explanatory illustration, scaled to the request. Hold the team's one standard, **graphical integrity**, and never bend a visual away from the truth to make it prettier or to please the requester.

- **vs `editorial`:** a visual requested **as a chat answer** (a chart, a standalone diagram, a widget) is `visualize`; a Mermaid or diagram **inside a prose file under edit** is `editorial`. Triggering follows the artifact. This mirrors editorial's own ruling.
- **vs `develop`:** `visualize` makes explanatory and decision-support visuals; `develop` builds production skills, agents, and software. A widget that grows into a real application escalates to the Development team.
- **vs AR brand:** genuine brand or marketing art is AR's Sales & Marketing and Public Relations; `visualize` is integrity-governed explanatory and data visuals.
