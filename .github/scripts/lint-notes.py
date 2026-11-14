#!/usr/bin/env python3
"""Check each note's frontmatter and naming against the vault's schema.

WHY THIS EXISTS. Every note in the vault opens with the account's hidden
frontmatter (.docs/technical/vault/Note-Schema.md): a title, a description and a type,
with keywords and a status where they say something. Retrieval, the catalog
and anyone who routes by a note's head read those fields, so a note that
drifts from the schema misleads every one of them, quietly. This is the
gate: run it on a note after an edit, and CI runs it on every note.

With no arguments it checks every note the vault walks: every folder but
hidden ones, plus the .template/ scaffolds, with each folder's README.md,
which is that folder's note. Given files, it checks only those. A file
outside the walk, such as one under .github/ or the README.md at the vault
root, is not a note and is skipped. So is a loose file waiting at the Inbox:
it becomes a note when it is sorted, with the frontmatter and the name it is
given then (Inbox/README.md). A folder explains itself in its
README.md alone, so a note named after its folder is flagged, and that
README.md is a page as well, so one without the page format's centered
header and footer is flagged too (Note-Schema.md).

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
# versions, which git replaces (the root README.md, Conventions).
RETIRED = frozenset({'tags', 'category', 'version'})
# The rest of the old two-band schema, each field now said by the path or git. A record or
# a template may still define one of these names as a field of its own kind.
RETIRED_UNLESS_OWN = frozenset({'aliases', 'created', 'updated', 'folder', 'layer', 'policy',
                                'author', 'path', 'id'})
# A Library holding's estimated lifespan, one token among its keywords (Library/README.md, Rules).
FRESHNESS = ('freshness/timeless', 'freshness/enduring', 'freshness/current')
# GitHub's five alerts, the only callouts a note uses (the root README.md, Conventions), each marker alone on its line.
ALERTS = ('NOTE', 'TIP', 'IMPORTANT', 'WARNING', 'CAUTION')
CALLOUT = re.compile(r'^[ \t]*(?:>[ \t]*)+\[!([^\]\n]*)\]([^\n]*)$', re.M)
# A folder's README.md is a page as well as its folder's note (Note-Schema.md), so it carries the
# account's page format: the centered header, its H1 and the top anchor, and the footer that links back.
MASTHEAD = re.compile(r'<div align="center">\s*\n\s*\n# [^\n]+\n\s*\n<a name="top"></a>')
BACK_TO_TOP = '[↑ Back to Top](#top)'
# Names the generators read. A tier sorts its session summaries by name and files each one in the
# archive by the year its name opens with, so a summary named any other way sorts after every
# digit: it reads as the newest at every start and never moves down (update-vault.py).
SUMMARY_FOLDERS = frozenset(folder for _name, _cap, folder in vault.TIERS)
SUMMARY_NAME = re.compile(r'^\d{8}-\d{6}(?:-\d+)?\.md$')
# The collections whose entries are listed in date order, which is name order: each README sets the form.
DATED_ENTRIES = {
    'Memory/Decisions': (re.compile(r'^\d{4}-\d{2}-'), 'YYYY-MM-slug.md'),
    'Memory/Insights': (re.compile(r'^\d{4}-\d{2}-'), 'YYYY-MM-slug.md'),
    'Memory/Events': (re.compile(r'^\d{4}-\d{2}-\d{2}-'), 'YYYY-MM-DD-slug.md'),
}
# What a scaffold leaves in a copy that was never finished (each .template/ README.md, How A Copy
# Is Made): the note that says how to copy it, a bracketed prompt where its own words belong, and
# the keyword that marks a scaffold. Left in, each one reaches the catalog as if it were content.
COPY_NOTE = re.compile(r'<!--\s*On copying:')
PLACEHOLDER = re.compile(r'\[[^\[\]\n]+\]')
# The Log's entries, the one body a generator reads (update-vault.py draws the Open Loops view from
# them): an entry's heading, its importance, and a line that reads as an open thread.
LOG_HEADING = re.compile(r'^### \d{4}-\d{2}-\d{2} - \S')
IMPORTANCE = re.compile(r'^\s*(?:[-*+]\s+)?(?:\*\*)?Importance:(?:\*\*)?\s*(.*?)\s*$')
STATUS_LIKE = re.compile(r'(?i)^\s*(?:[-*+]\s+)?[*_]{0,2}Status[*_]{0,2}\s*:\s*[*_]{0,2}\s*Open\b')
# A generated list links each entry by its name, and a wikilink reads # as a heading, | as an
# alias, ^ as a block and a bracket as its own end.
UNLINKABLE = re.compile(r'[#|\[\]^]')


def one_edit_apart(a: str, b: str) -> bool:
    """True when one slip of the hand turns a into b: a letter dropped, added or changed, or two
    neighbours swapped."""
    if a == b or abs(len(a) - len(b)) > 1:
        return False
    if len(a) == len(b):
        differ = [i for i in range(len(a)) if a[i] != b[i]]
        return len(differ) == 1 or (len(differ) == 2 and differ[1] == differ[0] + 1
                                    and a[differ[0]] == b[differ[1]] and a[differ[1]] == b[differ[0]])
    short, long = sorted((a, b), key=len)
    return any(long[:i] + long[i + 1:] == short for i in range(len(long)))


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
        meant = next((field for field in vault.FIELDS if one_edit_apart(key, field)), None)
        if meant and key not in vault.FIELDS:
            # A record may add fields of its own, so a slip here would pass as one: the note would
            # keep a status no script reads, or keywords the catalog never sees.
            problems.append(f"'{key}' reads as a slip for '{meant}', the field the scripts look for; correct the name")
        elif key in RETIRED or (key in RETIRED_UNLESS_OWN and kind not in vault.OWN_FIELDS):
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
    if not template:
        for field in ('title', 'description'):
            left = PLACEHOLDER.findall(str(fields.get(field, '') or ''))
            if left:
                problems.append(f"the {field} still holds a scaffold's prompt, {' '.join(left)}; give the copy its "
                                'own words (the .template/ README.md, How A Copy Is Made)')
        for word in vault.as_list(fields.get('keywords')):
            if PLACEHOLDER.search(word):
                problems.append(f"keyword '{word}' is a scaffold's prompt; replace it or drop it")
            elif word == 'template':
                problems.append("the keyword 'template' marks a scaffold; drop it from the copy")


def check_log(text: str) -> list[str]:
    """The problems with the Log's entries. update-vault.py lists an open thread only where it can
    read one, so a heading or a status line that is nearly right would drop a thread without a word."""
    problems = []
    for number, entry in vault.log_entries(text):
        if not LOG_HEADING.match(entry[0]):
            problems.append(f'line {number}: a Log entry is headed `### YYYY-MM-DD - Title`, the form the Open Loops '
                            f'view reads its date from (Memory/Log.md); this one reads `{entry[0].strip()}`')
        for offset, line in enumerate(entry[1:], 1):
            rated = IMPORTANCE.match(line)
            if rated and not re.fullmatch(r'[1-5]', rated.group(1)):
                problems.append(f'line {number + offset}: importance is one number from 1 to 5 (Memory/README.md, '
                                f'Operations); this line reads `{line.strip()}`')
            if STATUS_LIKE.match(line) and not vault.STATUS_OPEN.match(line):
                problems.append(f'line {number + offset}: an open thread is marked `**Status:** Open`, the one form '
                                f'the Open Loops view reads, so this one would be left out; it reads `{line.strip()}`')
    return problems


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
        problems.append('the note is empty, and a note is never emptied (the root README.md, Ask First); '
                        'restore it from git history or delete it')
    if '_' in path.name:
        problems.append('the file name has an underscore (the root README.md, Conventions); use spaces or hyphens')
    marks = sorted(set(UNLINKABLE.findall(path.name)))
    if marks:
        problems.append(f"the file name holds {' '.join(marks)}, which a wikilink cannot carry, so the list that "
                        'links this note would break (Link-Topology.md); rename it without')
    folder = '/'.join(parts[:-1])
    if path.name != vault.README:
        if folder in SUMMARY_FOLDERS and not SUMMARY_NAME.match(path.name):
            problems.append('a session summary is named YYYYMMDD-HHMMSS.md, the time it was filed: the tiers sort '
                            'by name, so this one would read as the newest at every start and never move down '
                            '(Memory/README.md, Session Summaries)')
        if folder in DATED_ENTRIES and not DATED_ENTRIES[folder][0].match(path.name):
            problems.append(f'an entry here is named {DATED_ENTRIES[folder][1]}, so the entries list in date order '
                            f'({folder}/README.md)')
    if vault.EM_DASH in text:
        problems.append(f'{text.count(vault.EM_DASH)} em dash(es) (the root README.md, Conventions); '
                        'use a comma, colon, parentheses or a hyphen')
    for kind, rest in CALLOUT.findall(vault.strip_code(text)):
        if kind not in ALERTS or rest.strip():
            problems.append(f'callout [!{kind}]{rest.rstrip()} does not render on GitHub (the root README.md, Conventions); use one of '
                            f"{', '.join(ALERTS)}, alone on its line, with any title as a bold first line")
    if template and '[[' in text:
        problems.append('a scaffold carries no wikilinks (Link-Topology.md)')
    if path.name == vault.README and text.strip() and (not MASTHEAD.search(text) or BACK_TO_TOP not in text):
        problems.append("a folder's README.md is a page: it opens with the centered header (its H1 and "
                        '<a name="top"></a> in a <div align="center">) and closes with the footer that links '
                        'back to it (Note-Schema.md)')
    if '/'.join(parts) == vault.LOG:
        problems.extend(check_log(text))
    if not template and COPY_NOTE.search(text):
        problems.append("the scaffold's `On copying:` note is still here; a copy follows that note and then "
                        'deletes it, so this one was never finished (the .template/ README.md, How A Copy Is Made)')
    fields = vault.parse_frontmatter(text)
    if fields is None:
        if text.strip():
            problems.append('no frontmatter block')
        return problems
    if vault.is_fenced(text):
        problems.append('the frontmatter is fenced with ---, which GitHub shows as a table; '
                        'wrap the fields in <!-- and --> (Note-Schema.md)')
        return problems
    check_fields(fields, template, problems)
    kind = str(fields.get('type', '') or '')
    if parts[0] == 'Library' and not template and kind not in ('index', 'record', 'template'):
        tokens = [w for w in vault.as_list(fields.get('keywords')) if w.startswith('freshness/')]
        if len(tokens) != 1 or tokens[0] not in FRESHNESS:
            problems.append('a Library holding carries one freshness token among its keywords: '
                            f"{', '.join(FRESHNESS)} (Library/README.md, Rules)")
    return problems


def main(argv: list[str] | None = None) -> int:
    parser = vault.arguments((__doc__ or '').split('\n', 1)[0])
    parser.add_argument('files', nargs='*', type=pathlib.Path, help='notes to check (default: every note)')
    args = parser.parse_args(argv)
    root = args.root.resolve()
    report = vault.Report(root)
    if args.files:
        targets = []
        waiting = set(vault.inbox_drops(root))
        for name in args.files:
            path = (name if name.is_absolute() else root / name).resolve()
            if not path.is_file():
                print(f'{name}: no such file', file=sys.stderr)
                return 2
            if path.suffix == '.md' and vault.in_walk(root, path) and path not in waiting:
                targets.append(path)
        given = {(n if n.is_absolute() else root / n).resolve() for n in args.files}
        strays = [path for path in vault.namesake_notes(root) if path.resolve() in given]
    else:
        targets = list(vault.filed_notes(root))
        strays = vault.namesake_notes(root)
    for path in strays:
        report.error(path, "a note named after its folder repeats the folder's README.md, which is the "
                           'folder\'s note (the root README.md, Conventions); move what it says into '
                           'README.md, then delete it')
    for path in targets:
        for problem in check_note(root, path):
            report.error(path, problem)
    noun = 'note passes' if len(targets) == 1 else 'notes pass'
    return report.finish(f'{len(targets)} {noun}.')


if __name__ == '__main__':
    sys.exit(main())
