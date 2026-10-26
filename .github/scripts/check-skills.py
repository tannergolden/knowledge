#!/usr/bin/env python3
"""Check each skill against the Agent Skills format and the vault's skill layout.

WHY THIS EXISTS. A skill lives in .agents/skills/<name>/, where the agent apps
read a repository's skills. update-vault.py copies it to .claude/skills/ for
Claude Code and packs it into System/Skills/<name>.skill for the Claude app,
and tannergolden/intelligence's home kit carries the faculties from a release
of this template. An app refuses a skill whose manifest breaks the Agent
Skills format, the home kit refuses one that breaks its stricter reading of
it, and a skill that names a team that no longer exists dispatches into
nothing. The vault adds its own layout on top (System/Skills/Skills.md): a
namesake doc, a License.txt, a Changelog.md, the assets/, references/ and
templates/ folders, a team in agents/ only when the skill keeps its own, and
no scripts/, because the vault keeps its scripts in .github/scripts. A
faculty, a skill with its own team, also opens with the rule that hands a
home copy of it over to a vault's own, word for word, because the home kit
carries the faculties and refuses one without it. This checks all of it, so
a broken skill fails in CI instead of on someone's install.

With no arguments it checks every skill; given names, only those.

Run it:

    python3 .github/scripts/check-skills.py
    python3 .github/scripts/check-skills.py research
"""

from __future__ import annotations

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import vault  # noqa: E402  (vault.py sits beside this file)

JUNK_DIRS = frozenset({'__pycache__', '.git', '.obsidian', '.trash'})
JUNK_FILES = frozenset({'.DS_Store', 'Thumbs.db'})
JUNK_SUFFIXES = frozenset({'.pyc', '.pyo', '.skill', '.swp'})
NAME = re.compile(r'[a-z0-9]+(-[a-z0-9]+)*')
CURRENT_VERSION = re.compile(r'##\s+Current Version\b.*?\*\*`([^`]+)`\*\*', re.S)
# What the home kit's reader accepts (tannergolden/intelligence, kit.py): these
# keys only, each on one line, a description that says when, and a short body.
KEYS = ('name', 'description', 'license', 'compatibility', 'metadata', 'allowed-tools')
ONE_LINE = re.compile(r'^[A-Za-z][A-Za-z0-9-]*:')
MAX_DESCRIPTION = 1024
MAX_BODY_LINES = 500
# allowed-tools pre-approves what it lists while the skill runs, so it lists
# these read-only tools alone; writing, running commands, starting agents and
# every MCP tool go through the session's own permissions.
READ_ONLY = ('Read', 'Grep', 'Glob', 'WebFetch', 'WebSearch', 'AskUserQuestion')
# A tool in allowed-tools, with or without a scope such as Bash(git push:*);
# the list may be separated by commas or spaces.
TOOL = re.compile(r'([A-Za-z_][\w-]*)\s*(?:\([^)]*\))?')
# The characters a YAML plain value may not start with.
YAML_INDICATORS = frozenset(',[]{}#&*!|>\'"%@`')
# The escapes YAML allows in a double-quoted value.
YAML_ESCAPE = re.compile(r'\\(?:[0abtnvfre "/\\N_LP\t]|x[0-9A-Fa-f]{2}|u[0-9A-Fa-f]{4}|U[0-9A-Fa-f]{8})')
# The rule a faculty, a skill with its own team, opens with, word for word, for
# its own name. tannergolden/intelligence's home kit carries the faculties to
# every repository, where Claude Code loads its copy over a vault's, and
# refuses a faculty without this rule, which hands that copy over.
HANDOVER = ("**Where it runs.** In a BRAIN vault, whose `AGENTS.md` says it is one, the vault's own copy of this "
            "skill runs: if the file you loaded is not that vault's `.agents/skills/{name}/SKILL.md` or "
            "`.claude/skills/{name}/SKILL.md`, read the vault's copy and follow it instead, with the files beside "
            "it, because a vault's copy matches its layout and its owner may have changed it.")
BACKSLASH = chr(92)  # one backslash, which kit.py refuses outside inline code in a SKILL.md body
DASHES = re.compile('[\u2013\u2014\u2015]')


def junk(relative: pathlib.Path) -> bool:
    """A file that never ships in an archive, so the checks never read it either."""
    return (any(part in JUNK_DIRS for part in relative.parts) or relative.name in JUNK_FILES
            or relative.name.startswith('._') or relative.suffix.lower() in JUNK_SUFFIXES)


def closing_quote(value: str) -> int | None:
    """Where a quoted value's closing quote stands, or None when it never closes."""
    quote, i = value[0], 1
    while i < len(value):
        if quote == '"' and value[i] == BACKSLASH:
            i += 2
            continue
        if value[i] == quote:
            if quote == "'" and value[i + 1:i + 2] == "'":
                i += 2
                continue
            return i
        i += 1
    return None


def yaml_value_problem(value: str) -> str | None:
    """Why YAML would not read this one-line value as written, or None when it would."""
    first = value[0]
    if first in '"\'':
        end = closing_quote(value)
        if end is None:
            return 'its quote never closes'
        if value[end + 1:].strip():
            return 'text follows its closing quote, so quote the whole value'
        if first == '"' and BACKSLASH in YAML_ESCAPE.sub('', value[1:end]):
            return 'it holds a backslash YAML does not read as an escape'
        return None
    if first in '[{':
        if not value.rstrip().endswith(']' if first == '[' else '}'):
            return 'it opens a list or map it never closes'
        return flow_problem(value.strip()[1:-1], first == '{')
    if first in YAML_INDICATORS:
        return f'it starts with {first}, which YAML reads as structure'
    if first in '-?:' and (len(value) == 1 or value[1] in ' \t'):
        return f'it starts with "{first} ", which YAML reads as structure'
    if ': ' in value or ':\t' in value or value.endswith(':'):
        return 'YAML reads a colon before a space, or at the end, as structure'
    if ' #' in value or '\t#' in value:
        return 'YAML reads " #" as the start of a comment'
    return None


def flow_problem(inside: str, is_map: bool) -> str | None:
    """Why YAML would misread an item of a one-line list or map, or None when it reads each as written."""
    items, start, quote = [], 0, ''
    for i, char in enumerate(inside):
        if quote:
            if char == quote and inside[i - 1:i] != BACKSLASH:
                quote = ''
        elif char in '"\'':
            quote = char
        elif char == ',':
            items.append(inside[start:i])
            start = i + 1
    items.append(inside[start:])
    for item in (item.strip() for item in items):
        if not item:
            continue
        if is_map:
            key, colon, item = item.partition(': ')
            if not colon:
                return f'its map entry {key[:20]!r} is not "key: value"'
            item = item.strip()
        if item and item[0] not in '"\'' and any(char in item for char in '[]{}'):
            return f'its entry {item[:20]!r} nests a list or map, where a value stays plain or quoted'
        problem = yaml_value_problem(item) if item else None
        if problem:
            return f'its entry {item[:20]!r} needs quotes ({problem})'
    return None


def check_manifest_shape(manifest: pathlib.Path, text: str, report: vault.Report) -> None:
    """The frontmatter as the strictest reader takes it: a first-line fence, then one key to a line."""
    lines = text.split('\n')
    if lines[0].rstrip('\r').rstrip() != '---':
        report.error(manifest, 'SKILL.md opens with a --- frontmatter fence on its first line')
        return
    end = next((i for i in range(1, len(lines)) if lines[i].rstrip('\r').rstrip() == '---'), None)
    if end is None:
        report.error(manifest, 'the frontmatter has no closing ---')
        return
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        if not ONE_LINE.match(line):
            report.error(manifest, f'keep each frontmatter key on one line, metadata as a one-line map, '
                                   f'because some loaders read nothing else: {line.strip()[:40]}')
            continue
        key, _, value = line.partition(':')
        value = value.strip()
        problem = yaml_value_problem(value) if value else None
        if problem:
            report.error(manifest, f'quote the {key} value: {problem}, and a loader that cannot parse the '
                                   'frontmatter drops it')
    body = '\n'.join(lines[end + 1:]).lstrip('\n')
    if body.count('\n') > MAX_BODY_LINES:
        report.error(manifest, f'the body is over {MAX_BODY_LINES} lines; move detail into references/')
    if BACKSLASH in re.sub(r'`[^`]*`', '', body).replace(BACKSLASH + '\n', ''):
        report.error(manifest, 'write paths with forward slashes: the home kit refuses a backslash in the body '
                               'outside inline code')


def check_team(root: pathlib.Path, folder: pathlib.Path, manifest: pathlib.Path, team: str,
               report: vault.Report) -> None:
    """A team kept in agents/ is the one metadata.team names, and only a skill's own team sits there."""
    held = folder / vault.TEAM_FOLDER
    if not held.is_dir():
        return
    if not team:
        report.error(held, f'{vault.TEAM_FOLDER}/ holds a team, so metadata.team names it')
        return
    roster = vault.find_roster(root, team)
    if roster is not None and roster.parent != held:
        report.error(held, f"metadata.team names '{team}', whose roster is {vault.rel(root, roster)}; "
                           f'a skill keeps only its own team in {vault.TEAM_FOLDER}/')


def check_skill(root: pathlib.Path, folder: pathlib.Path, report: vault.Report) -> None:
    manifest = folder / 'SKILL.md'
    if not manifest.is_file():
        report.error(folder, 'no SKILL.md at the root of the skill')
        return
    others = [p for p in folder.rglob('*') if p.is_file() and p != manifest and p.name.lower() == 'skill.md']
    for other in others:
        report.error(other, 'a skill holds exactly one SKILL.md, at its root; name a template manifest t-SKILL.md')
    text = vault.read_text(manifest)
    check_manifest_shape(manifest, text, report)
    fields = vault.parse_frontmatter(text) or {}
    extra = sorted(set(fields) - set(KEYS))
    if extra:
        report.error(manifest, f'the frontmatter may hold only {", ".join(KEYS)}, not {", ".join(extra)}')
    name = str(fields.get('name', '') or '')
    description = str(fields.get('description', '') or '')
    if not name:
        report.error(manifest, 'the frontmatter has no name')
    elif not NAME.fullmatch(name) or len(name) > 64:
        report.error(manifest, f"name '{name}' must be kebab-case and at most 64 characters")
    elif name != folder.name:
        report.error(manifest, f"name '{name}' differs from its folder, {folder.name}")
    if name and re.search(r'claude|anthropic', name, re.I):
        report.error(manifest, f"name '{name}' may not contain claude or anthropic (Agent Skills format)")
    if not description:
        report.error(manifest, 'the frontmatter has no description')
    else:
        if len(description) > MAX_DESCRIPTION:
            report.error(manifest, f'the description is {len(description)} characters; the format allows '
                                   f'{MAX_DESCRIPTION}')
        if 'Use when' not in description:
            report.error(manifest, 'the description says when to use the skill, with "Use when"')
        if '<' in description or '>' in description:
            report.error(manifest, 'the description may not hold angle brackets')
    for key in ('license', 'allowed-tools'):
        if not str(fields.get(key, '') or '').strip():
            report.error(manifest, f'the frontmatter has no {key}')
    tools = {match.group(1) for match in TOOL.finditer(str(fields.get('allowed-tools', '') or ''))}
    others = sorted(tool for tool in tools if tool not in READ_ONLY)
    if others:
        report.error(manifest, f'allowed-tools pre-approves read-only tools only, {", ".join(READ_ONLY)}; '
                               f'{", ".join(others)} goes through the session\'s own permissions')
    metadata = fields.get('metadata')
    if not isinstance(metadata, dict) or not metadata:
        report.error(manifest, 'the frontmatter has no metadata block')
        metadata = {}
    team = str(metadata.get('team', '') or '').strip()
    if team and vault.find_roster(root, team) is None:
        report.error(manifest, f"metadata.team names '{team}', which no roster in the agent library defines; "
                               'point it at a staffed team or drop the key')
    check_team(root, folder, manifest, team, report)
    opening = text.split('\n## ', 1)[0]
    if (folder / vault.TEAM_FOLDER).is_dir() and HANDOVER.format(name=folder.name) not in opening:
        report.error(manifest, 'a faculty, a skill with its own team, opens with the hand-over rule word for word, '
                               'before its first section, naming its own copies (System/Skills/Skills.md); the home '
                               'kit refuses one without it')
    if '_' in folder.name:
        report.warn(folder, 'the folder name has an underscore (AGENTS.md, Conventions)')
    namesake = next((p for p in sorted(folder.glob('*.md'))
                     if p.name != 'SKILL.md' and p.stem.lower() == folder.name.lower()), None)
    for required in ('License.txt', 'Changelog.md'):
        if not (folder / required).is_file():
            report.error(folder, f'{required} is missing')
    if namesake is None:
        report.error(folder, f'the namesake doc, {folder.name.capitalize()}.md, is missing')
    for required in ('assets', 'references', 'templates'):
        if not (folder / required).is_dir():
            report.error(folder, f'the {required}/ folder is missing')
    if (folder / 'scripts').is_dir():
        report.error(folder / 'scripts', 'a skill holds no scripts/; the vault keeps its scripts in .github/scripts')
    version = str(metadata.get('version', '') or '').strip()
    changelog = folder / 'Changelog.md'
    if not version:
        report.error(manifest, 'metadata.version is missing')
    elif changelog.is_file():
        current = CURRENT_VERSION.search(vault.read_text(changelog))
        if current is None:
            report.error(changelog, 'no `## Current Version` line with the version in bold code')
        elif current.group(1).strip() != version:
            report.error(changelog, f'the Current Version is {current.group(1).strip()}, but SKILL.md says {version}')
    for doc in (namesake, changelog):
        if doc is None or not doc.is_file():
            continue
        doc_fields = vault.note_fields(doc)
        missing = [field for field in vault.REQUIRED_FIELDS if field not in doc_fields]
        if missing:
            report.error(doc, f'the frontmatter lacks {", ".join(missing)}')
        if 'version' in doc_fields:
            report.error(doc, "per-file versions are retired; the skill's version lives in SKILL.md "
                              'metadata.version and the Changelog\'s Current Version line, so remove the field')
    for path in sorted(folder.rglob('*')):
        relative = path.relative_to(folder)
        if not path.is_file() or junk(relative):
            continue
        if len(relative.parts) > 2:
            report.error(path, 'keep every file at most one folder below SKILL.md, where every app finds it')
        try:
            body = path.read_bytes().decode('utf-8')
        except UnicodeDecodeError:
            report.error(path, 'a skill ships text only')
            continue
        except OSError as error:
            report.error(path, f'cannot be read ({error})')
            continue
        if DASHES.search(body):
            report.error(path, 'an en or em dash (DOC-002); use a comma, colon, parentheses or a spaced hyphen')
        if path.suffix == '.md' and vault.wikilinks(body):
            report.warn(path, 'a skill carries no wikilinks: they break when the skill is installed')
    if not re.search(r'^##\s+Boundaries\b', text, re.M):
        report.error(manifest, 'SKILL.md has no ## Boundaries section')


def main(argv: list[str] | None = None) -> int:
    parser = vault.arguments((__doc__ or '').split('\n', 1)[0])
    parser.add_argument('names', nargs='*', help='skills to check (default: every skill)')
    args = parser.parse_args(argv)
    root = args.root.resolve()
    folders = vault.skill_dirs(root)
    if args.names:
        known = {folder.name: folder for folder in folders}
        unknown = [name for name in args.names if name not in known]
        if unknown:
            print(f'no skill named {", ".join(unknown)}; the skills are {", ".join(known) or "none"}', file=sys.stderr)
            return 2
        folders = [known[name] for name in args.names]
    report = vault.Report(root)
    for folder in folders:
        check_skill(root, folder, report)
    noun = 'skill passes' if len(folders) == 1 else 'skills pass'
    return report.finish(f'{len(folders)} {noun}.')


if __name__ == '__main__':
    sys.exit(main())
