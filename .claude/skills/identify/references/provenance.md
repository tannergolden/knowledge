# Provenance - the law of the mark

The write-marking contract, read before composing or writing a single line. It restates the provenance convention hosted in `Profile/Profile.md` (its Rules and the "Provenance and freshness" section) exactly, so the marker grammar this skill writes is the marker grammar the whole `Profile/` layer already uses. The one standard it serves: **nothing enters `Profile/` unapproved or unmarked**. Every proposed line is either a verbatim-traceable self-report that carries no marker, or an inference that carries the full marker and stays a proposal until the user approves it.

## The two species of line

- **Stated (unmarked).** What the user actually said or selected, verbatim-traceable to a `stated` row in the interview ledger. A self-report is the default and needs no marker; a plain line is a self-reported fact (`Profile/Profile.md`, Provenance and freshness). If a line cannot be traced word-for-word to a ledger answer, it is not stated, and it is not allowed to go in unmarked.
- **Observed or inferred (marked).** What the lead noticed rather than was told: a pattern across answers, a tone, an aside. An inference is written only with the full marker and always as a proposal (`unconfirmed`). The Rules in `Profile/Profile.md` make this absolute: an inference is never presented as a fact. When in doubt, mark.

An assumed claim, one in neither the stated nor the observed column of the ledger, does not exist and is never written in either form (`interviewing.md`, the ledger).

## The marker grammar

The marker is an inline HTML comment appended to the end of the line. It renders invisibly on GitHub and in any Markdown preview but stays in the source, so the fact reads clean while the provenance stays machine-queryable:

```
**Field:** value <!-- observed 2026-07-04 · confidence: medium · unconfirmed -->
```

Three parts, in this fixed order, so the tokens stay filterable across the layer:

1. **State token, with an ISO date.** Exactly one of `observed` | `confirmed` | `reviewed`, followed by a `YYYY-MM-DD` date.
   - `observed` - the AI inferred it from evidence. Always paired with `unconfirmed` when first written.
   - `confirmed` - the user approved it. The date is the confirmation date.
   - `reviewed` - a standing line re-verified later; stamped on drift-prone sections (occupation, current chapter) when confirmed to still hold.
2. **Confidence, optional.** `confidence: low | medium | high` on `observed` lines, grading how strong the evidence is. Omit it on a `confirmed` or `reviewed` line, where confidence is no longer the question.
3. **The proposal flag.** `unconfirmed` marks a line that is a proposal awaiting approval, never treated as established (`Profile/Profile.md`, Rules). Every inference this skill proposes carries it until the user says yes.

The separator between parts is the middle dot ` · `. Never a dash of any kind between marker parts.

## The lifecycle

```
observed + unconfirmed   ->   confirmed   ->   reviewed
(an AI inference,             (the user           (re-verified
 a live proposal)             approved it)         later, on use)
```

- A newly proposed inference is `<!-- observed <date> · confidence: <level> · unconfirmed -->`.
- On the user's approval, the marker shortens to `<!-- confirmed <date> -->` (confidence and the proposal flag both drop), or the marker is removed entirely, since a confirmed fact is just a fact.
- A stated fact never enters this lifecycle: it is unmarked from birth.
- A corrected confirm-pass line becomes a new stated fact and loses its marker; a shrugged one keeps its existing marker untouched.

## Examples

Stated (traceable to a `stated` ledger row, so no marker):

```
- **Default length:** terse; the bottom line first, reasoning only on request.
```

Observed or inferred (a live proposal, fully marked):

```
- **Regulatory focus:** prevention-leaning; frames choices around avoiding downside <!-- observed 2026-07-04 · confidence: low · unconfirmed -->
```

The same line after the user confirms it:

```
- **Regulatory focus:** prevention-leaning; frames choices around avoiding downside <!-- confirmed 2026-07-04 -->
```

A drift-prone standing line, re-verified on use:

```
- **Occupation:** founder, building the BRAIN <!-- reviewed 2026-07-04 -->
```

## The query guarantee

Because the tokens are fixed, the layer stays queryable, and the skill's exit state must satisfy it: after a run, a search for `unconfirmed` returns every pending proposal the run wrote, and nothing that was approved and shortened. A search for `confidence: low` surfaces the weakest inferences for a later re-check. A proposal the user did not approve is either dropped or left carrying `unconfirmed`; it is never quietly promoted by removing the flag without approval.

## The Memory boundary

Memory-shaped facts never land in `Profile/`, in any marker state. A person, an event, a date, or a decision is a **Memory promotion**, not a Profile diff:

- A named person the user leans on -> a person entry in `Memory/Entities/People/`, never a name written into Relationships.
- A dated happening the run surfaced -> a `Memory/Log.md` entry, never an event line in Biography.
- A decision the user reports -> a decision record in `Memory/Decisions/`.

`Profile/` keeps only the user-fact phrasing (the relational style, the durable arc), and the record itself lives in Memory. A fact about the user lives in exactly one place, and that place is `Profile/`; the who, what, when, and which-decision lives in exactly one place, and that place is Memory. The two never carry parallel copies (`Memory/Memory.md` and `Profile/Profile.md`, Rules). Sensitive-category discretion (`Profile/Profile.md`, Rules, and SEC-003) governs both: record the minimum needed to be considerate, never a full account.

## What the mark is not for

- A skip or a refusal is **never** written, in any marker state, anywhere in the vault (`interviewing.md`). The mark records what was proposed, never what was declined.
- A confidence grade is not a hedge to smuggle a guess past approval: `confidence: low` still needs the user's yes, and Sterling's blind review still applies (`roster.md`). Low confidence lowers the bar for how the line is phrased, never for whether it may be written.
