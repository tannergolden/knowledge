<!--
title: '🧭 ADR-0005: EACH FOLDER EXPLAINS ITSELF IN A README'
description: 'Every folder explains itself in a README.md at its root, written for anyone, which is also its note, and the root README.md says how to work in the vault; the vault holds no AI instructions, so AGENTS.md and the Intelligence Sync stub are gone.'
type: record
keywords: [readme, folder notes, governance, documentation, agents-md]
status: 'Accepted'
date: '2026-11-07'
evidence: 'N/A'
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🧭 ADR-0005: EACH FOLDER EXPLAINS ITSELF IN A README

<a name="top"></a>

**Every folder explains itself in a README written for anyone, and the vault holds no AI instructions.**

_One description per folder, where every reader looks first._

</div>

---

## 📋 Meta Information

> [!NOTE]
> **Status**, **Date**, and **Evidence** live in the frontmatter above and feed the
> [ADR index](README.md). This record supersedes
> [ADR-0001](ADR-0001-AGENTS-Holds-The-Vaults-Rules.md).

> [!IMPORTANT]
> **Amended** by [ADR-0006](ADR-0006-AGENTS-Returns-With-The-Rules-For-Personal-Knowledge.md) on
> 2026-11-07: `AGENTS.md` and its Intelligence Sync stub return, with the universal rules and the
> rules every AI follows in a personal knowledge vault. Each folder still explains itself in its
> `README.md`, written for anyone. The record below is kept as it was decided.

| Attribute      | Specification                                                                                          |
| :------------- | :----------------------------------------------------------------------------------------------------- |
| **Deciders**   | The vault's owner                                                                                      |
| **Consulted**  | The AI agent that carried out the change                                                               |
| **Informed**   | Everyone who generates a vault from this template                                                      |
| **Amended by** | [ADR-0006](ADR-0006-AGENTS-Returns-With-The-Rules-For-Personal-Knowledge.md), for its `AGENTS.md` part |

---

## 🎯 Context & Problem Statement

Under ADR-0001, `AGENTS.md` held the universal Constitution, synced into it by 🔁 Intelligence Sync,
and then the vault's own rules. Each of 129 folders explained itself in a note named after it, such
as `Memory/Memory.md`, opening with a Rules section addressed to an agent ("before you create, edit,
move or delete anything...", "your user"). Only the seven top folders carried a `README.md`, their
GitHub page, which repeated the note's purpose and pointed to it, and the 18 template folders had
neither.

So every top folder had two descriptions that drifted apart, and every deeper folder's description
sat in a file no reader opens first: GitHub, an editor and a person all look for a folder's README. A
person reading the rules read instructions written for someone else. And once ADR-0004 moved the
skills to the home kit, which also installs the universal rules on every machine, `AGENTS.md` kept a
second copy of those rules here, which Intelligence Sync proposed to update every week.

The owner decided on 2026-11-07 that the knowledge repository holds no AI instructions and no agents:
each folder has a README at its root that explains the folder's purpose and how to work in it,
written for anyone, a person or any AI, rather than as directives to an agent.

---

## 🚦 Decision Drivers

- **One description per folder**, in the file every reader opens first.
- **Written for anyone.** The same pages serve a person, an editor and any AI, with every real rule
  kept and only the audience changed.
- **No AI instructions in the vault.** The universal rules come with the home kit, outside the
  repository.
- **The checks keep holding.** Every rule a script enforced still holds in the new layout, none
  weakened.
- **Nothing lost.** Each note's frontmatter, purpose, procedures and generated lists move with it.

---

## 🏗️ Considered Options

1. **Keep ADR-0001's layout**: `AGENTS.md`, a note named after each folder, and a README for the top
   folders only.
2. **Keep the folder notes and drop `AGENTS.md`**, moving its rules to the front page,
   `.github/README.md`.
3. **Make each folder's `README.md` its note**: rename every folder note to `README.md`, merge the
   seven top folders' two files into one, give each template folder a README, move the vault's rules
   to a root `README.md` written for anyone, and delete `AGENTS.md` and the Intelligence Sync stub.

---

## ✅ Decision Outcome

**Chosen Option**: Option 3, each folder explains itself in a README.

### Rationale for Selection

It is the only option with one description per folder, and it puts that description where every
reader already looks. Option 1 keeps the drift and the agent-only voice. Option 2 removes the
instruction file but keeps each folder's description in a file only the vault's own tooling knows to
open, and overloads the front page, which 🔄 Template Sync keeps current as the template's landing
page. A README at every folder's root is the convention GitHub, editors and people already follow,
so the vault needs no file addressed to any one AI.

### What Changed

| Was                                                                                           | Is now                                                                                                                                              |
| :-------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AGENTS.md`: the universal Constitution, then the vault's rules                               | The universal rules reach each session from the home kit; the vault's rules, rewritten for anyone, are the root `README.md`                         |
| 🔁 Intelligence Sync, `.github/workflows/intelligence-sync.yml`, on the sync list             | Gone from the template, its list and its derivation; the `no-intelligence` topic keeps the hub's sync away                                          |
| A note named after each of 129 folders (`Memory/Memory.md`)                                   | That folder's `README.md`: 122 renamed, and 7 merged with the top folders' READMEs                                                                  |
| No note in the 18 template folders                                                            | A README in each: written for the copy where the folder is copied whole (a venture, its departments, a project), explaining the scaffolds elsewhere |
| Rules addressed to an agent                                                                   | Documentation for anyone: purpose, what belongs, how to name and file things, what not to do, and how the checks enforce it                         |
| `lint-notes.py` failed a `README.md` outside the seven top folders                            | It fails a note named after its folder, the second copy that rule guarded against                                                                   |
| A folder note was the note named after its folder, for `check-links.py` and `update-vault.py` | It is the folder's `README.md`; a link to a folder is `[[Library/README\|Library]]`, and the generated lists draw into READMEs                      |
| `session.py start` cited `AGENTS.md`                                                          | It lists the root `README.md` first, and `Inbox/README.md` when files wait                                                                          |
| `AGENTS.md`, Where the skills write                                                           | The root `README.md`, Where Each Kind Of Work Goes, and each destination folder's own README                                                        |

ADR-0004 stands: the skills live in the home kit. Only the page that gives them the vault's layout
has moved, from `AGENTS.md` to the root `README.md`.

---

## 📈 Consequence Matrix

| Category         | Impact / Consequence                                                                                                                                                                                |
| :--------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Positive (+)** | One description per folder, shown where every reader looks; the vault reads the same to a person and to any AI; no weekly sync pull request; the checks hold the new layout                         |
| **Negative (-)** | A link to a folder names its README and an alias, which is longer; GitHub shows a README's wikilinks as raw text; an existing vault takes manual steps, and the renames ship in a new major release |
| **Neutral (~)**  | ADR-0001 is superseded; ADR-0002's note format now covers every README of the vault's folders; the root `README.md` is a page, not a note, as `AGENTS.md` was                                       |

---

## ⚖️ Trade-off Comparative

### Option 1: Keep ADR-0001's Layout

- ✅ Nothing moves, and no vault takes manual steps.
- ❌ Two drifting descriptions of each top folder, rules written to an agent, and a second copy of the
  universal rules kept current by a weekly sync.

### Option 2: Keep The Folder Notes, Drop AGENTS.md

- ✅ The vault holds no instruction file, and no note is renamed.
- ❌ Each folder's description stays where no reader looks first, and the front page carries what
  belongs to every folder.

---

## 🔗 Traceability & Links

- [ADR-0001](ADR-0001-AGENTS-Holds-The-Vaults-Rules.md), which this supersedes
- [ADR-0004](ADR-0004-The-Skills-Live-In-The-Home-Kit.md), whose layout section moves to the root
  `README.md`
- The root [`README.md`](../../README.md): how to work in the vault, and where each kind of work goes
- [Link Topology](../technical/vault/Link-Topology.md) and [Note Schema](../technical/vault/Note-Schema.md):
  a folder's README as its note and its hub
- [Moving A Vault To Folder READMEs](../distribution/How-A-Change-Reaches-A-Vault.md#-moving-a-vault-to-folder-readmes):
  the steps for a vault made before this change

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the
> [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md).
> If you rename or move a file, update every reference to it across the repository to prevent link
> drift.

---

<div align="center">

**Each folder says what it is, to whoever opens it.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
