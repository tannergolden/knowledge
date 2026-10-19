#!/usr/bin/env python3
"""Tests for session-hooks.py, the vault's three session helpers.

WHY THIS EXISTS. A helper that crashes or prints the wrong thing hands the
agent running it bad context, and breaks any session whose hook calls it.
These run each helper on a throwaway vault. For the helpers that call other
scripts, they copy session-hooks.py beside small stand-ins, so a test of a
helper never depends on the scripts it calls.

Run it:

    python3 .github/scripts/test_session_hooks.py
"""

from __future__ import annotations

import json
import pathlib
import shutil
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fixtures  # noqa: E402

SCRIPT = 'session-hooks.py'


def stub(exit_code: int, output: str) -> str:
    return f'import sys\nprint({output!r})\nsys.exit({exit_code})\n'


class TestStart(unittest.TestCase):
    def setUp(self) -> None:
        self.vault = fixtures.Vault()

    def tearDown(self) -> None:
        self.vault.cleanup()

    def test_the_card_lists_startup_notes_summaries_and_the_inbox(self) -> None:
        self.vault.note('Profile/Working Style.md')
        self.vault.note('Memory/Log.md')
        for name, status in (('20260101-000000', 'active'), ('20260102-000000', 'active'),
                             ('20260103-000000', 'deprecated'), ('20251231-000000', 'active')):
            self.vault.note(f'Memory/Context/Current/{name}.md', type='record', status=status)
        self.vault.write('Inbox/scan.pdf', 'pdf')
        self.vault.write('Inbox/Reports/kept.md', 'kept')
        result = self.vault.run(SCRIPT, 'start')
        self.assertEqual(result.returncode, 0)
        lines = result.stdout.splitlines()
        self.assertIn('READ Profile/Working Style.md', lines)
        self.assertLess(lines.index('READ Profile/Working Style.md'), lines.index('READ Memory/Log.md'))
        self.assertIn('READ Memory/Context/Current/20260102-000000.md  (session summary)', lines)
        self.assertIn('READ Memory/Context/Current/20260101-000000.md  (session summary)', lines)
        self.assertNotIn('20260103', result.stdout)
        self.assertNotIn('20251231', result.stdout)
        self.assertIn('INBOX Inbox/scan.pdf', lines)
        self.assertNotIn('kept.md', result.stdout)

    def test_an_empty_vault_still_gets_a_card(self) -> None:
        result = self.vault.run(SCRIPT, 'start')
        self.assertEqual(result.returncode, 0)
        self.assertIn('Inbox clear.', result.stdout)
        self.assertLess(len(result.stdout), 1500)


class TestWithStandIns(unittest.TestCase):
    """The hooks that call other scripts, run beside stand-ins for them."""

    def setUp(self) -> None:
        self.vault = fixtures.Vault()
        self.scripts = pathlib.Path(tempfile.mkdtemp(prefix='hooks-test-'))
        for name in (SCRIPT, 'vault.py'):
            shutil.copy(fixtures.SCRIPTS / name, self.scripts / name)

    def tearDown(self) -> None:
        self.vault.cleanup()
        shutil.rmtree(self.scripts, ignore_errors=True)

    def stand_in(self, name: str, exit_code: int, output: str) -> None:
        (self.scripts / name).write_text(stub(exit_code, output), encoding='utf-8')

    def hook(self, name: str, stdin: str = ''):
        return self.vault.run(SCRIPT, name, stdin=stdin, scripts=self.scripts)

    def edited(self, path: str) -> str:
        return json.dumps({'tool_input': {'file_path': str(self.vault.root / path)}})

    def test_after_edit_hands_a_lint_failure_back(self) -> None:
        self.stand_in('lint-notes.py', 1, 'error: Memory/Log.md: missing field: id')
        self.vault.write('Memory/Log.md', 'x')
        result = self.hook('after-edit', self.edited('Memory/Log.md'))
        self.assertEqual(result.returncode, 0)
        out = json.loads(result.stdout)['hookSpecificOutput']
        self.assertEqual(out['hookEventName'], 'PostToolUse')
        self.assertIn('lint-notes.py flagged Memory/Log.md', out['additionalContext'])
        self.assertIn('missing field: id', out['additionalContext'])

    def test_after_edit_is_silent_when_the_note_passes(self) -> None:
        self.stand_in('lint-notes.py', 0, '1 note passes.')
        self.vault.write('Memory/Log.md', 'x')
        self.assertEqual(self.hook('after-edit', self.edited('Memory/Log.md')).stdout, '')

    def test_after_edit_checks_a_skill_source(self) -> None:
        self.stand_in('lint-notes.py', 0, 'fine')
        self.stand_in('check-skills.py', 1, 'error: SKILL.md: the frontmatter has no name')
        self.vault.write('System/Skills/.unpackaged/demo/SKILL.md', 'x')
        result = self.hook('after-edit', self.edited('System/Skills/.unpackaged/demo/SKILL.md'))
        self.assertIn('check-skills.py flagged', result.stdout)

    def test_after_edit_ignores_what_is_not_the_vault_and_bad_input(self) -> None:
        self.stand_in('lint-notes.py', 1, 'error')
        outside = json.dumps({'tool_input': {'file_path': '/somewhere/else.md'}})
        for payload in (outside, 'not json', '', json.dumps({'tool_input': {'file_path': 'x.py'}})):
            result = self.hook('after-edit', payload)
            self.assertEqual((result.returncode, result.stdout), (0, ''), payload)

    def test_stop_is_silent_on_a_clean_tree(self) -> None:
        self.stand_in('update-vault.py', 0, 'updated: a.md')
        self.stand_in('check-vault.py', 1, 'error: x')
        self.vault.write('Memory/Log.md', 'x')
        self.vault.init_git()
        self.assertEqual(self.hook('stop').stdout, '')

    def test_stop_reports_what_it_redrew_and_what_fails(self) -> None:
        self.stand_in('update-vault.py', 0, 'updated: System/Data/catalog.ndjson')
        self.stand_in('check-vault.py', 1, 'error: Memory/Log.md: missing field: id')
        self.vault.init_git()
        self.vault.write('Memory/Log.md', 'changed')
        result = self.hook('stop')
        self.assertEqual(result.returncode, 0)
        message = json.loads(result.stdout)['systemMessage']
        self.assertIn('update-vault.py redrew 1 generated part(s): System/Data/catalog.ndjson.', message)
        self.assertIn('check-vault.py found problems:\nerror: Memory/Log.md: missing field: id', message)

    def test_stop_is_silent_when_all_is_well(self) -> None:
        self.stand_in('update-vault.py', 0, 'Everything generated is up to date.')
        self.stand_in('check-vault.py', 0, 'All 6 vault checks pass.')
        self.vault.init_git()
        self.vault.write('Memory/Log.md', 'changed')
        self.assertEqual(self.hook('stop').stdout, '')

    def test_stop_survives_missing_scripts(self) -> None:
        self.vault.write('Memory/Log.md', 'changed')
        result = self.hook('stop')
        self.assertEqual((result.returncode, result.stdout), (0, ''))


if __name__ == '__main__':
    unittest.main()
