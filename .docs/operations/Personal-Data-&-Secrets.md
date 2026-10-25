<!--
title: '🛡️ PERSONAL DATA & SECRETS'
description: 'Why a vault generated from this template stays private, how a secret is referenced without being stored, the scan that guards both, and what to do when something leaks. Read it before you touch anything sensitive.'
type: standard
keywords: [privacy, pii, security, vulnerability]
-->

<div align="center">

# 🛡️ PERSONAL DATA & SECRETS

<a name="top"></a>

**What the vault keeps private, and the one thing it never keeps at all.**

_Personal data stays private; secrets never arrive._

</div>

---

## 🔐 The Vault Holds Personal Data

A vault generated from this template holds biographical, relational and other sensitive
information about its owner, so it is kept **private**: generate it as a private repository and
keep it that way. This template itself is public, and every note in it about a person is a blank
scaffold.

---

## 🗝️ Secrets Are Pointers, Not Values

No secret is ever stored in this vault as a value: where one must be referenced, the vault holds a
pointer to where it lives. The rules and the scans that enforce them are the standards':

- [The golden rules of secrets](https://github.com/tannergolden/standards/blob/Development/docs/operations/Security-&-Secrets.md#-the-golden-rules-of-secrets)
- [The automated guardians](https://github.com/tannergolden/standards/blob/Development/docs/operations/Security-&-Secrets.md#-automated-guardians),
  which include the gitleaks scan `checks.yml` runs on every push and pull request.

The vault adds one scan of its own: `python3 .github/scripts/scan-pii.py` checks every tracked file
for Social Security and card numbers, and CI runs it through `check-vault.py`.

---

## 📣 When Something Leaks

> [!IMPORTANT]
> Never report a vulnerability in a public issue.

A vulnerability goes through the account's security policy, which GitHub serves to this repository
from the account's `.github` repository and shows on its Security tab.

If a secret is ever committed, follow the standards'
[incident response protocol](https://github.com/tannergolden/standards/blob/Development/docs/operations/Security-&-Secrets.md#-incident-response-protocol).

---

<div align="center">

**A pointer to a secret, never the secret itself.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
