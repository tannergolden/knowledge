# Deliverable contract (the output contract every operate deliverable carries)

*The header every OPERATE artifact ships with before it lands: what it is, who owns it, where it is filed, the Definition of Done it was built against, the verifier's sign-off (Grace), and whether it is Founder-gated. The lead fills this from the brief, the Head of Quality signs it, and the skill (the sole writer) lands it. No agent writes; agents compose and return, the skill persists.*

This is the producing-side twin of `templates/board-brief.md` (which frames a decide run). A board brief frames a question; a deliverable contract frames a produced artifact and travels with it from the lead's brief, through Grace's verification, to the write-gate. One contract per artifact. A request that needs three artifacts is three contracts, sequenced on their dependencies (`references/deliverable-dependency-chains.md`). The contract is what makes the producer-to-artifact handoff checkable end to end: a deliverable with no owning file and no Definition of Done is not producible, and the verifier returns it unbuilt.

Read this with `references/specialist-dispatch.md` (the produce loop that fills it), `references/department-deliverable-catalog.md` (the per-function owning file and DoD), `references/verification.md` (how Grace checks the DoD), and `references/write-gate.md` (the green and red lanes the gate field maps to). The owning-file names and the DoD lines below are drawn from the catalog; keep them in sync with it, never invent a new owning file here.

## The contract (fill one per artifact)

```
ARTIFACT:        [the specific deliverable, named, not a capability. "Q3 3-statement model", not "finance work".]
OWNING DEPT:     [the AR function that owns it, e.g. Finance and Accounting (F&A).]
LEAD (owner):    [the one accountable lead, e.g. CFO Eleanor. One name. This is the accountable owner of record.]
SPECIALIST(S):   [the producer(s) the lead dispatched, e.g. FP&A Analyst Priya. Who built it, for the record.]
FILED TO:        [the single Ventures/<Venture>/<Dept>/ file it lands in, from the catalog. e.g. F&A/Financial-Model.md.]
TRIGGER:         [what called for it: a planning cycle, a raise, a launch, a review run, a stage change.]
STAGE:           [found | scale | maintain. Scales the rigor: a Seed model is a driver-based projection, not an audit-grade build.]
LADDERS TO:      [the strategy objective or OKR in Strategy.md / Goals.md this serves, so nothing is built unmoored.]
DEPENDS ON:      [the upstream artifacts it builds on, if any (e.g. positioning before GTM); none if it is a root artifact.]

DEFINITION OF DONE (the bar Grace checks, from the catalog):
  - [checkable condition 1]
  - [checkable condition 2]
  - [checkable condition 3]

COMPLETION EVIDENCE (returned with the artifact; the verifier checks the evidence, not the claim):
  - [every number traced to a source, a tool call, or a venture file; every assumption named.]

VERIFIER SIGN-OFF (Head of Quality, Grace):
  - Result:     [ cleared | cleared with noted defects | returned | escalated ]
  - Checked:    [the specific evidence checked, not a general thumbs-up.]
  - Defects:    [any noted gaps or open questions that travel with the artifact; none if clean.]

FOUNDER-GATED:   [no | yes - <which red category>. A "no" means the skill writes it autonomously into the venture folder
                  once verified, with the prior state committed. A "yes" means the skill prepares the action and stops for the Founder's
                  explicit confirmation. The five red categories are fixed (write-gate.md): moving money, signing or
                  sending a contract, publishing or sending external comms, deleting a file, changing equity or the cap
                  table. When in doubt, gated.]

WRITE-BACK:      [the Log.md line the skill appends, and any Goals.md / Overview.md stage update the artifact triggers.]
```

## How each field is set, and by whom

- **Artifact, owning dept, filed-to, DoD** come straight from `references/department-deliverable-catalog.md`. The catalog is the source of truth for which file each artifact lands in and what its DoD is; the contract copies them, it does not redefine them. If the catalog has no owning file for the artifact, the artifact is not yet producible, and that is a finding, not a thing to invent a home for.
- **Lead and specialist(s)** come from the catalog's function entry. The lead is the single accountable owner; the specialists are the producers the lead dispatched (`references/specialist-dispatch.md`). The lead frames and approves and never types the artifact; the specialist builds it; neither one writes the file.
- **Stage and ladders-to** come from the venture-context preflight: the chair read `Overview.md`, `Goals.md`, `Strategy.md`, and recent `Log.md`, and detected the stage (`references/lifecycle.md`). The stage scales the rigor and the catalog subset; ladders-to keeps the artifact tied to a real objective so the work is not unmoored.
- **Completion evidence** is the producer's, returned with the artifact. The rule is `references/verification.md`'s: every number, every named fact, every external claim traces to a tool call, a venture file, or a cited source. Nothing load-bearing rests on recall.
- **Verifier sign-off** is Grace's alone. A producer never verifies its own work. Grace receives the artifact, this contract, and the claimed sources in a fresh worker that holds none of the producer's reasoning, and checks the artifact against the DoD and the evidence. The four results are `cleared`, `cleared with noted defects`, `returned`, `escalated` (`references/verification.md`). A `returned` artifact does not land; it goes back to the lead with the specific finding. Consequential output does not land unverified.
- **Founder-gated** maps to the write-gate's two lanes (`references/write-gate.md`). Green (autonomous): internal, reversible drafts and models into the venture's own folder, written once verified, with the prior state committed. Red (hard-gated): the five fixed categories, which never go autonomous at any stage or tier; a CEO-seat yes is advice, not authorization. Stage moves the dollar line inside the green lane, never the category line.
- **Write-back** is what the skill does after the gate clears: persist the artifact into the filed-to file (with an existing file's last state committed first), append a dated line to the venture `Log.md`, and update `Goals.md` or the `Overview.md` stage when they changed. Then `python3 .github/scripts/update-vault.py` and `check-vault.py`.

## The gate the contract walks before it is written

The skill walks the write-gate checklist (`references/write-gate.md`) against this contract, in order, and stops at the first red:

1. **Is the FOUNDER-GATED field a red category?** (money, contract, external comms, delete, equity or cap table.) Yes - frame the action, state it, get the Founder's explicit confirmation. Do not proceed on a CEO-seat yes.
2. **Does it cross outside this venture's folder, or is it irreversible?** Yes - same as above.
3. **Does the implied spend or hire exceed the stage threshold** (`assets/delegation-of-authority.json`)? The artifact is green to draft; the action is red to execute. Gate the action.
4. **Green so far - is the existing file's last state committed?** No - commit it first. A new file needs nothing.
5. **Is the output consequential, and has Grace cleared it?** Consequential and unverified does not pass, even when reversible. Verify first.
6. **All clear - write it.** Persist, append to `Log.md`, update `Goals.md` / `Overview.md` if changed, then `update-vault.py` and `check-vault.py`.

---

## Per-department artifact stubs (the highest-value contracts, pre-filled)

Four worked stubs, one per common producing department, with the owning file and DoD already drawn from `references/department-deliverable-catalog.md`. Copy the relevant stub into a fresh contract, fill the brackets from the venture, and let the body of the artifact follow the stub's structure. These are the artifacts an operate run produces most; the full per-function catalog is in `references/department-deliverable-catalog.md`.

### Stub A - PRD / product spec (R&D)

```
ARTIFACT:        [feature or product name] PRD
OWNING DEPT:     Research and Development (R&D)
LEAD (owner):    Chief Product Officer Oliver
SPECIALIST(S):   Product Manager Naomi (the what and why); Applied Researcher Victor (the validating evidence)
FILED TO:        R&D/Roadmap.md   (the GTM surface for the same product lands in S&M/Products.md)
TRIGGER:         a build is greenlit
STAGE:           [scale, typically]
LADDERS TO:      [the strategy objective in Strategy.md / the OKR in Goals.md this build serves]
DEPENDS ON:      user-research synthesis and the MRD (the evidence the requirements rest on)
DEFINITION OF DONE:
  - the requirement ties to a strategy objective in Strategy.md or Goals.md
  - each requirement has acceptance criteria a verifier can check (testable, not aspirational)
  - the validated and invalidated assumptions are recorded; an invalidated assumption is kept, not quietly dropped
  - the engineering contract is unambiguous: scope in, scope out, and the go / no-go gates named
FOUNDER-GATED:   no  (an internal spec; the build it authorizes may carry gated spend, checked separately)
```

Body sections: problem and the evidence for it; the user and the job-to-be-done; goals and non-goals; requirements with acceptance criteria; the assumptions (validated and invalidated); dependencies and the release gates; the metric that will tell us it worked (defined in Metrics.md, not redefined here).

### Stub B - SOP / runbook (O&L)

```
ARTIFACT:        [process name] SOP
OWNING DEPT:     Operations and Logistics (O&L)
LEAD (owner):    Head of Operations Hannah
SPECIALIST(S):   Process Analyst Wesley (maps and improves the process)
FILED TO:        O&L/Operations.md
TRIGGER:         a process that lives in one head, an audit, or a handoff that keeps breaking
STAGE:           [scale or maintain]
LADDERS TO:      [the operating objective or the reliability / cycle-time target this procedure serves]
DEPENDS ON:      none (or the upstream process it hands off from)
DEFINITION OF DONE:
  - every step is executable as written (a stranger to the process can run it)
  - the RACI names real owners, not placeholders
  - the exception and rollback paths exist and are reachable from the happy path
  - each KPI the SOP is measured by has a definition, a target band, and a current value (referencing Metrics.md)
FOUNDER-GATED:   no  (committing vendor spend or signing a supplier contract surfaced by the SOP is red, gated separately)
```

Body sections: purpose and scope; the trigger and the inputs; the RACI; the step-by-step procedure (a flowchart where it helps); the exception paths and the rollback; the KPIs and their target bands; the review cadence and the owner.

### Stub C - GTM one-pager (S&M)

```
ARTIFACT:        [product or launch name] GTM one-pager
OWNING DEPT:     Sales and Marketing (S&M)
LEAD (owner):    CRO Xavier
SPECIALIST(S):   Product Marketing Manager Felix (positioning, launch); Demand Generation Manager Derek (the channel and pipeline plan)
FILED TO:        S&M/Products.md   (the offer detail lands in S&M/Services.md; positioning lives in S&M/Brand.md)
TRIGGER:         a launch or a new market
STAGE:           [found for a founder-led GTM note; scale for the repeatable motion]
LADDERS TO:      [the growth OKR in Goals.md this launch serves]
DEPENDS ON:      the positioning and brand guide in S&M/Brand.md (positioning precedes GTM)
DEFINITION OF DONE:
  - the ICP is specific (not "everyone"); the segment is named and bounded
  - the why-now is evidenced, not asserted
  - launch tiers have owners and dates
  - the pipeline target and the channel mix are stated and traceable to a number
  - any published external asset is flagged Founder-gated, never sent autonomously
FOUNDER-GATED:   the plan: no.  any external publication or send it produces: yes - publishing or sending external comms.
```

Body sections (one page): ICP and the job-to-be-done; the why-now; how-we-win (the wedge against alternatives); the offer and pricing surface; launch tiers with owners and dates; the channel mix and the pipeline target; the metric that defines a successful launch (from Metrics.md).

### Stub D - Compensation bands (HR)

```
ARTIFACT:        Compensation bands - [scope: a level, a function, or company-wide]
OWNING DEPT:     Human Resources (HR)
LEAD (owner):    CHRO Vivian
SPECIALIST(S):   Compensation and Benefits Analyst Yvonne (the benchmarked ranges and the rewards mix)
FILED TO:        HR/Hierarchy.md
TRIGGER:         a hiring wave or an annual compensation review
STAGE:           [scale, typically]
LADDERS TO:      [the org-design objective in Strategy.md; costed against the runway in F&A/Financial-Model.md]
DEPENDS ON:      the org design and the role charters in HR/Hierarchy.md; the runway in F&A/Financial-Model.md
DEFINITION OF DONE:
  - each band is benchmarked to a named source and stated as a range, not a point
  - the equity guidelines and the approval workflow are stated
  - the plan is costed against Financial-Model.md runway, not set in a vacuum
  - no real person's actual compensation or termination is decided here (those escalate to the Founder)
FOUNDER-GATED:   the bands: no.  an actual offer drawn from them: yes - it commits money and is a contract.
```

Body sections: the leveling framework (the ladder the bands sit on); the benchmark source and its vintage; the bands by level and function (range, not point); the equity and total-rewards guidelines; the approval workflow; the runway cost of filling the open plan at band midpoint.

---

## The standard the contract holds

One contract, one artifact, one owning file, one accountable lead, one verifier's sign-off, one writer. **Every angle heard in producing it, one owner accountable for it.** The lead frames and approves; the specialists produce in isolation and never grade their own work; Grace verifies independently against the DoD; the skill alone writes, behind the write-gate. The contract is stage-aware (the rigor and the catalog subset scale to found, scale, or maintain), grounded (every number traces, the artifact ladders to a real objective), and gated (the five red categories are the Founder's alone to authorize). A deliverable that cannot fill this contract is not done, and the skill does not write a deliverable the verifier returned.

See `references/specialist-dispatch.md` for the produce loop that fills the contract, `references/verification.md` for the sign-off discipline, `references/write-gate.md` for the gate the FOUNDER-GATED field maps to, and `references/department-deliverable-catalog.md` for the owning file and DoD of every other artifact.
