<!--
title: '📖 GLOSSARY'
description: 'The vault''s own terms, from folder README and scaffold to held, skill and venture, each defined briefly, with the file that sets it. Look a term up here when a note, a rule or a script uses it; the account''s shared engineering terms are in the standards'' glossary.'
type: reference
keywords: [terms, definitions, vocabulary, held, scaffold, skill, venture, folder readme]
-->

<div align="center">

# 📖 GLOSSARY

<a name="top"></a>

**Every word the vault uses in a sense of its own, and the file that sets each one.**

_One meaning to a word, one place that sets it._

</div>

---

## 💡 About These Terms

Each term is defined as the vault uses it, with the file that sets it in parentheses, so the meaning
can be checked at its source. Terms of git, GitHub and the standards, such as ADR, ruleset or
Conventional Commits, are in the standards'
[Glossary](https://github.com/tannergolden/standards/blob/Development/docs/references/Glossary.md).

---

## 📦 Notes & Folders

- **AGENTS.md**: the page at the vault root that every AI reads first: the universal rules for AI
  agents, between `INTELLIGENCE` markers, then the rules every AI follows in a personal knowledge
  vault, which hold it to the root `README.md` and each folder's README (`AGENTS.md`).
- **BRAIN**: Behavioral Recursive Augmented Intelligence Network, the name of a vault made from this
  template (`.github/README.md`).
- **Collection**: a folder of one file per entry, whose README lists the entries in a generated
  block: `People/`, `Organizations/` and `Places/` under `Memory/Entities/`, and `Decisions/`,
  `Events/` and `Insights/` under `Memory/`. Profile's folder facets work the same way
  (`.github/scripts/vault.py`).
- **Drop**: a loose file waiting at the `Inbox/` root, outside the held sub-homes; the start card
  lists each one on an `INBOX` line (`.github/scripts/session.py`).
- **Enrichment**: what a file gets before it leaves the Inbox: hidden frontmatter for a note, and a
  clean name for anything else (`Inbox/README.md`).
- **Entry**: one file in a collection or a folder facet, copied from its scaffold.
- **Folder note**: a folder's own note, which is its README. Before every folder explained itself in
  its README, it was a note named after the folder, such as `Memory/Memory.md`; `lint-notes.py` now
  flags one.
- **Folder README**: the `README.md` at a folder's root, such as `Memory/README.md`, which is the
  folder's note, typed `index` (a Profile folder facet's is typed `reference`), and a page as well, in
  the account's full page format. It says what the folder is for and what belongs in it, holds the
  folder's rules where it has any, and is the only kind of note that may carry wikilinks, which is
  why it is also called the folder's hub ([Link Topology](../technical/vault/Link-Topology.md)). No
  note is named after its folder.
- **Held**: kept at the Inbox's path but never sorted. `Reports/`, `Visuals/`, `Ideas/` and
  `Backups/` are the held sub-homes (`Inbox/README.md`). The first three are still linted and
  cataloged; `Backups/`, which keeps the originals copied before a cleanup, is never walked
  (`SKIP_DIRS` in `.github/scripts/vault.py`).
- **Note**: any `.md` file in the seven top folders, each folder's `README.md` and the scaffolds
  included. It opens with the hidden frontmatter of the [Note Schema](../technical/vault/Note-Schema.md)
  and carries a single H1. Every note but a folder's `README.md` carries no decorative header or
  footer.
- **Page**: a document that follows the account's styling standard in full, its centered header and
  footer included: the root `README.md` and `AGENTS.md`, anything in a hidden folder other than a
  `.template/`, such as this one, and every folder's `README.md`, which is both a page and its
  folder's note.
- **Root README**: the `README.md` at the vault root, the vault's guide for anyone who works in it:
  the top folders, how a session goes, the commands, what done means, where each kind of work goes,
  and the conventions every folder shares. A page, read before any folder's README, and by an AI
  right after `AGENTS.md`.
- **Rules**: the section of a folder's README that holds the rules for working there, as each top
  folder's README does. A folder's rules add to the root `README.md` and to the rules of every folder
  above it, and never loosen them (the root `README.md`, How A Session Goes).
- **Scaffold**: a file in a `.template/` folder, typed `template`, copied to make a new note and never
  edited in place. Each opens with a note, a comment that begins `On copying:`, saying where its copy
  goes and what to fill, and the note is deleted from the copy. A scaffold carries no wikilinks,
  receives none, and is left out of the catalog. A `.template/` folder's own README explains its scaffolds, typed `index` and never copied, or, where
  the folder is copied whole, as a venture's or a project's is, is a scaffold itself, written for the
  folder it becomes.
- **Sort**: moving a drop out of the Inbox to its home, with its destination and clean name proposed
  first and nothing moved without a yes (`Inbox/README.md`).
- **Top folder**: one of the seven, Inbox, Library, Memory, Profile, Projects, System and Ventures.
  They and the vault root are the owner's to change.
- **Wikilink**: `[[Target]]`, the notes' one addition to GitHub's Markdown, allowed only where the
  link topology allows the edge.

---

## 🧠 Memory & Sessions

- **Archive**: the cold-storage tier, `Memory/Context/Archive/<year>/`, with no cap, reached only by
  search.
- **Cascade**: the move of the oldest summary down a tier while one holds more than its cap, made by
  `update-vault.py`; nothing is deleted
  ([Sessions & The Memory Cascade](../technical/vault/Sessions-&-The-Memory-Cascade.md)).
- **Checkpoint**: updating the running session summary at a task boundary, and writing one before the
  context runs short (`Memory/README.md`, Rules).
- **Consolidation**: the periodic pass that promotes, merges and supersedes Log entries, run when
  about ten wait unpromoted, monthly, or on request (`System/Workflows.md`).
- **Current**: the entry tier, `Memory/Context/Current/`, holding up to three summaries, the two
  newest of which every session reads at its start.
- **Importance**: the 1 to 5 score an entry gets when it is captured, from routine to pivotal, used to
  rank recall and to decide when to reflect (`Memory/README.md`).
- **Open loop**: a Log entry still marked `**Status:** Open`; the Log's Open Loops block lists every
  one (`Memory/Log.md`).
- **Promotion**: moving a Log entry into the collection or file where it lasts.
- **Recent**: the mid tier, `Memory/Context/Recent/`, holding up to six summaries, read on request.
- **Reflection**: writing `Insights/` that answer questions posed over recent memory, once the summed
  importance captured since the last reflection crosses about 25 (`Memory/README.md`).
- **Session summary**: the delta-update record of one session, filed in `Memory/Context/Current/` as
  `YYYYMMDD-HHMMSS.md` from `Memory/.template/Session Summary.md`.
- **Startup set**: what every session reads first: the root `README.md`, `Profile/Working Style.md`
  and `Memory/Log.md` (`STARTUP` in `.github/scripts/vault.py`), then the two newest summaries, and,
  when files wait at the Inbox, `Inbox/README.md`.
- **Supersede**: to mark an entry replaced, with a pointer to the entry that replaces it, rather than
  rewrite it in place. A superseded decision or insight sets its Status line to Superseded and its
  frontmatter to `status: deprecated`, so recall ranks it lower (`Memory/README.md`).
- **Tier**: one of Current, Recent and Archive.

---

## 🪪 Profile

- **Facet**: one of the twelve parts of `Profile/`. A flat facet is one file, such as `Biography.md`;
  a folder facet is an overview note plus one entry per item: Values, Goals, Skills and Health
  (`Profile/README.md`).
- **Focus**: the one dynamic facet, for what is true only now: current priorities, routines and the
  current life chapter.
- **Provenance marker**: the inline comment on a Profile line inferred rather than stated, such as
  `<!-- observed 2026-06-19 · confidence: medium · unconfirmed -->`, shortened to `confirmed` once the
  owner approves it (`Profile/README.md`).
- **Unconfirmed**: a proposal that waits for the owner's approval, and is never treated as
  established.

---

## 📚 Library

- **Catalog card**: the companion note a source document, such as a book or a paper, gets in the
  Library, holding its bibliography (`Library/README.md`).
- **Class**: one of the Library's ten top subjects, each a folder; a **division** is a recognized
  sub-discipline, one folder below its class.
- **Controlled token**: a slash-namespaced keyword a script can filter on exactly: `freshness/`,
  `form/`, `level/`, `period/`, `place/`, `class/` and `div/`
  ([Keywords](../technical/vault/Keywords.md)).
- **Freshness token**: how long a holding stays true: `freshness/timeless` for 25 years or more,
  `freshness/enduring` for 10 to 25, `freshness/current` for 5 to 10. Every holding carries exactly
  one, and anything shorter-lived stays out of the Library.
- **Holding**: a Library note other than a folder's README, a record or a scaffold: the reference
  knowledge itself.
- **Knowledge base**: an offline reference work, such as Wikipedia, kept as a ZIM file in
  `Library/Reference & Encyclopedia/` and read with `.github/scripts/knowledge-base.py`.

---

## 🤖 Skills

- **Department**: one of the twelve a venture is organized into, from Administration to Public
  Relations, each with a folder in the venture and a skill named for it, which also covers that part
  of the owner's own life (the root `README.md`, Where Each Kind Of Work Goes).
- **Home kit**: tannergolden/intelligence's installer, which puts every skill in its `kit/skills/`,
  with the universal rules an AI assistant follows, into each AI app on every machine and in every
  Claude Code cloud session. The vault holds no skill and no agent; its `AGENTS.md` carries the
  universal rules for any AI app.
- **Skill**: a capability with a `SKILL.md`, kept in tannergolden/intelligence and installed by the
  home kit. The root `README.md`, under Where Each Kind Of Work Goes, gives this vault's layout to
  whoever writes here, a skill included.
- **Venture**: a company the owner owns or runs, with clients, employees, revenue or a brand, kept in
  a folder of `Ventures/` copied from its scaffold. A personal initiative without them is a
  **project**, in `Projects/` (`Ventures/README.md`).
- **Write-gate**: the rule every write in a venture goes through, decided by the act, not by the
  file: internal drafts go ahead; moving money, a contract, outside communication, a change to equity
  and a deletion need the owner's yes (`Ventures/README.md`, Structure).

---

## ⚙️ Machinery & Sync

- **Catalog**: `System/Data/catalog.ndjson`, one line per note but the scaffolds, holding its path,
  title, type, keywords, description and status. `update-vault.py` draws it.
- **Generated block**: the text between `<!-- brain:NAME ... -->` and `<!-- /brain:NAME -->` in a
  note, which only `update-vault.py` writes ([Vault Scripts](../technical/Vault-Scripts.md)).
- **Initialisation**: the one run that claims a newly generated vault for its owner, then removes its
  own sentinel ([Setting Up A Vault](../introduction/Setting-Up-A-Vault.md)).
- **Intelligence Sync**: the workflow `.github/workflows/intelligence-sync.yml`, each vault's own,
  which proposes the universal rules of each tannergolden/intelligence release for the block in
  `AGENTS.md`, as a pull request
  ([How A Change Reaches A Vault](../distribution/How-A-Change-Reaches-A-Vault.md)).
- **Kept current**: a path `.github/template-sync` names without a `#`, so 🔄 Template Sync keeps it
  current in a vault.
- **Machined index**: a folder log between `AUTO-INDEX` markers, drawn by the standards' indexer.
- **Only ever in the template**: the files initialisation deletes from every vault.
- **Session helper**: one of `session.py`'s `start`, `after-edit` and `stop`.
- **Template Sync**: the workflow `.github/workflows/template-sync.yml`, run by the owner, which
  proposes the template's latest release, on the major its `ref:` names, as one pull request: `v2`
  in a vault generated now, while one generated before v2.0.0 follows `v1` until its owner sets
  `ref: 'v2'` ([How A Change Reaches A Vault](../distribution/How-A-Change-Reaches-A-Vault.md)).
- **The developer** and **the owner**: the developer designed and built the template, and is named
  on the landing page; the owner, whom the universal rules in `AGENTS.md` and the home kit's skills
  call the user, is whoever `Profile/` describes, whose vault it is (`.github/README.md`).
- **Yours**: a path `.github/template-sync` switches off with `#`, seeded once and never synced.

---

<div align="center">

**Say it the vault's way, and the vault finds it.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
