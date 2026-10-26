# Roster - the Research team wired to the pipeline

The contract that wires this skill to the standing Research team, whose specs ship in this skill's `agents/`. It is the single source of truth for who runs, on what, and what each one hands back; `dispatch.md` sets the per-tier order and the briefing shape.

**The return-based flow.** Every team agent **returns** its artifact as its final message and **persists nothing** (that is each spec's write-scope). The lead is the only one who writes a workspace file: `draft.md`, the synthesis the blind reviewers attack. So the lead collects the returns, writes `draft.md`, points the Fact-Checker and Devil's Advocate at it, and applies their returned ledgers. Never brief an agent to "write a file": that contradicts its spec and confuses it.

## Each agent: trigger, input, what it returns, and the template that shapes the return

| Agent (name) | Runs on | Input | Returns | Template |
|--------------|---------|-------|---------|----------|
| **Research Lead** (Beatrice) | every run, as orchestrator | the user's verbatim question | the findings-first answer, and `draft.md` for review | the chat shape in `reporting.md`; `report.md` when filed |
| **Knowledge Manager** (Mabel) | before every non-quick run (Step-0) | the topic | the library verdict: canonical report or gap, freshness vs `review_by`, prior findings | `reporting.md` Step-0 (inline) |
| **Information Specialist** (Lydia) | deep | the lanes | the source strategy per lane | `templates/source-strategy.md` |
| **Search Peer-Reviewer** (Mara) | deep, before the fan-out | the source strategy | the search audit: PASS or REVISE, with the sentinel check | `templates/search-audit.md` |
| **All-Source Analyst** (Jasper) xN | standard, deep | one lane (the five lane fields) | the lane findings brief | `templates/lane-brief.md` |
| **Fact-Checker** (Ruth) | standard, deep | `draft.md` | the claim ledger | `templates/verification.md` |
| **Devil's Advocate** (Damon) | deep; standard when contested | `draft.md` | the objection set | `templates/critique.md` |
| **Statistician** (Soren) | when load-bearing numbers carry the conclusion | `draft.md` | the number ledger, or NONE | `templates/statistical-review.md` |
| **Standards Reviewer** (Sterling) | sensitive or external-facing output | the draft | the exposure ledger: BLOCK / REVISE / CLEAR per exposure | the ledger shape below (inline) |
| **Editor** (Genevieve) | only when a report file ships | the draft report | the polished report plus an edit note (the lead applies it) | `templates/report.md` |

## Verdict vocabularies (so the lead applies a return mechanically)

- **Search Peer-Reviewer:** PASS (fan out) / REVISE (back to the Information Specialist once, then re-review).
- **Fact-Checker:** SUPPORTED / WEAK-BASIS / UNSUPPORTED / NEEDS-CITATION / CONTRADICTED. Apply: keep / soften to stated confidence / cut / add the citation / reverse the claim (CONTRADICTED, the source says the opposite).
- **Devil's Advocate:** FATAL / MATERIAL / MINOR. Respond to every FATAL and MATERIAL: accept (adjust the conclusion) or rebut (with the citation that settles it).
- **Statistician:** SUPPORTED / UNSUPPORTED-NUMBER / NOT-COMPARABLE / OVERSTATED, or NONE when the draft carries no load-bearing numbers.
- **Standards Reviewer:** BLOCK (do not ship) / REVISE (the named change) / CLEAR.

## The Standards Reviewer exposure ledger (its inline shape)

A by-demand seat with no template file; it returns one row per exposure: `exposure - the specific rule it touches - the concrete risk - disposition (BLOCK / REVISE / CLEAR) - the required change or the escalation`.

## Blind pairing

The Fact-Checker and the Devil's Advocate, plus the Statistician when the draft carries load-bearing numbers, are dispatched in one message, each reading only `draft.md`, never the lead's reasoning or each other's return. The rule and its rationale live in `dispatch.md`.
