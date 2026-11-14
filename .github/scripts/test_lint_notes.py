#!/usr/bin/env python3
"""Tests for lint-notes.py, the note schema check.

WHY THIS EXISTS. lint-notes.py runs on a note after an edit and on every note
in CI, so a rule it gets wrong either lets a broken note through or blocks a
good one everywhere. Each test builds a throwaway
vault, runs the real script on it, and checks one rule both ways. The last
test runs it, read only, on the vault this repository holds.

Run it:

    python3 .github/scripts/test_lint_notes.py
"""

from __future__ import annotations

import pathlib
import re
import shutil
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fixtures  # noqa: E402

SCRIPT = 'lint-notes.py'
ROOT = fixtures.SCRIPTS.parents[1]


class TestLintNotes(unittest.TestCase):
    def setUp(self) -> None:
        self.vault = fixtures.Vault()

    def tearDown(self) -> None:
        self.vault.cleanup()

    def lint(self, *args: str):
        return self.vault.run(SCRIPT, *args)

    def assert_flags(self, needle: str, *args: str) -> None:
        result = self.lint(*args)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(needle, result.stdout)

    def test_a_valid_note_passes(self) -> None:
        self.vault.note('Library/README.md')
        result = self.lint()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn('1 note passes.', result.stdout)

    def test_a_missing_field(self) -> None:
        self.vault.note('Library/README.md', description=None)
        self.assert_flags('missing field: description')

    def test_no_frontmatter_and_an_empty_note(self) -> None:
        self.vault.write('Library/Bare.md', '# No frontmatter\n')
        self.vault.write('Library/Empty.md', '   \n')
        result = self.lint()
        self.assertIn('no frontmatter block', result.stdout)
        self.assertIn('the note is empty', result.stdout)

    def test_values_outside_the_schema(self) -> None:
        self.vault.note('Library/README.md', type='essay', status='done', keywords=['Cooking', 'x', 'x'])
        result = self.lint()
        for needle in ("type 'essay'", "status 'done'", "keyword 'Cooking' is not lowercase",
                       'a keyword appears twice'):
            self.assertIn(needle, result.stdout)

    def test_status_is_left_out_while_a_note_is_current(self) -> None:
        self.vault.note('Library/README.md', status='active')
        self.assert_flags('leave it out while the note is current')
        self.vault.note('Library/README.md', status='deprecated')
        self.assertEqual(self.lint().returncode, 0)

    def test_a_fenced_note_is_caught(self) -> None:
        self.vault.write('Library/Fenced.md', '---\ntitle: "Fenced"\ndescription: "A note."\ntype: "index"\n---\n')
        self.assert_flags('fenced with ---, which GitHub shows as a table')
        # The vault holds no agent specs, so a --- block that names an agent is a fenced note too.
        self.vault.write('Library/Fenced.md', '---\nname: "Ada"\ndescription: "An agent."\ntools: Read\n---\n')
        self.assert_flags('fenced with ---, which GitHub shows as a table')

    def test_a_template_type_outside_a_scaffold(self) -> None:
        self.vault.note('Projects/Site/Overview.md', type='template')
        self.assert_flags("type 'template' outside a .template/ folder")

    def test_a_copied_readme_takes_its_real_type(self) -> None:
        # A venture's README.md is copied from the scaffold's, which is typed template; the copy is the folder's note.
        self.vault.note('Ventures/.template/README.md', type='template')
        self.assertEqual(self.lint().returncode, 0)
        self.vault.note('Ventures/Acme/README.md', type='template')
        self.assert_flags("type 'template' outside a .template/ folder")

    def test_the_old_schema_is_retired(self) -> None:
        self.vault.note('Library/README.md', tags=['library'], layer=1, version='01.00.00')
        result = self.lint()
        for field in ('tags', 'layer', 'version'):
            self.assertIn(f"'{field}' is retired", result.stdout)

    def test_a_note_named_after_its_folder_fails(self) -> None:
        self.vault.note('Memory/README.md')
        self.vault.note('Memory/Context/README.md')
        self.vault.note('Library/.template/Division.md', type='template')
        self.assertEqual(self.lint().returncode, 0, 'every folder explains itself in its README.md')
        self.vault.note('Memory/Context/Context.md')
        self.assert_flags("a note named after its folder repeats the folder's README.md")
        self.assert_flags("a note named after its folder repeats the folder's README.md", 'Memory/Context/Context.md')

    def test_a_readme_is_a_note_held_to_the_schema(self) -> None:
        self.vault.write('Memory/README.md', '# Memory\n')
        self.assert_flags('no frontmatter block')
        self.assert_flags('no frontmatter block', 'Memory/README.md')

    def test_a_readme_without_the_page_format_is_flagged(self) -> None:
        # A folder's README.md is a page (Note-Schema.md): its centered header and its footer are required.
        self.vault.write('Library/README.md', '<!--\ntitle: "x"\ndescription: "y"\ntype: "index"\n-->\n\n# Library\n')
        self.assert_flags("a folder's README.md is a page")
        self.vault.note('Library/README.md')
        self.vault.note('Library/Holding.md', body='# Holding\n', type='reference', keywords=['freshness/timeless'])
        self.assertEqual(self.lint().returncode, 0, 'a note that is not a README carries no page format')

    def test_only_a_record_or_a_template_adds_fields(self) -> None:
        self.vault.note('Library/README.md', lens='wide')
        self.assert_flags("'lens' is not one of a note's fields")
        self.vault.note('Library/README.md', type='record', lens='wide', id='in-idea-1')
        self.assertEqual(self.lint().returncode, 0)

    def test_keywords_stay_few(self) -> None:
        self.vault.note('Library/README.md', keywords=[f'term {i}' for i in range(9)])
        self.assert_flags('9 keywords')

    def test_a_library_holding_carries_one_freshness_token(self) -> None:
        self.vault.note('Library/Arts/Paint.md', type='reference', keywords=['pigment'])
        self.assert_flags('a Library holding carries one freshness token')
        self.vault.note('Library/Arts/Paint.md', type='reference', keywords=['freshness/timeless', 'pigment'])
        self.vault.note('Library/Arts/README.md', keywords=['painting'])
        self.assertEqual(self.lint().returncode, 0, "a folder's README.md is no holding")

    def test_a_scaffold_carries_no_wikilinks(self) -> None:
        self.vault.note('Library/.template/Card.md', body='See [[Library]].\n', type='template')
        self.assert_flags('a scaffold carries no wikilinks')

    def test_a_scaffold_folders_readme_carries_no_wikilinks(self) -> None:
        self.vault.note('Ventures/.template/Sales/README.md', body='See [[Ventures/README|Ventures]].\n',
                        type='template')
        self.assert_flags('a scaffold carries no wikilinks')

    def test_underscores_and_em_dashes(self) -> None:
        self.vault.note('Library/Snake_Case.md', body='A dash \u2014 here.\n')
        result = self.lint()
        self.assertIn('the file name has an underscore', result.stdout)
        self.assertIn('em dash', result.stdout)

    def test_a_session_summary_is_named_for_the_time_it_was_filed(self) -> None:
        # update-vault.py sorts a tier by name: any other name sorts after every digit, so it
        # would be read first at every start and never move down a tier.
        self.vault.note('Memory/Context/Current/README.md')
        self.vault.note('Memory/Context/Current/20260101-093000.md', type='record')
        self.vault.note('Memory/Context/Recent/20251231-180000-1.md', type='record')
        self.vault.note('Memory/Context/Archive/2025/2025 Digest.md', type='record')
        self.assertEqual(self.lint().returncode, 0, self.lint().stdout)
        self.vault.note('Memory/Context/Current/Session 2025-06-01.md', type='record')
        self.vault.note('Memory/Context/Recent/2026-01-01.md', type='record')
        result = self.lint()
        self.assertEqual(result.returncode, 1)
        for name in ('Memory/Context/Current/Session 2025-06-01.md', 'Memory/Context/Recent/2026-01-01.md'):
            self.assertIn(f'{name}: a session summary is named YYYYMMDD-HHMMSS.md', result.stdout)
        self.assertIn('2 problems.', result.stderr)

    def test_a_dated_entry_leads_with_its_date(self) -> None:
        for rel in ('Memory/Decisions/2026-05-switched-to-llc.md', 'Memory/Insights/2026-05-mornings-go-better.md',
                    'Memory/Events/2026-05-17-first-met-dana.md', 'Memory/Entities/People/Dana Smith.md',
                    'Memory/Decisions/README.md'):
            self.vault.note(rel, type='record' if not rel.endswith('README.md') else 'index')
        self.assertEqual(self.lint().returncode, 0, self.lint().stdout)
        self.vault.note('Memory/Decisions/Switched to an LLC.md', type='record')
        self.vault.note('Memory/Events/2026-05-first-met-dana.md', type='record')
        result = self.lint()
        self.assertIn('Memory/Decisions/Switched to an LLC.md: an entry here is named YYYY-MM-slug.md', result.stdout)
        self.assertIn('Memory/Events/2026-05-first-met-dana.md: an entry here is named YYYY-MM-DD-slug.md', result.stdout)
        self.assertIn('2 problems.', result.stderr)

    def test_a_name_a_wikilink_cannot_carry(self) -> None:
        # update-vault.py lists an entry as [[folder/name|name]]: a # would end the link's target there.
        self.vault.note('Memory/Entities/Organizations/C# User Group.md', type='record')
        self.vault.note('Projects/Reading/Notes [draft].md', type='record')
        self.vault.note('Memory/Entities/Organizations/AT&T.md', type='record')
        result = self.lint()
        self.assertEqual(result.returncode, 1)
        self.assertIn('Memory/Entities/Organizations/C# User Group.md: the file name holds #, which a wikilink cannot carry',
                      result.stdout)
        self.assertIn('Projects/Reading/Notes [draft].md: the file name holds [ ], which a wikilink cannot carry', result.stdout)
        self.assertNotIn('AT&T', result.stdout)

    def test_a_copy_that_was_never_filled_in(self) -> None:
        # A scaffold copied and left as it came: its copy note, its bracketed prompts and its
        # scaffold keyword would each reach the catalog as if they were content.
        self.vault.note('Memory/Entities/People/Jane Doe.md', type='record',
                        body='<!-- On copying: save this as Memory/Entities/People/<First Last>.md. -->\n\n# Jane Doe\n')
        self.vault.note('Ventures/Acme/Overview.md', title='[Company] - Overview', type='reference',
                        description='The profile of [Company], and [when to read it].',
                        keywords=['[other name for the company]', 'template', 'acme'])
        result = self.lint()
        self.assertEqual(result.returncode, 1)
        self.assertIn("Memory/Entities/People/Jane Doe.md: the scaffold's `On copying:` note is still here", result.stdout)
        self.assertIn("Ventures/Acme/Overview.md: the title still holds a scaffold's prompt, [Company]", result.stdout)
        self.assertIn("the description still holds a scaffold's prompt, [Company] [when to read it]", result.stdout)
        self.assertIn("keyword '[other name for the company]' is a scaffold's prompt", result.stdout)
        self.assertIn("the keyword 'template' marks a scaffold; drop it from the copy", result.stdout)
        self.assertIn('5 problems.', result.stderr)

    def test_a_scaffold_keeps_its_prompts(self) -> None:
        self.vault.note('Memory/.template/Person.md', title='[Person Name]', type='template',
                        description='[Who this person is to the owner.]', keywords=['[nickname]', 'template'],
                        body='<!-- On copying: save this as Memory/Entities/People/<First Last>.md. -->\n\n# [Person Name]\n')
        self.assertEqual(self.lint().returncode, 0, self.lint().stdout)

    def test_a_venture_copied_with_only_its_type_changed_fails(self) -> None:
        # The real scaffold, copied whole and given a type that passes: every other step skipped.
        copy = self.vault.path('Ventures/Example-Company')
        shutil.copytree(ROOT / 'Ventures' / '.template', copy)
        notes = sorted(copy.rglob('*.md'))
        for note in notes:
            note.write_text(re.sub(r"(?m)^type: ['\"]template['\"]$", "type: 'reference'", note.read_text(encoding='utf-8')),
                            encoding='utf-8')
        result = self.lint()
        self.assertEqual(result.returncode, 1)
        for note in notes:
            name = note.relative_to(self.vault.root).as_posix()
            self.assertIn(f"{name}: the scaffold's `On copying:` note is still here", result.stdout)
        self.assertIn("Ventures/Example-Company/Overview.md: the title still holds a scaffold's prompt, [Company]", result.stdout)
        self.assertIn("the keyword 'template' marks a scaffold", result.stdout)

    def test_a_field_one_slip_away_from_a_real_one(self) -> None:
        # A record may add fields of its own, so a slip would pass as one, and vault.is_stale would
        # never see the status that was meant: the start card would keep listing an overridden summary.
        self.vault.note('Memory/Context/Current/20260101-093000.md', type='record', stauts='deprecated')
        self.vault.note('Memory/Decisions/2026-05-switched-to-llc.md', type='record', keyword=['llc'], tittle='Switched')
        self.vault.note('Library/Other.md', descripton='A slip in a note that may add no field at all.')
        result = self.lint()
        self.assertEqual(result.returncode, 1)
        self.assertIn("'stauts' reads as a slip for 'status'", result.stdout)
        self.assertIn("'keyword' reads as a slip for 'keywords'", result.stdout)
        self.assertIn("'tittle' reads as a slip for 'title'", result.stdout)
        self.assertIn("'descripton' reads as a slip for 'description'", result.stdout)
        self.assertIn('4 problems.', result.stderr)

    def test_a_records_own_fields_still_pass(self) -> None:
        self.vault.note('Inbox/Research/Heat Pumps.md', type='record', review_by='2026-02-14')
        self.vault.note('Inbox/Ideas/Solar Shed.md', type='record', id='idea-0001', statement='A shed that powers itself.',
                        lifecycle='raw', ice='6', elo='1500', lens='inversion', parents='idea-0000', serves='the workshop')
        self.assertEqual(self.lint().returncode, 0, self.lint().stdout)

    LOG = ('# Log\n\n## Log Entries\n\n{entries}\n## Open Loops\n\n### Not an entry, outside the section\n\n'
           'Status: Open\n')

    def log(self, entries: str):
        self.vault.note('Memory/Log.md', body=self.LOG.format(entries=entries), type='record')
        return self.lint()

    def test_a_log_entry_the_open_loops_view_can_read_passes(self) -> None:
        result = self.log('### 2026-01-03 - Renew the passport\n\nThe status of the open house came up too.\n'
                          'Importance: 3\n**Status:** Open\n\n'
                          '### 2026-01-02 - Call the bank\n\n- Importance: 5\n- **Status:** Open\n\n'
                          '### 2026-01-01 - Done thing\n\n**Importance:** 1\n**Status:** Resolved (2026-01-03)\n')
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_a_log_heading_without_its_date_is_flagged(self) -> None:
        result = self.log('### November 8 - A free-form date\n\n### 2026-01-02 Call the bank\n\n### 2026-01-01 - Fine\n')
        self.assertEqual(result.returncode, 1)
        # Lines are counted in the file as written, its frontmatter included.
        self.assertIn('Memory/Log.md: line 11: a Log entry is headed `### YYYY-MM-DD - Title`', result.stdout)
        self.assertIn('this one reads `### 2026-01-02 Call the bank`', result.stdout)
        self.assertIn('2 problems.', result.stderr)

    def test_importance_is_one_number_from_one_to_five(self) -> None:
        result = self.log('### 2026-01-03 - One\n\nImportance: 11\n\n### 2026-01-02 - Two\n\n- Importance: high\n\n'
                          '### 2026-01-01 - Three\n\nImportance: 0\n')
        self.assertEqual(result.returncode, 1)
        for line, value in ((13, 'Importance: 11'), (17, '- Importance: high'), (21, 'Importance: 0')):
            self.assertIn(f'Memory/Log.md: line {line}: importance is one number from 1 to 5', result.stdout)
            self.assertIn(f'this line reads `{value}`', result.stdout)
        self.assertIn('3 problems.', result.stderr)

    def test_a_status_line_the_open_loops_view_would_miss_is_flagged(self) -> None:
        # Each of these reads as an open thread to a person and as nothing to update-vault.py.
        result = self.log('### 2026-01-03 - One\n\n**Status**: Open\n\n### 2026-01-02 - Two\n\nStatus: Open\n\n'
                          '### 2026-01-01 - Three\n\n- *Status:* open, waiting on the bank\n')
        self.assertEqual(result.returncode, 1)
        for line in (13, 17, 21):
            self.assertIn(f'Memory/Log.md: line {line}: an open thread is marked `**Status:** Open`', result.stdout)
        self.assertIn('3 problems.', result.stderr)

    def test_only_the_memory_log_is_held_to_the_form(self) -> None:
        self.vault.note('Projects/Site/Log.md', body='# Log\n\n## Log Entries\n\n### Sometime - Free\n\nStatus: Open\n',
                        type='record')
        self.assertEqual(self.lint().returncode, 0, self.lint().stdout)

    def test_only_githubs_five_callouts(self) -> None:
        self.vault.note('Memory/Log.md', body='# Log\n\n> [!NOTE]\n> **Kept.**\n> Fine.\n\n'
                        '```markdown\n> [!tip] An example, inside code\n```\n')
        self.assertEqual(self.lint().returncode, 0)
        self.vault.note('Memory/Log.md', body='# Log\n\n> [!warning] Titled\n> Body.\n\n> [!TIP] Titled too\n')
        result = self.lint()
        self.assertIn('callout [!warning] Titled does not render on GitHub', result.stdout)
        self.assertIn('callout [!TIP] Titled too does not render on GitHub', result.stdout)

    def test_one_file_checks_only_that_file(self) -> None:
        self.vault.note('Library/Good.md')
        self.vault.note('Library/Bad.md', description=None)
        result = self.lint('Library/Good.md')
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn('1 note passes.', result.stdout)

    def test_a_file_outside_the_walk_is_skipped(self) -> None:
        self.vault.write('.github/README.md', '# not a note\n')
        self.vault.write('README.md', '# the vault root, a page\n')
        result = self.lint('.github/README.md', 'README.md')
        self.assertEqual(result.returncode, 0)
        self.assertIn('0 notes pass.', result.stdout)
        self.assertEqual(self.lint().returncode, 0)

    def test_a_file_waiting_at_the_inbox_is_not_yet_a_note(self) -> None:
        # Leaving a file at the Inbox root is the safe default (Inbox/README.md): it takes its
        # frontmatter and its clean name when it is sorted, so until then nothing here is held against it.
        self.vault.note('Inbox/README.md')
        self.vault.write('Inbox/call_notes.md', '# Raw \u2014 no frontmatter, and [[Somewhere]]\n')
        self.vault.write('Inbox/Scans/Scans.md', '# A dropped folder, with a file named after it\n')
        result = self.lint()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn('1 note passes.', result.stdout)
        # Named outright it is passed by too, as a file outside the walk is.
        self.assertIn('0 notes pass.', self.lint('Inbox/call_notes.md').stdout)
        # The held libraries are not the waiting room: a report is a note like any other.
        self.vault.write('Inbox/Research/Bare.md', '# no frontmatter\n')
        self.assert_flags('Inbox/Research/Bare.md: no frontmatter block')

    def test_what_git_ignores_is_not_a_note(self) -> None:
        self.vault.write('.gitignore', 'build/\n')
        self.vault.write('Projects/Shed/build/Bare.md', '# no frontmatter\n')
        self.vault.note('Projects/Shed/Plan.md')
        self.vault.init_git()
        result = self.lint()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn('1 note passes.', result.stdout)
        # Named outright, it is skipped like any other file outside the walk.
        self.assertIn('0 notes pass.', self.lint('Projects/Shed/build/Bare.md').stdout)

    def test_a_folder_named_backups_or_template_is_an_ordinary_folder(self) -> None:
        self.vault.write('Projects/Server/Backups/Bare.md', '# no frontmatter\n')
        self.vault.write('Inbox/Backups/2026-01-01/Raw.md', '# a raw copy, never walked\n')
        self.vault.note('Projects/Server/Template/Note.md', type='template')
        result = self.lint()
        self.assertEqual(result.returncode, 1)
        self.assertIn('Projects/Server/Backups/Bare.md: no frontmatter block', result.stdout)
        self.assertIn("Projects/Server/Template/Note.md: type 'template' outside a .template/ folder", result.stdout)
        self.assertNotIn('Inbox/Backups', result.stdout)

    def test_a_missing_file_is_a_usage_error(self) -> None:
        self.assertEqual(self.lint('Nope.md').returncode, 2)

    def test_the_real_vault_passes(self) -> None:
        result = fixtures.subprocess.run([sys.executable, str(fixtures.SCRIPTS / SCRIPT)],
                                         capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main()
