#!/usr/bin/env python3
"""Tests for check-ignored.py, the check for vault files a rule written for code keeps out of git.

WHY THIS EXISTS. A file git ignores is never committed, and nothing says so:
the status stays clean while the file lives on one machine only. The check
that catches it must fail on the folders and files the template's inherited
rules hide, and stay quiet about everything hidden on purpose: the vault's
own rules, a folder's own .gitignore, and junk. Each test builds a small
vault with a .gitignore shaped like the real one and runs the real script on
it.

Run it:

    python3 .github/scripts/test_check_ignored.py
"""

from __future__ import annotations

import pathlib
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fixtures  # noqa: E402

SCRIPT = 'check-ignored.py'
ROOT = fixtures.SCRIPTS.parents[1]
SECTION = '# --- BRAIN Vault ---'
# The real file's shape: rules inherited for code first, then the vault's own below its line.
IGNORE = f'build/\ndist/\ntest-results/\n*.zip\n*.key\nnode_modules/\n\n{SECTION}\n*.zim\nSystem/Backups/\n'


class TestCheckIgnored(unittest.TestCase):
    def setUp(self) -> None:
        self.vault = fixtures.Vault()
        self.vault.write('.gitignore', IGNORE)
        self.vault.note('Memory/README.md')

    def tearDown(self) -> None:
        self.vault.cleanup()

    def check(self, files: dict[str, str]):
        for rel, text in files.items():
            self.vault.write(rel, text)
        self.vault.init_git()
        return self.vault.run(SCRIPT)

    def test_a_vault_with_nothing_ignored_passes(self) -> None:
        result = self.check({'Projects/Kitchen/Plan.md': 'x'})
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('git ignores nothing the vault keeps.', result.stdout)

    def test_a_folder_or_file_an_inherited_rule_hides_fails(self) -> None:
        result = self.check({'Profile/Health/test-results/panel.md': 'x', 'Inbox/statements.zip': 'x',
                             'Ventures/Acme/Pitch-Deck.key': 'x', 'Projects/Kitchen/build/Timeline.md': 'x'})
        self.assertEqual(result.returncode, 1)
        # A wholly ignored folder is one finding, named with the rule that hides it.
        self.assertIn('error: Profile/Health/test-results/: git ignores it (.gitignore:3: test-results/)', result.stdout)
        self.assertIn('error: Inbox/statements.zip: git ignores it (.gitignore:4: *.zip)', result.stdout)
        self.assertIn('error: Ventures/Acme/Pitch-Deck.key: git ignores it (.gitignore:5: *.key)', result.stdout)
        self.assertIn('error: Projects/Kitchen/build/: git ignores it (.gitignore:1: build/)', result.stdout)
        self.assertIn('4 problems.', result.stderr)

    def test_what_the_vaults_own_rules_hide_is_meant(self) -> None:
        result = self.check({'Library/Reference & Encyclopedia/wikipedia_2026-01.zim': 'x', 'System/Backups/old.md': 'x'})
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_a_folders_own_gitignore_is_its_owners_choice(self) -> None:
        # A code project brings its own .gitignore; the same folder name without one is a finding.
        result = self.check({'Projects/Site/Code/.gitignore': 'dist/\n', 'Projects/Site/Code/dist/app.js': 'x',
                             'Projects/Shed/dist/Parts.md': 'x'})
        self.assertEqual(result.returncode, 1)
        self.assertNotIn('Projects/Site', result.stdout)
        self.assertIn('error: Projects/Shed/dist/: git ignores it (.gitignore:2: dist/)', result.stdout)

    def test_junk_is_left_alone(self) -> None:
        # The junk rules sit above the section line, among the inherited ones, as in the real file.
        result = self.check({'.gitignore': '.DS_Store\n__pycache__/\n*.pyc\n*.swp\n.venv\n' + IGNORE, 'Projects/.DS_Store': 'x',
                             'Projects/Site/__pycache__/a.pyc': 'x', 'Projects/Site/node_modules/pad/README.md': 'x',
                             'Projects/Site/.venv/bin/python': 'x', 'Memory/.Log.md.swp': 'x', 'Memory/notes.swp': 'x'})
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_only_the_seven_top_folders_are_its_business(self) -> None:
        result = self.check({'.assets/kit.zip': 'x', 'export.zip': 'x'})
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_a_gitignore_without_the_section_line_is_inherited_throughout(self) -> None:
        result = self.check({'.gitignore': '*.zim\n', 'Library/works.zim': 'x'})
        self.assertEqual(result.returncode, 1)
        self.assertIn('error: Library/works.zim: git ignores it (.gitignore:1: *.zim)', result.stdout)

    def test_outside_a_checkout_there_is_nothing_to_check(self) -> None:
        self.vault.write('Inbox/statements.zip', 'x')
        result = self.vault.run(SCRIPT)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('Not a git checkout', result.stdout)

    def test_the_real_vault(self) -> None:
        result = fixtures.subprocess.run([sys.executable, str(fixtures.SCRIPTS / SCRIPT)],
                                         capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_the_real_gitignore_keeps_its_section_line(self) -> None:
        # The check tells the inherited rules from the vault's own by this line, in both files.
        self.assertIn(f'\n{SECTION}\n', (ROOT / '.gitignore').read_text(encoding='utf-8'))
        self.assertIn(f"VAULT_SECTION = '{SECTION}'", (fixtures.SCRIPTS / SCRIPT).read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
