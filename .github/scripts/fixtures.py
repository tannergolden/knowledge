#!/usr/bin/env python3
"""Throwaway vaults for the vault scripts' tests, built in a temporary folder.

WHY THIS EXISTS. Every vault script takes --root, so a test can build a small
vault of its own, run the real script on it exactly as CI does, and assert on
the exit code, the output and the files, without ever touching the vault this
repository holds. This module builds those vaults: a note with valid
frontmatter from one call, any other file from another. It is imported by the
test_*.py files beside it and runs nothing itself.
"""

from __future__ import annotations

import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

SCRIPTS = pathlib.Path(__file__).resolve().parent
PREFIX = {'root': 'ro', 'library': 'li', 'profile': 'id', 'memory': 'me', 'projects': 'pr',
          'ventures': 've', 'system': 'sy', 'inbox': 'in'}


class Vault:
    """A throwaway vault. Call cleanup() when done, or use it from setUp and tearDown."""

    def __init__(self) -> None:
        self.root = pathlib.Path(tempfile.mkdtemp(prefix='vault-test-')).resolve()

    def cleanup(self) -> None:
        shutil.rmtree(self.root, ignore_errors=True)

    def path(self, rel: str) -> pathlib.Path:
        return self.root / rel

    def write(self, rel: str, text: str) -> pathlib.Path:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')
        return path

    def read(self, rel: str) -> str:
        return (self.root / rel).read_text(encoding='utf-8')

    def note(self, rel: str, body: str = '', **fields: object) -> pathlib.Path:
        """A note whose frontmatter passes lint-notes.py, unless a field given here says otherwise.
        A field set to None is left out."""
        parts = pathlib.PurePosixPath(rel).parts
        folder = 'root' if len(parts) == 1 else parts[0].lower()
        stem = pathlib.PurePosixPath(rel).stem
        slug = re.sub(r'[^a-z0-9]+', '-', '-'.join(parts).lower().removesuffix('.md')).strip('-')
        kind = str(fields.get('type', 'information'))
        values: dict[str, object] = {
            'title': stem, 'description': f'The note at {rel}.', 'status': 'active',
            'tags': [folder, kind], 'aliases': [], 'keywords': [], 'created': '2026-01-01',
            'updated': '2026-01-01', 'type': kind, 'folder': folder, 'layer': len(parts) - 1,
            'policy': False, 'author': 'Test Author', 'path': f'BRAIN/{rel}',
            'id': f'{PREFIX.get(folder, "xx")}-{slug}',
        }
        values.update(fields)
        lines = ['---']
        for key, value in values.items():
            if value is None:
                continue
            if isinstance(value, bool):
                lines.append(f'{key}: {str(value).lower()}')
            elif isinstance(value, list):
                lines.append(f'{key}: [' + ', '.join(f'"{item}"' for item in value) + ']')
            elif isinstance(value, int):
                lines.append(f'{key}: {value}')
            else:
                lines.append(f'{key}: "{value}"')
        lines.append('---')
        return self.write(rel, '\n'.join(lines) + '\n\n' + (body or f'# {stem}\n'))

    def run(self, script: str, *args: str, stdin: str | None = None,
            scripts: pathlib.Path | None = None) -> subprocess.CompletedProcess[str]:
        """Run a vault script on this vault, the way CI runs it."""
        return subprocess.run([sys.executable, str((scripts or SCRIPTS) / script), '--root', str(self.root), *args],
                              capture_output=True, text=True, input=stdin, timeout=300, check=False)

    def git(self, *args: str) -> None:
        subprocess.run(['git', '-C', str(self.root), *args], check=True, capture_output=True)

    def init_git(self) -> None:
        self.git('init', '-q')
        self.git('config', 'user.email', 'test@example.com')
        self.git('config', 'user.name', 'Test')
        self.git('add', '-A')
        self.git('commit', '-q', '-m', 'test: seed', '--allow-empty')
