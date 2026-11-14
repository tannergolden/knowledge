<!--
title: '🧭 ARCHITECTURE DECISIONS'
description: 'Architecture decision records, one file per decision, each logged with its status, date and evidence.'
type: index
-->

<div align="center">

# 🧭 ARCHITECTURE DECISIONS

<a name="top"></a>

**Every significant decision about the vault itself, and why, one record each.**

_One decision per record. One row per decision._

</div>

---

## 💡 What This Folder Is For

An architecture decision record (ADR) captures one significant decision about
the vault itself, such as a change to its layout, its rules or its machinery:
the context it was made in, the options weighed, and the consequences accepted.
Every record lives in this folder, one file per decision, and the log below is
their index.

A decision in the owner's own life is not an ADR: it is recorded in
`Memory/Decisions/`, and a venture's in its `Administration/Decisions.md`, each
by its folder's README.

The folder is a living record, not a fill-in form, and its records are **yours
from the first commit**: nothing upstream ever writes, moves or removes one. In
a vault it arrives with no decisions in it, since the records here are this
template's own and initialisation deletes them, and it gains a row each time a
record is written. Only this README is ever updated from the template, when you
run 🔄 Template Sync, merged with the rows your records add.

---

## 🎯 Why Decisions Are Recorded

The _why_ matters as much as the _what_. An auditable record of how the vault
evolved lets whoever changes it later, a person or any AI, see the constraints
and trade-offs that shaped it first.

- **Traceability**: every major architectural pivot is documented and numbered.
- **Context**: each decision is recorded with the situation it was made in.
- **Consequences**: the benefits and the technical debt are both written down.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log fields=status,date,evidence -->

| Entry                                                                                                                                  | Status     | Date       | Evidence | Purpose                                                                                                                                                                                                                                                                                                             |
| :------------------------------------------------------------------------------------------------------------------------------------- | :--------- | :--------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [`ADR-0001-AGENTS-Holds-The-Vaults-Rules.md`](ADR-0001-AGENTS-Holds-The-Vaults-Rules.md)                                               | Superseded | 2026-10-19 | N/A      | The vault's Constitution and Instructions dissolve into AGENTS.md, the folder notes and reference pages, and standards owns every repository convention.                                                                                                                                                            |
| [`ADR-0002-Notes-Take-The-Hidden-Frontmatter.md`](ADR-0002-Notes-Take-The-Hidden-Frontmatter.md)                                       | Accepted   | 2026-10-19 | N/A      | The vault drops its Obsidian and Claude Code configuration: every note opens with the account's hidden frontmatter, renders as GitHub-Flavored Markdown and keeps its wikilinks.                                                                                                                                    |
| [`ADR-0003-The-Skills-Live-Where-The-Apps-Read-Them.md`](ADR-0003-The-Skills-Live-Where-The-Apps-Read-Them.md)                         | Superseded | 2026-10-26 | N/A      | The vault keeps its seven skills in .agents/skills/, each faculty with its team inside, draws a copy into .claude/skills/ for Claude Code, and lets a home install of a faculty hand over to the vault's own copy.                                                                                                  |
| [`ADR-0004-The-Skills-Live-In-The-Home-Kit.md`](ADR-0004-The-Skills-Live-In-The-Home-Kit.md)                                           | Superseded | 2026-11-07 | N/A      | The vault holds no skills or agents: every skill and its team live in tannergolden/intelligence and arrive through the home kit, and AGENTS.md gives the universal skills the vault's layout.                                                                                                                       |
| [`ADR-0005-Each-Folder-Explains-Itself-In-A-README.md`](ADR-0005-Each-Folder-Explains-Itself-In-A-README.md)                           | Accepted   | 2026-11-07 | N/A      | Every folder explains itself in a README.md at its root, written for anyone, which is also its note, and the root README.md says how to work in the vault; the vault holds no AI instructions, so AGENTS.md and the Intelligence Sync stub are gone.                                                                |
| [`ADR-0006-AGENTS-Returns-With-The-Rules-For-Personal-Knowledge.md`](ADR-0006-AGENTS-Returns-With-The-Rules-For-Personal-Knowledge.md) | Accepted   | 2026-11-07 | N/A      | AGENTS.md returns at the vault root, with the universal rules kept current by Intelligence Sync and then the rules every AI follows in a personal knowledge vault, so every vault generated from the template starts with them; each folder still explains itself in its README, written for anyone.                |
| [`ADR-0007-The-Vault-Keeps-Only-The-Templates-It-Uses.md`](ADR-0007-The-Vault-Keeps-Only-The-Templates-It-Uses.md)                     | Accepted   | 2026-11-08 | N/A      | The template drops the golden path's fill-in standards for a software repository and its Project README seed, takes .docs/templates/ out of its derivation from tannergolden/path, and keeps the eight work-product forms as its own, rewritten for a one-owner vault.                                              |
| [`ADR-0008-The-Vault-Relies-On-No-Skills.md`](ADR-0008-The-Vault-Relies-On-No-Skills.md)                                               | Proposed   | 2026-11-14 | N/A      | tannergolden/intelligence ships no skills since its ADR-0041, so the vault stops naming the twelve department skills: its pages name the twelve departments and the work each covers, the profile interview is the one Profile/README.md describes, and nothing tells an AI or the owner to install or use a skill. |
| [`README.md`](README.md)                                                                                                               | -          | -          | -        | This file.                                                                                                                                                                                                                                                                                                          |

<!-- AUTO-INDEX:END -->

**This log is the decision index, and nobody types its rows.** 🗂️ Machined
Indexes redraws it after every push to the default branch, from each record's
own frontmatter.
**Status** is Proposed, Accepted, Superseded, or Deprecated; **Date** is when
the decision was made; **Evidence** links the research report(s) that informed
it, or reads N/A.

---

## 🌿 Adding A Decision

- [ ] Copy the [ADR template](../templates/ADR.md) into this folder as
      `ADR-NNNN-Short-Slug.md`, taking the next number.
- [ ] Give it its own title and description, set `type: record`, `status`, `date` and
      `evidence` in its frontmatter, and write every section.
- [ ] Propose it in a pull request. Once merged, it is **Accepted**.

A later decision supersedes an earlier one rather than rewriting it: mark the
old record **Superseded** and link the new one.

---

## 🔗 See also

- [Documentation index](../README.md) - every document the vault keeps in `.docs/`
- [Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md) - the canonical engineering standards

---

<div align="center">

**Write the decision down while the reasons are still fresh.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
