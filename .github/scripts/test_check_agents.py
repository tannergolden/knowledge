#!/usr/bin/env python3
"""Tests for check-agents.py, the agent library check.

WHY THIS EXISTS. An agent is addressed by its spoken name and a team is
dispatched by its folder, so a duplicate name, a team with no lead or two,
or a lead holding labor tools breaks dispatch quietly. Each test builds
a small library in a throwaway vault, breaks one rule, and runs the real
script; the last runs it, read only, on the library this repository holds.

Run it:

    python3 .github/scripts/test_check_agents.py
"""

from __future__ import annotations

import pathlib
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fixtures  # noqa: E402

SCRIPT = 'check-agents.py'
STAR = '★'
LEAD = f'{STAR} Research Lead'
TEAM = '.agents/skills/research/agents'
SECTIONS = ('Identity', 'Role & Objective', 'Inputs', 'Method', 'Output contract', 'Examples', 'Boundaries',
            'Recovery', 'Non-negotiables')


def spec(title: str) -> str:
    body = [f'# {title}', '', '## Identity', '', '- **Name:** x', '- **Persona:** x', '- **Voice:** x', '']
    for section in SECTIONS[1:]:
        body += [f'## {section}', '', 'x', '']
    return '\n'.join(body)


class TestCheckAgents(unittest.TestCase):
    def setUp(self) -> None:
        self.vault = fixtures.Vault()
        self.roster()
        self.agent(LEAD, name='Beatrice', tools='Read, Grep, Glob, Task')
        self.agent('Fact-Checker', name='Felix', tools='Read, Grep, Glob, WebSearch')

    def tearDown(self) -> None:
        self.vault.cleanup()

    def roster(self, **fields: object) -> None:
        self.vault.note(f'{TEAM}/Research.md', **fields)

    def agent(self, role: str, folder: str = TEAM, body: str | None = None, **fields: object) -> None:
        self.vault.agent(f'{folder}/{role}.md', body=body if body is not None else spec(role), **fields)

    def assert_flags(self, needle: str) -> None:
        result = self.vault.run(SCRIPT)
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn(needle, result.stdout)

    def test_a_valid_library_passes(self) -> None:
        result = self.vault.run(SCRIPT)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn('2 agents and 1 rosters pass across 1 homes.', result.stdout)

    def test_a_spoken_name_and_a_description(self) -> None:
        self.agent('Fact-Checker', tools='Read', name=None, description=None)
        result = self.vault.run(SCRIPT)
        self.assertIn('no name (the spoken name)', result.stdout)
        self.assertIn('no description (the routing key)', result.stdout)

    def test_the_nine_sections(self) -> None:
        self.agent('Fact-Checker', name='Felix', tools='Read', body='# Fact-Checker\n\n## Identity\n')
        self.assert_flags('no ## Method section')

    def test_a_lead_holds_exactly_the_orchestration_tools(self) -> None:
        self.agent(LEAD, name='Beatrice', tools='Read, Grep, Glob, Task, Write')
        self.assert_flags('a lead holds exactly Glob, Grep, Read, Task')

    def test_a_specialist_never_writes(self) -> None:
        self.agent('Fact-Checker', name='Felix', tools='Read, Edit')
        self.assert_flags('holds neither Write nor Edit')

    def test_the_librarian_may_labor(self) -> None:
        self.vault.note('Library/Library.md')
        self.agent(f'{STAR} Librarian', folder='Library', name='Marian',
                   tools='Read, Grep, Glob, Write, Edit, Bash, Task')
        result = self.vault.run(SCRIPT)
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_a_team_has_exactly_one_lead(self) -> None:
        self.agent(f'{STAR} Second Lead', name='Sasha', tools='Read, Grep, Glob, Task')
        self.assert_flags('a team stars exactly one member, its lead; found 2')
        self.vault.path(f'{TEAM}/{STAR} Second Lead.md').unlink()
        self.vault.path(f'{TEAM}/{LEAD}.md').unlink()
        self.assert_flags('found 0')

    def test_the_folder_is_the_team(self) -> None:
        self.agent('Statistician', name='Stella', tools='Read')
        result = self.vault.run(SCRIPT)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn('3 agents and 1 rosters pass', result.stdout)

    def test_a_team_needs_its_own_note(self) -> None:
        folder = 'Ventures/Agent Resources (AR)/Legal'
        self.agent(f'{STAR} General Counsel', folder=folder, name='Gwen', tools='Read, Grep, Glob, Task')
        self.assert_flags('the team Legal has no note of its own')

    def test_a_skill_keeps_exactly_one_roster_beside_its_team(self) -> None:
        self.vault.path(f'{TEAM}/Research.md').unlink()
        self.assert_flags('exactly one roster, the note named for the team; found 0')
        self.roster()
        self.vault.note(f'{TEAM}/Notes.md')
        self.assert_flags('found 2')

    def test_a_roster_needs_a_title_and_a_description(self) -> None:
        self.roster(description=None)
        self.assert_flags('the frontmatter has no description')

    def test_names_are_unique_across_homes(self) -> None:
        self.vault.note('Library/Library.md')
        self.agent(f'{STAR} Librarian', folder='Library', name='Felix',
                   tools='Read, Grep, Glob, Write, Edit, Bash, Task')
        self.assert_flags("the spoken name 'felix' is also used by")

    def test_naming_one_agent(self) -> None:
        self.assertEqual(self.vault.run(SCRIPT, 'Felix').returncode, 0)
        self.assertEqual(self.vault.run(SCRIPT, 'Nobody').returncode, 2)

    def test_the_real_library_passes(self) -> None:
        result = fixtures.subprocess.run([sys.executable, str(fixtures.SCRIPTS / SCRIPT)],
                                         capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main()
