# Self-improvement - the recursive loop

How develop improves a skill or agent that misbehaved, including itself. Self-correction is reliable only when bound to an external signal; prompt-only self-critique is weak and can degrade output. So every step here is anchored to an oracle (a failing test, the validator, a tool result, a golden example), never to the model's own say-so.

## The loop

1. **Capture** the failure from the transcript and any explicit notes: what was asked, what the skill did, what was wrong. Concrete, not paraphrased.
2. **Blameless postmortem** to the root cause, not the symptom (Google SRE). 5-Whys: a wrong output usually traces to a missing instruction, an ambiguous boundary, or a weak description, not to "the model erred." Fix the cause.
3. **Minimal corrective diff.** The smallest change that addresses the root cause and prevents the class of failure. Resist rewriting; a large diff is a new build, not a fix.
4. **Propose, then apply only on approval.** Show the diff and the reasoning; apply nothing until the user approves.
5. **Verify independently.** Re-run `brain.command skill validate` (and `brain.command lint`/`health` for a conformance check against the live BRAIN); dispatch a fresh QA Engineer to re-check only the changed area, joined by the Application Security Engineer where the change is security-relevant; run a trigger check if the description changed. The author never grades its own fix (self-preference bias is real and significant).
6. **Freeze a regression case.** Append one line to the target skill's `assets/regression-cases.jsonl`: the failing input, the expected behavior, and a one-line lesson. Every future self-edit must re-pass every frozen case, so a later fix cannot silently regress an earlier lesson.

## No self-grading, even on develop itself

When develop edits develop, the same rule holds: the fix is verified by the deterministic validator and the independent auditor and the regression ledger, never by develop declaring its own change good. The ledger is the objective memory that keeps recursion honest.

## Regression ledger format (`assets/regression-cases.jsonl`)

One JSON object per line:

```json
{"id":"rc-0001","date":"YYYY-MM-DD","skill":"<name>","input":"<the triggering request>","expected":"<the correct behavior>","was":"<what it did wrong>","lesson":"<the one-line rule that prevents recurrence>"}
```

Managed append-only. The file ships empty at `01.00.00` and grows one entry per real fix.
