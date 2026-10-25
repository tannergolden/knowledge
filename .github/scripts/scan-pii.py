#!/usr/bin/env python3
"""Find US Social Security numbers and payment card numbers in the files git tracks.

WHY THIS EXISTS. The vault holds a person's own context, and its standing
rule is that sensitive values are pointers, never the values themselves. The
secret scan in checks.yml (gitleaks) catches keys and tokens across the whole
history; it does not look for the personal numbers a Profile or a Memory note
could pick up by accident. This does: a number shaped like a Social Security
number, and a 13 to 19 digit number that opens with a card issuer's digit and
passes the Luhn check. It favours precision over breadth so it does not cry
wolf, it skips the number checks in machine JSON, and it never prints a full
value.

A reviewed false positive is kept by putting pii-allow in a comment on its
line.

Run it:

    python3 .github/scripts/scan-pii.py
"""

from __future__ import annotations

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import vault  # noqa: E402  (vault.py sits beside this file)

ALLOW = 'pii-allow'
TEXT_SUFFIXES = frozenset({'.md', '.txt', '.py', '.sh', '.command', '.json', '.ndjson', '.yaml', '.yml',
                           '.env', '.cfg', '.ini', '.toml', '.csv'})
# Machine JSON is full of long numbers (graph layouts, colours, coordinates).
NUMERIC_EXEMPT = frozenset({'.json', '.ndjson'})
SSN = re.compile(r'\b\d{3}-\d{2}-\d{4}\b')
# A card opens with an issuer's digit: 3 Amex, 4 Visa, 5 Mastercard, 6 Discover.
CARD = re.compile(r'\b[3-6]\d{12,18}\b')


def luhn(number: str) -> bool:
    """The Luhn check digit test, so ordinary long numbers do not read as cards."""
    digits = [int(c) for c in number if c.isdigit()]
    if not 13 <= len(digits) <= 19:
        return False
    total, parity = 0, len(digits) % 2
    for i, digit in enumerate(digits):
        if i % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    return total % 10 == 0


def masked(value: str) -> str:
    """Enough of a value to find it again, never the whole of it."""
    return value[:2] + '...' + value[-2:] if len(value) > 6 else '...'


def findings(text: str, numeric: bool = True) -> list[tuple[int, str, str]]:
    """Each (line, kind, masked value) in a file's text."""
    out = []
    if not numeric:
        return out
    for number, line in enumerate(text.splitlines(), 1):
        if ALLOW in line:
            continue
        for match in SSN.finditer(line):
            out.append((number, 'a Social Security number', masked(match.group(0))))
        for match in CARD.finditer(line):
            if luhn(match.group(0)):
                out.append((number, 'a payment card number', masked(match.group(0))))
    return out


def targets(root: pathlib.Path) -> list[pathlib.Path]:
    """The text files git tracks, or every text file when the vault is not a checkout."""
    names = vault.tracked_files(root)
    paths = [root / name for name in names] if names is not None else [
        p for p in root.rglob('*') if p.is_file() and '.git' not in p.relative_to(root).parts]
    return [p for p in paths if p.suffix.lower() in TEXT_SUFFIXES and p.is_file()]


def main(argv: list[str] | None = None) -> int:
    args = vault.arguments((__doc__ or '').split('\n', 1)[0]).parse_args(argv)
    root = args.root.resolve()
    report = vault.Report(root)
    files = targets(root)
    for path in files:
        try:
            text = path.read_text(encoding='utf-8', errors='replace')
        except OSError:
            continue
        for line, kind, value in findings(text, numeric=path.suffix.lower() not in NUMERIC_EXEMPT):
            report.error(path, f'looks like {kind} ({value}); keep a pointer to it instead, or mark a '
                               f'reviewed false positive with {ALLOW} on the line', line)
    return report.finish(f'No personal numbers in {len(files)} tracked files.')


if __name__ == '__main__':
    sys.exit(main())
