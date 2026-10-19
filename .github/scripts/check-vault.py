#!/usr/bin/env python3
"""Run every vault check, as CI does: notes, links, skills, agents, personal data and generated parts.

WHY THIS EXISTS. Each check is its own script so it can run alone, the way the
Claude Code hook lints one note after an edit. Before a commit, and in CI, all
of them need to pass together, and nobody should have to remember the list.
This runs each one in turn, prints what each found, and fails if any did. The
generated parts are checked with `update-vault.py --check`, so it never writes.

Run it:

    python3 .github/scripts/check-vault.py
"""

from __future__ import annotations

import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import vault  # noqa: E402  (vault.py sits beside this file)

HERE = pathlib.Path(__file__).resolve().parent
CHECKS = (
    ('notes', 'lint-notes.py', ()),
    ('links', 'check-links.py', ()),
    ('skills', 'check-skills.py', ()),
    ('agents', 'check-agents.py', ()),
    ('personal data', 'scan-pii.py', ()),
    ('generated parts', 'update-vault.py', ('--check',)),
)


def main(argv: list[str] | None = None) -> int:
    args = vault.arguments((__doc__ or '').split('\n', 1)[0]).parse_args(argv)
    root = args.root.resolve()
    failed = []
    for label, script, extra in CHECKS:
        print(f'== {label} ({script})', flush=True)
        result = subprocess.run([sys.executable, str(HERE / script), '--root', str(root), *extra], check=False)
        if result.returncode != 0:
            failed.append(label)
    if failed:
        print(f'{len(failed)} of {len(CHECKS)} vault checks fail: {", ".join(failed)}.', file=sys.stderr)
        return 1
    print(f'All {len(CHECKS)} vault checks pass.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
