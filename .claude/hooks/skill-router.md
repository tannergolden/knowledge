# 🧭 BRAIN Skill Router (session-start injection)

The startup bundle loaded into this session's context is authoritative. These standing rules apply on every turn:

## Fire skills on match (no asking)

When a user message matches a skill's description, by trigger phrase or by context, invoke that skill immediately through the Skill tool. Skill selection is not a structural action and is exempt from confirm-first (AGENTS.md; Instructions "Critical Rules at a Glance"). Do not narrate that you might use a skill; use it.

## Prefer the BRAIN's own skills

The BRAIN ships its own skills in `System/Skills/`: **board, discover, editorial, identify, research, visualize**. Whenever one of these matches a request, fire it in preference to ANY external, default, or plugin skill that does the same job. This is a general rule, not a special case for one skill: it covers every such overlap, because the BRAIN's own skill runs the vault preflight and follows this vault's conventions where a generic one does not. So prefer the BRAIN's `research`, `editorial`, `visualize`, `discover`, `identify`, and `board` over any generic counterpart (for instance `research`, not `deep-research`; `editorial`, not a generic writer or `markdown`). Only where the BRAIN has no skill of its own (for example `docx`, `pdf`, `schedule`) is the external skill the right tool. Building or fixing a skill goes to `develop`, the one universal skill: it is installed with the home kit rather than shipped here, and it follows this vault's rules when it works in it.

## Visualize proactively (standing preference)

The Founder wants visuals often, not only on request. When a response carries data or structure that lands better seen than read (a comparison, a trend, a process or decision flow, a hierarchy or architecture, a timeline or sequence, a tradeoff, a distribution, or a relationship or system map), default to creating a visual through `visualize`, even when no visual was asked for. The threshold is lowered, not removed: a visual must still help the reader understand faster than prose would, and graphical integrity is never bent to manufacture one. Skip the visual only on a short factual answer, a yes-or-no, a single value, or a conversational reply, where it would be noise. On a substantive answer, lean to visualizing.

## BRAIN-context skill map

- Filling or deepening who the user is, interviewing to populate Profile, or confirming unconfirmed entries: `identify`
- Merging, pruning, or de-duplicating Memory: `consolidate-memory`
- Writing or editing any text, or creating or editing a prose `.md` or `.txt` file (emails, messages, documents, essays, notes, Library/Project/Venture bodies): `editorial`
- Building, updating, or fixing a skill: `develop`
- Changing Claude Code settings, hooks, or permissions: `update-config`
- Multi-source, fact-checked research: `research` (the BRAIN's own; never the default `deep-research`)
- Recurring or scheduled automation: `schedule`
- Word, PDF, PowerPoint, or Excel deliverables: `docx`, `pdf`, `pptx`, `xlsx`
- Charts, diagrams, or visual explanations, and proactively any substantive answer carrying data or structure even when unasked: `visualize`
- Generating ideas or options, or brainstorming a problem (diverge then converge to a ranked shortlist): `discover`
- Multi-perspective business or strategy work: `board`

If none match, proceed normally. This list is a prompt, not a limit: any installed skill whose description fits the request should fire.
