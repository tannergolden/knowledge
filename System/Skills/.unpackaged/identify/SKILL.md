---
name: identify
description: Coverage-driven interviewing that fills and deepens the Profile facets by asking the user about themselves with validated frameworks (Big Five, HEXACO, Schwartz, McAdams life story). Use this whenever the user types /identify, says interview me, fill out my profile, help me populate my Working Style, get to know me better, or asks to confirm unconfirmed profile entries, and proactively when a Profile facet is found thin or template-empty, even when they never say identify. Mixed structured and conversational questions with skip options; writes only an approved proposal batch.
license: proprietary
allowed-tools: Read, Grep, Glob, Bash, Write, Edit, Task, AskUserQuestion
metadata:
  team: Research & Development (R&D)
  version: "01.00.00"
  id: "sy-skill-identify-spec"
  author: "Tanner Golden"
  status: "active"
---

# 🪪 Identify

Identify fills and deepens the `Profile/` facets by interviewing the user about themselves: it reads the engine's coverage report to find what is thin, plans a short mixed-delivery interview from validated frameworks, and turns the answers into a reviewed proposal batch the user approves line by line. The one standard, which wins every conflict: **nothing enters `Profile/` unapproved or unmarked**. Every write is either a verbatim-traceable self-report or an inference carrying the full provenance marker, and no write happens before the user says yes.

> Operating doctrine lives in `references/`. Read `references/interviewing.md` before asking anything, `references/question-maps.md` before planning the interview, and `references/provenance.md` before composing or writing a single line.

## Modes

| Mode | Trigger | What it does |
|------|---------|--------------|
| **interview** | `/identify`, "interview me", "get to know me better", "fill out my profile", or a facet found thin in passing | Coverage-driven: `profile coverage` picks the target facet, then the full pipeline runs |
| **confirm** | "confirm my unconfirmed profile entries", or a confirm sweep is due | Targets existing `unconfirmed` markers: short confirmation asks, then markers shortened to `confirmed` or the line corrected, through the same batch, review, and approval path |
| **facet-named** | The caller names a facet ("let's fill in my Working Style", "/identify Health") | Caller-named wins over coverage; the pipeline runs scoped to that facet, consent gate included when it is sensitive |

## The architecture it serves

This skill composes the **Research & Development (R&D)** team (`Ventures/Agent Resources (AR)/Research & Development (R&D)/`), the home of its embodied lead. Three seats, all reuse, constant across runs: the skill **embodies Adeline** (UX and Design Research Lead) as the interviewer, so only the top-level context converses and calls the question tool; **Calvin** (Writer, `Inbox/Faculties/Editorial/`) composes the proposal batch; **Sterling** (Standards Reviewer, `Inbox/Faculties/Research/`) reviews it blind against Article IV. Calvin and Sterling are cross-home references, the research skill's Marian convention: `metadata.team` names the embodied lead's home team, and the two dispatched seats are referenced by name from their own homes. Nothing is copied locally; on Publish the referenced agents are vendored into this skill's `agents/` so the package is self-contained. Seats, briefs, verdict vocabulary, and rejected alternatives: `references/roster.md`.

## The interview pipeline

1. **Preflight.** Read `Constitution.md`, `Instructions.md`, and `Profile/Profile.md` in full, then `references/interviewing.md`, `references/question-maps.md`, and `references/provenance.md`. Announce as Adeline embodied, no handoff ceremony: curious, grounded, one line of what is about to happen.
2. **Coverage call.** `python3 System/brain.command profile coverage --json`. Take its `target` unless the caller named a facet; caller-named wins.
3. **Facet pick + consent gate.** Sensitive facets (Health, Finances, Values, Relationships) open only on opt-in: one question-tool ask offering that facet, the two next-thinnest non-sensitive alternatives, and "not today". Non-sensitive facets get a one-line announcement ("Working Style is still template; about 10 questions, say stop anytime").
4. **Section detail + plan.** `profile coverage "<facet>" --json` for per-section gaps; read the facet file; search `unconfirmed` scoped to it. Fill `templates/interview-plan.md`: max 2 confirm-pass items for existing unconfirmed markers first, then the highest-signal unfilled sections per `references/question-maps.md`; Snapshot always last; about 10 questions (6 to 8 for sensitive facets).
5. **Interview loop.** Scaled items via the question tool, batched up to 4 per call within one framework block, max 4 options each; every sensitive-facet question and sensitive-adjacent item carries an explicit "Prefer not to say" option (never the tool's free-text Other as the skip). Narrative items one at a time in chat prose; simple fact clusters as one compact chat question. Skips honored silently: no follow-up, no recording of the refusal anywhere in the vault. Keep the session ledger: verbatim answers tagged stated; lead observations tagged observed with confidence.
6. **Checkpoint at about 10 questions** (question tool): continue 10 more, switch to the next-thinnest facet, or wrap to proposals. Any stop signal goes straight to step 7 with whatever was gathered.
7. **Compose (dispatch Calvin).** Self-contained brief in the `references/roster.md` shape: the interview ledger inline, the target facet file paths, `references/provenance.md`, and `templates/proposal-batch.md`. Calvin returns the batch and persists nothing.
8. **Review (dispatch Sterling, blind).** Inputs: the batch, `Profile/Profile.md`, Constitution 4.4, `references/provenance.md`; never the interview reasoning or Calvin's brief. One ledger row per proposal: BLOCK, REVISE, or CLEAR. Verdicts apply mechanically: REVISE applied, BLOCK dropped or re-marked, one round only.
9. **Present the proposal batch** in chat in the `templates/proposal-batch.md` shape: per-file numbered diffs with markers visible, then Memory promotion offers, then skipped items (shown once, never persisted). Approval is explicit and line-item capable: approve all, approve except N, or per item. No answer, no write.
10. **Write path (the skill is the sole writer).** Each approved change to an existing file: backup via the engine, then Edit, then bump that file's `updated:` to today. Each approved entry: `profile add <belief|goal|skill|condition> "Title"`, then Edit the scaffolded body (a fresh scaffold needs no pre-backup). After all writes: `profile sync`, `lint` on every touched file (the exit gate, must pass), and `sync` for Finder tags on new files. Facet files are not core files (no `version:` field): no changelog entry, no `bump`.
11. **Memory promotions.** For each approved promotion, run the engine command and nothing else (`memory add person|decision|date`, or `remember` for a dated happening). Constitution 2.7 is absolute: the record never lands in `Profile/`; Profile keeps only the user-fact phrasing.
12. **Closing.** Report written, confirmed, and deferred counts; offer (never silently) a `remember` log line for the session; name the next-thinnest facet as the natural next run; confirm lint is clean. No unapproved text remains anywhere.

## Dispatch scaling

Posture scales by sensitivity, not by roster size; the seats are constant.

- **Non-sensitive facet run** (Working Style, Personality, Biography, Lifestyle, Skills, Preferences, Goals, Focus): announce and go; about 10 questions to the checkpoint; Calvin then Sterling on the batch.
- **Sensitive facet run** (Health, Finances, Values, Relationships): consent gate first, 6 to 8 questions, explicit skip on every item, gentlest register; Calvin then Sterling on the batch, and Sterling's blind review is non-negotiable here.
- **Aborted run** (stop before any answers): dispatch nobody; close with the coverage picture and the offer to run later.
- Every run that produces a proposal batch dispatches Calvin then Sterling, Sterling always and always blind. There is no batch too small to review.

## Conformance with the live BRAIN

Read `Instructions.md` and `Constitution.md` and the namesake of every folder written into (`Profile/Profile.md` hosts Article IV, the law governing every write this skill makes). Back up before editing any existing vault file; new engine-scaffolded files need no backup. Reference vault files by plain path, never wikilinks. `brain.command lint` on every touched file is the exit gate. Use the engine for everything it can do: `profile coverage` to target, `profile add` to scaffold entries, `profile sync` after entry writes, `memory add` and `remember` for promotions, `backup` before edits.

## Quality bars

- **Nothing enters `Profile/` unapproved or unmarked**, the one standard. Unmarked lines must be verbatim-traceable to a ledger answer; when in doubt, mark (`references/provenance.md`).
- Provenance tokens are exact and machine-queryable: `observed` | `confirmed` | `reviewed` with ISO date, optional `confidence: low|medium|high`, proposal flag `unconfirmed`. `brain.command search unconfirmed` must find every pending proposal afterward.
- Skips are silent and stateless: never probed again, never recorded anywhere in the vault, session-only.
- One construct per question, non-leading, 3-point scales plus skip where scaled; hard caps (checkpoint at about 10, 6 to 8 on sensitive facets).
- No em dashes anywhere (Constitution 9.1); the shared validator fails on the character.
- Tools declared exactly: `allowed-tools` is the minimal set the workflow actually calls.
- Memory-shaped facts (people, events, dates, decisions) route to Memory promotions, never into a Profile diff (Constitution 2.7).

## Boundaries

- Stay within Profile interviewing and the approved batch write. Never write unapproved or unproposed text, never record a refusal, never open a sensitive facet without opt-in, never re-probe a skip, never store people, events, dates, or decisions in `Profile/` (they are Memory promotions), and never edit `Memory/` beyond the approved promotion commands. Confirm-first governs every write; back up before editing existing files; never create or delete top-level folders.
- vs **research**: questions about the world route to research; identify asks the user about themselves. "Research Big Five versus HEXACO" is research, not identify.
- vs **editorial**: a prose file under instruction is editorial's; identify writes only the approved proposal batch into `Profile/`.
- vs the **normal 4.1 write path**: a user-dictated update ("update my Focus: heads-down on the launch") is a direct edit under Article 4.1, no interview needed; identify is for eliciting, not transcribing.
