#!/usr/bin/env python3
"""Tests for profile-coverage.py, the report the profile interview reads.

WHY THIS EXISTS. The profile interview decides which part of a person's
Profile to ask about from this report, so a line counted wrongly sends the
interview to the wrong place, and a change to the JSON breaks the interview
outright. These score small Profiles in a throwaway vault, pin the
JSON contract's keys, and read the real vault's report, which never writes. In
the blank template they also check that every facet still scores as scaffold,
so a reworded facet fails here until the frozen table is refrozen.

Run it:

    python3 .github/scripts/test_profile_coverage.py
"""

from __future__ import annotations

import json
import pathlib
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fixtures  # noqa: E402

SCRIPT = 'profile-coverage.py'
ROW_KEYS = ['facet', 'kind', 'path', 'files', 'entries', 'substantive', 'unconfirmed', 'depth', 'status', 'rank']


class TestProfileCoverage(unittest.TestCase):
    def setUp(self) -> None:
        self.vault = fixtures.Vault()

    def tearDown(self) -> None:
        self.vault.cleanup()

    def report(self, *args: str) -> dict:
        result = self.vault.run(SCRIPT, '--json', *args)
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def facet(self, report: dict, name: str) -> dict:
        return next(f for f in report['facets'] if f['facet'] == name)

    def test_a_missing_profile_scores_zero_everywhere(self) -> None:
        report = self.report()
        self.assertEqual(sorted(report), ['facets', 'generated', 'target'])
        self.assertEqual(len(report['facets']), 12)
        self.assertEqual(list(report['facets'][0]), ROW_KEYS + ['missing'])
        self.assertEqual(report['target'], 'Working Style')

    def test_real_lines_count_and_placeholders_do_not(self) -> None:
        self.vault.note('Profile/Biography.md', body='\n'.join([
            '# Biography', '## Early life', '- **Born:**', '- **Raised:** (city)', '[Name]', '| --- | --- |',
            '_None recorded yet._', 'Grew up by the sea and learned to sail at nine.',
            '- **School:** Ridgeview High', '<!-- a comment only -->', '']), type='self')
        biography = self.facet(self.report(), 'Biography')
        self.assertEqual(biography['substantive'], 2)
        self.assertEqual(biography['status'], 'sparse')

    def test_unconfirmed_proposals_count_against_depth(self) -> None:
        self.vault.note('Profile/Focus.md', body='# Focus\n## Now\nShipping the vault. <!-- unconfirmed 2026-01-01 -->\n',
                        type='self')
        focus = self.facet(self.report(), 'Focus')
        self.assertEqual((focus['substantive'], focus['unconfirmed'], focus['depth']), (1, 1, 0))

    def test_a_folder_facet_counts_its_entries(self) -> None:
        self.vault.note('Profile/Values/README.md', body='# Values\n')
        self.vault.note('Profile/Values/Honesty.md', body='# Honesty\nTell the truth even when it costs.\n')
        values = self.vault.run(SCRIPT, 'Values', '--json')
        row = json.loads(values.stdout)
        # The facet's README.md is the facet itself, never one of its entries.
        self.assertEqual(row['path'], 'Profile/Values/README.md')
        self.assertEqual((row['files'], row['entries'], row['substantive']), (2, 1, 1))
        self.assertEqual([entry['name'] for entry in row['entry_files']], ['Honesty.md'])
        self.assertIn('sections', row)

    def test_a_page_shaped_facet_names_its_sections_plainly(self) -> None:
        # A folder facet's README.md is a page: emoji section headings, and an opening section on what the
        # folder is for, which holds no fact about the owner and is never scored or asked about.
        self.vault.note('Profile/Values/README.md', body='# 🧭 VALUES\n\n## 💡 What This Folder Is For\n\n'
                                                          'Core values, ranked.\n\n## 📸 Snapshot\n\n'
                                                          'Honesty first.\n')
        sections = json.loads(self.vault.run(SCRIPT, 'Values', '--json').stdout)['sections']
        self.assertEqual([section['heading'] for section in sections], ['Snapshot'])
        self.assertEqual(sections[0]['substantive'], 1)

    def test_lines_in_the_generated_entries_block_do_not_count(self) -> None:
        self.vault.note('Profile/Goals/README.md', body='# Goals\n<!-- brain:profile-entries (x) -->\n- [[Profile/Goals/Run|Run]]\n'
                                                         '<!-- /brain:profile-entries -->\n')
        self.assertEqual(self.facet(self.report(), 'Goals')['substantive'], 0)

    def test_the_template_folder_counts_as_scaffold(self) -> None:
        self.vault.write('Profile/.template/Entry.md', '---\ntitle: x\n---\nDescribe the entry here.\n')
        self.vault.note('Profile/Skills/README.md', body='# Skills\n')
        self.vault.note('Profile/Skills/Cooking.md', body='# Cooking\nDescribe the entry here.\n')
        self.assertEqual(self.facet(self.report(), 'Skills')['substantive'], 0)

    def test_the_template_folders_readme_is_no_scaffold(self) -> None:
        # The README.md explains the scaffolds and is never copied, so its lines say nothing about an entry.
        self.vault.write('Profile/.template/README.md', '<!--\ntitle: x\n-->\nEach scaffold makes one entry.\n')
        self.vault.note('Profile/Skills/README.md', body='# Skills\n')
        self.vault.note('Profile/Skills/Cooking.md', body='# Cooking\nEach scaffold makes one entry.\n')
        self.assertEqual(self.facet(self.report(), 'Skills')['substantive'], 1)

    def test_working_style_leads_until_it_holds_something(self) -> None:
        self.vault.note('Profile/Biography.md', body='# Biography\nA real line.\n')
        self.assertEqual(self.report()['target'], 'Working Style')
        self.vault.note('Profile/Working Style.md', body='# Working Style\nMornings for deep work.\n')
        self.assertNotEqual(self.report()['target'], 'Working Style')

    def test_a_facet_by_name_and_an_unknown_one(self) -> None:
        self.assertEqual(self.vault.run(SCRIPT, 'working-style').returncode, 0)
        result = self.vault.run(SCRIPT, 'Hobbies')
        self.assertEqual(result.returncode, 2)
        self.assertIn('the facets are Working Style', result.stderr)

    def test_the_real_vault(self) -> None:
        result = fixtures.subprocess.run([sys.executable, str(fixtures.SCRIPTS / SCRIPT), '--json'],
                                         capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual([f['facet'] for f in report['facets']][:3], ['Working Style', 'Biography', 'Personality'])

    def test_the_blank_template_leads_with_working_style(self) -> None:
        if not (fixtures.SCRIPTS.parents[1] / '.github' / 'TEMPLATE_INIT').is_file():
            self.skipTest('only the template and a vault not yet initialised hold the blank facets')
        result = fixtures.subprocess.run([sys.executable, str(fixtures.SCRIPTS / SCRIPT), '--json'],
                                         capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        filled = [f['facet'] for f in report['facets'] if f['status'] != 'template']
        self.assertEqual(filled, [], 'a blank facet scores as filled; in the template, refreeze SCAFFOLD '
                                     'with --print-scaffold')
        self.assertEqual(report['target'], 'Working Style')


if __name__ == '__main__':
    unittest.main()
