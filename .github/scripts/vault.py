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

# ── The note schema (.docs/technical/vault/Note-Schema.md) ──
#
# The account's frontmatter standard, hidden in an HTML comment: a title, a
# description and a type, with keywords and a status where they say
# something. A record or a template may add the fields its kind needs.

REQUIRED_FIELDS = ('title', 'description', 'type')
FIELDS = (*REQUIRED_FIELDS, 'keywords', 'status')
TYPES = frozenset({'index', 'guide', 'standard', 'reference', 'record', 'template'})
OWN_FIELDS = frozenset({'record', 'template'})
STATUSES = frozenset({'draft', 'deprecated', 'archived'})
STALE_STATUSES = frozenset({'deprecated', 'archived'})
MAX_KEYWORDS = 8

DATE_RE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
EM_DASH = '\u2014'

# The notes every session reads first (AGENTS.md, Start here), stable before volatile.
STARTUP = ('Profile/Working Style.md', 'Memory/Log.md')

# ── Where things live ──

SKILLS = 'System/Skills'
# A skill's source sits where the agent apps read a repository's skills, and
# Claude Code, which reads nothing under .agents/, gets a copy update-vault.py draws.
SKILL_SOURCES = '.agents/skills'
SKILL_MIRROR = '.claude/skills'
# The folder in a skill that holds the team it dispatches, when the skill keeps its own.
TEAM_FOLDER = 'agents'
CATALOG = 'System/Data/catalog.ndjson'
AGENT_CATALOG = 'System/Data/agent-catalog.json'
AGENT_HOMES = ('Ventures/Agent Resources (AR)', SKILL_SOURCES, 'Library')
HOME_LABELS = {
    'Ventures/Agent Resources (AR)': 'Agent Resources (AR)',
    SKILL_SOURCES: 'Faculties',
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
INBOX_HELD = frozenset({'Backups', 'Reports', 'Visuals', 'Ideas'})

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


# A note's block is hidden in an HTML comment, as the account's standard asks;
# an agent spec or a skill keeps the --- block its loader reads.
_CLOSERS = {'<!--': ('-->',), '---': ('---', '...')}


def frontmatter_span(text: str) -> tuple[int, int] | None:
    """Where the frontmatter's lines start and end in the text, or None when it has none.
    The block opens with a <!-- or --- first line and closes at the next line that is -->,
    or --- and ..., so a marker inside a value can never cut it short."""
    first = text.split('\n', 1)[0]
    closers = _CLOSERS.get(first.rstrip('\r').rstrip())
    if closers is None:
        return None
    start = len(first) + 1
    at = start
    while at <= len(text):
        end = text.find('\n', at)
        line = text[at:] if end == -1 else text[at:end]
        if line.rstrip('\r').rstrip() in closers:
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


def is_fenced(text: str) -> bool:
    """A --- block: an agent spec's or a skill's, the format its loader reads."""
    return text.split('\n', 1)[0].rstrip('\r').rstrip() == '---'


# ── Wikilinks ──

_WIKILINK = re.compile(r'(!?)\[\[([^\[\]\n]+?)\]\]')


def strip_code(text: str) -> str:
    """The text without fenced code and inline code, where a link is only text."""
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
    code, or inside a %% comment, are not links, so they are left out."""
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
# One library, three homes. A home is a folder of team folders, or, when it
# holds agent specs itself, a single team. A team folder holds one spec per
# agent, the --- block naming it, and a roster: the folder's own note. The
# team's members are the specs in its folder, and its lead the starred one.
# The skills are the third home: a skill that keeps its own team holds it in
# its agents/ folder, whose roster is the one note there named for the team.

def is_agent(path: pathlib.Path) -> bool:
    """An agent spec: a note whose --- block names its agent or its tools."""
    try:
        text = read_text(path)
    except OSError:
        return False
    return is_fenced(text) and bool({'name', 'tools'} & set(parse_frontmatter(text) or {}))


def _specs(folder: pathlib.Path) -> list[pathlib.Path]:
    return [p for p in sorted(folder.glob('*.md')) if p.stem.lower() != folder.name.lower() and is_agent(p)]


def _holds_skills(home: pathlib.Path) -> bool:
    """The skills folder, where each skill that keeps a team keeps it in its agents/."""
    return home.as_posix().endswith('/' + SKILL_SOURCES)


def team_dirs(home: pathlib.Path) -> list[pathlib.Path]:
    if not home.is_dir():
        return []
    if _holds_skills(home):
        return [d / TEAM_FOLDER for d in sorted(home.iterdir(), key=lambda d: d.name.lower())
                if d.is_dir() and not d.name.startswith('.') and (d / TEAM_FOLDER).is_dir()]
    if _specs(home):
        return [home]
    return [d for d in sorted(home.iterdir())
            if d.is_dir() and not d.name.startswith('.') and d.name.lower() not in NON_TEAM_DIRS]


def team_rosters(team: pathlib.Path) -> list[pathlib.Path]:
    """The notes in a skill's agents/ folder that are not agent specs: its roster, when there is exactly one."""
    return [p for p in sorted(team.glob('*.md')) if not is_agent(p)]


def team_name(team: pathlib.Path) -> str:
    """A team's name: its folder's, or, for a team a skill keeps in agents/, its roster's."""
    if team.name == TEAM_FOLDER:
        notes = team_rosters(team)
        if len(notes) == 1:
            return notes[0].stem
    return team.name


def agent_files(home: pathlib.Path) -> list[tuple[pathlib.Path, str]]:
    """Each agent spec in a home, with the team it belongs to."""
    return [(path, team_name(team)) for team in team_dirs(home) for path in _specs(team)]


def roster_files(home: pathlib.Path) -> list[tuple[pathlib.Path, str]]:
    """Each team's roster in a home: the note of a team folder that holds specs."""
    out = []
    for team in team_dirs(home):
        name = team_name(team)
        roster = team / f'{name}.md'
        if roster.is_file() and _specs(team):
            out.append((roster, name))
    return out


def members(team: pathlib.Path) -> list[str]:
    """A team's members by role, its file name: the lead first, then the rest in name order."""
    roles = [p.stem for p in _specs(team)]
    return sorted(roles, key=lambda role: (not role.startswith(STAR), role.lstrip(STAR + ' ').lower()))


def lead(team: pathlib.Path) -> str:
    """The team's lead: its one starred member, or '' when it has none."""
    starred = [role for role in members(team) if role.startswith(STAR)]
    return starred[0] if len(starred) == 1 else ''


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
    """The notes every session reads first, stable before volatile, as many as the vault holds."""
    return [root / name for name in STARTUP if (root / name).is_file()]


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
        # The Inbox's own note and its GitHub page are the folder, never a drop.
        if parts[0] in INBOX_HELD or parts[0].startswith('.') or (len(parts) == 1 and path.name in ('Inbox.md', 'README.md')):
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
