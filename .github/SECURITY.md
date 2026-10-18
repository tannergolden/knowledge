<div align="center">

# 🔐 Security Policy

</div>

## The vault holds personal data

This repository is a personal context and memory system. It contains biographical, relational, and other sensitive information about its owner, and it is kept **private** by design. Treat everything here as confidential.

## Secrets are pointers, not values

The single most important rule: **no secret is ever stored as a value in this vault.** No API keys, tokens, passwords, or credentials belong in any file. Where a secret must be referenced, the vault stores a pointer to where it lives (a password manager, an environment variable, a vault service), never the secret itself.

This is machine enforced:

- `python3 System/brain.command secrets` scans all tracked text for cloud keys, tokens, private-key blocks, SSNs, and card numbers.
- A **pre-push git hook** runs that scan and blocks any push that would ship a secret.
- The scan also runs inside `python3 System/brain.command health` as a standing check.

Wire the hooks on a fresh clone with `python3 System/brain.command install-hooks`.

## Reporting a vulnerability

If you discover a security issue, a leaked secret in history, or a weakness in the vault's safeguards:

> [!IMPORTANT]
> Do not open a public issue. Report privately.

Contact the owner, **Tanner Golden**, through [github.com/tannergolden](https://github.com/tannergolden). Please include what you found, where, and how to reproduce it. You will get an acknowledgement, and a fix or a clear explanation of why no change is needed.

## If a secret is ever committed

1. Treat it as compromised and rotate it immediately at its source.
2. Remove it from the working tree and from history.
3. Record the incident and the rotation so the same value is never trusted again.

A private repository is not a safe place for a live secret. Rotation, not obscurity, is the remedy.

<div align="center">

---

Thank you for helping keep this system secure.

</div>
