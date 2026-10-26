<!--
title: '🔬 REPOSITORY SCRIPTS'
description: 'The checks this repository runs on its own configuration, and the tests that guard them.'
type: index
-->

<div align="center">

# 🔬 REPOSITORY SCRIPTS

<a name="top"></a>

**The checks a new repository runs before it has any code of its own.**

_The first gates you have, every one under test._

</div>

---

## 💡 What This Folder Is For

A new repository has no source code to lint, but it already has configuration
that decides how it behaves: workflows, Dependabot, forms, editor settings. A
typo in any of them breaks something quietly. The scripts here check those files
from the first commit, and the tests beside them check the scripts.

They live under `.github/` so the root of the repository stays yours. Each needs
only Python 3, plus the one package pinned in
[`requirements.txt`](requirements.txt), PyYAML, for the ones that read YAML.

[`hooks/`](hooks/README.md) holds the git hooks that run the commit-message,
sign-off and secret checks on your machine before a commit exists, so a pull
request is not the first place you hear about them.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                                          | Purpose                                                                                                        |
| :------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------- |
| [`hooks/`](hooks/README.md)                                    | The git hooks this repository ships, what each catches before a commit is recorded, and how to switch them on. |
| [`check-agents.py`](check-agents.py)                           | Check the agent library: each agent spec, each team roster, and names unique across every home.                |
| [`check-links.py`](check-links.py)                             | Check the wikilink graph: every link resolves, and links follow the hub topology.                              |
| [`check-skills.py`](check-skills.py)                           | Check each skill against the Agent Skills format and the vault's skill layout.                                 |
| [`check-vault.py`](check-vault.py)                             | Run every vault check, as CI does: notes, links, skills, agents, personal data and generated parts.            |
| [`fixtures.py`](fixtures.py)                                   | Throwaway vaults for the vault scripts' tests, built in a temporary folder.                                    |
| [`knowledge-base.py`](knowledge-base.py)                       | Search and read offline reference works, such as Wikipedia, kept as ZIM files beside the vault's notes.        |
| [`lint-notes.py`](lint-notes.py)                               | Check each note's frontmatter and naming against the vault's schema.                                           |
| [`profile-coverage.py`](profile-coverage.py)                   | Score how filled in each Profile facet is, and name the one the identify skill should ask about next.          |
| [`README.md`](README.md)                                       | This file.                                                                                                     |
| [`requirements.txt`](requirements.txt)                         | The Python packages the scripts beside this file need, and nothing else.                                       |
| [`scan-pii.py`](scan-pii.py)                                   | Find US Social Security numbers and payment card numbers in the files git tracks.                              |
| [`session.py`](session.py)                                     | The vault's session helpers: orient a session, check a note after an edit, and tidy up when a turn ends.       |
| [`test_check_agents.py`](test_check_agents.py)                 | Tests for check-agents.py, the agent library check.                                                            |
| [`test_check_links.py`](test_check_links.py)                   | Tests for check-links.py, the wikilink graph check.                                                            |
| [`test_check_skills.py`](test_check_skills.py)                 | Tests for check-skills.py, the skill source check.                                                             |
| [`test_check_vault.py`](test_check_vault.py)                   | Tests for check-vault.py, and for the wiring that runs the vault scripts.                                      |
| [`test_gitignore.py`](test_gitignore.py)                       | Tests for this repository's .gitignore.                                                                        |
| [`test_hooks.py`](test_hooks.py)                               | Tests for the git hooks in .github/scripts/hooks/.                                                             |
| [`test_knowledge_base.py`](test_knowledge_base.py)             | Tests for knowledge-base.py, the offline reference works.                                                      |
| [`test_lint_notes.py`](test_lint_notes.py)                     | Tests for lint-notes.py, the note schema check.                                                                |
| [`test_profile_coverage.py`](test_profile_coverage.py)         | Tests for profile-coverage.py, the report the identify skill reads.                                            |
| [`test_scan_pii.py`](test_scan_pii.py)                         | Tests for scan-pii.py, the personal number scan.                                                               |
| [`test_session.py`](test_session.py)                           | Tests for session.py, the vault's three session helpers.                                                       |
| [`test_update_vault.py`](test_update_vault.py)                 | Tests for update-vault.py, which draws every generated part of the vault.                                      |
| [`test_validate_repository.py`](test_validate_repository.py)   | Tests for the repository validator.                                                                            |
| [`test_vault.py`](test_vault.py)                               | Tests for vault.py, the library every vault script shares.                                                     |
| [`test_verify_stub_ceilings.py`](test_verify_stub_ceilings.py) | Tests for the stub ceiling checker.                                                                            |
| [`update-vault.py`](update-vault.py)                           | Bring every generated part of the vault up to date, or report what is stale.                                   |
| [`validate-repository.py`](validate-repository.py)             | Validate this repository's own configuration.                                                                  |
| [`vault.py`](vault.py)                                         | The vault's layout, notes and schema, shared by every vault script.                                            |
| [`verify-stub-ceilings.py`](verify-stub-ceilings.py)           | Check every stub's permission ceiling against the workflow it calls.                                           |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push to the default branch,
from each docstring. Who runs them:

- `checks.yml` runs `validate-repository.py` as the `ci` job's `lint-command`,
  and every `test_*.py` here as its `test-command`. That discovers a test
  added beside a new script without anyone remembering to list it.
- `verify-stubs.yml` installs `requirements.txt` and runs
  `verify-stub-ceilings.py`.
- `cut-release.yml` runs `validate-repository.py` before it tags a release, so
  a release the validator fails is refused. In the template, that includes a
  change to the owner's half of `docs/Prompts.md`.
- Git runs the hooks in `hooks/` once `core.hooksPath` points at them, which
  the development container does for you; `test_hooks.py` holds them to the
  same rules CI applies.

> [!NOTE]
> **The tests keep their underscores on purpose.** `unittest` imports each
> `test_*.py` as a module, and a module name cannot contain a hyphen, which is
> the one exception the naming standard allows. The scripts are run as files,
> so their names are hyphenated like everything else.

---

## 🚀 Running Them Locally

From the root of the repository:

```bash
python3 -m pip install --require-hashes --requirement .github/scripts/requirements.txt
python3 .github/scripts/validate-repository.py
python3 -m unittest discover -s .github/scripts -p 'test_*.py'
```

And once per clone, to have git run the hooks:

```bash
git config core.hooksPath .github/scripts/hooks
```

`verify-stub-ceilings.py` also needs the standards checked out at `v1` in
`.standards/`, which `verify-stubs.yml` does before it runs it.

Once `lint-command` points at your project's real linter, the validator can stay
as a second gate or go. What it checks stays true either way.

---

<div align="center">

**Configuration checked from the first commit, and the checkers checked too.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
