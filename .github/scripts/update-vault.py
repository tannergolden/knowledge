#!/usr/bin/env python3
"""Bring every generated part of the vault up to date, or report what is stale.

WHY THIS EXISTS. Some of the vault is derived from the rest, and a person or
an AI keeping it by hand would let it drift. This script owns all of it:

1. The memory cascade. Memory/Context/Current holds at most 3 session
   summaries and Recent at most 6; the oldest move down a tier, and Recent's
   overflow moves to Archive/<year>/. Nothing is ever deleted.
2. The generated blocks, between <!-- brain:NAME --> and <!-- /brain:NAME -->:
   each tier's list of summaries, each Memory collection's and Profile
   facet's list of entries, the subfolder list in any folder note that asks
   for one, and the Open Loops view of Memory/Log.md.
3. The catalogs: System/Data/catalog.ndjson, one record per note, and
   System/Data/agent-catalog.json, every agent and team in the library.
4. The skill archives: System/Skills/<name>.skill, each built from its source
   with its team vendored, so an installed skill carries its agents.
5. The .gitkeep markers: an empty folder keeps one, a folder with files loses it.

Run it after a change. With --check it
writes nothing and fails when anything is out of date, which is what CI runs.
Archives are compared by their contents, never their bytes, since two zlib
builds compress the same files differently.

Run it:

    python3 .github/scripts/update-vault.py
    python3 .github/scripts/update-vault.py --check
"""

from __future__ import annotations

import io
import json
import os
import pathlib
import re
import shutil
import sys
import zipfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import vault  # noqa: E402  (vault.py sits beside this file)

FIXED_DATE = (1980, 1, 1, 0, 0, 0)  # the earliest a zip records, so a rebuild changes nothing
JUNK_DIRS = frozenset({'__pycache__', '.git', '.obsidian', '.trash'})
JUNK_FILES = frozenset({'.DS_Store', 'Thumbs.db'})
JUNK_SUFFIXES = frozenset({'.pyc', '.pyo', '.skill', '.swp'})
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


def children(root: pathlib.Path, note: pathlib.Path) -> str:
    """Links to the notes of a folder's immediate subfolders."""
    docs = []
    for sub in sorted(note.parent.iterdir(), key=lambda p: p.name):
        if sub.is_dir() and not sub.name.startswith('.') and sub.name != 'Template' and (sub / f'{sub.name}.md').is_file():
            docs.append(sub / f'{sub.name}.md')
    if not docs:
        return '_No subfolders yet._'
    return '\n'.join(f'- [[{vault.rel(root, d.parent)}/{d.stem}|{d.stem}]]' for d in docs)


def registered_blocks(root: pathlib.Path) -> list[tuple[pathlib.Path, str, object]]:
    """Each (note, block, how to draw it) the vault requires."""
    out: list[tuple[pathlib.Path, str, object]] = []
    for _name, _cap, folder in vault.TIERS:
        note = root / folder / f'{pathlib.PurePosixPath(folder).name}.md'
        body = '\n'.join(f'- [[{p.stem}]]' for p in vault.tier_summaries(root / folder)) \
            or '_No summaries in this tier right now._'
        out.append((note, 'tier-summaries', body))
    for name, folder in vault.COLLECTIONS:
        out.append((root / folder / f'{name}.md', 'collection-entries',
                    link_list(folder, vault.entry_files(root / folder), f'_No {name.lower()} recorded yet._')))
    for folder in vault.PROFILE_COLLECTIONS:
        name = pathlib.PurePosixPath(folder).name
        out.append((root / folder / f'{name}.md', 'profile-entries',
                    link_list(folder, vault.entry_files(root / folder), '_None recorded yet._')))
    out.append((root / vault.LOG, 'open-loops', open_loops))
    return out


def blocks(run: Run) -> None:
    root = run.root
    planned: dict[pathlib.Path, list[tuple[str, object]]] = {}
    for note, name, body in registered_blocks(root):
        if note.is_file():
            planned.setdefault(note, []).append((name, body))
    for note in vault.walk_notes(root):
        if vault.is_folder_note(note) and not vault.is_template(note.relative_to(root).parts):
            if vault.has_block(vault.read_text(note), 'children'):
                planned.setdefault(note, []).append(('children', children(root, note)))
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


# ── 3. The catalogs ──

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


def agent_catalog(root: pathlib.Path) -> str:
    agents, teams, labels = [], [], []
    for home in vault.homes(root):
        label = vault.HOME_LABELS.get(vault.rel(root, home), vault.rel(root, home))
        labels.append(label)
        for path, team in vault.agent_files(home):
            fields = vault.note_fields(path)
            agents.append({
                'name': str(fields.get('name', '') or '').strip(),
                'role': path.stem,
                'home': label,
                'team': team,
                'description': str(fields.get('description', '') or '').strip(),
                'path': 'BRAIN/' + vault.rel(root, path),
            })
        for path, team in vault.roster_files(home):
            fields = vault.note_fields(path)
            teams.append({
                'team': team,
                'home': label,
                'lead': vault.lead(path.parent),
                'members': vault.members(path.parent),
                'description': str(fields.get('description', '') or '').strip(),
                'path': 'BRAIN/' + vault.rel(root, path),
            })
    agents.sort(key=lambda a: (a['home'], a['team'], a['role'].lstrip(vault.STAR + ' ')))
    teams.sort(key=lambda t: (t['home'], t['team']))
    body = {
        'schema_version': 1,
        'home_count': len(labels),
        'team_count': len(teams),
        'agent_count': len(agents),
        'homes': labels,
        'agents': agents,
        'teams': teams,
    }
    return json.dumps(body, indent=2, ensure_ascii=False) + '\n'


def catalogs(run: Run) -> None:
    root = run.root
    # A vault with nothing to catalog needs no catalog file, so a fresh one stays clean.
    wanted = ((vault.CATALOG, catalog(root), any(True for _ in vault.walk_notes(root))),
              (vault.AGENT_CATALOG, agent_catalog(root), bool(vault.homes(root))))
    for relative, drawn, needed in wanted:
        path = root / relative
        current = path.read_text(encoding='utf-8') if path.is_file() else None
        if current != drawn and (needed or current is not None):
            run.write(path, drawn, 'the catalog is out of date')


# ── 4. The skill archives ──

def junk(relative: pathlib.Path) -> bool:
    return (any(part in JUNK_DIRS for part in relative.parts) or relative.name in JUNK_FILES
            or relative.name.startswith('._') or relative.suffix.lower() in JUNK_SUFFIXES)


def archive_entries(root: pathlib.Path, folder: pathlib.Path, report: vault.Report) -> dict[str, bytes]:
    """Each entry the skill's archive holds, and its bytes."""
    name = folder.name
    entries: dict[str, bytes] = {}
    for path in sorted(folder.rglob('*')):
        relative = path.relative_to(folder)
        if path.is_dir() or path.is_symlink() or junk(relative):
            continue
        data = path.read_bytes()
        if len(relative.parts) == 1 and path.suffix == '.md' and path.name != 'SKILL.md' \
                and path.stem.lower() == name.lower():
            # The namesake travels without its vault frontmatter: the guide ships, the metadata stays.
            text = data.decode('utf-8', 'replace')
            data = text[vault.body_start(text):].lstrip('\n').encode('utf-8')
        entries[f'{name}/{relative.as_posix()}'] = data
    manifest = folder / 'SKILL.md'
    fields = (vault.parse_frontmatter(vault.read_text(manifest)) or {}) if manifest.is_file() else {}
    meta = fields.get('metadata')
    team = str(meta.get('team', '') or '').strip() if isinstance(meta, dict) else ''
    if team and not (folder / 'agents').is_dir():
        roster = vault.find_roster(root, team)
        if roster is None:
            report.error(folder / 'SKILL.md', f"metadata.team names '{team}', which no roster defines, "
                                             'so the archive cannot carry its team')
            return entries
        by_role = {path.stem: path for home in vault.homes(root) for path, _team in vault.agent_files(home)}
        entries[f'{name}/agents/{roster.name}'] = roster.read_bytes()
        for member in vault.members(roster.parent):
            path = by_role.get(member)
            if path is None:
                report.error(roster, f"names '{member}', which no agent file in the library is named")
                continue
            entries[f'{name}/agents/{path.name}'] = path.read_bytes()
    return dict(sorted(entries.items()))


def zipped(entries: dict[str, bytes]) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in entries.items():
            info = zipfile.ZipInfo(name, date_time=FIXED_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, data)
    return buffer.getvalue()


def unzipped(path: pathlib.Path) -> dict[str, bytes] | None:
    try:
        with zipfile.ZipFile(path) as archive:
            return {name: archive.read(name) for name in sorted(archive.namelist()) if not name.endswith('/')}
    except (OSError, zipfile.BadZipFile):
        return None


def archives(run: Run) -> None:
    root = run.root
    sources = vault.skill_dirs(root)
    for folder in sources:
        entries = archive_entries(root, folder, run.report)
        path = root / vault.SKILLS / f'{folder.name}.skill'
        if unzipped(path) != entries:
            run.write(path, zipped(entries), "the archive differs from its source")
    built = {folder.name for folder in sources}
    skills = root / vault.SKILLS
    if skills.is_dir():
        for path in sorted(skills.glob('*.skill')):
            if path.stem not in built:
                run.report.error(path, 'has no source in System/Skills/.unpackaged; delete it or restore the source')


# ── 5. The .gitkeep markers ──

def keeps(run: Run) -> None:
    root = run.root
    for folder, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if (not d.startswith('.') or d == '.template') and d not in vault.SKIP_DIRS)
        here = pathlib.Path(folder)
        if here == root:
            continue
        others = [name for name in os.listdir(here) if name not in ('.gitkeep', '.DS_Store')]
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
    for step in (cascade, blocks, catalogs, archives, keeps):
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
