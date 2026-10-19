#!/usr/bin/env python3
"""Check each skill source against the Agent Skills format and the vault's skill layout.

WHY THIS EXISTS. A skill's source lives in System/Skills/.unpackaged/<name>/
and installs from the archive built from it. Claude refuses a skill whose
manifest breaks the Agent Skills format, and a skill that names a team that
no longer exists dispatches into nothing. The vault adds its own layout on
top (System/Skills/Skills.md): a namesake doc, a License.txt, a Changelog.md,
the assets/, references/ and templates/ folders, and no agents/ or scripts/
in the source, because agents are vendored into the archive when it is built
and scripts live in .github/scripts. This checks all of it, so a broken skill
fails in CI instead of on someone's install.

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


def junk(relative: pathlib.Path) -> bool:
    """A file that never ships in an archive, so the checks never read it either."""
    return (any(part in JUNK_DIRS for part in relative.parts) or relative.name in JUNK_FILES
            or relative.name.startswith('._') or relative.suffix.lower() in JUNK_SUFFIXES)


def check_skill(root: pathlib.Path, folder: pathlib.Path, report: vault.Report) -> None:
    manifest = folder / 'SKILL.md'
    if not manifest.is_file():
        report.error(folder, 'no SKILL.md at the root of the skill')
        return
    others = [p for p in folder.rglob('*') if p.is_file() and p != manifest and p.name.lower() == 'skill.md']
    for other in others:
        report.error(other, 'a skill holds exactly one SKILL.md, at its root; name a template manifest t-SKILL.md')
    text = vault.read_text(manifest)
    fields = vault.parse_frontmatter(text) or {}
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
    elif len(description) > 1024:
        report.error(manifest, f'the description is {len(description)} characters; the format allows 1024')
    for key in ('license', 'allowed-tools'):
        if not str(fields.get(key, '') or '').strip():
            report.error(manifest, f'the frontmatter has no {key}')
    metadata = fields.get('metadata')
    if not isinstance(metadata, dict) or not metadata:
        report.error(manifest, 'the frontmatter has no metadata block')
        metadata = {}
    team = str(metadata.get('team', '') or '').strip()
    if team and vault.find_roster(root, team) is None:
        report.error(manifest, f"metadata.team names '{team}', which no roster in the agent library defines; "
                               'point it at a staffed team or drop the key')
    if '_' in folder.name:
        report.warn(folder, 'the folder name has an underscore (Article 2.6)')
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
    if (folder / 'agents').is_dir():
        report.error(folder / 'agents', 'a source holds no agents/; the team is vendored into the archive when it is built')
    if (folder / 'scripts').is_dir():
        report.error(folder / 'scripts', 'a source holds no scripts/; the vault keeps its scripts in .github/scripts')
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
        try:
            body = path.read_bytes().decode('utf-8')
        except UnicodeDecodeError:
            continue
        except OSError as error:
            report.error(path, f'cannot be read ({error})')
            continue
        if vault.EM_DASH in body:
            report.error(path, 'em dash (Article 9.1); use a comma, colon, parentheses or a hyphen')
        if path.suffix == '.md' and vault.wikilinks(body):
            report.warn(path, 'a skill source carries no wikilinks: it is hidden from Obsidian, and they break on install')
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
