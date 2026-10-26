<!--
title: '🌿 HOW A CHANGE REACHES A VAULT'
description: 'The path a change takes from tannergolden/path, the golden path template, through tannergolden/knowledge and its releases, into a vault whose owner runs 🔄 Template Sync, what each section of the sync list means for a vault, and what a sync leaves alone. Read it before you add a file the template ships, cut a release, or merge a sync pull request.'
type: guide
keywords: [template sync, releases, cut release, intelligence sync, derived template, versioning, delivery]
-->

<div align="center">

# 🌿 HOW A CHANGE REACHES A VAULT

<a name="top"></a>

**From the golden path template, through a release here, to a pull request in each vault.**

_Two hops, one release, every merge the owner's._

</div>

---

## 💡 Two Hops & A Side Road

```mermaid
graph LR
    PT["tannergolden/path"] -->|"🔄 Template Sync, mapped"| KN["tannergolden/knowledge"]
    KN -->|"🏷️ Cut Release, then 🔄 Template Sync"| V["A vault"]
    IN["tannergolden/intelligence"] -->|"🔁 Intelligence Sync"| KN
    IN -->|"🔁 Intelligence Sync"| V
```

**The first hop: the golden path template into this one.** tannergolden/knowledge was generated from
tannergolden/path, the golden path template, and follows it as a template derived from another. A
dispatch of 🔄 Template Sync here takes that template's latest release as a mapped sync, through
`.github/template-derive.json`:

| The mapping  | What it does                                                                                                                                                                                                                                                         |
| :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Relocates    | Its `docs/` to `.docs/`, and its `assets/` to `.assets/`                                                                                                                                                                                                             |
| Excludes     | What a vault has no use for: `src/`, `tests/`, `packages/`, `benchmarks/` and `examples/`, its changelog, its seed decision record, whose number this template's own records took, and the vulnerability report issue form, which a public repository must not carry |
| Leaves alone | This template's own `LICENSE` and `.github/actions/README.md`, and its front page, `.github/README.md`, which stands in for the template's root `README.md`                                                                                                          |

`.github/template-derive.lock` records where each file was last synced from. Both files are needed
only here: initialisation deletes them from every vault, so a vault syncs from this template alone.

**The second hop: this template into a vault.** A merge to the default branch here reaches no vault.
🏷️ Cut Release, dispatched with a version `vX.Y.Z`, publishes the release and moves `v1` to it, after
checking that `.github/template-sync` and the Template Sync stub exist and that
`validate-repository.py` passes. A vault follows `v1`: when its owner runs 🔄 Template Sync, every file
the template changed that the vault's list keeps current arrives as one pull request on
`chore/template-sync`, merged with the owner's own changes. A vault never follows `v2` until its owner
changes `ref:` in its stub.

**The side road: the universal rules.** 🔁 Intelligence Sync runs every Monday and on request, here
and in every vault. It proposes the latest release of tannergolden/intelligence's block between the
`INTELLIGENCE` markers in `AGENTS.md` as a pull request on `chore/intelligence`, and leaves every
section the repository owns as it was. 🔄 Template Sync passes that sealed block over.

---

## 📋 What A Vault Takes

`.github/template-sync` names every file this template ships, in five sections, then a last one for
the owner's own rules:

| Section                          | In a vault                | What it holds here                                                                                                                                                                             |
| :------------------------------- | :------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Kept current                     | Synced                    | The repository files this template takes from tannergolden/path: the workflow stubs, the repository scripts, the editor and container settings, the `.docs/` folder READMEs and seed templates |
| The vault: kept current          | Synced                    | The vault itself: its scripts and action, `AGENTS.md`, the landing page, the folder notes and scaffolds, the Library, the skills, the agent teams and the `.docs/` pages written for the vault |
| Yours: seeded once, never synced | Arrives once              | `LICENSE`, `.git-blame-ignore-revs`, `.github/CODEOWNERS`, `.github/FUNDING.yml`, `cut-release.yml` and `.assets/`                                                                             |
| The vault: yours                 | Arrives once              | The intelligence stub, `Memory/Log.md`, `Memory/Dates.md`, the eight flat Profile facets and the two catalogs                                                                                  |
| Only ever in the template        | Deleted at initialisation | The sentinel, the derivation and its lock, and the template's own decision records                                                                                                             |

A sync never touches a file the template does not ship, which is every note an owner writes, nor a
file the list leaves to its owner. A file both changed is merged; where both changed the same lines,
the owner's file stays exactly as it was and the pull request shows the template's change. An owner
puts a `#` before a line to keep that file, or writes `# keep mine: /path` under Your rules to keep
their own lines and take the rest. To keep a skill of their own, they add three lines under Your
rules, `!/.agents/skills/<skill>/**`, `!/.claude/skills/<skill>/**` and
`!/System/Skills/<skill>.skill`, so the skill, its Claude Code copy and its archive all stay theirs. [Template Sync](../../.github/template-sync.md) explains every
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

## 🚚 Moving A Vault To v2

v2 moves the skills from `System/Skills/.unpackaged/` to `.agents/skills/`, moves each faculty's
team from `Inbox/Faculties/` into its skill's own `agents/`, and adds Claude Code's copy in
`.claude/skills/` ([ADR-0003](../adrs/ADR-0003-The-Skills-Live-Where-The-Apps-Read-Them.md)). A
vault that kept the template's skills as they came needs only the sync: 🔄 Template Sync moves every
file. A vault whose owner changed them needs one step first, before `ref:` in its stub moves to
`v2`, because a sync does not carry an owner's choice from an old path to a new one:

- **You kept your own skills or teams**, with lines such as `#/System/Skills/**` or
  `#/Inbox/Faculties/**`: move each skill you changed to `.agents/skills/<skill>/` and its team's
  files into `.agents/skills/<skill>/agents/`, and under Your rules replace those lines with
  `!/.agents/skills/<skill>/**`, `!/.claude/skills/<skill>/**` and
  `!/System/Skills/<skill>.skill`. Otherwise the template's skills arrive switched on, and Claude
  Code loads them in place of yours.
- **You deleted a skill**: add the same three lines for it under Your rules, or it comes back at
  the new paths.
- **You edited a skill file or a roster the template also changed**: the sync reports the
  conflict, keeps your file at its old path and leaves its new path empty, so the skill's checks
  fail. Move your file to its new path and carry in the template's change, which the pull request
  shows. An `Inbox/Faculties/` note you edited stays behind the same way; delete it once nothing
  you need is left in it.

Once the sync pull request is open, run `python3 .github/scripts/update-vault.py` on its branch and
commit what it redraws: the two catalogs in `System/Data/` are yours, so the sync leaves them, and
`check-vault.py` fails until they are redrawn.

---

<div align="center">

**Merged here, released once, taken by each vault when its owner asks.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
