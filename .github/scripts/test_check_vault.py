#!/usr/bin/env python3
"""Tests for check-vault.py, and for the wiring that runs the vault scripts.

WHY THIS EXISTS. check-vault.py is the one command CI and a person run, so it
must run every check and fail when any one does. The scripts are also called
from a place a unit test of each script never sees: the composite action CI
uses. A renamed script would leave it pointing at nothing, silently. These
tests check the umbrella on a throwaway vault, then check that every script
the action names exists, and that every script is written the way this
folder's File Log reads them.

Run it:

    python3 .github/scripts/test_check_vault.py
"""

from __future__ import annotations

import ast
import importlib.util
import pathlib
import re
import shutil
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fixtures  # noqa: E402
import vault  # noqa: E402

SCRIPT = 'check-vault.py'
ROOT = fixtures.SCRIPTS.parents[1]
DASHES = re.compile('[\u2013\u2014\u2015]')
VAULT_SCRIPTS = ('vault.py', 'lint-notes.py', 'check-links.py', 'scan-pii.py', 'check-ignored.py', 'update-vault.py', 'check-vault.py', 'session.py',
                 'profile-coverage.py', 'knowledge-base.py', 'fixtures.py')


class TestCheckVault(unittest.TestCase):
    def setUp(self) -> None:
        self.vault = fixtures.Vault()

    def tearDown(self) -> None:
        self.vault.cleanup()

    def test_an_empty_vault_passes_every_check(self) -> None:
        self.vault.init_git()
        result = self.vault.run(SCRIPT)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('All 5 vault checks pass.', result.stdout)

    def test_one_failing_check_fails_the_run_and_is_named(self) -> None:
        self.vault.write('Memory/README.md', '# no frontmatter, and [[Nowhere]]\n')
        self.vault.init_git()
        result = self.vault.run(SCRIPT)
        self.assertEqual(result.returncode, 1)
        # A note with no catalog drawn yet also leaves the generated parts stale.
        self.assertIn('3 of 5 vault checks fail: notes, links, generated parts.', result.stderr)

    def test_a_plain_note_left_at_the_inbox_keeps_every_check_green(self) -> None:
        # The capture path: drop a note, sort it later. Done means check-vault.py passes, so a
        # waiting file must not turn it red, and the start card must still say it waits.
        self.vault.note('Inbox/README.md')
        self.vault.write('Inbox/call notes.md', '# Notes from the call\n\nQuote due Friday.\n')
        self.vault.init_git()
        self.assertEqual(self.vault.run('update-vault.py').returncode, 0)
        result = self.vault.run(SCRIPT)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn('call notes', self.vault.read('System/Data/catalog.ndjson'))
        self.assertIn('INBOX Inbox/call notes.md', self.vault.run('session.py', 'start').stdout)

    def test_a_file_git_ignores_fails_the_run(self) -> None:
        self.vault.write('.gitignore', '*.zip\n')
        self.vault.write('Inbox/statements.zip', 'x')
        self.vault.init_git()
        result = self.vault.run(SCRIPT)
        self.assertEqual(result.returncode, 1)
        self.assertIn('1 of 5 vault checks fail: ignored files.', result.stderr)

    def test_the_real_vault_passes(self) -> None:
        result = fixtures.subprocess.run([sys.executable, str(fixtures.SCRIPTS / SCRIPT)],
                                         capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


# One of each kind of file the audit found turning CI red while it waited at the Inbox: a note with no
# frontmatter, a PDF, an export in Latin-1, JSON lines saved under .json, a line ending in a space, and
# a file inside a folder dropped there whole.
DROPS = {
    'Inbox/call notes.md': b'# Notes from the call\n\nTeh quote is due Friday.\n',
    'Inbox/receipt.pdf': b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n1 0 obj\n<<>>\nendobj\ntrailer\n<<>>\n%%EOF\n',
    'Inbox/export.csv': 'date,payee,amount\n2026-11-02,Caf\xe9 Luz,4.50\n'.encode('latin-1'),
    'Inbox/activity.json': b'{"when": "2026-11-10", "what": "regatta"}\n{"when": "2026-11-12", "what": "call"}\n',
    'Inbox/todo.txt': b'buy tile samples \ncall teh plumber\n',
    'Inbox/scans/page 1.txt': b'scanned \n',
}


class TestTheInheritedChecksLeaveTheInboxAlone(unittest.TestCase):
    """CI runs checks the vault inherits, which know nothing of the Inbox. .gitattributes and
    .typos.toml tell them which files wait there, and must name exactly the files vault.py does."""

    def setUp(self) -> None:
        self.vault = fixtures.Vault()
        shutil.copy(ROOT / '.gitattributes', self.vault.path('.gitattributes'))
        shutil.copy(ROOT / '.typos.toml', self.vault.path('.typos.toml'))
        for rel, data in DROPS.items():
            self.vault.path(rel).parent.mkdir(parents=True, exist_ok=True)
            self.vault.path(rel).write_bytes(data)
        self.vault.note('Inbox/README.md')

    def tearDown(self) -> None:
        self.vault.cleanup()

    def test_git_keeps_exactly_the_drops_byte_for_byte(self) -> None:
        kept = ['Inbox/README.md', 'Inbox/.keep', 'Inbox/.cache/state.txt']
        for held in sorted(vault.INBOX_HELD):
            kept += [f'Inbox/{held}/Kitchen Costs.md', f'Inbox/{held}/Floor Plan.pdf']
        for rel in kept[1:]:
            self.vault.write(rel, 'x\n')
        self.vault.init_git()
        drops = {p.relative_to(self.vault.root).as_posix() for p in vault.inbox_drops(self.vault.root)}
        self.assertEqual(drops, set(DROPS))
        listing = fixtures.subprocess.run(['git', '-C', str(self.vault.root), 'check-attr', '-z', '--stdin', 'text'],
                                          input='\0'.join([*DROPS, *kept]) + '\0', capture_output=True,
                                          text=True, check=True).stdout.split('\0')
        text = {listing[i]: listing[i + 2] for i in range(0, len(listing) - 2, 3)}
        for rel in DROPS:
            self.assertEqual(text[rel], 'unset', f'{rel} waits at the Inbox, so git keeps it as it arrived')
        for rel in kept:
            # A kept folder's note takes the default back; its PDF stays binary, as anywhere else.
            want = 'unset' if rel.endswith('.pdf') else 'auto'
            self.assertEqual(text[rel], want, f'{rel} is not a drop')

    @unittest.skipUnless(importlib.util.find_spec('yaml'), 'the repository validator needs PyYAML')
    def test_the_repository_validator_passes_the_drops_and_still_reads_the_kept_folders(self) -> None:
        # The validator checks the repository it sits in, so a copy of it checks this one.
        validator = self.vault.path('.github/scripts/validate-repository.py')
        validator.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(fixtures.SCRIPTS / 'validate-repository.py', validator)
        # A kept note with a fault the validator catches in any file, so it shows the note is still read.
        self.vault.write('Inbox/Research/Kitchen Costs.md', '# Kitchen Costs')
        self.vault.init_git()
        result = fixtures.subprocess.run([sys.executable, str(validator)], cwd=self.vault.root,
                                         capture_output=True, text=True, check=False)
        output = result.stdout + result.stderr
        self.assertEqual(result.returncode, 1, output)
        self.assertIn('Inbox/Research/Kitchen Costs.md', output)
        self.assertIn('1 problem', output)
        for rel in DROPS:
            self.assertNotIn(rel, output)

    def test_the_spell_check_leaves_out_exactly_the_drops(self) -> None:
        listed = re.search(r'(?ms)^extend-exclude = \[(.*?)^\]', (ROOT / '.typos.toml').read_text(encoding='utf-8'))
        self.assertIsNotNone(listed, '.typos.toml has no extend-exclude list')
        patterns = re.findall(r'"([^"]+)"', listed.group(1))
        self.assertEqual(patterns[0], '/Inbox/*')
        self.assertEqual(set(patterns[1:]), {'!/Inbox/README.md'} | {f'!/Inbox/{held}/' for held in vault.INBOX_HELD})
        typos = shutil.which('typos')
        if typos is None:
            return
        # Where the spell checker is installed, run it: a drop is left as it is, a kept note is read.
        self.vault.write('Inbox/Research/Kitchen Costs.md', '# Kitchen Costs\n\nTeh tiles cost more.\n')
        self.vault.init_git()
        result = fixtures.subprocess.run([typos, '--format', 'brief', '.'], cwd=self.vault.root,
                                         capture_output=True, text=True, check=False)
        self.assertIn('Inbox/Research/Kitchen Costs.md', result.stdout, result.stdout + result.stderr)
        for rel in DROPS:
            self.assertNotIn(rel, result.stdout)


class TestWiring(unittest.TestCase):
    def test_the_action_runs_scripts_that_exist(self) -> None:
        action = (ROOT / '.github' / 'actions' / 'vault' / 'action.yml').read_text(encoding='utf-8')
        named = re.findall(r'\.github/scripts/([\w.-]+\.py)', action)
        self.assertIn('check-vault.py', named)
        for name in named:
            self.assertTrue((fixtures.SCRIPTS / name).is_file(), name)
        workflow = (ROOT / '.github' / 'workflows' / 'vault.yml').read_text(encoding='utf-8')
        self.assertIn('uses: ./.github/actions/vault', workflow)
        self.assertNotIn('is_template', workflow.split('jobs:', 1)[1])

    def test_check_vault_runs_every_check_script(self) -> None:
        source = (fixtures.SCRIPTS / SCRIPT).read_text(encoding='utf-8')
        for name in ('lint-notes.py', 'check-links.py', 'scan-pii.py', 'check-ignored.py', 'update-vault.py'):
            self.assertIn(f"'{name}'", source)

    def test_the_template_delivers_every_vault_script(self) -> None:
        # check-vault.py is kept current in every vault made from the template, so each script it runs has to
        # travel with it: a script the sync list does not name never reaches a vault that already exists.
        sync_list = ROOT / '.github' / 'template-sync'
        if not sync_list.is_file():
            self.skipTest('this vault keeps no template sync list')
        # A path is named whether the list keeps it current or, behind a `#`, leaves it to the owner.
        named = {line.lstrip('#') for line in sync_list.read_text(encoding='utf-8').splitlines()}
        for script in VAULT_SCRIPTS:
            test = 'test_' + script.replace('-', '_')
            for name in (script, test) if (fixtures.SCRIPTS / test).is_file() else (script,):
                self.assertTrue(f'/.github/scripts/{name}' in named, f'{name} is not named in .github/template-sync')

    def test_every_script_reads_well_in_the_file_log(self) -> None:
        for name in VAULT_SCRIPTS + tuple(p.name for p in fixtures.SCRIPTS.glob('test_*.py')):
            text = (fixtures.SCRIPTS / name).read_text(encoding='utf-8')
            doc = ast.get_docstring(ast.parse(text))
            self.assertTrue(doc, f'{name} has no docstring')
            first = doc.split('\n', 1)[0]
            self.assertTrue(first.endswith('.'), f'{name}: the first docstring line is the File Log purpose')
            self.assertIsNone(DASHES.search(text), f'{name} holds an en, em or bar dash')
            self.assertIn('from __future__ import annotations', text, f'{name} must run on Python 3.9')


if __name__ == '__main__':
    unittest.main()
