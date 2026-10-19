#!/usr/bin/env python3
"""The vault's layout, notes and schema, shared by every vault script.

WHY THIS EXISTS. The vault's checks and generators used to live in one
8,784-line engine. They now live as separate scripts in this folder, and
this module is the part they share: where things are, how a note's
frontmatter reads, what the schema allows, how a wikilink resolves, and how
a generated block is found and redrawn. One copy, so no two scripts can
disagree about what a note says.

It is a library, not a command: the scripts beside it import it. It reads
only, never writes, and needs nothing beyond Python 3.9's standard library,
because the scripts run on whatever python3 the machine has.
"""

from __future__ import annotations

import argparse
import os
import pathlib
import re
import subprocess
import sys
from typing import Iterator

ROOT = pathlib.Path(__file__).resolve().parents[2]
IN_ACTIONS = os.environ.get('GITHUB_ACTIONS') == 'true'

# ── The note schema (.docs/vault/Note-Schema.md and Tag-Vocabulary.md) ──

REQUIRED_FIELDS = (
    'title', 'description', 'status', 'tags', 'aliases', 'keywords', 'created',
    'updated', 'type', 'folder', 'layer', 'policy', 'author', 'path', 'id',
)
STATUSES = frozenset({'draft', 'active', 'deprecated', 'archived'})
STALE_STATUSES = frozenset({'deprecated', 'archived'})
TYPES = frozenset({
    'guide', 'information', 'template', 'log', 'record', 'self',
    'reference', 'script', 'agent',
})
FOLDERS = frozenset({
    'library', 'profile', 'memory', 'ventures', 'projects', 'system', 'inbox',
})
SIGNAL_TAGS = frozenset({'startup'})
SENSITIVITY_TAGS = frozenset({'sensitive'})
FRESHNESS_TAGS = frozenset({'timeless', 'enduring', 'current'})
VOCABULARY = FOLDERS | TYPES | SIGNAL_TAGS | SENSITIVITY_TAGS | FRESHNESS_TAGS

ID_RE = re.compile(r'^[a-z]{2}-[a-z0-9-]+$')
DATE_RE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
EM_DASH = '\u2014'

# ── Where things live ──

SKILLS = 'System/Skills'
SKILL_SOURCES = 'System/Skills/.unpackaged'
CATALOG = 'System/Data/catalog.ndjson'
AGENT_CATALOG = 'System/Data/agent-catalog.json'
AGENT_HOMES = ('Ventures/Agent Resources (AR)', 'Inbox/Faculties', 'Library')
HOME_LABELS = {
    'Ventures/Agent Resources (AR)': 'Agent Resources (AR)',
    'Inbox/Faculties': 'Faculties',
    'Library': 'Library',
}
NON_TEAM_DIRS = frozenset({'assets', 'references', 'templates', 'scripts'})
STAR = '★'

# The session-summary tiers, newest first, each with its cap; Recent's
# overflow moves to Archive/<year>/, which has no cap.
TIERS = (('Current', 3, 'Memory/Context/Current'), ('Recent', 6, 'Memory/Context/Recent'))
ARCHIVE = 'Memory/Context/Archive'
# Per-entry collections: a folder of one file per entry, whose namesake lists them.
COLLECTIONS = (
    ('People', 'Memory/Entities/People'),
    ('Organizations', 'Memory/Entities/Organizations'),
    ('Places', 'Memory/Entities/Places'),
    ('Decisions', 'Memory/Decisions'),
    ('Events', 'Memory/Events'),
    ('Insights', 'Memory/Insights'),
)
PROFILE_COLLECTIONS = ('Profile/Values', 'Profile/Goals', 'Profile/Skills', 'Profile/Health')
LOG = 'Memory/Log.md'
INBOX = 'Inbox'
# Inbox sub-homes that are kept, never sorted.
INBOX_HELD = frozenset({'Backups', 'Reports', 'Faculties', 'Visuals', 'Ideas'})

# Folders never walked, and files that are never notes or link targets. A
# README.md is a top folder's GitHub page and AGENTS.md the agents' rules:
# both are pages, in the hidden frontmatter standards' styling guide asks for.
SKIP_DIRS = frozenset({'Backups', '__pycache__'})
SKIP_FILES = frozenset({'.DS_Store', '.gitkeep', '.localized', 'LICENSE', 'README.md', 'AGENTS.md'})
# The only folders that carry a README.md: the seven top folders.
TOP_FOLDERS = ('Inbox', 'Library', 'Memory', 'Profile', 'Projects', 'System', 'Ventures')
TRANSIENT_SUFFIXES = ('.part', '.tmp', '.aria2', '.tmp~')


# ── Walking the vault ──

def _keep_dir(name: str) -> bool:
    """Walk every folder but hidden ones, except .template/, which holds the scaffolds."""
    return (not name.startswith('.') or name == '.template') and name not in SKIP_DIRS


def walk_files(root: pathlib.Path) -> Iterator[pathlib.Path]:
    """Every file in the vault a note could link to, in a stable order."""
    for folder, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if _keep_dir(d))
        for name in sorted(files):
            if name.startswith('.') or name in SKIP_FILES or name.endswith(TRANSIENT_SUFFIXES):
                continue
            yield pathlib.Path(folder) / name


def walk_notes(root: pathlib.Path) -> Iterator[pathlib.Path]:
    """Every Markdown note in the vault, in the same stable order."""
    for path in walk_files(root):
        if path.suffix == '.md':
            yield path


def in_walk(root: pathlib.Path, path: pathlib.Path) -> bool:
    """True when walk_files would visit this path: inside the root, outside hidden
    folders other than .template/, and not a dotfile or junk file."""
    try:
        parts = path.resolve().relative_to(root.resolve()).parts
    except (OSError, ValueError):
        return False
    if not parts or not all(_keep_dir(part) for part in parts[:-1]):
        return False
    name = parts[-1]
    return not (name.startswith('.') or name in SKIP_FILES or name.endswith(TRANSIENT_SUFFIXES))


def stray_readmes(root: pathlib.Path) -> list[pathlib.Path]:
    """Every README.md the vault walks past but the seven top folders' own.

    A README is a folder's GitHub page, and only a top folder has one: deeper
    folders are described by their notes, so a README there is a second,
    drifting copy of what the note already says.
    """
    out = []
    for folder, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if _keep_dir(d))
        if 'README.md' in files:
            path = pathlib.Path(folder) / 'README.md'
            parts = path.relative_to(root).parts
            if not (len(parts) == 2 and parts[0] in TOP_FOLDERS):
                out.append(path)
    return out


def rel(root: pathlib.Path, path: pathlib.Path) -> str:
    """The path from the vault root, with forward slashes."""
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def read_text(path: pathlib.Path) -> str:
    """A note's text. A malformed byte becomes a replacement character, so one bad file never stops a check."""
    return path.read_text(encoding='utf-8', errors='replace')


def is_template(parts: tuple[str, ...]) -> bool:
    """A scaffold: anything under a .template/ folder."""
    return '.template' in parts or 'Template' in parts


def is_folder_note(path: pathlib.Path) -> bool:
    """A folder's own note: Memory/Memory.md, Library/Arts & Recreation/Arts & Recreation.md."""
    return path.suffix == '.md' and path.stem == path.parent.name


# ── Frontmatter ──
#
# The vault's frontmatter is flat YAML: scalars, flow lists such as
# ["a", "b"], block lists, and the one-level maps a SKILL.md's metadata uses.
# This reads exactly that subset, keeps every scalar as a string, as the
# schema compares them, and never guesses at anything else.

_KEY = re.compile(r'^([A-Za-z_][\w-]*)[ \t]*:(?:[ \t]+(.*))?[ \t]*$')
_ESCAPES = {'"': '"', '\\': '\\', '/': '/', 'n': '\n', 't': '\t', 'r': '\r', '0': '\0'}


def frontmatter_span(text: str) -> tuple[int, int] | None:
    """Where the frontmatter's lines start and end in the text, or None when it has none.
    The block opens with a --- first line and closes at the next line that is --- or ...,
    so a --- inside a value can never cut it short."""
    first = text.split('\n', 1)[0]
    if first.rstrip('\r').rstrip() != '---':
        return None
    start = len(first) + 1
    at = start
    while at <= len(text):
        end = text.find('\n', at)
        line = text[at:] if end == -1 else text[at:end]
        if line.rstrip('\r').rstrip() in ('---', '...'):
            return start, at
        if end == -1:
            return None
        at = end + 1
    return None


def body_start(text: str) -> int:
    """Where a note's body begins: just past the frontmatter's closing line, or 0."""
    span = frontmatter_span(text)
    if span is None:
        return 0
    end = text.find('\n', span[1])
    return len(text) if end == -1 else end + 1


def _unquote(raw: str) -> str:
    raw = raw.strip()
    if len(raw) >= 2 and raw[0] == '"':
        out, i = [], 1
        while i < len(raw):
            c = raw[i]
            if c == '\\' and i + 1 < len(raw):
                nxt = raw[i + 1]
                if nxt == 'u' and re.fullmatch(r'[0-9a-fA-F]{4}', raw[i + 2:i + 6] or ''):
                    out.append(chr(int(raw[i + 2:i + 6], 16)))
                    i += 6
                    continue
                out.append(_ESCAPES.get(nxt, '\\' + nxt))
                i += 2
                continue
            if c == '"':
                return ''.join(out)
            out.append(c)
            i += 1
        return ''.join(out)
    if len(raw) >= 2 and raw[0] == "'":
        out, i = [], 1
        while i < len(raw):
            if raw[i] == "'":
                if raw[i + 1:i + 2] == "'":
                    out.append("'")
                    i += 2
                    continue
                return ''.join(out)
            out.append(raw[i])
            i += 1
        return ''.join(out)
    # A plain scalar: a space then # starts a comment.
    return re.split(r'[ \t]#', raw, maxsplit=1)[0].strip()


def _scan_flow(text: str) -> Iterator[tuple[int, str, bool]]:
    """Each character of a flow collection with whether it sits inside quotes.
    A quote opens a quoted scalar only where one can start: after [ { , or :,
    so the apostrophe in [Devil's Advocate] is just a letter."""
    quote, prev = '', ''
    i = 0
    while i < len(text):
        c = text[i]
        if quote:
            yield i, c, True
            if c == '\\' and quote == '"' and i + 1 < len(text):
                yield i + 1, text[i + 1], True
                i += 2
                continue
            if c == quote:
                if quote == "'" and text[i + 1:i + 2] == "'":
                    yield i + 1, "'", True
                    i += 2
                    continue
                quote, prev = '', c
        elif c in '"\'' and prev in ('', '[', '{', ',', ':'):
            quote = c
            yield i, c, True
        else:
            yield i, c, False
            if not c.isspace():
                prev = c
        i += 1


def _split_flow(inner: str) -> list[str]:
    """The items of a flow collection's inside, split on commas outside quotes and brackets."""
    items, depth, start = [], 0, 0
    for i, c, quoted in _scan_flow(inner):
        if quoted:
            continue
        if c in '[{':
            depth += 1
        elif c in ']}':
            depth -= 1
        elif c == ',' and depth == 0:
            items.append(inner[start:i])
            start = i + 1
    items.append(inner[start:])
    return [item.strip() for item in items if item.strip()]


def _flow_closed(text: str) -> bool:
    """True once every [ and { opened outside quotes is closed again."""
    depth = 0
    for _i, c, quoted in _scan_flow(text):
        if not quoted:
            if c in '[{':
                depth += 1
            elif c in ']}':
                depth -= 1
    return depth <= 0


def _flow_value(raw: str) -> list[str] | dict[str, str]:
    raw = raw.strip()
    inner = raw[1:raw.rfind(']' if raw[0] == '[' else '}')]
    if raw[0] == '[':
        return [_unquote(item) for item in _split_flow(inner)]
    pairs: dict[str, str] = {}
    for item in _split_flow(inner):
        key, _, value = item.partition(':')
        pairs[_unquote(key)] = _unquote(value)
    return pairs


def parse_frontmatter(text: str) -> dict[str, object] | None:
    """A note's frontmatter as a dict, or None when it has none.
    Scalars stay strings; flow and block lists become lists; a block of indented
    `key: value` lines becomes a dict."""
    span = frontmatter_span(text)
    if span is None:
        return None
    lines = text[span[0]:span[1]].replace('\r\n', '\n').split('\n')
    fields: dict[str, object] = {}
    i = 0
    while i < len(lines):
        match = _KEY.match(lines[i])
        i += 1
        if not match:
            continue
        key, raw = match.group(1), (match.group(2) or '').strip()
        if raw[:1] in ('[', '{'):
            while not _flow_closed(raw) and i < len(lines):
                raw += ' ' + lines[i].strip()
                i += 1
            fields[key] = _flow_value(raw)
        elif raw[:1] in ('|', '>') and re.fullmatch(r'[|>][+-]?', raw):
            block = []
            while i < len(lines) and (not lines[i].strip() or lines[i][:1] in ' \t'):
                block.append(lines[i].strip())
                i += 1
            while block and not block[-1]:
                block.pop()
            fields[key] = ('\n' if raw[0] == '|' else ' ').join(block)
        elif raw:
            fields[key] = _unquote(raw)
        else:
            nested = []
            while i < len(lines) and (lines[i][:1] in ' \t-' or not lines[i].strip()):
                if lines[i].strip():
                    nested.append(lines[i].strip())
                i += 1
            if nested and nested[0][:1] in ('[', '{'):
                # A flow collection that starts on the line after its key, as prettier writes long ones.
                fields[key] = _flow_value(' '.join(nested))
            elif nested and all(line.startswith('- ') or line == '-' for line in nested):
                fields[key] = [_unquote(line[1:]) for line in nested]
            elif nested:
                mapping: dict[str, str] = {}
                for line in nested:
                    sub = _KEY.match(line)
                    if sub:
                        mapping[sub.group(1)] = _unquote(sub.group(2) or '')
                fields[key] = mapping
            else:
                fields[key] = ''
    return fields


def as_list(value: object) -> list[str]:
    """A list field as a list, whatever shape a hand edit left it in."""
    if isinstance(value, list):
        return [str(item) for item in value]
    if value in (None, ''):
        return []
    return [str(value)]


def note_fields(path: pathlib.Path) -> dict[str, object]:
    """A note's frontmatter, or {} when it has none or cannot be read."""
    try:
        return parse_frontmatter(read_text(path)) or {}
    except OSError:
        return {}


def is_stale(fields: dict[str, object]) -> bool:
    """Deprecated or archived: kept, but no longer the live version."""
    return str(fields.get('status', '') or '').strip().lower() in STALE_STATUSES


# ── Wikilinks ──

_WIKILINK = re.compile(r'(!?)\[\[([^\[\]\n]+?)\]\]')


def strip_code(text: str) -> str:
    """The text without fenced code and inline code, where Obsidian renders no links."""
    out, fenced = [], False
    for line in text.split('\n'):
        if re.match(r'^\s*(```|~~~)', line):
            fenced = not fenced
            continue
        if not fenced:
            out.append(re.sub(r'`[^`\n]*`', '', line))
    return '\n'.join(out)


def wikilinks(text: str) -> list[str]:
    """Each wikilink's target, without its alias, heading or block. Links inside
    code, or inside an Obsidian %% comment, are not links, so they are left out."""
    visible = re.sub(r'%%.*?(?:%%|\Z)', '', strip_code(text), flags=re.S)
    targets = []
    for _embed, raw in _WIKILINK.findall(visible):
        target = raw.replace('\\|', '|').split('|')[0].split('#')[0].strip()
        if target:
            targets.append(target)
    return targets


# ── Generated blocks ──
#
# A generated block sits between a start marker, <!-- brain:NAME (note) -->,
# and an end marker, <!-- /brain:NAME -->. Only update-vault.py writes inside
# one; everything else in the note is the author's.

BLOCK_NOTE = 'drawn by .github/scripts/update-vault.py - do not edit by hand'


def _block_re(name: str) -> re.Pattern[str]:
    return re.compile(
        r'<!--\s*brain:' + re.escape(name) + r'(?![\w-])[^>]*-->(.*?)<!--\s*/brain:'
        + re.escape(name) + r'\s*-->',
        re.S,
    )


def has_block(text: str, name: str) -> bool:
    return _block_re(name).search(text) is not None


def redraw_block(text: str, name: str, body: str) -> str | None:
    """The text with one block redrawn to hold `body`, or None when the note has no such block."""
    match = _block_re(name).search(text)
    if match is None:
        return None
    drawn = f'<!-- brain:{name} ({BLOCK_NOTE}) -->\n{body}\n<!-- /brain:{name} -->'
    return text[:match.start()] + drawn + text[match.end():]


# ── The agent library ──
#
# One library, three homes. A home is a folder of team folders, or, when its
# own note lists members, a single team itself. A team folder holds one file
# per agent and a roster named after the folder that lists the members.

def team_dirs(home: pathlib.Path) -> list[pathlib.Path]:
    if not home.is_dir():
        return []
    roster = home / f'{home.name}.md'
    if roster.is_file() and 'members' in note_fields(roster):
        return [home]
    return [d for d in sorted(home.iterdir())
            if d.is_dir() and not d.name.startswith('.') and d.name.lower() not in NON_TEAM_DIRS]


def agent_files(home: pathlib.Path) -> list[tuple[pathlib.Path, str]]:
    """Each agent spec in a home, with the team it belongs to."""
    out = []
    for team in team_dirs(home):
        for path in sorted(team.glob('*.md')):
            # A README is the folder's GitHub page, never an agent.
            if path.stem.lower() != team.name.lower() and path.name not in SKIP_FILES:
                out.append((path, team.name))
    return out


def roster_files(home: pathlib.Path) -> list[tuple[pathlib.Path, str]]:
    """Each team's roster in a home. A team folder's note counts as a roster once it lists members."""
    out = []
    for team in team_dirs(home):
        roster = team / f'{team.name}.md'
        if roster.is_file() and 'members' in note_fields(roster):
            out.append((roster, team.name))
    return out


def members(fields: dict[str, object]) -> list[str]:
    return [m.strip() for m in as_list(fields.get('members')) if m.strip()]


def homes(root: pathlib.Path) -> list[pathlib.Path]:
    return [root / home for home in AGENT_HOMES if (root / home).is_dir()]


def find_roster(root: pathlib.Path, team: str) -> pathlib.Path | None:
    """The roster of the team named `team`, in any home."""
    for home in homes(root):
        for roster, name in roster_files(home):
            if name == team:
                return roster
    return None


# ── Skills ──

def skill_dirs(root: pathlib.Path) -> list[pathlib.Path]:
    """Each skill source folder, in name order."""
    sources = root / SKILL_SOURCES
    if not sources.is_dir():
        return []
    return sorted((d for d in sources.iterdir() if d.is_dir() and not d.name.startswith('.')),
                  key=lambda d: d.name.lower())


# ── Memory and the Inbox ──

def tier_summaries(folder: pathlib.Path) -> list[pathlib.Path]:
    """The session summaries in one tier folder, oldest first. The tier's own note is not one."""
    if not folder.is_dir():
        return []
    return sorted(p for p in folder.iterdir()
                  if p.is_file() and p.suffix == '.md' and p.stem != folder.name
                  and not p.name.startswith('.'))


def entry_files(folder: pathlib.Path) -> list[pathlib.Path]:
    """The entries of a per-entry collection, in name order. The folder's own note is not one."""
    if not folder.is_dir():
        return []
    return sorted(p for p in folder.iterdir()
                  if p.is_file() and p.suffix == '.md' and p.stem != folder.name
                  and not p.name.startswith('.'))


def startup_notes(root: pathlib.Path) -> list[pathlib.Path]:
    """The notes tagged startup, stable before volatile: by layer, with Memory last."""
    tagged = []
    for path in walk_notes(root):
        if is_template(path.relative_to(root).parts):
            continue
        fields = note_fields(path)
        if 'startup' in as_list(fields.get('tags')):
            try:
                layer = int(str(fields.get('layer', '')))
            except ValueError:
                layer = 99
            tagged.append(((layer, fields.get('folder') == 'memory', rel(root, path)), path))
    return [path for _key, path in sorted(tagged)]


def inbox_drops(root: pathlib.Path) -> list[pathlib.Path]:
    """The loose files waiting at the Inbox, outside the sub-homes it keeps."""
    inbox = root / INBOX
    if not inbox.is_dir():
        return []
    out = []
    for path in sorted(inbox.rglob('*')):
        if not path.is_file() or path.name.startswith('.'):
            continue
        parts = path.relative_to(inbox).parts
        if parts[0] in INBOX_HELD or parts[0].startswith('.') or (len(parts) == 1 and path.name == 'Inbox.md'):
            continue
        out.append(path)
    return out


# ── git ──

def tracked_files(root: pathlib.Path) -> list[str] | None:
    """The files git tracks, or None outside a checkout."""
    try:
        result = subprocess.run(['git', '-C', str(root), 'ls-files', '-z'],
                                capture_output=True, timeout=60, check=False)
    except (OSError, subprocess.SubprocessError):
        return None
    if result.returncode != 0:
        return None
    return [name for name in result.stdout.decode('utf-8', 'replace').split('\0') if name]


# ── Reporting ──

class Report:
    """Findings, printed one to a line and, under GitHub Actions, as annotations on the file."""

    def __init__(self, root: pathlib.Path, quiet: bool = False) -> None:
        self.root = root
        self.quiet = quiet
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def _where(self, path: pathlib.Path | str | None, line: int | None) -> tuple[str, str]:
        if path is None:
            return '', ''
        name = path if isinstance(path, str) else rel(self.root, path)
        return name, (f'{name}:{line}' if line else name)

    def error(self, path: pathlib.Path | str | None, message: str, line: int | None = None) -> None:
        name, where = self._where(path, line)
        self.errors.append(f'{where}: {message}' if where else message)
        if IN_ACTIONS and name:
            print(f'::error file={name}{f",line={line}" if line else ""}::{message}')

    def warn(self, path: pathlib.Path | str | None, message: str, line: int | None = None) -> None:
        name, where = self._where(path, line)
        self.warnings.append(f'{where}: {message}' if where else message)
        if IN_ACTIONS and name:
            print(f'::warning file={name}{f",line={line}" if line else ""}::{message}')

    def finish(self, passed: str) -> int:
        """Print what was found, or `passed` when nothing was, and return the exit code."""
        for line in self.errors:
            print(f'error: {line}')
        for line in self.warnings:
            print(f'warning: {line}')
        if self.errors:
            noun = 'problem' if len(self.errors) == 1 else 'problems'
            print(f'{len(self.errors)} {noun}.', file=sys.stderr)
            return 1
        if not self.quiet:
            print(passed)
        return 0


def arguments(description: str) -> argparse.ArgumentParser:
    """An argument parser that knows --root, the vault to work on (the repository by default)."""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--root', type=pathlib.Path, default=ROOT,
                        help='the vault to work on (default: this repository)')
    return parser
