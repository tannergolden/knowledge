<!--
title: '🛠️ CONTRIBUTING'
description: 'How to change this vault: read its rules, keep every note to the schema, and commit the way the standards say.'
type: guide
keywords: [workflow, standards]
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🛠️ CONTRIBUTING

<a name="top"></a>

**How to change this vault without breaking what it promises.**

_Read the rules, keep the schema, commit the standard way._

</div>

---

## 🧭 Read These First

1. [`AGENTS.md`](../AGENTS.md): the rules every agent follows, the universal Constitution first,
   then the vault's own. People follow them too.
2. The note of each folder you change, named after the folder (`Memory/Memory.md`): its Rules come
   first.
3. [`.docs/vault/`](../.docs/vault/README.md): the note schema, the keywords and the link
   topology the checks hold every note to.

---

## 📏 The Vault's Rules That Matter Most

> [!IMPORTANT]
> These are enforced, not aspirational.

- **Every note carries the schema's frontmatter**, tagged only from the closed vocabulary.
  `python3 .github/scripts/lint-notes.py` is the gate, after every edit and in CI.
- **Changes are commits.** Git history is the backup and the change record; commit before a risky
  edit.
- **Never delete a file without confirmation.** An approved deletion is a `git rm`, recoverable
  from history.
- **Never restructure the top folders.** They and the root are the owner's to change.
- **Keep personal data private.** In this public template every note about a person stays a blank
  scaffold.

---

## 🌿 Commits, Branches And Reviews

This repository follows [`tannergolden/standards`](https://github.com/tannergolden/standards), and
copies none of it here:

- **Commits:** [Conventional Commits](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Conventional-Commits.md), with a required
  scope, a body saying why and a `Signed-off-by:` line, which the DCO check on every pull request
  requires.
- **Branches:** the [branching strategy](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Branching-Strategy-&-Workflow.md).
- **Pull requests:** [pull requests and code reviews](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Pull-Requests-&-Code-Reviews.md).
- **Documents:** [document styling and formatting](https://github.com/tannergolden/standards/blob/Development/docs/technical/interface/Document-Styling-&-Formatting.md),
  which exempts the vault's notes from its hidden frontmatter and decorative headers.
- **Secrets:** [security and secrets](https://github.com/tannergolden/standards/blob/Development/docs/operations/Security-&-Secrets.md).

---

## 🚀 Before You Push

- [ ] Run every vault check and make sure it is green:

```bash
python3 .github/scripts/check-vault.py   # notes, links, skills, agents, personal data, generated parts
```

- [ ] Redraw anything it reports as stale with `python3 .github/scripts/update-vault.py`.
- [ ] Push. CI runs the same checks, the secret scan and the commit check. A reviewed false
      positive in the personal-number scan is kept by putting `pii-allow` in a comment on its line;
      use it sparingly.

---

<div align="center">

**Every note to the schema, every change a commit.**

[↑ Back to Top](#top)

<br />

Questions go to [@tannergolden](https://github.com/tannergolden).

</div>
