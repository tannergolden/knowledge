<!--
title: '🧠 BRAIN'
description: 'A public template for a personal knowledge vault: plain Markdown that gives any AI lasting, structured knowledge of one person.'
type: index
keywords: [knowledge-vault, ai-context, template]
-->

<!-- The Markdown Kit's blocks: the header here, and the trophy case and the footer at the foot. In
a vault, 📝 Markdown draws into each; here they hold the typed masthead and footer. -->

<!-- markdown:header:start -->
<!-- markdownlint-disable MD041 -->
<div align="center">

# 🧠 BRAIN

<a name="top"></a>

**A personal context and memory vault for AI, in plain Markdown.**

_Generate your own, keep it private, and let the AI keep it current._

</div>
<!-- markdown:header:end -->

---

## 💡 What It Is

**BRAIN** stands for **B**ehavioral **R**ecursive **A**ugmented **I**ntelligence **N**etwork: a
portable personal data layer for any AI agent, retrieval pipeline or context window. It holds who
you are, what you are working on, and everything worth remembering, in plain Markdown.

It relies on a consistent folder layout and clean hidden frontmatter alone, so any model that can
read files can use it: no database, no embeddings required, no vendor lock-in. The AI maintains it:
it reads from it, writes to it, and keeps it current as it learns. Its principles: structured over
freeform, relative over absolute, minimal over maximal, portable across models, and safe by
construction, since nothing is deleted without your yes and git history keeps whatever is.

- **Status**: Active. The template, `tannergolden/knowledge`, holds no personal context; each vault
  generated from it is a private repository made to hold its owner's.

---

## 🚀 Quick Start

- [ ] **Generate a repository from this template, and make it private.** It is made to hold who
      you are, and every rule in it assumes it stays private.
- [ ] **Let initialisation run.** It makes the vault yours (the licence holder and the code owner)
      and removes what only the template needs. If nothing happens, dispatch
      🎯 Standards Lifecycle from the Actions tab.
- [ ] **Open the folder with any AI assistant, or in an editor**, and work in it there.
- [ ] **Fill in `Profile/`** with the profile interview `Profile/README.md` describes: ask any AI
      assistant working in the vault to run it, and it interviews you and writes only what you
      confirm.

[Setting Up A Vault](../.docs/introduction/Setting-Up-A-Vault.md) takes each step in turn, with the
settings the automation needs.

---

## 📖 Using It

| Where                                                          | What it holds                                                                                            |
| :------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------- |
| [`README.md`](../README.md) at the root                        | How to work in the vault: the top folders, a session, the commands and where each kind of work goes      |
| [`AGENTS.md`](../AGENTS.md) at the root                        | The rules every AI follows here: the universal rules, then the rules for working with personal knowledge |
| Each folder's `README.md`                                      | That folder's purpose, rules and procedures, read before working there                                   |
| [`.docs/technical/vault/`](../.docs/technical/vault/README.md) | The note schema, the keywords, the link topology, how to assemble context and how a session runs         |

```bash
.
├── AGENTS.md    # The rules every AI follows here: the universal ones, then the vault's
├── README.md    # How to work in the vault: read it first
├── Inbox/       # Staging for unsorted files, plus the held research, visuals and ideas
├── Library/     # Reference knowledge in ten classes, never personal
├── Memory/      # What happened, who is around you, what you decided, what is due
├── Profile/     # Who you are: values, goals, skills, working style
├── Projects/    # Personal projects, one folder each
├── System/      # Standing settings, the workflow map and the generated catalog
└── Ventures/    # Each company you run, one folder each
```

The vault's checks and generators are small Python scripts in
[`.github/scripts/`](scripts/README.md), and [`vault.yml`](workflows/vault.yml) runs every check on
every pull request and every push to the default branch:

```bash
python3 .github/scripts/check-vault.py    # every check: notes, links, personal data, ignored files, generated parts
python3 .github/scripts/update-vault.py   # redraw everything generated: memory tiers, lists, the catalog
python3 .github/scripts/session.py start  # what a session reads first
```

**Staying current.** Run 🔄 Template Sync when you want this template's improvements: it opens a
pull request and changes nothing you have not merged. 🔁 Intelligence Sync keeps the universal
rules in `AGENTS.md` current on its own, with a pull request each time `tannergolden/intelligence`
releases new ones. [How The Vault Works](../.docs/introduction/How-The-Vault-Works.md) says how the
parts fit together.

---

## 🤝 Getting Involved

- **Questions**: [`SUPPORT.md`](SUPPORT.md) says where to ask.
- **A change to the template**: read
  [Working In The Vault](../.docs/introduction/Working-In-The-Vault.md) first, and
  [Personal Data & Secrets](../.docs/operations/Personal-Data-&-Secrets.md) before you touch
  anything sensitive. [`CONTRIBUTING.md`](CONTRIBUTING.md) explains how, and the work follows
  [`tannergolden/standards`](https://github.com/tannergolden/standards) by link.
- **Who decides**: [`GOVERNANCE.md`](GOVERNANCE.md) names the maintainers, and every contribution
  follows the [code of conduct](CODE_OF_CONDUCT.md).

### 👤 The Developer

The BRAIN was designed and built by **Tanner Golden**: its folder structure, naming conventions,
documentation and scripts all originate with him, and "the developer" means him. "The owner",
whom the universal rules in `AGENTS.md` call the user, means whoever
`Profile/` describes: the vault is portable, so its owner is whoever adopts it.

<!-- The domain is capitalised on purpose: initialisation rewrites the template owner's
handle wherever it stands alone, and this address must survive in every vault. -->

Website: [TannerGolden.com](https://www.TannerGolden.com) · The template:
[`tannergolden/knowledge`](https://github.com/tannergolden/knowledge)

---

## 🛡️ Security

Report a vulnerability privately, never in an issue: [`SECURITY.md`](SECURITY.md) says how, and
how fast a fix follows.

---

## ⚖️ Licence

The BRAIN is released under the terms in [LICENSE](/LICENSE).

---

<!-- markdown:trophies:start -->
<!-- markdown:trophies:end -->

<!-- markdown:footer:start -->
<div align="center">

**Your context, in your files, for any model you choose.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
<!-- markdown:footer:end -->
