#!/usr/bin/env python3
"""Check each note's frontmatter and naming against the vault's schema.

WHY THIS EXISTS. Every note in the vault opens with the account's hidden
frontmatter (.docs/technical/vault/Note-Schema.md): a title, a description and a type,
with keywords and a status where they say something. Retrieval, the catalog
and every agent that routes by a note's head read those fields, so a note
that drifts from the schema misleads every one of them, quietly. This is the
gate: run it on a note after an edit, and CI runs it on every note.

With no arguments it checks every note the vault walks: every folder but
hidden ones, plus the .template/ scaffolds. Given files, it checks only
those. A file outside the walk, such as one under .github/, is not a note and
is skipped, and an agent spec, whose --- block its loader reads, is left to
check-agents.py. A README.md belongs only in the seven top folders, as their
GitHub page, so one anywhere else is flagged.

Run it:

    python3 .github/scripts/lint-notes.py
    python3 .github/scripts/lint-notes.py "Memory/Log.md"
"""

from __future__ import annotations

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import vault  # noqa: E402  (vault.py sits beside this file)

# Retired on every note: tags and category, which type and keywords replace, and per-file
# versions, which git replaces (AGENTS.md, Conventions).
RETIRED = frozenset({'tags', 'category', 'version'})
# The rest of the old two-band schema, each field now said by the path or git. A record or
# a template may still define one of these names as a field of its own kind.
RETIRED_UNLESS_OWN = frozenset({'aliases', 'created', 'updated', 'folder', 'layer', 'policy',
                                'author', 'path', 'id'})
# A Library holding's estimated lifespan, one token among its keywords (Library/Library.md, Rules).
FRESHNESS = ('freshness/timeless', 'freshness/enduring', 'freshness/current')
# GitHub's five alerts, the only callouts a note uses (AGENTS.md, Conventions), each marker alone on its line.
ALERTS = ('NOTE', 'TIP', 'IMPORTANT', 'WARNING', 'CAUTION')
CALLOUT = re.compile(r'^[ \t]*(?:>[ \t]*)+\[!([^\]\n]*)\]([^\n]*)$', re.M)


def check_fields(fields: dict[str, object], template: bool, problems: list[str]) -> None:
    for field in vault.REQUIRED_FIELDS:
        if not str(fields.get(field, '') or '').strip():
            problems.append(f'missing field: {field}')
    kind = str(fields.get('type', '') or '')
    if kind and kind not in vault.TYPES:
        problems.append(f"type '{kind}' is not one of {sorted(vault.TYPES)}")
    if kind == 'template' and not template:
        problems.append("type 'template' outside a .template/ folder; give the copy its real type")
    for key in fields:
        if key in RETIRED or (key in RETIRED_UNLESS_OWN and kind not in vault.OWN_FIELDS):
            problems.append(f"'{key}' is retired (Note-Schema.md); remove the line")
        elif key not in vault.FIELDS and kind not in vault.OWN_FIELDS:
            problems.append(f"'{key}' is not one of a note's fields ({', '.join(vault.FIELDS)}); only "
                            'a record or a template adds fields of its own')
    status = str(fields.get('status', '') or '').strip().lower()
    if status and kind != 'template':
        if status == 'active':
            problems.append('status is active; leave it out while the note is current')
        elif status not in vault.STATUSES:
            problems.append(f"status '{status}' is not one of {sorted(vault.STATUSES)}")
    if 'keywords' in fields:
        words = fields['keywords']
        if not isinstance(words, list) or not words:
            problems.append('keywords is not a list of terms; write it inline as ["a", "b"], or leave it out')
        else:
            if len(words) > vault.MAX_KEYWORDS:
                problems.append(f'{len(words)} keywords; keep the {vault.MAX_KEYWORDS} that best find the note')
            for word in words:
                if word != word.lower():
                    problems.append(f"keyword '{word}' is not lowercase")
            if len(set(words)) != len(words):
                problems.append('a keyword appears twice')


def check_note(root: pathlib.Path, path: pathlib.Path) -> list[str]:
    """The problems with one note."""
    problems: list[str] = []
    try:
        text = vault.read_text(path)
    except OSError as error:
        return [f'cannot be read ({error})']
    parts = path.relative_to(root).parts
    template = vault.is_template(parts)
    if not text.strip():
        problems.append('the note is empty, and a note is never emptied (AGENTS.md, Ask first); restore it from git history or delete it')
    if '_' in path.name:
        problems.append('the file name has an underscore (AGENTS.md, Conventions); use spaces or hyphens')
    if vault.EM_DASH in text:
        problems.append(f'{text.count(vault.EM_DASH)} em dash(es) (DOC-002); use a comma, colon, parentheses or a hyphen')
    for kind, rest in CALLOUT.findall(vault.strip_code(text)):
        if kind not in ALERTS or rest.strip():
            problems.append(f'callout [!{kind}]{rest.rstrip()} does not render on GitHub (AGENTS.md, Conventions); use one of '
                            f"{', '.join(ALERTS)}, alone on its line, with any title as a bold first line")
    if template and '[[' in text:
        problems.append('a scaffold carries no wikilinks (Link-Topology.md)')
    fields = vault.parse_frontmatter(text)
    if fields is None:
        if text.strip():
            problems.append('no frontmatter block')
        return problems
    if vault.is_fenced(text):
        if 'name' not in fields:
            problems.append('the frontmatter is fenced with ---, which GitHub shows as a table; '
                            'wrap the fields in <!-- and --> (Note-Schema.md)')
        return problems
    check_fields(fields, template, problems)
    kind = str(fields.get('type', '') or '')
    if parts[0] == 'Library' and not template and kind not in ('index', 'record', 'template'):
        tokens = [w for w in vault.as_list(fields.get('keywords')) if w.startswith('freshness/')]
        if len(tokens) != 1 or tokens[0] not in FRESHNESS:
            problems.append('a Library holding carries one freshness token among its keywords: '
                            f"{', '.join(FRESHNESS)} (Library/Library.md, Rules)")
    return problems


def main(argv: list[str] | None = None) -> int:
    parser = vault.arguments((__doc__ or '').split('\n', 1)[0])
    parser.add_argument('files', nargs='*', type=pathlib.Path, help='notes to check (default: every note)')
    args = parser.parse_args(argv)
    root = args.root.resolve()
    report = vault.Report(root)
    if args.files:
        targets = []
        for name in args.files:
            path = (name if name.is_absolute() else root / name).resolve()
            if not path.is_file():
                print(f'{name}: no such file', file=sys.stderr)
                return 2
            if path.suffix == '.md' and vault.in_walk(root, path):
                targets.append(path)
        given = {(n if n.is_absolute() else root / n).resolve() for n in args.files}
        strays = [path for path in vault.stray_readmes(root) if path.resolve() in given]
    else:
        targets = list(vault.walk_notes(root))
        strays = vault.stray_readmes(root)
    for path in strays:
        report.error(path, 'a README.md belongs only in the seven top folders (AGENTS.md, Conventions); '
                           "describe this folder in its own note")
    for path in targets:
        for problem in check_note(root, path):
            report.error(path, problem)
    noun = 'note passes' if len(targets) == 1 else 'notes pass'
    return report.finish(f'{len(targets)} {noun}.')


if __name__ == '__main__':
    sys.exit(main())
