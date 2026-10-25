# Tiers - the complexity decision table

The tier is chosen from this table, not by feel. The lead applies it and announces the tier before any dispatch, because the tier is a cost decision made with the owner's tokens.

## Pick the tier by the question's shape

| The question is... | Tier | Why |
|--------------------|------|-----|
| a single current fact with one authoritative source plausible (a version, date, price, definition, "is X still true") | **quick** | one good source answers it; a team is waste |
| multi-angle but bounded: 2-4 distinct sub-questions, no strong disagreement expected | **standard** | a small parallel fan-out covers it, one verifier confirms |
| contested (credible sources will disagree), decision-grade (drives a costly-to-reverse choice), data-carrying (a number carries the conclusion), or sensitive / external-facing | **deep** | needs independent search review, full fan-out, and a blind adversarial gate |

When two rows fit, take the higher tier. When genuinely ambiguous, ask the user through the structured ask tool when available, otherwise in chat, rather than guessing.

## Calibrate the fan-out by effort (Anthropic's measured thresholds)

- **quick** - 1 searcher, about 3-10 tool calls, no subagents.
- **standard** - 2-4 All-Source Analysts, about 10-15 calls each, then the Fact-Checker.
- **deep** - 4-6 Analysts (10+ dispatches once the reviewers are counted), the full gate.

These thresholds are from Anthropic's multi-agent research system: simple fact-finding uses 1 agent, direct comparisons 2-4 subagents, complex research 10 or more. Match the dispatch to the band; do not exceed it reflexively.

## Triggers that force the tier up

- **Contested** (you expect credible sources to disagree) -> at least deep, and decompose **by viewpoint** (perspective lanes: regulator, incumbent, challenger, practitioner, affected user), not only by subtopic, because a subtopic split silently inherits one side's framing.
- **Decision-grade / high stakes** (the answer drives a choice that is costly to reverse) -> deep.
- **Load-bearing numbers** (an effect size, trend, or comparison carries the conclusion) -> keep the tier and add the **Statistician**.
- **Sensitive or external-facing** output -> add the **Standards Reviewer**.

## Triggers that drop the tier down

- **A current report exists.** The Knowledge Manager Step-0 check finds a report in `Inbox/Reports/` on the canonicalized topic within its three-month window -> reuse it (a quick confirmation refreshes the window), do not re-run. This is the single largest token saver.
- **The web is unreachable.** Answer from model knowledge with an explicit currency disclaimer and offer to retry; never fan out into nothing.

## The cost the tier buys

A full deep run costs roughly **15x** a chat answer (Anthropic measured multi-agent systems at about 15x chat tokens and 4x a single agent; token use alone explained about 80% of quality variance on their browse benchmark, one of three factors totaling 95%). So pick the lightest tier whose ceiling clears the question. A cheap lookup must never pay for the team.

**Fan out only when the question is genuinely breadth-first or exceeds a single context window.** Below that, a single agent under an equal token budget is at least as good (the data-processing-inequality result), so the tier ladder is a real gate, not a formality. Multi-agent runs also fail more as they grow (step-repetition, disobeying the spec), so a tight brief and the verify gate buy more than an extra seat.
