# Verification - the independent verifier before a deliverable lands

*How the Head of Quality (Grace) checks every consequential deliverable before the skill persists it, so produced work is grounded, complete, and honest. Read in operate mode, after the specialists return and before the write-gate. The verifier never produced the work it checks; a producer never grades its own output.*

In operate mode a lead frames a brief, its specialists produce the work, and then, before the skill writes anything, the **Head of Quality (Grace)** verifies it. This is the third phase of the universal run shape (challenge-or-verify), and in operate mode it is a hard gate, not a courtesy pass: the skill does not call the write-gate until the verifier has cleared the deliverable or the run has stopped on a documented failure. Verification sits between the producer and the writer on purpose, because the two roles the skill must never collapse are the one that makes the work and the one that judges it. See `specialist-dispatch.md` for how the work arrives, and `write-gate.md` for what happens after it clears.

## Why an independent verifier, and why not self-check

The AI-operating-system research that grounds this overhaul is blunt on one point: a model that generates work and then checks its own work is worse than one that does neither, because the self-check launders a wrong answer into a confident one. The failure mode is hallucination presented with full fluency, and it is most dangerous exactly where it is hardest to catch by eye: a financial model with a plausible but invented growth rate, a contract clause that sounds standard but is not, a metric stated to two decimals with no source behind it. Fluent and wrong is the default failure of a language model under production pressure, and the same context that produced the error is the worst possible context to catch it from. So the discipline is structural, not exhortative: the producer cannot verify, and the verifier did not produce. Grace receives the deliverable, the brief it was made against, and the sources it claims, in a fresh worker that holds none of the producer's reasoning, and checks the artifact against the standard rather than against the story the producer told itself. This is the same anti-anchoring logic that makes the decide mode take independent views in isolation (`synthesis.md`), applied to produced work: the check is worthless if it inherits the producer's frame.

## What counts as consequential

Verification has a cost in tokens and a cost in latency, so it is reserved for deliverables that can do damage if they are wrong. A deliverable is **consequential**, and must be verified before it lands, if it is any of:

- **Load-bearing.** Other work or other decisions will rely on it. A financial model the budget ladders up to, a metric definition the scorecard reads, a PRD the engineering build follows, a comp band an offer is drawn from. If a downstream artifact or decision inherits its numbers or its claims, it is load-bearing.
- **External.** It will leave the building or be read as the company's word: a press release, a customer-facing brand or pricing page, a board deck, an investor update, a contract or a proposal sent to a counterparty. Anything a third party will act on.
- **Irreversible.** Persisting it commits something that is costly or impossible to take back: it moves money, signs or sends a contract, deletes a file, or changes equity or the cap table. These are also the hard-gated actions at the write-gate (`write-gate.md`); verification is the quality check, the gate is the authorization, and an irreversible action needs both.

When in doubt, treat it as consequential. The cheap internal drafts that are none of these (a working outline, a first-pass list, a scratch note the skill writes into a venture's internal file and can revise next run) get a lighter touch: the lead's own review suffices and the skill may write autonomously. The line tracks the write-gate's line between autonomous internal drafts and gated output, because the same property that makes something worth verifying (load-bearing, external, irreversible) is what makes it worth gating.

## The completion-evidence requirement

A deliverable does not arrive as "done." It arrives with the **evidence that it is done**, and the verifier checks the evidence, not the claim. Each operate brief carries a **Definition of Done** from the department deliverable catalog (`department-deliverable-catalog.md`): the concrete, checkable conditions the artifact must meet to count as complete. The producer returns the artifact plus its completion evidence against that definition; Grace verifies the evidence supports the claim of done before anything is written.

Completion evidence is specific to the artifact and stated in checkable terms:

- For a **financial model**: the three statements tie out (the balance sheet balances, cash on the cash-flow statement matches the balance sheet, net income flows to retained earnings), every assumption is labeled with its source, and the scenarios are present and internally consistent.
- For a **metric definition**: the formula is explicit, the inputs name their source table or system, the definition is unique (no second definition of the same metric elsewhere), and the benchmark band, if cited, names its origin.
- For a **contract or policy**: every required clause from the playbook is present, the party names and entity match the venture record, no placeholder or bracketed term survives, and any non-standard term is flagged not buried.
- For an **SOP or runbook**: every step is executable as written, the RACI names real owners, and the failure and rollback paths exist.
- For a **GTM or brand artifact**: the positioning matches the strategy on file, the claims are supportable, and nothing contradicts a published venture artifact.

If the brief carried no Definition of Done, that is itself a finding: the verifier sends it back to the lead to define done before the work is graded, because a deliverable with no completion criteria cannot be verified and must not be persisted on faith.

## Ground every number in a tool or a source

The single rule that catches the most dangerous class of hallucination: **every number, every named fact, and every external claim in a consequential deliverable traces to a tool call, a venture file, or a cited source.** Nothing load-bearing rests on the model's recall. A figure that cannot be traced to where it came from is treated as unverified and is either grounded or struck before the artifact lands.

In practice the verifier checks that:

- **Figures from the venture trace to the venture.** Revenue, runway, headcount, customer counts, and the like come from the venture's own files (`Financials.md`, `Metrics.md`, `Overview.md`) or from a connected system of record read at run time, not from a guess and not from a stale memory of a prior run.
- **Benchmarks name their band.** A metric stated against a benchmark (NRR floor, Rule of 40, CAC payback) carries the benchmark's source and vintage from `metrics-and-kpis.md`, so a 2026 number is not being judged against a remembered 2019 band.
- **Computed numbers are recomputed, not recalled.** A ratio, a total, a growth rate, or a projection is arithmetic the verifier can redo from the inputs; if the inputs are not present to redo it, the number is unverified.
- **External facts carry a citation.** A regulatory deadline, a market-size figure, a competitor claim, a legal standard names its source, and a fact that turns on something after the model's knowledge cutoff or that is contested is sent to research rather than asserted (see `modes-router.md` on the research boundary).

This rule is most acute for **financial and legal output**, the two domains the research flags as highest-risk for fluent fabrication. A plausible-looking number in a model and a plausible-sounding clause in a contract are exactly the errors a casual read misses and a downstream reader trusts. In those two domains the verifier's default is suspicion: assume a number is invented until its source is shown, assume a clause is non-standard until the playbook confirms it.

## Confidence-based escalation

Verification is not a binary stamp. The verifier returns a **confidence** in the deliverable, and the confidence sets what happens next:

- **Cleared (high confidence).** The Definition of Done is met, every number traces, no material defect remains. The deliverable proceeds to the write-gate. If the artifact is an autonomous internal draft, the skill writes it; if it is external or irreversible, it still needs the Founder's confirmation at the gate (verification clears quality, it does not authorize an irreversible act).
- **Cleared with noted defects (medium confidence).** The artifact is sound but carries known gaps, stated assumptions, or open questions that a reader must see. It proceeds, but the gaps travel with it: they are surfaced in the synthesis, written into the deliverable's own caveats, and logged. A medium-confidence deliverable is never silently upgraded to clean.
- **Returned (low confidence or a found defect).** A failed Definition-of-Done check, an ungrounded number, an unsupported claim, an internal contradiction. The deliverable goes back to the producing lead with the specific finding, is reworked, and is verified again. It does not land in its current form, and the skill does not write a deliverable the verifier returned.
- **Escalated.** When verification surfaces something above the deliverable itself, a material risk, a number that contradicts the venture's own record, an irreversible action the brief assumed but did not flag, the verifier escalates to the chair, who carries it to the Founder if it crosses the write-gate line. The verifier's job includes refusing to let a confident artifact paper over a real problem.

The standard the verifier holds is the skill's standard, **every angle heard, one owner accountable**, in its operate form: the deliverable is checked independently of whoever made it, and the verifier owns the call on whether it is fit to persist. The chair holds the synthesis and the skill holds the pen, but the verifier holds the gate on quality, and a producer's confidence never overrides the verifier's finding.

## Anti-self-deception checks

The verifier runs a short, explicit battery against the ways produced work flatters itself. These are the operate-mode analogues of the decide-mode dissent pass (`frameworks.md`), aimed at the artifact rather than the decision:

- **Does it actually answer the brief?** Compare the deliverable to the framed brief, not to a nearby question it happens to answer well. A polished artifact for the wrong question is a defect, not a partial win.
- **Trace three numbers at random.** Pick load-bearing figures and follow each to its source. If one does not trace, assume the rest are suspect and trace them all.
- **Find the seam the producer skated over.** Every artifact has a hard part the producer was tempted to assume away: the assumption with no basis, the edge case the SOP ignores, the clause quietly softened, the cohort the model excludes. Name it.
- **Read it as the reader who acts on it.** If this is external or load-bearing, read it as the customer, the counterparty, or the engineer who will rely on it, and ask what goes wrong when they do.
- **Check it against the venture's own record.** A new number that contradicts `Financials.md`, a positioning that contradicts `Strategy.md`, a claim that contradicts a prior `Log.md` entry is a contradiction to resolve before the artifact lands, not after.
- **Confirm nothing was bent toward a wished-for answer.** If the deliverable lands suspiciously close to what someone hoped for, check whether an assumption was chosen to get there. The skill never bends a deliverable toward a wished-for answer (SKILL.md Boundaries), and the verifier is where that rule is enforced on produced work.

## Human-in-the-loop on irreversible actions

Verification clears quality; it does not authorize an irreversible or external act. The two are separate gates and an irreversible action needs both. A press release can be perfectly verified, every claim grounded and every figure traced, and it still does not go out without the Founder's confirmation, because publishing it is irreversible. The research is explicit that an AI operating system must keep a human in the loop on actions it cannot take back: moving money, sending or signing a contract, publishing or sending external communications, deleting a file, and changing equity or the cap table all stop at the Founder regardless of how clean the verification is. So the verifier's clearance is a precondition for the write-gate on these actions, never a substitute for it: Grace certifies the artifact is sound, the Founder authorizes the irreversible step. The verifier also surfaces, as part of clearing such an artifact, that the action it enables is irreversible, so the Founder confirms with the consequence in view. The full doctrine and the stage-keyed thresholds are in `write-gate.md` and `assets/delegation-of-authority.json`.

## What the verifier returns

The verifier's output is itself a small, checkable artifact, not a verdict alone:

1. **The confidence call.** Cleared, cleared-with-defects, returned, or escalated.
2. **The Definition-of-Done check.** Each completion condition marked met or unmet, against the brief's stated definition.
3. **The grounding check.** Which load-bearing numbers and claims were traced, and to what source; anything that did not trace, named.
4. **The defects and caveats.** Each finding stated specifically enough for the producing lead to act on, with the noted gaps that must travel with a cleared-with-defects deliverable.
5. **The escalation, if any.** What rose above the artifact and why, and whether it crosses the write-gate line to the Founder.

The chair folds this into the synthesis, the noted caveats travel into the deliverable and the `Log.md` entry, and only then does the skill, behind the write-gate, persist the work. A deliverable that reached the venture folder did so because an independent verifier, who did not make it, found it grounded, complete, and honest, and said so on the record.
