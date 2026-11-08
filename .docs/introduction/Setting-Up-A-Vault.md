<!--
title: '🚀 SETTING UP A VAULT'
description: 'How to make your own vault from this template: generating it private, what initialisation changes and leaves alone, the settings its automation needs, the first session, and how it stays current. Read it when you generate a vault, and again if initialisation or a sync pull request fails.'
type: guide
keywords: [setup, initialisation, generate, private repository, first session, profile interview, onboarding]
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
- **An editor, or any AI assistant that reads files.** The root `README.md` says how to work in the
  vault, each folder's `README.md` how to work in that folder, and `AGENTS.md` the rules every AI
  follows here, which most AI apps load by themselves.
- **The home kit** from [tannergolden/intelligence](https://github.com/tannergolden/intelligence) on
  each machine you work from, if you work with an AI assistant. The vault holds no skills: the kit
  installs them into each AI app and every Claude Code cloud session, and the root `README.md` says
  where each kind of work goes.

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
`tannergolden/standards`, and everything under `.github/workflows/`, so 🏷️ Cut Release stays, inert
outside a template.

> [!WARNING]
> A ruleset on the default branch blocks the push initialisation makes. Let it run first, and apply
> protection afterwards. A failed run is safe to re-run: the sentinel goes only on success.

Deleting `.github/TEMPLATE_INIT` by hand skips initialisation. Then set the licence holder in
`LICENSE` and the owner in `.github/CODEOWNERS` yourself, and delete `.github/template-derive.json`
and `.github/template-derive.lock`.

---

## ⚙️ Settings The Automation Needs

| Setting                                                                                                                                | Lets                                                                                                                    | Without it                                                                                                     |
| :------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------- |
| **Settings → Actions → General: allow GitHub Actions to create and approve pull requests**                                             | 🔄 Template Sync, 🗂️ Machined Indexes and 🔁 Intelligence Sync open their pull requests with the repository's own token | Unless a `BOT_ACCESS_TOKEN` opens them, none can open its pull request                                         |
| **A `BOT_ACCESS_TOKEN` secret**: the `repo` and `workflow` scopes, or fine-grained Contents, Pull requests, Issues and Workflows write | 🔄 Template Sync writes the stubs under `.github/workflows/`, and the checks run on its pull requests                   | Workflow files wait, named in an issue, and the checks on a pull request the default token opened wait for you |
| **🎯 Apply Standards**, dispatched after initialisation                                                                                | The shared labels and, with an `ADMIN_TOKEN`, the repository settings and the branch and tag rulesets                   | Labels and protection stay unset                                                                               |

🧠 Vault runs every vault check and the scripts' tests, and 🚦 Checks the repository validator, so
a vault's CI checks something real from its first commit.

---

## 🧠 The First Session

Clone the vault, open it, and start where every session starts:

```bash
python3 .github/scripts/session.py start
python3 .github/scripts/check-vault.py
python3 .github/scripts/profile-coverage.py
```

- **`session.py start`** lists what to read first: the root `README.md`, `Profile/Working Style.md`,
  `Memory/Log.md`, the two newest session summaries (none yet) and, when files wait at the Inbox,
  `Inbox/README.md` and each waiting file.
- **`check-vault.py`** runs every check CI runs, so your machine sees what 🧠 Vault sees.
- **`profile-coverage.py`** scores each of the twelve Profile facets and names the one to ask about
  next. Every facet starts as a blank scaffold.
- **Fill `Profile/` with the `human-resources` skill.** Its profile interview reads that report,
  interviews you about one facet at a time, and writes only the proposals you approve; it opens
  Health, Finances, Values and Relationships only when you choose to. It starts with
  `Profile/Working Style.md`, which the report names first while it is blank, and which says how
  you want to be helped.
- **Drop files into `Inbox/`** to have them sorted into the vault, with your yes for each move.
- **Turn on an offline reference work** if you want one:
  `Library/Reference & Encyclopedia/README.md` lists the sources, every one off at first.

A session commits what it writes, and pushing stays yours.

---

## 🌿 Staying Current

Three automations keep your vault current, each as a pull request you merge:

- **🔄 Template Sync**, when you run it, brings the template's released fixes, each file merged with
  your changes, from the latest release of the major your vault follows: `v2` for a vault generated
  now. One generated before v2.0.0 follows `v1` until you set `ref: 'v2'` in its stub,
  `.github/workflows/template-sync.yml`. Put a `#` before a line in `.github/template-sync` to keep
  that file as yours.
- **🗂️ Machined Indexes**, after each push to the default branch, proposes the redrawn folder logs.
- **🔁 Intelligence Sync**, every Monday, proposes the universal rules of each new
  tannergolden/intelligence release for the block at the top of `AGENTS.md`, and leaves the rest of
  the file alone.

No sync touches the notes you write, nor the files the list leaves to you: `Memory/Log.md`,
`Memory/Dates.md`, the eight flat Profile facets, the catalog and the Intelligence Sync stub.
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
