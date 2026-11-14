<!--
title: '🧭 ADR-0009: THE WORKFORCE FILES BY THE VAULT''S PAGES'
description: 'tannergolden/intelligence adds an AI workforce whose Knowledge Vault Manager alone writes the vault, so the vault names it in its own pages: AGENTS.md and the root README say how a record reaches the vault, Ventures/README.md names the seat that keeps each venture file, and the folders it sorts, interviews or files in point to it. Read it before changing how the workforce is described here.'
type: record
keywords: [knowledge vault manager, chief of staff, records, departments, ventures, agents]
status: 'Proposed'
date: '2026-11-14'
evidence: 'N/A'
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🧭 ADR-0009: THE WORKFORCE FILES BY THE VAULT'S PAGES

<a name="top"></a>

**The vault names the workforce that can work in it, and keeps the one say over where its records land.**

_One writer, filing by the vault's own pages._

</div>

---

## 📋 Meta Information

> [!NOTE]
> **Status**, **Date**, and **Evidence** live in the frontmatter above and feed the
> [ADR index](README.md). This record adds to
> [ADR-0008](ADR-0008-The-Vault-Relies-On-No-Skills.md) and supersedes nothing: the vault still
> relies on no skills.

| Attribute     | Specification                                     |
| :------------ | :------------------------------------------------ |
| **Deciders**  | The vault's owner                                 |
| **Consulted** | The AI agent that carried out the change          |
| **Informed**  | Everyone who generates a vault from this template |

---

## 🎯 Context & Problem Statement

Under ADR-0008 the vault named its twelve departments and the work each covers, and nothing did that
work but whoever worked in the vault. On 2026-11-14 tannergolden/intelligence added an AI workforce
in `workforce/`, beside its home kit
([ADR-0044](https://github.com/tannergolden/intelligence/blob/Development/docs/adrs/ADR-0044-The-Workforce-Lives-Beside-The-Kit.md)):
a Chief of Staff who routes every request, a Knowledge Vault Manager that alone writes the owner's
vault, and a team for each department, in folders named as the venture template's are. Each
department's charter says where its records land, by the vault's `AGENTS.md` and the README of the
folder they land in.

The vault said nothing of it. `AGENTS.md` and the root `README.md` said the vault holds no agents,
no page said that one agent writes for the rest, and no venture page said which seat keeps which
file. The Knowledge Vault Manager reads `AGENTS.md`, the root `README.md` and each folder's README
before it writes, so those pages are where it has to learn where a record goes.

---

## 🚦 Decision Drivers

- **The vault decides where things go**: a record lands where this vault's pages say, whoever sends
  it, and the workforce's charters follow them.
- **The writer learns it from the pages it reads first**: `AGENTS.md`, the root `README.md` and the
  README of each folder it writes into.
- **One home for each fact**: the map of who keeps each venture file is written once, not in every
  department's README.
- **Nothing changes for a vault without the workforce**: every home, rule and check stands.

---

## 🏗️ Considered Options

1. **Say nothing**, and leave the Knowledge Vault Manager to infer the homes from the charters.
2. **Name the workforce in the vault's pages**: say how a record reaches the vault and who writes
   it, map each venture file to the seat that keeps it once, and point to that from the folders it
   touches.
3. **Copy the workforce's charters into the vault**, so the vault carries its own copy of who owns
   what.

---

## ✅ Decision Outcome

**Chosen Option**: Option 2, the workforce named in the vault's own pages.

### Rationale for Selection

The Knowledge Vault Manager already reads these pages before every write, so naming the workforce
there puts the homes where it looks, and keeps the vault the authority over its own layout. Option 1
leaves the one agent that writes the vault to work out its rules from another repository, and lets
the two drift unseen. Option 3 brings agent files back into a vault that holds none (ADR-0004,
ADR-0008), and makes a second copy of who owns what to keep in step.

### What Changed

| Was                                                                                  | Is now                                                                                                                         |
| :----------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| `AGENTS.md`, Departments: the twelve departments, and no skill for any of them        | The same, and the workforce: only the Knowledge Vault Manager writes, a record names its venture, and every rule binds every agent |
| The root `README.md` said the vault holds no agents                                   | It says where the workforce lives, and When The Workforce Works Here says how a record reaches the vault                       |
| No page named who keeps a venture file                                                | `Ventures/README.md`, Who Keeps Each File, names the seat for each file, and each venture README points to it                  |
| `Inbox/README.md`, `Profile/README.md` and `Library/README.md` named no agent         | Each says what the workforce does there: the sort, the profile interview and the Library's holdings                           |
| `System/Workflows.md` had no workforce row                                            | It maps the filing of a workforce record                                                                                       |
| The glossary, How The Vault Works and Setting Up A Vault did not name the workforce   | They define it, its Chief of Staff and its Knowledge Vault Manager, and say how to set it up                                   |

---

## 📈 Consequence Matrix

| Category         | Impact / Consequence                                                                                                                                                                                       |
| :--------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Positive (+)** | The Knowledge Vault Manager finds every home in the pages it reads first, and the vault stays the one authority over where its records land                                                                 |
| **Negative (-)** | Who Keeps Each File names the workforce's seats, so a seat renamed or moved in tannergolden/intelligence needs an edit here; a venture copied before this change lacks the pointer in its own READMEs, and needs none, since `Ventures/README.md` holds the table |
| **Neutral (~)**  | ADR-0008 stands: the vault relies on no skills and holds no agents; the layout, the checks and the note schema are unchanged                                                                                |

---

## ⚖️ Trade-off Comparative

### Option 1: Say Nothing

- ✅ Nothing to keep in step with the workforce.
- ❌ The vault's one writer learns its homes from charters in another repository, and nothing shows
  when the two disagree.

### Option 3: Copy The Charters Into The Vault

- ✅ Every department's ownership sits beside the folders it covers.
- ❌ Agent files return to a vault that holds none, and a second copy of who owns what drifts from
  the first.

---

## 🔗 Traceability & Links

- tannergolden/intelligence's
  [ADR-0044](https://github.com/tannergolden/intelligence/blob/Development/docs/adrs/ADR-0044-The-Workforce-Lives-Beside-The-Kit.md)
  and its [`workforce/`](https://github.com/tannergolden/intelligence/tree/Development/workforce)
- [ADR-0008](ADR-0008-The-Vault-Relies-On-No-Skills.md), which this adds to
- [`AGENTS.md`](../../AGENTS.md), Departments, and the root [`README.md`](../../README.md), When The
  Workforce Works Here
- [`Ventures/README.md`](../../Ventures/README.md), Who Keeps Each File

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the
> [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md).
> If you rename or move a file, update every reference to it across the repository to prevent link
> drift.

---

<div align="center">

**The workforce does the work; the vault says where it lands.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
