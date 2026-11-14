<!--
title: '🧭 ADR-[NNNN]: [THE DECISION, FULLY CAPPED]'
description: 'The form for one decision about the vault itself, such as its layout, its rules, its scripts or its automation: the context, the options weighed, the outcome and its consequences. Copy it to .docs/adrs/ when such a decision is made.'
type: 'template'
keywords: ['[a search term not in the title]', '[another name for the decision]', 'template']
status: '[Proposed / Accepted / Superseded / Deprecated]'
date: '[YYYY-MM-DD]'
evidence: '[A commit-pinned permalink to each research log behind it, as a markdown link, or N/A]'
-->

<!-- On copying: copy this file to .docs/adrs/ADR-[NNNN]-[Short-Slug].md, taking the next number and naming it in Capitalized-Kebab, to record one decision about the vault itself: its layout, its rules, its scripts or its automation. A decision in the owner's own life is a record in Memory/Decisions/, made from Memory/.template/Decision.md, and a venture's goes in its Administration/Decisions.md. Set type to 'record', status to the one that holds, date to the day it was decided, and evidence to a commit-pinned permalink to each research log behind it, or N/A; evidence never links a report in Inbox/Research/, which only that folder's index links. Replace every [bracketed] placeholder: the title and the H1 alike, with the number and the decision fully capped, the description with one of the record's own, saying what it holds and when to read it, the one-line summary, the tagline and the closing phrase; give it up to eight lowercase keywords not already in the title, without 'template'. Delete a section or a row that does not apply. In tannergolden/knowledge itself, the copy takes a line under "Only ever in the template" in .github/template-sync (.docs/distribution/How-A-Change-Reaches-A-Vault.md). A later decision supersedes this one rather than rewriting it: this record is marked Superseded and links the one that replaces it. Delete this note from the copy. -->

<div align="center">

# 🧭 ADR-[NNNN]: [THE DECISION, FULLY CAPPED]

<a name="top"></a>

**[One line: what was decided, as a reader should remember it.]**

_[A principle of this decision's own, shorter than the line above.]_

</div>

---

## 📋 Meta Information

> [!NOTE]
> **Status**, **Date** and **Evidence** live in the frontmatter above and feed the
> [ADR index](/.docs/adrs/README.md), so they are recorded once. This table records who took part.

| Attribute     | Specification                                                             |
| :------------ | :------------------------------------------------------------------------ |
| **Deciders**  | [Who decided: the owner, and anyone they decided with]                    |
| **Consulted** | [Who or what was asked: a person, an AI, a research log]                  |
| **Informed**  | [Who it reaches: this vault alone, or every vault made from the template] |
| **Amends**    | [The record this one amends or supersedes, as a link, or delete this row] |

---

## 🎯 Context & Problem Statement

[The situation that called for a decision, the problem it solves and the limits it was made
within, in a few short paragraphs.]

---

## 🚦 Decision Drivers

- **[Driver]**: [such as: every AI finds the rules without the home kit]
- **[Driver]**: [such as: nothing about the owner leaves the vault]
- **[Driver]**: [such as: a vault made before the change can still take it]

---

## 🏗️ Considered Options

1. **[The first option's name]**: [The option, in one sentence]
2. **[The second option's name]**: [The option]
3. **[The third option's name]**: [The option]

---

## ✅ Decision Outcome

**Chosen Option**: Option [N], [its name]

### Rationale for Selection

[Why this option won over the others, against the drivers above.]

### What Changed

| Was | Is now |
| :-- | :----- |
| [How it was before] | [How it is now] |

[Delete this table when the decision changes nothing already in the vault.]

---

## 📈 Consequence Matrix

| Category         | Impact / Consequence                                            |
| :--------------- | :-------------------------------------------------------------- |
| **Positive (+)** | [such as: one description per folder, where every reader looks] |
| **Negative (-)** | [such as: a vault made before the change takes a manual step]   |
| **Neutral (~)**  | [such as: the note schema is unchanged]                         |

---

## ⚖️ Trade-off Comparative

<!-- One section for each option not chosen. -->

### Option [N]: [The Name of an Option Not Chosen]

- ✅ [What it does well]
- ❌ [What it costs]

---

## 🔗 Traceability & Links

- [The pull request that carries the change]
- [The research log, design or plan behind it, in `.docs/technical/`]
- [The records it supersedes or amends, or that amend it]

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**[A closing phrase of this decision's own.]**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
