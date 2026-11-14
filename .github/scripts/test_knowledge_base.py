#!/usr/bin/env python3
"""Tests for knowledge-base.py, the offline reference works.

WHY THIS EXISTS. The knowledge base downloads gigabytes and edits the committed
source list, so the parts that decide what it downloads and installs must be
right without anyone watching: which build is newest, whether a download
matches its checksum, which names are safe to turn into files, and that a
broken source list stops it instead of being replaced. These run without the
network and without libzim, which CI has neither of. Search and read are run
against stand-ins for libzim, under both generations of its calls, since
nothing else runs them where libzim is absent: when libzim 4 renamed those
calls, every search found nothing and no test said so.

Run it:

    python3 .github/scripts/test_knowledge_base.py
"""

from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import json
import pathlib
import sys
import unittest
import urllib.error

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
            {'name': 'wikipedia-simple', 'prefix': 'wikipedia_en-simple_all_nopic',
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
        # Names as Kiwix lists them: the simple English build carries a hyphen, wikipedia_en-simple.
        listing = ('<a href="wikipedia_en-simple_all_nopic_2025-11.zim">x</a>'
                   '<a href="wikipedia_en-simple_all_nopic_2026-02.zim">x</a>'
                   '<a href="wikipedia_en_all_nopic_2026-06.zim">x</a>'
                   '<a href="other_wikipedia_en-simple_all_nopic_2027-01.zim">x</a>')
        self.assertEqual(kb.newest('wikipedia_en-simple_all_nopic', listing), 'wikipedia_en-simple_all_nopic_2026-02.zim')
        self.assertEqual(kb.newest('wikipedia_en_all_nopic', listing), 'wikipedia_en_all_nopic_2026-06.zim')
        self.assertIsNone(kb.newest('wiktionary_en_all', listing))
        # The name the list carried before, with an underscore, matches nothing Kiwix lists.
        self.assertIsNone(kb.newest('wikipedia_en_simple_all_nopic', listing))

    def test_only_a_missing_file_means_there_is_no_checksum(self) -> None:
        # A network failure used to read as "Kiwix publishes no checksum ... pass --no-verify".
        url, build = 'https://example.org/zim/x_2026-01.zim.sha256', 'x_2026-01.zim'
        real = kb.fetch

        def answering(error: Exception):
            def fetch(_url: str, timeout: int = 60) -> bytes:
                raise error
            return fetch

        try:
            kb.fetch = answering(urllib.error.HTTPError(url, 404, 'Not Found', None, None))
            with self.assertRaises(kb.Problem) as missing:
                kb.published_checksum('x', url, build)
            self.assertIn('publishes no checksum', str(missing.exception))
            self.assertIn('--no-verify', str(missing.exception))
            for error in (urllib.error.HTTPError(url, 503, 'Service Unavailable', None, None),
                          urllib.error.URLError('timed out'), TimeoutError('timed out')):
                kb.fetch = answering(error)
                with self.assertRaises(kb.Problem) as failed:
                    kb.published_checksum('x', url, build)
                self.assertIn('could not be fetched', str(failed.exception))
                self.assertIn('run refresh again', str(failed.exception))
                self.assertNotIn('--no-verify', str(failed.exception))
            kb.fetch = lambda _url, timeout=60: b'ABCDEF0123  x_2026-01.zim\n'
            self.assertEqual(kb.published_checksum('x', url, build), 'abcdef0123')
        finally:
            kb.fetch = real

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

    def test_the_real_source_list_is_one_refresh_can_use(self) -> None:
        # Each name and prefix must pass the rule refresh applies before it downloads anything,
        # and the list must be in the form the script itself writes, so enable changes one line.
        text = (fixtures.SCRIPTS.parents[1] / SOURCES).read_text(encoding='utf-8')
        data = json.loads(text)
        self.assertEqual(json.dumps(data, indent=2, ensure_ascii=False) + '\n', text)
        for source in data['sources']:
            self.assertTrue(kb.SAFE_NAME.fullmatch(source['name']), source['name'])
            self.assertTrue(kb.SAFE_NAME.fullmatch(source['prefix']), source['prefix'])
            self.assertTrue(source['base'].startswith('https://') and source['base'].endswith('/'), source['base'])
        simple = next(s for s in data['sources'] if s['name'] == 'wikipedia-simple')
        self.assertEqual(simple['prefix'], 'wikipedia_en-simple_all_nopic')



class TestCheck(unittest.TestCase):
    """check reads each listing and downloads nothing, so it can run every week with nobody watching."""

    WIKI = 'https://download.kiwix.org/zim/wikipedia/'
    WIKTIONARY = 'https://download.kiwix.org/zim/wiktionary/'

    def setUp(self) -> None:
        self.vault = fixtures.Vault()
        self.vault.write(SOURCES, json.dumps({'sources': [
            {'name': 'wikipedia-simple', 'prefix': 'wikipedia_en-simple_all_nopic', 'base': self.WIKI, 'enabled': False},
            {'name': 'wiktionary', 'prefix': 'wiktionary_en_all_nopic', 'base': self.WIKTIONARY, 'enabled': True},
            {'name': 'renamed', 'prefix': 'wikipedia_en_simple_all_nopic', 'base': self.WIKI, 'enabled': False},
        ]}, indent=2) + '\n')
        self.listings = {
            self.WIKI: b'<a href="wikipedia_en-simple_all_nopic_2026-09.zim">x</a>',
            self.WIKTIONARY: b'<a href="wiktionary_en_all_nopic_2026-10.zim">x</a>',
        }
        self.read: list[str] = []
        self.real = kb.fetch

        def fetch(url: str, timeout: int = 60) -> bytes:
            self.read.append(url)
            if url not in self.listings:
                raise urllib.error.URLError('no route to host')
            return self.listings[url]

        kb.fetch = fetch

    def tearDown(self) -> None:
        kb.fetch = self.real
        self.vault.cleanup()

    def check(self, *args: str) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = kb.main(['--root', str(self.vault.root), 'check', *args])
        return code, out.getvalue(), err.getvalue()

    def test_the_sources_that_are_on_are_read_and_nothing_is_downloaded(self) -> None:
        before = sorted(p.name for p in self.vault.path(SOURCES).parent.iterdir())
        code, out, err = self.check()
        self.assertEqual(code, 0, err)
        self.assertEqual(out, 'wiktionary: wiktionary_en_all_nopic_2026-10.zim\n')
        # One listing read, no build and no checksum fetched, and nothing written beside the sources.
        self.assertEqual(self.read, [self.WIKTIONARY])
        self.assertEqual(sorted(p.name for p in self.vault.path(SOURCES).parent.iterdir()), before)

    def test_a_prefix_that_names_no_build_is_named_and_fails(self) -> None:
        code, out, err = self.check('--all')
        self.assertEqual(code, 1)
        self.assertIn('wikipedia-simple: wikipedia_en-simple_all_nopic_2026-09.zim', out)
        self.assertIn(f'renamed: the listing at {self.WIKI} names no wikipedia_en_simple_all_nopic_YYYY-MM.zim build',
                      err)

    def test_a_listing_that_cannot_be_read_is_not_a_missing_build(self) -> None:
        del self.listings[self.WIKTIONARY]
        code, _out, err = self.check()
        self.assertEqual(code, 2)
        self.assertIn(f'wiktionary: the listing at {self.WIKTIONARY} could not be read', err)
        # A source that names no build outranks a listing that could not be read.
        self.assertEqual(self.check('--all')[0], 1)

    def test_with_no_source_on_nothing_is_read(self) -> None:
        data = json.loads(self.vault.read(SOURCES))
        for source in data['sources']:
            source['enabled'] = False
        self.vault.write(SOURCES, json.dumps(data, indent=2) + '\n')
        code, out, _err = self.check()
        self.assertEqual(code, 0)
        self.assertIn('No source is on', out)
        self.assertEqual(self.read, [])

    def test_a_named_source_is_read_on_or_off(self) -> None:
        code, out, _err = self.check('wikipedia-simple')
        self.assertEqual(code, 0)
        self.assertEqual(self.read, [self.WIKI])
        self.assertEqual(self.check('nowhere')[0], 1)

    def test_a_name_that_cannot_be_trusted_is_refused_before_its_listing_is_read(self) -> None:
        data = json.loads(self.vault.read(SOURCES))
        data['sources'] = [{'name': 'bad/name', 'prefix': 'x', 'base': 'https://example.org/', 'enabled': True}]
        self.vault.write(SOURCES, json.dumps(data, indent=2) + '\n')
        code, _out, err = self.check()
        self.assertEqual(code, 1)
        self.assertIn('a name and prefix hold only letters', err)
        self.assertEqual(self.read, [])

ARTICLES = {'Lisbon': '<p>Trams climb the hills of Lisbon.</p>', 'Porto': '<p>Port wine ages in cellars by the river.</p>'}


def stand_ins(generation: int):
    """libzim's classes as one generation names their calls: 3 says getResults and hands back paths, 4 says
    get_results and hands back each full-text result as an object carrying its path."""

    class Entry:
        def __init__(self, path: str) -> None:
            self.title, self.content = path, ARTICLES[path].encode()

        def get_item(self) -> Entry:
            return self

    class Archive:
        def __init__(self, path: str) -> None:
            self.path = path

        def get_entry_by_path(self, path: str) -> Entry:
            return Entry(path)

    class Hit:
        def __init__(self, path: str) -> None:
            self.path = path

    class Found:
        def __init__(self, paths: list[str], whole: bool) -> None:
            self.paths, self.whole = paths, whole

    def fetch(self: Found, start: int, count: int) -> list:
        paths = self.paths[start:start + count]
        return [Hit(path) for path in paths] if self.whole and generation >= 4 else paths

    # A generation nobody has met yet is played by a call under a third name.
    setattr(Found, {3: 'getResults', 4: 'get_results'}.get(generation, 'results'), fetch)

    class Query:
        def set_query(self, text: str) -> Query:
            self.text = text
            return self

    class Searcher:
        def __init__(self, archive: Archive) -> None:
            self.archive = archive

        def search(self, query: Query) -> Found:
            return Found([path for path, body in ARTICLES.items() if query.text.lower() in body.lower()], whole=True)

    class SuggestionSearcher:
        def __init__(self, archive: Archive) -> None:
            self.archive = archive

        def suggest(self, text: str) -> Found:
            return Found([path for path in ARTICLES if path.lower().startswith(text.lower())], whole=False)

    return Archive, Query, Searcher, SuggestionSearcher


class TestSearchAndRead(unittest.TestCase):
    def setUp(self) -> None:
        self.vault = fixtures.Vault()
        self.vault.write('Library/Reference & Encyclopedia/wikivoyage_2026-09.zim', 'not really')
        self.reader = kb.reader

    def tearDown(self) -> None:
        kb.reader = self.reader
        self.vault.cleanup()

    def run_with(self, generation: int, call, *args) -> tuple[int, str, str]:
        kb.reader = lambda: stand_ins(generation)
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = call(*args)
        return code, out.getvalue(), err.getvalue()

    def test_search_finds_articles_under_either_libzim(self) -> None:
        for generation in (3, 4):
            # By the start of a title, then by a word only the text holds.
            code, out, _ = self.run_with(generation, kb.search, self.vault.root, 'lisb')
            self.assertEqual(code, 0, generation)
            self.assertIn('- Lisbon  [wikivoyage]', out, generation)
            code, out, _ = self.run_with(generation, kb.search, self.vault.root, 'cellars')
            self.assertEqual(code, 0, generation)
            self.assertIn('- Porto  [wikivoyage]', out, generation)
            self.assertIn('Port wine ages in cellars by the river.', out, generation)

    def test_read_follows_a_title_that_is_not_exact(self) -> None:
        for generation in (3, 4):
            code, out, _ = self.run_with(generation, kb.read, self.vault.root, 'lisb', 6000)
            self.assertEqual(code, 0, generation)
            self.assertIn('Trams climb the hills of Lisbon.', out, generation)
            self.assertIn('Cite as: wikivoyage, article "Lisbon"', out, generation)

    def test_a_search_that_matches_nothing_says_so(self) -> None:
        code, out, _ = self.run_with(4, kb.search, self.vault.root, 'glacier')
        self.assertEqual(code, 0)
        self.assertIn('No matches for: glacier', out)

    def test_a_libzim_that_answers_another_way_is_a_problem_not_an_empty_result(self) -> None:
        for command in (['search', 'lisb'], ['read', 'lisb']):
            code, out, err = self.run_with(5, kb.main, ['--root', str(self.vault.root), *command])
            self.assertEqual(code, 1, command)
            self.assertIn('has neither get_results nor getResults', err, command)
            self.assertNotIn('No matches', out, command)
            self.assertNotIn('No article matching', err, command)


if __name__ == '__main__':
    unittest.main()
