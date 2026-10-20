#!/usr/bin/env python3
"""Check the wikilink graph: every link resolves, and links follow the hub topology.

WHY THIS EXISTS. The vault is a knowledge graph of wikilinks, and its links
follow one shape (.docs/technical/vault/Link-Topology.md). A folder's own note links
the files in its folder and the notes of its immediate subfolders, and every
other note links nothing and names files by plain path. Links
flow downhill and never back. A broken link is a lie in the graph, and a link
out of place makes the graph, and every note's backlinks, say something
untrue, and nothing else would notice either one. Link checkers that read Markdown links
do not read wikilinks, so this does.

It fails on a link that resolves to no file, a link the topology does not
allow, a link into a .template/ scaffold, and two notes that link each other.
It warns on a link that matches several files (give it a path) and on longer
cycles. Links inside code and inside %% comments are not links.

Run it:

    python3 .github/scripts/check-links.py
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import vault  # noqa: E402  (vault.py sits beside this file)


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
        return False, ('the vault root holds no notes; AGENTS.md names the top folder notes '
                       'with Markdown links (Link-Topology.md)')
    if src[-1].rsplit('.', 1)[0] == src[-2]:
        folder = src[:-1]
        sibling = dst[:-1] == folder
        child = (len(dst) == len(folder) + 2 and dst[:len(folder)] == folder
                 and dst[-1].rsplit('.', 1)[0] == dst[-2])
        return sibling or child, ("a folder's note links the files in its folder and its "
                                  "subfolders' notes, nothing else (Link-Topology.md)")
    return False, 'a note that is not a folder note carries no wikilinks; name the file by plain path (Link-Topology.md)'


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
            scaffolds.update({path.stem.lower(), path.name.lower()})
            continue
        files.append(name)
        for key in {path.name.lower()} | ({path.stem.lower()} if path.suffix == '.md' else set()):
            by_name.setdefault(key, []).append(name)
    edges: set[tuple[str, str]] = set()
    total = 0
    for path in vault.walk_notes(root):
        if vault.is_template(path.relative_to(root).parts):
            continue
        source = vault.rel(root, path)
        try:
            targets = vault.wikilinks(vault.read_text(path))
        except OSError:
            continue
        total += len(targets)
        for target in targets:
            hits = resolve(target, by_name, files)
            if not hits:
                base = target.rsplit('/', 1)[-1].lower()
                if base in scaffolds or base + '.md' in scaffolds or '.template' in target.lower():
                    report.error(path, f'[[{target}]] links a scaffold; a .template/ file is not a graph node, '
                                       'so name it by plain path (3.7)')
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
                continue
            edges.add((source, hit))
    for a, b in sorted({tuple(sorted(edge)) for edge in edges if (edge[1], edge[0]) in edges}):
        report.error(a, f'{a} and {b} link each other; links flow downhill, so the note nearer the root '
                        'keeps the link and the other names it by plain path (3.7)')
    following: dict[str, set[str]] = {}
    for a, b in edges:
        following.setdefault(a, set()).add(b)
    state: dict[str, int] = {}
    for start in sorted(following):
        if state.get(start):
            continue
        # Depth-first, without recursion, so a deep vault cannot overflow the stack.
        stack = [(start, iter(sorted(following.get(start, ()))))]
        trail = [start]
        state[start] = 1
        while stack:
            node, children = stack[-1]
            child = next(children, None)
            if child is None:
                state[node] = 2
                stack.pop()
                trail.pop()
                continue
            if state.get(child) == 1 and child in trail:
                cycle = trail[trail.index(child):] + [child]
                if len(cycle) > 3:
                    report.warn(child, 'link cycle ' + ' > '.join(cycle) + '; the graph should run downhill, '
                                       'so cut the uphill link')
            elif not state.get(child):
                state[child] = 1
                trail.append(child)
                stack.append((child, iter(sorted(following.get(child, ())))))
    return report.finish(f'All {total} wikilinks resolve and follow the hub topology.')


if __name__ == '__main__':
    sys.exit(main())
