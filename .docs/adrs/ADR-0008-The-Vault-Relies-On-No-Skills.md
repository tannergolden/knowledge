<!--
title: '🧭 ADR-0008: THE VAULT RELIES ON NO SKILLS'
description: 'tannergolden/intelligence ships no skills since its ADR-0041, so the vault stops naming the twelve department skills: its pages name the twelve departments and the work each covers, the profile interview is the one Profile/README.md describes, and nothing tells an AI or the owner to install or use a skill.'
type: record
keywords: [departments, home kit, profile interview, agents-md, kinds of work, ventures]
status: 'Proposed'
date: '2026-11-14'
evidence: 'N/A'
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🧭 ADR-0008: THE VAULT RELIES ON NO SKILLS

<a name="top"></a>

**The vault names its twelve departments and the work each covers, never a skill to install.**

_A page points only at what exists._

</div>

---

## 📋 Meta Information

> [!NOTE]
> **Status**, **Date**, and **Evidence** live in the frontmatter above and feed the
> [ADR index](README.md). This record supersedes
> [ADR-0004](ADR-0004-The-Skills-Live-In-The-Home-Kit.md).

| Attribute     | Specification                                     |
| :------------ | :------------------------------------------------ |
| **Deciders**  | The vault's owner                                 |
| **Consulted** | The AI agent that carried out the change          |
| **Informed**  | Everyone who generates a vault from this template |

---

## 🎯 Context & Problem Statement

Under ADR-0004 the vault held no skills and relied on twelve department skills, from
`administration` to `public-relations`, that tannergolden/intelligence kept in `kit/skills/` and its
home kit installed. `AGENTS.md` listed them under Skills and told an AI to use the one whose
description matched the request. The root `README.md`, under Where Each Kind Of Work Goes, routed
work by skill. Each folder's README and each file of the venture template named the skill whose
work lands there, down to the `administration` skill's Chief Executive Officer and the
`finance-and-accounting` skill's Chief Financial Officer. The profile interview was the
`human-resources` skill's, and two prompts sent a stale report or visual through a skill.

On 2026-11-14 the hub decided, in its
[ADR-0041](https://github.com/tannergolden/intelligence/blob/Development/docs/adrs/ADR-0041-The-Kit-Carries-No-Skills.md),
to write no skills: `kit/skills/` is gone, the kit carries the guard alone, and every install takes
out the skills earlier releases wrote. Its `v0.9.0` tag keeps each skill as it last shipped. From
then on the vault told every AI and its owner to use skills that no release installs.

---

## 🚦 Decision Drivers

- **Nothing points at what does not exist**: no page tells an AI or the owner to install, use or
  rely on a skill.
- **The layout stays**: the twelve departments still organize a venture and the owner's own life,
  and every kind of work keeps its home.
- **No new machinery**: the vault says in its own pages how its work is done, and nothing replaces
  the skills.
- **Records stay as decided**: ADR-0003, ADR-0004 and ADR-0006 keep their text.

---

## 🏗️ Considered Options

1. **Keep naming the skills**, for whoever still runs a copy from the hub's `v0.9.0` tag.
2. **Name the departments instead of the skills**, keeping every home and every rule, and point the
   profile interview at `Profile/README.md`, which already describes it.
3. **Drop the departments with the skills**, and route work by folder alone.

---

## ✅ Decision Outcome

**Chosen Option**: Option 2, the departments in place of the skills.

### Rationale for Selection

The departments never depended on the skills: a venture has a folder for each, and each folder's
README already says what lands there and by what rules. Option 2 changes the words, not the
layout, so every home, rule and check stands, and the vault reads the same to an AI with skills of
its own or none. Option 1 sends every AI and owner after skills no release installs, and leaves the
vault's guidance out of step with the hub's. Option 3 throws away the venture template's twelve
folders and the routing every folder's README is written around, to fix what is only a matter of
names.

### What Changed

| Was                                                                                                                      | Is now                                                                                                                |
| :----------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `AGENTS.md`, Skills: twelve skills from the home kit, and the one whose description matches the request                  | `AGENTS.md`, Departments: the twelve departments, no skill from this repository or the home kit, and where work lands |
| The root `README.md`, Where Each Kind Of Work Goes, by skill                                                             | The same table, by department                                                                                         |
| Each venture README and copied note named the skill that keeps it, and that skill's Chief Executive or Financial Officer | Each names the department that keeps it, and the company's own Chief Executive or Financial Officer                   |
| The profile interview was the `human-resources` skill's, installed by the home kit                                       | It is the interview `Profile/README.md` describes, which any AI assistant working here runs when the owner asks       |
| Two prompts sent a stale report through the `research-and-development` skill and a stale visual through another          | They say what to do without a skill                                                                                   |
| The home kit was described as installing every skill with the universal rules                                            | It is described as installing the universal rules and their guard, and no skill                                       |
| The idea pool's discovery method was defined with the `research-and-development` skill                                   | It last shipped in that skill, kept at the hub's `v0.9.0` tag, and no later release carries it                        |

---

## 📈 Consequence Matrix

| Category         | Impact / Consequence                                                                                                                                                                                       |
| :--------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Positive (+)** | No page tells an AI or the owner to use a skill that no release installs; the vault says how its work is done in its own words, the same to any AI app                                                     |
| **Negative (-)** | The discovery method's scoring and gates are kept current nowhere, only at the hub's `v0.9.0` tag; a venture copied before this change keeps the skill names in its own files until its owner updates them |
| **Neutral (~)**  | ADR-0004 is superseded; ADR-0003 and ADR-0006 stand as records; the layout, the checks and the note schema are unchanged                                                                                   |

---

## ⚖️ Trade-off Comparative

### Option 1: Keep Naming The Skills

- ✅ Nothing to rewrite, and a copy kept from the hub's `v0.9.0` tag still finds its name.
- ❌ Every page points at skills no release installs, and the vault drifts from the hub.

### Option 3: Drop The Departments With The Skills

- ✅ No department names left to keep in step with anything.
- ❌ The venture template's folders and the routing every README is written around go too, for a
  change of names alone.

---

## 🔗 Traceability & Links

- tannergolden/intelligence's
  [ADR-0041](https://github.com/tannergolden/intelligence/blob/Development/docs/adrs/ADR-0041-The-Kit-Carries-No-Skills.md):
  the hub writes no skills
- [ADR-0004](ADR-0004-The-Skills-Live-In-The-Home-Kit.md), which this supersedes
- [`AGENTS.md`](../../AGENTS.md), Departments, and the root [`README.md`](../../README.md), Where
  Each Kind Of Work Goes
- [`Profile/README.md`](../../Profile/README.md), Filling These Files: The Profile Interview
- [Updating A Venture Copied Before The Skills Left](../distribution/How-A-Change-Reaches-A-Vault.md#-updating-a-venture-copied-before-the-skills-left):
  the step for a venture made before this change

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the
> [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md).
> If you rename or move a file, update every reference to it across the repository to prevent link
> drift.

---

<div align="center">

**The departments organize the work; no skill is needed to do it.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
