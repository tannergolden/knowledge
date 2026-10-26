<!--
title: '📖 GLOSSARY'
description: 'The vault''s own terms, from folder note and scaffold to held, faculty and venture, each defined briefly, with the file that sets it. Look a term up here when a note, a rule or a script uses it; the account''s shared engineering terms are in the standards'' glossary.'
type: reference
keywords: [terms, definitions, vocabulary, held, scaffold, faculty, venture, folder note]
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

- **BRAIN**: Behavioral Recursive Augmented Intelligence Network, the name of a vault made from this
  template (`.github/README.md`).
- **Collection**: a folder of one file per entry, whose folder note lists the entries in a generated
  block: `People/`, `Organizations/` and `Places/` under `Memory/Entities/`, and `Decisions/`,
  `Events/` and `Insights/` under `Memory/`. Profile's folder facets work the same way
  (`.github/scripts/vault.py`).
- **Drop**: a loose file waiting at the `Inbox/` root, outside the held sub-homes; the start card
  lists each one on an `INBOX` line (`.github/scripts/session.py`).
- **Enrichment**: what a file gets before it leaves the Inbox: hidden frontmatter for a note, and a
  clean name for anything else (`Inbox/Inbox.md`).
- **Entry**: one file in a collection or a folder facet, copied from its scaffold.
- **Folder note**: the note named after its folder, such as `Memory/Memory.md`, typed `index`. It
  describes its folder, holds the folder's Rules where it has any, and is the only kind of note that
  may carry wikilinks, which is why it is also called the folder's hub ([Link Topology](../technical/vault/Link-Topology.md)).
- **Held**: kept at the Inbox's path but never sorted. `Reports/`, `Visuals/`, `Ideas/` and
  `Backups/` are the held sub-homes; they are still linted and cataloged (`Inbox/Inbox.md`).
- **Note**: any `.md` file in the seven top folders, scaffolds included. It opens with the hidden
  frontmatter of the [Note Schema](../technical/vault/Note-Schema.md), and carries a single H1 and no
  decorative header or footer.
- **Page**: a file that is not a note: a top folder's `README.md`, `AGENTS.md`, or anything in a
  hidden folder, such as this one. A page follows the account's styling standard in full.
- **Rules**: the section a top folder's note opens with. Folder Rules add to `AGENTS.md` and never
  loosen it (`AGENTS.md`, Start here).
- **Scaffold**: a file in a `.template/` folder, typed `template`, copied to make a new note and never
  edited in place. A scaffold carries no wikilinks, receives none, and is left out of the catalog.
- **Sort**: moving a drop out of the Inbox to its home, with its destination and clean name proposed
  first and nothing moved without a yes (`Inbox/Inbox.md`).
- **Top folder**: one of the seven, Inbox, Library, Memory, Profile, Projects, System and Ventures,
  and the only folders that carry a `README.md`. They and the vault root are the owner's to change.
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
  context runs short (`Memory/Memory.md`, Rules).
- **Consolidation**: the periodic pass that promotes, merges and supersedes Log entries, run when
  about ten wait unpromoted, monthly, or on request (`System/Workflows.md`).
- **Current**: the entry tier, `Memory/Context/Current/`, holding up to three summaries, the two
  newest of which every session reads at its start.
- **Importance**: the 1 to 5 score an entry gets when it is captured, from routine to pivotal, used to
  rank recall and to decide when to reflect (`Memory/Memory.md`).
- **Open loop**: a Log entry still marked `**Status:** Open`; the Log's Open Loops block lists every
  one (`Memory/Log.md`).
- **Promotion**: moving a Log entry into the collection or file where it lasts.
- **Recent**: the mid tier, `Memory/Context/Recent/`, holding up to six summaries, read on request.
- **Reflection**: writing `Insights/` that answer questions posed over recent memory, once the summed
  importance captured since the last reflection crosses about 25 (`Memory/Memory.md`).
- **Session summary**: the delta-update record of one session, filed in `Memory/Context/Current/` as
  `YYYYMMDD-HHMMSS.md` from `Memory/.template/Session Summary.md`.
- **Startup set**: what every session reads first: the startup notes, `Profile/Working Style.md` and
  `Memory/Log.md` (`STARTUP` in `.github/scripts/vault.py`), then the two newest summaries.
- **Supersede**: to mark an entry replaced, with a pointer to the entry that replaces it, rather than
  rewrite it in place (`Memory/Memory.md`).
- **Tier**: one of Current, Recent and Archive.

---

## 🪪 Profile

- **Facet**: one of the twelve parts of `Profile/`. A flat facet is one file, such as `Biography.md`;
  a folder facet is an overview note plus one entry per item: Values, Goals, Skills and Health
  (`Profile/Profile.md`).
- **Focus**: the one dynamic facet, for what is true only now: current priorities, routines and the
  current life chapter.
- **Provenance marker**: the inline comment on a Profile line the AI inferred, such as
  `<!-- observed 2026-06-19 · confidence: medium · unconfirmed -->`, shortened to `confirmed` once the
  owner approves it (`Profile/Profile.md`).
- **Unconfirmed**: a proposal that waits for the owner's approval, and is never treated as
  established.

---

## 📚 Library

- **Catalog card**: the companion note a source document, such as a book or a paper, gets in the
  Library, holding its bibliography (`Library/Library.md`).
- **Class**: one of the Library's ten top subjects, each a folder; a **division** is a recognized
  sub-discipline, one folder below its class.
- **Controlled token**: a slash-namespaced keyword a script can filter on exactly: `freshness/`,
  `form/`, `level/`, `period/`, `place/`, `class/` and `div/`
  ([Keywords](../technical/vault/Keywords.md)).
- **Freshness token**: how long a holding stays true: `freshness/timeless` for 25 years or more,
  `freshness/enduring` for 10 to 25, `freshness/current` for 5 to 10. Every holding carries exactly
  one, and anything shorter-lived stays out of the Library.
- **Holding**: a Library note other than a folder note, a record, a scaffold or the Librarian's own
  spec: the reference knowledge itself.
- **Knowledge base**: an offline reference work, such as Wikipedia, kept as a ZIM file in
  `Library/Reference & Encyclopedia/` and read with `.github/scripts/knowledge-base.py`.

---

## 🤖 Agents & Skills

- **Agent home**: a folder of agent teams. The three are `Ventures/Agent Resources (AR)/`,
  `.agents/skills/`, where each faculty keeps its team in its skill's `agents/`, and `Library/`, whose
  one agent is the Librarian; together they make one library with one namespace
  (`.github/scripts/vault.py`).
- **Agent Resources (AR)**: the shared corporate workforce in `Ventures/`, one team per department,
  that serves every venture.
- **Agent spec**: one agent's file, opening with the `---` block its loader reads: `name`,
  `description` and `tools`.
- **Faculty**: one of the five standing teams that serve the owner's own work: Research, Discovery,
  Editorial, Design and Finance, each kept in the `agents/` folder of the skill that dispatches it.
- **Founder**: the owner, as the agents know them: named in `Profile/Biography.md` and above the whole
  workforce.
- **Lead**: the one member of a team whose file name opens with ★ and a space. A lead orchestrates and
  holds only `Read`, `Grep`, `Glob` and `Task`; the Librarian, a team of one, also holds `Write`,
  `Edit` and `Bash` (`.github/scripts/check-agents.py`).
- **Role**: an agent's file name, unique across the library.
- **Roster**: a team folder's own note, which describes the team.
- **Skill**: a capability with a `SKILL.md`, kept in `.agents/skills/<name>/`, where the agent apps
  read it, copied to `.claude/skills/<name>/` for Claude Code, and packed into the `<name>.skill`
  archive for the Claude app (`System/Skills/Skills.md`).
- **Spoken name**: an agent's `name`, by which the owner addresses it, unique across the library.
- **Team**: the agent specs in one folder, with its roster.
- **Vendoring**: copying a team's roster and members into a skill's archive as it is built, so an
  installed skill carries its agents.
- **Venture**: a company the owner owns or runs, with clients, employees, revenue or a brand, kept in
  a folder of `Ventures/` copied from its scaffold. A personal initiative without them is a
  **project**, in `Projects/` (`Ventures/Ventures.md`).
- **Write-gate**: the `board` skill's check before it writes to a venture: internal drafts go ahead,
  while money, contracts, outside communication and deletions need the Founder.

---

## ⚙️ Machinery & Sync

- **Catalog**: `System/Data/catalog.ndjson`, one line per note but the scaffolds, holding its path,
  title, type, keywords, description and status. The **agent catalog**,
  `System/Data/agent-catalog.json`, lists every agent and team. `update-vault.py` draws both.
- **Generated block**: the text between `<!-- brain:NAME ... -->` and `<!-- /brain:NAME -->` in a
  note, which only `update-vault.py` writes ([Vault Scripts](../technical/Vault-Scripts.md)).
- **Initialisation**: the one run that claims a newly generated vault for its owner, then removes its
  own sentinel ([Setting Up A Vault](../introduction/Setting-Up-A-Vault.md)).
- **Kept current**: a path `.github/template-sync` names without a `#`, so 🔄 Template Sync keeps it
  current in a vault.
- **Machined index**: a folder log between `AUTO-INDEX` markers, drawn by the standards' indexer.
- **Only ever in the template**: the files initialisation deletes from every vault.
- **Sealed block**: the block between the `INTELLIGENCE` markers in `AGENTS.md`, delivered by
  tannergolden/intelligence and kept current by 🔁 Intelligence Sync.
- **Session helper**: one of `session.py`'s `start`, `after-edit` and `stop`.
- **The developer** and **the user**: the developer designed and built the template, and is named on
  the landing page; the user is whoever `Profile/` describes (`.github/README.md`).
- **Yours**: a path `.github/template-sync` switches off with `#`, seeded once and never synced.

---

<div align="center">

**Say it the vault's way, and the vault finds it.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
