#!/usr/bin/env python3
"""Tests for knowledge-base.py, the offline reference works.

WHY THIS EXISTS. The knowledge base downloads gigabytes and edits the committed
source list, so the parts that decide what it downloads and installs must be
right without anyone watching: which build is newest, whether a download
matches its checksum, which names are safe to turn into files, and that a
broken source list stops it instead of being replaced. These run without the
network and without libzim, which CI has neither of.

Run it:

    python3 .github/scripts/test_knowledge_base.py
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import pathlib
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fixtures  # noqa: E402

SCRIPT = 'knowledge-base.py'
SOURCES = 'Library/Reference & Encyclopedia/sources.json'
spec = importlib.util.spec_from_file_location('knowledge_base', fixtures.SCRIPTS / SCRIPT)
kb = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(kb)


class TestKnowledgeBase(unittest.TestCase):
    def setUp(self) -> None:
        self.vault = fixtures.Vault()
        self.vault.write(SOURCES, json.dumps({'sources': [
            {'name': 'wikipedia-simple', 'prefix': 'wikipedia_en_simple_all_nopic',
             'base': 'https://download.kiwix.org/zim/wikipedia/', 'enabled': False, 'note': 'small'},
            {'name': 'bad/name', 'prefix': 'x', 'base': 'https://example.org/', 'enabled': False},
        ]}, indent=2) + '\n')

    def tearDown(self) -> None:
        self.vault.cleanup()

    def test_list_shows_every_source_off(self) -> None:
        result = self.vault.run(SCRIPT, 'list')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('[off] wikipedia-simple', result.stdout)
        self.assertIn('No knowledge bases are installed', result.stdout)

    def test_enable_and_disable_edit_only_the_flag(self) -> None:
        self.assertEqual(self.vault.run(SCRIPT, 'enable', 'wikipedia-simple').returncode, 0)
        data = json.loads(self.vault.read(SOURCES))
        self.assertTrue(data['sources'][0]['enabled'])
        self.assertEqual(data['sources'][0]['note'], 'small')
        self.vault.run(SCRIPT, 'disable', 'wikipedia-simple')
        self.assertFalse(json.loads(self.vault.read(SOURCES))['sources'][0]['enabled'])
        self.assertEqual(self.vault.run(SCRIPT, 'enable', 'nope').returncode, 2)

    def test_a_broken_source_list_stops_everything(self) -> None:
        self.vault.write(SOURCES, '{ not json')
        result = self.vault.run(SCRIPT, 'list')
        self.assertEqual(result.returncode, 1)
        self.assertIn('cannot be read', result.stderr)
        self.assertEqual(self.vault.read(SOURCES), '{ not json')

    def test_refresh_with_nothing_on_does_nothing(self) -> None:
        result = self.vault.run(SCRIPT, 'refresh')
        self.assertEqual(result.returncode, 0)
        self.assertIn('No source is on', result.stderr)

    def test_an_unsafe_name_is_refused_before_any_download(self) -> None:
        result = self.vault.run(SCRIPT, 'refresh', 'bad/name')
        self.assertEqual(result.returncode, 1)
        self.assertIn('hold only letters, digits', result.stderr)

    def test_search_without_any_work_installed(self) -> None:
        result = self.vault.run(SCRIPT, 'search', 'photosynthesis')
        self.assertEqual(result.returncode, 0)
        self.assertIn('No knowledge bases are installed', result.stdout)

    def test_search_without_libzim_says_how_to_add_it(self) -> None:
        if kb.reader() is not None:
            self.skipTest('libzim is installed here')
        self.vault.write('Library/Reference & Encyclopedia/wikipedia-simple_2026-05.zim', 'not really')
        result = self.vault.run(SCRIPT, 'search', 'x')
        self.assertEqual(result.returncode, 1)
        self.assertIn('pip install --user libzim', result.stderr)

    def test_the_newest_build_in_a_listing(self) -> None:
        listing = ('<a href="wikipedia_en_simple_all_nopic_2025-11.zim">x</a>'
                   '<a href="wikipedia_en_simple_all_nopic_2026-02.zim">x</a>'
                   '<a href="other_wikipedia_en_simple_all_nopic_2027-01.zim">x</a>')
        self.assertEqual(kb.newest('wikipedia_en_simple_all_nopic', listing), 'wikipedia_en_simple_all_nopic_2026-02.zim')
        self.assertIsNone(kb.newest('wiktionary_en_all', listing))

    def test_a_download_installs_only_when_its_checksum_matches(self) -> None:
        source = self.vault.write('source.bin', 'payload')
        url = source.as_uri()
        good = hashlib.sha256(b'payload').hexdigest()
        kb.download(url, self.vault.path('good.zim'), good)
        self.assertEqual(self.vault.read('good.zim'), 'payload')
        with self.assertRaises(kb.Problem):
            kb.download(url, self.vault.path('bad.zim'), '0' * 64)
        self.assertFalse(self.vault.path('bad.zim').exists())

    def test_the_real_source_list_ships_every_source_off(self) -> None:
        data = json.loads((fixtures.SCRIPTS.parents[1] / SOURCES).read_text(encoding='utf-8'))
        self.assertEqual([s['name'] for s in data['sources'] if s.get('enabled')], [])


if __name__ == '__main__':
    unittest.main()
