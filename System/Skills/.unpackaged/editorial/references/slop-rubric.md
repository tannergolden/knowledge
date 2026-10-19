# The slop rubric - the externalized quality standard

The Line Editor (and, on quick, the lead self-editing) critiques every piece against this rubric, never against a vague "make it better." A written standard is the point: naked self-critique degrades, so the bar lives on paper and the critic checks the draft against it.

> [!IMPORTANT]
> **Single source of truth.**
> This rubric does **not** define what slop is. Standards' [Plain Words](https://github.com/tannergolden/standards/blob/Development/docs/technical/interface/Document-Styling-&-Formatting.md#plain-words) list does: its banned words and its habits, which **DOC-003** holds every agent to. **DOC-002** bans the em dash. **Read the Plain Words list at that link before grading**, and grade against it as it stands there, never against a copy from memory; a Line Editor dispatched without web access gets the list in its brief, read at the link by the lead and passed inline. This file is the working checklist around it: the patterns that go beyond the list, and how the gate scores. When the list and this file ever disagree, the **list wins**, and this file is the bug. The rubric points at the list; it never forks it.

## The two hard gates (everywhere, internal files included)

1. **No em dash (DOC-002).** Zero U+2014 in the piece; DOC-002 names the replacements, and a rewrite often beats all of them. `lint-notes.py` flags any em dash in a vault file, so this is enforced on disk, not merely stated. The en dash (U+2013) and the hyphen are fine.
2. **No slop (DOC-003).** No word or habit from the Plain Words list, and none of the patterns below.

## Cite the span (the rule that makes the rubric work)

Every flag **names the offending span**: the exact word, phrase, or sentence, with its location, and the fix. "This feels like AI" is not a flag; "'in order to' in paragraph two, cut to 'to'" is. A flag without a cited span is not a flag. This is what keeps the critique mechanical and keeps the critic honest.

## Resist length-bias and lenient scoring

- **Shorter wins when meaning is preserved.** A cut that loses nothing is an improvement; do not reward length, polish, or effort. The critic actively prefers the tighter version.
- **"Leave it alone" is a valid verdict.** If the draft already reads clear and true, return a no-op. Editing for the sake of editing is itself a defect (see the Meta group).
- **The fix is not synonym-swapping.** The cure for slop is to **write as you speak and take a position**, not to trade one inflated word for another. Swapping one word on the list for another fixes nothing.

## The five groups (the working checklist)

A 51-pattern taxonomy reduced to five groups. The Plain Words list is the spine: its words are the core of the Language group, and its habits run through the rest. The patterns below are the ones beyond the list that the gate also flags.

### 1. Content - says nothing specific

The list's "language that sounds polished but says nothing specific", in its common shapes:

- **Significance inflation.** Calling a thing important, essential, key, or significant (or any inflation word on the list) instead of showing why. If the weight is real, demonstrate it; if it is not, cut the claim.
- **Vague attribution.** "Experts say," "studies show," "it is widely regarded" with no named source. Either name the source or drop the appeal.
- **Promotional adjectives.** Marketing gloss on neutral facts (rich, powerful, seamless, game-changing). State the fact; let it carry itself.
- **Superficial -ing analysis.** Trailing participial clauses that gesture at insight without adding it ("highlighting the importance of," "reflecting a broader trend"). Cut or replace with the actual point.

### 2. Language - the words themselves

- **The banned words.** Every word on the Plain Words list is a flag on sight. The strongest tells are inflated stand-ins for a plain verb or adjective, so the fix is the plain word (use, strong, solid), never another inflated one.
- **Copula avoidance.** Dodging a plain "is" with "serves as," "functions as," "acts as," "represents," "stands as." Usually "is" is the honest verb.
- **Synonym cycling.** Renaming one thing three ways in a paragraph to seem varied (the tool, the solution, the platform, the offering). Name it once, keep the name.
- **Filler.** "In order to" for "to," "due to the fact that" for "because," "at this point in time" for "now," "a number of" for "some" or a count.

### 3. Structure - the shape gives it away

- **Transition abuse.** A stock connective opening paragraph after paragraph: the ones on the list, and "To that end" or "That said" used the same way. Cut them; let the ideas connect themselves, or use a plain "and" or "but."
- **Inline-header lists.** Every bullet opening with a **bold lead-in: then a colon then a clause**, used where flowing prose would read better. A list is for genuinely parallel items, not for dressing up a paragraph.
- **Uniform sentence rhythm.** Every sentence the same length and shape. Vary it; a short sentence after two long ones lands.
- **List inflation.** Bulleting prose that should stay prose. The list names "bullets where prose would read better" directly.
- **Bold and emoji excess.** Bolding for emphasis until nothing is emphasized; emoji as decoration. (See `formatting.md` and the beauty principle: signal-scarcity, not maximalism.)

### 4. Communication - the chatbot tells

- **Chatbot artifacts.** The list's hollow affirmations, and the sign-off tells beside them: "I hope this helps," "Let me know if you need anything else," "Feel free to." Delete on sight.
- **Hedges.** The list's stock hedges, and "it should be mentioned that," "arguably," "in many ways," "to some extent." Either say the thing or do not.
- **Sycophancy.** Flattering the reader or the prompt before answering. Just answer.
- **Generic uplift conclusions.** The closing paragraph that zooms out to a feel-good nothing ("Ultimately, the key is to find what works for you," "By embracing these strategies, you'll be well on your way"). End on the last real point.

### 5. Meta - over-working the text

- **Over-structuring short text.** Headers, bullets, and bold on a three-sentence answer. Match the structure to the length; a short answer is a short paragraph.
- **Over-polishing.** Sanding off every natural variation until the prose is frictionless and dead. Some unevenness is human; preserve the author's rhythm rather than ironing it flat (this is why the editor preserves length and register).

## How the gate runs

The Line Editor returns its edit ledger with each flag as `location - group - the cited span - the fix`, plus a separate list of load-bearing factual claims flagged for verification (the editor flags, it does not fact-check; the lead verifies or routes to the Research team). The lead applies the ledger, and the piece does not ship on an unresolved hard-gate violation (DOC-002 or DOC-003) or an unverified load-bearing claim. The asset `assets/slop-patterns.md` is the fuller pattern catalog the editor can scan against; this file is the doctrine.
