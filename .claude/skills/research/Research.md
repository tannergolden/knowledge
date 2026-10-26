<!--
title: "Research - Skill Information"
description: "BRAIN documentation node for the research skill: dispatches the standing Research team to run depth-scaled, multi-source, fact-checked research with cited synthesis."
type: "index"
keywords: ["/research", "research skill", "deep research", "multi-source research", "fact-checked", "research team", "cited synthesis", "look into"]
-->

# 🔬 research - Information Guide

Filed in `.agents/skills/research/`, where the agent apps read a repository's skills; `update-vault.py` copies it to `.claude/skills/research/` for Claude Code and packs `System/Skills/research.skill` for the Claude app. Skill files carry no wikilinks. Governance: `AGENTS.md` and the Rules in each folder's note.

## What this skill does

`research` is the BRAIN's own multi-source, fact-checked research skill. It dispatches the standing Research team, which ships inside it, scaled to the question across three tiers (quick, standard, deep): parallel source analysts gather and cite, a fresh-context fact-checker and devil's advocate attack the draft, and the lead synthesizes a cited answer. It delivers a findings-first chat synthesis by default and files a report only on request. It is preferred over any generic deep-research because it runs the vault preflight and follows this BRAIN's conventions.

## How it fits the architecture

The skill names the **Research team** in `metadata.team: Research`, the standing research team in the federated agent library, and carries it in its own `agents/` folder (lead Research Lead), the way `develop` carries the Development team, so it runs the same in a vault, in any other repository, and from a home install. The skill is a thin orchestration and doctrine layer: its `references/` carry the research method (the tier decision table, the `roster.md` contract that wires each agent to the artifact it returns, the dispatch and briefing protocol, the methodology spine, and reporting and freshness), and its `templates/` scaffold each agent's returned artifact (lane brief, source strategy, search audit, verification, critique, statistical review, and the filed report). The agents themselves live once, in the skill's `agents/`; every agent returns its artifact and persists nothing, and the lead alone writes the working draft. Finished reports file to `Inbox/Reports/`, the held reports library, on a flat three-month freshness window, with durable findings promoted out of the disposable report layer.

## Design basis

Built by `develop` from a deep research run on how to build the best AI research skill (Anthropic's multi-agent research system, OpenAI and Google deep-research architectures, PRISMA / PRESS systematic-review method, LLM-as-judge and citation-hallucination evidence, ICD-203 / GRADE calibrated uncertainty, and Anthropic's Agent Skills authoring guidance), gap-analyzed against the reference research skill and hardened by a blind fact-checker and devil's-advocate pass. Two design corrections from that pass are load-bearing here: dispatch the **smallest sufficient** roster rather than the whole team, and make tier selection a **written decision table** (`references/tiers.md`), not a judgment call.
