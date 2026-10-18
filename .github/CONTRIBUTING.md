<div align="center">

# 🛠️ Contributing

Thanks for working on the BRAIN. This vault is governed, so a little orientation goes a long way.

</div>

## Read these first

The BRAIN is not an ordinary repository. Before you change anything, orient yourself:

1. [`AGENTS.md`](../AGENTS.md) is the front door. It points you at the canonical documents in the order you should read them.
2. [`Constitution.md`](../Constitution.md) is non negotiable governance and wins every conflict.
3. [`Instructions.md`](../Instructions.md) is the operating manual: structure, protocols, and the frontmatter schema.

An AI agent's first move is `python3 System/brain.command startup`, which loads the orientation set in one call.

## The rules that matter most

> [!IMPORTANT]
> These are enforced, not aspirational.

- **Every Markdown content file carries YAML frontmatter** from the closed vocabulary in Constitution Article VII. `python3 System/brain.command lint` is the gate.
- **Back up before editing**, or commit often. In a vault with a reachable git remote, git history is the backstop; locally, the engine writes a pre-edit snapshot to `.backups/`.
- **Never delete a file without confirmation.** Deletion is two stage (`trash` then `trash empty`) locally, or a recoverable `git rm` when remote.
- **Never restructure the top-level folders.** Layer 0 and Layer 1 are frozen (Constitution Article II).
- **Secrets are pointers, not values.** Never commit a key, token, or credential. A pre-push hook scans for them.

## Commit convention

Commits follow the **AI-Driven Commit Process**: [Conventional Commits](https://www.conventionalcommits.org), one intent per commit.

```
<type>(<scope>): <emoji> <summary>
```

- **Type:** one of `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`, `security`
- **Summary:** imperative, lowercase, 72 characters or fewer, with exactly one emoji
- **Body:** two to four sentences on the what, the why, and the impact, plus up to six bullets

A `commit-msg` hook validates every message. Wire the hooks once per clone with `python3 System/brain.command install-hooks`.

```
feat(secrets): ✨ add a pre-push scan for keys and PII
docs(readme): 📝 document the engine command surface
fix(memory): 🐛 stop the tier cascade from doubling date prefixes
```

## Before you push

Run the full health check and make sure it is green:

```bash
python3 System/brain.command health   # lint, links, stale, drift, secrets, and more
```

Then push. The pre-push hook runs the secret scan; the commit-msg hook already validated your message. If something is a genuine false positive, an inline `brain-allow-secret` marker or `git commit --no-verify` will bypass a single check, but use these sparingly.

<div align="center">

---

Questions go to **[Tanner Golden](https://github.com/tannergolden)**.

</div>
