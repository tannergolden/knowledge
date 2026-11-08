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

Every AI that works in a vault is held to the same lines by `AGENTS.md`: the owner's context never
leaves the vault unasked (SEC-003), and a secret is recorded by where it lives, never by its value
(SEC-001). The [Check Nothing Personal Leaks](../Prompts.md#check-nothing-personal-leaks) prompt
audits a vault, or the template, against this page.

---

## 🗝️ Secrets Are Pointers, Not Values

No secret is ever stored in this vault as a value: where one must be referenced, the vault holds a
pointer to where it lives. The rules and the scans that enforce them are the standards':

- [The golden rules of secrets](https://github.com/tannergolden/standards/blob/Development/docs/operations/Security-&-Secrets.md#-the-golden-rules-of-secrets)
- [The automated guardians](https://github.com/tannergolden/standards/blob/Development/docs/operations/Security-&-Secrets.md#-automated-guardians),
  which include the gitleaks scan `checks.yml` runs on every pull request and every push to the
  default branch.

The vault adds one scan of its own: `python3 .github/scripts/scan-pii.py` checks every tracked text
file for Social Security and card numbers, and CI runs it through `check-vault.py`. A reviewed false
positive is kept by putting `pii-allow` in a comment on its line, sparingly.

---

## 📣 When Something Leaks

> [!IMPORTANT]
> Never report a vulnerability in a public issue.

A vulnerability goes through this repository's [security policy](../../.github/SECURITY.md), which
GitHub shows on its Security tab and which says how to report one privately.

If a secret is ever committed, follow the standards'
[incident response protocol](https://github.com/tannergolden/standards/blob/Development/docs/operations/Security-&-Secrets.md#-incident-response-protocol).

---

<div align="center">

**A pointer to a secret, never the secret itself.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
