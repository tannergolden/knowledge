<!--
title: '🐳 DEVELOPMENT CONTAINER'
description: 'The BRAIN development container: what it installs for working in the vault and running its checks, and how to add a toolchain for code a project or a venture keeps there. Read it before opening the vault in a container, or before changing what the container installs.'
type: index
-->

<div align="center">

# 🐳 DEVELOPMENT CONTAINER

<a name="top"></a>

**The BRAIN container: what the vault's notes and checks need, and nothing more.**

_Python for the checks, nothing else by default._

</div>

---

## 💡 What This Folder Is For

Open the vault in a dev container - <kbd>Reopen in Container</kbd> in VS
Code, or a Codespace - and this folder decides what you get: the **BRAIN**
container, as `devcontainer.json` names it, with an Ubuntu base image, git, the
common shell utilities, and a handful of editor extensions for Markdown and the
configuration files beside it.

**A vault is plain Markdown, so nothing is installed for any language but
one.** A toolchain nobody needs costs a slow rebuild every time the container
is made.

**Python is that one, and it is not a language choice.** The checks this
repository runs are Python: the vault's own scripts, which need only the
standard library, and the checks on its configuration (the validator, the stub
checker and the commit-message hook), with their tests. So the container
installs Python and the scripts' one requirement, PyYAML, and switches on the
[git hooks](../.github/scripts/hooks/README.md) when it is created. A
container that cannot run those checks cannot tell you whether CI will pass.
It also installs gitleaks from Ubuntu's archive, so the `pre-commit` hook
scans what you stage for secrets. That release trails gitleaks itself, and CI
scans every pull request with the current one.

`.gitattributes` marks this folder `export-ignore`, so `git archive` leaves it
out of a source tarball. It is for working in the vault, not for shipping it.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                    | Purpose                                                |
| :--------------------------------------- | :----------------------------------------------------- |
| [`devcontainer.json`](devcontainer.json) | Development container - deliberately language-neutral. |
| [`README.md`](README.md)                 | This file.                                             |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push to the default branch,
from what each file says about itself.

---

## ⚙️ Adding To It

- [ ] **To search and read the offline knowledge bases** inside the container,
      append `&& python3 -m pip install --user libzim` to `postCreateCommand`
      in `devcontainer.json`. `knowledge-base.py` needs it to search and read;
      without it, `list` still works.
- [ ] **For code a project or a venture keeps in the vault**, uncomment the
      feature for its language under `features`, from the full catalogue at
      [containers.dev/features](https://containers.dev/features), and append
      its bootstrap step to `postCreateCommand`, such as `&& npm ci`,
      `&& pip install -e .` or `&& go mod download`, so a fresh container is
      ready to build it. Add its editor extension to
      `customizations.vscode.extensions`.
- [ ] Keep what `postCreateCommand` already does: it installs what the
      repository's own checks need and switches on the hooks.
- [ ] Rebuild the container.

> [!NOTE]
> **There is no `settings` block, deliberately.** VS Code reads
> [`.vscode/settings.json`](../.vscode/settings.json) inside the container like
> anywhere else, so a copy here would be a second source of truth, and the copy
> that drifts is always the one nobody remembers.

`devcontainer.json` is JSON with comments, which is what dev containers read.
The repository validator parses it the same way, so a comment is never reported
as an error.

---

<div align="center">

**Equip it for the vault, and for nothing else.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
