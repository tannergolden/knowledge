# Reporting - output, filing, and freshness

How a run's findings are delivered, filed, and kept fresh. This is the BRAIN's model, and it overrides any per-volatility scheme a generic research skill would use.

## Chat first, file on request

Every run delivers a **cited chat synthesis, findings first**, in a fixed shape: **Bottom line** (the answer with its two-axis certainty) -> **findings by angle**, each inline-cited and source-tier-aware -> **disagreements and the falsifier** (what would change the conclusion). Findings first, never a narrative of the run. A report **file** is produced only when the user asks for one, or by standing instruction, so the inbox stays lean. Offer it; do not file by reflex.

**Resolve before shipping (a stop step).** Before any deliverable ships, chat or file, resolve every load-bearing URL (live, dead, or fabricated): any that does not resolve is cut or replaced before the synthesis ships, never shipped with a caveat. A measured 3-13% of deep-research citations are fabricated, so this is a gate, not a hope.

## The Step-0 check (before every non-quick run)

The Knowledge Manager canonicalizes the topic (reduce the question to its topic slug, then match it against existing report titles and `keywords`) and checks `Inbox/Reports/` for an existing report first; on a near-match it returns the candidate and the lead, who is the one talking to the user, confirms it is the same topic before reusing. A report still inside its three-month window is **reused** (a quick confirmation of its load-bearing claims refreshes the window without a rewrite, reuse is review), not re-run. A match that has aged out is **refreshed in place**: same file, same `id` and `created`, advance `updated` and `review_by`; the report is rewritten as a fresh report, never as a diff. This check is the single largest token saver, so it runs first.

## Filing a report

In a vault, a filed report goes to **`Inbox/Reports/`**, the held reports library, never into the skill's own folder, which holds the team; outside a vault it goes where the user says. One topic, one canonical file, named `<Topic Title>.md` (the topic title alone, no prefix), built from `templates/report.md` with full BRAIN frontmatter and a `review_by` date. **In the same edit, add the report's entry to the `Inbox/Reports/Reports.md` index** (a bullet with a wikilink to the new file, its `review_by` "good through" date, and a one-line summary), so the index always mirrors the folder; a refreshed report has its index entry updated, a cleared one has it removed. Run the BRAIN edit protocol when filing: commit first if overwriting, write, then `update-vault.py` and `check-vault.py`.

## Flat three-month freshness

Every report is good through its `review_by` date, **three months** after it was filed or last verified; after that it must be verified before reuse. One flat window covers all reports, the rule lives in `Inbox/Reports/Reports.md`. This BRAIN deliberately does not use per-volatility windows: the flat window plus the promote-to-durable step below is the whole freshness model.

## Reports are linked only from the `Reports.md` index

A report is a working artifact: produced, consumed, refreshed, cleared. The held library's namesake, **`Inbox/Reports/Reports.md`, is the one hub that wikilinks every held report.** No other file in the BRAIN links to a report, which keeps the wider wikilink graph free of disposable nodes. Reports are also found by searching their folder.

## Promote to the durable layer (the explicit step)

The flat three-month window is correct only because durable findings do not live in reports. Before filing, the lead names any finding that must outlive three months and **promotes it into the durable layer**: a `Library/` reference doc, a folder note, a skill's `references/`, or a proposed change to `AGENTS.md`. The disposable report then expires harmlessly; the durable finding persists and can be linked. A foundational result left to rot in an expiring report is the failure this step prevents, so make the promote decision explicit on every filed run, not an afterthought.

## Memory write-back

After a substantial run, offer (never silently) to fold the distilled outcome into Memory: a `Memory/Log.md` entry, promotion to a permanent Memory file, or a session summary. The offer is the contract; the user decides.
