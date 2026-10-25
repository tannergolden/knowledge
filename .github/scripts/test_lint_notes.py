#!/usr/bin/env python3
"""Tests for lint-notes.py, the note schema check.

WHY THIS EXISTS. lint-notes.py runs on a note after an edit and on every note
in CI, so a rule it gets wrong either lets a broken note through or blocks a
good one everywhere. Each test builds a throwaway
vault, runs the real script on it, and checks one rule both ways. The last
test runs it, read only, on the vault this repository holds.

Run it:

    python3 .github/scripts/test_lint_notes.py
"""

from __future__ import annotations

import pathlib
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fixtures  # noqa: E402

SCRIPT = 'lint-notes.py'


class TestLintNotes(unittest.TestCase):
    def setUp(self) -> None:
        self.vault = fixtures.Vault()

    def tearDown(self) -> None:
        self.vault.cleanup()

    def lint(self, *args: str):
        return self.vault.run(SCRIPT, *args)

    def assert_flags(self, needle: str, *args: str) -> None:
        result = self.lint(*args)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(needle, result.stdout)

    def test_a_valid_note_passes(self) -> None:
        self.vault.note('Library/Library.md')
        result = self.lint()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn('1 note passes.', result.stdout)

    def test_a_missing_field(self) -> None:
        self.vault.note('Library/Library.md', description=None)
        self.assert_flags('missing field: description')

    def test_no_frontmatter_and_an_empty_note(self) -> None:
        self.vault.write('Library/Bare.md', '# No frontmatter\n')
        self.vault.write('Library/Empty.md', '   \n')
        result = self.lint()
        self.assertIn('no frontmatter block', result.stdout)
        self.assertIn('the note is empty', result.stdout)

    def test_values_outside_the_schema(self) -> None:
        self.vault.note('Library/Library.md', type='essay', status='done', keywords=['Cooking', 'x', 'x'])
        result = self.lint()
        for needle in ("type 'essay'", "status 'done'", "keyword 'Cooking' is not lowercase",
                       'a keyword appears twice'):
            self.assertIn(needle, result.stdout)

    def test_status_is_left_out_while_a_note_is_current(self) -> None:
        self.vault.note('Library/Library.md', status='active')
        self.assert_flags('leave it out while the note is current')
        self.vault.note('Library/Library.md', status='deprecated')
        self.assertEqual(self.lint().returncode, 0)

    def test_a_fenced_note_is_caught_and_an_agent_spec_is_not(self) -> None:
        self.vault.write('Library/Fenced.md', '---\ntitle: "Fenced"\ndescription: "A note."\ntype: "index"\n---\n')
        self.assert_flags('fenced with ---, which GitHub shows as a table')
        self.vault.write('Library/Fenced.md', '---\nname: "Ada"\ndescription: "An agent."\ntools: Read\n---\n')
        self.assertEqual(self.lint().returncode, 0)

    def test_a_template_type_outside_a_scaffold(self) -> None:
        self.vault.note('Projects/Site/Overview.md', type='template')
        self.assert_flags("type 'template' outside a .template/ folder")

    def test_the_old_schema_is_retired(self) -> None:
        self.vault.note('Library/Library.md', tags=['library'], layer=1, version='01.00.00')
        result = self.lint()
        for field in ('tags', 'layer', 'version'):
            self.assertIn(f"'{field}' is retired", result.stdout)

    def test_a_readme_outside_the_top_folders_fails(self) -> None:
        self.vault.note('Memory/Memory.md')
        self.vault.write('Memory/README.md', 'The GitHub page.\n')
        self.assertEqual(self.lint().returncode, 0, 'a top folder carries a README')
        self.vault.write('Memory/Context/README.md', 'A second copy.\n')
        self.assert_flags('a README.md belongs only in the seven top folders')
        self.assert_flags('a README.md belongs only in the seven top folders', 'Memory/Context/README.md')

    def test_only_a_record_or_a_template_adds_fields(self) -> None:
        self.vault.note('Library/Library.md', lens='wide')
        self.assert_flags("'lens' is not one of a note's fields")
        self.vault.note('Library/Library.md', type='record', lens='wide', id='in-idea-1')
        self.assertEqual(self.lint().returncode, 0)

    def test_keywords_stay_few(self) -> None:
        self.vault.note('Library/Library.md', keywords=[f'term {i}' for i in range(9)])
        self.assert_flags('9 keywords')

    def test_a_library_holding_carries_one_freshness_token(self) -> None:
        self.vault.note('Library/Arts/Paint.md', type='reference', keywords=['pigment'])
        self.assert_flags('a Library holding carries one freshness token')
        self.vault.note('Library/Arts/Paint.md', type='reference', keywords=['freshness/timeless', 'pigment'])
        self.assertEqual(self.lint().returncode, 0)

    def test_a_scaffold_carries_no_wikilinks(self) -> None:
        self.vault.note('Library/.template/Card.md', body='See [[Library]].\n', type='template')
        self.assert_flags('a scaffold carries no wikilinks')

    def test_underscores_and_em_dashes(self) -> None:
        self.vault.note('Library/Snake_Case.md', body='A dash \u2014 here.\n')
        result = self.lint()
        self.assertIn('the file name has an underscore', result.stdout)
        self.assertIn('em dash', result.stdout)

    def test_only_githubs_five_callouts(self) -> None:
        self.vault.note('Memory/Log.md', body='# Log\n\n> [!NOTE]\n> **Kept.**\n> Fine.\n\n'
                        '```markdown\n> [!tip] An example, inside code\n```\n')
        self.assertEqual(self.lint().returncode, 0)
        self.vault.note('Memory/Log.md', body='# Log\n\n> [!warning] Titled\n> Body.\n\n> [!TIP] Titled too\n')
        result = self.lint()
        self.assertIn('callout [!warning] Titled does not render on GitHub', result.stdout)
        self.assertIn('callout [!TIP] Titled too does not render on GitHub', result.stdout)

    def test_one_file_checks_only_that_file(self) -> None:
        self.vault.note('Library/Good.md')
        self.vault.note('Library/Bad.md', description=None)
        result = self.lint('Library/Good.md')
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn('1 note passes.', result.stdout)

    def test_a_file_outside_the_walk_is_skipped(self) -> None:
        self.vault.write('.github/README.md', '# not a note\n')
        result = self.lint('.github/README.md')
        self.assertEqual(result.returncode, 0)
        self.assertIn('0 notes pass.', result.stdout)

    def test_a_missing_file_is_a_usage_error(self) -> None:
        self.assertEqual(self.lint('Nope.md').returncode, 2)

    def test_the_real_vault_passes(self) -> None:
        result = fixtures.subprocess.run([sys.executable, str(fixtures.SCRIPTS / SCRIPT)],
                                         capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main()
