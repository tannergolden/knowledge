#!/usr/bin/env python3
"""Check the agent library: each agent spec, each team roster, and names unique across every home.

WHY THIS EXISTS. The vault's agents live in three homes, the Agent Resources
(AR) workforce, the Faculties and the Library, which make one library with one
namespace: an agent is addressed by its spoken name, so two agents sharing a
name or a role would misroute a request. A skill dispatches a team by its
roster, so a roster that names a missing agent dispatches into nothing. And a
team lead orchestrates and never does the labor itself, so its tools are fixed.
This holds every spec to the agent standard, every roster to its team, and the
whole library to one namespace.

With no arguments it checks the whole library; given names (a role, a file
name or a spoken name), it checks just those agents.

Run it:

    python3 .github/scripts/check-agents.py
    python3 .github/scripts/check-agents.py Beatrice
"""

from __future__ import annotations

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import vault  # noqa: E402  (vault.py sits beside this file)

SECTIONS = ('Identity', 'Role & Objective', 'Inputs', 'Method', 'Output contract',
            'Examples', 'Boundaries', 'Recovery', 'Non-negotiables')
LEAD_TOOLS = frozenset({'Read', 'Grep', 'Glob', 'Task'})
# The Library's lead stewards its own collection, so it holds the labor tools itself.
LIBRARIAN_TOOLS = frozenset({'Read', 'Grep', 'Glob', 'Write', 'Edit', 'Bash', 'Task'})
LIBRARIAN = vault.STAR + ' Librarian'


def tools(fields: dict[str, object]) -> set[str]:
    return {tool.strip() for tool in str(fields.get('tools', '') or '').split(',') if tool.strip()}


def role(path: pathlib.Path, fields: dict[str, object]) -> str:
    return str(fields.get('title', '') or '').strip() or path.stem


def check_agent(root: pathlib.Path, path: pathlib.Path, fields: dict[str, object], report: vault.Report) -> None:
    text = vault.read_text(path)
    title = str(fields.get('title', '') or '').strip()
    if not title:
        report.error(path, 'the frontmatter has no title (the role)')
    elif title != path.stem:
        report.error(path, f"title '{title}' differs from the file name, {path.stem}")
    if not str(fields.get('name', '') or '').strip():
        report.error(path, 'the frontmatter has no name (the spoken name)')
    if not str(fields.get('description', '') or '').strip():
        report.error(path, 'the frontmatter has no description (the routing key)')
    for section in SECTIONS:
        if not re.search(r'(?im)^#{1,6}\s+' + re.escape(section) + r'\b', text):
            report.error(path, f'no ## {section} section')
    if re.search(r'(?im)^#{1,6}\s+Identity\b', text):
        for line in ('Name', 'Persona', 'Voice'):
            if not re.search(rf'(?im)^\s*[-*]\s*\*\*{line}', text):
                report.warn(path, f'the Identity block has no **{line}:** line')
    held = tools(fields)
    shown = ', '.join(sorted(held)) or 'none'
    if path.stem.startswith(vault.STAR):
        if role(path, fields) == LIBRARIAN and path.parent == root / 'Library':
            if held != LIBRARIAN_TOOLS:
                report.error(path, f'the Librarian holds exactly {", ".join(sorted(LIBRARIAN_TOOLS))}; found {shown}')
        elif held != LEAD_TOOLS:
            report.error(path, f'a lead holds exactly {", ".join(sorted(LEAD_TOOLS))} (leads orchestrate, they do '
                               f'not labor); found {shown}')
    elif held & {'Write', 'Edit'}:
        report.error(path, f'an agent that is not a lead holds neither Write nor Edit; found {shown}')
    if vault.EM_DASH in text:
        report.error(path, 'em dash (DOC-002); use a comma, colon, parentheses or a hyphen')


def check_roster(path: pathlib.Path, fields: dict[str, object], roles: set[str], report: vault.Report) -> None:
    for key in ('title', 'description', 'lead'):
        if not str(fields.get(key, '') or '').strip():
            report.error(path, f'the frontmatter has no {key}')
    names = vault.members(fields)
    lead = str(fields.get('lead', '') or '').strip()
    if not names:
        report.error(path, 'members is missing or empty')
    if lead and names and lead not in names:
        report.error(path, f"the lead, '{lead}', is not one of the members")
    if lead and not lead.startswith(vault.STAR + ' '):
        report.error(path, f"the lead, '{lead}', does not start with the star and a space")
    starred = [name for name in names if name.startswith(vault.STAR)]
    if names and len(starred) != 1:
        report.error(path, f'a roster stars exactly one member, its lead; found {len(starred)}')
    for name in names:
        if name not in roles:
            report.error(path, f"member '{name}' is no agent's title in any home")
    if vault.EM_DASH in vault.read_text(path):
        report.error(path, 'em dash (DOC-002); use a comma, colon, parentheses or a hyphen')


def main(argv: list[str] | None = None) -> int:
    parser = vault.arguments((__doc__ or '').split('\n', 1)[0])
    parser.add_argument('names', nargs='*', help='agents to check, by role, file name or spoken name')
    args = parser.parse_args(argv)
    root = args.root.resolve()
    report = vault.Report(root)
    homes = vault.homes(root)
    agents = [(path, team, home, vault.note_fields(path))
              for home in homes for path, team in vault.agent_files(home)]
    if args.names:
        chosen = []
        for wanted in args.names:
            match = next((a for a in agents if wanted in (role(a[0], a[3]), a[0].stem)
                          or str(a[3].get('name', '') or '').strip().lower() == wanted.lower()), None)
            if match is None:
                print(f'no agent named {wanted} in any home', file=sys.stderr)
                return 2
            chosen.append(match)
        for path, _team, _home, fields in chosen:
            check_agent(root, path, fields, report)
        noun = 'agent passes' if len(chosen) == 1 else 'agents pass'
        return report.finish(f'{len(chosen)} {noun}.')
    for path, _team, _home, fields in agents:
        check_agent(root, path, fields, report)
    roles = {role(path, fields) for path, _t, _h, fields in agents}
    rosters: dict[tuple[pathlib.Path, str], tuple[pathlib.Path, dict[str, object]]] = {}
    for home in homes:
        for path, team in vault.roster_files(home):
            fields = vault.note_fields(path)
            rosters[(home, team)] = (path, fields)
            check_roster(path, fields, roles, report)
    for path, team, home, fields in agents:
        entry = rosters.get((home, team))
        own = role(path, fields)
        if path.stem.startswith(vault.STAR):
            if entry is None:
                report.error(path, f"a starred agent's team, {team}, has no roster naming it lead")
            elif str(entry[1].get('lead', '') or '').strip() != own:
                report.error(path, f'a starred agent is its roster\'s lead, but {vault.rel(root, entry[0])} '
                                   f"names '{entry[1].get('lead', '')}'")
        if entry is not None and own not in vault.members(entry[1]):
            report.error(path, f"'{own}' is not one of {vault.rel(root, entry[0])}'s members")
    by_role: dict[str, list[str]] = {}
    by_name: dict[str, list[str]] = {}
    for path, _team, _home, fields in agents:
        by_role.setdefault(role(path, fields), []).append(vault.rel(root, path))
        spoken = str(fields.get('name', '') or '').strip()
        if spoken:
            by_name.setdefault(spoken.lower(), []).append(vault.rel(root, path))
    for label, table in (('role', by_role), ('spoken name', by_name)):
        for key, paths in sorted(table.items()):
            if len(paths) > 1:
                report.error(paths[0], f"the {label} '{key}' is also used by {', '.join(paths[1:])}")
    return report.finish(f'{len(agents)} agents and {len(rosters)} rosters pass across {len(homes)} homes.')


if __name__ == '__main__':
    sys.exit(main())
