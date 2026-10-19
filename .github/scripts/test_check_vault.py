#!/usr/bin/env python3
"""Tests for check-vault.py, and for the wiring that runs the vault scripts.

WHY THIS EXISTS. check-vault.py is the one command CI and a person run, so it
must run every check and fail when any one does. The scripts are also called
from places a unit test of each script never sees: the Claude Code hooks in
.claude/settings.json and the composite action CI uses. A renamed script
would leave those pointing at nothing, silently. These tests check the
umbrella on a throwaway vault, then check that every script the hooks and
the action name exists, and that every script is written the way this
folder's File Log reads them.

Run it:

    python3 .github/scripts/test_check_vault.py
"""

from __future__ import annotations

import ast
import json
import pathlib
import re
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fixtures  # noqa: E402

SCRIPT = 'check-vault.py'
ROOT = fixtures.SCRIPTS.parents[1]
DASHES = re.compile('[\u2013\u2014\u2015]')
VAULT_SCRIPTS = ('vault.py', 'lint-notes.py', 'check-links.py', 'check-skills.py', 'check-agents.py',
                 'scan-pii.py', 'update-vault.py', 'check-vault.py', 'session-hooks.py', 'profile-coverage.py',
                 'knowledge-base.py', 'fixtures.py')


class TestCheckVault(unittest.TestCase):
    def setUp(self) -> None:
        self.vault = fixtures.Vault()

    def tearDown(self) -> None:
        self.vault.cleanup()

    def test_an_empty_vault_passes_every_check(self) -> None:
        self.vault.init_git()
        result = self.vault.run(SCRIPT)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('All 6 vault checks pass.', result.stdout)

    def test_one_failing_check_fails_the_run_and_is_named(self) -> None:
        self.vault.write('Memory/Memory.md', '# no frontmatter, and [[Nowhere]]\n')
        self.vault.init_git()
        result = self.vault.run(SCRIPT)
        self.assertEqual(result.returncode, 1)
        # A note with no catalog drawn yet also leaves the generated parts stale.
        self.assertIn('3 of 6 vault checks fail: notes, links, generated parts.', result.stderr)

    def test_the_real_vault_passes(self) -> None:
        result = fixtures.subprocess.run([sys.executable, str(fixtures.SCRIPTS / SCRIPT)],
                                         capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


class TestWiring(unittest.TestCase):
    def test_every_hook_runs_a_script_that_exists(self) -> None:
        settings = json.loads((ROOT / '.claude' / 'settings.json').read_text(encoding='utf-8'))
        commands = [hook['command'] for groups in settings['hooks'].values() for group in groups
                    for hook in group['hooks']]
        self.assertTrue(commands)
        for command in commands:
            self.assertNotIn('brain.command', command)
            for path in re.findall(r'\$\{CLAUDE_PROJECT_DIR\}/([^"\s]+)', command):
                self.assertTrue((ROOT / path).is_file(), f'{command} names {path}, which does not exist')

    def test_the_action_runs_scripts_that_exist(self) -> None:
        action = (ROOT / '.github' / 'actions' / 'vault' / 'action.yml').read_text(encoding='utf-8')
        named = re.findall(r'\.github/scripts/([\w.-]+\.py)', action)
        self.assertIn('check-vault.py', named)
        for name in named:
            self.assertTrue((fixtures.SCRIPTS / name).is_file(), name)
        workflow = (ROOT / '.github' / 'workflows' / 'vault.yml').read_text(encoding='utf-8')
        self.assertIn('uses: ./.github/actions/vault', workflow)
        self.assertNotIn('is_template', workflow.split('jobs:', 1)[1])

    def test_check_vault_runs_every_check_script(self) -> None:
        source = (fixtures.SCRIPTS / SCRIPT).read_text(encoding='utf-8')
        for name in ('lint-notes.py', 'check-links.py', 'check-skills.py', 'check-agents.py', 'scan-pii.py',
                     'update-vault.py'):
            self.assertIn(f"'{name}'", source)

    def test_every_script_reads_well_in_the_file_log(self) -> None:
        for name in VAULT_SCRIPTS + tuple(p.name for p in fixtures.SCRIPTS.glob('test_*.py')):
            text = (fixtures.SCRIPTS / name).read_text(encoding='utf-8')
            doc = ast.get_docstring(ast.parse(text))
            self.assertTrue(doc, f'{name} has no docstring')
            first = doc.split('\n', 1)[0]
            self.assertTrue(first.endswith('.'), f'{name}: the first docstring line is the File Log purpose')
            self.assertIsNone(DASHES.search(text), f'{name} holds an en, em or bar dash')
            self.assertIn('from __future__ import annotations', text, f'{name} must run on Python 3.9')


if __name__ == '__main__':
    unittest.main()
