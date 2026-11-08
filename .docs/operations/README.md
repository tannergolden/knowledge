<!--
title: '🛡️ OPERATIONS & SECURITY'
description: 'Keeping the vault healthy and safe: why it stays private, how a secret is kept out of it, and the runbooks and post-mortems written for it. Read it before you touch anything sensitive, or after something goes wrong.'
type: index
-->

<div align="center">

# 🛡️ OPERATIONS & SECURITY

<a name="top"></a>

**Keeping the vault private, safe and working, and what to do when it is not.**

_What to do while it runs, and when it breaks._

</div>

---

## 💡 What This Folder Is For

What it takes to keep the vault private, safe and working, and what to do when
something goes wrong.

- **Personal data and secrets**: why a vault stays private, how a secret is
  referenced without being stored, the scans that guard both, and what to do
  when something leaks, in
  [Personal Data & Secrets](Personal-Data-&-Secrets.md).
- **Runbooks**: the steps for a routine task or a known failure, such as a
  sync that keeps failing, written to be followed under pressure, one each in
  `runbooks/`, from the [Runbook](../templates/Runbook.md) template.
- **Post-mortems**: one for each incident, such as a leak or a lost change, in
  `post-mortems/`, from the [Post-Mortem](../templates/Post-Mortem.md)
  template.

The guardrails every repository shares, such as branch protection, dependency
updates and secret scanning, are the standards', linked below.

Personal Data & Secrets, like this README, is the template's, and
🔄 Template Sync keeps it current in a vault. A document you add here is
**yours from the first commit**: nothing upstream ever writes, moves or removes
it. The log below is redrawn from the files the folder holds.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                                      | Purpose                                                                                                                                                                                                               |
| :--------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`Personal-Data-&-Secrets.md`](Personal-Data-&-Secrets.md) | Why a vault generated from this template stays private, how a secret is referenced without being stored, the scan that guards both, and what to do when something leaks. Read it before you touch anything sensitive. |
| [`README.md`](README.md)                                   | This file.                                                                                                                                                                                                            |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push to the default branch,
from each document's own frontmatter.

---

## 🔗 See also

- [Documentation index](../README.md) - every document the vault keeps in `.docs/`
- [Operations & Security](https://github.com/tannergolden/standards/blob/Development/docs/operations/README.md) - the shared guardrails: protection, dependencies, secrets and troubleshooting

---

<div align="center">

**Write the runbook before the night you need it.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
