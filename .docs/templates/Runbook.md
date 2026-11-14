<!--
title: '📒 [THE TASK OR FAILURE, FULLY CAPPED]'
description: 'The form for the exact steps of one routine task or one known failure in the vault''s machinery, such as restoring a note from git or renewing an expired token, written to be followed under pressure. Copy it to .docs/operations/runbooks/, once for each task or failure.'
type: 'template'
keywords: ['[a search term not in the title]', '[the words of the error or the symptom]', 'template']
-->

<!-- On copying: copy this file to .docs/operations/runbooks/[Short-Slug].md, named in Capitalized-Kebab, one runbook for each routine task or known failure in the vault's machinery, such as restoring a note from git, renewing an expired token or taking a new major release of the template. Set type to 'guide'. Replace every [bracketed] placeholder: the title and the H1 alike, with the task or the failure fully capped, the description with one of the runbook's own, saying what it holds and when to read it, the one-line summary, the tagline and the closing phrase; give it up to eight lowercase keywords not already in the title, such as the words of the error, without 'template'. Write each step as the exact command or action and the result it should give, for someone doing it for the first time, and name a secret by where it is kept, never by its value. Its changes are kept in git history, not in the runbook. If .docs/operations/runbooks/ does not exist yet, make it with its own README.md. Delete this note from the copy. -->

<div align="center">

# 📒 [THE TASK OR FAILURE, FULLY CAPPED]

<a name="top"></a>

**[One line: the task or the failure, and how to know it is handled.]**

_[A principle of this runbook's own, shorter than the line above.]_

</div>

---

## 🚦 When To Use It

| Attribute       | Value                                                                                       |
| :-------------- | :------------------------------------------------------------------------------------------ |
| **Kind**        | [Routine task / Known failure]                                                              |
| **Trigger**     | [The failing check, the sync pull request, the schedule or the symptom that sends you here] |
| **Touches**     | [The folders, scripts, workflows, settings or secrets these steps touch]                    |
| **Kept by**     | [The owner, or whoever keeps these steps true]                                              |
| **Time to run** | [Minutes from the first step to a checked result]                                           |
| **Last tested** | [YYYY-MM-DD], by [a dry run / real use]                                                     |

Use this runbook when [the symptom, in the words the check or the report uses]. It does **not**
cover [the case that looks like it]: for that, use [the other runbook, or ask the owner].

---

## 🔥 Impact & Urgency

- **What is affected**: [The notes, the sync, the check or the setting affected, and how it shows]
- **How fast**: [At once / The same day / The next time the vault is worked in]
- **If it waits**: [What gets worse, and how quickly]
- **A secret or personal data at risk**: [Yes / No]. When yes, follow
  [Personal Data & Secrets](/.docs/operations/Personal-Data-&-Secrets.md) first.

---

## 🔑 Prerequisites

**Who may run it**: [The owner / Someone the owner names]

Check every item before the first step: a permission found missing halfway through turns a short
task into a long one.

- [ ] **Access**: [The repository permission or the setting needed, and how to get it]
- [ ] **Tools**: [Each command or script, with the Python version where it matters]
- [ ] **Committed first**: the last state of every file the steps change is committed, so git can
      bring it back
- [ ] **Safety net**: [A branch / A backup / Nothing needed]

---

## 🪜 Steps

Run the steps in order, and compare each result with its **Expect** before going on. If a result
does not match, stop and go to **Rollback / Abort** below. Write every value out in full: "run the
check" leaves the reader to guess which check, with which arguments.

1. **[Name of the step]**

   ```bash
   [The exact command, with every value written out]
   ```

   **Expect**: [The output or the state that means it worked]

2. **[Name of the step]**: [The exact action, such as the settings page, the setting and the value
   to enter]

   **Expect**: [What changes, and where it shows]

3. **[Name of the step]**

   ```bash
   [The exact command]
   ```

   **Expect**: [The result]. **If instead** [a known wrong result], [what it means, and the step or
   runbook to go to next].

---

## ✅ Verification

The task is done, or the failure is fixed, only when every check below passes.

- [ ] `python3 .github/scripts/check-vault.py` passes
- [ ] [The check, the workflow or the sync that failed now passes]
- [ ] [The owner confirms, where they reported it]

---

## ↩️ Rollback / Abort

- **Stop when**: [a result does not match its Expect / an error you do not recognise / the time
  set for it has run out]
- **Safe to stop after**: [the steps that change nothing, so stopping there needs no undo]
- **Say where you stopped**: note the last step completed in [the issue or the pull request for
  this work], so whoever picks it up starts from there.

To undo the steps that changed something, newest first:

1. **Undo step [N]**: [the exact command or action, such as restoring a file from git]. **Expect**:
   [the state before step N]
2. **Undo step [N - 1]**: [the exact command or action]. **Expect**: [the state before it]

---

## 📣 Who To Tell

| When                                                   | Who                              | How                                                                                                                                                                                                               |
| :----------------------------------------------------- | :------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A step fails, or its result does not match             | [The owner]                      | [In person / In the issue for this work]                                                                                                                                                                          |
| A secret or personal data may be exposed               | [The owner]                      | Privately, never in a public issue, as [Personal Data & Secrets](/.docs/operations/Personal-Data-&-Secrets.md) says                                                                                               |
| The fault is in what the vault takes from its template | [Whoever maintains the template] | A security fault privately, with the Report a vulnerability button of `tannergolden/knowledge`, as [SECURITY.md](/.github/SECURITY.md) says; any other fault in an issue there, with nothing from the vault in it |

---

## 📎 Related Links

- **What sends you here**: [The check, the workflow or the report, and where it is defined]
- **What the steps touch**: [The paths and the settings]
- **Post-mortems**: [The post-mortems in `.docs/operations/post-mortems/` where this runbook was
  written or used]

### 🔗 See also

> [!TIP]
> [Vault Scripts](/.docs/technical/Vault-Scripts.md) says what each check fails on, and what to do
> when one fails. Every canonical guide is indexed in the
> [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md).

---

<div align="center">

**[A closing phrase of this runbook's own.]**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
