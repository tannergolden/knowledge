---
title: "Develop - Skill Information"
description: "BRAIN documentation node for the develop skill: the factory that builds skills, single-file agents, and team rosters for the BRAIN federated agent library, and improves them and itself."
status: "active"
tags: ["system", "information", "timeless"]
aliases: ["/develop", "develop skill"]
keywords: ["skill factory", "agent builder", "meta-skill", "build a skill", "create an agent", "make a team", "self-improving skill"]
created: 2026-06-20
updated: 2026-07-02
type: "information"
folder: "system"
layer: 4
policy: false
version: "03.06.02"
author: "Tanner Golden"
path: "BRAIN/System/Skills/.unpackaged/develop/Develop.md"
id: "sy-skill-develop"
---

# 🏭 develop - Information Guide

Filed in `System/Skills/.unpackaged/` - skill sources live hidden and carry no wikilinks; the packaged `develop.skill` artifact sits at the `Skills/` root. Governance: Constitution.md. Operating manual: Instructions.md.

## What this skill does

`develop` is the factory that builds every other skill in this BRAIN, the single-file agents those skills use, and the team rosters that group the agents. It runs a short pipeline (requirements, mandatory research, reuse-first design, build, an independent-review gate) and reserves its heavy tests for skills bound for distribution. It is the one skill that creates other skills, and it improves them and itself after a mistake.

## How it fits the architecture

Agents live once in team folders `<agent-home>/<team>/` named for real professional teams; each team folder carries a namesake roster that references members by name; skills live in `Skills/.unpackaged/` and name their team in `metadata.team`. Develop authors into all three, reuses an existing agent before creating a new one, places each agent in its home team, and vendors agents into a skill only when packaging it to share. Skills carry no scripts of their own: deterministic helpers live in `brain.command`, shared across all skills, and develop checks conformance against the live BRAIN (running `brain.command skill validate` and reading the live governance) rather than freezing copies of its rules, so a skill stays aligned as the BRAIN changes.

## Self-improvement

In Recursive mode, develop runs a blameless postmortem on a skill or agent that misbehaved, proposes the minimal fix, applies it only on approval, verifies it independently (never grading its own work), and freezes the lesson into a regression ledger so a later change cannot undo it. It works on any skill, including develop itself.

## Design basis

The design is research-backed: the single-file agent standard, the shared library with vendor-on-export, and the meta-skill factory (lean v0, the validator-plus-independent-auditor gate, oracle-grounded self-improvement, and the hand-authored bootstrap).
