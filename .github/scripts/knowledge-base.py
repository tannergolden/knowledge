#!/usr/bin/env python3
"""Search and read offline reference works, such as Wikipedia, kept as ZIM files beside the vault's notes.

WHY THIS EXISTS. Some questions are about the world, not the person, and an
offline encyclopedia answers them without the web. The vault keeps reference
works as Kiwix ZIM files in Library/Reference & Encyclopedia/, each with its
own full-text index, and this searches and reads them. Which works to keep is
the committed list in that folder's sources.json; the ZIM files themselves
are large downloads, never committed, fetched by `refresh`.

Every source ships off. Turn one on with `enable`, fetch it with `refresh`,
which checks each download against the checksum Kiwix publishes beside it
before installing it. Reading needs the optional libzim package
(python3 -m pip install --user libzim); without it, `list` still works and
`search` says how to add it.

Run it:

    python3 .github/scripts/knowledge-base.py list
    python3 .github/scripts/knowledge-base.py enable wikipedia-simple
    python3 .github/scripts/knowledge-base.py refresh
    python3 .github/scripts/knowledge-base.py search "photosynthesis"
    python3 .github/scripts/knowledge-base.py read "Photosynthesis"
"""

from __future__ import annotations

import hashlib
import html
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import vault  # noqa: E402  (vault.py sits beside this file)

FOLDER = 'Library/Reference & Encyclopedia'
SOURCES = 'sources.json'
RESULTS = 10
SAFE_NAME = re.compile(r'[A-Za-z0-9._-]+')
INSTALL_HINT = 'libzim is not installed; add it with: python3 -m pip install --user libzim (or in a venv)'


class Problem(Exception):
    """Something the person has to fix, said in one line."""


def folder(root: pathlib.Path) -> pathlib.Path:
    return root / FOLDER


def load_sources(root: pathlib.Path) -> dict[str, object]:
    """The committed source list. A missing or broken file is an error, never silently replaced."""
    path = folder(root) / SOURCES
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except FileNotFoundError:
        raise Problem(f'{vault.rel(root, path)} is missing') from None
    except (OSError, ValueError) as error:
        raise Problem(f'{vault.rel(root, path)} cannot be read: {error}') from None
    if not isinstance(data, dict) or not isinstance(data.get('sources'), list):
        raise Problem(f'{vault.rel(root, path)} needs a "sources" list')
    return data


def save_sources(root: pathlib.Path, data: dict[str, object]) -> None:
    path = folder(root) / SOURCES
    partial = path.with_name('.' + path.name + '.tmp~')
    partial.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    os.replace(partial, path)


def installed(root: pathlib.Path) -> list[pathlib.Path]:
    return sorted(folder(root).glob('*.zim')) if folder(root).is_dir() else []


def label(path: pathlib.Path) -> str:
    """A readable name for a ZIM: its file name without the _YYYY-MM.zim tail."""
    return re.sub(r'_\d{4}-\d{2}\.zim$', '', path.name).replace('_', ' ')


def size(count: float) -> str:
    for unit in ('B', 'KB', 'MB', 'GB'):
        if count < 1024:
            return f'{count:.0f} {unit}' if unit in ('B', 'KB') else f'{count:.1f} {unit}'
        count /= 1024
    return f'{count:.1f} TB'


def reader():
    """libzim's reader and search classes, or None when the package is missing."""
    try:
        from libzim.reader import Archive
        from libzim.search import Query, Searcher
    except ImportError:
        return None
    try:
        from libzim.suggestion import SuggestionSearcher
    except ImportError:
        SuggestionSearcher = None
    return Archive, Query, Searcher, SuggestionSearcher


def plain_text(archive, path: str) -> str:
    """An article's text: styles and scripts dropped, block ends kept as line breaks, entities decoded."""
    try:
        raw = bytes(archive.get_entry_by_path(path).get_item().content).decode('utf-8', 'ignore')
    except Exception:  # noqa: BLE001  (a damaged entry reads as empty)
        return ''
    raw = re.sub(r'(?is)<(style|script)\b[^>]*>.*?</\1>', ' ', raw)
    raw = re.sub(r'(?i)</(p|div|li|h[1-6]|tr)\s*>', '\n', raw)
    raw = re.sub(r'(?i)<br\s*/?>', '\n', raw)
    text = html.unescape(re.sub(r'<[^>]+>', ' ', raw))
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n[ \t]+', '\n', text)
    return re.sub(r'\n{3,}', '\n\n', text).strip()


def interleave(results: list[tuple[str, str, object]], limit: int) -> list[tuple[str, str, object]]:
    """Hits taken in turn from each source, since one archive's scores mean nothing beside another's."""
    buckets: dict[str, list[tuple[str, str, object]]] = {}
    for result in results:
        buckets.setdefault(result[0], []).append(result)
    out: list[tuple[str, str, object]] = []
    while len(out) < limit and any(buckets.values()):
        for key in list(buckets):
            if buckets[key]:
                out.append(buckets[key].pop(0))
                if len(out) >= limit:
                    break
    return out


def search(root: pathlib.Path, query: str, limit: int = RESULTS) -> int:
    zims = installed(root)
    if not zims:
        print(f'No knowledge bases are installed in {FOLDER}/. Enable a source, then run refresh.')
        return 0
    libs = reader()
    if libs is None:
        print(INSTALL_HINT, file=sys.stderr)
        return 1
    Archive, Query, Searcher, SuggestionSearcher = libs
    words = set(re.findall(r'[a-z0-9]+', query.lower()))
    results: list[tuple[str, str, object]] = []
    for zim in zims:
        try:
            archive = Archive(str(zim))
        except Exception:  # noqa: BLE001
            continue
        seen: set[str] = set()
        # Titles first, so the article named like the query leads its relatives.
        if SuggestionSearcher is not None:
            try:
                for path in SuggestionSearcher(archive).suggest(query).getResults(0, limit):
                    try:
                        title = str(archive.get_entry_by_path(path).title)
                    except Exception:  # noqa: BLE001
                        title = path
                    tokens = set(re.findall(r'[a-z0-9]+', f'{title} {path}'.lower()))
                    # A suggestion sharing no word or prefix with the query is noise.
                    if path in seen or (words and not (words & tokens or any(
                            t.startswith(w) for w in words for t in tokens))):
                        continue
                    seen.add(path)
                    results.append((label(zim), path, archive))
            except Exception:  # noqa: BLE001
                pass
        try:
            for path in Searcher(archive).search(Query().set_query(query)).getResults(0, limit):
                if path not in seen:
                    seen.add(path)
                    results.append((label(zim), path, archive))
        except Exception:  # noqa: BLE001
            continue
    if not results:
        print(f'No matches for: {query}')
        return 0
    for source, path, archive in interleave(results, limit):
        try:
            title = archive.get_entry_by_path(path).title
        except Exception:  # noqa: BLE001
            title = path
        snippet = re.sub(r'\s+', ' ', plain_text(archive, path))
        print(f'- {title}  [{source}]')
        if snippet:
            print(f'  {snippet[:160]}{"..." if len(snippet) > 160 else ""}')
    return 0


def read(root: pathlib.Path, article: str, chars: int) -> int:
    zims = installed(root)
    if not zims:
        print(f'No knowledge bases are installed in {FOLDER}/.')
        return 0
    libs = reader()
    if libs is None:
        print(INSTALL_HINT, file=sys.stderr)
        return 1
    Archive, _Query, _Searcher, SuggestionSearcher = libs
    for zim in zims:
        try:
            archive = Archive(str(zim))
        except Exception:  # noqa: BLE001
            continue
        path = None
        try:
            archive.get_entry_by_path(article)
            path = article
        except Exception:  # noqa: BLE001
            if SuggestionSearcher is not None:
                try:
                    hits = list(SuggestionSearcher(archive).suggest(article).getResults(0, 1))
                    path = hits[0] if hits else None
                except Exception:  # noqa: BLE001
                    path = None
        if not path:
            continue
        text = plain_text(archive, path)
        if not text:
            continue
        try:
            title = archive.get_entry_by_path(path).title
        except Exception:  # noqa: BLE001
            title = path
        print(f'{title}  [{label(zim)}]  path: {path}, {len(text)} characters, {zim.name}')
        print(text if len(text) <= chars else text[:chars])
        if len(text) > chars:
            print(f'[{len(text) - chars} more characters; raise --chars to read more]')
        print(f'Cite as: {label(zim)}, article "{title}" ({zim.stem})')
        return 0
    print(f"No article matching '{article}'; search first to find its exact title.", file=sys.stderr)
    return 1


def show(root: pathlib.Path) -> int:
    data = load_sources(root)
    zims = installed(root)
    libs = reader()
    for zim in zims:
        detail = ''
        if libs is not None:
            try:
                archive = libs[0](str(zim))
                detail = f', {archive.entry_count:,} entries'
            except Exception:  # noqa: BLE001
                detail = ', unreadable'
        print(f'installed: {zim.name} ({size(zim.stat().st_size)}{detail})')
    if not zims:
        print(f'No knowledge bases are installed in {FOLDER}/.')
    print('Sources (turn one on with: enable <name>):')
    for source in data['sources']:  # type: ignore[union-attr]
        state = 'on ' if source.get('enabled') else 'off'
        print(f"  [{state}] {source.get('name', '?'):<22} {source.get('note', '')}")
    if libs is None:
        print(INSTALL_HINT)
    return 0


def toggle(root: pathlib.Path, name: str, enable: bool) -> int:
    data = load_sources(root)
    for source in data['sources']:  # type: ignore[union-attr]
        if source.get('name') == name:
            source['enabled'] = enable
            save_sources(root, data)
            print(f"{name} is {'on; run refresh to download it' if enable else 'off'}.")
            return 0
    names = ', '.join(str(s.get('name', '?')) for s in data['sources'])  # type: ignore[union-attr]
    print(f'no source named {name}; the sources are {names}', file=sys.stderr)
    return 2


def newest(prefix: str, listing: str) -> str | None:
    """The newest dated build of a source named in a Kiwix directory listing, as a file name."""
    dates = sorted(set(re.findall(r'(?:^|[">/])' + re.escape(prefix) + r'_(\d{4}-\d{2})\.zim', listing)))
    return f'{prefix}_{dates[-1]}.zim' if dates else None


def sha256_of(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with open(path, 'rb') as handle:
        for block in iter(lambda: handle.read(1 << 20), b''):
            digest.update(block)
    return digest.hexdigest()


def fetch(url: str, timeout: int = 60) -> bytes:
    with urllib.request.urlopen(url, timeout=timeout) as response:  # noqa: S310  (https only, checked by the caller)
        return response.read()


def download(url: str, destination: pathlib.Path, expected: str | None) -> None:
    """Stream a file to destination, resuming a .part when the server allows, and install it
    only once its size and, when one is published, its checksum match."""
    part = destination.with_name(destination.name + '.part')
    have = part.stat().st_size if part.exists() else 0
    request = urllib.request.Request(url)
    if have:
        request.add_header('Range', f'bytes={have}-')
    try:
        response = urllib.request.urlopen(request, timeout=120)  # noqa: S310
    except urllib.error.HTTPError as error:
        if have and error.code == 416:
            part.unlink()
            return download(url, destination, expected)
        raise Problem(f'download failed: {error}') from None
    except (OSError, urllib.error.URLError) as error:
        raise Problem(f'download failed: {error}') from None
    with response:
        mode = 'ab'
        if have and getattr(response, 'status', 200) != 206:
            have, mode = 0, 'wb'
        length = response.headers.get('Content-Length')
        total = have + int(length) if length and length.isdigit() else 0
        done = have
        with open(part, mode) as handle:
            while True:
                chunk = response.read(1 << 20)
                if not chunk:
                    break
                handle.write(chunk)
                done += len(chunk)
                if total and sys.stdout.isatty():
                    print(f'\r  {done * 100 // total:3d}%  {size(done)} of {size(total)}', end='', flush=True)
    if total and sys.stdout.isatty():
        print()
    if total and done != total:
        raise Problem(f'the download stopped at {size(done)} of {size(total)}; run refresh again to resume')
    if expected is not None and sha256_of(part) != expected:
        raise Problem('the download does not match its published checksum; it was not installed')
    os.replace(part, destination)


def refresh(root: pathlib.Path, name: str, verify: bool, assume_yes: bool) -> int:
    data = load_sources(root)
    sources = [s for s in data['sources']  # type: ignore[union-attr]
               if (s.get('name') == name) or (not name and s.get('enabled'))]
    if not sources:
        print(f'no source named {name}' if name else 'No source is on; turn one on with: enable <name>',
              file=sys.stderr)
        return 1 if name else 0
    folder(root).mkdir(parents=True, exist_ok=True)
    failed = 0
    for source in sources:
        prefix, base, key = str(source.get('prefix', '')), str(source.get('base', '')), str(source.get('name', ''))
        try:
            if not (SAFE_NAME.fullmatch(prefix) and SAFE_NAME.fullmatch(key)) or '..' in prefix + key:
                raise Problem(f'{key!r}: a name and prefix hold only letters, digits, dot, dash and underscore')
            if not base.startswith('https://') or not base.endswith('/'):
                raise Problem(f'{key}: the base must be an https:// folder address ending in /')
            build = newest(prefix, fetch(base).decode('utf-8', 'ignore'))
            if build is None:
                raise Problem(f'{key}: the listing at {base} names no {prefix}_YYYY-MM.zim build')
            date = re.search(r'_(\d{4}-\d{2})\.zim$', build).group(1)  # type: ignore[union-attr]
            destination = folder(root) / f'{key}_{date}.zim'
            if destination.exists():
                print(f'{key}: {destination.name} is current')
                continue
            expected = None
            if verify:
                try:
                    expected = fetch(base + build + '.sha256', timeout=30).decode().split()[0].lower()
                except (OSError, urllib.error.URLError, IndexError):
                    raise Problem(f'{key}: Kiwix publishes no checksum for {build}; '
                                  'pass --no-verify to install it unchecked') from None
            print(f"{key}: downloading {build} ({source.get('note', '')})")
            download(base + build, destination, expected)
            print(f'{key}: installed {destination.name} ({size(destination.stat().st_size)})')
            older = [p for p in installed(root)
                     if p != destination and re.fullmatch(re.escape(key) + r'_\d{4}-\d{2}\.zim', p.name)]
            for old in older:
                if assume_yes or (sys.stdin.isatty() and input(f'Remove the older build {old.name}? (yes/no): ')
                                  .strip().lower() in ('y', 'yes')):
                    old.unlink()
                    print(f'{key}: removed the older build {old.name}')
                else:
                    print(f'{key}: kept the older build {old.name}')
        except Problem as problem:
            print(str(problem), file=sys.stderr)
            failed += 1
        except (OSError, urllib.error.URLError) as error:
            print(f'{key}: {error}', file=sys.stderr)
            failed += 1
    return 1 if failed else 0


def main(argv: list[str] | None = None) -> int:
    parser = vault.arguments((__doc__ or '').split('\n', 1)[0])
    commands = parser.add_subparsers(dest='command')
    commands.add_parser('list', help='the installed works and every source, on or off')
    finding = commands.add_parser('search', help='search every installed work')
    finding.add_argument('terms', nargs='+')
    reading = commands.add_parser('read', help="an article's text, by title or path")
    reading.add_argument('article', nargs='+')
    reading.add_argument('--chars', type=int, default=6000, help='how much of the article to print')
    for verb in ('enable', 'disable'):
        commands.add_parser(verb, help=f'{verb} a source').add_argument('name')
    refreshing = commands.add_parser('refresh', help='download the newest build of each source that is on')
    refreshing.add_argument('name', nargs='?', default='', help='just this source, on or off')
    refreshing.add_argument('--no-verify', action='store_true', help='install without the published checksum')
    refreshing.add_argument('--yes', action='store_true', help='remove older builds without asking')
    args = parser.parse_args(argv)
    root = args.root.resolve()
    try:
        if args.command in (None, 'list'):
            return show(root)
        if args.command == 'search':
            return search(root, ' '.join(args.terms))
        if args.command == 'read':
            return read(root, ' '.join(args.article), max(args.chars, 1))
        if args.command in ('enable', 'disable'):
            return toggle(root, args.name, args.command == 'enable')
        return refresh(root, args.name, not args.no_verify, args.yes)
    except Problem as problem:
        print(str(problem), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
