<!--
title: "Finance - Skill Information"
description: "BRAIN documentation node for the finance skill: dispatches the standing Finance team to advise on any personal or household money matter, from budgets and debt to taxes, retirement, insurance, benefits and big purchases. Use when the user asks a money question, wants a plan, faces a money life event, or wants a checkup."
type: "index"
keywords: ["/finance", "personal finance skill", "money advice", "budget", "debt payoff", "retirement planning", "household finance", "finance team"]
-->

# 💰 Finance - Information Guide

Filed in `System/Skills/.unpackaged/` - skill sources live hidden and carry no wikilinks; the packaged `finance.skill` artifact sits at the `Skills/` root. Governance: `AGENTS.md` and the Rules in each folder's note.

## What this skill does

`finance` advises the Founder on any personal or household money matter. It runs in three modes: **ask** answers one question or decision, **plan** builds a plan toward a goal or through a life event, and **review** runs the money checkups on their cadence. Each is scaled across three tiers (quick, standard, deep). It holds one standard, the Founder's interest first, with show the math as its craft rule, and it gives advice only: nothing it does moves money, applies, signs, files or logs in. It delivers in chat by default, records dated deadlines and open loops in `Memory/`, and proposes every `Profile/Finances.md` change for the Founder's yes.

## How it fits the architecture

The skill names the **Finance team** in `metadata.team: Finance`, the standing personal and household finance team in the federated agent library (`Inbox/Faculties/Finance/`, lead Financial Planning Lead). The roster is the lead plus eight: seven domain seats (cash flow, credit and debt, tax, investing and retirement, insurance and estate, equity and benefits, home and major purchases) and an independent Plan Reviewer. It carries no `agents/` folder: agents are referenced by name and vendored in only at Publish. The skill is a thin orchestration and doctrine layer: its `references/` carry the method (the doctrine and the foundations order, the dispatch and routing, the data and write rules, the checkup cadence, the life-event checklists), its `templates/` scaffold each artifact (the fact sheet, the brief, the plan, the review ledger, the checkup scorecard), and its `assets/` hold the trigger tests and the official sources. Every agent returns its artifact and persists nothing; the skill alone writes, behind its gate. Where the Founder's money meets a venture's, it works with AR's Finance & Accounting department through `board`.

## Design basis

Built on the vault's federated-team architecture, modeled on the Research and Design teams' maker-and-reviewer split, and organized around the domains of personal financial planning practice: cash flow, credit and debt, tax, investing and retirement, risk management and estate planning, employee benefits and equity, and major purchases. Its standard follows the fiduciary duty of a fee-only planner (the client's interest first, conflicts disclosed), and its method rests on durable heuristics (the foundations order, total cost over the monthly payment, the horizon before the return, insure the catastrophic first) rather than figures that change every year, which each run fetches from the official source and dates. Two design choices are load-bearing: every load-bearing number is reproduced by a script before review, because arithmetic is where language models fail quietly; and the Plan Reviewer reads the draft blind, because suitability errors are the ones a maker cannot see in its own work.
