<!--
title: '🚀 SETTING UP A VAULT'
description: 'How to make your own vault from this template: generating it private, what initialisation changes and leaves alone, the settings its automation needs, the first session, and how it stays current. Read it when you generate a vault, and again if initialisation or a sync pull request fails.'
type: guide
keywords: [setup, initialisation, generate, private repository, first session, identify, onboarding]
-->

<div align="center">

# 🚀 SETTING UP A VAULT

<a name="top"></a>

**From the Use this template button to a first session that knows its owner.**

_Generated private, claimed once, filled in by interview._

</div>

---

## 💡 Before You Start

- **A private repository.** The vault fills with who you are, so generate it private and keep it
  that way. [Personal Data & Secrets](../operations/Personal-Data-&-Secrets.md) says why.
- **git and Python 3.9 or later** on the machine you work from. The vault scripts need only Python's
  standard library; the repository validator also needs PyYAML, and the offline reference works need
  `libzim`.
- **An AI agent that reads files.** Every agent reads `AGENTS.md` first. The vault's skills sit
  where the apps look for them: `.agents/skills/`, with a copy in `.claude/skills/` for Claude Code.

The steps every repository on the standards shares, such as the admin token, 🎯 Apply Standards and
signed commits, are in the standards'
[What You Do By Hand](https://github.com/tannergolden/standards/blob/Development/docs/introduction/What-You-Do-By-Hand.md).
This page adds what a vault needs.

---

## 🚀 Generate & Initialise

- [ ] On [tannergolden/knowledge](https://github.com/tannergolden/knowledge), choose
      <kbd>Use this template</kbd>, and set the new repository to **Private**.
- [ ] Wait for 🎯 Standards Lifecycle to initialise it. GitHub does not always send the event that
      starts it: if nothing happens, dispatch 🎯 Standards Lifecycle from the Actions tab. Running it
      twice is harmless.
- [ ] Apply branch protection only after it has run, as below.

Initialisation runs once, and never in a template:

| It changes                   | How                                                                                                                                                                                                                                                                           |
| :--------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The owner's identity         | The template author's identity becomes yours: the licence holder and year in `LICENSE`, the owner in `.github/CODEOWNERS`, and the author's handle wherever it stands on its own                                                                                              |
| What only the template needs | Each file under "Only ever in the template" in `.github/template-sync` is deleted: the sentinel `.github/TEMPLATE_INIT`, the derivation `.github/template-derive.json` and its lock, and the template's own decision records in `.docs/adrs/`. Their lines stay, switched off |
| The folder logs              | Every `AUTO-INDEX` log is redrawn from what is left                                                                                                                                                                                                                           |
| The first commit             | Rewritten into a Conventional Commit, when it is the only commit                                                                                                                                                                                                              |

It leaves alone the addresses of the shared repositories a vault calls, such as
`tannergolden/standards`, the sealed block between the `INTELLIGENCE` markers in `AGENTS.md`, and
everything under `.github/workflows/`, so 🏷️ Cut Release stays, inert outside a template.

> [!WARNING]
> A ruleset on the default branch blocks the push initialisation makes. Let it run first, and apply
> protection afterwards. A failed run is safe to re-run: the sentinel goes only on success.

Deleting `.github/TEMPLATE_INIT` by hand skips initialisation. Then set the licence holder in
`LICENSE` and the owner in `.github/CODEOWNERS` yourself, and delete `.github/template-derive.json`
and `.github/template-derive.lock`.

---

## ⚙️ Settings The Automation Needs

| Setting                                                                                                                                | Lets                                                                                                                                                      | Without it                                                                                                     |
| :------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------- |
| **Settings → Actions → General: allow GitHub Actions to create and approve pull requests**                                             | 🔁 Intelligence Sync and 🔄 Template Sync open their pull requests with the repository's own token                                                        | Unless a `BOT_ACCESS_TOKEN` opens them, neither can open its pull request                                      |
| **A `BOT_ACCESS_TOKEN` secret**: the `repo` and `workflow` scopes, or fine-grained Contents, Pull requests, Issues and Workflows write | 🔄 Template Sync writes the stubs under `.github/workflows/`, and the checks run on its pull requests; 🔁 Intelligence Sync opens its pull request as you | Workflow files wait, named in an issue, and the checks on a pull request the default token opened wait for you |
| **🎯 Apply Standards**, dispatched after initialisation                                                                                | The shared labels and, with an `ADMIN_TOKEN`, the repository settings and the branch and tag rulesets                                                     | Labels and protection stay unset                                                                               |

`checks.yml` already runs the repository validator and the vault scripts' tests, so a vault's CI
checks something real from its first commit.

---

## 🧠 The First Session

Clone the vault, open it with your agent, and start where every session starts:

```bash
python3 .github/scripts/session.py start
python3 .github/scripts/check-vault.py
python3 .github/scripts/profile-coverage.py
```

- **`session.py start`** lists what to read first: `Profile/Working Style.md`, `Memory/Log.md`, the
  two newest session summaries (none yet) and any file waiting at the Inbox.
- **`check-vault.py`** runs every check CI runs, so your machine sees what 🧠 Vault sees.
- **`profile-coverage.py`** scores each of the twelve Profile facets and names the one to ask about
  next. Every facet starts as a blank scaffold.
- **Fill `Profile/` with `/identify`.** The skill reads that report, interviews you about one facet at
  a time, and writes only the proposals you approve; it opens Health, Finances, Values and
  Relationships only when you choose to. It starts with `Profile/Working Style.md`, which tells every
  agent how to work with you.
- **Drop files into `Inbox/`** to have them sorted into the vault, with your yes for each move.
- **Turn on an offline reference work** if you want one:
  `Library/Reference & Encyclopedia/Reference & Encyclopedia.md` lists the sources, every one off at
  first.

The agent commits what a session writes, and pushing stays yours.

---

## 🌿 Staying Current

Three automations bring outside change to your vault, each as a pull request you merge:

- **🔄 Template Sync**, when you run it, brings the template's released fixes, each file merged with
  your changes. Put a `#` before a line in `.github/template-sync` to keep that file as yours.
- **🔁 Intelligence Sync**, every Monday and on request, proposes the latest universal rules for the
  sealed block in `AGENTS.md`.
- **🗂️ Machined Indexes**, after each push to the default branch, proposes the redrawn folder logs.

No sync touches the notes you write, nor the files the list leaves to you: `Memory/Log.md`,
`Memory/Dates.md`, the eight flat Profile facets and the two catalogs.
[Template Sync](../../.github/template-sync.md) explains every outcome a sync pull request reports,
and [How A Change Reaches A Vault](../distribution/How-A-Change-Reaches-A-Vault.md) follows a change
from the template to your vault.

---

<div align="center">

**Generate it private, let it claim itself, then let it learn you.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
