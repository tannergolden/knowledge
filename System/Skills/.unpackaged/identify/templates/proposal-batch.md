<!-- Calvin RETURNS one of these at pipeline step 7 (persists nothing); Sterling reviews it blind at
     step 8; the embodied lead presents the reviewed version in chat at step 9 for line-item approval,
     then is the sole writer at step 10. Every line is either verbatim-traceable and unmarked, or an
     inference carrying the full provenance marker and left `unconfirmed` (references/provenance.md).
     Memory-shaped facts go under Memory promotions, never into a file diff (Constitution 2.7). Skipped
     items are shown once and never persisted. No em dashes; plain paths, no wikilinks. -->

# Proposal batch: [Facet name]

**Target facet:** [the facet]
**Run summary:** [written N · confirmed N · deferred N, filled at step 12]
**Review status:** [Sterling reviewed blind: BLOCK N · REVISE N · CLEAR N; verdicts applied, one round]

## File diffs

Per file, numbered, markers visible. Approve all, approve except N, or per item.

### [Profile/[Facet].md]

1. **[Section] -> add / edit:**
   ```
   - **[Field]:** [value]
   ```
   [stated - traceable to ledger answer [q-id], no marker]

2. **[Section] -> add / edit:**
   ```
   - **[Field]:** [value] <!-- observed [YYYY-MM-DD] · confidence: [low|medium|high] · unconfirmed -->
   ```
   [observed - the inference and the evidence it rests on]

3. **[Confirm-pass] -> shorten marker:**
   ```
   - **[Field]:** [value] <!-- confirmed [YYYY-MM-DD] -->
   ```
   [was `unconfirmed`; the user confirmed it this run]

### [Profile/[Facet]/[Entry].md] (new engine-scaffolded entry)

4. **New [belief|goal|skill|condition] entry:** [Title]
   - Scaffolded via `profile add [belief|goal|skill|condition] "[Title]"`, then the body edited to:
   ```
   [the entry body, each line marked per provenance.md]
   ```

## Memory promotions (offered, not written into Profile)

Memory-shaped facts route here, never into a file diff (Constitution 2.7). Each is an explicit offer:

- **[Person]:** [what the ledger holds] -> offer `memory add person "[Name]"`. [Profile keeps only the user-fact phrasing, e.g. the relational style; the person record lives in Memory.]
- **[Dated happening]:** [what the ledger holds] -> offer `remember "[the log line]"`.
- **[Decision]:** [what the ledger holds] -> offer `memory add decision "[the decision]"`.

## Skipped this run (shown once, never persisted)

- [q-id / section]: skipped. [Listed here once so the approval view is complete; recorded nowhere in the vault, never re-probed.]

## Approval

Explicit and line-item capable: **approve all**, **approve except [N]**, or **per item**. No answer, no write.
