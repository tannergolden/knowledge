#!/usr/bin/env python3
"""Tests for update-vault.py, which draws every generated part of the vault.

WHY THIS EXISTS. update-vault.py moves session summaries, rewrites blocks
inside notes, rebuilds the catalog, and adds and removes .gitkeep markers,
often with nobody watching. A mistake in
any of those changes the vault behind someone's back. Each test builds a
small vault, runs the real script (and its --check), and checks the files it
leaves. The last test checks, read only, that the vault this repository holds
is up to date.

Run it:

    python3 .github/scripts/test_update_vault.py
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

SCRIPT = 'update-vault.py'
NOTE = 'drawn by .github/scripts/update-vault.py - do not edit by hand'


def block(name: str, body: str = '', note: str = 'old note') -> str:
    return f'<!-- brain:{name} ({note}) -->\n{body}\n<!-- /brain:{name} -->\n'


def drawn(name: str, body: str) -> str:
    return f'<!-- brain:{name} ({NOTE}) -->\n{body}\n<!-- /brain:{name} -->'


class Base(unittest.TestCase):
    def setUp(self) -> None:
        self.vault = fixtures.Vault()
        v = self.vault
        v.note('Memory/Context/Current/README.md', body='# Current\n\n' + block('tier-summaries'))
        v.note('Memory/Context/Recent/README.md', body='# Recent\n\n' + block('tier-summaries'))
        for name, folder in (('People', 'Memory/Entities/People'), ('Organizations', 'Memory/Entities/Organizations'),
                             ('Places', 'Memory/Entities/Places'), ('Decisions', 'Memory/Decisions'),
                             ('Events', 'Memory/Events'), ('Insights', 'Memory/Insights')):
            v.note(f'{folder}/README.md', body=f'# {name}\n\n' + block('collection-entries'))
        for name in ('Values', 'Goals', 'Skills', 'Health'):
            v.note(f'Profile/{name}/README.md', body=f'# {name}\n\n' + block('profile-entries'))
        v.note('Memory/Log.md', body='# Log\n\n## Open Loops\n\n' + block('open-loops') + '\n## Log Entries\n\n')

    def tearDown(self) -> None:
        self.vault.cleanup()

    def update(self, *args: str):
        return self.vault.run(SCRIPT, *args)

    def summary(self, tier: str, name: str) -> None:
        self.vault.note(f'Memory/Context/{tier}/{name}.md', type='record')


class TestCascade(Base):
    def test_current_overflow_moves_down_and_recent_overflow_is_archived(self) -> None:
        for i in range(1, 5):
            self.summary('Current', f'2026010{i}-000000')
        for i in range(1, 7):
            self.summary('Recent', f'2025010{i}-000000')
        result = self.update()
        self.assertEqual(result.returncode, 0, result.stdout)
        current = sorted(p.name for p in self.vault.path('Memory/Context/Current').glob('2*.md'))
        self.assertEqual(current, ['20260102-000000.md', '20260103-000000.md', '20260104-000000.md'])
        self.assertTrue(self.vault.path('Memory/Context/Recent/20260101-000000.md').exists())
        self.assertTrue(self.vault.path('Memory/Context/Archive/2025/20250101-000000.md').exists())
        self.assertIn('moved: Memory/Context/Current/20260101-000000.md -> Memory/Context/Recent/20260101-000000.md',
                      result.stdout)

    def test_an_undated_summary_and_a_name_already_taken(self) -> None:
        for name in ('a', 'b', 'c', 'd', 'e', 'f', 'g'):
            self.summary('Recent', name)
        self.vault.write('Memory/Context/Archive/undated/a.md', 'already here')
        self.update()
        self.assertEqual(self.vault.read('Memory/Context/Archive/undated/a.md'), 'already here')
        self.assertTrue(self.vault.path('Memory/Context/Archive/undated/a-1.md').exists())

    def test_check_reports_a_tier_over_its_cap_and_moves_nothing(self) -> None:
        for i in range(1, 5):
            self.summary('Current', f'2026010{i}-000000')
        result = self.update('--check')
        self.assertEqual(result.returncode, 1)
        self.assertIn('Current holds 4 summaries; its cap is 3', result.stdout)
        self.assertEqual(len(list(self.vault.path('Memory/Context/Current').glob('2*.md'))), 4)


class TestBlocks(Base):
    def test_every_registered_block_is_drawn(self) -> None:
        self.summary('Current', '20260101-000000')
        self.vault.note('Memory/Entities/People/Ada Lovelace.md')
        self.vault.note('Profile/Values/Honesty.md')
        self.update()
        self.assertIn(drawn('tier-summaries', '- [[20260101-000000]]'), self.vault.read('Memory/Context/Current/README.md'))
        self.assertIn(drawn('tier-summaries', '_No summaries in this tier right now._'),
                      self.vault.read('Memory/Context/Recent/README.md'))
        self.assertIn(drawn('collection-entries', '- [[Memory/Entities/People/Ada Lovelace|Ada Lovelace]]'),
                      self.vault.read('Memory/Entities/People/README.md'))
        self.assertIn(drawn('collection-entries', '_No places recorded yet._'),
                      self.vault.read('Memory/Entities/Places/README.md'))
        self.assertIn(drawn('profile-entries', '- [[Profile/Values/Honesty|Honesty]]'),
                      self.vault.read('Profile/Values/README.md'))

    def test_open_loops_come_from_the_log(self) -> None:
        log = self.vault.read('Memory/Log.md') + (
            '### 2026-01-02 - Call the bank\n\nAbout the card.\n\n**Status:** Open\n\n'
            '### 2026-01-01 - Done thing\n\n**Status:** Resolved (2026-01-03)\n')
        self.vault.write('Memory/Log.md', log)
        self.update()
        self.assertIn(drawn('open-loops', '- Call the bank  (opened 2026-01-02)'), self.vault.read('Memory/Log.md'))

    def test_children_only_where_a_folders_readme_asks(self) -> None:
        self.vault.note('Library/Arts/README.md', body='# Arts\n\n' + block('children'))
        self.vault.note('Library/Arts/Painting/README.md')
        self.vault.note('Library/Arts/Sculpture/Notes.md')
        self.vault.note('Library/Science/README.md')
        self.vault.note('Library/Science/Physics/README.md')
        self.update()
        # A subfolder is listed by its README.md, named after the folder; one with no README.md is not.
        self.assertIn(drawn('children', '- [[Library/Arts/Painting/README|Painting]]'),
                      self.vault.read('Library/Arts/README.md'))
        self.assertNotIn('brain:children', self.vault.read('Library/Science/README.md'))

    def test_a_scaffolds_readme_is_never_drawn(self) -> None:
        text = '# [Company]\n\n' + block('children')
        self.vault.note('Ventures/.template/README.md', body=text, type='template')
        self.vault.note('Ventures/.template/Sales/README.md', type='template')
        self.update()
        # The block is left exactly as it was: a scaffold's README is never drawn.
        self.assertIn(block('children'), self.vault.read('Ventures/.template/README.md'))

    def test_a_registered_note_without_its_block_is_an_error(self) -> None:
        self.vault.note('Memory/Events/README.md', body='# Events\n')
        result = self.update()
        self.assertEqual(result.returncode, 1)
        self.assertIn('Memory/Events/README.md: has no <!-- brain:collection-entries --> block', result.stdout)

    def test_an_old_marker_counts_as_stale_and_is_migrated(self) -> None:
        self.update()
        text = self.vault.read('Memory/Events/README.md').replace(NOTE, 'auto-maintained by brain.command')
        self.vault.write('Memory/Events/README.md', text)
        self.assertEqual(self.update('--check').returncode, 1)
        self.update()
        self.assertIn(NOTE, self.vault.read('Memory/Events/README.md'))
        self.assertEqual(self.update('--check').returncode, 0)


class TestCatalogs(Base):
    def test_the_note_catalog(self) -> None:
        self.vault.note('Library/.template/Card.md', type='template')
        self.vault.note('Library/.template/README.md', title='[Company]')
        self.vault.note('Library/README.md', keywords=['books'])
        self.vault.write('README.md', '# The vault\n')
        self.update()
        lines = self.vault.read('System/Data/catalog.ndjson').splitlines()
        records = [json.loads(line) for line in lines]
        paths = [r['path'] for r in records]
        self.assertEqual(paths, sorted(paths))
        # No scaffold is cataloged, a scaffold folder's README.md included, and the root's README.md is a page.
        self.assertNotIn('BRAIN/Library/.template/Card.md', paths)
        self.assertNotIn('BRAIN/Library/.template/README.md', paths)
        self.assertNotIn('BRAIN/README.md', paths)
        self.assertNotIn('[Company]', [r['title'] for r in records])
        library = next(r for r in records if r['path'] == 'BRAIN/Library/README.md')
        self.assertEqual(sorted(library), ['description', 'keywords', 'path', 'status', 'title', 'type'])
        self.assertEqual(library['keywords'], ['books'])
        self.assertEqual(library['type'], 'index')


class TestWhatGitIgnores(Base):
    def test_nothing_git_ignores_is_drawn_and_a_fresh_checkout_agrees(self) -> None:
        v = self.vault
        v.write('.gitignore', 'build/\n*.zip\n')
        v.note('Projects/README.md', body='# Projects\n\n' + block('children'))
        v.note('Projects/Shed/README.md')
        v.note('Projects/Shed/build/Plan.md')
        v.note('Projects/build/README.md')
        v.path('Projects/Shed/build/empty').mkdir(parents=True)
        v.write('Ventures/Acme/Miscellaneous/.gitkeep', '')
        v.write('Ventures/Acme/Miscellaneous/export.zip', 'x')
        v.init_git()
        self.update()
        catalog = v.read('System/Data/catalog.ndjson')
        self.assertIn('BRAIN/Projects/Shed/README.md', catalog)
        self.assertNotIn('build', catalog)
        self.assertIn('[[Projects/Shed/README|Shed]]', v.read('Projects/README.md'))
        self.assertNotIn('Projects/build', v.read('Projects/README.md'))
        self.assertFalse(v.path('Projects/Shed/build/empty/.gitkeep').exists())
        # A folder holding only what git ignores is empty to git, so it keeps its marker.
        self.assertTrue(v.path('Ventures/Acme/Miscellaneous/.gitkeep').exists())
        self.assertEqual(self.update('--check').returncode, 0)
        # The machine that holds the ignored notes and a fresh checkout of the same commit draw the same vault.
        v.git('add', '-A')
        v.git('commit', '-q', '-m', 'test: drawn')
        clone = pathlib.Path(tempfile.mkdtemp(prefix='vault-clone-'))
        try:
            fixtures.subprocess.run(['git', 'clone', '-q', str(v.root), str(clone)], check=True, capture_output=True)
            result = fixtures.subprocess.run([sys.executable, str(fixtures.SCRIPTS / SCRIPT), '--root', str(clone), '--check'],
                                             capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        finally:
            shutil.rmtree(clone, ignore_errors=True)


class TestKeepsAndCheck(Base):
    def test_gitkeep_both_ways(self) -> None:
        self.vault.path('Projects/Empty').mkdir(parents=True)
        self.vault.write('Projects/Full/.gitkeep', '')
        self.vault.write('Projects/Full/Note.md', 'x')
        self.assertEqual(self.update('--check').returncode, 1)
        self.update()
        self.assertTrue(self.vault.path('Projects/Empty/.gitkeep').exists())
        self.assertFalse(self.vault.path('Projects/Full/.gitkeep').exists())

    def test_a_second_run_changes_nothing(self) -> None:
        self.summary('Current', '20260101-000000')
        self.update()
        result = self.update()
        self.assertIn('Everything generated is up to date.', result.stdout)
        self.assertEqual(self.update('--check').returncode, 0)

    def test_check_writes_nothing(self) -> None:
        before = sorted(str(p) for p in self.vault.root.rglob('*'))
        self.update('--check')
        self.assertEqual(sorted(str(p) for p in self.vault.root.rglob('*')), before)

    def test_the_real_vault_is_up_to_date(self) -> None:
        result = fixtures.subprocess.run([sys.executable, str(fixtures.SCRIPTS / SCRIPT), '--check'],
                                         capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main()
