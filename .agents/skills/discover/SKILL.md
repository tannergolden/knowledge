---
name: discover
description: "Use when the user wants ideas or options generated, on request or proactively when a problem clearly calls for divergent options. Fires on brainstorm this, brainstorm ideas for, give me ideas, how might we, how could I, what are my options for, ways to, ideate on, help me think through, what could I do about, come up with approaches to, and any open-ended generate-possibilities request. The BRAIN's own ideation skill: it dispatches the Discovery team to generate ideas wide from distinct lenses, then converge to a ranked shortlist by a fair pairwise tournament, to a standard of generate wide, select fair. It generates options; deciding among them stays yours. A what-are-my-options is brainstorm; what-is-known-about-X is research; which-should-I-choose is board."
license: MIT
allowed-tools: Read, Grep, Glob
metadata: { team: Discovery, version: "1.1.0", id: sy-skill-discover-spec, author: Tanner Golden, status: active }
---

# 💡 Discover - the BRAIN's ideation skill

Discover generates ideas for any challenge by dispatching the standing **Discovery team**, whose specs ship with this skill in `agents/`, scaled to the question. The one standard, the team's, is **generate wide, select fair**: bold ideas are protected while generating (judgment deferred), and the winner is settled by a fair pairwise tournament, never by whose idea it is or which answer was hoped for. The skill is a thin orchestration and doctrine layer over its team. The hard rule, shared with `research` and `develop`: the lead holds the brief and generation happens in isolated parallel workers, so no generator grades its own idea and the tournament decides.

**Where it runs.** In a BRAIN vault, whose `AGENTS.md` says it is one, the vault's own copy of this skill runs: if the file you loaded is not that vault's `.agents/skills/discover/SKILL.md` or `.claude/skills/discover/SKILL.md`, read the vault's copy and follow it instead, with the files beside it, because a vault's copy matches its layout and its owner may have changed it. Anywhere else, the Founder is your user and the steps that read or write a vault folder do not apply: keep the idea pool in the conversation, dedup against what this run produced, write idea records only when asked and where your user says, and never write anything about your user into a repository that is not their private vault (SEC-003).

> Operating doctrine lives in `references/`. Read `references/brief.md` to frame the challenge, `references/lenses.md` for the generation lenses, `references/method.md` for the diverge-converge method and why parallel generation wins, `references/convergence.md` before ranking, and `references/dispatch.md` before choosing a tier.

## Tiers

The operational axis is the tier: how much of the team to spend on the challenge. Quick is a fast spread; standard and deep add the full tournament and, for cross-venture calls, the portfolio weighing.

| Tier | When | Dispatch | Deliverable |
|------|------|----------|-------------|
| **quick** | a fast spread of options on a small or low-stakes question | the lead frames a how-might-we, runs a light diverge across 1 to 2 lenses, dedups, and picks | a short ranked list, in chat |
| **standard** | a real ideation challenge worth a wide field | Lead frames and assigns lenses -> Idea Generators in parallel -> Curator dedups -> Critic stress-tests -> Tournament Ranker (Elo) -> Generators evolve the top -> lead kill-gate | a ranked shortlist with a recommendation; idea records and a report on request |
| **deep / portfolio** | a high-stakes challenge, or a cross-venture call | adds more lenses and more tournament rounds; the Portfolio Manager weighs the survivors across ventures by RICE | a filed discovery report; the idea pool updated |

**Announce the tier before dispatching**; it is a cost decision made with the owner's tokens. The quick tier is deliberately light: a fast "give me a few angles" never spins up the full tournament. Choose the tier from the decision table in `references/dispatch.md`, not by feel; when two rows fit, take the higher. If the challenge is underspecified (no clear problem, audience, or constraints where they matter), ask 1 to 3 framing questions first. One challenge per run.

## The team it dispatches

`metadata.team: Discovery` names the standing Discovery team, whose roster (`agents/Discovery.md`) and specs ship in this skill's `agents/` folder (lead **Creative Lead / Sebastian**). The roster is the lead plus five: **Idea Generator** (Iris), **Idea Critic** (Hugo), **Tournament Ranker** (Desmond), **Idea Curator** (Pearl), and **Portfolio Manager** (Lionel). Agents are routed by their `description`, and a brief names the spec to read, `<skill>/agents/<Role>.md`, by the absolute path of this skill's folder. How the tiers map onto the roster and how each agent is briefed is in `references/dispatch.md`.

## How a run works

Every run is frame, then diverge, then converge, then deliver.

**Phase 0, frame (every run).** The lead reframes the challenge as one or more "how might we" questions at the right altitude: broad enough to admit many solutions, narrow enough to give traction, and never a baked-in solution. A wrong frame produces the wrong ideas, so the framing is restated a few ways before any generation. The method is in `references/brief.md`; the scaffold is `templates/generative-brief.md`.

**Diverge (generate wide).** The lead assigns each Idea Generator a distinct lens from `references/lenses.md` and dispatches them as isolated parallel workers, judgment deferred. Parallel independent generation is the whole point: it neutralizes the production blocking, evaluation apprehension, and free-riding that make verbal group brainstorming underproduce (the evidence is in `references/method.md`). Go for quantity, welcome wild ideas.

**Converge (select fair).** The Curator dedups the raw pool against the whole pool, including killed ideas, so the team never re-treads a dead end. The Critic steelmans then stress-tests the survivors. The Tournament Ranker runs a pairwise Elo tournament, which yields a more reliable order than rating each idea in isolation. The Generators evolve and recombine the top ideas, which re-enter the tournament. The lead applies the kill-gate: most ideas die, by design.

**Deliver.** The lead hands over a ranked shortlist with a recommendation; the decision of what to pursue stays the Founder's. On request, the survivors are filed as idea records in the held pool at `Inbox/Ideas/` (with ICE and Elo scores, lifecycle status, lens, and lineage), and a finished discovery report goes to `Inbox/Reports/`.

## Dispatch scaling

A bigger roster is not a better one. Dispatch the **smallest sufficient** seats: a quick spread is the lead plus one or two Idea Generators; the Curator, Critic, and Tournament Ranker fire whenever a real field is generated and must be ranked; the Portfolio Manager fires only on a cross-venture or cross-project call (RICE). Every dispatch is a self-contained brief (the framed challenge, the assigned lens, the output contract); the subagent sees none of this conversation. Generators run in parallel and return their idea lists; the lead alone holds the brief, runs the kill-gate, and synthesizes the shortlist.

## Conformance with the live BRAIN

**Preflight (before any vault write).** Filing idea records or a report is a vault write: read `AGENTS.md` and the Rules in the folder note of every folder written into and of each folder above it (`Inbox/Ideas/Ideas.md` for records, `Inbox/Reports/Reports.md` for a report, and `Inbox/Inbox.md` above both), commit an existing file's last state before editing it, and reference vault files by plain path, never wikilinks (the one exception is the `Inbox/Reports/Reports.md` index, whose entries are wikilinks by design). Idea records carry the `record` File Role and the idea schema (`templates/idea-record.md`); a filed report adds its entry to the Reports index in the same edit.

**Read before acting.** Before filing into `Inbox/Ideas/`, read its namesake so records fit the pool, and dedup against the existing pool (including killed ideas) so the same idea is not re-filed. After a substantial run, **offer** (never silently) to file the survivors and to fold the distilled outcome into `Memory/`. Confirm before filing into the vault; never create or delete top-level folders.

## Quality bars

- **Generate wide, select fair.** The team's one standard; defer judgment while generating, and let the tournament, not the requester's preference or whose idea it is, pick the winner.
- **Generation and judgment never happen at once.** Generate first, criticize second; mixing them collapses both.
- **Generators are isolated parallel workers.** This is the evidence-backed way to beat verbal-brainstorming productivity loss; never collapse generation into one undifferentiated pass.
- **Select by pairwise tournament,** which is more reliable than rating ideas in isolation; the maker of an idea is never its sole judge.
- **Dedup against the whole pool, including killed ideas;** never re-tread a rejected dead end.
- **The decision stays the Founder's.** The skill delivers a ranked shortlist and a recommendation, not a committed choice.
- **No em dashes** (DOC-002); the shared validator fails on the character.
- **Tools declared exactly:** `allowed-tools` is the minimal set the workflow actually calls.

## Boundaries

Stay within ideation: generate options for a challenge and converge to the best, scaled to the question. Hold the team's one standard, **generate wide, select fair**, and never bend the tournament toward a preferred answer.

- **vs `research`:** discover **generates** new options; `research` **finds and verifies** what is already known. They are duals (research grounds ideas; ideation produces hypotheses research tests). "What is known about X" is research; "what could I do about X" is discover.
- **vs `board`:** discover generates **options**; `board` makes a multi-perspective business or strategy **decision**. "What are my options" is discover; "which should I choose" or "should I do X" is board.
- **vs `develop`:** discover produces ideas; `develop` builds the skill, agent, or thing.
- **vs `editorial` and `visualize`:** those render and communicate a result; discover generates the ideas in the first place.
