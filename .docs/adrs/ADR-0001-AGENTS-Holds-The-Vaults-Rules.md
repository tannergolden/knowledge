<!--
title: '🧭 ADR-0001: AGENTS.MD HOLDS THE VAULT''S RULES'
description: 'The vault''s Constitution and Instructions dissolve into AGENTS.md, the folder notes and reference pages, and standards owns every repository convention.'
type: record
keywords: [governance]
status: 'Accepted'
date: '2026-10-19'
evidence: 'N/A'
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🧭 ADR-0001: AGENTS.MD HOLDS THE VAULT'S RULES

<a name="top"></a>

**The Constitution and Instructions dissolve into AGENTS.md, the folder notes and reference pages.**

_One root file for agents, each folder's rules where its work happens._

</div>

---

## 📋 Meta Information

> [!NOTE]
> **Status**, **Date**, and **Evidence** live in the frontmatter above and feed the
> [ADR index](README.md).

| Attribute     | Specification                                     |
| :------------ | :------------------------------------------------ |
| **Deciders**  | The vault's owner                                 |
| **Consulted** | The AI agent that carried out the restructure     |
| **Informed**  | Everyone who generates a vault from this template |

---

## 🎯 Context & Problem Statement

The vault was governed by four root files: `Constitution.md` (60 KB), `Instructions.md` (50 KB),
`Information.md` and a `CLAUDE.md` shim, plus three hook digests injected at session start. An
agent read about 130 KB of rules before doing anything, the rules most likely to be forgotten sat
in the middle of that context, and the same rules lived in up to three places.

Much of it was not the vault's to define. Universal agent rules (privacy, honest reporting,
minimal changes, no em dashes, plain words, 12-hour time) now come from the Constitution that
`tannergolden/intelligence` delivers into every repository's `AGENTS.md`, and repository
conventions (commits, branches, releases, document styling, secrets) belong to
`tannergolden/standards`. The template was also marked proprietary while public.

---

## 🚦 Decision Drivers

- **One root file for agents.** `AGENTS.md` is read natively by Claude Code and by every other
  agent that follows the AGENTS.md standard, so it is the only root instruction file.
- **Rules where the work happens.** A folder's rules load when work reaches that folder, so an
  agent is not lost in the middle of a long context.
- **One source per rule.** Universal rules come from intelligence, conventions from standards, and
  only what is the vault's own stays here.
- **A public template.** Anyone generates a private vault from it, so it is MIT and initialises
  each vault into its owner's identity.

---

## 🏗️ Considered Options

1. **Keep the Constitution and Instructions below `AGENTS.md`**, as vault documents an agent reads
   after the root file.
2. **Dissolve them**: the universal block and the vault's own rules in `AGENTS.md`, each folder's
   rules in a Rules section of its note, and the long reference parts in `.docs/vault/`.
3. **One `AGENTS.md` per folder**, which Claude Code loads on its own when work reaches a folder.

---

## ✅ Decision Outcome

**Chosen Option**: Option 2, dissolve them.

### Rationale for Selection

It is the only option with one source for each rule. Option 1 kept 110 KB of rules that repeat the
universal block and standards, and Option 3 loads rules only in apps that read nested `AGENTS.md`
files. Folder notes already held most folder rules (the Inbox protocol, the Library's and the
Profile's delegated articles), and the root `AGENTS.md` makes reading them mandatory. A session
now reads about 14 KB before work: the 4.5 KB universal block and the vault's own rules.

### Where Every Rule Went

| Was                                                    | Is now                                                                        |
| :----------------------------------------------------- | :---------------------------------------------------------------------------- |
| Constitution I (1.1, 1.3, 1.4), III 3.2, V 5.4 and 5.5 | The universal block in `AGENTS.md`: WORK-001, COM-002 and its precedence      |
| Constitution 1.2, 2.4, 2.5, 2.6, 3.6, 9.6, 9.7         | `AGENTS.md`, Conventions                                                      |
| Constitution 2.1-2.3, 3.1, 3.4, 3.8, VIII              | `AGENTS.md`, Ask first                                                        |
| Constitution 2.7, 4.1-4.4, 1.5                         | `Profile/Profile.md` and `Memory/Memory.md`, Rules; SEC-003                   |
| Constitution 3.3, 3.5; Instructions 4.2, 8             | `.docs/vault/Note-Schema.md`                                                  |
| Constitution 3.7; Instructions 12                      | `.docs/vault/Link-Topology.md`                                                |
| Constitution 5.1, 5.2; Instructions 4.3-4.5, 9         | `AGENTS.md`, Start here and Commands                                          |
| Constitution 5.3; Instructions 7                       | `Inbox/Inbox.md`, Rules                                                       |
| Constitution 5.6                                       | STD-001 and `tannergolden/standards`                                          |
| Constitution VI                                        | `Library/Library.md`, Rules                                                   |
| Constitution VII                                       | `.docs/vault/Tag-Vocabulary.md`                                               |
| Constitution 9.1, 9.2, 9.5, X                          | DOC-002, DOC-003 (with standards' Plain Words), COM-005, COM-004              |
| Constitution 9.3                                       | An owner's own `Profile/Working Style.md`, never the template                 |
| Constitution 9.4                                       | `System/System.md`, Reports On The Vault                                      |
| Instructions 1, 2, 5, 6, 11, 13                        | `.github/README.md`, `AGENTS.md`, `Profile/Profile.md` and `Memory/Memory.md` |
| Instructions 14                                        | `.docs/vault/Context-Assembly.md`                                             |
| `Information.md`                                       | `.github/README.md`                                                           |
| `CLAUDE.md` and the three hook digests                 | Removed: Claude Code reads `AGENTS.md` itself                                 |

Every amendment the deleted files recorded stays in the git history.

---

## 📈 Consequence Matrix

| Category         | Impact / Consequence                                                                                                       |
| :--------------- | :------------------------------------------------------------------------------------------------------------------------- |
| **Positive (+)** | A session reads a tenth of the rules it did; each rule has one source; the template is public, MIT and initialises a vault |
| **Negative (-)** | No app loads a folder note by itself, so folder rules hold only because `AGENTS.md` makes reading them mandatory           |
| **Neutral (~)**  | Notes keep their `---` properties, which standards' styling guide now exempts for an Obsidian vault                        |

---

## ⚖️ Trade-off Comparative

### Option 1: Keep Them Below AGENTS.md

- ✅ No rewrite, and every amendment stays in place.
- ❌ 110 KB of rules read at every start, two of every three repeated elsewhere.

### Option 3: One AGENTS.md Per Folder

- ✅ Claude Code loads a folder's rules on its own.
- ❌ Other apps handle nested files differently, and a folder's procedures would split from its
  note.

---

## 🔗 Traceability & Links

- [`AGENTS.md`](../../AGENTS.md), the vault's rules
- [Vault reference](../vault/README.md): the schema, the tag vocabulary, the link topology and
  context assembly
- The universal rules:
  [`CONSTITUTION.md` in tannergolden/intelligence](https://github.com/tannergolden/intelligence/blob/Development/CONSTITUTION.md)

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the
> [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md).
> If you rename or move a file, update every reference to it across the repository to prevent link
> drift.

---

<div align="center">

**Each rule once, where the work needs it.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
