<!--
title: '🧭 ADR-0006: AGENTS.MD RETURNS WITH THE RULES FOR PERSONAL KNOWLEDGE'
description: 'AGENTS.md returns at the vault root, with the universal rules kept current by Intelligence Sync and then the rules every AI follows in a personal knowledge vault, so every vault generated from the template starts with them; each folder still explains itself in its README, written for anyone.'
type: record
keywords: [agents-md, ai-agents, governance, personal knowledge, intelligence sync]
status: 'Accepted'
date: '2026-11-07'
evidence: 'N/A'
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🧭 ADR-0006: AGENTS.MD RETURNS WITH THE RULES FOR PERSONAL KNOWLEDGE

<a name="top"></a>

**Every AI that opens a vault starts with the rules, in whatever app it runs.**

_The READMEs for anyone, AGENTS.md for every AI._

</div>

---

## 📋 Meta Information

> [!NOTE]
> **Status**, **Date**, and **Evidence** live in the frontmatter above and feed the
> [ADR index](README.md). This record amends
> [ADR-0005](ADR-0005-Each-Folder-Explains-Itself-In-A-README.md).

| Attribute     | Specification                                                                             |
| :------------ | :---------------------------------------------------------------------------------------- |
| **Deciders**  | The vault's owner                                                                         |
| **Consulted** | The AI agent that carried out the change                                                  |
| **Informed**  | Everyone who generates a vault from this template                                         |
| **Amends**    | [ADR-0005](ADR-0005-Each-Folder-Explains-Itself-In-A-README.md), for its `AGENTS.md` part |

---

## 🎯 Context & Problem Statement

Under ADR-0005 the vault held no AI instructions: each folder explained itself in a `README.md`,
written for anyone, and the universal rules reached an AI only through the home kit installed from
tannergolden/intelligence on each machine.

A vault is worked in by AIs the kit never reaches: an agent that works on GitHub, the Grok Bot Chief
of Staff that reads the vault through its GitHub connection, an app on a machine without the kit, or
a new owner's first session before the kit is installed. Each of those started with no rules at all.
Nothing it loaded told it to keep the owner's context private, to mark an inference unconfirmed, to
read a folder's README before writing there, or to wait for the owner's yes before deleting a file.
The READMEs say all of it, but an AI has to know to look for them first.

The owner decided on 2026-11-07 to add `AGENTS.md` back, holding every rule an AI needs to work in a
personal knowledge vault, so that every vault generated from the template starts with the best
setup.

---

## 🚦 Decision Drivers

- **Every AI starts with the rules**, whatever app it runs in, with or without the home kit.
- **Every vault has them from its first commit**, and keeps them current without its owner's work.
- **The READMEs stay written for anyone.** ADR-0005's one description per folder stands.
- **Each rule has one home.** `AGENTS.md` holds an AI to the READMEs, and repeats only what every
  session needs before it opens them.

---

## 🏗️ Considered Options

1. **Keep ADR-0005**: no `AGENTS.md`, and the universal rules from the home kit alone.
2. **`AGENTS.md` with the vault's rules only**, and no universal block.
3. **`AGENTS.md` with the universal block**, kept current by 🔁 Intelligence Sync, and the rules
   every AI follows in a personal knowledge vault below it.

---

## ✅ Decision Outcome

**Chosen Option**: Option 3, `AGENTS.md` with the universal block and the vault's rules.

### Rationale for Selection

`AGENTS.md` is the file most AI apps load by themselves, so it is the one place a rule reaches every
AI before it acts. The universal block makes the vault's copy whole where the kit is not installed,
and the stub keeps it current. Option 2 leaves an AI without the kit with no rule on credentials,
pushing or deleting; Option 1 leaves it with no rule at all.

### What Changed

| Was                                                          | Is now                                                                                                                                                                                                            |
| :----------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| No `AGENTS.md`; the universal rules from the home kit alone  | `AGENTS.md` at the root: the hub's `INTELLIGENCE` block, then Start here, Working with personal knowledge, Skills, Commands, Definition of done, Conventions, Where things live, Gotchas, Ask first and Overrides |
| No Intelligence Sync stub, and the `no-intelligence` topic   | `.github/workflows/intelligence-sync.yml`, each vault's own, which proposes each release's block as a pull request; no topic                                                                                      |
| `.github/template-sync` named no `AGENTS.md`                 | `/AGENTS.md` kept current in every vault, merged with what its owner adds, and the stub under The vault: yours                                                                                                    |
| `vault.py` passed over the root `README.md` alone            | It passes over both root pages, `README.md` and `AGENTS.md`                                                                                                                                                       |
| The hub's sync would add a `docs/Prompts.md` beside `.docs/` | tannergolden/intelligence counts `.docs/Prompts.md`, where a vault keeps its prompts, as the page, from its next release                                                                                          |
| The pages said the vault holds no AI instructions            | The root `README.md`, the front page, How The Vault Works, Setting Up A Vault, the Glossary, How A Change Reaches A Vault and `System/README.md` name `AGENTS.md` and its place in the order rules win            |

`AGENTS.md` overrides two universal Defaults, under its Overrides: WORK-001, so keeping the vault
current is part of every task, and STD-001, since the vault keeps its docs in `.docs/`.

ADR-0005 stands otherwise: each folder explains itself in its `README.md`, written for anyone, and
the root `README.md` says how to work in the vault. ADR-0004 stands: the vault holds no skills and
no agents.

---

## 📈 Consequence Matrix

| Category         | Impact / Consequence                                                                                                                                                                                         |
| :--------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Positive (+)** | Every AI that opens a vault, in any app, starts with the universal rules and the rules for personal knowledge; every vault generated from the template has them from its first commit and keeps them current |
| **Negative (-)** | A pull request for each release of the universal rules; a second copy of them where the home kit is installed too; the session steps in both `AGENTS.md` and the root `README.md`, which change together     |
| **Neutral (~)**  | ADR-0005 is amended, not superseded; `AGENTS.md` is a page, not a note, as the root `README.md` is                                                                                                           |

---

## ⚖️ Trade-off Comparative

### Option 1: Keep ADR-0005

- ✅ One copy of the universal rules, and no sync pull requests.
- ❌ An AI the kit does not reach starts with no rules.

### Option 2: AGENTS.md Without The Universal Block

- ✅ No sync pull requests.
- ❌ Without the kit, no Invariant reaches the AI: nothing on credentials, pushing or deleting.

---

## 🔗 Traceability & Links

- [ADR-0005](ADR-0005-Each-Folder-Explains-Itself-In-A-README.md), which this amends
- [ADR-0001](ADR-0001-AGENTS-Holds-The-Vaults-Rules.md), whose root file for agents returns
- [ADR-0004](ADR-0004-The-Skills-Live-In-The-Home-Kit.md): the skills live in the home kit
- [`AGENTS.md`](../../AGENTS.md): the rules every AI follows here
- [How A Change Reaches A Vault](../distribution/How-A-Change-Reaches-A-Vault.md): the road the
  universal rules take, and the steps for a vault made before the folder READMEs

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the
> [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md).
> If you rename or move a file, update every reference to it across the repository to prevent link
> drift.

---

<div align="center">

**The rules travel with the vault, to every AI that opens it.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
