<!--
title: "Identify - Skill Information"
description: "BRAIN documentation node for the identify skill: coverage-driven interviewing that fills and deepens the Profile facets with validated frameworks, provenance-marked inferences, and approval-gated writes."
type: "index"
keywords: ["/identify", "identify skill", "profile interview", "fill out my profile", "get to know me", "coverage", "big five", "schwartz values"]
-->

# 🪪 identify - Information Guide

## What this skill does

Identify populates and deepens the `Profile/` facets by interviewing the user about themselves instead of waiting for hand-edits. It reads `.github/scripts/profile-coverage.py` to find the thinnest facet, runs a short mixed-delivery interview built on validated frameworks (Big Five and HEXACO for Personality, Schwartz values and Moral Foundations for Values, McAdams life-story prompts for Biography, the assistant custom-instruction schema for Working Style), and delivers a reviewed proposal batch the user approves line by line before anything is written. Self-reported facts land unmarked; every inference carries the full provenance marker and stays `unconfirmed` until approved; skips and refusals are never recorded anywhere.

## How it fits the architecture

`metadata.team` names **Research & Development (R&D)** (`Ventures/Agent Resources (AR)/Research & Development (R&D)/`), the home of the embodied lead: the skill runs as Adeline, the UX and Design Research Lead, whose interview craft (instrument design, non-leading questions, observed versus stated versus assumed evidence discipline) is the skill's spine. Two seats are dispatched cross-home, the research skill's Marian convention: Calvin the Writer (`Inbox/Faculties/Editorial/Writer.md`) composes the batch in the Founder's voice, and Sterling the Standards Reviewer (`Inbox/Faculties/Research/Standards Reviewer.md`) audits it blind against the Rules in `Profile/Profile.md` with BLOCK, REVISE, or CLEAR verdicts. The scoring side is the read-only `.github/scripts/profile-coverage.py`, which scores every facet with a dual net (a frozen scaffold fingerprint plus a placeholder grammar) and names the next target.

## Design basis

The interviewing doctrine, per-facet question maps with item banks, provenance contract, and roster contract live in this skill's `references/`. The governing law is the Rules in `Profile/Profile.md` (read-only by default, inferences flagged, no speculation, the most care for sensitive categories), with SEC-003 for privacy and the Rules in `Memory/Memory.md` for the Memory boundary (Memory and Profile never overlap). The provenance marker grammar restates `Profile/Profile.md` exactly; the facet science follows the frameworks named in the facet files themselves (BFI-2 facets, HEXACO Honesty-Humility, Schwartz's four higher-order value families, Self-Determination Theory, Moral Foundations, VIA strengths, Erikson life stage, McAdams narrative identity).
