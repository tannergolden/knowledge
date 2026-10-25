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
        self.assertIn('No personal numbers in 1 tracked files.', result.stdout)

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
        result = self.scan({'System/Data/agent-catalog.json': f'{{"seed": {CARD}}}\n'})
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_only_tracked_files_count(self) -> None:
        self.scan({'Memory/Log.md': 'clean\n'})
        self.vault.write('Memory/Draft.md', f'{SSN}\n')
        self.assertEqual(self.vault.run(SCRIPT).returncode, 0)

    def test_the_real_vault_is_clean(self) -> None:
        result = fixtures.subprocess.run([sys.executable, str(fixtures.SCRIPTS / SCRIPT)],
                                         capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main()
