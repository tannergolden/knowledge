# The slop rubric - the externalized quality standard

The Line Editor (and, on quick, the lead self-editing) critiques every piece against this rubric, never against a vague "make it better." A written standard is the point: naked self-critique degrades, so the bar lives on paper and the critic checks the draft against it.

> [!important] Single source of truth
> This rubric does **not** define what slop is. **Constitution Article 9.2** (No AI Slop) and **9.1** (No Em Dashes) define it; this file is a working checklist that points back to them. When the Constitution and this file ever disagree, the **Constitution wins**, and this file is the bug. The rubric references the Constitution; it never forks it.

## The two hard gates (Article IX, everywhere, internal files included)

1. **No em dash (9.1).** Zero U+2014 in the piece. Replace with a comma, colon, parentheses, or a hyphen, or rewrite. `lint-notes.py` flags any em dash in a vault file, so this is enforced on disk, not merely stated. The en dash (U+2013) and the hyphen are fine.
2. **No slop (9.2).** None of the patterns below. "Write like a sharp human. Be direct, specific, and clear."

## Cite the span (the rule that makes the rubric work)

Every flag **names the offending span**: the exact word, phrase, or sentence, with its location, and the fix. "This feels like AI" is not a flag; "leverage in paragraph two, replace with use" is. A flag without a cited span is not a flag. This is what keeps the critique mechanical and keeps the critic honest.

## Resist length-bias and lenient scoring

- **Shorter wins when meaning is preserved.** A cut that loses nothing is an improvement; do not reward length, polish, or effort. The critic actively prefers the tighter version.
- **"Leave it alone" is a valid verdict.** If the draft already reads clear and true, return a no-op. Editing for the sake of editing is itself a defect (see the Meta group).
- **The fix is not synonym-swapping.** The cure for slop is to **write as you speak and take a position**, not to trade one inflated word for another. Swapping "utilize" for "leverage" fixes nothing.

## The five groups (the working checklist, aligned to 9.2)

A 51-pattern taxonomy reduced to five groups. The Constitution's banned-word list (9.2) is the spine of the Language group; the rest operationalize 9.2's "phrases and habits" and "language that sounds polished but says nothing specific."

### 1. Content - says nothing specific

- **Significance inflation.** Calling a thing important, crucial, vital, notable, or essential instead of showing why. If the weight is real, demonstrate it; if it is not, cut the claim.
- **Vague attribution.** "Experts say," "studies show," "it is widely regarded" with no named source. Either name the source or drop the appeal.
- **Promotional adjectives.** Marketing gloss on neutral facts (rich, powerful, seamless, game-changing). State the fact; let it carry itself.
- **Superficial -ing analysis.** Trailing participial clauses that gesture at insight without adding it ("highlighting the importance of," "underscoring the need for," "reflecting a broader trend"). Cut or replace with the actual point.

### 2. Language - the slop vocabulary (9.2's banned list)

- **Three-tier inflation.** The tell-tale upgrades: **leverage** (as a verb) for use, **utilize** for use, **robust** for strong or solid. Plus the rest of the 9.2 list: delve, comprehensive, streamlined, cutting-edge, synergy, paradigm, holistic, actionable, empower, foster, harness, elevate, underscore, crucial, vital, notable.
- **Copula avoidance.** Dodging a plain "is" with "serves as," "functions as," "acts as," "represents," "stands as." Usually "is" is the honest verb.
- **Synonym cycling.** Renaming one thing three ways in a paragraph to seem varied (the tool, the solution, the platform, the offering). Name it once, keep the name.
- **Filler.** "In order to" for "to," "due to the fact that" for "because," "at this point in time" for "now," "a number of" for "some" or a count.

### 3. Structure - the shape gives it away

- **Transition abuse.** **Moreover, Furthermore, Additionally, In conclusion, Importantly** as connective tissue between every paragraph (all on the 9.2 list). Cut them; let the ideas connect themselves, or use a plain "and" or "but."
- **Inline-header lists.** Every bullet opening with a **bold lead-in: then a colon then a clause**, used where flowing prose would read better. A list is for genuinely parallel items, not for dressing up a paragraph.
- **Uniform sentence rhythm.** Every sentence the same length and shape. Vary it; a short sentence after two long ones lands.
- **List inflation.** Bulleting prose that should stay prose. The Constitution names "over-bulleting things that should be prose" directly.
- **Bold and emoji excess.** Bolding for emphasis until nothing is emphasized; emoji as decoration. (See `formatting.md` and the beauty principle: signal-scarcity, not maximalism.)

### 4. Communication - the chatbot tells

- **Chatbot artifacts.** "I hope this helps," "Let me know if you need anything else," "I'd be happy to," "Great question," "Certainly," "Absolutely," "Of course" (9.2's hollow affirmations). Delete on sight.
- **Hedges.** "It's worth noting," "it's important to remember," "it should be mentioned that," "arguably," "in many ways." Either say the thing or do not.
- **Sycophancy.** Flattering the reader or the prompt before answering. Just answer.
- **Generic uplift conclusions.** The closing paragraph that zooms out to a feel-good nothing ("Ultimately, the key is to find what works for you," "By embracing these strategies, you'll be well on your way"). End on the last real point.

### 5. Meta - over-working the text

- **Over-structuring short text.** Headers, bullets, and bold on a three-sentence answer. Match the structure to the length; a short answer is a short paragraph.
- **Over-polishing.** Sanding off every natural variation until the prose is frictionless and dead. Some unevenness is human; preserve the author's rhythm rather than ironing it flat (this is why the editor preserves length and register).

## How the gate runs

The Line Editor returns its edit ledger with each flag as `location - group - the cited span - the fix`, plus a separate list of load-bearing factual claims flagged for verification (the editor flags, it does not fact-check; the lead verifies or routes to the Research team). The lead applies the ledger, and the piece does not ship on an unresolved hard-gate violation (9.1 or 9.2) or an unverified load-bearing claim. The asset `assets/slop-patterns.md` is the fuller pattern catalog the editor can scan against; this file is the doctrine.
