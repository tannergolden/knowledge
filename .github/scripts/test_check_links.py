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
