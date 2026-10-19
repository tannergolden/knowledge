#!/usr/bin/env python3
"""Tests for update-vault.py, which draws every generated part of the vault.

WHY THIS EXISTS. update-vault.py moves session summaries, rewrites blocks
inside notes, rebuilds two catalogs and every skill archive, and adds and
removes .gitkeep markers, often with nobody watching. A mistake in
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
import sys
import unittest
import zipfile

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fixtures  # noqa: E402

SCRIPT = 'update-vault.py'
STAR = '★'
NOTE = 'drawn by .github/scripts/update-vault.py - do not edit by hand'


def block(name: str, body: str = '', note: str = 'old note') -> str:
    return f'<!-- brain:{name} ({note}) -->\n{body}\n<!-- /brain:{name} -->\n'


def drawn(name: str, body: str) -> str:
    return f'<!-- brain:{name} ({NOTE}) -->\n{body}\n<!-- /brain:{name} -->'


class Base(unittest.TestCase):
    def setUp(self) -> None:
        self.vault = fixtures.Vault()
        v = self.vault
        v.note('Memory/Context/Current/Current.md', body='# Current\n\n' + block('tier-summaries'))
        v.note('Memory/Context/Recent/Recent.md', body='# Recent\n\n' + block('tier-summaries'))
        for name, folder in (('People', 'Memory/Entities/People'), ('Organizations', 'Memory/Entities/Organizations'),
                             ('Places', 'Memory/Entities/Places'), ('Decisions', 'Memory/Decisions'),
                             ('Events', 'Memory/Events'), ('Insights', 'Memory/Insights')):
            v.note(f'{folder}/{name}.md', body=f'# {name}\n\n' + block('collection-entries'))
        for name in ('Values', 'Goals', 'Skills', 'Health'):
            v.note(f'Profile/{name}/{name}.md', body=f'# {name}\n\n' + block('profile-entries'))
        v.note('Memory/Log.md', body='# Log\n\n## Open Loops\n\n' + block('open-loops') + '\n## Log Entries\n\n')

    def tearDown(self) -> None:
        self.vault.cleanup()

    def update(self, *args: str):
        return self.vault.run(SCRIPT, *args)

    def summary(self, tier: str, name: str) -> None:
        self.vault.note(f'Memory/Context/{tier}/{name}.md', type='record', tags=['memory', 'record'])


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
        self.assertIn(drawn('tier-summaries', '- [[20260101-000000]]'), self.vault.read('Memory/Context/Current/Current.md'))
        self.assertIn(drawn('tier-summaries', '_No summaries in this tier right now._'),
                      self.vault.read('Memory/Context/Recent/Recent.md'))
        self.assertIn(drawn('collection-entries', '- [[Memory/Entities/People/Ada Lovelace|Ada Lovelace]]'),
                      self.vault.read('Memory/Entities/People/People.md'))
        self.assertIn(drawn('collection-entries', '_No places recorded yet._'),
                      self.vault.read('Memory/Entities/Places/Places.md'))
        self.assertIn(drawn('profile-entries', '- [[Profile/Values/Honesty|Honesty]]'),
                      self.vault.read('Profile/Values/Values.md'))

    def test_open_loops_come_from_the_log(self) -> None:
        log = self.vault.read('Memory/Log.md') + (
            '### 2026-01-02 - Call the bank\n\nAbout the card.\n\n**Status:** Open\n\n'
            '### 2026-01-01 - Done thing\n\n**Status:** Resolved (2026-01-03)\n')
        self.vault.write('Memory/Log.md', log)
        self.update()
        self.assertIn(drawn('open-loops', '- Call the bank  (opened 2026-01-02)'), self.vault.read('Memory/Log.md'))

    def test_children_only_where_a_folder_note_asks(self) -> None:
        self.vault.note('Library/Arts/Arts.md', body='# Arts\n\n' + block('children'))
        self.vault.note('Library/Arts/Painting/Painting.md')
        self.vault.note('Library/Science/Science.md')
        self.vault.note('Library/Science/Physics/Physics.md')
        self.update()
        self.assertIn(drawn('children', '- [[Library/Arts/Painting/Painting|Painting]]'),
                      self.vault.read('Library/Arts/Arts.md'))
        self.assertNotIn('brain:children', self.vault.read('Library/Science/Science.md'))

    def test_a_registered_note_without_its_block_is_an_error(self) -> None:
        self.vault.note('Memory/Events/Events.md', body='# Events\n')
        result = self.update()
        self.assertEqual(result.returncode, 1)
        self.assertIn('Memory/Events/Events.md: has no <!-- brain:collection-entries --> block', result.stdout)

    def test_an_old_marker_counts_as_stale_and_is_migrated(self) -> None:
        self.update()
        text = self.vault.read('Memory/Events/Events.md').replace(NOTE, 'auto-maintained by brain.command')
        self.vault.write('Memory/Events/Events.md', text)
        self.assertEqual(self.update('--check').returncode, 1)
        self.update()
        self.assertIn(NOTE, self.vault.read('Memory/Events/Events.md'))
        self.assertEqual(self.update('--check').returncode, 0)


class TestCatalogs(Base):
    def test_the_note_catalog(self) -> None:
        self.vault.note('Library/.template/Card.md', type='template', tags=['library', 'template'])
        self.vault.note('Library/Library.md', keywords=['books'])
        self.update()
        lines = self.vault.read('System/Data/catalog.ndjson').splitlines()
        records = [json.loads(line) for line in lines]
        paths = [r['path'] for r in records]
        self.assertEqual(paths, sorted(paths))
        self.assertNotIn('BRAIN/Library/.template/Card.md', paths)
        library = next(r for r in records if r['path'] == 'BRAIN/Library/Library.md')
        self.assertEqual(sorted(library), ['description', 'folder', 'keywords', 'layer', 'path', 'status', 'tags',
                                           'title', 'type', 'updated'])
        self.assertEqual(library['keywords'], ['books'])
        self.assertEqual(library['layer'], '1')

    def test_the_agent_catalog(self) -> None:
        self.vault.note('Inbox/Faculties/Faculties.md')
        self.vault.note('Inbox/Faculties/Research/Research.md', members=[f'{STAR} Lead', 'Analyst'], lead=f'{STAR} Lead')
        self.vault.note(f'Inbox/Faculties/Research/{STAR} Lead.md', name='Bea', type='agent', tags=['inbox', 'agent'])
        self.vault.note('Inbox/Faculties/Research/Analyst.md', name='Al', type='agent', tags=['inbox', 'agent'])
        self.update()
        first = self.vault.read('System/Data/agent-catalog.json')
        catalog = json.loads(first)
        self.assertEqual(catalog['agent_count'], 2)
        self.assertEqual([a['role'] for a in catalog['agents']], ['Analyst', f'{STAR} Lead'])
        self.assertEqual(catalog['teams'][0]['members'], [f'{STAR} Lead', 'Analyst'])
        self.assertNotIn('generated', catalog)
        self.update()
        self.assertEqual(self.vault.read('System/Data/agent-catalog.json'), first)


class TestArchives(Base):
    SOURCE = 'System/Skills/.unpackaged/demo'

    def setUp(self) -> None:
        super().setUp()
        v = self.vault
        v.write(f'{self.SOURCE}/SKILL.md', '---\nname: demo\nmetadata:\n  team: Research\n  version: "01.00.00"\n---\n# Demo\n')
        v.write(f'{self.SOURCE}/Demo.md', '---\ntitle: Demo\n---\n\n# Demo guide\n')
        v.write(f'{self.SOURCE}/references/guide.md', 'guide\n')
        v.write(f'{self.SOURCE}/assets/.gitkeep', '')
        v.write(f'{self.SOURCE}/.DS_Store', 'junk')
        v.write(f'{self.SOURCE}/__pycache__/x.pyc', 'junk')
        v.note('Inbox/Faculties/Faculties.md')
        v.note('Inbox/Faculties/Research/Research.md', members=[f'{STAR} Lead'], lead=f'{STAR} Lead')
        v.note(f'Inbox/Faculties/Research/{STAR} Lead.md', type='agent', tags=['inbox', 'agent'])

    def entries(self) -> dict[str, bytes]:
        with zipfile.ZipFile(self.vault.path('System/Skills/demo.skill')) as archive:
            return {name: archive.read(name) for name in archive.namelist()}

    def test_the_archive_holds_the_source_and_its_team(self) -> None:
        self.assertEqual(self.update().returncode, 0)
        entries = self.entries()
        self.assertEqual(sorted(entries), sorted([
            'demo/Demo.md', 'demo/SKILL.md', 'demo/assets/.gitkeep', 'demo/references/guide.md',
            'demo/agents/Research.md', f'demo/agents/{STAR} Lead.md']))
        self.assertEqual(entries['demo/Demo.md'], b'# Demo guide\n')
        with zipfile.ZipFile(self.vault.path('System/Skills/demo.skill')) as archive:
            self.assertEqual({info.date_time for info in archive.infolist()}, {(1980, 1, 1, 0, 0, 0)})

    def test_an_unchanged_archive_is_left_alone_even_when_compressed_differently(self) -> None:
        self.update()
        path = self.vault.path('System/Skills/demo.skill')
        contents = self.entries()
        with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_STORED) as archive:
            for name, data in contents.items():
                archive.writestr(name, data)
        stored = path.read_bytes()
        self.assertEqual(self.update('--check').returncode, 0)
        self.update()
        self.assertEqual(path.read_bytes(), stored)

    def test_a_changed_source_is_stale(self) -> None:
        self.update()
        self.vault.write(f'{self.SOURCE}/references/guide.md', 'changed\n')
        result = self.update('--check')
        self.assertEqual(result.returncode, 1)
        self.assertIn('System/Skills/demo.skill: the archive differs from its source', result.stdout)

    def test_a_member_no_agent_file_holds(self) -> None:
        self.vault.note('Inbox/Faculties/Research/Research.md', members=[f'{STAR} Lead', 'Ghost'], lead=f'{STAR} Lead')
        result = self.update()
        self.assertEqual(result.returncode, 1)
        self.assertIn("names 'Ghost', which no agent file in the library is titled", result.stdout)

    def test_an_archive_without_a_source(self) -> None:
        self.vault.write('System/Skills/orphan.skill', 'x')
        self.assertIn('has no source', self.update().stdout)


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
