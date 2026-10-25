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
import shutil
import subprocess
import sys
import tempfile

SCRIPTS = pathlib.Path(__file__).resolve().parent


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
        """A note whose hidden frontmatter passes lint-notes.py, unless a field given here says
        otherwise. A field set to None is left out."""
        stem = pathlib.PurePosixPath(rel).stem
        values: dict[str, object] = {'title': stem, 'description': f'The note at {rel}.', 'type': 'index'}
        values.update(fields)
        return self.write(rel, block('<!--', '-->', values) + '\n\n' + (body or f'# {stem}\n'))

    def agent(self, rel: str, body: str = '', **fields: object) -> pathlib.Path:
        """An agent spec: the --- block its loader reads, naming the agent."""
        stem = pathlib.PurePosixPath(rel).stem
        values: dict[str, object] = {'name': stem.lstrip('★ ').split()[0], 'description': f'The agent {stem}.',
                                     'tools': 'Read, Grep, Glob'}
        values.update(fields)
        return self.write(rel, block('---', '---', values) + '\n\n' + (body or f'# {stem}\n'))

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


def block(opener: str, closer: str, values: dict[str, object]) -> str:
    """A frontmatter block holding the values that are not None, one field to a line."""
    lines = [opener]
    for key, value in values.items():
        if value is None:
            continue
        if isinstance(value, bool):
            lines.append(f'{key}: {str(value).lower()}')
        elif isinstance(value, list):
            lines.append(f'{key}: [' + ', '.join(f'"{item}"' for item in value) + ']')
        elif isinstance(value, int) or key == 'tools':
            lines.append(f'{key}: {value}')
        else:
            lines.append(f'{key}: "{value}"')
    lines.append(closer)
    return '\n'.join(lines)
