#!/usr/bin/env python3
"""Tests for vault.py, the library every vault script shares.

WHY THIS EXISTS. Every check and generator reads notes through vault.py, so a
mistake in how it reads frontmatter, walks the folders, finds a wikilink or
redraws a block would spread to all of them at once. These tests pin each of
those down on small inputs, and on a throwaway vault where a folder is needed.

Run it:

    python3 .github/scripts/test_vault.py
"""

from __future__ import annotations

import pathlib
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fixtures  # noqa: E402
import vault  # noqa: E402


class TestFrontmatter(unittest.TestCase):
    def parse(self, block: str) -> dict:
        fields = vault.parse_frontmatter('---\n' + block + '\n---\n# Body\n')
        assert fields is not None
        return fields

    def test_a_note_without_frontmatter_has_none(self) -> None:
        self.assertIsNone(vault.parse_frontmatter('# Just a heading\n'))
        self.assertIsNone(vault.parse_frontmatter('---\ntitle: never closed\n'))

    def test_scalars_stay_strings_and_lose_their_quotes(self) -> None:
        fields = self.parse('title: "A \\"quoted\\" title"\nname: \'It\'\'s\'\nlayer: 2\npolicy: false\nplain: word # a comment')
        self.assertEqual(fields['title'], 'A "quoted" title')
        self.assertEqual(fields['name'], "It's")
        self.assertEqual(fields['layer'], '2')
        self.assertEqual(fields['policy'], 'false')
        self.assertEqual(fields['plain'], 'word')

    def test_flow_lists_respect_quotes_and_apostrophes(self) -> None:
        fields = self.parse('members: ["★ Lead", "Devil\'s Advocate", "A, B"]\ntags: [inbox, agent]\nempty: []')
        self.assertEqual(fields['members'], ['★ Lead', "Devil's Advocate", 'A, B'])
        self.assertEqual(fields['tags'], ['inbox', 'agent'])
        self.assertEqual(fields['empty'], [])

    def test_a_placeholder_in_brackets_inside_a_list_is_one_item(self) -> None:
        fields = self.parse('keywords: ["[synonym]", "[topic]", "template"]')
        self.assertEqual(fields['keywords'], ['[synonym]', '[topic]', 'template'])

    def test_a_flow_list_may_span_lines(self) -> None:
        fields = self.parse('members:\n  [\n    "One",\n    "Two",\n  ]\nlead: One')
        self.assertEqual(fields['members'], ['One', 'Two'])
        self.assertEqual(fields['lead'], 'One')

    def test_block_lists_and_nested_maps(self) -> None:
        fields = self.parse('tags:\n  - memory\n  - log\nmetadata:\n  team: Research\n  version: "01.05.00"\nafter: yes')
        self.assertEqual(fields['tags'], ['memory', 'log'])
        self.assertEqual(fields['metadata'], {'team': 'Research', 'version': '01.05.00'})
        self.assertEqual(fields['after'], 'yes')

    def test_a_flow_map(self) -> None:
        fields = self.parse("metadata: { 'team': 'Design', 'version': '02.00.00' }")
        self.assertEqual(fields['metadata'], {'team': 'Design', 'version': '02.00.00'})

    def test_folded_and_literal_scalars(self) -> None:
        fields = self.parse('folded: >-\n  one\n  two\nliteral: |\n  first\n  second\nnext: x')
        self.assertEqual(fields['folded'], 'one two')
        self.assertEqual(fields['literal'], 'first\nsecond')
        self.assertEqual(fields['next'], 'x')

    def test_an_empty_value_is_empty(self) -> None:
        self.assertEqual(self.parse('aliases:\nkeywords: []')['aliases'], '')

    def test_a_dashed_line_in_a_value_does_not_close_the_block(self) -> None:
        fields = vault.parse_frontmatter('---\ndescription: "a --- b"\n---\nbody\n')
        self.assertEqual(fields, {'description': 'a --- b'})

    def test_crlf_line_ends(self) -> None:
        fields = vault.parse_frontmatter('---\r\ntitle: x\r\ntags: [a]\r\n---\r\nbody\r\n')
        self.assertEqual(fields, {'title': 'x', 'tags': ['a']})

    def test_body_start_skips_the_closing_line(self) -> None:
        text = '---\ntitle: x\n---\n# Body\n'
        self.assertEqual(text[vault.body_start(text):], '# Body\n')
        self.assertEqual(vault.body_start('# none\n'), 0)


class TestWikilinks(unittest.TestCase):
    def test_targets_lose_alias_heading_and_block(self) -> None:
        self.assertEqual(vault.wikilinks('[[A|alias]] [[B#Heading]] [[C#^block]] ![[D.png]]'), ['A', 'B', 'C', 'D.png'])

    def test_code_and_comments_hold_no_links(self) -> None:
        text = '`[[inline]]`\n```\n[[fenced]]\n```\n%% [[hidden]] %%\n[[real]]'
        self.assertEqual(vault.wikilinks(text), ['real'])

    def test_a_table_escaped_pipe(self) -> None:
        self.assertEqual(vault.wikilinks('| [[Note\\|Alias]] |'), ['Note'])


class TestBlocks(unittest.TestCase):
    TEXT = 'before\n<!-- brain:children (old note) -->\n- old\n<!-- /brain:children -->\nafter\n'

    def test_redraw_replaces_the_inside_and_the_note(self) -> None:
        drawn = vault.redraw_block(self.TEXT, 'children', '- new')
        self.assertEqual(drawn, f'before\n<!-- brain:children ({vault.BLOCK_NOTE}) -->\n- new\n<!-- /brain:children -->\nafter\n')

    def test_a_missing_block_is_none(self) -> None:
        self.assertIsNone(vault.redraw_block('no block\n', 'children', '- x'))
        self.assertFalse(vault.has_block('no block\n', 'children'))

    def test_a_name_never_matches_a_longer_one(self) -> None:
        text = '<!-- brain:children-extra -->\nx\n<!-- /brain:children-extra -->\n'
        self.assertFalse(vault.has_block(text, 'children'))


class TestLayout(unittest.TestCase):
    def setUp(self) -> None:
        self.vault = fixtures.Vault()

    def tearDown(self) -> None:
        self.vault.cleanup()

    def test_the_walk_skips_hidden_folders_but_not_scaffolds(self) -> None:
        for rel in ('A.md', 'Library/B.md', 'Library/.template/C.md', '.github/D.md', 'System/Backups/E.md',
                    'Memory/.hidden.md', 'Memory/F.txt'):
            self.vault.write(rel, 'x')
        notes = [vault.rel(self.vault.root, p) for p in vault.walk_notes(self.vault.root)]
        self.assertEqual(notes, ['A.md', 'Library/B.md', 'Library/.template/C.md'])
        self.assertTrue(vault.in_walk(self.vault.root, self.vault.path('Library/.template/C.md')))
        self.assertFalse(vault.in_walk(self.vault.root, self.vault.path('.github/D.md')))

    def test_startup_notes_run_stable_before_volatile(self) -> None:
        self.vault.note('Memory/Context/Context.md', tags=['memory', 'information', 'startup'], layer=2)
        self.vault.note('Memory/Log.md', tags=['memory', 'information', 'startup'], layer=1)
        self.vault.note('Profile/Values/Values.md', tags=['profile', 'information', 'startup'], layer=2)
        self.vault.note('System/System.md', tags=['system', 'information', 'startup'], layer=1)
        self.vault.note('Profile/Working Style.md', tags=['profile', 'information', 'startup'], layer=1)
        self.vault.note('Profile/Other.md')
        names = [vault.rel(self.vault.root, p) for p in vault.startup_notes(self.vault.root)]
        self.assertEqual(names, ['Profile/Working Style.md', 'System/System.md', 'Memory/Log.md',
                                 'Profile/Values/Values.md', 'Memory/Context/Context.md'])

    def test_pages_are_not_notes(self) -> None:
        # AGENTS.md and the top folders' READMEs are GitHub pages, never walked as notes.
        for rel in ('AGENTS.md', 'Memory/README.md', 'Memory/Memory.md'):
            self.vault.write(rel, 'x')
        notes = [vault.rel(self.vault.root, p) for p in vault.walk_notes(self.vault.root)]
        self.assertEqual(notes, ['Memory/Memory.md'])

    def test_only_the_top_folders_carry_a_readme(self) -> None:
        for rel in ('README.md', 'Memory/README.md', 'Memory/Context/README.md', '.github/README.md',
                    'Memory/.template/README.md'):
            self.vault.write(rel, 'x')
        strays = [vault.rel(self.vault.root, p) for p in vault.stray_readmes(self.vault.root)]
        self.assertEqual(strays, ['README.md', 'Memory/.template/README.md', 'Memory/Context/README.md'])

    def test_inbox_drops_leave_the_kept_homes_alone(self) -> None:
        for rel in ('Inbox/Inbox.md', 'Inbox/drop.pdf', 'Inbox/Reports/r.md', 'Inbox/Faculties/f.md', 'Inbox/sub/x.md'):
            self.vault.write(rel, 'x')
        drops = [vault.rel(self.vault.root, p) for p in vault.inbox_drops(self.vault.root)]
        self.assertEqual(drops, ['Inbox/drop.pdf', 'Inbox/sub/x.md'])

    def test_a_home_with_its_own_roster_is_one_team(self) -> None:
        self.vault.note('Library/Library.md', members=['★ Librarian'])
        self.vault.note('Library/★ Librarian.md')
        self.vault.note('Inbox/Faculties/Faculties.md')
        self.vault.note('Inbox/Faculties/Research/Research.md', members=['★ Lead'])
        self.vault.note('Inbox/Faculties/Research/★ Lead.md')
        library, faculties = self.vault.path('Library'), self.vault.path('Inbox/Faculties')
        self.assertEqual(vault.team_dirs(library), [library])
        self.assertEqual([p.name for p, _t in vault.agent_files(library)], ['★ Librarian.md'])
        self.assertEqual([t for _p, t in vault.roster_files(faculties)], ['Research'])
        self.assertEqual(vault.find_roster(self.vault.root, 'Research'), faculties / 'Research' / 'Research.md')
        self.assertIsNone(vault.find_roster(self.vault.root, 'Missing'))


class TestReport(unittest.TestCase):
    def test_findings_set_the_exit_code(self) -> None:
        report = vault.Report(pathlib.Path('/vault'), quiet=True)
        self.assertEqual(report.finish('fine'), 0)
        report.error(pathlib.Path('/vault/a.md'), 'broken', 3)
        self.assertEqual(report.errors, ['a.md:3: broken'])


if __name__ == '__main__':
    unittest.main()
