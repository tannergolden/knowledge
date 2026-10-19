<!--
title: '🛡️ SECURITY POLICY'
description: 'How this vault keeps personal data and secrets out of reach, and how to report a problem with either.'
tags: [security, privacy, secrets, obsidian-vault]
category: docs
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🛡️ SECURITY POLICY

<a name="top"></a>

**How this vault keeps personal data and secrets out of reach.**

_Private by design, pointers instead of secrets._

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
pointer to where it lives. The rules and the scans that enforce them are standards':

- [The golden rules of secrets](https://github.com/tannergolden/standards/blob/Development/docs/operations/Security-&-Secrets.md#-the-golden-rules-of-secrets)
- [The automated guardians](https://github.com/tannergolden/standards/blob/Development/docs/operations/Security-&-Secrets.md#-automated-guardians), which
  include the gitleaks scan `checks.yml` runs on every push and pull request.

The vault adds one scan of its own: `python3 .github/scripts/scan-pii.py` checks every tracked file
for Social Security and card numbers, and CI runs it through `check-vault.py`.

---

## 📣 Reporting A Vulnerability

> [!IMPORTANT]
> Do not open a public issue. Report privately.

Contact the owner through [their GitHub profile](https://github.com/tannergolden) with what you
found, where, and how to reproduce it. You will get an acknowledgement, and a fix or a clear
explanation of why no change is needed.

If a secret is ever committed, follow standards'
[incident response protocol](https://github.com/tannergolden/standards/blob/Development/docs/operations/Security-&-Secrets.md#-incident-response-protocol).

---

<div align="center">

**Personal data stays private; secrets never arrive.**

[↑ Back to Top](#top)

</div>
