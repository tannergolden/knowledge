#!/usr/bin/env python3
"""The vault's session helpers: orient a session, check a note after an edit, and tidy up when a turn ends.

WHY THIS EXISTS. These began as the vault's Claude Code hooks. The vault no
longer carries an agent configuration of its own, so nothing wires them;
each runs by hand, and an agent's own hook settings may call one:

- start: a short orientation card. It lists the startup notes, the two
  newest session summaries and anything waiting at the Inbox, as paths to
  read rather than whole files, so the card stays short.
- after-edit: given a hook's JSON on stdin naming the file just written,
  checks it with lint-notes.py (and a skill source with check-skills.py),
  and reports any problem, so a mistake is fixed in the same turn.
- stop: when the working tree has changes, redraws everything generated
  with update-vault.py, runs check-vault.py, and says what changed and what
  fails.

A helper called from a hook must never break a session, so every subcommand
exits 0 whatever happens.

Run them:

    python3 .github/scripts/session.py start
    echo '{"tool_input": {"file_path": "Memory/Log.md"}}' | python3 .github/scripts/session.py after-edit
    python3 .github/scripts/session.py stop
"""

from __future__ import annotations

import json
import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import vault  # noqa: E402  (vault.py sits beside this file)

HERE = pathlib.Path(__file__).resolve().parent
CURRENT = 'Memory/Context/Current'


def start(root: pathlib.Path) -> None:
    print('Vault startup (AGENTS.md, Start here). The startup set is listed, not inlined:')
    print('Read every file on a READ line before substantive work.')
    for path in vault.startup_notes(root):
        print(f'READ {vault.rel(root, path)}')
    summaries = [p for p in reversed(vault.tier_summaries(root / CURRENT)) if not vault.is_stale(vault.note_fields(p))][:2]
    for path in summaries:
        print(f'READ {vault.rel(root, path)}  (session summary)')
    if not summaries:
        print(f'No session summaries in {CURRENT} yet.')
    drops = vault.inbox_drops(root)
    for path in drops:
        print(f'INBOX {vault.rel(root, path)}')
    if drops:
        noun = 'file waits' if len(drops) == 1 else 'files wait'
        print(f'{len(drops)} {noun} at the Inbox; sort them per Inbox/Inbox.md before other work.')
    else:
        print('Inbox clear.')


def run(script: str, *args: str, timeout: int = 120) -> subprocess.CompletedProcess[str] | None:
    """Run a sibling script, or None when it is missing or does not finish."""
    path = HERE / script
    if not path.is_file():
        return None
    try:
        return subprocess.run([sys.executable, str(path), *args], capture_output=True, text=True,
                              timeout=timeout, check=False)
    except (OSError, subprocess.SubprocessError):
        return None


def after_edit(root: pathlib.Path, payload: str) -> None:
    try:
        data = json.loads(payload or '{}')
    except ValueError:
        return
    tool_input = data.get('tool_input') if isinstance(data, dict) else None
    name = tool_input.get('file_path') if isinstance(tool_input, dict) else None
    if not isinstance(name, str) or not name:
        return
    path = pathlib.Path(name)
    path = (path if path.is_absolute() else root / path).resolve()
    try:
        parts = path.relative_to(root).parts
    except ValueError:
        return
    flagged = []
    if path.suffix == '.md':
        result = run('lint-notes.py', '--root', str(root), str(path), timeout=60)
        if result is not None and result.returncode != 0:
            flagged.append(('lint-notes.py', (result.stdout + result.stderr).strip()))
    if parts[:3] == tuple(vault.SKILL_SOURCES.split('/')) and len(parts) > 4:
        result = run('check-skills.py', '--root', str(root), parts[3], timeout=60)
        if result is not None and result.returncode != 0:
            flagged.append(('check-skills.py', (result.stdout + result.stderr).strip()))
    if flagged:
        where = vault.rel(root, path)
        context = '\n\n'.join(f'{script} flagged {where}:\n{output}' for script, output in flagged)
        print(json.dumps({'hookSpecificOutput': {'hookEventName': 'PostToolUse', 'additionalContext': context}}))


def changed(root: pathlib.Path) -> bool:
    """True when the working tree differs from the last commit, or when git cannot say."""
    try:
        result = subprocess.run(['git', '-C', str(root), 'status', '--porcelain'], capture_output=True,
                                text=True, timeout=30, check=False)
    except (OSError, subprocess.SubprocessError):
        return True
    return result.returncode != 0 or bool(result.stdout.strip())


def stop(root: pathlib.Path) -> None:
    if not changed(root):
        return
    messages = []
    update = run('update-vault.py', '--root', str(root))
    if update is not None:
        lines = [line for line in update.stdout.splitlines() if line.startswith(('updated:', 'moved:', 'removed:'))]
        if lines:
            shown = ', '.join(line.split(': ', 1)[1] for line in lines[:5])
            more = f' and {len(lines) - 5} more' if len(lines) > 5 else ''
            messages.append(f'update-vault.py redrew {len(lines)} generated part(s): {shown}{more}.')
        if update.returncode != 0:
            problems = [line for line in update.stdout.splitlines() if line.startswith('error:')][:3]
            messages.append('update-vault.py could not draw everything:\n' + '\n'.join(problems))
    check = run('check-vault.py', '--root', str(root), timeout=300)
    if check is not None and check.returncode != 0:
        problems = [line for line in check.stdout.splitlines() if line.startswith('error:')][:5]
        messages.append('check-vault.py found problems:\n' + '\n'.join(problems)
                        + '\nRun python3 .github/scripts/check-vault.py to see them all.')
    if messages:
        print(json.dumps({'systemMessage': '\n'.join(messages)}))


def main(argv: list[str] | None = None) -> int:
    parser = vault.arguments((__doc__ or '').split('\n', 1)[0])
    parser.add_argument('helper', choices=('start', 'after-edit', 'stop'), help='which helper to run')
    args = parser.parse_args(argv)
    root = args.root.resolve()
    try:
        if args.helper == 'start':
            start(root)
        elif args.helper == 'after-edit':
            after_edit(root, sys.stdin.read())
        else:
            stop(root)
    except Exception as error:  # noqa: BLE001  (a helper never breaks a session)
        print(f'session.py {args.helper}: {error}', file=sys.stderr)
    return 0


if __name__ == '__main__':
    sys.exit(main())
