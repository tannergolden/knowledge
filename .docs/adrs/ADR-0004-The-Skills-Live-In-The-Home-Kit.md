<!--
title: '🧭 ADR-0004: THE SKILLS LIVE IN THE HOME KIT'
description: 'The vault holds no skills or agents: every skill and its team live in tannergolden/intelligence and arrive through the home kit, and AGENTS.md gives the universal skills the vault''s layout.'
type: record
keywords: [skills, agent teams, home kit, agents-md, universal skills]
status: 'Accepted'
date: '2026-11-07'
evidence: 'N/A'
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🧭 ADR-0004: THE SKILLS LIVE IN THE HOME KIT

<a name="top"></a>

**No skill or agent lives in the vault: the home kit brings them, and AGENTS.md shows them where to write.**

_One copy of each skill, universal, and a vault that holds only notes and the scripts that check them._

</div>

---

## 📋 Meta Information

> [!NOTE]
> **Status**, **Date**, and **Evidence** live in the frontmatter above and feed the
> [ADR index](README.md). This record supersedes
> [ADR-0003](ADR-0003-The-Skills-Live-Where-The-Apps-Read-Them.md).

| Attribute     | Specification                                     |
| :------------ | :------------------------------------------------ |
| **Deciders**  | The vault's owner                                 |
| **Consulted** | The AI agent that carried out the change          |
| **Informed**  | Everyone who generates a vault from this template |

---

## 🎯 Context & Problem Statement

Under ADR-0003 the vault kept its seven skills in `.agents/skills/`, drew a copy into
`.claude/skills/` and an archive into `System/Skills/`, kept the venture workforce in
`Ventures/Agent Resources (AR)/` and the Librarian in `Library/`, and listed every agent in
`System/Data/agent-catalog.json`. tannergolden/intelligence carried another copy, pinned to a
release of this template, and each faculty opened with a rule that handed over to the vault's copy.
So every skill existed four times, two checks and three generator steps kept the copies in step, and
the skills named the vault's paths, so outside a vault they only half worked.

The owner decided on 2026-11-07 that this repository holds no agent instruction files. Every skill
and agent spec moves to tannergolden/intelligence under `kit/skills/` and is made universal: it works
in any repository, or in a conversation with no repository.

---

## 🚦 Decision Drivers

- **One copy of each skill**, versioned where it is built.
- **A skill works anywhere**, in a vault, in another repository, or with none.
- **The vault keeps what is the vault's**: its notes, its layout and the scripts that check them.
- **No new delivery machinery**: the home kit already installs into each AI app's skills folder on
  every machine and in every Claude Code cloud session.

---

## 🏗️ Considered Options

1. **Keep ADR-0003's layout**: the skills in the vault, a copy for Claude Code, a pinned copy in the
   home kit.
2. **Move the skills to tannergolden/intelligence as they are**, still naming the vault's paths.
3. **Move the skills to tannergolden/intelligence and make them universal**, and let each
   repository's `AGENTS.md` give them its layout.

---

## ✅ Decision Outcome

**Chosen Option**: Option 3, universal skills in the home kit.

### Rationale for Selection

It leaves one copy of each skill, in the repository that builds and versions it, delivered by the
route that already reaches every app on every machine. A universal skill reads the repository's own
instructions before it writes, so the vault keeps its layout in one place, `AGENTS.md`, under Where
the skills write, and the same skill writes nothing into a repository that does not ask it to.
Option 1 keeps four copies and the machinery that holds them together. Option 2 moves the copies but
leaves every other repository a skill that writes to folders it does not have.

### What Changed

| Was                                                                                          | Is now                                                                                                           |
| :------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------- |
| Seven skills in `.agents/skills/`, a copy in `.claude/skills/`, archives in `System/Skills/` | None in the vault: every skill, `develop` included, in tannergolden/intelligence's `kit/skills/`                 |
| The venture workforce in `Ventures/Agent Resources (AR)/`                                    | The `board` skill's own team, in its `agents/` folder, at most six agents a department                           |
| The Librarian in `Library/`                                                                  | A seat on the `research` skill's team                                                                            |
| `System/Data/agent-catalog.json`                                                             | Gone: `System/Data/` holds the note catalog alone                                                                |
| `check-skills.py`, `check-agents.py`, and the archives, copy and agent catalog steps         | Gone: `check-vault.py` runs four checks, and `update-vault.py` draws four parts                                  |
| Skills that named the vault's paths, with a rule that handed over to the vault's copy        | Universal skills that read the repository's instructions; `AGENTS.md`, Where the skills write, gives the vault's |
| A copy of the faculties in the home kit, pinned to a release of this template                | The home kit's own skills, with nothing pinned here                                                              |

---

## 📈 Consequence Matrix

| Category         | Impact / Consequence                                                                                                                                                                               |
| :--------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Positive (+)** | One copy of each skill; the skills work in every repository and none; the vault's checks shrink to notes, links, personal data and generated parts                                                 |
| **Negative (-)** | A vault without the home kit has no skills; a skill changes when its owner updates the kit, not with Template Sync, so `AGENTS.md`, Where the skills write, has to keep up with the vault's layout |
| **Neutral (~)**  | ADR-0003 is superseded, and ADR-0002's removal of `.claude/` holds in full again; a vault made before this change takes the steps in How A Change Reaches A Vault                                  |

---

## ⚖️ Trade-off Comparative

### Option 1: Keep ADR-0003's Layout

- ✅ Nothing moves, and a vault works with nothing installed.
- ❌ Four copies of every skill, and the checks and generators that keep them in step.

### Option 2: Move The Skills As They Are

- ✅ One copy of each skill.
- ❌ Every repository but a vault gets skills that write to folders it does not have.

---

## 🔗 Traceability & Links

- [ADR-0003](ADR-0003-The-Skills-Live-Where-The-Apps-Read-Them.md), which this supersedes
- `AGENTS.md`, Where the skills write: the vault's layout for the universal skills, now in the root
  [`README.md`](../../README.md), Where Each Kind Of Work Goes
  ([ADR-0005](ADR-0005-Each-Folder-Explains-Itself-In-A-README.md))
- [Moving A Vault Off Its Own Skills](../distribution/How-A-Change-Reaches-A-Vault.md#-moving-a-vault-off-its-own-skills):
  the steps for a vault made before this change
- tannergolden/intelligence, `kit/skills/`: every skill and its team, and the home kit that installs
  them

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the
> [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md).
> If you rename or move a file, update every reference to it across the repository to prevent link
> drift.

---

<div align="center">

**One home for each skill, and the vault tells it where to write.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
