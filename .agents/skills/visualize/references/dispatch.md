# Dispatch - how the tiers map onto the Design team

How `visualize` spends the Design team, scaled to the visual. Read before choosing a tier. The roster is the lead plus two: Design Lead (Margot), Visualization Designer (Otto), Design Critic (Vera). Every dispatch is a self-contained brief; the subagent sees none of the conversation, returns its artifact, and persists nothing. The lead alone renders and owns delivery.

## Tier decision table

| Signal | Tier |
|--------|------|
| One static chart or diagram, data already clean, stays in chat | quick |
| The visual ships, is load-bearing, will be saved, or will be seen by others | standard |
| Interactive, a dashboard, multiple linked panels, or exploration of many values | interactive |

When two rows fit, take the higher. Announce the tier before dispatching; it is a cost decision.

## What runs at each tier

- **quick.** The Lead picks the form and briefs the Visualization Designer, who renders and self-checks against the integrity and accessibility checklist in `principles.md`. No separate Critic pass. Reserve for a one-off visual from clean data that stays in chat.
- **standard.** Lead frames and picks the form -> Visualization Designer makes -> Design Critic gates (form-fit, integrity, the blocking accessibility gate, clarity) -> Designer revision loop on cited issues only, with an iteration cap -> Lead renders and delivers. The Critic is the premium seat; keep it whenever the visual ships or will be saved.
- **interactive.** As standard, plus the Designer builds the interactive as one self-contained client-side artifact, and the Critic always runs (interactives fail accessibility most often). 

## How to brief each agent

- **Design Lead (Margot).** Give the request, the data or content, the question the visual must answer, and the audience. She returns the framed brief with the chosen form and why, then orchestrates. Use `templates/visual-brief.md`.
- **Visualization Designer (Otto).** Give the chosen form, the data, the integrity constraints, the palette or house style, and the render target (inline SVG or self-contained HTML). He returns the artifact source plus a one-line note of the encoding choices.
- **Design Critic (Vera).** Give the rendered visual or its source and the question it must answer; withhold the maker's notes so she does not inherit the maker's blind spots. She returns the review: form-fit verdict, integrity findings, the accessibility gate result (PASS or FAIL with the failing checks), clarity notes, and a ship-or-hold call. She never fixes.

## By-demand collaborations (not roster seats)

- **Development team.** When an interactive grows into a real application (a backend, persistence, a deploy), it is no longer a visualize widget; escalate to the Development team for the full build lifecycle. A disposable inline widget stays with the Visualization Designer.
- **Business Intelligence, Data Analyst (Aaron).** When the source data needs real cleaning, shaping, or validation before it can be plotted, the Lead reaches into BI's Data Analyst on a take-their-data, never-co-ownership basis. Most requests arrive with clean data and need no wrangling.

## The fix loop

A Critic HOLD or a failed accessibility gate resumes the Visualization Designer on the cited issues only; re-render, then re-run the Critic on the cited items with a fresh pass. If the same blocking issue survives two rounds, stop and surface it to the Founder: it usually means the data or the request cannot honestly produce the asked-for visual.
