<div align="center">

# 🧠 BRAIN

**A portable, file-based personal context and memory system for AI.**

One folder of plain Markdown that gives any AI model persistent, structured
knowledge of a person: who they are, what they are working on, and everything
worth remembering. Model agnostic, embedding agnostic, location independent.

![License](https://img.shields.io/badge/license-proprietary-b23a35.svg)
![Access](https://img.shields.io/badge/access-private%20%26%20confidential-b23a35.svg)
![Format](https://img.shields.io/badge/format-Markdown-16202b.svg)
![AGENTS.md](https://img.shields.io/badge/AGENTS.md-standard-b9761f.svg)

</div>

---

> [!IMPORTANT]
> **Private and confidential.** This repository and everything in it are the private property of Tanner Golden. It is not open source, and no license is granted. No one may use, copy, distribute, or disclose any part of it, or discuss it, without written permission. See [`LICENSE`](../LICENSE).

## What it is

**BRAIN** stands for **B**ehavioral **R**ecursive **A**ugmented **I**ntelligence **N**etwork. It is a personal data layer designed to be dropped into any RAG system, AI agent, or context window. It relies entirely on a consistent folder layout and clean YAML frontmatter, so any model that can read files can use it, with no vendor lock in and no database required.

The BRAIN travels with its owner. It can be loaded into Claude, GPT, Gemini, a LangChain pipeline, or a custom agent, and the structure reads the same everywhere.

> [!NOTE]
> This is a living system, not a static archive. The AI maintains it: reading from it, writing to it, and keeping it current as it learns.

## How it is governed

Two documents at the root rule everything an AI does here:

| Document | Role |
|----------|------|
| [`Constitution.md`](../Constitution.md) | Non negotiable governance. Wins every conflict. |
| [`Instructions.md`](../Instructions.md) | The operating manual: structure, protocols, the frontmatter schema. |
| [`AGENTS.md`](../AGENTS.md) | The front door for any agent, following the [AGENTS.md](https://agents.md) standard. |

An agent's first move on arrival is to read the Constitution, then the Instructions, then run the startup checklist. Everything else follows from there.

## The structure

```
BRAIN/
├── Constitution.md     Governance. Non negotiable.
├── Instructions.md     The operating manual.
├── Information.md       What the BRAIN is.
├── Library/            Universal reference knowledge, a Dewey-like taxonomy.
├── Profile/            Who the owner is: values, goals, skills, working style.
├── Memory/             Continuity across sessions: log, decisions, entities, summaries.
├── Ventures/           Business context, plus a reusable agent workforce.
├── Projects/           Personal projects and initiatives.
├── Inbox/              Staging for unsorted input, plus the standing agent faculties.
└── System/             Workflows, the skills, and the generated catalogs.
```

## The scripts

The vault's checks and generators are small Python scripts in [`.github/scripts/`](scripts/README.md). Each finds the vault from its own location, so the vault works wherever it is placed, and [`vault.yml`](workflows/vault.yml) runs them all on every pull request.

```bash
python3 .github/scripts/check-vault.py    # every check: notes, links, skills, agents, personal data, generated parts
python3 .github/scripts/update-vault.py   # redraw everything generated: memory tiers, link blocks, catalogs, skill archives
python3 .github/scripts/lint-notes.py X   # one note against the frontmatter schema
```

In Claude Code the hooks run them on their own: the session start lists what to read, every note written is checked, and the end of a turn redraws what is generated.

## What makes it different

- **Structured over freeform.** Every file carries YAML frontmatter drawn from a closed, linted vocabulary. Nothing enters without metadata.
- **Governed, not vibes.** A written Constitution, a git history every change is committed to, and checks CI runs on every pull request (the frontmatter schema, the wikilink graph, the skills, the agents, and scans for secrets and personal numbers) keep the vault honest.
- **A workforce, not just notes.** The BRAIN ships its own skills (research, editorial, visualize, discover, identify, board) that compose teams of specialized agents, and builds new ones with the universal `develop` skill.
- **Safe by construction.** Nothing is deleted without confirmation, and nothing deleted is lost, since git history keeps it; and a "secrets are pointers, not values" rule that CI's scans back.

## Working in this repository

Commits follow the [AI-Driven Commit Process](.github/CONTRIBUTING.md) (Conventional Commits, one intent per commit), checked on every pull request. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before you start, [`SECURITY.md`](SECURITY.md) before you touch anything sensitive, and [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) for how we work together.

<div align="center">

---

Built and maintained by **[Tanner Golden](https://github.com/tannergolden)** &middot; [tannergolden.com](https://www.tannergolden.com)

</div>
