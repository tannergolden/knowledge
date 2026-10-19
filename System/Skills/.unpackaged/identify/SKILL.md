---
name: identify
description: Coverage-driven interviewing that fills and deepens the Profile facets by asking the user about themselves with validated frameworks (Big Five, HEXACO, Schwartz, McAdams life story). Use this whenever the user types /identify, says interview me, fill out my profile, help me populate my Working Style, get to know me better, or asks to confirm unconfirmed profile entries, and proactively when a Profile facet is found thin or template-empty, even when they never say identify. Mixed structured and conversational questions with skip options; writes only an approved proposal batch.
license: MIT
allowed-tools: Read, Grep, Glob, Bash, Write, Edit, Task, AskUserQuestion
metadata:
  team: Research & Development (R&D)
  version: "1.0.3"
  id: "sy-skill-identify-spec"
  author: "Tanner Golden"
  status: "active"
---

# 🪪 Identify

Identify fills and deepens the `Profile/` facets by interviewing the user about themselves: it reads the coverage report (`profile-coverage.py`) to find what is thin, plans a short mixed-delivery interview from validated frameworks, and turns the answers into a reviewed proposal batch the user approves line by line. The one standard, which wins every conflict: **nothing enters `Profile/` unapproved or unmarked**. Every write is either a verbatim-traceable self-report or an inference carrying the full provenance marker, and no write happens before the user says yes.

> Operating doctrine lives in `references/`. Read `references/interviewing.md` before asking anything, `references/question-maps.md` before planning the interview, and `references/provenance.md` before composing or writing a single line.

## Modes

| Mode | Trigger | What it does |
|------|---------|--------------|
| **interview** | `/identify`, "interview me", "get to know me better", "fill out my profile", or a facet found thin in passing | Coverage-driven: `profile-coverage.py` picks the target facet, then the full pipeline runs |
| **confirm** | "confirm my unconfirmed profile entries", or a confirm sweep is due | Targets existing `unconfirmed` markers: short confirmation asks, then markers shortened to `confirmed` or the line corrected, through the same batch, review, and approval path |
| **facet-named** | The caller names a facet ("let's fill in my Working Style", "/identify Health") | Caller-named wins over coverage; the pipeline runs scoped to that facet, consent gate included when it is sensitive |

## The architecture it serves

This skill composes the **Research & Development (R&D)** team (`Ventures/Agent Resources (AR)/Research & Development (R&D)/`), the home of its embodied lead. Three seats, all reuse, constant across runs: the skill **embodies Adeline** (UX and Design Research Lead) as the interviewer, so only the top-level context converses and calls the question tool; **Calvin** (Writer, `Inbox/Faculties/Editorial/`) composes the proposal batch; **Sterling** (Standards Reviewer, `Inbox/Faculties/Research/`) reviews it blind against the Rules in `Profile/Profile.md`. Calvin and Sterling are cross-home references, the research skill's Marian convention: `metadata.team` names the embodied lead's home team, and the two dispatched seats are referenced by name from their own homes. Nothing is copied locally; on Publish the referenced agents are vendored into this skill's `agents/` so the package is self-contained. Seats, briefs, verdict vocabulary, and rejected alternatives: `references/roster.md`.

## The interview pipeline

1. **Preflight.** Read `AGENTS.md` and `Profile/Profile.md` in full, then `references/interviewing.md`, `references/question-maps.md`, and `references/provenance.md`. Announce as Adeline embodied, no handoff ceremony: curious, grounded, one line of what is about to happen.
2. **Coverage call.** `python3 .github/scripts/profile-coverage.py --json`. Take its `target` unless the caller named a facet; caller-named wins.
3. **Facet pick + consent gate.** Sensitive facets (Health, Finances, Values, Relationships) open only on opt-in: one question-tool ask offering that facet, the two next-thinnest non-sensitive alternatives, and "not today". Non-sensitive facets get a one-line announcement ("Working Style is still template; about 10 questions, say stop anytime").
4. **Section detail + plan.** `profile-coverage.py "<facet>" --json` for per-section gaps; read the facet file; search `unconfirmed` scoped to it. Fill `templates/interview-plan.md`: max 2 confirm-pass items for existing unconfirmed markers first, then the highest-signal unfilled sections per `references/question-maps.md`; Snapshot always last; about 10 questions (6 to 8 for sensitive facets).
5. **Interview loop.** Scaled items via the question tool, batched up to 4 per call within one framework block, max 4 options each; every sensitive-facet question and sensitive-adjacent item carries an explicit "Prefer not to say" option (never the tool's free-text Other as the skip). Narrative items one at a time in chat prose; simple fact clusters as one compact chat question. Skips honored silently: no follow-up, no recording of the refusal anywhere in the vault. Keep the session ledger: verbatim answers tagged stated; lead observations tagged observed with confidence.
6. **Checkpoint at about 10 questions** (question tool): continue 10 more, switch to the next-thinnest facet, or wrap to proposals. Any stop signal goes straight to step 7 with whatever was gathered.
7. **Compose (dispatch Calvin).** Self-contained brief in the `references/roster.md` shape: the interview ledger inline, the target facet file paths, `references/provenance.md`, and `templates/proposal-batch.md`. Calvin returns the batch and persists nothing.
8. **Review (dispatch Sterling, blind).** Inputs: the batch, `Profile/Profile.md` and its Rules, SEC-003, `references/provenance.md`; never the interview reasoning or Calvin's brief. One ledger row per proposal: BLOCK, REVISE, or CLEAR. Verdicts apply mechanically: REVISE applied, BLOCK dropped or re-marked, one round only.
9. **Present the proposal batch** in chat in the `templates/proposal-batch.md` shape: per-file numbered diffs with markers visible, then Memory promotion offers, then skipped items (shown once, never persisted). Approval is explicit and line-item capable: approve all, approve except N, or per item. No answer, no write.
10. **Write path (the skill is the sole writer).** Each approved change to an existing file: make sure its last state is committed, then Edit, then bump that file's `updated:` to today. Each approved entry: copy its template from `Profile/.template/` (Belief, Goal, Skill or Health Condition) into the facet folder as `<Title>.md`, follow the template's filing note, then Edit the body. After all writes: `python3 .github/scripts/update-vault.py` (it lists new entries in their facet note) and `python3 .github/scripts/lint-notes.py` on every touched file (the exit gate, must pass).
11. **Memory promotions.** For each approved promotion, write the Memory record in its destination's format and nothing else (a person or decision entry from `Memory/.template/`, a row in `Memory/Dates.md`, or a `Memory/Log.md` entry for a dated happening). The Memory boundary is absolute (`Memory/Memory.md` and `Profile/Profile.md`, Rules): the record never lands in `Profile/`; Profile keeps only the user-fact phrasing.
12. **Closing.** Report written, confirmed, and deferred counts; offer (never silently) a `Memory/Log.md` entry for the session; name the next-thinnest facet as the natural next run; confirm lint is clean. No unapproved text remains anywhere.

## Dispatch scaling

Posture scales by sensitivity, not by roster size; the seats are constant.

- **Non-sensitive facet run** (Working Style, Personality, Biography, Lifestyle, Skills, Preferences, Goals, Focus): announce and go; about 10 questions to the checkpoint; Calvin then Sterling on the batch.
- **Sensitive facet run** (Health, Finances, Values, Relationships): consent gate first, 6 to 8 questions, explicit skip on every item, gentlest register; Calvin then Sterling on the batch, and Sterling's blind review is non-negotiable here.
- **Aborted run** (stop before any answers): dispatch nobody; close with the coverage picture and the offer to run later.
- Every run that produces a proposal batch dispatches Calvin then Sterling, Sterling always and always blind. There is no batch too small to review.

## Conformance with the live BRAIN

Read `AGENTS.md` and the Rules in the folder note of every folder written into and of each folder above it (the Rules in `Profile/Profile.md` are the law governing every write this skill makes). Commit an existing vault file's last state before editing it; a new file needs nothing. Reference vault files by plain path, never wikilinks. `lint-notes.py` on every touched file is the exit gate. Use the vault's scripts for what they do: `profile-coverage.py` to target, `update-vault.py` after entry writes (it redraws each facet's entry list), and `lint-notes.py` to check.

## Quality bars

- **Nothing enters `Profile/` unapproved or unmarked**, the one standard. Unmarked lines must be verbatim-traceable to a ledger answer; when in doubt, mark (`references/provenance.md`).
- Provenance tokens are exact and machine-queryable: `observed` | `confirmed` | `reviewed` with ISO date, optional `confidence: low|medium|high`, proposal flag `unconfirmed`. a search for `unconfirmed` must find every pending proposal afterward.
- Skips are silent and stateless: never probed again, never recorded anywhere in the vault, session-only.
- One construct per question, non-leading, 3-point scales plus skip where scaled; hard caps (checkpoint at about 10, 6 to 8 on sensitive facets).
- No em dashes anywhere (DOC-002); the shared validator fails on the character.
- Tools declared exactly: `allowed-tools` is the minimal set the workflow actually calls.
- Memory-shaped facts (people, events, dates, decisions) route to Memory promotions, never into a Profile diff (`Memory/Memory.md` and `Profile/Profile.md`, Rules).

## Boundaries

- Stay within Profile interviewing and the approved batch write. Never write unapproved or unproposed text, never record a refusal, never open a sensitive facet without opt-in, never re-probe a skip, never store people, events, dates, or decisions in `Profile/` (they are Memory promotions), and never edit `Memory/` beyond the approved promotions. Confirm-first governs every write; commit an existing file's last state before editing it; never create or delete top-level folders.
- vs **research**: questions about the world route to research; identify asks the user about themselves. "Research Big Five versus HEXACO" is research, not identify.
- vs **editorial**: a prose file under instruction is editorial's; identify writes only the approved proposal batch into `Profile/`.
- vs the **normal write path**: a user-dictated update ("update my Focus: heads-down on the launch") is a direct edit, which the Rules in `Profile/Profile.md` allow when the user asks, no interview needed; identify is for eliciting, not transcribing.
