<!--
title: '🧭 ADR-0003: THE SKILLS LIVE WHERE THE APPS READ THEM'
description: 'The vault keeps its seven skills in .agents/skills/, each faculty with its team inside, draws a copy into .claude/skills/ for Claude Code, and lets a home install of a faculty hand over to the vault''s own copy.'
type: record
keywords: [skills, faculties, agent teams, home kit, claude code]
status: 'Accepted'
date: '2026-10-26'
evidence: 'N/A'
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🧭 ADR-0003: THE SKILLS LIVE WHERE THE APPS READ THEM

<a name="top"></a>

**Every skill sits where an agent app finds it, and a faculty carries its own team.**

_One source in the template, a copy for Claude Code, and a home install that hands over._

</div>

---

## 📋 Meta Information

> [!NOTE]
> **Status**, **Date**, and **Evidence** live in the frontmatter above and feed the
> [ADR index](README.md).

| Attribute     | Specification                                     |
| :------------ | :------------------------------------------------ |
| **Deciders**  | The vault's owner                                 |
| **Consulted** | The AI agent that carried out the change          |
| **Informed**  | Everyone who generates a vault from this template |

---

## 🎯 Context & Problem Statement

The vault's seven skills kept their sources in `System/Skills/.unpackaged/`, and the five faculty
teams they dispatch lived in `Inbox/Faculties/`. No agent app reads either place: Claude Code reads
a repository's skills only from `.claude/skills/`, and Codex, Copilot, Cursor, Gemini and
Antigravity only from `.agents/skills/`. So a session in a vault never listed the skills, the line
in `AGENTS.md` that says to fire them had nothing to fire, and the teams never ran. Four of the
descriptions also held an unquoted colon, which made their frontmatter invalid YAML, so a loader
that found them would have dropped the description that triggers them.

The owner wants tannergolden/intelligence's home kit to install the faculties on their machines,
so that they work in every repository. And other people generate private vaults from this
template, with neither the owner's dotfiles nor the home kit, so a vault has to carry everything
its skills need.

---

## 🚦 Decision Drivers

- **A vault works with nothing installed**, in every agent app, for whoever generated it.
- **One source for each skill**, kept beside the layout it depends on.
- **The home kit can carry the faculties** to every repository on the owner's machines.
- **Inside a vault, the vault's own copy decides**, whichever copy an app loaded.
- **No new delivery machinery**: Template Sync and the home kit already exist.

---

## 🏗️ Considered Options

1. **Keep the layout**, and tell agents in `AGENTS.md` where to find the skills.
2. **Move the faculties into tannergolden/intelligence's kit**, and have Intelligence Sync write
   them into every vault.
3. **Keep the skills in the template, where the apps read them**: sources in `.agents/skills/`
   with each faculty's team inside, a generated `.claude/skills/` copy, vaults kept current by
   Template Sync, a pinned copy in the home kit, and a rule that hands a home copy over to a
   vault's.

---

## ✅ Decision Outcome

**Chosen Option**: Option 3, the skills where the apps read them.

### Rationale for Selection

It is the option in which a vault generated from the template loads its skills in every app with
nothing installed, and it uses only the routes that already exist: a new vault starts with the
skills, and Template Sync brings each later release with the layout it depends on, so a vault's
skills and its folders always come from the same release. The home kit carries a copy pinned to a
release for the owner's other repositories, and because Claude Code prefers a personal skill to a
project's, each faculty opens with a rule that makes the vault's copy win: a copy that finds itself
in a BRAIN vault reads the vault's and follows it. Option 1 leaves triggering to an instruction the
apps never act on. Option 2 widens Intelligence Sync from one block to skill folders in every
vault, and splits a faculty from the vault layout it names.

### What Changed

| Was                                                                | Is now                                                                                                   |
| :----------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------- |
| Skill sources in `System/Skills/.unpackaged/`                      | `.agents/skills/<skill>/`, read by every app but Claude Code                                             |
| No copy for Claude Code                                            | `.claude/skills/`, drawn byte for byte by `update-vault.py` and held to its source by `--check`          |
| The five teams in `Inbox/Faculties/`, a held sub-home of the Inbox | Each in the `agents/` folder of the skill that dispatches it; `Inbox/` holds three sub-homes             |
| A team vendored into the archive at build time                     | A faculty's archive packs its own `agents/`; `board` and `identify` still vendor their AR department     |
| Frontmatter in loose YAML, four descriptions unparseable           | One key to a line, `metadata` as a one-line map, quoted where YAML would misread a value                 |
| `allowed-tools` pre-approving writes, commands and agents          | Read-only tools only; the rest goes through the session's own permissions                                |
| A skill that assumed the vault                                     | A faculty that runs anywhere: the vault's own copy wins inside a vault, and outside one it works in chat |

---

## 📈 Consequence Matrix

| Category         | Impact / Consequence                                                                                                                                                            |
| :--------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Positive (+)** | The skills load in every app, in every vault, for anyone; the home kit can carry the faculties everywhere; a vault's copy and layout never drift apart                          |
| **Negative (-)** | The teams leave the tree Obsidian shows; each skill file is kept twice, once as its generated copy; a vault takes new skills only when its owner runs Template Sync             |
| **Neutral (~)**  | The move renames every skill and team file a vault holds, so the release that carries it is a new major; ADR-0002's removal of `.claude/` now admits one generated folder in it |

---

## ⚖️ Trade-off Comparative

### Option 1: Keep The Layout

- ✅ Nothing moves.
- ❌ No app lists a skill it cannot find, so the skills keep never triggering.

### Option 2: Deliver From The Hub

- ✅ Every vault takes a new faculty every week, with no Template Sync run.
- ❌ Intelligence Sync writes skill folders into every vault, and a faculty updates apart from the
  vault layout it depends on.

---

## 🔗 Traceability & Links

- [Skills](../../System/Skills/Skills.md): the layout, the hand-over and how to keep a skill of
  your own
- `.github/scripts/check-skills.py` and `.github/scripts/update-vault.py`: the check and the copy
- [ADR-0002](ADR-0002-Notes-Take-The-Hidden-Frontmatter.md), whose removal of `.claude/` this
  narrows to one generated folder
- tannergolden/intelligence keeps the pinned copy of the five faculties for its home kit

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the
> [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md).
> If you rename or move a file, update every reference to it across the repository to prevent link
> drift.

---

<div align="center">

**Where the apps look, with the team inside.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
