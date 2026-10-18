---
name: [skill-name]
description: [Use this skill whenever the user ... - 4 to 6 concrete trigger phrases, plus "even without saying [skill-name]". This line decides whether the skill ever fires.]
license: proprietary
allowed-tools: [the exact, minimal tools this skill's workflow calls, comma-separated. List only what it actually uses, for example Read, Write, Edit, Bash, Grep, Glob, Task.]
metadata:
  team: [team-name]
  version: "01.00.00"
  id: "sy-skill-[skill-name]-spec"
  author: "Tanner Golden"
  status: "active"
---

# [emoji] [Skill Name]

<!-- Copy this folder's contents to Skills/.unpackaged/<skill-name>/ and fill them in (paths here are relative to the
     agent-home root). Rename this manifest from t-SKILL.md to SKILL.md in the new skill (keep no t-SKILL.md); it is named t-SKILL.md in the template only
     so the packaged develop.skill carries exactly one SKILL.md and installs cleanly. metadata.team names the team folder in an agent home that this skill composes (a portable
     string annotation). The real per-complexity dispatch is the "Dispatch scaling" section below, in the body. -->

<!-- BODY SKELETON: every skill mirrors this spine, in this order (references/architecture.md). Title a slot for the
     skill's own domain if it helps (a Modes table may be Tiers); insert domain sections between the pipeline and
     Quality bars; never reorder the spine. Drop Conformance if the skill never touches the vault. -->

[One paragraph: what the skill does and its one standard, the principle that wins every conflict.]

> Operating doctrine lives in `references/`. Read [the key reference] before [the key step].

## Modes
[The operational table: the axis this skill runs on. First, so the reader learns how to invoke it before anything else.]

| Mode | Trigger | What it does |
|------|---------|--------------|
| **[mode]** | [trigger] | [what it does] |

## The architecture it serves
This skill composes the **[team-name]** team (`<agent-home>/[team-name]/`). Agents are referenced by name and routed by their description; nothing is copied locally. On Publish, the referenced agents are vendored into this skill's `agents/` so the package is self-contained.

## [Pipeline]
[The main method, named for the skill. Numbered steps from request to delivery.]
1. [step]
2. [step]

## Dispatch scaling
- Light task: dispatch [the smallest useful subset].
- Standard task: dispatch [more of the roster].
- Full task: dispatch the whole roster, the star lead last for synthesis or the gate.

## Conformance with the live BRAIN
[BRAIN-resident skills only; drop this section otherwise.] Read `Instructions.md` and `Constitution.md` and the namesake of every folder written into; back up before editing a vault file; reference vault files by plain path, never wikilinks; `brain.command lint` is the exit gate.

## Quality bars
- [The one standard, stated first.]
- No em dashes anywhere (Constitution 9.1); the shared validator fails on the character.
- Tools declared exactly: `allowed-tools` is the minimal set the workflow actually calls.
- [Other non-negotiables.]

## Boundaries
- Stay within [scope]. Never [the hard limits]. [confirm-first or write rules if it touches the vault.]
- vs [adjacent skill]: [the ruling that prevents overlap].
