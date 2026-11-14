#!/usr/bin/env python3
"""Bring every generated part of the vault up to date, or report what is stale.

WHY THIS EXISTS. Some of the vault is derived from the rest, and a person or
an AI keeping it by hand would let it drift. This script owns all of it:

1. The memory cascade. Memory/Context/Current holds at most 3 session
   summaries and Recent at most 6; the oldest move down a tier, and Recent's
   overflow moves to Archive/<year>/. Nothing is ever deleted.
2. The generated blocks, between <!-- brain:NAME --> and <!-- /brain:NAME -->:
   each tier's list of summaries, each Memory collection's and Profile
   facet's list of entries, the list of subfolders in any folder's README.md
   that asks for one, and the Open Loops view of Memory/Log.md. A folder's
   README.md is its note, so every one of these lists lives in a README but
   the Open Loops view.
3. The catalog: System/Data/catalog.ndjson, one record per note.
4. The .gitkeep markers: an empty folder keeps one, a folder with files loses it.

Run it after a change. With --check it
writes nothing and fails when anything is out of date, which is what CI runs.

Run it:

    python3 .github/scripts/update-vault.py
    python3 .github/scripts/update-vault.py --check
"""

from __future__ import annotations

import json
import os
import pathlib
import re
import shutil
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import vault  # noqa: E402  (vault.py sits beside this file)

CATALOG_FIELDS = ('path', 'title', 'type', 'keywords', 'description', 'status')
STATUS_OPEN = re.compile(r'(?im)^\s*\*\*Status:\*\*\s*Open\b')
LOG_HEADING = re.compile(r'###\s+(\S+)\s+-\s+(.+)')


class Run:
    """One pass: what it changed, and what it could not do."""

    def __init__(self, root: pathlib.Path, check: bool) -> None:
        self.root = root
        self.check = check
        self.report = vault.Report(root)
        self.changes: list[str] = []

    def stale(self, path: pathlib.Path, what: str) -> None:
        self.report.error(path, f'{what}; run python3 .github/scripts/update-vault.py')

    def write(self, path: pathlib.Path, data: bytes | str, what: str) -> None:
        """Write a generated file, or in --check report that it is out of date."""
        if self.check:
            self.stale(path, what)
            return
        path.parent.mkdir(parents=True, exist_ok=True)
        partial = path.with_name('.' + path.name + '.tmp~')
        if isinstance(data, str):
            partial.write_text(data, encoding='utf-8')
        else:
            partial.write_bytes(data)
        os.replace(partial, path)
        self.changes.append(f'updated: {vault.rel(self.root, path)}')


# ── 1. The memory cascade ──

def free_name(destination: pathlib.Path) -> pathlib.Path:
    """A destination no file holds yet: the name itself, else -1, -2 and so on."""
    if not destination.exists():
        return destination
    i = 1
    while True:
        candidate = destination.with_name(f'{destination.stem}-{i}{destination.suffix}')
        if not candidate.exists():
            return candidate
        i += 1


def cascade(run: Run) -> None:
    root = run.root
    if run.check:
        for name, cap, folder in vault.TIERS:
            count = len(vault.tier_summaries(root / folder))
            if count > cap:
                run.stale(root / folder, f'{name} holds {count} summaries; its cap is {cap}')
        return
    settled = False
    while not settled:
        settled = True
        for i, (_name, cap, folder) in enumerate(vault.TIERS):
            summaries = vault.tier_summaries(root / folder)
            while len(summaries) > cap:
                oldest = summaries.pop(0)
                if i + 1 < len(vault.TIERS):
                    target_dir = root / vault.TIERS[i + 1][2]
                else:
                    year = oldest.name[:4] if oldest.name[:4].isdigit() else 'undated'
                    target_dir = root / vault.ARCHIVE / year
                target_dir.mkdir(parents=True, exist_ok=True)
                target = free_name(target_dir / oldest.name)
                shutil.move(str(oldest), str(target))
                run.changes.append(f'moved: {vault.rel(root, oldest)} -> {vault.rel(root, target)}')
                settled = False


# ── 2. The generated blocks ──

def link_list(folder: str, entries: list[pathlib.Path], empty: str) -> str:
    if not entries:
        return empty
    return '\n'.join(f'- [[{folder}/{p.stem}|{p.stem}]]' for p in entries)


def open_loops(text: str) -> str:
    """The Open Loops view: every Log entry still marked **Status:** Open."""
    lines = text.split('\n')
    head = next((i for i, line in enumerate(lines) if line.strip() == '## Log Entries'), None)
    loops = []
    if head is not None:
        end = next((i for i in range(head + 1, len(lines)) if lines[i].startswith('## ')), len(lines))
        j = head + 1
        while j < end:
            if not lines[j].startswith('### '):
                j += 1
                continue
            k = j + 1
            while k < end and not lines[k].startswith('### '):
                k += 1
            if STATUS_OPEN.search('\n'.join(lines[j:k])):
                match = LOG_HEADING.match(lines[j])
                title, date = (match.group(2).strip(), match.group(1)) if match else (lines[j][4:].strip(), '')
                loops.append(f'- {title}  (opened {date})')
            j = k
    return '\n'.join(loops) if loops else '_No open loops._'


def children(root: pathlib.Path, note: pathlib.Path, ignored: frozenset[str] = frozenset()) -> str:
    """Links to the README.md of each of a folder's immediate subfolders, named by the subfolder.
    A subfolder git ignores is left out, as the walk leaves it out: no other machine has it."""
    docs = []
    for sub in sorted(note.parent.iterdir(), key=lambda p: p.name):
        if (sub.is_dir() and not sub.name.startswith('.') and vault.rel(root, sub) + '/' not in ignored
                and vault.folder_note(sub).is_file()):
            docs.append(vault.folder_note(sub))
    if not docs:
        return '_No subfolders yet._'
    return '\n'.join(f'- [[{vault.rel(root, d.parent)}/{d.stem}|{d.parent.name}]]' for d in docs)


def registered_blocks(root: pathlib.Path) -> list[tuple[pathlib.Path, str, object]]:
    """Each (note, block, how to draw it) the vault requires."""
    out: list[tuple[pathlib.Path, str, object]] = []
    for _name, _cap, folder in vault.TIERS:
        note = vault.folder_note(root / folder)
        body = '\n'.join(f'- [[{p.stem}]]' for p in vault.tier_summaries(root / folder)) \
            or '_No summaries in this tier right now._'
        out.append((note, 'tier-summaries', body))
    for name, folder in vault.COLLECTIONS:
        out.append((vault.folder_note(root / folder), 'collection-entries',
                    link_list(folder, vault.entry_files(root / folder), f'_No {name.lower()} recorded yet._')))
    for folder in vault.PROFILE_COLLECTIONS:
        out.append((vault.folder_note(root / folder), 'profile-entries',
                    link_list(folder, vault.entry_files(root / folder), '_None recorded yet._')))
    out.append((root / vault.LOG, 'open-loops', open_loops))
    return out


def blocks(run: Run) -> None:
    root = run.root
    planned: dict[pathlib.Path, list[tuple[str, object]]] = {}
    for note, name, body in registered_blocks(root):
        if note.is_file():
            planned.setdefault(note, []).append((name, body))
    ignored = vault.ignored_paths(root)
    for note in vault.walk_notes(root):
        if vault.is_folder_note(note) and not vault.is_template(note.relative_to(root).parts):
            if vault.has_block(vault.read_text(note), 'children'):
                planned.setdefault(note, []).append(('children', children(root, note, ignored)))
    for note in sorted(planned):
        text = vault.read_text(note)
        drawn = text
        for name, body in planned[note]:
            content = body(drawn) if callable(body) else body
            redrawn = vault.redraw_block(drawn, name, str(content))
            if redrawn is None:
                run.report.error(note, f'has no <!-- brain:{name} --> block for update-vault.py to draw; '
                                       f'add the start and end markers')
                continue
            drawn = redrawn
        if drawn != text:
            run.write(note, drawn, 'a generated block is out of date')


# ── 3. The catalog ──

def catalog(root: pathlib.Path) -> str:
    records = []
    for note in vault.walk_notes(root):
        if vault.is_template(note.relative_to(root).parts):
            continue
        fields = vault.note_fields(note)
        record: dict[str, object] = {}
        for key in CATALOG_FIELDS:
            if key == 'path':
                record[key] = 'BRAIN/' + vault.rel(root, note)
            elif key == 'keywords':
                record[key] = vault.as_list(fields.get(key))
            elif key == 'title':
                record[key] = str(fields.get('title', note.stem))
            else:
                value = fields.get(key, '')
                record[key] = value if isinstance(value, (list, dict)) else str(value)
        records.append((record['path'], json.dumps(record, ensure_ascii=False, sort_keys=True)))
    # Sorted by path, so a note's record sits in the same place on every machine.
    lines = [line for _path, line in sorted(records)]
    return '\n'.join(lines) + '\n' if lines else ''


def catalog_file(run: Run) -> None:
    root = run.root
    path = root / vault.CATALOG
    drawn = catalog(root)
    current = path.read_text(encoding='utf-8') if path.is_file() else None
    # A vault with no notes needs no catalog file, so a fresh one stays clean.
    needed = any(True for _ in vault.walk_notes(root))
    if current != drawn and (needed or current is not None):
        run.write(path, drawn, 'the catalog is out of date')


# ── 4. The .gitkeep markers ──

def keeps(run: Run) -> None:
    root = run.root
    ignored = vault.ignored_paths(root)
    for folder, dirs, files in os.walk(root):
        here = pathlib.Path(folder)
        dirs[:] = vault.walked_dirs(root, here, dirs, ignored)
        if here == root:
            continue
        # What git ignores is not there for git: a folder holding nothing else is empty to it.
        prefix = vault.rel(root, here) + '/'
        others = [name for name in os.listdir(here) if name not in ('.gitkeep', '.DS_Store')
                  and prefix + name not in ignored and prefix + name + '/' not in ignored]
        keep = here / '.gitkeep'
        if not others and not keep.exists():
            if run.check:
                run.stale(here, 'an empty folder needs a .gitkeep to survive git')
            else:
                keep.touch()
                run.changes.append(f'updated: {vault.rel(root, keep)}')
        elif others and keep.exists():
            if run.check:
                run.stale(keep, 'the folder has files, so its .gitkeep is stale')
            else:
                keep.unlink()
                run.changes.append(f'removed: {vault.rel(root, keep)}')


def main(argv: list[str] | None = None) -> int:
    parser = vault.arguments((__doc__ or '').split('\n', 1)[0])
    parser.add_argument('--check', action='store_true', help='write nothing; fail when anything is out of date')
    args = parser.parse_args(argv)
    run = Run(args.root.resolve(), args.check)
    for step in (cascade, blocks, catalog_file, keeps):
        step(run)
    for line in run.changes:
        print(line)
    if args.check:
        return run.report.finish('Every generated part of the vault is up to date.')
    count = len(run.changes)
    noun = 'change' if count == 1 else 'changes'
    return run.report.finish(f'{count} {noun}.' if count else 'Everything generated is up to date.')


if __name__ == '__main__':
    sys.exit(main())
