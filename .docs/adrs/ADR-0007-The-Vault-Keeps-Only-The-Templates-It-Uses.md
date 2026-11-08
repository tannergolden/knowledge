<!--
title: '🧭 ADR-0007: THE VAULT KEEPS ONLY THE TEMPLATES IT USES'
description: 'The template drops the golden path''s fill-in standards for a software repository and its Project README seed, takes .docs/templates/ out of its derivation from tannergolden/path, and keeps the eight work-product forms as its own, rewritten for a one-owner vault.'
type: record
keywords: [fill-in standards, work-product forms, seeds, derivation, golden path, template-sync]
status: 'Accepted'
date: '2026-11-08'
evidence: 'N/A'
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🧭 ADR-0007: THE VAULT KEEPS ONLY THE TEMPLATES IT USES

<a name="top"></a>

**A vault keeps the forms it can fill in, written for a vault, and nothing else.**

_A form earns its place by being used._

</div>

---

## 📋 Meta Information

> [!NOTE]
> **Status**, **Date**, and **Evidence** live in the frontmatter above and feed the
> [ADR index](README.md).

| Attribute     | Specification                                                      |
| :------------ | :----------------------------------------------------------------- |
| **Deciders**  | The vault's owner                                                  |
| **Consulted** | The AI agents that audited the template and carried out the change |
| **Informed**  | Everyone who generates a vault from this template                  |

---

## 🎯 Context & Problem Statement

This template takes `docs/templates/` from tannergolden/path, the golden path template, through its
derivation, `.github/template-derive.json`, which relocates it to `.docs/templates/`, and every
vault keeps that folder current through 🔄 Template Sync. It held 47 files: eight work-product forms
(ADR, Communication, Implementation Plan, Post-Mortem, Research Log, Runbook, Technical Design and
User Story), a Project README seed, and 26 fill-in standards in `introduction/`, `technical/` with
six area folders, `operations/`, `distribution/` and `references/`, with the 11 READMEs that logged
them.

The fill-in standards are for a software repository: its architecture, stack and source, its API,
data model and migrations, its interface and tests, its pipelines and deployment, its incidents,
threats and dependencies, and its releases. A vault is a personal knowledge base, not a software
project, so none of them can ever apply to it, and the Project README seed has nowhere to go, since
a vault's root `README.md` is its guide. The forms a vault can use still assumed a software team:
`docs/` paths that do not exist in a vault, architects and engineering teams, an API gateway and
microservices, `make test`, on-call rotations and incident channels, and a directive addressed to
an AI.

The owner decided on 2026-11-08, in making the template ready for a personal knowledge vault, to
keep only the templates a vault can use, and to rewrite those for a vault.

---

## 🚦 Decision Drivers

- **Every template a vault holds is one it can use.**
- **Every form fits a one-owner vault**: it says where its copy goes, what the copy is for and what
  type it takes, and it carries the page format the copy needs.
- **Nothing synced later undoes it**: no sync brings a removed seed back or overwrites a rewritten
  form.
- **Each form has one home and one maintainer.**

---

## 🏗️ Considered Options

1. **Keep every seed and form** as the golden path ships them.
2. **Remove the fill-in standards and the Project README seed**, exclude them in the derivation, and
   keep the eight forms synced from the golden path, edited where a vault needs it.
3. **Remove the fill-in standards and the Project README seed, take the whole `docs/templates`
   folder out of the derivation**, and rewrite the eight forms for a one-owner vault, as this
   template's own.

---

## ✅ Decision Outcome

**Chosen Option**: Option 3, the vault's document templates are its own.

### Rationale for Selection

Option 1 ships 38 files a vault can never use into every vault and keeps them current for good.
Option 2 removes them, but a form rewritten for a vault differs from the golden path's in nearly
every line, so each later sync from tannergolden/path would set the golden path's changes against
the vault's lines, and report each one it cannot merge as waiting on whoever maintains the template.
Option 3 makes the folder this template's: one `exclude` entry keeps every file in it, present and
future, out of the derivation, each form says what is true in a vault, and every vault still keeps
the forms current from this template.

### What Changed

| Was                                                                                                                                                                                                                            | Is now                                                                                                                                                                             |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `.docs/templates/` held the eight work-product forms, a Project README seed, and 26 fill-in standards with the 11 READMEs that logged them, in `introduction/`, `technical/`, `operations/`, `distribution/` and `references/` | It holds the eight forms and its README; the 38 seed files are gone                                                                                                                |
| `.github/template-derive.json` took `docs/templates/` from tannergolden/path                                                                                                                                                   | Its `exclude` list names `docs/templates`, so no sync from the golden path touches the folder                                                                                      |
| `.github/template-sync` listed the folder's 47 files under Kept current, among the files taken from tannergolden/path                                                                                                          | It lists the eight forms and the README under The vault: kept current, so every vault keeps them current from this template, and lists this record under Only ever in the template |
| The forms assumed a software team: `docs/` paths, architects and engineering teams, an API gateway, `make test`, on-call rotations and incident channels, and a directive addressed to an AI                                   | Each says where its copy goes in a vault and what type the copy takes, carries the page format with placeholders, and asks only what a one-owner vault can answer                  |
| A user story was copied to a stories folder or a tracker                                                                                                                                                                       | A user story goes into an issue opened from ✨ Feature Request                                                                                                                     |
| The templates README catalogued fill-in standards and a Project README                                                                                                                                                         | It lists the eight forms, where each copy goes, and why the rest is not here                                                                                                       |
| `.docs/README.md`, `SECURITY.md`, `CONTRIBUTING.md`, `GOVERNANCE.md` and two forms named a removed seed                                                                                                                        | Each names what a vault has instead                                                                                                                                                |

The rest of the derivation stands: it still takes the golden path's workflow stubs, repository
scripts, community files and forms, and the other `.docs/` folder READMEs.

---

## 📈 Consequence Matrix

| Category         | Impact / Consequence                                                                                                                                                                                                                          |
| :--------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Positive (+)** | A vault holds only templates it can use, each saying where its copy goes and what it takes; `.docs/templates/` reads as a vault's; 38 fewer files reach every vault                                                                           |
| **Negative (-)** | A vault made before this change loses, on its next 🔄 Template Sync, each removed seed it never changed, and keeps as its own any it changed; the golden path's later fixes to the forms no longer arrive, so this template keeps them itself |
| **Neutral (~)**  | A document already copied from a seed or a form is its owner's and untouched; a software repository the owner builds is generated from tannergolden/path, which ships the fill-in standards                                                   |

---

## ⚖️ Trade-off Comparative

### Option 1: Keep Every Seed And Form

- ✅ Nothing to maintain beyond the golden path's own fixes.
- ❌ 38 documents a vault can never use in every vault, and forms written for a software team.

### Option 2: Remove The Seeds, Keep Syncing The Forms

- ✅ The forms keep taking the golden path's fixes.
- ❌ A form rewritten for a vault conflicts with nearly every later change the golden path makes to
  it.

---

## 🔗 Traceability & Links

- [`.github/template-derive.json`](../../.github/template-derive.json): the derivation, whose
  `exclude` list names `docs/templates`
- [`.github/template-sync`](../../.github/template-sync): the eight forms and the README under The
  vault: kept current
- [The document templates](../templates/README.md): the eight forms, where each copy goes, and why
  the rest is not here
- [How A Change Reaches A Vault](../distribution/How-A-Change-Reaches-A-Vault.md): the two hops, and
  what the mapping excludes
- The standards'
  [Template Sync](https://github.com/tannergolden/standards/blob/Development/docs/distribution/automation/Template-Sync.md),
  A Template Derived From Another

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the
> [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md).
> If you rename or move a file, update every reference to it across the repository to prevent link
> drift.

---

<div align="center">

**Every form a vault holds is one it can fill in.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
