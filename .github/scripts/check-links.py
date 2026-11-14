#!/usr/bin/env python3
"""Check every reference between notes: a wikilink resolves and follows the hub topology, and a plain path names a file.

WHY THIS EXISTS. The vault is a knowledge graph of wikilinks, and its links
follow one shape (.docs/technical/vault/Link-Topology.md). A folder's own note,
its README.md, links the files in its folder and the README.md of each
immediate subfolder, and every other note links nothing and names files by
plain path. Links flow downhill and never back. A broken link is a lie in the graph, and a link
out of place makes the graph, and every note's backlinks, say something
untrue, and nothing else would notice either one. Link checkers that read Markdown links
do not read wikilinks, so this does.

It fails on a link that resolves to no file, a link the topology does not
allow and a link into a .template/ scaffold, and warns on a link that matches
several files (give it a path). Links inside code and inside %% comments are
not links. Every folder has a README.md, so a link to one names its folder:
[[Library/README|Library]]. The topology leaves no room for two notes to
link each other, or for a longer loop, so there is nothing to check there.

Every note but a folder's README.md refers to another by plain path, so most
of the vault's references are plain text, and a rename or a typing slip
breaks one without a word. So it also fails on a plain path that names no
file or folder: the path on a `Related:` line, and any path in backticks
that runs from one of the seven top folders and ends in .md or in a slash,
as `Memory/Entities/People/README.md` or `Profile/Skills/` does. A path
holding a placeholder, such as [Company], <year>, * or YYYY, is a pattern
and is passed by, and so is one inside a fenced block, which is an example.
A folder the vault makes when it is first needed counts as there: the
Inbox's Backups, and the archive's folder for a year.

Run it:

    python3 .github/scripts/check-links.py
"""

from __future__ import annotations

import os
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import vault  # noqa: E402  (vault.py sits beside this file)

# A plain path, as a note that may not wikilink writes one (Link-Topology.md): on a Related: line,
# or in backticks, from one of the seven top folders, ending in .md or in a slash.
RELATED = re.compile(r'^\s*(?:[-*+]\s+)?Related:\s*(\S.*?)\s*$')
CODE_SPAN = re.compile(r'`([^`\n]+)`')
FROM_THE_ROOT = tuple(name + '/' for name in vault.TOP_FOLDERS)
# What marks a path as a pattern, to be filled in, and never a file: [Company], <year>, *.md, YYYY-MM.
PLACEHOLDER = re.compile(r'[\[\]<>*]|YYYY')
# Folders the vault makes the first time it needs one, so a path to one is sound before it exists:
# the Inbox's Backups (Inbox/README.md), and a year of the archive, which update-vault.py makes.
MADE_ON_DEMAND = re.compile(r'^(?:Inbox/Backups|Memory/Context/Archive/(?:\d{4}|undated))/$')


def resolve(target: str, by_name: dict[str, list[str]], files: list[str]) -> list[str]:
    """The files a link names: a path, or a file name anywhere in the vault."""
    lowered = target.lower()
    if '/' in target:
        # A path link matches a whole path, or a tail of one at a folder boundary.
        wanted = (lowered, lowered + '.md')
        return [f for f in files if any(f.lower() == w or f.lower().endswith('/' + w) for w in wanted)]
    hits = by_name.get(lowered, []) or by_name.get(lowered + '.md', [])
    if len(hits) > 1:
        exact = [h for h in hits if h.rsplit('/', 1)[-1] in (target, target + '.md')]
        if len(exact) == 1:
            return exact
    return hits


def allowed(source: str, target: str) -> tuple[bool, str]:
    """Whether the hub topology lets `source` link `target`, and why not."""
    src, dst = source.split('/'), target.split('/')
    if len(src) == 1:
        return False, ('the vault root holds no notes; its README.md names the top folders '
                       'with Markdown links (Link-Topology.md)')
    if src[-1] == vault.README:
        folder = src[:-1]
        sibling = dst[:-1] == folder
        child = len(dst) == len(folder) + 2 and dst[:len(folder)] == folder and dst[-1] == vault.README
        return sibling or child, ("a folder's README.md links the files in its folder and its "
                                  "subfolders' README.md files, nothing else (Link-Topology.md)")
    return False, ("a note that is not a folder's README.md carries no wikilinks; "
                   'name the file by plain path (Link-Topology.md)')


def there(root: pathlib.Path, name: str) -> bool:
    """Whether a path from the vault root names a file, or with a closing slash a folder, in the
    case it is written in: a file system that folds case would pass a path that fails everywhere else."""
    here = root
    for part in name.rstrip('/').split('/'):
        try:
            if part not in os.listdir(here):
                return False
        except OSError:
            return False
        here = here / part
    return here.is_dir() if name.endswith('/') else here.is_file()


def plain_paths(text: str) -> list[tuple[int, str]]:
    """Each plain path a note writes, with its line: the path on a Related: line, and each path in
    backticks that runs from a top folder and ends in .md or a slash. Fenced blocks hold examples,
    and a path holding a placeholder is a pattern; neither is a reference."""
    found = []
    for number, line in enumerate(vault.strip_fences(text).split('\n'), 1):
        related = RELATED.match(line)
        spans = [related.group(1).strip('`')] if related else CODE_SPAN.findall(line)
        for span in spans:
            name = span.strip()
            if PLACEHOLDER.search(name):
                continue
            if related:
                # A word after the path, such as why it is related, is not part of the path.
                name = name[:name.rfind('.md') + 3] if '.md' in name else name
                found.append((number, name))
            elif name.startswith(FROM_THE_ROOT) and name.endswith(('.md', '/')):
                found.append((number, name))
    return found


def main(argv: list[str] | None = None) -> int:
    args = vault.arguments((__doc__ or '').split('\n', 1)[0]).parse_args(argv)
    root = args.root.resolve()
    report = vault.Report(root)
    by_name: dict[str, list[str]] = {}
    files: list[str] = []
    scaffolds: set[str] = set()
    for path in vault.walk_files(root):
        name = vault.rel(root, path)
        if vault.is_template(path.relative_to(root).parts):
            # Every folder has a README.md, so that name alone says nothing about a scaffold;
            # a link into one by path is still caught below, by its .template/ folder.
            if not vault.is_folder_note(path):
                scaffolds.update({path.stem.lower(), path.name.lower()})
            continue
        files.append(name)
        for key in {path.name.lower()} | ({path.stem.lower()} if path.suffix == '.md' else set()):
            by_name.setdefault(key, []).append(name)
    total = paths = 0
    # A loose file waiting at the Inbox is not a note yet, so what it links is not checked.
    for path in vault.filed_notes(root):
        if vault.is_template(path.relative_to(root).parts):
            continue
        source = vault.rel(root, path)
        try:
            text = vault.read_text(path)
        except OSError:
            continue
        targets = vault.wikilinks(text)
        total += len(targets)
        for target in targets:
            hits = resolve(target, by_name, files)
            if not hits:
                base = target.rsplit('/', 1)[-1].lower()
                if base in scaffolds or base + '.md' in scaffolds or '.template' in target.lower():
                    report.error(path, f'[[{target}]] links a scaffold; a .template/ file is not a graph node, '
                                       'so name it by plain path (Link-Topology.md)')
                else:
                    report.error(path, f'[[{target}]] resolves to no file')
                continue
            if len(set(hits)) > 1:
                report.warn(path, f'[[{target}]] matches {len(set(hits))} files ({", ".join(sorted(set(hits))[:3])}); '
                                  'give it a path')
            hit = hits[0]
            if hit == source:
                continue
            ok, why = allowed(source, hit)
            if not ok:
                report.error(path, f'[[{target}]]: {why}')
        for line, name in plain_paths(text):
            paths += 1
            if there(root, name) or MADE_ON_DEMAND.match(name):
                continue
            kind = 'folder' if name.endswith('/') else 'file'
            report.error(path, f'`{name}` names no {kind}; a plain path does not follow a rename, so write the path '
                               'the file has now, from the vault root (Link-Topology.md)', line)
    return report.finish(f'All {total} wikilinks resolve and follow the hub topology, and all {paths} plain paths '
                         'name a file or a folder.')


if __name__ == '__main__':
    sys.exit(main())
