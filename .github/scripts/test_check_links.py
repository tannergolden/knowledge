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
        self.vault.write('Memory/Memory.md', '# Memory\n')
        self.vault.write('Memory/Log.md', '# Log\n')
        self.vault.write('Memory/Events/Events.md', '# Events\n')
        self.vault.write('Memory/Events/Party.md', '# Party\n')

    def tearDown(self) -> None:
        self.vault.cleanup()

    def check(self):
        return self.vault.run(SCRIPT)

    def test_a_folder_note_links_its_files_and_its_subfolders_notes(self) -> None:
        self.vault.write('Memory/Memory.md', '[[Log]] [[Memory/Events/Events|Events]]\n')
        self.vault.write('Memory/Events/Events.md', '[[Memory/Events/Party|Party]]\n')
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn('All 3 wikilinks resolve', result.stdout)

    def test_a_broken_link(self) -> None:
        self.vault.write('Memory/Memory.md', '[[Nowhere]]\n')
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn('[[Nowhere]] resolves to no file', result.stdout)

    def test_a_content_note_links_nothing(self) -> None:
        self.vault.write('Memory/Log.md', 'see [[Memory]]\n')
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn('carries no wikilinks', result.stdout)

    def test_a_folder_note_may_not_skip_a_level(self) -> None:
        self.vault.write('Memory/Memory.md', '[[Memory/Events/Party|Party]]\n')
        self.assertIn("a folder's note links the files in its folder", self.check().stdout)

    def test_the_root_chain(self) -> None:
        self.vault.write('AGENTS.md', '[[Instructions]]\n')
        self.vault.write('Instructions.md', '[[Constitution]] [[Memory/Memory|Memory]]\n')
        self.vault.write('Constitution.md', '# Constitution\n')
        self.assertEqual(self.check().returncode, 0)
        self.vault.write('Constitution.md', '[[AGENTS]]\n')
        self.assertIn('the root carries one chain', self.check().stdout)

    def test_a_link_back_up_the_tree_fails(self) -> None:
        # Links flow downhill: a folder note links its children, and a child never links its parent.
        self.vault.write('Memory/Memory.md', '[[Memory/Events/Events|Events]]\n')
        self.vault.write('Memory/Events/Events.md', '[[Memory/Events/Party|Party]] [[Memory/Memory|Memory]]\n')
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("a folder's note links the files in its folder", result.stdout)

    def test_links_inside_code_or_comments_do_not_count(self) -> None:
        self.vault.write('Memory/Log.md', '`[[Memory]]` and %% [[Memory]] %%\n')
        self.assertEqual(self.check().returncode, 0)

    def test_a_link_into_a_scaffold(self) -> None:
        self.vault.write('Memory/.template/Entry.md', '# Entry\n')
        self.vault.write('Memory/Memory.md', '[[Entry]]\n')
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn('links a scaffold', result.stdout)

    def test_an_ambiguous_link_warns(self) -> None:
        self.vault.write('Memory/Party.md', '# another party\n')
        self.vault.write('Memory/Memory.md', '[[party]]\n')
        result = self.check()
        self.assertIn('matches 2 files', result.stdout)

    def test_a_link_to_a_binary_resolves(self) -> None:
        self.vault.write('Memory/photo.png', 'png')
        self.vault.write('Memory/Memory.md', '![[photo.png]]\n')
        self.assertEqual(self.check().returncode, 0)

    def test_the_real_vault(self) -> None:
        result = fixtures.subprocess.run([sys.executable, str(fixtures.SCRIPTS / SCRIPT)],
                                         capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main()
