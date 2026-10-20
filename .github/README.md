<!--
title: '🧠 BRAIN'
description: 'A public template for a personal knowledge vault: plain Markdown that gives any AI lasting, structured knowledge of one person.'
type: index
keywords: [knowledge-vault, ai-agents, template]
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🧠 BRAIN

<a name="top"></a>

**A personal context and memory vault for AI, in plain Markdown.**

_Generate your own, keep it private, and let the AI keep it current._

</div>

---

## 💡 What It Is

**BRAIN** stands for **B**ehavioral **R**ecursive **A**ugmented **I**ntelligence **N**etwork: it adapts to
its owner, refines what it holds over time, adds retrieval and memory to a model, and connects
memory, context and knowledge in one place.

It is a portable personal data layer for any AI agent, retrieval pipeline or context window: who
you are, what you are working on, and everything worth remembering. It relies on a consistent
folder layout and clean hidden frontmatter alone, so any model that can read files can use it: no
database, no embeddings required, no vendor lock-in. Claude, GPT, Gemini, a LangChain pipeline or
a custom agent all read it the same way.

> [!NOTE]
> This is a living system, not an archive. The AI maintains it: it reads from it, writes to it,
> and keeps it current as it learns.

---

## 🚀 Make Your Own

- [ ] **Generate a repository from this template, and make it private.** It is made to hold who
      you are, and every rule in it assumes it stays private.
- [ ] **Let initialisation run.** It makes the vault yours (the licence holder and the code owner)
      and removes what only the template needs. If nothing happens, dispatch
      🎯 Standards Lifecycle from the Actions tab.
- [ ] **Open the folder with an AI agent**, and work with it there. Every agent reads
      [`AGENTS.md`](../AGENTS.md) first.
- [ ] **Fill in `Profile/`** with the `/identify` skill, which interviews you and writes only what you
      confirm.
- [ ] **Stay current.** Run 🔄 Template Sync when you want this template's improvements, and let
      🔁 Intelligence Sync keep the universal rules in `AGENTS.md` up to date. Both open a pull
      request; neither changes anything you have not merged.

[Setting Up A Vault](../.docs/introduction/Setting-Up-A-Vault.md) takes each step in turn, with the
settings the automation needs.

---

## 🧭 How It Is Governed

| Where                                                                 | What it holds                                                                                                    |
| :-------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------- |
| [`AGENTS.md`](../AGENTS.md)                                           | The rules every agent follows: the universal Constitution from `tannergolden/intelligence`, then the vault's own |
| Each folder's note                                                    | That folder's rules and procedures, read before working there                                                    |
| [`.docs/technical/vault/`](../.docs/technical/vault/README.md)        | The note schema, the keywords, the link topology, how to assemble context and how a session runs                 |
| [`tannergolden/standards`](https://github.com/tannergolden/standards) | How the repository itself works: commits, branches, releases, documents                                          |

---

## 🗂️ The Structure

```bash
.
├── AGENTS.md    # The rules every agent reads first
├── Inbox/       # Staging for unsorted files, plus the standing agent teams
├── Library/     # Reference knowledge in ten classes, never personal
├── Memory/      # What happened, who is around you, what you decided, what is due
├── Profile/     # Who you are: values, goals, skills, working style
├── Projects/    # Personal projects, one folder each
├── System/      # Workflows, the skills and the generated catalogs
└── Ventures/    # Each company you run, plus a shared agent workforce
```

Each top folder has a `README.md` for GitHub and a note named after it for the AI.
[How The Vault Works](../.docs/introduction/How-The-Vault-Works.md) says how the parts fit together,
and the [Glossary](../.docs/references/Glossary.md) defines the vault's own terms.

---

## ⚙️ The Scripts

The vault's checks and generators are small Python scripts in
[`.github/scripts/`](scripts/README.md). Each finds the vault from its own location, so the vault
works wherever it is placed, and [`vault.yml`](workflows/vault.yml) runs them all on every pull
request.

```bash
python3 .github/scripts/check-vault.py    # every check: notes, links, skills, agents, personal data, generated parts
python3 .github/scripts/update-vault.py   # redraw everything generated: memory tiers, link blocks, catalogs, skill archives
python3 .github/scripts/lint-notes.py X   # one note against the schema
```

`python3 .github/scripts/session.py start` lists what to read at the start of a session.
[Vault Scripts](../.docs/technical/Vault-Scripts.md) says how the scripts fit together, and what to
do when one fails.

---

## 🎯 Design Principles

- **Structured over freeform.** Every note carries frontmatter from a closed, checked vocabulary;
  nothing enters without it.
- **Relative over absolute.** No hardcoded paths: the vault works wherever it is placed.
- **Minimal over maximal.** Notes are filled in as information surfaces, never invented up front.
- **AI-maintained.** The AI keeps the vault current, so you do not have to.
- **Portable across models.** It works with any model that can read files.
- **Safe by construction.** Nothing is deleted without your yes, and git history keeps whatever is.

---

## 👤 The Developer

The BRAIN was designed and built by **Tanner Golden**: its folder structure, naming conventions,
agent instructions and scripts all originate with him, and "the developer" means him. "The user"
means whoever `Profile/` describes: the vault is portable, so the user is whoever adopts it.

<!-- The domain is capitalised on purpose: initialisation rewrites the template owner's
handle wherever it stands alone, and this address must survive in every vault. -->

Website: [TannerGolden.com](https://www.TannerGolden.com) · The template:
[`tannergolden/knowledge`](https://github.com/tannergolden/knowledge)

---

## 🤝 Working On The Template

Work on the template follows [`tannergolden/standards`](https://github.com/tannergolden/standards):
[Conventional Commits](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Conventional-Commits.md), the
[branching strategy](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Branching-Strategy-&-Workflow.md) and
[pull request reviews](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Pull-Requests-&-Code-Reviews.md). Read
[Working In The Vault](../.docs/introduction/Working-In-The-Vault.md) before you start, and
[Personal Data & Secrets](../.docs/operations/Personal-Data-&-Secrets.md) before you touch anything
sensitive. [How A Change Reaches A Vault](../.docs/distribution/How-A-Change-Reaches-A-Vault.md)
says what to do when you add a file the template ships. The code of conduct, the contributing guide
and the security policy are the account's, which GitHub serves to every repository that keeps none
of its own.

---

<div align="center">

**Your context, in your files, for any model you choose.**

[↑ Back to Top](#top)

<br />

Distributed under the MIT License.

</div>
