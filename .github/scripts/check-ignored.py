#!/usr/bin/env python3
"""Find the vault files a rule written for code keeps out of git, where nothing commits or backs them up.

WHY THIS EXISTS. The vault's history is its backup, and git keeps only what
it is shown. The .gitignore at the vault root opens with the rules every
repository on the standards shares, written for code: build/, dist/,
coverage/, test-results/, *.zip, *.key. In a vault they match the build
folder of a kitchen project, a folder of health test results, a bank's
zipped statements and a Keynote deck, and git then leaves each one out
without a word. `git add -A` succeeds, the status is clean, and the file
lives on one machine only.

This lists what git ignores under the seven top folders and fails on each
file or folder that one of those inherited rules hides. It leaves alone:

- what the vault's own rules hide, the ones below the BRAIN Vault line of
  the .gitignore, such as the offline reference works (*.zim);
- what any other ignore file hides, such as the .gitignore a code project
  keeps in its own folder, which is its owner's choice, written down;
- junk no one keeps: dot files and folders, __pycache__/, node_modules/
  and an editor's swap and backup files.

So the way to say "this one is ignored on purpose" is a .gitignore in the
folder that holds it. Outside a git checkout there is nothing to check.

Run it:

    python3 .github/scripts/check-ignored.py
"""

from __future__ import annotations

import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import vault  # noqa: E402  (vault.py sits beside this file)

IGNORE_FILE = '.gitignore'
# Where the vault's own rules begin in its .gitignore; every rule above the line came with the template.
VAULT_SECTION = '# --- BRAIN Vault ---'
JUNK_NAMES = frozenset({'__pycache__', 'node_modules', 'Thumbs.db'})
JUNK_SUFFIXES = ('.pyc', '.pyo', '.pyd', '.swp', '.swo', '~')


def junk(path: str) -> bool:
    """A path no one keeps: inside a dot folder, a dot file, a cache, or an editor's leftover."""
    parts = path.rstrip('/').split('/')
    return any(part.startswith('.') for part in parts) or parts[-1] in JUNK_NAMES or parts[-1].endswith(JUNK_SUFFIXES)


def ignored(root: pathlib.Path) -> list[str] | None:
    """What git ignores under the top folders, a wholly ignored folder as one path with a trailing
    slash, or None outside a checkout."""
    tops = [name for name in vault.TOP_FOLDERS if (root / name).is_dir()]
    if not tops:
        return [] if vault.tracked_files(root) is not None else None
    return vault.git_paths(root, 'ls-files', '--others', '--ignored', '--exclude-standard', '--directory', '--', *tops)


def rules(root: pathlib.Path, paths: list[str]) -> dict[str, tuple[str, int, str]]:
    """For each ignored path, the rule that hides it: the ignore file, the line and the pattern."""
    if not paths:
        return {}
    try:
        result = subprocess.run(['git', '-C', str(root), 'check-ignore', '-v', '-z', '--stdin'],
                                input='\0'.join(paths).encode('utf-8'), capture_output=True, timeout=60, check=False)
    except (OSError, subprocess.SubprocessError):
        return {}
    fields = result.stdout.decode('utf-8', 'replace').split('\0')
    found = {}
    for i in range(0, len(fields) - 3, 4):
        source, line, pattern, path = fields[i:i + 4]
        found[path] = (source, int(line) if line.isdigit() else 0, pattern)
    return found


def inherited_lines(root: pathlib.Path) -> int:
    """How many lines of the vault's .gitignore came with the template: those above its own section.
    A file without the section line is read as inherited throughout."""
    try:
        lines = (root / IGNORE_FILE).read_text(encoding='utf-8', errors='replace').split('\n')
    except OSError:
        return 0
    for number, line in enumerate(lines, 1):
        if line.strip() == VAULT_SECTION:
            return number - 1
    return len(lines)


def main(argv: list[str] | None = None) -> int:
    args = vault.arguments((__doc__ or '').split('\n', 1)[0]).parse_args(argv)
    root = args.root.resolve()
    report = vault.Report(root)
    paths = ignored(root)
    if paths is None:
        print('Not a git checkout, so git ignores nothing here.')
        return 0
    inherited = inherited_lines(root)
    hidden = rules(root, [path for path in paths if not junk(path)])
    own = (root / IGNORE_FILE).resolve()
    for path in sorted(hidden):
        source, line, pattern = hidden[path]
        if (root / source).resolve() != own or line > inherited:
            continue
        report.error(path, f'git ignores it ({IGNORE_FILE}:{line}: {pattern}), so it is never committed or backed up; '
                           'rename or move it, or, if that is meant, ignore it in a .gitignore of its own folder')
    return report.finish('git ignores nothing the vault keeps.')


if __name__ == '__main__':
    sys.exit(main())
