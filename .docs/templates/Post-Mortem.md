<!--
title: '📉 POST-MORTEM: [WHAT HAPPENED, FULLY CAPPED]'
description: 'The form for a blameless account of something that went wrong in the vault or its machinery, such as a leak, a lost change or a sync that overwrote work: what happened, why, and the actions that stop a repeat. Copy it to .docs/operations/post-mortems/.'
type: 'template'
keywords: ['[a search term not in the title]', '[another name for what happened]', 'template']
-->

<!-- On copying: copy this file to .docs/operations/post-mortems/[YYYY-MM-DD]-[Short-Slug].md, dated the day it happened and named in Capitalized-Kebab, after something went wrong in the vault or its machinery, such as a leak, a lost change or a sync that overwrote work. Set type to 'record'. Replace every [bracketed] placeholder: the title and the H1 alike, with what happened fully capped, the description with one of the post-mortem's own, the one-line summary, the tagline and the closing phrase; give it up to eight lowercase keywords not already in the title, without 'template'. Stay blameless: name the process or the safeguard that failed, never a person. Name a leak by where it was, never by what it held: no secret, number or personal detail is written here (.docs/operations/Personal-Data-&-Secrets.md). If .docs/operations/post-mortems/ does not exist yet, make it with its own README.md. Delete this note from the copy. -->

<div align="center">

# 📉 POST-MORTEM: [WHAT HAPPENED, FULLY CAPPED]

<a name="top"></a>

**[One line: what went wrong, and what changes because of it.]**

_[A principle of this post-mortem's own, shorter than the line above.]_

</div>

---

## 🗓️ Overview

| Attribute    | Value                                                                |
| :----------- | :------------------------------------------------------------------- |
| **Date**     | [YYYY-MM-DD]                                                         |
| **Severity** | [Critical / High / Medium / Low]                                     |
| **Duration** | [From the first effect to recovery, such as 2 h 15 min]              |
| **Affected** | [The notes, folders, scripts, settings or secrets affected, and how] |

---

## 📝 Summary

[What happened, in two or three sentences.]

---

## ⏱️ Timeline

- [h:mm am or pm]: [The first effect, or the change that set it off]
- [h:mm am or pm]: Detected, by [a failing check / a sync pull request / a scan / the owner]
- [h:mm am or pm]: Contained, by [what stopped it getting worse]
- [h:mm am or pm]: Resolved, by [how the vault was put right]

---

## 📈 What Went Well

- [What helped]

---

## 📉 What Could Be Improved

- [What made it worse, or slower to put right]

---

## 🛠️ Root Cause

- **Why it happened**: [Ask why until the answer is a process or a safeguard, never a person]
- **Why it was not caught sooner**: [The check, the review or the session step that missed it]
- **How it was found**: [How it came to light]

---

## 💡 Lessons Learned

- [What this taught]

---

## ✅ Action Items

Each item has an owner and an issue, so it is followed to done.

- [ ] [The change that stops a repeat]: owner [the owner / @handle], issue [#number]
- [ ] [The check or scan that would catch it sooner]: owner [the owner / @handle], issue [#number]
- [ ] [The runbook or README that changes]: owner [the owner / @handle], issue [#number]

### 🔗 See also

> [!TIP]
> [Personal Data & Secrets](/.docs/operations/Personal-Data-&-Secrets.md) says what to do when
> something leaks, and a [Runbook](/.docs/templates/Runbook.md) written from a post-mortem makes the
> next one shorter. Every canonical guide is indexed in the
> [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md).

---

<div align="center">

**[A closing phrase of this post-mortem's own.]**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
