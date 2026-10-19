<div align="center">

# 🛠️ Contributing

Thanks for working on the BRAIN. This vault is governed, so a little orientation goes a long way.

</div>

## Read these first

The BRAIN is not an ordinary repository. Before you change anything, orient yourself:

1. [`AGENTS.md`](../AGENTS.md) is the front door. It points you at the canonical documents in the order you should read them.
2. [`Constitution.md`](../Constitution.md) is non negotiable governance and wins every conflict.
3. [`Instructions.md`](../Instructions.md) is the operating manual: structure, protocols, and the frontmatter schema.

An AI agent's first move is the Instructions Section 9 checklist; in Claude Code, the SessionStart hook lists the files to read.

## The rules that matter most

> [!IMPORTANT]
> These are enforced, not aspirational.

- **Every Markdown content file carries YAML frontmatter** from the closed vocabulary in Constitution Article VII. `python3 .github/scripts/lint-notes.py` is the gate, after every edit and in CI.
- **Changes are commits.** Git history is the backup and the change record; commit before a risky edit.
- **Never delete a file without confirmation.** An approved deletion is a `git rm`, recoverable from history.
- **Never restructure the top-level folders.** Layer 0 and Layer 1 are frozen (Constitution Article II).
- **Secrets are pointers, not values.** Never commit a key, token, or credential. CI scans every push for them, and for personal numbers.

## Commit convention

Commits follow the **AI-Driven Commit Process**: [Conventional Commits](https://www.conventionalcommits.org), one intent per commit.

```
<type>(<scope>): <emoji> <summary>
```

- **Type:** one of `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`, `security`
- **Summary:** imperative, lowercase, 72 characters or fewer, with exactly one emoji
- **Body:** two to four sentences on the what, the why, and the impact, plus up to six bullets

The commit check on every pull request validates each message against these rules.

```
feat(secrets): ✨ add a pre-push scan for keys and PII
docs(readme): 📝 document the vault scripts
fix(memory): 🐛 stop the tier cascade from doubling date prefixes
```

## Before you push

Run every vault check and make sure it is green:

```bash
python3 .github/scripts/check-vault.py   # notes, links, skills, agents, personal data, generated parts
```

Then push. CI runs the same checks, the secret scan and the commit check. A reviewed false positive in the personal-number scan is kept by putting `pii-allow` in a comment on its line; use it sparingly.

<div align="center">

---

Questions go to **[Tanner Golden](https://github.com/tannergolden)**.

</div>
