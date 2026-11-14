#!/usr/bin/env python3
"""The vault's session helpers: orient a session, check a note after an edit, and tidy up when a turn ends.

WHY THIS EXISTS. These began as the vault's Claude Code hooks. The vault
carries no agent configuration of its own, so nothing wires them; each runs
by hand, and any app's own hook settings may call one:

- start: a short orientation card. It lists the files every session reads
  first (the root README.md, Profile/Working Style.md and Memory/Log.md), the
  two newest session summaries, and, when files wait at the Inbox, the
  Inbox's README.md and each waiting file, as paths to read rather than whole
  files, so the card stays short. It then says what is due, since nothing
  else in the vault raises a date by itself: each one-time date in
  Memory/Dates.md that has passed or falls within two weeks, each held report
  past its review_by date, and how many threads the Log holds open. Those
  lines carry a date and a path, never what the date is for.
- after-edit: given a hook's JSON on stdin naming the file just written,
  checks it with lint-notes.py and reports any problem, so a mistake is
  fixed in the same turn.
- stop: when the working tree has changes, redraws everything generated
  with update-vault.py, runs check-vault.py, and says what changed and what
  fails.

A helper called from a hook must never break a session, so every subcommand
exits 0 whatever happens.

Run them:

    python3 .github/scripts/session.py start
    python3 .github/scripts/session.py start --today 2026-11-14
    echo '{"tool_input": {"file_path": "Memory/Log.md"}}' | python3 .github/scripts/session.py after-edit
    python3 .github/scripts/session.py stop
"""

from __future__ import annotations

import datetime
import json
import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import vault  # noqa: E402  (vault.py sits beside this file)

HERE = pathlib.Path(__file__).resolve().parent
CURRENT = 'Memory/Context/Current'
# How far ahead the card looks for a date in Memory/Dates.md.
AHEAD = datetime.timedelta(days=14)
ONE_TIME = '## One-Time'


def day(text: object) -> datetime.date | None:
    """A date written YYYY-MM-DD, or None for anything else."""
    text = str(text or '').strip().strip('`*')
    if not vault.DATE_RE.match(text):
        return None
    try:
        return datetime.date.fromisoformat(text)
    except ValueError:
        return None


def one_time_dates(text: str) -> list[datetime.date]:
    """The dates that open the rows of the One-Time table in Memory/Dates.md, in the order written.
    A row whose first cell is not a date written YYYY-MM-DD is passed by."""
    lines = text.split('\n')
    head = next((i for i, line in enumerate(lines) if line.strip() == ONE_TIME), None)
    if head is None:
        return []
    found = []
    for line in lines[head + 1:]:
        if line.startswith('## '):
            break
        if line.lstrip().startswith('|'):
            when = day(line.strip().strip('|').split('|')[0])
            if when is not None:
                found.append(when)
    return found


def due(root: pathlib.Path, today: datetime.date) -> list[str]:
    """What is due, a line each, a date and a path and never what it is for: the one-time dates
    that have passed or fall within two weeks, the held reports past their review date, and how
    many threads the Log holds open."""
    lines = []
    dates = root / vault.DATES
    if dates.is_file():
        for when in sorted(one_time_dates(vault.read_text(dates))):
            if when < today:
                lines.append(f'OVERDUE {when.isoformat()}  {vault.DATES}')
            elif when <= today + AHEAD:
                lines.append(f'DUE {when.isoformat()}  {vault.DATES}')
    for report in vault.entry_files(root / vault.REPORTS):
        fields = vault.note_fields(report)
        review_by = day(fields.get('review_by'))
        if review_by is not None and review_by < today and not vault.is_stale(fields):
            lines.append(f'REVIEW {vault.rel(root, report)}  (review_by {review_by.isoformat()})')
    log = root / vault.LOG
    if log.is_file():
        loops = len(vault.open_entries(vault.read_text(log)))
        noun = 'open loop' if loops == 1 else 'open loops'
        lines.append(f"{loops if loops else 'No'} {noun} in {vault.LOG}.")
    return lines


def start(root: pathlib.Path, today: datetime.date) -> None:
    print('Vault startup (README.md, How A Session Goes). The startup set is listed, not inlined:')
    print('Read every file on a READ line before substantive work.')
    for path in vault.startup_notes(root):
        print(f'READ {vault.rel(root, path)}')
    summaries = [p for p in reversed(vault.tier_summaries(root / CURRENT)) if not vault.is_stale(vault.note_fields(p))][:2]
    for path in summaries:
        print(f'READ {vault.rel(root, path)}  (session summary)')
    if not summaries:
        print(f'No session summaries in {CURRENT} yet.')
    drops = vault.inbox_drops(root)
    protocol = vault.folder_note(root / vault.INBOX)
    if drops and protocol.is_file():
        print(f'READ {vault.rel(root, protocol)}  (how to sort the Inbox)')
    for path in drops:
        print(f'INBOX {vault.rel(root, path)}')
    if drops:
        noun = 'file waits' if len(drops) == 1 else 'files wait'
        print(f'{len(drops)} {noun} at the Inbox; sort them per {vault.rel(root, protocol)} before other work.')
    else:
        print('Inbox clear.')
    for line in due(root, today):
        print(line)
    print("Before changing anything in a folder, read its README.md and the README.md of each folder above it.")


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
        path.relative_to(root)
    except ValueError:
        return
    flagged = []
    if path.suffix == '.md':
        result = run('lint-notes.py', '--root', str(root), str(path), timeout=60)
        if result is not None and result.returncode != 0:
            flagged.append(('lint-notes.py', (result.stdout + result.stderr).strip()))
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
        for verb, prefixes in (('redrew', ('updated:', 'moved:')), ('removed', ('removed:',))):
            lines = [line for line in update.stdout.splitlines() if line.startswith(prefixes)]
            if lines:
                shown = ', '.join(line.split(': ', 1)[1] for line in lines[:5])
                more = f' and {len(lines) - 5} more' if len(lines) > 5 else ''
                messages.append(f'update-vault.py {verb} {len(lines)} generated part(s): {shown}{more}.')
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
    parser.add_argument('--today', help='the day the start card counts from, as YYYY-MM-DD (default: today)')
    args = parser.parse_args(argv)
    root = args.root.resolve()
    try:
        if args.helper == 'start':
            start(root, day(args.today) or datetime.date.today())
        elif args.helper == 'after-edit':
            after_edit(root, sys.stdin.read())
        else:
            stop(root)
    except Exception as error:  # noqa: BLE001  (a helper never breaks a session)
        print(f'session.py {args.helper}: {error}', file=sys.stderr)
    return 0


if __name__ == '__main__':
    sys.exit(main())
