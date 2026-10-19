<!--
title: '🧠 VAULT CHECKS ACTION'
description: 'Checks every note, wikilink, skill, agent and generated part of the vault, and tests the scripts that do it.'
tags: [github-actions, composite-action, vault, validation]
category: docs
-->

<div align="center">

# 🧠 VAULT CHECKS ACTION

<a name="top"></a>

**Every vault check, as one step.**

_The scripts check the vault. The action runs them. The workflow runs the action._

</div>

---

## 💡 What This Folder Is For

`action.yml` runs [`check-vault.py`](../../scripts/check-vault.py), which runs
each vault check in turn: the note schema, the wikilink graph, the skills, the
agent library, the scan for personal numbers, and `update-vault.py --check`,
which fails when a generated part is out of date. It then runs the unit tests
of every script in [`.github/scripts/`](../../scripts/README.md). Set the
`tests` input to `'false'` to skip the tests.

[`vault.yml`](../../workflows/vault.yml) runs it on every pull request and
every push to the default branch, with no template guard, so the template is
held to the same checks as every vault made from it.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                      | Purpose                                                                                                                                 |
| :------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| [`action.yml`](action.yml) | The vault's checks as one step: every check in .github/scripts/, through check-vault.py, then the unit tests of the scripts themselves. |
| [`README.md`](README.md)   | This file.                                                                                                                              |

<!-- AUTO-INDEX:END -->

---

<div align="center">

**Checked by the scripts, run by the action, called by the workflow.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](../../../LICENSE).

</div>
