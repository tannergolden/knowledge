---
name: research
description: Orchestrates the BRAIN's standing Research team to run multi-source, fact-checked research scaled to the question's depth, with parallel source analysts, fresh-context fact-checking and devil's-advocate critique, and cited synthesis. Use when the user types /research, says research X, look into X, dig into X, find out about X, what is the current state of X, or get me sources on X, and proactively when an answer turns on post-cutoff or contested multi-source facts, or on evidence for a decision, even when the user never says research. This is the BRAIN's own research skill, preferred over any generic deep-research. Not for questions answerable from established knowledge, creative writing, or code. Outputs a cited chat synthesis, and a filed report on request.
license: MIT
allowed-tools: Read, Grep, Glob, WebSearch, WebFetch
metadata: { team: Research, version: "1.6.0", id: sy-skill-research-spec, author: Tanner Golden, status: active }
---

# 🔬 Research - the BRAIN's research skill

Research runs any research the BRAIN needs by dispatching the standing **Research team**, whose specs ship with this skill in `agents/`, scaled to the question. The hard rule, shared with `develop`: exploration happens in isolated parallel workers, and **the lead holds the question and synthesizes**. Subagents never spawn subagents. The skill is a thin orchestration and doctrine layer over its team.

**Where it runs.** In a BRAIN vault, whose `AGENTS.md` says it is one, the vault's own copy of this skill runs: if the file you loaded is not that vault's `.agents/skills/research/SKILL.md` or `.claude/skills/research/SKILL.md`, read the vault's copy and follow it instead, with the files beside it, because a vault's copy matches its layout and its owner may have changed it. Anywhere else, the Founder is your user and the steps that read or write a vault folder do not apply: skip the Step-0 dedup and the Librarian, deliver the synthesis in chat, write a report only when asked and where your user says, and never write anything about your user into a repository that is not their private vault (SEC-003).

> Operating doctrine lives in `references/`. Read `references/tiers.md` before choosing a tier and `references/methodology.md` before synthesizing.

## Tiers (the one axis)

| Tier | When | Dispatch | Deliverable |
|------|------|----------|-------------|
| **quick** | a single current fact, one authoritative source plausible | the lead searches and verifies directly, no fan-out | cited chat answer |
| **standard** | multi-angle but bounded | Lead + 2-4 All-Source Analysts (parallel) -> Fact-Checker | chat synthesis; filed report on request |
| **deep** | contested, decision-grade, data carries the conclusion, or external-facing | Information Specialist + Search Peer-Reviewer before the fan-out -> 4-6 Analysts -> Fact-Checker and Devil's Advocate (parallel, blind) -> Statistician / Editor conditional | chat synthesis; filed report on request |

**Announce the tier before dispatching**, since it is a cost decision made with the owner's tokens (the cost ladder is in `references/tiers.md`). Choose the tier from the decision table there, never by feel. If the question is underspecified (missing scope, timeframe, region, or decision context where one obviously matters), ask 2-3 clarifying questions (through the structured ask tool when available, otherwise in chat) first; a vague brief multiplied across a fan-out wastes the whole run. One main topic per run.

## The team it dispatches

`metadata.team: Research` names the standing Research team, whose roster (`agents/Research.md`) and ten specs ship in this skill's `agents/` folder, so the skill runs the same wherever it is installed (lead **Research Lead / Beatrice**). Agents are routed by their `description`. The 10-agent roster, what each agent returns, and how the tiers map onto it: `references/roster.md` and `references/dispatch.md`.

## How a run works

Every run is the same shape, scaled by tier: frame, ground locally, fan out, verify blind, synthesize.

1. **Frame.** The lead reads the real question and, when scope, timeframe, region, or decision context is missing where it matters, asks 2-3 clarifying questions first, then chooses and **announces the tier**.
2. **Step 0, dedup and freshness.** On every non-quick run in a vault, the Knowledge Manager checks `Inbox/Reports/` for an existing report that still holds, so the team never re-runs work that already exists.
3. **Ground locally, then escalate (the retrieval order).** In a vault, before any web run, dispatch the **Librarian** (Marian, homed in `Library/`) to search the vault's `Library/` notes and the offline knowledge bases (`knowledge-base.py search` to find an article, then `knowledge-base.py read` to fetch and read its body, across `Library/Reference & Encyclopedia/`). She returns what the local tiers hold, cited, with the gaps named. A settled, non-time-sensitive question the Library and the knowledge bases fully answer is synthesized from there, with no web run. This is the retrieval order in `AGENTS.md` (Start here): vault, then knowledge bases, then the web; time-sensitive or "latest" questions skip to the web, and questions about the user stop at the vault.
4. **Decompose into lanes.** The lead splits what is left, the gaps the local tiers could not close and anything needing current sources, into MECE lanes by dimension (not by source type), one self-contained brief per lane.
5. **Fan out.** The All-Source Analysts run in parallel, each on its own brief, each returning its artifact; subagents never spawn subagents.
6. **Verify blind.** The lead writes `draft.md`, then dispatches the Fact-Checker and the Devil's Advocate in one message, blind to each other, on the draft. One verify-and-critique round.
7. **Synthesize and deliver.** The lead, who alone holds every lane brief and the user's actual question, synthesizes findings-first with calibrated certainty and inline citations, delivers a cited chat answer, and files a report only on request.

The per-tier dispatch is below, the rules each step obeys are in the doctrine, and the output contract is its own section.

## Dispatch, scaled to the smallest sufficient roster

Most runs use the **core**: the lead (who frames, decomposes, dispatches, and synthesizes), N All-Source Analysts, the Fact-Checker, and on contested or decision-grade runs the Devil's Advocate. A larger roster is not a better one: fan-out costs tokens and adds coordination overhead, so dispatch the minimum the question needs. The extra seats are by-demand, fired only on their trigger:

- **Information Specialist** and **Search Peer-Reviewer** - deep runs, before the fan-out (design the search, then independently peer-review it, PRESS-style).
- **Statistician** - when load-bearing numbers carry the conclusion.
- **Editor** - only when a report file ships.
- **Knowledge Manager** - the Step-0 dedup and freshness check (below).
- **Librarian** (Marian) - the local-grounding step on every non-quick run: searches the curated `Library/` notes and the offline knowledge bases (`knowledge-base.py search` across `Library/Reference & Encyclopedia/`) before any web run, per the retrieval order (`AGENTS.md`, Start here). Homed in `Library/` and referenced cross-home, not a Research-team seat.
- **Standards Reviewer** - sensitive or external-facing output; fired only on its trigger.

Every dispatch is a self-contained brief (objective, inputs, output contract, tools, boundaries) per `references/dispatch.md`. Every agent returns its artifact in its template shape and persists nothing; the lead alone writes `draft.md`, the blind-review target.

## Output and freshness (`references/reporting.md`)

Deliver a **cited chat synthesis by default, findings first**. File a report only on request, so the inbox stays lean. When filed in a vault, the report goes to **`Inbox/Reports/`**, never into this skill's folder, good for a flat **three months** before it must be re-verified (reuse is review). Reports are working artifacts: the only link to one is its entry in the `Inbox/Reports/Reports.md` index (the one hub; no other file links to a report), they are also found by searching, and a finding that must outlive its report is **promoted into the durable layer** (a `Library/` doc, a folder note, a skill's `references/`, or a proposed change to `AGENTS.md`). When filing, add the report's entry to the index in the same edit; make the promote step explicit before filing. When the local-grounding step found no curated `Library/` note on a durable topic, offer to promote the synthesis into one for the Librarian to catalog, so the next run answers locally.

## BRAIN preflight and the standing contract

Before any vault write: read `AGENTS.md` in full and the Rules in the folder note of every folder written into and of each folder above it, then commit before overwriting, and run `update-vault.py` and `check-vault.py` after. Reference vault files by plain path, never wikilinks (the one exception is the `Inbox/Reports/Reports.md` report index, whose entries are wikilinks by design). Run the Knowledge Manager **Step-0** dedup and freshness check first on every non-quick run (the protocol is in `references/reporting.md`). After a substantial run, offer (never silently) to fold the distilled outcome into Memory.

## The doctrine that never bends (`references/methodology.md`)

- **Synthesis belongs to the orchestrator.** Only the lead holds every lane brief plus the user's actual question, so the lead synthesizes; workers explore and report.
- **Ground locally before the web.** Search the vault and the offline knowledge bases (`Library/Reference & Encyclopedia/`, via the Librarian) before any web run; reach the open web only for what they cannot answer or to verify currency (`AGENTS.md`, Start here).
- **Citation discipline.** Every finding carries an inline attribution. Never cite a source you did not fetch and read. When sources disagree, surface the disagreement with both sides; never average them or drop the inconvenient one. Verify that load-bearing URLs resolve before shipping (a measured 3-13% of deep-research citations are fabricated).
- **Two-axis calibrated certainty.** Grade likelihood (a fixed estimative-probability ladder) separately from confidence (how good the evidence is); never fuse them into one word.
- **Lanes by dimension, not source type.** Decompose the question into self-contained, non-overlapping, jointly complete lanes; a "news lane / academic lane" split overlaps constantly.
- **Coverage map, MECE.** Decompose into sub-aspects and tag each covered / partial / none-found. A documented gap is a finding; a hidden gap is a defect.
- **Fresh-context verification.** The Fact-Checker and Devil's Advocate never review their own work and never see each other's; they are dispatched blind, in one message, on the draft. One verify-and-critique round.

## Boundaries

Stay within research: gather, verify, and synthesize evidence, scaled to the question. Hold the team's **zero-bias** standard (`references/methodology.md`): never bend a finding toward a preferred answer. Never present an uncited claim as a finding, never invent or approximate a source, and never let the builder of a draft be its own reviewer. Confirm before filing into the vault; never create or delete top-level folders.
