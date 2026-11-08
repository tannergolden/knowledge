#!/usr/bin/env python3
"""Score how filled in each Profile facet is, and name the one the profile interview should ask about next.

WHY THIS EXISTS. The profile interview, which the human-resources skill runs,
fills the Profile by asking the person about themselves, one facet at a time,
and it needs to know which facet is thinnest. This reads the twelve facets,
counts the lines that say something real about the person (not the scaffold's
own prose, not a placeholder, not an empty field), counts the proposals still
marked unconfirmed, and ranks the facets. The --json form is the contract the
human-resources skill reads. It only reads, and never writes.

A line counts as scaffold when its fingerprint is in the frozen table below,
taken from the blank facets, or in the live Profile/.template/ files. Refreeze
the table with --print-scaffold only on the blank template: run on a filled
Profile, it would publish checksums of personal lines. A refreeze keeps every
fingerprint the table already holds and adds the blank facets' current lines,
because the flat facets are each vault's own and never synced: a vault whose
blank facet still holds an older scaffold's line keeps scoring it as scaffold.

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

# The twelve facets in Profile/README.md's order. A flat facet is one file; a
# folder facet is its README.md plus one file per entry.
FACETS = (
    ('Working Style', 'flat'), ('Biography', 'flat'), ('Personality', 'flat'), ('Values', 'folder'),
    ('Goals', 'folder'), ('Relationships', 'flat'), ('Finances', 'flat'), ('Lifestyle', 'flat'),
    ('Skills', 'folder'), ('Preferences', 'flat'), ('Health', 'folder'), ('Focus', 'flat'),
)

HEADING = re.compile(r'^\s*#{1,6}\s')
H2 = re.compile(r'^\s*##\s+(.+?)\s*$')
# A folder facet's README.md is a page (Note-Schema.md): each section heading opens with an emoji,
# which a section's name in the report leaves out, and its opening section says what the folder is
# for, which holds no fact about the owner, so it is never scored or asked about.
EMOJI = re.compile(r'^[^\w\s(\[]+\s*')
ABOUT = frozenset({'What This Folder Is For'})
COMMENT = re.compile(r'<!--[^>]*-->')
UNCONFIRMED = re.compile(r'<!--[^>]*\bunconfirmed\b[^>]*-->')
FIELD_STUB = re.compile(r'^\s*[-*]\s+\*\*[^:]+:\*\*\s*$')
FIELD_VALUE = re.compile(r'^\s*[-*]\s+\*\*[^:]+:\*\*\s*(.+?)\s*$')
TABLE_RULE = re.compile(r'^\s*\|[\s|:\-]*\|?\s*$')
BRACKETED = re.compile(r'^\[[^\]]+\]$')
BLOCK_START = re.compile(r'<!--\s*brain:profile-entries\b')
BLOCK_END = re.compile(r'<!--\s*/brain:profile-entries\s*-->')

# The frozen scaffold fingerprint: per facet file, the CRC32 of each normalized
# body line of the blank facet, in this release and the ones before it. Refreeze
# with --print-scaffold, on the blank template only.
SCAFFOLD = {
    'Working Style.md': frozenset({
        225209147, 442933976, 548755893, 567785087, 872849886, 1320592178, 1473648760, 1507654220,
        1528284317, 1639605086, 1763157381, 1954678798, 1990592902, 2143291461, 2351806529,
        2399925122, 2434787203, 2487941427, 2677263777, 2808827032, 2832163386, 3017449629,
        3083319045, 3357992108, 3402499179, 3837814167, 3935893116, 3943732477, 3964262313,
        4015858581
    }),
    'Biography.md': frozenset({
        249768181, 310840053, 354147002, 401978619, 453334733, 482937417, 519194785, 549516871,
        658314844, 685211297, 762757395, 775385252, 831918062, 926591936, 941151755, 1029135874,
        1051983102, 1139149987, 1171063423, 1242860332, 1445288146, 1537616239, 1707618477,
        1935698839, 2038284520, 2089378971, 2124765175, 2155206015, 2293530323, 2297704327,
        2323602823, 2328447477, 2352517808, 2467674828, 2527877439, 2690999041, 2698396655,
        2701507878, 2821568757, 2893001682, 2944849416, 3095903692, 3166980710, 3280337304,
        3326179636, 3349361925, 3375409968, 3533523800, 3557068584, 3632022837, 3707757044,
        3965579265, 4117528051, 4267856163
    }),
    'Personality.md': frozenset({
        43106626, 172949556, 263251845, 385762225, 414789057, 453011166, 597959258, 718861257,
        764357537, 766929257, 787799655, 868917294, 931882618, 940583144, 972310397, 988814532,
        1286581933, 1336166355, 1356839883, 1438837970, 1440537495, 1469418942, 1477117266,
        1502783263, 1574938528, 1660748535, 1718235761, 1769595493, 1779503197, 1847685552,
        1918441090, 1947656589, 1983469875, 2272899200, 2340378090, 2511452218, 2570411252,
        2678175334, 2731052230, 2731067632, 2774464729, 2881780122, 2908505410, 2972041163,
        2982020050, 2994267298, 3164336382, 3228439105, 3329436946, 3344212629, 3377343814,
        3377466330, 3442278076, 3492840022, 3517038197, 3614768266, 3633935119, 4094835117,
        4106442123, 4117649750, 4124503548, 4147376602
    }),
    'Values/README.md': frozenset({
        64571753, 126044342, 133184907, 144034127, 193874281, 209117326, 567585524, 745447918,
        849332693, 860163393, 968711492, 1100624917, 1210420169, 1242869265, 1354489659, 1393933323,
        1419137375, 1513730738, 1541944181, 1692748845, 1770499243, 1791513285, 1842859433,
        1964396377, 1980950795, 2030850315, 2053164607, 2146954983, 2195606387, 2215321892,
        2328996219, 2460764168, 2470841111, 2518387491, 2527713059, 2536750863, 2547483114,
        2619580341, 2848029190, 2854292027, 2916704654, 2970584590, 3040386114, 3400371584,
        3447046022, 3863433903, 4015021805, 4054868288, 4131442375, 4192891031, 4195196696,
        4208915591, 4289391736
    }),
    'Goals/README.md': frozenset({
        22761007, 74663413, 193874281, 329954006, 537310124, 745447918, 833632538, 1354489659,
        1509716455, 1541944181, 1555809486, 1726050361, 2144247977, 2518387491, 2742862132,
        2854292027, 3173850250, 3357936836, 3400371584, 4192891031, 4246501810
    }),
    'Relationships.md': frozenset({
        45720942, 205762334, 400581226, 909950840, 1098543220, 1493176178, 1589068732, 1598304787,
        1868085603, 2330930919, 2381618827, 2708366302, 2786653605, 2834508921, 3517747445,
        3705302770, 3712249236, 4100675524
    }),
    'Finances.md': frozenset({
        92225503, 158731507, 640776382, 1383392617, 1543356404, 1637126693, 2161504222, 2451098709,
        2581540218, 2823334144, 3025783623, 3032485432, 3519053553, 3622255849, 4162862514,
        4165506174, 4215442947
    }),
    'Lifestyle.md': frozenset({
        251181226, 326667407, 333009999, 347189939, 501402642, 735756371, 818900200, 927845150,
        1192851427, 1442215377, 1820033771, 2008339254, 2452350216, 2590878688, 2727397193,
        2728366794, 3548305967, 3642232629, 3652943350, 3867517956, 3999570569
    }),
    'Skills/README.md': frozenset({
        55426573, 193874281, 745447918, 1256340403, 1354489659, 1495859745, 1541944181, 1545437221,
        1695391521, 1861054185, 2268847954, 2435509755, 2518387491, 2565699907, 2820437041,
        2854292027, 3164114714, 3191792892, 3315365580, 3400371584, 3669970215, 3697358632,
        4192891031
    }),
    'Preferences.md': frozenset({
        124895376, 315944096, 322728521, 445245874, 522087176, 658137327, 693982146, 705033735,
        1047176323, 1053336049, 1066299920, 1242246075, 1320195823, 1334221162, 1610036074,
        1807862734, 1906574449, 1933927458, 2152556847, 2442169554, 2511509271, 2517046073,
        2574557650, 2869907037, 2874091983, 2874497879, 2881929483, 3280393706, 3634789523,
        3785487452, 3806365873, 3859953358, 4140291926
    }),
    'Health/README.md': frozenset({
        134704662, 193874281, 248177932, 556539478, 745447918, 1354489659, 1423946993, 1541944181,
        2262221187, 2518387491, 2748034427, 2750784822, 2854292027, 2970566443, 3002567387,
        3107348501, 3374826145, 3376311458, 3400371584, 3801061885, 4192891031
    }),
    'Focus.md': frozenset({
        220222445, 904439264, 949487940, 1041995441, 1104286287, 1112599439, 1679408761, 1737140127,
        1848870927, 2495542468, 2659992988, 2887700068, 2956903128, 3278924594, 3525233028,
        3866080260, 3903848953, 4067029393, 4086500816, 4132993285
    }),
}


def facet_key(name: str, kind: str) -> str:
    """A facet's file under Profile/: the flat file itself, or a folder facet's README.md."""
    return f'{name}.md' if kind == 'flat' else f'{name}/{vault.README}'


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
    """The live Profile/.template/ bodies, so a freshly copied entry scores empty until it is filled.
    The folder's README.md explains the scaffolds and is never copied, so it is not one of them."""
    out: set[int] = set()
    folder = root / 'Profile' / '.template'
    if folder.is_dir():
        for path in sorted(folder.glob('*.md')):
            if vault.is_folder_note(path):
                continue
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
    in_block = about = False
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
                name = EMOJI.sub('', h2.group(1))
                about = name in ABOUT
                section = None if about else {'heading': name, 'substantive': 0, 'unconfirmed': 0}
                if section is not None:
                    sections.append(section)
            continue
        if about:
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
        key = facet_key(name, kind)
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
        if kind == 'folder':
            for entry in vault.entry_files(root / 'Profile' / name):
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
        key = facet_key(name, kind)
        path = root / 'Profile' / key
        current = scaffold_lines(vault.read_text(path)) if path.is_file() else set()
        hashes = sorted(set(SCAFFOLD.get(key, frozenset())) | current)
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
    parser.add_argument('--json', action='store_true', help='print the JSON the human-resources skill reads')
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
