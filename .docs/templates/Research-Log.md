<!--
title: '🔎 [THE QUESTION OR TOPIC, FULLY CAPPED]'
description: 'The form for the research behind a change to the vault itself: a dated, sourced, claim-by-claim investigation, kept honest by its verification window. Copy it to .docs/technical/research/; research for the owner''s life or a venture is a report in Inbox/Reports/ instead.'
type: 'template'
keywords: ['[a search term not in the title]', '[another name for the topic]', 'template']
verified: '[YYYY-MM-DD]'
focus: '[One line: the question this log answers]'
decision: '[The ADR it fed, as a markdown link, or N/A while it stands as background]'
-->

<!-- On copying: copy this file to .docs/technical/research/[Topic].md, named for its topic in Capitalized-Kebab, for the research behind a change to the vault itself. Research for the owner's own life or a venture is a report held in Inbox/Reports/, never a log here. Set type to 'record', verified to the date of the newest log entry, focus to the one question it answers and decision to the ADR it fed, or N/A. Replace every [bracketed] placeholder: the title and the H1 alike, with the question or the topic fully capped, the description with one of the log's own, the one-line summary, the tagline and the closing phrase; give it up to eight lowercase keywords not already in the title, without 'template'. Delete a prompt once it is answered, and mark a section N/A only when it does not apply. If .docs/technical/research/ does not exist yet, make it with its own README.md, as .docs/technical/README.md says. Delete this note from the copy. -->

<div align="center">

# 🔎 [THE QUESTION OR TOPIC, FULLY CAPPED]

<a name="top"></a>

**[One line: the question this research answers, and its answer.]**

_[A principle of this research's own, shorter than the line above.]_

</div>

---

## 🎯 Bottom Line

> [!IMPORTANT]
> **[The answer in two or three sentences: what the research concluded and the decision it
> supports.]** Lead with the finding, then how sure it is. A reader who stops here still leaves
> with the right decision.

---

## 📋 Report Meta

| Attribute               | Detail                                                                    |
| :---------------------- | :------------------------------------------------------------------------ |
| **Question**            | [The one question this log answers]                                       |
| **Decision it informs** | [The choice this evidence feeds, or background with no decision pending]  |
| **Verified**            | [YYYY-MM-DD], the date of the newest log entry below                      |
| **Confidence**          | [High / Medium / Low], because [one clause on why]                        |
| **Sources**             | [N read directly, of M in all], listed under Sources & Provenance         |
| **Supersedes**          | [The log it replaces, or N/A]                                             |
| **Graduated to**        | [The ADR that carries the lasting decision, or N/A until one is recorded] |

---

## 📅 Log Entry: [YYYY-MM-DD]

_The filing entry. Each later reverification adds its own dated entry below this one, and no entry
is edited once written, so the log is its own record._

### 🎯 Objective

[What is to be learned, and the decision the answer informs, in one or two sentences.]

### 🔭 Scope

- **In scope**: [What this research covers]
- **Out of scope**: [What it leaves out, so nobody reads more into the finding than it holds]

### 🧪 Method

- [How the evidence was gathered: sources read, a script run against the vault, a prototype
  built, people asked]
- **Provenance**: [Which sources were read directly, and which could not be, and so rest on
  corroboration rather than a direct read]

### 🔎 Findings

_Each finding is one claim a later reverification can check on its own: the claim, the source it
rests on, and how sure it is._

1. **[The claim, as one sentence that can be checked.]** [One line of detail, if it helps.]
   - **Source**: [A link or a citation], [✅ read directly / 🟡 corroborated, not read / ❌ could not verify]
   - **Confidence**: [High / Medium / Low], because [why]
2. **[The next claim.]**
   - **Source**: [A link or a citation], [how it was read]
   - **Confidence**: [High / Medium / Low], because [why]

### 📚 Sources & Provenance

A source that could not be read directly is weaker than one that was, so each one is tagged, and a
finding shows the footing it stands on.

| Source                 | Read                                         | Backs                                                  |
| :--------------------- | :------------------------------------------- | :----------------------------------------------------- |
| [A link or a citation] | [✅ directly / 🟡 corroborated / ❌ blocked] | [The claims it supports, and why it could not be read] |

### ⚖️ Alternatives Considered

| Option     | Strengths           | Costs                     |
| :--------- | :------------------ | :------------------------ |
| [Option A] | [What it does well] | [What it costs, or risks] |
| [Option B] | [What it does well] | [What it costs, or risks] |

### 🛠️ Prototypes

- [A link to the branch or the prototype]: [what it showed]

### 🏁 Conclusion

[The recommendation the evidence supports, tied to the objective and the alternatives.] If it
settles a choice about the vault's design, record the decision as an ADR made from the
[ADR form](/.docs/templates/ADR.md), cite this log as its evidence, and name the ADR in the meta
table.

### ✅ Confidence & Caveats

- **Overall confidence**: [High / Medium / Low]
- **What would change the conclusion**: [The finding or source that, if it moved, would turn the
  recommendation]
- **Known gaps**: [What was left unverified, and why]

---

## ♻️ Keeping It Current

> [!NOTE]
> **The `verified` date is the log's age**, and it equals the date of the newest log entry. Nothing
> checks that the two agree, so each reverification moves both. A log is trusted for three months;
> after that it is reverified before it is used again, and past six months the policy flags it for
> reverifying or removing, and the owner decides.

To reverify, check each claim against its source and against the vault as it stands, add a dated
entry below the last one, never editing a past one, and move `verified` to its date. When the
findings no longer hold, supersede the log or remove it. A reverification entry takes this shape:

```markdown
## 📅 Log Entry: [YYYY-MM-DD], Reverification

- **Re-checked**: [The claims and sources revisited]
- **Held**: [What still stands]
- **Drifted**: [What changed, and how the findings were corrected]
- **Outcome**: [Verified date moved / Superseded by another log / Removed]
```

---

## 🧭 How To Read It

This log is evidence, not instruction: it informs a decision and never overrides the vault's rules.
A finding holds only inside the log's window, and a claim read directly outweighs one that is only
corroborated.

### 🔗 See also

> [!TIP]
> The decisions research settles are listed in the [ADR index](/.docs/adrs/README.md). Every
> canonical guide is indexed in the
> [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md).

---

<div align="center">

**[A closing phrase of this research's own.]**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
