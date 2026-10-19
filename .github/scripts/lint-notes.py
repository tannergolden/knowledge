#!/usr/bin/env python3
"""Check each note's frontmatter, tags and naming against the vault's schema.

WHY THIS EXISTS. Every note in the vault carries the same frontmatter
(.docs/vault/Note-Schema.md) and draws its tags from one closed vocabulary
(.docs/vault/Tag-Vocabulary.md). Retrieval, the catalog and the link graph all
read those fields, so a note that drifts from the schema misleads every one
of them, quietly. This is the gate: run it on one note after every edit,
and CI runs it on every note.

With no arguments it checks every note the vault walks: every folder but
hidden ones, plus the .template/ scaffolds. Given files, it checks only
those, and still catches one that reuses another note's id. A file outside
the walk, such as one under .github/, is not a note and is skipped.

Run it:

    python3 .github/scripts/lint-notes.py
    python3 .github/scripts/lint-notes.py "Memory/Log.md"
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import vault  # noqa: E402  (vault.py sits beside this file)

# Note types that are structure, not holdings, and so carry no freshness tag (Library/Library.md, Rules).
STRUCTURE_TYPES = frozenset({'index', 'information', 'template', 'log', 'record', 'agent'})


def is_summary(parts: tuple[str, ...]) -> bool:
    """A session summary moves between tiers, so its path field may lag where it sits."""
    return len(parts) > 1 and 'Memory' in parts and (parts[-2] in ('Current', 'Recent') or 'Archive' in parts)


def check_tags(fields: dict[str, object], problems: list[str]) -> None:
    tags = fields.get('tags')
    if not isinstance(tags, list):
        problems.append(f'tags is not a list (got {tags!r}); the tag vocabulary needs a tag array (Tag-Vocabulary.md)')
        return
    folder, kind = str(fields.get('folder', '')), str(fields.get('type', ''))
    for tag in tags:
        if tag not in vault.VOCABULARY:
            problems.append(f"tag '{tag}' is outside the closed vocabulary, which has no content tags (Tag-Vocabulary.md)")
    if folder and folder not in tags:
        problems.append(f"missing the Folder tag '{folder}' (Tag-Vocabulary.md)")
    if kind and kind not in tags:
        problems.append(f"missing the File Role tag '{kind}' (Tag-Vocabulary.md)")
    for label, family, most in (('Folder', vault.FOLDERS, 1), ('File Role', vault.TYPES, 1),
                                ('Freshness', vault.FRESHNESS_TAGS, 1)):
        count = sum(1 for tag in tags if tag in family)
        if count > most:
            problems.append(f'{count} {label} tags; the vocabulary allows one (Tag-Vocabulary.md)')
    if folder in tags and kind in tags:
        order = ([folder, kind] + [t for t in tags if t in vault.SIGNAL_TAGS]
                 + [t for t in tags if t in vault.SENSITIVITY_TAGS]
                 + [t for t in tags if t in vault.FRESHNESS_TAGS])
        if tags != order and not set(tags) - set(order):
            problems.append(f'tags are {tags}; the vocabulary orders them {order} (Tag-Vocabulary.md)')


def check_note(root: pathlib.Path, path: pathlib.Path) -> tuple[list[str], str]:
    """The problems with one note, and its id."""
    problems: list[str] = []
    try:
        text = vault.read_text(path)
    except OSError as error:
        return [f'cannot be read ({error})'], ''
    parts = path.relative_to(root).parts
    template = vault.is_template(parts)
    if not text.strip():
        problems.append('the note is empty, and a note is never emptied (AGENTS.md, Ask first); restore it from git history or delete it')
    if '_' in path.name:
        problems.append('the file name has an underscore (AGENTS.md, Conventions); use spaces or hyphens')
    if vault.EM_DASH in text:
        problems.append(f'{text.count(vault.EM_DASH)} em dash(es) (DOC-002); use a comma, colon, parentheses or a hyphen')
    fields = vault.parse_frontmatter(text)
    if fields is None:
        if text.strip():
            problems.append('no frontmatter block')
        return problems, ''
    for field in vault.REQUIRED_FIELDS:
        if field not in fields:
            problems.append(f'missing field: {field}')
    kind, folder, status = (str(fields.get(key, '') or '') for key in ('type', 'folder', 'status'))
    note_id = str(fields.get('id', '') or '')
    if kind and kind not in vault.TYPES:
        problems.append(f"type '{kind}' is not one of {sorted(vault.TYPES)}")
    if kind == 'template' and not template:
        problems.append("type 'template' outside a .template/ folder; give the copy its real type")
    if folder and folder not in vault.FOLDERS:
        problems.append(f"folder '{folder}' is not one of {sorted(vault.FOLDERS)}")
    if status and status not in vault.STATUSES:
        problems.append(f"status '{status}' is not one of {sorted(vault.STATUSES)}")
    if note_id and not vault.ID_RE.fullmatch(note_id):
        problems.append(f"id '{note_id}' must be lowercase, a two-letter folder prefix, then hyphenated words")
    if 'version' in fields:
        problems.append('per-file versions are retired; git history is the record, so remove the line')
    declared = str(fields.get('path', '') or '')
    expected = 'BRAIN/' + vault.rel(root, path)
    if declared and declared != expected and not template and not is_summary(parts):
        problems.append(f"path is '{declared}', expected '{expected}'")
    check_tags(fields, problems)
    policy = fields.get('policy')
    if policy is not None and str(policy).lower() not in ('true', 'false'):
        problems.append(f"policy must be true or false, got '{policy}'")
    for field in ('created', 'updated'):
        value = str(fields.get(field, '') or '')
        if value and not vault.DATE_RE.fullmatch(value):
            problems.append(f"{field} is '{value}'; the schema writes dates as YYYY-MM-DD (Note-Schema.md)")
    if template and '[[' in text:
        problems.append('a scaffold carries no wikilinks (Link-Topology.md)')
    tags = vault.as_list(fields.get('tags'))
    if (folder == 'library' and kind not in STRUCTURE_TYPES
            and not set(tags) & vault.FRESHNESS_TAGS and not template):
        problems.append('a Library holding needs a freshness tag: timeless, enduring or current (Library/Library.md, Rules)')
    return problems, note_id


def main(argv: list[str] | None = None) -> int:
    parser = vault.arguments((__doc__ or '').split('\n', 1)[0])
    parser.add_argument('files', nargs='*', type=pathlib.Path, help='notes to check (default: every note)')
    args = parser.parse_args(argv)
    root = args.root.resolve()
    report = vault.Report(root)
    every = list(vault.walk_notes(root))
    if args.files:
        targets = []
        for name in args.files:
            path = (name if name.is_absolute() else root / name).resolve()
            if not path.is_file():
                print(f'{name}: no such file', file=sys.stderr)
                return 2
            if path.suffix == '.md' and vault.in_walk(root, path):
                targets.append(path)
        strays = [path for path in vault.stray_readmes(root)
                  if path.resolve() in {(n if n.is_absolute() else root / n).resolve() for n in args.files}]
    else:
        targets = every
        strays = vault.stray_readmes(root)
    for path in strays:
        report.error(path, 'a README.md belongs only in the seven top folders (AGENTS.md, Conventions); '
                           "describe this folder in its own note")
    ids: dict[str, str] = {}
    checked = {path.resolve() for path in targets}
    for path in targets:
        problems, note_id = check_note(root, path)
        for problem in problems:
            report.error(path, problem)
        if note_id:
            if note_id in ids:
                report.error(path, f"id '{note_id}' is also {ids[note_id]}'s")
            else:
                ids[note_id] = vault.rel(root, path)
    if args.files:
        # A single note can still collide with one it was not given.
        for other in every:
            if other.resolve() in checked:
                continue
            other_id = str(vault.note_fields(other).get('id', '') or '')
            if other_id in ids:
                report.error(ids[other_id], f"id '{other_id}' is also {vault.rel(root, other)}'s")
    noun = 'note passes' if len(targets) == 1 else 'notes pass'
    return report.finish(f'{len(targets)} {noun}.')


if __name__ == '__main__':
    sys.exit(main())
