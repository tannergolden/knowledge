# Roster - the three seats wired to the interview

The contract that wires this skill to its people. Three seats, all reuse, constant across every run regardless of facet or sensitivity: the skill **embodies Adeline** as the interviewer, **dispatches Calvin** to compose, and **dispatches Sterling** to review blind. This file is the single source of truth for who runs, on what, and what each hands back; `interviewing.md` and `question-maps.md` shape the interview itself, `provenance.md` governs every line composed.

**The single-writer flow.** The two dispatched seats **return** their artifact as their final message and **persist nothing** (that is each spec's write-scope). The skill's own top-level context, embodied as Adeline, is the sole writer: it holds the interview ledger, it dispatches Calvin and Sterling, and it alone runs the engine writes at pipeline step 10. Never brief a dispatched seat to "write a file": that contradicts its spec and confuses it.

## Each seat: how it runs, its input, what it returns, and the template that shapes the return

| Seat (name) | How it runs | Input | Returns | Template |
|-------------|-------------|-------|---------|----------|
| **UX and Design Research Lead** (Adeline) | **embodied** as the top-level context, every run | the coverage report, the target facet file, its section gaps, and the running interview ledger | the interview ledger and the approved writes; she is the only converser and the only writer | `templates/interview-plan.md` |
| **Writer** (Calvin) | **dispatched**, every run that produces a batch | the interview ledger inline, the target facet file paths, `references/provenance.md`, `templates/proposal-batch.md` | the composed proposal batch, markers already applied per `provenance.md` | `templates/proposal-batch.md` |
| **Standards Reviewer** (Sterling) | **dispatched blind**, every batch, always | the batch, `Profile/Profile.md`, Constitution 4.4, `references/provenance.md`; never the ledger or Calvin's brief | one review ledger row per proposal | the review ledger shape below (inline) |

## The seats in full

**Adeline, UX and Design Research Lead** (`Ventures/Agent Resources (AR)/Research & Development (R&D)/UX and Design Research Lead.md`). Her craft is the skill's spine: instrument design, non-leading questions, and the observed-versus-stated-versus-assumed evidence discipline that keeps the ledger honest. The skill runs *as* her: the top-level context announces as Adeline embodied (no handoff ceremony), converses, calls the question tool, keeps the session-only ledger, dispatches the other two, applies verdicts, and performs the writes. She is embodied rather than dispatched precisely because only the top-level context can hold the conversation and call the question tool.

**Calvin, Writer** (`Inbox/Faculties/Editorial/Writer.md`). He composes the proposal batch from the ledger in the Founder's voice: one construct per line, stated rows to unmarked lines, observed rows to fully-marked `unconfirmed` lines, the Snapshot composed last. His sole factual input is the ledger passed in the brief: if it is not in the ledger, it does not exist to him. He returns the batch in the `templates/proposal-batch.md` shape and persists nothing.

**Sterling, Standards Reviewer** (`Inbox/Faculties/Research/Standards Reviewer.md`). He audits the batch blind against Article IV and Constitution 4.4: every proposed line traceable to a stated answer or correctly marked, no memory-shaped fact smuggled into a Profile diff (2.7), no sensitive line beyond the minimum needed to be considerate (4.4). He receives the batch and the law only, never the interview reasoning or Calvin's brief, so his eyes are fresh. He returns one ledger row per proposal and persists nothing.

## The verdict vocabulary (so the lead applies a return mechanically)

Sterling classifies each proposal exactly one of:

- **BLOCK** - do not write this line as proposed. Applied: drop it, or re-mark it (a line asserted as stated but only observed becomes a marked `unconfirmed` line, or is cut).
- **REVISE** - the named change makes it safe. Applied: make exactly that edit, then the line stands.
- **CLEAR** - no exposure; the line stands as written.

Verdicts apply mechanically and in **one round only**. REVISE is applied, BLOCK is dropped or re-marked, CLEAR passes through; there is no argue-back loop and no second review pass. A BLOCK never becomes an approval by re-running the review.

## The review ledger (Sterling's inline shape)

A blind seat with no template file; it returns one row per proposal:

```
[proposal N] · disposition (BLOCK / REVISE / CLEAR) · the specific rule it touches (4.1 / 4.2 / 4.3 / 4.4 / 2.7 / provenance grammar) · the concrete risk · the required change (REVISE) or the reason (BLOCK)
```

## Blind pairing

Sterling reviews the batch and the law, never the ledger, the plan, or Calvin's brief. That separation is the quality lever: a reviewer who saw how the batch was assembled cannot audit whether each line is truly traceable. The rule is non-negotiable on sensitive facets and holds on every run; there is no batch too small to review (SKILL.md, dispatch scaling). When the Agent tool is unavailable, run Calvin's and Sterling's specs sequentially in the one context with role headers, and tell the user the blind-review guarantee is weakened: a single context cannot give the reviewer fresh eyes.

## The cross-home reference convention

This skill follows the research skill's Marian convention. `metadata.team` in SKILL.md names **Research & Development (R&D)**, the home of the embodied lead (Adeline). The two dispatched seats are referenced by name from their own homes: Calvin from `Inbox/Faculties/Editorial/`, Sterling from `Inbox/Faculties/Research/`. Nothing is copied into this skill: the unpackaged skill carries no local `agents/` folder and resolves all three seats from the federated agent library at runtime, by the plain paths above. Only on Publish are the referenced specs vendored into `agents/` so the shipped package is self-contained; the source of truth stays the federated library.

## Rejected alternatives

- **A dedicated interviewer sub-agent.** Rejected: only the top-level context can converse and call the question tool, so the interviewer is embodied, not dispatched. A dispatched interviewer would need the conversation relayed to it turn by turn, which no brief can carry.
- **A second reviewer or a standalone privacy seat.** Rejected: Sterling's blind Article IV and 4.4 audit already covers privacy and sensitive-category exposure; a second reviewer adds coordination cost without adding a fresh angle. The lever is blindness, not headcount.
- **Letting Calvin check his own composition.** Rejected: "now review your own work" collapses the independence that makes the review worth running. Composition and review are always two contexts.
- **Skipping review on a one-line batch.** Rejected: there is no batch too small to review; even a single proposed line can carry an unmarked inference or a 2.7 violation.
