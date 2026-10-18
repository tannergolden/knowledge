---
id: "sy-skill-develop-changelog"
title: "develop - Changelog"
description: "Change history for the develop skill and agent factory."
aliases: []
keywords: ["version history", "release notes", "develop skill changes", "revision log"]
author: "Tanner Golden"
path: "BRAIN/System/Skills/.unpackaged/develop/Changelog.md"
layer: 4
folder: "system"
type: "log"
tags: ["system", "log"]
status: "active"
policy: false
version: "03.06.02"
created: 2026-06-20
updated: 2026-07-02
---
# develop Changelog

## Current Version

**`03.06.02`**

Semantic versioning, `MAJOR.MINOR.PATCH`, two-digit zero-padded segments. This value matches `metadata.version` in `SKILL.md`. Each section shows the 4 most recent entries; older entries age out. Newest on top.

---

## How This File Works

- **Tracks** changes to how develop works: modes, the crew, references, templates, scripts, the output contract. Not below-PATCH tweaks.
- **Bump** PATCH for a fix, MINOR for a backward-compatible addition, MAJOR for a breaking change. Update the Current Version line with every entry.
- **4-entry cap** per section; a fifth drops the oldest.

---

## Major Updates

> Breaking changes, restructured pipeline, incompatible output. Most recent 4 entries.

### `03.00.00` - 2026-06-21

Reversed the cut-name/persona standard for the named AI workforce. Every agent now carries a tight **Identity block** above Role (a unique American `agent-name`, a one-line persona, a one-line voice) layered on the unchanged Role/Method/Output; the cut-decorative-backstory discipline holds (identity is not a biography, never claims competence, never restates Method). `agent-standard.md` and `templates/agent.md` carry the Identity block and the `agent-name` frontmatter; the four crew agents are named Marcus (builder), Diane (qa-auditor), Ray (requirements-analyst), Owen (reliability-engineer) as the worked example. `validation.md` adds the Identity check and the federated dual-home name-and-role uniqueness check (across `Toolkit/Agents` and `Ventures/Agent Resources (AR)`), with the honest note that the agent/team/library validator and the agent-catalog generator are specified but not yet built in `brain.command` (the next engine step). The name is an addressing handle: saying an agent's name routes to it.

### `02.00.00` - 2026-06-20

Breaking: removed the `scripts/` folder from the mandatory skill structure. Deterministic helpers no longer live inside a skill; they live in `brain.command` and are shared across all skills, invoked as subcommands (the validator is now `brain.command skill validate`, added to the engine this session). This makes the checks dynamic: the engine enforces the live BRAIN schema and rules, so a skill is never pinned to a frozen copy (the old `validate.py` carried a static frontmatter key list, exactly the staleness this removes). Added a Conformance-with-the-live-BRAIN doctrine: develop reads live governance and runs `brain.command` conformance for any BRAIN rule, for the skills it builds and for itself. The full skill/agent/team/library check set (spec in `references/validation.md`) merges into the engine's skill validator at Toolkit cutover, guarded so the richer checks apply only to new-architecture skills.

### `01.00.00` - 2026-06-20

Initial hand-authored v0 of the rebuilt develop factory for the Toolkit architecture. Modes: Create (default), Update, Recursive (self-improving, and improves other skills), Publish (vendor-on-export). Reuse-first authoring of single-file agents into the shared `Agents/` library, teams as rosters that reference agents by name, skills in `Skills/.unpackaged/`. Quality gate is the deterministic `scripts/validate.py` plus a fresh-context independent qa-auditor; heavy trigger smoke test and test-drive reserved for the Publish or complex tier. Self-improvement is oracle-grounded, approval-gated, independently verified, and frozen into a regression ledger, with no self-grading. Bootstrapped by hand; the rest grows by demand.

## Minor Updates

> Backward-compatible additions. Most recent 4 entries.

### `03.06.00` - 2026-06-28

Built out the deterministic Gate-1 skill validator so it checks everything `references/validation.md` specifies, not a subset. `brain.command`'s `_skill_validate` now also enforces the required files (`License.txt`, `Changelog.md`, the namesake) and folders (`assets`, `references`, `templates`); the `license`, `allowed-tools`, and `metadata` frontmatter keys; the `claude`/`anthropic` name ban; version consistency across the manifest, the Changelog Current Version, the Changelog frontmatter, and the namesake (one version, every site); the namesake and Changelog BRAIN frontmatter schema; no em dash in any source file; a `## Boundaries` section; and `## Bootstrap` only in develop. `validation.md` moves from partial to built (all four check sets). Verified by a broken-fixture negative test where every check fired, and by all three skills passing clean. The pass also fixed editorial's license filename (`license.txt` to `License.txt`).

### `03.05.00` - 2026-06-28

Canonicalized the SKILL.md skeleton. Every skill's SKILL.md body now follows one fixed section spine, with develop's own SKILL.md as the exemplar: an emoji H1 and intro, the references pointer, then Modes, the architecture it serves, the pipeline, dispatch scaling, conformance with the live BRAIN, quality bars, and boundaries (develop's own `## Bootstrap` origin note stays develop-only). `references/architecture.md` documents the skeleton, `templates/skill/t-SKILL.md` scaffolds it, and the Mandatory output structure section points to it. A skill may title a slot for its domain (a Modes table may be Tiers) and insert domain sections between the pipeline and quality bars, but never reorders the spine.

### `03.04.00` - 2026-06-21

develop now builds with the Development team, the BRAIN's standing engineering team at `Inbox/Faculties/Development/`, in place of the deleted platform-engineering crew. `metadata.team` is set to `Development`, and develop dispatches the Development team's Software Architect to design, its Full-Stack Engineer to build, and its QA Engineer and Application Security Engineer to verify independently in a fresh context, alongside the deterministic `brain.command` validator; SKILL.md and orchestration.md carry the new dispatch model and the dangling `platform-engineering` references (SKILL.md, orchestration.md) are removed. To make the team pointer safe, `brain.command`'s `_skill_validate` now rejects a `metadata.team` that does not resolve to a staffed roster, closing the blind spot that let the dead crew survive the gate; the Development team is registered as a flat federated agent home. The fresh-context-reviewer rule, build single-threaded and verify in parallel, is unchanged, and the Development team's own doctrine now enforces it.

### `03.03.00` - 2026-06-21

Made the agents more comprehensive by deepening the decision kernel, grounded in new deep-tier research. The honest finding: the lean standard was largely right, and the task-solving effect sizes (self-reflection, ReAct) do not transfer to advisory agents, but explicit decision criteria and worked examples do improve a decision-making agent's consistency, while length for its own sake degrades performance (lost-in-the-middle, instruction overload near 150 to 200, context rot). So `agent-standard.md` gains a "deepen the decision kernel, not every section" quality bar: each Method step carries its decision rule plus the role's framework, Examples carry a contrasting decide-versus-escalate pair, Identity, Recovery, and Non-negotiables stay lean, and depth is governed by instruction count (a spec past ~150 lines is a smell). Applied to the five Administration agents (each about 60 lines, roughly +12 of pure decision content, zero backstory) and verified by agents validate.

## Patch Updates

> Fixes and clarifications. Most recent 4 entries.

### `03.06.02` - 2026-07-02

Retired the phantom qa-auditor name from the live doctrine: SKILL.md (the self-improvement mode line), `references/orchestration.md`, `references/self-improvement.md` (step 5), `references/validation.md` (the Gate 2 heading and body), and `assets/golden-set.md` now name the real fresh-context reviewers, the Development team's QA Engineer and, where security-relevant, the Application Security Engineer. Documented the lead embodiment in SKILL.md's "How develop runs": develop embodies the Development team's ★ Engineering Lead (Maxwell) when it orchestrates, the same convention the research skill uses for its lead. Aligned the reviewer wording from "read-only" to fresh-context reviewers who never touch the build (the QA Engineer runs the validator and tests via Bash; neither holds Write). Historical Changelog entries keep their original terms as append-only record.

### `03.06.01` - 2026-06-28

Reconciled `references/validation.md` with the live agent schema and engine. The Agent and Library check descriptions now use `title` (the role key, equal to the file name) and `name` (the spoken handle), matching `_agent_validate` and the agent files, in place of the retired `name`/`agent-name` terms; the `agents validate` example uses a current agent (Ruth / Fact-Checker) instead of the deleted Marcus/builder crew. Dropped the vestigial requirements-analyst dispatch from Create pipeline step 1 (develop runs requirements itself). Historical Changelog entries keep their original terms as append-only record.

### `03.04.01` - 2026-06-27

Fixed a claude.ai install failure: the skill template manifest shipped as `templates/skill/SKILL.md`, so the packaged bundle carried two files named `SKILL.md` (the real manifest plus the template's placeholder `name: [skill-name]`). The template manifest is renamed `t-SKILL.md`, with a one-line comment recording the rename, so the bundle now ships exactly one `SKILL.md`. Added the class-of-failure guard: `brain.command`'s `_skill_validate` now rejects any skill source that contains a second file named `SKILL.md`. Reconciled `references/validation.md` with the engine: the Skill gate status moves from "built, all four check sets" to "partial" (the lightweight Skill subset is built, the richer checks remain specified), the agent-catalog path is corrected to `System/Data/agent-catalog.json`, and the federation prose is generalized from two homes to all homes. Replaced the dead top-level `Agents/<team>/` token with the federated `<agent-home>/<team>/` form in the Create pipeline and templates, fixed the stale `Inbox/Development/` and dangling `Agents.md` references in the `03.04.00` entry, and re-tensed the Bootstrap "v0" clause. Froze regression case rc-0002.

### `02.01.01` - 2026-06-20

Re-audit pass (independent fresh-context auditor plus a mechanical scan). Fixed three scripts-to-`brain.command` migration leftovers in the crew specs (the builder's scaffold list still named `scripts/`; the reliability-engineer and the `platform-engineering` roster still named `validate.py`), refreshed the namesake doc to describe the `brain.command` and dynamic-review model, and aligned the namesake's `version` with the skill (the namesake now versions with the skill; the template records the rule).
