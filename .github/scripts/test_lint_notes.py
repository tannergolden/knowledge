#!/usr/bin/env python3
"""Tests for lint-notes.py, the note schema check.

WHY THIS EXISTS. lint-notes.py runs after every edit Claude makes in the vault
and on every note in CI, so a rule it gets wrong either lets a broken note
through or blocks a good one in every session. Each test builds a throwaway
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
        self.vault.note('Library/Library.md', author=None)
        self.assert_flags('missing field: author')

    def test_no_frontmatter_and_an_empty_note(self) -> None:
        self.vault.write('Library/Bare.md', '# No frontmatter\n')
        self.vault.write('Library/Empty.md', '   \n')
        result = self.lint()
        self.assertIn('no frontmatter block', result.stdout)
        self.assertIn('the note is empty', result.stdout)

    def test_values_outside_the_schema(self) -> None:
        self.vault.note('Library/Library.md', type='essay', tags=['library', 'essay'], folder='library',
                        status='done', id='Bad_Id', created='June 1')
        result = self.lint()
        for needle in ("type 'essay'", "status 'done'", "id 'Bad_Id'", "created is 'June 1'"):
            self.assertIn(needle, result.stdout)

    def test_a_template_type_outside_a_scaffold(self) -> None:
        self.vault.note('Projects/Site/Overview.md', type='template', tags=['projects', 'template'])
        self.assert_flags("type 'template' outside a .template/ folder")

    def test_a_retired_version_field(self) -> None:
        self.vault.note('Library/Library.md', version='01.00.00')
        self.assert_flags('per-file versions are retired')

    def test_the_path_field_tracks_the_file(self) -> None:
        self.vault.note('Library/Library.md', path='BRAIN/Library/Elsewhere.md')
        self.assert_flags("expected 'BRAIN/Library/Library.md'")

    def test_a_summary_may_lag_its_tier(self) -> None:
        self.vault.note('Memory/Context/Recent/20260101-000000.md', type='record', tags=['memory', 'record'],
                        path='BRAIN/Memory/Context/Current/20260101-000000.md')
        self.assertEqual(self.lint().returncode, 0)

    def test_the_closed_tag_vocabulary(self) -> None:
        self.vault.note('Library/Library.md', tags=['library', 'information', 'cooking'])
        self.assert_flags("tag 'cooking' is outside the closed vocabulary")

    def test_the_folder_and_role_tags(self) -> None:
        self.vault.note('Library/Library.md', tags=['information'])
        self.assert_flags("missing the Folder tag 'library'")
        self.vault.note('Library/Library.md', tags=['library'])
        self.assert_flags("missing the File Role tag 'information'")

    def test_one_tag_per_family_in_order(self) -> None:
        self.vault.note('Library/Library.md', tags=['library', 'information', 'timeless', 'current'])
        self.assert_flags('2 Freshness tags')
        self.vault.note('Library/Library.md', tags=['information', 'library'])
        self.assert_flags('the vocabulary orders them')

    def test_a_readme_outside_the_top_folders_fails(self) -> None:
        self.vault.note('Memory/Memory.md')
        self.vault.write('Memory/README.md', 'The GitHub page.\n')
        self.assertEqual(self.lint().returncode, 0, 'a top folder carries a README')
        self.vault.write('Memory/Context/README.md', 'A second copy.\n')
        self.assert_flags('a README.md belongs only in the seven top folders')
        self.assert_flags('a README.md belongs only in the seven top folders', 'Memory/Context/README.md')

    def test_tags_must_be_a_list(self) -> None:
        self.vault.note('Library/Library.md')
        text = self.vault.read('Library/Library.md').replace('tags: ["library", "information"]', 'tags: library')
        self.vault.write('Library/Library.md', text)
        self.assert_flags('tags is not a list')

    def test_policy_is_a_boolean(self) -> None:
        self.vault.note('Library/Library.md', policy='maybe')
        self.assert_flags('policy must be true or false')

    def test_a_scaffold_carries_no_wikilinks(self) -> None:
        self.vault.note('Library/.template/Card.md', body='See [[Library]].\n', type='template',
                        tags=['library', 'template'])
        self.assert_flags('a scaffold carries no wikilinks')

    def test_a_library_holding_needs_a_freshness_tag(self) -> None:
        self.vault.note('Library/Arts/Paint.md', type='reference', tags=['library', 'reference'])
        self.assert_flags('needs a freshness tag')
        self.vault.note('Library/Arts/Paint.md', type='reference', tags=['library', 'reference', 'timeless'])
        self.assertEqual(self.lint().returncode, 0)

    def test_underscores_and_em_dashes(self) -> None:
        self.vault.note('Library/Snake_Case.md', body='A dash \u2014 here.\n')
        result = self.lint()
        self.assertIn('the file name has an underscore', result.stdout)
        self.assertIn('em dash', result.stdout)

    def test_duplicate_ids_across_the_vault(self) -> None:
        self.vault.note('Library/A.md', id='li-same')
        self.vault.note('Library/B.md', id='li-same')
        self.assert_flags("id 'li-same' is also")

    def test_one_file_still_catches_a_duplicate_id(self) -> None:
        self.vault.note('Library/A.md', id='li-same')
        self.vault.note('Library/B.md', id='li-same')
        result = self.lint('Library/A.md')
        self.assertEqual(result.returncode, 1)
        self.assertIn("id 'li-same' is also Library/B.md's", result.stdout)

    def test_one_file_checks_only_that_file(self) -> None:
        self.vault.note('Library/Good.md')
        self.vault.note('Library/Bad.md', author=None)
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
