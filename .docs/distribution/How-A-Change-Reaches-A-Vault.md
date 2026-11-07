<!--
title: '🌿 HOW A CHANGE REACHES A VAULT'
description: 'The path a change takes from tannergolden/path, the golden path template, through tannergolden/knowledge and its releases, into a vault whose owner runs 🔄 Template Sync, what each section of the sync list means for a vault, and what a sync leaves alone. Read it before you add a file the template ships, cut a release, or merge a sync pull request.'
type: guide
keywords: [template sync, releases, cut release, derived template, versioning, delivery, migration]
-->

<div align="center">

# 🌿 HOW A CHANGE REACHES A VAULT

<a name="top"></a>

**From the golden path template, through a release here, to a pull request in each vault.**

_Two hops, one release, every merge the owner's._

</div>

---

## 💡 Two Hops

```mermaid
graph LR
    PT["tannergolden/path"] -->|"🔄 Template Sync, mapped"| KN["tannergolden/knowledge"]
    KN -->|"🏷️ Cut Release, then 🔄 Template Sync"| V["A vault"]
```

**The first hop: the golden path template into this one.** tannergolden/knowledge was generated from
tannergolden/path, the golden path template, and follows it as a template derived from another. A
dispatch of 🔄 Template Sync here takes that template's latest release as a mapped sync, through
`.github/template-derive.json`:

| The mapping  | What it does                                                                                                                                                                                                                                                                                                                                |
| :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Relocates    | Its `docs/` to `.docs/`, and its `assets/` to `.assets/`                                                                                                                                                                                                                                                                                    |
| Excludes     | What a vault has no use for: `src/`, `tests/`, `packages/`, `benchmarks/` and `examples/`, its changelog, its seed decision record, whose number this template's own records took, the vulnerability report issue form, which a public repository must not carry, and the Intelligence Sync stub, since a vault takes no rules from the hub |
| Leaves alone | This template's own `LICENSE`, `.github/actions/README.md` and root `README.md`, the vault's guide; its front page is `.github/README.md`, which GitHub shows ahead of a root `README.md`                                                                                                                                                   |

`.github/template-derive.lock` records where each file was last synced from. Both files are needed
only here: initialisation deletes them from every vault, so a vault syncs from this template alone.

**The second hop: this template into a vault.** A merge to the default branch here reaches no vault.
🏷️ Cut Release, dispatched with a version `vX.Y.Z`, publishes the release and moves `v1` to it, after
checking that `.github/template-sync` and the Template Sync stub exist and that
`validate-repository.py` passes. Every earlier version stays, page and tag, so a vault that names
one in full in its stub's `ref:` still finds it; tannergolden/intelligence no longer pins one, since
the skills live there now. A vault follows `v1`: when its owner runs 🔄 Template Sync, every file
the template changed that the vault's list keeps current arrives as one pull request on
`chore/template-sync`, merged with the owner's own changes. A vault never follows `v2` until its owner
changes `ref:` in its stub.

**No road for the universal rules.** The universal rules an AI assistant follows reach every
session from the home kit installed from tannergolden/intelligence, not from this repository: the
template keeps no `AGENTS.md` and no Intelligence Sync stub, nor does a vault made from it. The hub's own
sync leaves alone a repository with the `no-intelligence` topic, which the template carries and each
vault is given when it is set up.

---

## 📋 What A Vault Takes

`.github/template-sync` names every file this template ships, in five sections, then a last one for
the owner's own rules:

| Section                          | In a vault                | What it holds here                                                                                                                                                                             |
| :------------------------------- | :------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Kept current                     | Synced                    | The repository files this template takes from tannergolden/path: the workflow stubs, the repository scripts, the editor and container settings, the `.docs/` folder READMEs and seed templates |
| The vault: kept current          | Synced                    | The vault itself: its scripts and action, the root `README.md`, the landing page, each folder's `README.md` and the scaffolds, the Library and the `.docs/` pages written for the vault        |
| Yours: seeded once, never synced | Arrives once              | `LICENSE`, `.git-blame-ignore-revs`, `.github/CODEOWNERS`, `.github/FUNDING.yml`, `cut-release.yml` and `.assets/`                                                                             |
| The vault: yours                 | Arrives once              | `Memory/Log.md`, `Memory/Dates.md`, the eight flat Profile facets and the catalog                                                                                                              |
| Only ever in the template        | Deleted at initialisation | The sentinel, the derivation and its lock, and the template's own decision records                                                                                                             |

A sync never touches a file the template does not ship, which is every note an owner writes, nor a
file the list leaves to its owner. A file both changed is merged; where both changed the same lines,
the owner's file stays exactly as it was and the pull request shows the template's change. An owner
puts a `#` before a line to keep that file, or writes `# keep mine: /path` under Your rules to keep
their own lines and take the rest. To keep a whole folder the list keeps current, they add two
lines under Your rules, such as `!/Library/Life & Practice/` and `!/Library/Life & Practice/**`. A
folder takes a line of its own beside the one for what it holds, because the sync reads the list with
git's matcher, which cannot switch off a file inside a folder a line above keeps current. [Template Sync](../../.github/template-sync.md) explains every
outcome a sync pull request reports.

---

## 🧰 Adding A File To The Template

For whoever maintains tannergolden/knowledge:

- [ ] **Name it in `.github/template-sync`**, in the same change: under "The vault: kept current" when
      every vault keeps it current, under "The vault: yours" as `#/path` when each owner writes their
      own, or under "Only ever in the template" when no vault needs it. A pattern already there, such
      as `/.docs/technical/vault/**`, may cover it. When you remove a file, remove its line: a line
      naming nothing fails the check.
- [ ] **Make it true in a vault.** A file every vault keeps must still read right once initialisation
      has deleted the template-only files, so it links none of them.
- [ ] **Run the check.** 🔄 Template Sync checks the list on every pull request and every push to the
      default branch here, and fails on a file it does not name. To run it first, from a checkout of
      tannergolden/standards beside this one:

```bash
python3 ../standards/.github/scripts/template-sync.py check --repo-dir .
```

- [ ] **Release it.** Dispatch 🏷️ Cut Release with the next version: until then no vault can take
      the change. A change that renames a file a vault depends on, or reshapes a stub past what a merge
      can carry, is breaking: release it as a new major, which no vault follows until its owner
      decides to.

The full standard for templates, derived ones included, is the standards'
[Template Sync](https://github.com/tannergolden/standards/blob/Development/docs/distribution/automation/Template-Sync.md).

---

## 🚚 Moving A Vault Off Its Own Skills

A vault made before the skills moved to tannergolden/intelligence kept them and their agents itself: the skills in
`.agents/skills/` with a copy in `.claude/skills/` and archives in `System/Skills/`, the venture
workforce in `Ventures/Agent Resources (AR)/`, the Librarian in `Library/`, and
`System/Data/agent-catalog.json`; one older still kept them in `System/Skills/.unpackaged/` and
`Inbox/Faculties/`. The template ships none of them now: every skill and its team live in
tannergolden/intelligence under `kit/skills/`, and the home kit installs them.

- **Install the home kit** on each machine you work from, so the skills keep reaching the vault.
- **Run 🔄 Template Sync.** It removes each of those files you had not changed, and keeps one you had
  changed as yours.
- **On the sync pull request's branch**, carry any change you made to a skill or an agent into your
  own copy of tannergolden/intelligence, or your AI app's own skills folder, then `git rm` what the
  sync kept, empty folders included. Delete `System/Data/agent-catalog.json` too: it was yours, so the
  sync leaves it. Remove the lines under Your rules in `.github/template-sync` that name a skill path,
  such as `!/.agents/skills/<skill>/**`, since they now name nothing.
- Run `python3 .github/scripts/update-vault.py` and commit the catalog it redraws, then merge once
  `python3 .github/scripts/check-vault.py` passes.

---

## 📁 Moving A Vault To Folder READMEs

A vault made before every folder explained itself in a README explained each folder in a note named
after it (`Memory/Memory.md`), kept a `README.md` only in its seven top
folders, and kept its rules in `AGENTS.md`, synced by 🔁 Intelligence Sync. Now every folder explains
itself in its `README.md`, the root `README.md` says how to work in the vault, and the vault holds no
`AGENTS.md` and no Intelligence Sync stub. The change renames files every vault keeps current, so it
ships in a new major release: a vault takes it when its owner changes `ref:` in
`.github/workflows/template-sync.yml` to that major.

- **Run 🔄 Template Sync.** Each folder note the template ships moves to its `README.md`, your
  changes with it, and each top folder's note and README arrive as one `README.md`. A note you had
  changed, and the template removed, stays as yours: `lint-notes.py` names it, as a note named after
  its folder.
- **Merge what stayed.** For each note `lint-notes.py` names, move what it says that the folder's
  `README.md` does not into the README, then `git rm` the note. The same goes for a folder note of
  your own, such as a Library division you added: `git mv` it to that folder's `README.md`.
- **Repoint the links.** A wikilink to an old folder note now resolves to nothing, and
  `check-links.py` names each one: `[[Library/Arts & Recreation/Arts & Recreation|Arts]]` becomes
  `[[Library/Arts & Recreation/README|Arts]]`. A plain path in a file of your own, such as
  `Profile/Profile.md` in `Profile/Biography.md`, is not checked: search for each old name and
  update it.
- **Retire the hub's files.** `git rm` `AGENTS.md`, which the sync keeps as yours once
  🔁 Intelligence Sync had changed it, and `.github/workflows/intelligence-sync.yml`, which was yours
  from the start, then delete the `#/.github/workflows/intelligence-sync.yml` line under The vault:
  yours in `.github/template-sync`. Add the `no-intelligence` topic, so the hub's sync leaves the vault
  alone. Anything you had added to `AGENTS.md` that the vault still needs belongs in the root
  `README.md` or a folder's README.
- Run `python3 .github/scripts/update-vault.py` and commit what it redraws, then merge once
  `python3 .github/scripts/check-vault.py` passes.

---

<div align="center">

**Merged here, released once, taken by each vault when its owner asks.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
