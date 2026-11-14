#!/usr/bin/env python3
"""Tests for check-links.py, the wikilink graph check.

WHY THIS EXISTS. The hub topology is the vault's shape in Obsidian: which note
may link which. A rule check-links.py gets wrong would either let the graph
rot or fail a vault that is fine. Each test builds a small vault with just the
links it needs and runs the real script on it; the last runs it, read only,
on the vault this repository holds.

Run it:

    python3 .github/scripts/test_check_links.py
"""

from __future__ import annotations

import pathlib
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fixtures  # noqa: E402

SCRIPT = 'check-links.py'


class TestCheckLinks(unittest.TestCase):
    def setUp(self) -> None:
        self.vault = fixtures.Vault()
        self.vault.write('Memory/README.md', '# Memory\n')
        self.vault.write('Memory/Log.md', '# Log\n')
        self.vault.write('Memory/Events/README.md', '# Events\n')
        self.vault.write('Memory/Events/Party.md', '# Party\n')

    def tearDown(self) -> None:
        self.vault.cleanup()

    def check(self):
        return self.vault.run(SCRIPT)

    def test_a_folders_readme_links_its_files_and_its_subfolders_readmes(self) -> None:
        self.vault.write('Memory/README.md', '[[Log]] [[Memory/Events/README|Events]]\n')
        self.vault.write('Memory/Events/README.md', '[[Memory/Events/Party|Party]]\n')
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn('All 3 wikilinks resolve', result.stdout)

    def test_a_broken_link(self) -> None:
        self.vault.write('Memory/README.md', '[[Nowhere]]\n')
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn('[[Nowhere]] resolves to no file', result.stdout)

    def test_a_link_to_a_folders_old_namesake_resolves_to_nothing(self) -> None:
        # A folder's note is its README.md, so a link still naming Events/Events is broken.
        self.vault.write('Memory/README.md', '[[Memory/Events/Events|Events]]\n')
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn('[[Memory/Events/Events]] resolves to no file', result.stdout)

    def test_a_content_note_links_nothing(self) -> None:
        self.vault.write('Memory/Log.md', 'see [[Memory/README|Memory]]\n')
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn('carries no wikilinks', result.stdout)

    def test_a_folders_readme_may_not_skip_a_level(self) -> None:
        self.vault.write('Memory/README.md', '[[Memory/Events/Party|Party]]\n')
        self.assertIn("a folder's README.md links the files in its folder", self.check().stdout)

    def test_the_root_holds_no_notes_and_its_pages_are_not_walked(self) -> None:
        # The root's README.md and a hidden folder's README.md are pages: never walked, so
        # their links are Markdown links the topology does not govern.
        self.vault.write('README.md', '[Memory](Memory/README.md) [[Memory/Events/Party|Party]]\n')
        self.vault.write('.github/README.md', '[[Memory/Events/Party|Party]]\n')
        self.assertEqual(self.check().returncode, 0)
        self.vault.write('Notes.md', '[[Memory/README|Memory]]\n')
        self.assertIn('the vault root holds no notes', self.check().stdout)

    def test_a_link_back_up_the_tree_fails(self) -> None:
        # Links flow downhill: a folder's README links its children, and a child never links its parent.
        self.vault.write('Memory/README.md', '[[Memory/Events/README|Events]]\n')
        self.vault.write('Memory/Events/README.md', '[[Memory/Events/Party|Party]] [[Memory/README|Memory]]\n')
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("a folder's README.md links the files in its folder", result.stdout)

    def test_links_inside_code_or_comments_do_not_count(self) -> None:
        self.vault.write('Memory/Log.md', '`[[Memory]]` and %% [[Memory]] %%\n')
        self.assertEqual(self.check().returncode, 0)

    def test_a_link_into_a_scaffold(self) -> None:
        self.vault.write('Memory/.template/Entry.md', '# Entry\n')
        self.vault.write('Memory/.template/README.md', '# Memory templates\n')
        self.vault.write('Memory/README.md', '[[Entry]]\n')
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn('links a scaffold', result.stdout)
        # A scaffold folder's README.md is a scaffold too: no link reaches it by its path.
        self.vault.write('Memory/README.md', '[[Memory/.template/README|Templates]]\n')
        self.assertIn('links a scaffold', self.check().stdout)

    def test_a_file_waiting_at_the_inbox_links_whatever_it_likes(self) -> None:
        # An export from another app arrives full of wikilinks; it is not a note until it is sorted.
        self.vault.write('Inbox/README.md', '# Inbox\n')
        self.vault.write('Inbox/export.md', 'See [[Nowhere]] and [[Memory/Log|the log]].\n')
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn('All 0 wikilinks resolve', result.stdout)

    def test_plain_paths_that_name_what_is_there_pass(self) -> None:
        self.vault.write('Memory/Events/Party.md', '# Party\n\nSee `Memory/Log.md` and `Memory/Events/`.\n\n'
                         '- Related: Memory/Log.md\n- Related: `Memory/Events/README.md` (its folder)\n')
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn('all 4 plain paths name a file or a folder.', result.stdout)

    def test_a_related_line_to_a_file_that_is_not_there_fails(self) -> None:
        self.vault.write('Memory/Events/Party.md', '# Party\n\n- Related: Memory/Entities/People/Dana Smith.md\n')
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn('error: Memory/Events/Party.md:3: `Memory/Entities/People/Dana Smith.md` names no file', result.stdout)

    def test_a_rename_leaves_no_plain_path_behind(self) -> None:
        # A wikilink follows a rename in an editor that knows them; a plain path never does.
        self.vault.write('Memory/Entities/People/Dana Smith.md', '# Dana\n')
        self.vault.write('Memory/Events/Party.md', '# Party\n\nRelated: Memory/Entities/People/Dana Smith.md\n')
        self.assertEqual(self.check().returncode, 0)
        self.vault.path('Memory/Entities/People/Dana Smith.md').rename(self.vault.path('Memory/Entities/People/Dana Jones.md'))
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn('Memory/Events/Party.md:3: `Memory/Entities/People/Dana Smith.md` names no file', result.stdout)

    def test_a_path_in_backticks_from_a_top_folder_is_checked(self) -> None:
        self.vault.write('Memory/Log.md', '# Log\n\nSee `Memory/Gone.md`, `Memory/Nowhere/` and `Memory/log.md`.\n')
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn('Memory/Log.md:3: `Memory/Gone.md` names no file', result.stdout)
        self.assertIn('Memory/Log.md:3: `Memory/Nowhere/` names no folder', result.stdout)
        # The case is read as written, so a path that only a case-folding disk would find fails everywhere.
        self.assertIn('Memory/Log.md:3: `Memory/log.md` names no file', result.stdout)
        self.assertIn('3 problems.', result.stderr)

    def test_what_is_not_a_reference_is_passed_by(self) -> None:
        # A pattern to fill in, an example in a fenced block, a path from the note's own folder or from a
        # hidden one, a word in code, and the two folders the vault makes when it first needs them.
        self.vault.write('Memory/Log.md', '# Log\n\n`Ventures/[Company]/Overview.md` `Memory/Entities/People/<First Last>.md` '
                         '`Memory/Decisions/YYYY-MM-slug.md` `Library/*.md`\n\n```txt\nRelated: Memory/Decisions/2026-05-gone.md\n```\n\n'
                         '`Gone.md` `Events/` `.docs/Gone.md` `Memory/Gone` `update-vault.py`\n\n'
                         '`Inbox/Backups/` `Memory/Context/Archive/2026/`\n\n- Related: [the plain path of a related entry]\n')
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn('all 2 plain paths name a file or a folder.', result.stdout)
        # A file in the archive is a reference like any other: only the year's folder is made on demand.
        self.vault.write('Memory/Log.md', '# Log\n\n`Memory/Context/Archive/2026/20260101-090000.md`\n')
        self.assertEqual(self.check().returncode, 1)

    def test_a_scaffold_is_not_read_for_plain_paths(self) -> None:
        self.vault.write('Memory/.template/Event.md', '# [Event]\n\n- Related: Memory/Entities/People/Gone.md\n')
        self.assertEqual(self.check().returncode, 0)

    def test_an_ambiguous_link_warns(self) -> None:
        self.vault.write('Memory/Party.md', '# another party\n')
        self.vault.write('Memory/README.md', '[[party]]\n')
        result = self.check()
        self.assertIn('matches 2 files', result.stdout)

    def test_a_link_to_a_binary_resolves(self) -> None:
        self.vault.write('Memory/photo.png', 'png')
        self.vault.write('Memory/README.md', '![[photo.png]]\n')
        self.assertEqual(self.check().returncode, 0)

    def test_the_real_vault(self) -> None:
        result = fixtures.subprocess.run([sys.executable, str(fixtures.SCRIPTS / SCRIPT)],
                                         capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main()
