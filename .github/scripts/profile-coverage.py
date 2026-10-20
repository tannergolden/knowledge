#!/usr/bin/env python3
"""Score how filled in each Profile facet is, and name the one the identify skill should ask about next.

WHY THIS EXISTS. The identify skill fills the Profile by interviewing the
person about themselves, one facet at a time, and it needs to know which facet
is thinnest. This reads the twelve facets, counts the lines that say something
real about the person (not the scaffold's own prose, not a placeholder, not an
empty field), counts the proposals still marked unconfirmed, and ranks the
facets. The --json form is the contract the identify skill reads. It only
reads, and never writes.

A line counts as scaffold when its fingerprint is in the frozen table below,
taken from the blank facets, or in the live Profile/.template/ files. Refreeze
the table with --print-scaffold only on the blank template: run on a filled
Profile, it would publish checksums of personal lines.

Run it:

    python3 .github/scripts/profile-coverage.py
    python3 .github/scripts/profile-coverage.py --json
    python3 .github/scripts/profile-coverage.py "Working Style" --json
"""

from __future__ import annotations

import datetime
import json
import pathlib
import re
import sys
import unicodedata
import zlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import vault  # noqa: E402  (vault.py sits beside this file)

# The twelve facets in Profile.md's order. A flat facet is one file; a folder
# facet is its namesake plus one file per entry.
FACETS = (
    ('Working Style', 'flat'), ('Biography', 'flat'), ('Personality', 'flat'), ('Values', 'folder'),
    ('Goals', 'folder'), ('Relationships', 'flat'), ('Finances', 'flat'), ('Lifestyle', 'flat'),
    ('Skills', 'folder'), ('Preferences', 'flat'), ('Health', 'folder'), ('Focus', 'flat'),
)

HEADING = re.compile(r'^\s*#{1,6}\s')
H2 = re.compile(r'^\s*##\s+(.+?)\s*$')
COMMENT = re.compile(r'<!--[^>]*-->')
UNCONFIRMED = re.compile(r'<!--[^>]*\bunconfirmed\b[^>]*-->')
FIELD_STUB = re.compile(r'^\s*[-*]\s+\*\*[^:]+:\*\*\s*$')
FIELD_VALUE = re.compile(r'^\s*[-*]\s+\*\*[^:]+:\*\*\s*(.+?)\s*$')
TABLE_RULE = re.compile(r'^\s*\|[\s|:\-]*\|?\s*$')
BRACKETED = re.compile(r'^\[[^\]]+\]$')
BLOCK_START = re.compile(r'<!--\s*brain:profile-entries\b')
BLOCK_END = re.compile(r'<!--\s*/brain:profile-entries\s*-->')

# The frozen scaffold fingerprint: per facet file, the CRC32 of each normalized
# body line of the blank facet. Refreeze with --print-scaffold, on the blank template only.
SCAFFOLD = {
    'Working Style.md': frozenset({
        225209147, 442933976, 567785087, 872849886, 1473648760, 1528284317, 1639605086, 1763157381,
        1954678798, 2143291461, 2399925122, 2434787203, 2487941427, 2677263777, 2808827032,
        2832163386, 3017449629, 3083319045, 3357992108, 3402499179, 3837814167, 3964262313
    }),
    'Biography.md': frozenset({
        310840053, 354147002, 401978619, 453334733, 482937417, 519194785, 549516871, 658314844,
        762757395, 831918062, 941151755, 1029135874, 1051983102, 1139149987, 1171063423, 1242860332,
        1445288146, 1537616239, 1707618477, 2038284520, 2124765175, 2155206015, 2293530323,
        2328447477, 2352517808, 2467674828, 2527877439, 2690999041, 2701507878, 2821568757,
        3095903692, 3166980710, 3280337304, 3326179636, 3349361925, 3375409968, 3533523800,
        3557068584, 3707757044, 3965579265, 4267856163
    }),
    'Personality.md': frozenset({
        43106626, 172949556, 263251845, 385762225, 414789057, 453011166, 597959258, 766929257,
        787799655, 868917294, 940583144, 988814532, 1286581933, 1336166355, 1440537495, 1469418942,
        1502783263, 1574938528, 1660748535, 1718235761, 1769595493, 1918441090, 1947656589,
        1983469875, 2272899200, 2340378090, 2511452218, 2570411252, 2678175334, 2731067632,
        2774464729, 2881780122, 2908505410, 2972041163, 2994267298, 3164336382, 3329436946,
        3344212629, 3377343814, 3377466330, 3442278076, 3492840022, 3517038197, 3633935119,
        4094835117, 4106442123, 4147376602
    }),
    'Values/Values.md': frozenset({
        64571753, 133184907, 567585524, 849332693, 1100624917, 1242869265, 1393933323, 1541944181,
        1692748845, 1791513285, 1964396377, 2030850315, 2146954983, 2195606387, 2215321892,
        2460764168, 2470841111, 2536750863, 2547483114, 2970584590, 3447046022, 3863433903,
        4015021805, 4054868288, 4131442375, 4208915591, 4289391736
    }),
    'Goals/Goals.md': frozenset({
        537310124, 833632538, 1509716455, 1541944181, 1555809486, 3357936836
    }),
    'Relationships.md': frozenset({
        45720942, 400581226, 909950840, 1493176178, 1589068732, 3705302770, 3712249236, 4100675524
    }),
    'Finances.md': frozenset({
        158731507, 640776382, 1543356404, 1637126693, 2161504222, 3032485432, 3519053553,
        3622255849, 4162862514, 4165506174, 4215442947
    }),
    'Lifestyle.md': frozenset({
        347189939, 501402642, 818900200, 1442215377, 2008339254, 2452350216, 2590878688, 2728366794,
        3642232629, 3999570569
    }),
    'Skills/Skills.md': frozenset({
        1541944181, 1695391521, 2435509755, 2820437041, 3164114714, 3191792892, 3315365580,
        3669970215, 3697358632
    }),
    'Preferences.md': frozenset({
        124895376, 315944096, 322728521, 522087176, 693982146, 1053336049, 1066299920, 1242246075,
        1320195823, 1334221162, 1610036074, 1807862734, 2152556847, 2511509271, 2574557650,
        2869907037, 2874091983, 2874497879, 2881929483, 3280393706, 3634789523, 3859953358,
        4140291926
    }),
    'Health/Health.md': frozenset({
        134704662, 248177932, 1423946993, 1541944181, 2750784822, 2970566443, 3376311458
    }),
    'Focus.md': frozenset({
        904439264, 949487940, 1041995441, 1104286287, 1112599439, 1848870927, 2495542468,
        2659992988, 2887700068, 3278924594, 4067029393, 4086500816
    }),
}


def fingerprint(line: str) -> int:
    """A line's fingerprint: stripped, inner whitespace collapsed, NFC, then CRC32 of the UTF-8."""
    return zlib.crc32(unicodedata.normalize('NFC', re.sub(r'\s+', ' ', line.strip())).encode('utf-8'))


def body(text: str) -> str:
    return text[vault.body_start(text):]


def scaffold_lines(text: str) -> set[int]:
    """The fingerprints of a file's body lines that could be scaffold: not blank, not a heading."""
    out = set()
    for raw in body(text).splitlines():
        if not raw.strip() or HEADING.match(raw):
            continue
        line = COMMENT.sub('', raw)
        if line.strip():
            out.add(fingerprint(line))
    return out


def template_lines(root: pathlib.Path) -> frozenset[int]:
    """The live Profile/.template/ bodies, so a freshly copied entry scores empty until it is filled."""
    out: set[int] = set()
    folder = root / 'Profile' / '.template'
    if folder.is_dir():
        for path in sorted(folder.glob('*.md')):
            try:
                out |= scaffold_lines(vault.read_text(path))
            except OSError:
                continue
    return frozenset(out)


def placeholder(line: str, scaffold: frozenset[int]) -> bool:
    """A line that holds no real content: scaffold prose, an empty field, a bare parenthetical,
    a table rule, the generated block's empty line, or one bracketed token."""
    stripped = line.strip()
    if fingerprint(line) in scaffold or FIELD_STUB.match(line) or TABLE_RULE.match(line):
        return True
    value = FIELD_VALUE.match(line)
    if value and (re.fullmatch(r'\(.*\)', value.group(1)) or value.group(1).endswith(' -')):
        return True
    return stripped == '_None recorded yet._' or bool(BRACKETED.match(stripped))


def score(path: pathlib.Path, scaffold: frozenset[int]) -> dict[str, object] | None:
    """One file's substantive and unconfirmed lines, overall and per ## section."""
    try:
        text = vault.read_text(path)
    except OSError:
        return None
    substantive = unconfirmed = 0
    sections: list[dict[str, object]] = []
    section: dict[str, object] | None = None
    in_block = False
    for raw in body(text).splitlines():
        if BLOCK_START.search(raw):
            in_block = True
            continue
        if BLOCK_END.search(raw):
            in_block = False
            continue
        if not raw.strip():
            continue
        if HEADING.match(raw):
            h2 = H2.match(raw)
            if h2:
                section = {'heading': h2.group(1), 'substantive': 0, 'unconfirmed': 0}
                sections.append(section)
            continue
        pending = len(UNCONFIRMED.findall(raw))
        line = COMMENT.sub('', raw)
        if pending:
            unconfirmed += pending
            if section is not None:
                section['unconfirmed'] = int(section['unconfirmed']) + pending
        if in_block or not line.strip() or placeholder(line, scaffold):
            continue
        substantive += 1
        if section is not None:
            section['substantive'] = int(section['substantive']) + 1
    for each in sections:
        each['filled'] = int(each['substantive']) > 0
    return {'substantive': substantive, 'unconfirmed': unconfirmed, 'sections': sections}


def coverage(root: pathlib.Path) -> tuple[list[dict[str, object]], str]:
    """Every facet scored and ranked, thinnest first, and the facet to ask about next."""
    live = template_lines(root)
    facets = []
    for name, kind in FACETS:
        key = f'{name}.md' if kind == 'flat' else f'{name}/{name}.md'
        path = root / 'Profile' / key
        scaffold = frozenset(SCAFFOLD.get(key, frozenset()) | live)
        files = substantive = unconfirmed = 0
        sections: list[dict[str, object]] = []
        entries: list[dict[str, object]] = []
        result = score(path, scaffold) if path.is_file() else None
        missing = result is None
        if result is not None:
            files += 1
            substantive += int(result['substantive'])
            unconfirmed += int(result['unconfirmed'])
            sections = list(result['sections'])  # type: ignore[arg-type]
        if kind == 'folder' and (root / 'Profile' / name).is_dir():
            for entry in sorted((root / 'Profile' / name).glob('*.md')):
                if entry.name == f'{name}.md' or entry.name.startswith('.'):
                    continue
                scored = score(entry, scaffold) or {'substantive': 0, 'unconfirmed': 0}
                files += 1
                entries.append({'name': entry.name, 'substantive': scored['substantive'],
                                'unconfirmed': scored['unconfirmed'],
                                'depth': int(scored['substantive']) - int(scored['unconfirmed'])})
                substantive += int(scored['substantive'])
                unconfirmed += int(scored['unconfirmed'])
        depth = substantive - unconfirmed
        status = ('template' if substantive == 0 else 'sparse' if depth < 10
                  else 'partial' if depth < 30 else 'developed')
        facets.append({'facet': name, 'kind': kind, 'path': f'Profile/{key}', 'files': files,
                       'entries': len(entries), 'substantive': substantive, 'unconfirmed': unconfirmed,
                       'depth': depth, 'status': status, 'missing': missing, 'sections': sections,
                       'entry_files': entries})
    order = {f['facet']: i for i, f in enumerate(facets)}
    ranked = sorted(facets, key=lambda f: (f['depth'], f['substantive'], -int(f['unconfirmed']), order[f['facet']]))
    for rank, facet in enumerate(ranked, 1):
        facet['rank'] = rank
    working_style = next(f for f in facets if f['facet'] == 'Working Style')
    # Working Style leads while it is still the blank scaffold: the least invasive, most useful first interview.
    target = 'Working Style' if working_style['status'] == 'template' else str(ranked[0]['facet'])
    return facets, target


def row(facet: dict[str, object]) -> dict[str, object]:
    out = {key: facet[key] for key in ('facet', 'kind', 'path', 'files', 'entries', 'substantive',
                                       'unconfirmed', 'depth', 'status', 'rank')}
    if facet['missing']:
        out['missing'] = True
    return out


def table(facets: list[dict[str, object]]) -> None:
    print(f"{'Rank':>4}  {'Facet':<14}  {'Kind':<6}  {'Files':>5}  {'Entries':>7}  {'Subst':>5}  {'Unconf':>6}  "
          f"{'Depth':>5}  Status")
    for f in sorted(facets, key=lambda x: int(x['rank'])):
        print(f"{f['rank']:>4}  {f['facet']:<14}  {f['kind']:<6}  {f['files']:>5}  {f['entries']:>7}  "
              f"{f['substantive']:>5}  {f['unconfirmed']:>6}  {f['depth']:>5}  {f['status']}")


def print_scaffold(root: pathlib.Path) -> None:
    print('SCAFFOLD = {')
    for name, kind in FACETS:
        key = f'{name}.md' if kind == 'flat' else f'{name}/{name}.md'
        path = root / 'Profile' / key
        hashes = sorted(scaffold_lines(vault.read_text(path))) if path.is_file() else []
        print(f"    '{key}': frozenset({{")
        line = '       '
        for i, value in enumerate(hashes):
            token = f' {value}' + (',' if i < len(hashes) - 1 else '')
            if len(line) + len(token) > 100:
                print(line)
                line = '       '
            line += token
        print(line)
        print('    }),')
    print('}')


def main(argv: list[str] | None = None) -> int:
    parser = vault.arguments((__doc__ or '').split('\n', 1)[0])
    parser.add_argument('facet', nargs='*', help='one facet to report in detail, such as "Working Style"')
    parser.add_argument('--json', action='store_true', help='print the JSON the identify skill reads')
    parser.add_argument('--print-scaffold', action='store_true',
                        help='print a fresh scaffold table from the facets (on the blank template only)')
    args = parser.parse_args(argv)
    root = args.root.resolve()
    if args.print_scaffold:
        print_scaffold(root)
        return 0
    facets, target = coverage(root)
    rule = target == 'Working Style' and next(f for f in facets if f['facet'] == 'Working Style')['status'] == 'template'
    wanted = re.sub(r'\s+', ' ', ' '.join(args.facet).replace('-', ' ').strip().lower())
    if wanted:
        hit = next((f for f in facets if str(f['facet']).lower() == wanted), None)
        if hit is None:
            print(f"no facet named '{' '.join(args.facet)}'; the facets are "
                  f"{', '.join(name for name, _kind in FACETS)}", file=sys.stderr)
            return 2
        if args.json:
            out = row(hit)
            out['sections'] = hit['sections']
            out['entry_files'] = hit['entry_files']
            print(json.dumps(out, indent=2))
            return 0
        if hit['missing']:
            print(f"warning: {hit['path']} is missing, so it scores zero")
        table([hit])
        for section in hit['sections']:  # type: ignore[union-attr]
            print(f"  {section['heading']}: {section['substantive']} substantive, {section['unconfirmed']} "
                  f"unconfirmed, {'filled' if section['filled'] else 'not filled'}")
        for entry in hit['entry_files']:  # type: ignore[union-attr]
            print(f"  entry {entry['name']}: {entry['substantive']} substantive, {entry['unconfirmed']} "
                  f"unconfirmed, depth {entry['depth']}")
        return 0
    if args.json:
        print(json.dumps({'generated': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d'),
                          'target': target, 'facets': [row(f) for f in facets]}, indent=2))
        return 0
    for facet in facets:
        if facet['missing']:
            print(f"warning: {facet['path']} is missing, so it scores zero")
    table(facets)
    print(f"Target: {target}" + ('  (Working Style leads while it is still the scaffold)' if rule else ''))
    return 0


if __name__ == '__main__':
    sys.exit(main())
