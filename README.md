<!--
title: '🧠 HOW TO WORK IN THIS VAULT'
description: 'How this BRAIN vault is laid out and how to work in it: what each top folder holds, how a session goes, the commands, what done means, and where each kind of work goes. Read it first; the README.md at the root of each folder adds that folder''s rules.'
type: guide
keywords: [vault guide, sessions, folder readmes, conventions, where work goes]
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🧠 HOW TO WORK IN THIS VAULT

<a name="top"></a>

**What this vault holds, where each kind of work goes, and how to work in it.**

_This page for the whole vault, each folder's README for that folder._

</div>

---

## 💡 What This Vault Is

This repository is a BRAIN: a vault of plain Markdown that holds lasting, structured knowledge of
one person, its owner. [The front page](.github/README.md) says what a BRAIN is, how to make one
and how it is governed; this page says how to work in it, for anyone who does, a person or any AI.

It is either the public template, `tannergolden/knowledge`, which holds no personal context and
keeps every note about a person a blank scaffold, or a vault generated from it: **a private
repository made to hold its owner's personal context**, and kept private.

Every folder explains itself in a `README.md` at its root: what the folder is for, what belongs in
it, how to name and file things there, what not to do there, and how the checks enforce it. That
README is the folder's note. This page holds the rules for the whole vault, and a folder's README
adds to them and never loosens them. The vault holds no instructions for any particular assistant
and no agents: whoever works here reads the same pages.

---

## 🗂️ The Top Folders

| Folder      | Holds                                                                     | Its README                     |
| :---------- | :------------------------------------------------------------------------ | :----------------------------- |
| `Inbox/`    | Files waiting to be sorted, and the held reports, visuals and ideas       | [Inbox](Inbox/README.md)       |
| `Library/`  | Reference knowledge about the world, in ten classes, never personal       | [Library](Library/README.md)   |
| `Memory/`   | What happened, who is around the owner, what they decided and what is due | [Memory](Memory/README.md)     |
| `Profile/`  | Who the owner is; `Working Style.md` says how they want to be helped      | [Profile](Profile/README.md)   |
| `Projects/` | The owner's personal projects, one folder each                            | [Projects](Projects/README.md) |
| `Ventures/` | Each company the owner runs, one folder each                              | [Ventures](Ventures/README.md) |
| `System/`   | Standing settings, the workflow map and the generated catalog             | [System](System/README.md)     |

Hidden folders are infrastructure: `.github/scripts/` holds the vault's checks and generators,
`.docs/` its documentation, with the note schema, the keywords, the link topology and how to
assemble context in `.docs/technical/vault/`, and each `.template/` the scaffolds new notes are
copied from.

---

## 🌅 How A Session Goes

At the start of every session, before other work:

1. **Read `Profile/Working Style.md`.** It records how the owner wants to be helped, and it decides
   every choice this page, the folder READMEs and the `System/` files leave open.
2. **Check `Inbox/`.** If loose files wait there, they are sorted first, by the protocol in
   `Inbox/README.md`.
3. **Read `Memory/Log.md`** and the two newest summaries in `Memory/Context/Current/`.
4. **Read the README of each folder the task touches**, and of each folder above it, before
   anything there is created, edited, moved or deleted. A folder's rules add to this page and never
   loosen it. The catalog, `System/Data/catalog.ndjson`, says what exists without walking the tree.

`python3 .github/scripts/session.py start` lists what to read: this page, `Profile/Working Style.md`,
`Memory/Log.md` and the two newest summaries, then, when files wait, `Inbox/README.md` and each
waiting file.

- **Retrieval order.** A fact is grounded in the closest source that holds it: the vault (its notes
  and the catalog), then an offline knowledge base when one is installed
  (`python3 .github/scripts/knowledge-base.py search`), then the web. Anything about the owner stops
  at the vault; anything current goes straight to the web.
- **Writing.** A log entry, a session summary, a Memory or Profile entry, or a new project or venture
  is written in the format its folder's README shows; the scripts check the result and redraw what
  derives from it.
- **Keeping the vault current is part of every task.** What happened, was decided or is due is
  recorded in Memory and the Log without waiting to be asked. It is one of this vault's own rules,
  so it is part of the task asked, as the home kit's universal rule on scope, WORK-001, counts what
  a repository's rules require.
- **Checkpoints.** The running session summary is updated after each finished task, and one is
  written before the context runs short (`Memory/README.md`, Rules).

---

## ⚙️ Commands

Each runs from the vault root, on Python 3.9 or later, with nothing beyond the standard library but
the optional `libzim`, which only `knowledge-base.py` needs to search and read:

| Command                                                          | Does                                                                                                           |
| :--------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------- |
| `python3 .github/scripts/check-vault.py`                         | Every check CI runs: notes, links, personal data and generated parts                                           |
| `python3 .github/scripts/update-vault.py`                        | Redraws everything generated: the memory tiers, the generated lists, the catalog and the `.gitkeep` markers    |
| `python3 .github/scripts/lint-notes.py "<note>"`                 | One note against the schema; `check-links.py` and `scan-pii.py` check one part each                            |
| `python3 .github/scripts/session.py start`                       | Lists what a session reads first; `after-edit` checks a note once it is written, and `stop` redraws and checks |
| `python3 .github/scripts/profile-coverage.py --json`             | Scores each Profile facet and names the one to ask about next                                                  |
| `python3 .github/scripts/knowledge-base.py`                      | Turns on, fetches, searches and reads the offline reference works                                              |
| `python3 -m unittest discover -s .github/scripts -p 'test_*.py'` | The scripts' own tests                                                                                         |

After any write, whatever makes it, `lint-notes.py` runs on each note written, then
`update-vault.py`, then `check-vault.py`. Each script's purpose is in
[`.github/scripts/README.md`](.github/scripts/README.md).

---

## ✅ What Done Means

- `check-vault.py` passes, and `update-vault.py` has nothing left to redraw.
- Every note written carries [the note schema](.docs/technical/vault/Note-Schema.md), and
  `lint-notes.py` passes on it.
- The change is committed, with a message that follows
  [Conventional Commits](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Conventional-Commits.md).
- The owner knows which files changed and what is not yet committed.

---

## 📍 Where Each Kind Of Work Goes

Every kind of work has a fixed home here, whoever does it. A vault generated from this template is a
private repository made to hold its owner's personal context; in the public template nothing
personal is written.

The skills the home kit installs are twelve, one for each department and named for it, and each
covers both a company the owner runs and the owner's own life. A company's records go in its venture
folder, `Ventures/<Venture>/`, each department's in the folder named for it; the owner's own life
goes to the folders of this vault, each by its README's rules:

| Skill                      | A company's records, in `Ventures/<Venture>/`                                                                                                            | The owner's own life, in this vault                                                                                                                          |
| :------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `administration`           | `Administration/`, with the venture's `Overview.md`, `Goals.md` and `Log.md`: founding, strategy, decisions across departments and the operating cadence | Decisions in `Memory/Decisions/`, dates and commitments in `Memory/Dates.md`, and goals and priorities proposed for `Profile/Goals/` and `Profile/Focus.md`  |
| `finance-and-accounting`   | `Finance & Accounting (F&A)/`: the books, the financial model, the cap table and company tax                                                             | Budget, debt, taxes, investing, insurance and estate as the picture in `Profile/Finances.md`, and dated bills in `Memory/`                                   |
| `legal-and-compliance`     | `Legal & Compliance (L&C)/`: formation, contracts, IP, compliance and privacy                                                                            | Leases, contracts and wills by reference only, where each is kept, in `Profile/Finances.md`, and a dispute's dates and open loops in `Memory/`               |
| `sales-and-marketing`      | `Sales & Marketing (S&M)/`: the pipeline and deals, positioning and demand                                                                               | A job search or a personal brand as a project in `Projects/`, the people met networking in `Memory/`, and what a negotiation settles in `Memory/Decisions/`  |
| `operations-and-logistics` | `Operations & Logistics (O&L)/`: processes, programs and vendors                                                                                         | A household plan, a trip or a move as a project in `Projects/`, its dates, contractors and events in `Memory/`, and routines proposed for `Profile/Focus.md` |
| `human-resources`          | `Human Resources (HR)/`: roles, hiring, pay, onboarding and the people records                                                                           | The profile interview, career and skills, health and wellbeing, in `Profile/` by `Profile/README.md`'s rules                                                 |
| `information-technology`   | `Information Technology (IT)/`: the internal systems and their security                                                                                  | The devices, accounts and tools the owner uses, proposed for `Profile/Preferences.md` and never with a password or key, and a security incident in `Memory/` |
| `research-and-development` | `Research & Development (R&D)/`: research, ideas, and the building of products, skills and software                                                      | Reports in `Inbox/Reports/`, ideas in `Inbox/Ideas/`, learning in `Library/`, and side projects in `Projects/`                                               |
| `business-intelligence`    | `Business Intelligence (BI)/`: metrics, data, dashboards, and any chart or diagram                                                                       | Visuals in `Inbox/Visuals/`, and a habit or metric the owner tracks as a project in `Projects/`                                                              |
| `quality-assurance`        | `Quality Assurance (QA)/`: the independent verification of consequential work                                                                            | A check of an important document or plan, logged with what it checked, such as in its project's `Log.md`                                                     |
| `customer-experience`      | `Customer Experience (CX)/`: onboarding, success and support                                                                                             | A complaint, a return or a warranty as an open loop in `Memory/Log.md` and a date in `Memory/Dates.md`, and the company in `Memory/Entities/Organizations/`  |
| `public-relations`         | `Public Relations (PR)/`: announcements, press and crises                                                                                                | The owner's writing as a project in `Projects/`, and what an email commits them to, or a moment that touches their reputation, in `Memory/`                  |

- **A venture** is created only with the owner's yes, by copying `Ventures/.template/` whole, as
  `Ventures/README.md` says. The `administration` skill keeps its strategy in
  `Administration/Strategy.md`, records each of its decisions in `Administration/Decisions.md`, and
  logs its work in the venture's `Log.md`.
- **Reports** are held in `Inbox/Reports/` and **ideas** in `Inbox/Ideas/`, a company's as well as
  the owner's, until what must outlive them is promoted, such as into a venture's
  `Research & Development (R&D)/`, and a standalone **visual** is held in `Inbox/Visuals/`, each by
  that folder's README.
- **The owner's profile** is written in `Profile/` from `Profile/.template/`, by
  `Profile/README.md`'s rules, and is read-only until the owner asks or confirms. The profile
  interview, such as the `human-resources` skill's, picks the next facet with
  `python3 .github/scripts/profile-coverage.py --json`, and the people, events, dates and decisions it
  learns are promoted to `Memory/` by `Memory/README.md`.
- **The owner's own money facts** go only where `Profile/` and its rules allow, in
  `Profile/Finances.md`: an account, a policy or a document is recorded as where it is kept, never
  its number.
- **The Library** is the reference collection in `Library/`, with its rules in `Library/README.md`:
  what is learned about the world, never anything personal. Its notes are found by search and by
  the catalog's `BRAIN/Library/` records, and the offline reference works it keeps are searched
  with `python3 .github/scripts/knowledge-base.py search`.
- **A skill** that `research-and-development` builds is not vault content: it lives in
  tannergolden/intelligence or an AI app's own skills folder (`Inbox/README.md`, System Assets).

The README of each of these folders says which skill's work lands there and by what rules, so
whoever writes there learns it from that folder.

---

## 📏 Conventions

The vault follows [tannergolden/standards](https://github.com/tannergolden/standards) for everything
a repository does:
[commits](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Conventional-Commits.md),
[branches](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Branching-Strategy-&-Workflow.md),
[pull requests](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Pull-Requests-&-Code-Reviews.md),
[releases](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Releases-&-Versioning.md),
[secrets](https://github.com/tannergolden/standards/blob/Development/docs/operations/Security-&-Secrets.md)
and
[documents](https://github.com/tannergolden/standards/blob/Development/docs/technical/interface/Document-Styling-&-Formatting.md).
What it does differently, and why:

- **Notes open with hidden frontmatter.** Each opens with the HTML-comment block of
  [the note schema](.docs/technical/vault/Note-Schema.md), the account's own standard, and is found
  by its path, its title and a few [keywords](.docs/technical/vault/Keywords.md), never by tags, with
  no decorative header or footer. A note's single H1 opens with one fitting emoji and then its title;
  the `title` field stays plain.
- **Markdown is GitHub's**: CommonMark plus GitHub-Flavored Markdown, with its five alerts
  (`> [!NOTE]`, `[!TIP]`, `[!IMPORTANT]`, `[!WARNING]` and `[!CAUTION]`, each marker alone on its
  line), and wikilinks as the notes' one addition. Embeds, highlights, `%%` comments, block
  references and other callout types are not used, and `lint-notes.py` flags a callout beyond the
  five.
- **Links follow the tree.** An entity is wikilinked wherever
  [the link topology](.docs/technical/vault/Link-Topology.md) allows the edge, and named by plain
  path where it does not. Only a folder's README carries wikilinks, and a link to a folder names its
  README with the folder as the alias: `[[Library/README|Library]]`.
- **Names are plain.** Every folder explains itself in a `README.md` at its root, which is that
  folder's note, so no note is named after its folder. Scaffolds live in `.template/`. A project or
  venture folder takes a short hyphenated name. Names use spaces or hyphens, never underscores: a
  garbled name is renamed as it is filed.
- **No em dash.** No file holds an em dash (U+2014): a comma, a colon, parentheses or a spaced hyphen
  takes its place, and `lint-notes.py` flags one in a note.
- **One home for each thing.** Before a file or folder is created, it is checked that none already
  serves its purpose. A fact about the owner lives in `Profile/` alone.
- **Accurate over complete.** Less that is true and current beats more that is stale: a note is not
  padded, and what is no longer true is not kept.
- **Paths are relative.** Nothing in the vault holds an absolute path; every reference runs from the
  vault root, so the vault works wherever it is placed.
- **History is git.** No hand-kept changelog and no per-file versions: the commits and the release
  notes are the record.

---

## ✋ Ask First

These need the owner's yes before they happen:

- **Deleting any file.** After the owner says yes, the file is removed with `git rm`, and anything git
  could not bring back is committed first. A file is never emptied in place of being deleted.
- **A new folder below a top folder**: one directly inside a top folder is suggested first, and one
  deeper down, such as a project's subfolder or one an Inbox sort needs when no folder fits, is
  proposed first. The folders a copied `.template/` brings, and the year folders `update-vault.py`
  makes in the archive, need no yes of their own.
- **Moving a file out of `Inbox/`**, whose destination and clean name are proposed first.
- **Writing to `Profile/`**, which is read-only unless the owner asks or confirms.
- **Removing anything a retention policy flags**: the policy says what may go, and the owner decides.
- **Changing this page's rules or a folder README's rules**: the change is proposed on its own, never
  made as a side effect of other work.

A top folder, or a file at the vault root, is created, renamed, moved or deleted by the owner alone.
Transient junk (`__pycache__/`, `*.pyc`, `._*` files) needs no yes to clear.

---

## ⚠️ Gotchas

- **Hidden folders are infrastructure**: `.assets/`, `.devcontainer/`, `.docs/`, `.git/`, `.github/`,
  `.vscode/` and each `.template/`. None is deleted, empty or not. `.DS_Store` is ignored completely:
  never deleted, moved, reported or counted.
- **Some text is machine-owned.** The `.gitkeep` markers and the blocks between `<!-- brain:` markers
  are `update-vault.py`'s, the `AUTO-INDEX` folder logs are the indexer's, and the catalog is
  generated. Change the source and redraw; they are never edited by hand.
- **The public template stays blank.** In it, every note about a person is a blank scaffold, and none
  is ever filled in there.
- **Memory is checked before a premise is.** A premise is checked against Memory before it is acted
  on, and when Memory disagrees, the conflict is named rather than either version adopted.
- **Commits are made here; pushes are the owner's.** A meaningful state is committed before a risky
  or wide edit.
- **A long context has a forgetful middle**:
  [context assembly](.docs/technical/vault/Context-Assembly.md) says what goes first and what goes
  last.

---

<div align="center">

**This page for the vault, each folder's README for its folder, the checks for both.**

[↑ Back to Top](#top)

<br />

Distributed under the terms in [LICENSE](/LICENSE).

</div>
