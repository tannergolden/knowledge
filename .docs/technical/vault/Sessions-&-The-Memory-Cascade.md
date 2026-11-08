<!--
title: '🔄 SESSIONS & THE MEMORY CASCADE'
description: 'What happens in a session from its first read to its last commit, which session helper serves each step and what each one reads and prints, and how update-vault.py moves summaries from Current to Recent to Archive. Read it when you run the helpers, call one from your own tooling, or change how summaries age.'
type: guide
keywords: [startup, checkpoint, summaries, tiers, hooks, helpers, update-vault, current recent archive]
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🔄 SESSIONS & THE MEMORY CASCADE

<a name="top"></a>

**What a session does from its first read to its last commit, and how its summary ages.**

_Two summaries read at the start, none ever deleted._

</div>

---

## 💡 A Session, Start To Finish

The root [`README.md`](../../../README.md) sets the steps, [`AGENTS.md`](../../../AGENTS.md) holds every
AI to them, and `.github/scripts/session.py` takes the three a script can: it lists what to read,
checks a note once it is written, and tidies up when the work stops.

```mermaid
graph LR
    S["start: read the startup set"] --> I["Sort the Inbox"]
    I --> W["Write, and lint each note"]
    W --> C["Checkpoint the session summary"]
    C --> W
    C --> E["Finish: redraw, check, commit"]
```

| Step       | What happens                                                                                                                     | Helper                                                       | Set by                                    |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------- | :---------------------------------------- |
| Start      | Reads the root `README.md`, `Profile/Working Style.md`, `Memory/Log.md` and the two newest summaries in `Memory/Context/Current/` | `session.py start`                                           | The root `README.md`, How A Session Goes  |
| Sort       | Sorts any file waiting at the Inbox before other work, by `Inbox/README.md`, each move with a yes                                | The card's `INBOX` lines                                     | `Inbox/README.md`                         |
| Orient     | Reads the README of each folder the task touches and of each folder above it, or the catalog                                     | The card's last line                                         | The root `README.md`, How A Session Goes  |
| Write      | Writes each note in its folder's format, and lints it                                                                            | `lint-notes.py "<note>"`, or `session.py after-edit`         | The root `README.md`, Commands            |
| Record     | Records in Memory and the Log what happened, was decided or is due, without being asked                                          | None                                                         | The root `README.md`, How A Session Goes  |
| Checkpoint | Updates the running session summary after each finished task, and writes one before the context runs short                       | None                                                         | `Memory/README.md`, Rules                 |
| Finish     | Redraws what is generated, runs every check, commits, and leaves pushing to the owner                                            | `update-vault.py` and `check-vault.py`, or `session.py stop` | The root `README.md`, What Done Means     |

---

## 🚀 The Start Card

`session.py start` prints paths to read, never their contents, so the card stays short. This is the
template's own card, with no summary written yet and nothing waiting:

```text
Vault startup (README.md, How A Session Goes). The startup set is listed, not inlined:
Read every file on a READ line before substantive work.
READ README.md
READ Profile/Working Style.md
READ Memory/Log.md
No session summaries in Memory/Context/Current yet.
Inbox clear.
Before changing anything in a folder, read its README.md and the README.md of each folder above it.
```

- **`READ` lines** name the startup set, `STARTUP` in `.github/scripts/vault.py`, stable before
  volatile: the root `README.md`, `Profile/Working Style.md` and `Memory/Log.md`, then up to two
  summaries from `Memory/Context/Current/`, newest first by file name, skipping any marked
  `deprecated` or `archived`. When files wait at the Inbox, `Inbox/README.md`, the sorting protocol,
  is listed too.
- **`INBOX` lines** name each loose file outside the held sub-homes (`Reports/`, `Visuals/`, `Ideas/`
  and `Backups/`), then say how many wait and that they are sorted before other work.
- **The last line** says to read the `README.md` of each folder a change touches, and of each folder
  above it, before changing anything there.

---

## 🤖 The Helpers' Contract

The helpers began as the vault's Claude Code hooks. The vault carries no configuration for any one
AI app, only `AGENTS.md`, which every app can read, so nothing wires the helpers: each runs by hand,
or from an app's own hook settings. Every helper exits 0 whatever happens, so a helper never breaks a
session.

| Helper       | Reads                                                                                                          | Does                                                                                                                    | Prints                                                                                                                                                         |
| :----------- | :------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start`      | The vault                                                                                                      | Lists the startup set and the Inbox                                                                                     | The card above                                                                                                                                                 |
| `after-edit` | JSON on standard input naming the file just written at `tool_input.file_path`, from the vault root or absolute | Runs `lint-notes.py` on a Markdown file; skips a path outside the vault and input that is not JSON                      | Nothing when the file passes; otherwise `{"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": "..."}}`, holding each script's findings |
| `stop`       | `git status`                                                                                                   | Only when the working tree has changes, or git cannot tell: runs `update-vault.py`, which writes, then `check-vault.py` | Nothing when all is well; otherwise `{"systemMessage": "..."}`, naming up to five redrawn parts and the first problems                                         |

```bash
python3 .github/scripts/session.py start
echo '{"tool_input": {"file_path": "Memory/Log.md"}}' | python3 .github/scripts/session.py after-edit
python3 .github/scripts/session.py stop
```

---

## 📝 Writing The Session Summary

- **When.** After each finished task, update the running summary, and before the context runs short,
  make sure one is written (`Memory/README.md`, Rules).
- **Where.** Copy `Memory/.template/Session Summary.md` into `Memory/Context/Current/` as
  `YYYYMMDD-HHMMSS.md`, the time of filing, so the names sort by time. Give the copy `type: record`,
  its own title and description, and an H1 with an emoji and the date. It carries no wikilinks.
- **What.** A delta update, in the scaffold's order: its metadata, with who wrote it and the
  session's importance; the current state, as the active changes this session made; what it
  overrides, each override saying in so many words that it supersedes any earlier statement; the
  foundations that still stand; the decisions; the open questions; anything that must be kept word
  for word; and the next steps, last. The scaffold has the sections.
- **How long.** Short: the two newest summaries are read in full at every start. The order keeps the
  active changes near the top and the next steps at the bottom, where
  [Context Assembly](Context-Assembly.md) asks for them.
- **Then** run `python3 .github/scripts/update-vault.py`, which lists the summary in its tier and
  moves the oldest on when the tier is full.

When a new summary overrides an earlier one, mark the earlier one `status: deprecated`: the start
card skips it from then on (`Memory/Context/Current/README.md`).

---

## 🧊 The Memory Cascade

```mermaid
graph LR
    New["A new summary"] --> Cur["Current: up to 3"]
    Cur -->|"the oldest, when over 3"| Rec["Recent: up to 6"]
    Rec -->|"the oldest, when over 6"| Arc["Archive/year: no cap"]
```

`update-vault.py` runs the cascade first, before it draws anything else:

- **Oldest by file name.** A tier's summaries are the Markdown files in its folder other than its
  `README.md`, sorted by name, so `YYYYMMDD-HHMMSS.md` names put the oldest first. While a tier holds more
  than its cap, its oldest moves down one tier.
- **Into the year it names.** From Recent, a summary moves to `Memory/Context/Archive/<year>/`, the
  year read from the first four characters of its name, or `undated` when they are not digits.
- **Never over another file.** A name already taken where it lands gets `-1`, `-2` and so on.
  Nothing is overwritten or deleted.
- **Lists redrawn.** The READMEs of `Current/` and `Recent/` each list their summaries in a
  `brain:tier-summaries` block, redrawn on the same run. The Archive keeps no generated list: it is
  reached by search, and a year may carry a `<year> Digest.md` that links to its summaries, never
  replacing them (`Memory/Context/Archive/README.md`).
- **Checked, not moved, in CI.** `update-vault.py --check` moves nothing, and fails while a tier is
  over its cap: `Current holds 4 summaries; its cap is 3`.

The caps are `TIERS` in `.github/scripts/vault.py`, and the tier notes state them for the reader, so a
change to a cap changes both. Recent and Archive are read on request, ranked by recency, importance
and relevance, so an important summary stays within reach however far it has moved
(`Memory/README.md`).

---

## 🌿 Ending Cleanly

A session is done when `check-vault.py` passes, `update-vault.py` has nothing left to redraw, every
note written carries the schema, the change is committed, and the owner knows which files changed and
what is not yet committed (the root `README.md`, What Done Means). `session.py stop` runs the redraw
and the checks in one step, but commits nothing: the commit is the session's, and the push the
owner's.

---

<div align="center">

**Read the card, checkpoint at every boundary, and finish on a commit.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
