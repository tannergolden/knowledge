# Interviewing - the doctrine of the ask

How identify asks, in Adeline's craft: instrument design before conversation, one construct at a time, the user always free to pass. Read this before asking anything. The per-facet items themselves live in `question-maps.md`; this file is the rules every item obeys regardless of facet.

## Non-leading question craft

- **One construct per item.** A question measures exactly one thing. "Are you organized and deadline-driven?" is two constructs (orderliness, time pressure response) and produces an unusable answer; split it or drop one.
- **No embedded desired answer.** Never signal which option flatters. "Do you value honesty?" answers itself; "When a hard truth would cost you something, what usually wins?" does not. Options are phrased so every option is a respectable self-description.
- **Behavior over self-theory where possible.** "What do you do when plans change last minute?" reads better evidence than "Are you flexible?"; people report behavior more accurately than traits.
- **Self-anchored scales.** Scaled items describe the user to themselves ("Usually true of me"), not against other people ("More than most people"), unless the construct is inherently comparative.
- **Neutral framing on sensitive ground.** Gentle, matter-of-fact wording; no clinical vocabulary, no implied concern. "Worry tends to stick with me" rather than "Do you suffer from anxiety?".
- **Plain language.** No framework jargon in the question itself. The framework names live in the plan and the ledger, never in the user's ear.

## Mixed delivery

Three delivery modes, chosen per item in the plan (the S/P split per facet is in `question-maps.md`):

| Delivery | Used for | Rule |
|----------|----------|------|
| **Question tool (scaled)** | Dials, levels, picks, orderings | Options fixed in the plan; max 4 options; batched (below) |
| **Chat prose (narrative)** | Stories, philosophies, open descriptions | One at a time; ask, then listen; never stacked |
| **Chat fact cluster** | Simple registry facts (name, location, languages) | One compact chat question covering the cluster; the user answers what they want, gaps stay gaps |

- **The 4-option ceiling.** A scaled item carries at most 4 options: a 3-point scale plus "Prefer not to say" where the skip is mandatory, or up to 4 substantive options where it is not. A construct that wants more options than that is delivered as prose with the menu inline, or split into two scaled items within the same call.
- **Batching.** Up to 4 scaled items per question-tool call, and one framework block per call: BFI-2 items batch with BFI-2 items, never with a Schwartz ordering. A narrative prose item is never batched with anything.
- **Prose skip line.** Every prose question on sensitive or sensitive-adjacent ground states it plainly: "say skip and we move on."

## The consent gate (sensitive facets)

Health, Finances, Values, and Relationships never open without opt-in. The gate is one question-tool ask offering exactly: that facet, the two next-thinnest non-sensitive facets by coverage rank, and "not today". Declining is not a skip to record; it is a routing answer. A sensitive run is shorter (6 to 8 questions), gentler, and every single item in it carries the explicit skip option.

## Skips, refusals, and re-probes

- **Skip is honored silently.** No follow-up, no "can I ask why", no rephrasing of the same construct later in the run or in any later run prompted by this one.
- **Never record a refusal.** A skip or refusal is never written anywhere in the vault: not in the batch, not in a marker, not in Memory, not in the session summary. The session-only ledger notes the question id as skipped purely so the run does not re-ask; the note dies with the session.
- **The explicit skip option.** Every question in a sensitive facet and every sensitive-adjacent item elsewhere carries "Prefer not to say" as a real option. Never rely on the question tool's free-text Other as the skip; an option the user must type is not an option.
- **Stop anytime.** Announced at the start of every run. Any stop signal ("stop", "enough", "let's do this later", visible fatigue) collapses the run immediately to the proposal step with whatever was gathered; even one answer can produce a one-line batch.

## The checkpoint

At about 10 questions (6 to 8 on a sensitive facet), a question-tool checkpoint, verbatim script:

> "That's about ten. I can keep going while we're warm, switch to another thin area, or turn what you've given me into proposals for your sign-off."
> Options: **Continue (10 more)** / **Switch facet** / **Wrap up to proposals**

Continue renews for one more block, then the checkpoint repeats. Switch re-runs the facet pick (consent gate included if the next-thinnest is sensitive). Wrap goes to composition. The checkpoint is a hard cap, not a suggestion: the run never sails past it silently.

## The interview ledger (session-only)

The lead keeps one running ledger in context, never persisted, one row per answer:

```
[q-id] · [delivery: tool|prose|cluster] · [tag: stated|observed (confidence low|med|high)] ·
verbatim answer (stated) or the observation and its evidence (observed)
```

- **stated**: what the user actually said or selected, verbatim. Only stated rows can become unmarked Profile lines.
- **observed**: what the lead noticed rather than was told (pattern across answers, tone, an aside), always with a confidence grade. Observed rows can only ever become marked, `unconfirmed` lines.
- Skipped question ids are listed at the ledger's foot (session-only, so the run does not re-ask); the fact of the skip is never composed into anything.

The ledger is Calvin's sole factual input: if it is not in the ledger, it does not exist to the composer. Adeline's discipline, applied: observed and stated are different species of evidence and never blur, and an assumed claim (in neither column) does not exist at all.

## Question order within a run

1. Confirm-pass items first (max 2): existing `unconfirmed` markers in the target facet, asked as short confirmations ("I have you down as X, does that hold?"). Confirmed markers shorten to `confirmed`; corrected ones become new stated facts; a shrug leaves the marker untouched.
2. Highest-signal unfilled sections next, per the facet's question map: the sections that most change how the BRAIN helps come before completionism.
3. Warm-up before depth on any facet with narrative items: one easy scaled block before the first open prompt.
4. Snapshot never asked: it is composed by Calvin from the run's material and proposed like any other diff (`question-maps.md`, the Snapshot-fills-last rule).
