<!--
title: "Discover - Skill Information"
description: "BRAIN documentation node for the discover skill: dispatches the Discovery team to generate ideas wide for a challenge, then converge to a ranked shortlist by a fair pairwise tournament. Use when the user wants ideas or options generated."
type: "index"
keywords: ["/discover", "discover skill", "brainstorm", "ideation", "idea generation", "discovery team", "how might we", "idea tournament"]
-->

# 💡 Discover - Information Guide

## What this skill does

Discover takes a challenge or open question and generates a wide field of ideas, then converges to the strongest by a fair pairwise tournament, delivering a ranked shortlist with a recommendation. The decision of what to pursue stays the Founder's. It holds one overriding standard, generate wide, select fair: bold ideas are protected while generating, and the winner is settled on merit by tournament, never by whose idea it is or which answer was hoped for.

## How it fits the architecture

The skill composes the standing **Discovery team** (`metadata.team: Discovery`, in the skill's own `agents/`): the Creative Lead (Sebastian) frames the challenge and runs the diverge-then-converge cycle, the Idea Generator (Iris) produces ideas in parallel from distinct lenses, the Idea Critic (Hugo) stress-tests, the Tournament Ranker (Desmond) ranks by pairwise Elo, the Idea Curator (Pearl) dedups and keeps the records, and the Portfolio Manager (Lionel) weighs across ventures by RICE. It is the fifth faculty skill, the ideation counterpart to `research` (find): research finds and verifies what is known, discover generates what is new. Idea records live in the held idea pool at `Inbox/Ideas/`. The skill carries its team in `agents/`, so it runs the same in a vault, in any other repository, and from a home install; in a vault, the vault's own copy runs.

## Design basis

Built on the federated-team architecture over the pre-existing Discovery team. Grounded in a research pass over the established ideation methodology: Alex Osborn's brainstorming rules and the Osborn-Parnes Creative Problem Solving model, the Design Council's Double Diamond and IDEO / d.school design thinking (diverge then converge), the Diehl and Stroebe productivity-loss evidence (production blocking, why independent parallel generation beats verbal group brainstorming), the convergent selection methods (pairwise comparison and Bradley-Terry / Elo, ICE, RICE, dot voting, the kill-gate funnel), the divergent lens library (SCAMPER, de Bono lateral thinking, analogy and biomimicry, constraint manipulation, first-principles, assumption-reversal, and more), and the how-might-we briefing craft. The durable synthesis lives in `references/` (method, lenses, convergence, brief, dispatch).
