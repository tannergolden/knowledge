#!/usr/bin/env python3
"""Tests for check-skills.py, the skill source check.

WHY THIS EXISTS. A skill that breaks the Agent Skills format fails to install,
and one that names a missing team dispatches into nothing; check-skills.py is
what catches both before anyone installs it. Each test builds a valid skill
in a throwaway vault, breaks one thing, and runs the real script. The last
test runs it, read only, on the skills this repository holds.

Run it:

    python3 .github/scripts/test_check_skills.py
"""

from __future__ import annotations

import pathlib
import shutil
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fixtures  # noqa: E402

SCRIPT = 'check-skills.py'
SOURCE = 'System/Skills/.unpackaged/demo'
LEAD = '★ Demo Lead'


def skill_md(**overrides: str) -> str:
    fields = {'name': 'demo', 'description': 'Does the demo. Use when the user asks for a demo.',
              'license': 'MIT', 'allowed-tools': 'Read, Grep'}
    fields.update(overrides)
    head = '\n'.join(f'{key}: {value}' for key, value in fields.items() if value is not None)
    return f'---\n{head}\nmetadata:\n  team: Demo\n  version: "01.00.00"\n---\n\n# Demo\n\n## Boundaries\n\n- Stay small.\n'


def build_skill(vault: fixtures.Vault) -> None:
    vault.write(f'{SOURCE}/SKILL.md', skill_md())
    vault.write(f'{SOURCE}/License.txt', 'MIT License\n')
    vault.note(f'{SOURCE}/Changelog.md', body='# Changelog\n\n## Current Version\n\n**`01.00.00`**\n',
               folder='system', tags=['system', 'information'])
    vault.note(f'{SOURCE}/Demo.md', folder='system', tags=['system', 'information'])
    for sub in ('assets', 'references', 'templates'):
        vault.write(f'{SOURCE}/{sub}/.gitkeep', '')
    vault.note('Inbox/Faculties/Faculties.md')
    vault.note('Inbox/Faculties/Demo/Demo.md', members=[LEAD], lead=LEAD)
    vault.note(f'Inbox/Faculties/Demo/{LEAD}.md', type='agent', tags=['inbox', 'agent'])


class TestCheckSkills(unittest.TestCase):
    def setUp(self) -> None:
        self.vault = fixtures.Vault()
        build_skill(self.vault)

    def tearDown(self) -> None:
        self.vault.cleanup()

    def assert_flags(self, needle: str) -> None:
        result = self.vault.run(SCRIPT)
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn(needle, result.stdout)

    def test_a_valid_skill_passes(self) -> None:
        result = self.vault.run(SCRIPT)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn('1 skill passes.', result.stdout)

    def test_the_name_rules(self) -> None:
        self.vault.write(f'{SOURCE}/SKILL.md', skill_md(name='Demo_Skill'))
        self.assert_flags('must be kebab-case')
        self.vault.write(f'{SOURCE}/SKILL.md', skill_md(name='other'))
        self.assert_flags('differs from its folder')
        self.vault.write(f'{SOURCE}/SKILL.md', skill_md(name=None))
        self.assert_flags('the frontmatter has no name')

    def test_claude_in_a_name(self) -> None:
        source = self.vault.path(SOURCE)
        source.rename(source.with_name('claude-demo'))
        self.vault.write('System/Skills/.unpackaged/claude-demo/SKILL.md', skill_md(name='claude-demo'))
        (self.vault.path('System/Skills/.unpackaged/claude-demo/Demo.md')).rename(
            self.vault.path('System/Skills/.unpackaged/claude-demo/Claude-demo.md'))
        self.assert_flags('may not contain claude or anthropic')

    def test_the_description(self) -> None:
        self.vault.write(f'{SOURCE}/SKILL.md', skill_md(description='x' * 1025))
        self.assert_flags('the format allows 1024')

    def test_license_and_allowed_tools(self) -> None:
        self.vault.write(f'{SOURCE}/SKILL.md', skill_md(license=None))
        self.assert_flags('the frontmatter has no license')

    def test_a_team_no_roster_defines(self) -> None:
        shutil.rmtree(self.vault.path('Inbox/Faculties/Demo'))
        self.assert_flags("metadata.team names 'Demo'")

    def test_the_layout(self) -> None:
        self.vault.path(f'{SOURCE}/License.txt').unlink()
        shutil.rmtree(self.vault.path(f'{SOURCE}/templates'))
        self.vault.write(f'{SOURCE}/agents/x.md', 'x')
        self.vault.write(f'{SOURCE}/scripts/x.py', 'x')
        result = self.vault.run(SCRIPT)
        for needle in ('License.txt is missing', 'the templates/ folder is missing', 'a source holds no agents/',
                       'a source holds no scripts/'):
            self.assertIn(needle, result.stdout)

    def test_a_second_manifest(self) -> None:
        self.vault.write(f'{SOURCE}/templates/SKILL.md', 'x')
        self.assert_flags('a skill holds exactly one SKILL.md')

    def test_the_version_lives_in_the_manifest_and_the_changelog(self) -> None:
        text = self.vault.read(f'{SOURCE}/Changelog.md').replace('**`01.00.00`**', '**`01.01.00`**')
        self.vault.write(f'{SOURCE}/Changelog.md', text)
        self.assert_flags('the Current Version is 01.01.00, but SKILL.md says 01.00.00')

    def test_a_retired_per_file_version(self) -> None:
        self.vault.note(f'{SOURCE}/Demo.md', folder='system', tags=['system', 'information'], version='01.00.00')
        self.assert_flags('per-file versions are retired')

    def test_the_docs_carry_the_note_schema(self) -> None:
        self.vault.note(f'{SOURCE}/Demo.md', folder='system', tags=['system', 'information'], author=None)
        self.assert_flags('the frontmatter lacks author')

    def test_em_dashes_and_boundaries(self) -> None:
        self.vault.write(f'{SOURCE}/references/guide.md', 'one \u2014 two\n')
        self.vault.write(f'{SOURCE}/SKILL.md', skill_md().replace('## Boundaries', '## Limits'))
        result = self.vault.run(SCRIPT)
        self.assertIn('em dash', result.stdout)
        self.assertIn('no ## Boundaries section', result.stdout)

    def test_wikilinks_only_warn(self) -> None:
        self.vault.write(f'{SOURCE}/references/guide.md', 'See [[Somewhere]].\n')
        result = self.vault.run(SCRIPT)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn('warning:', result.stdout)

    def test_naming_one_skill(self) -> None:
        self.assertEqual(self.vault.run(SCRIPT, 'demo').returncode, 0)
        self.assertEqual(self.vault.run(SCRIPT, 'nope').returncode, 2)

    def test_the_real_skills_pass(self) -> None:
        result = fixtures.subprocess.run([sys.executable, str(fixtures.SCRIPTS / SCRIPT)],
                                         capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main()
