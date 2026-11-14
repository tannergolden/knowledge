#!/usr/bin/env python3
"""Tests for scan-pii.py, the personal number scan.

WHY THIS EXISTS. The scan is the one check that keeps a Social Security or
card number out of a vault that lives on GitHub, and it must not cry wolf on
every long number either. The tests build every sample number from pieces at
run time, so this file never holds one whole and the scan of the real vault,
the last test, stays clean.

Run it:

    python3 .github/scripts/test_scan_pii.py
"""

from __future__ import annotations

import pathlib
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fixtures  # noqa: E402

SCRIPT = 'scan-pii.py'
SSN = '-'.join(('123', '45', '6789'))
CARD = '4111' + '1111' * 3          # passes the Luhn check
NOT_A_CARD = '4111' + '1111' * 2 + '1112'  # fails it
GROUPS = ('4111', '1111', '1111', '1111')   # the same card, as people write it


class TestScanPii(unittest.TestCase):
    def setUp(self) -> None:
        self.vault = fixtures.Vault()

    def tearDown(self) -> None:
        self.vault.cleanup()

    def scan(self, files: dict[str, str]):
        for rel, text in files.items():
            self.vault.write(rel, text)
        self.vault.init_git()
        return self.vault.run(SCRIPT)

    def test_a_clean_vault_passes(self) -> None:
        result = self.scan({'Memory/Log.md': 'Nothing personal here.\n'})
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn('No personal numbers in 1 files.', result.stdout)

    def test_a_social_security_number(self) -> None:
        result = self.scan({'Profile/Biography.md': f'Mine is {SSN}.\n'})
        self.assertEqual(result.returncode, 1)
        self.assertIn('Profile/Biography.md:1: looks like a Social Security number', result.stdout)

    def test_a_card_number_only_when_it_passes_luhn(self) -> None:
        result = self.scan({'Memory/Log.md': f'card {CARD}\nrecord {NOT_A_CARD}\n'})
        self.assertEqual(result.returncode, 1)
        self.assertIn('Memory/Log.md:1: looks like a payment card number', result.stdout)
        self.assertNotIn('Memory/Log.md:2', result.stdout)

    def test_the_full_value_is_never_printed(self) -> None:
        result = self.scan({'Memory/Log.md': f'{CARD}\n'})
        self.assertNotIn(CARD, result.stdout + result.stderr)

    def test_the_allow_marker(self) -> None:
        result = self.scan({'Memory/Log.md': f'{SSN} <!-- pii-allow: a published example -->\n'})
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_machine_json_skips_the_number_checks(self) -> None:
        result = self.scan({'System/Data/layout.json': f'{{"seed": {CARD}}}\n'})
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_a_card_number_written_in_groups(self) -> None:
        spaced, dashed = ' '.join(GROUPS), '-'.join(GROUPS)
        amex = ' '.join(('3782', '822463', '10005'))
        result = self.scan({'Memory/Log.md': f'card {spaced}\ncard {dashed}\ncard {amex}\n'})
        self.assertEqual(result.returncode, 1)
        for line in (1, 2, 3):
            self.assertIn(f'Memory/Log.md:{line}: looks like a payment card number', result.stdout)
        self.assertNotIn(spaced, result.stdout + result.stderr)

    def test_grouped_digits_that_fail_luhn_pass(self) -> None:
        not_a_card = ' '.join(GROUPS[:3] + ('1112',))
        result = self.scan({'Memory/Log.md': f'order {not_a_card}\nyears 2023 2024 2025 2026\n'})
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_a_new_note_is_scanned_before_it_is_staged(self) -> None:
        # A note is untracked until it is staged, which is when the documented order runs the check.
        self.scan({'Memory/Log.md': 'clean\n'})
        self.vault.write('Memory/Draft.md', f'{SSN}\n')
        result = self.vault.run(SCRIPT)
        self.assertEqual(result.returncode, 1)
        self.assertIn('Memory/Draft.md:1: looks like a Social Security number', result.stdout)

    def test_an_ignored_file_is_not_scanned(self) -> None:
        self.scan({'Memory/Log.md': 'clean\n', '.gitignore': 'scratch/\n'})
        self.vault.write('scratch/Draft.md', f'{SSN}\n')
        self.assertEqual(self.vault.run(SCRIPT).returncode, 0)

    def test_a_saved_visual_is_read_as_its_reader_sees_it(self) -> None:
        # Tags, scripts and styles hold coordinates and data; the text between them is what a person reads.
        spaced = ' '.join(GROUPS)
        drawing = f'<svg viewBox="0 0 {spaced}"><path d="M{spaced} L{SSN}"/><script>var seed = {CARD};</script></svg>\n'
        self.assertEqual(self.scan({'Inbox/Visuals/Chart.svg': drawing}).returncode, 0)
        result = self.scan({'Inbox/Visuals/Chart.svg': f'<svg>\n<text x="1">{spaced}</text>\n</svg>\n',
                            'Inbox/Visuals/Board.html': f'<p>\n<b>ID</b> {SSN}</p>\n'})
        self.assertEqual(result.returncode, 1)
        self.assertIn('Inbox/Visuals/Chart.svg:2: looks like a payment card number', result.stdout)
        self.assertIn('Inbox/Visuals/Board.html:2: looks like a Social Security number', result.stdout)

    def test_the_allow_marker_in_a_page_of_markup(self) -> None:
        result = self.scan({'Inbox/Visuals/Board.html': f'<p>{SSN}</p> <!-- pii-allow: a published example -->\n'})
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_the_real_vault_is_clean(self) -> None:
        result = fixtures.subprocess.run([sys.executable, str(fixtures.SCRIPTS / SCRIPT)],
                                         capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main()
