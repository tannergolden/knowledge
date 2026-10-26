#!/usr/bin/env python3
"""Check the agent library: each agent spec, each team roster, and names unique across every home.

WHY THIS EXISTS. The vault's agents live in three homes, the Agent Resources
(AR) workforce, the Faculties, each kept in the agents/ folder of the skill
that dispatches it, and the Library, which make one library with one
namespace: an agent is addressed by its spoken name, so two agents sharing a
name or a role would misroute a request. A skill dispatches a team by its
folder: the specs in it are the members, and the starred one leads, so a team
needs exactly one star. And a team lead orchestrates and never does the labor
itself, so its tools are fixed. This holds every spec to the agent standard,
every team to one lead, and the whole library to one namespace.

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


def role(path: pathlib.Path) -> str:
    """An agent's role is its file name."""
    return path.stem


def check_agent(root: pathlib.Path, path: pathlib.Path, fields: dict[str, object], report: vault.Report) -> None:
    text = vault.read_text(path)
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
        if role(path) == LIBRARIAN and path.parent == root / 'Library':
            if held != LIBRARIAN_TOOLS:
                report.error(path, f'the Librarian holds exactly {", ".join(sorted(LIBRARIAN_TOOLS))}; found {shown}')
        elif held != LEAD_TOOLS:
            report.error(path, f'a lead holds exactly {", ".join(sorted(LEAD_TOOLS))} (leads orchestrate, they do '
                               f'not labor); found {shown}')
    elif held & {'Write', 'Edit'}:
        report.error(path, f'an agent that is not a lead holds neither Write nor Edit; found {shown}')
    if vault.EM_DASH in text:
        report.error(path, 'em dash (DOC-002); use a comma, colon, parentheses or a hyphen')


def check_roster(path: pathlib.Path, fields: dict[str, object], report: vault.Report) -> None:
    for key in ('title', 'description'):
        if not str(fields.get(key, '') or '').strip():
            report.error(path, f'the frontmatter has no {key}')
    names = vault.members(path.parent)
    starred = [name for name in names if name.startswith(vault.STAR)]
    if len(starred) != 1:
        report.error(path, f'a team stars exactly one member, its lead; found {len(starred)}')
    for name in starred:
        if not name.startswith(vault.STAR + ' '):
            report.error(path, f"the lead, '{name}', does not start with the star and a space")
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
            match = next((a for a in agents if wanted == role(a[0])
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
    rosters: dict[tuple[pathlib.Path, str], pathlib.Path] = {}
    for home in homes:
        for path, team in vault.roster_files(home):
            rosters[(home, team)] = path
            check_roster(path, vault.note_fields(path), report)
    for home in homes:
        for team in vault.team_dirs(home):
            if not vault.members(team) or (home, vault.team_name(team)) in rosters:
                continue
            if team.name == vault.TEAM_FOLDER:
                found = len(vault.team_rosters(team))
                report.error(team, f'a skill keeps its team in {vault.TEAM_FOLDER}/ with exactly one roster, '
                                   f'the note named for the team; found {found}')
            else:
                report.error(team, f'the team {team.name} has no note of its own, {team.name}.md, to describe it')
    by_role: dict[str, list[str]] = {}
    by_name: dict[str, list[str]] = {}
    for path, _team, _home, fields in agents:
        by_role.setdefault(role(path), []).append(vault.rel(root, path))
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
