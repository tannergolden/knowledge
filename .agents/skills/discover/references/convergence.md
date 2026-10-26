# Converging - narrowing and ranking the idea pool

How to cull a wide field to the best, fairly. A reliable funnel runs cheap fast triage early (many ideas, little information) and rigorous relative ranking late (a few finalists to order). Read before ranking.

## ICE - the cheap intake triage

Score each raw idea 1 to 10 on **Impact** (how much it moves the goal), **Confidence** (how sure it works), and **Ease** (how simple to do), and multiply: ICE = Impact x Confidence x Ease (created by Sean Ellis for ranking growth experiments). Use it to triage the raw pool fast: a low ICE kills an idea early; a high ICE shortlists it. Failure mode: all three are gut estimates on one person's scale, so it inherits absolute-rating bias and is easily gamed by inflating the favorable factor. ICE triages; it does not produce the final order.

## Pairwise tournament: Bradley-Terry and Elo (the load-bearing ranker)

Rank the shortlist by repeated "which of these two is better?" contests, aggregated into one stable order. **Bradley-Terry** (1952) models the probability that idea i beats idea j as Pr(i > j) = p_i / (p_i + p_j), fitting a strength p per idea. **Elo** is the sequential cousin: each idea carries a rating, the expected score is E = 1 / (1 + 10^((R_other - R_self) / 400)), and after each contest the rating updates by K x (S - E) with S = 1 win, 0.5 tie, 0 loss; a low number of games marks an unsettled rank.

**Why pairwise beats rating each idea in isolation.** Humans are consistent at relative judgments even when their absolute ratings vary wildly (Thurstone's law of comparative judgment, 1927, which underlies Bradley-Terry). Pairwise comparison sidesteps absolute-scale miscalibration, neutralizes anchoring and rater-to-rater scale differences, and is cognitively easier, so judgment quality holds. It is the only ranking stage whose reliability does not depend on shared scale calibration, which is why it is the load-bearing ranker for the final order. Failure modes: it needs many comparisons (use adaptive pairing); intransitive or cyclic preferences strain the model; and it yields a relative order, not an absolute "is this good enough" verdict.

## RICE - cross-project and portfolio weighing

RICE = (Reach x Impact x Confidence) / Effort (Intercom). Reach is people or events affected per period; Impact is a tier (3 massive, 2 high, 1 medium, 0.5 low, 0.25 minimal); Confidence is 100, 80, or 50 percent; Effort is person-months. It puts heterogeneous initiatives on a common footing, which ICE cannot, so it is the Portfolio Manager's tool for weighing developed ideas across ventures. Failure mode: reach and effort are often guesses dressed as data; ratio scoring lets tiny-effort trivia outrank strategic bets, so the Confidence factor is the only guard.

## Lighter triage tools

- **Dot voting** - each person spends a few tokens on options; tally the heatmap. Fast and inclusive, but it measures popularity, not merit, and suffers anchoring, vote-splitting among similar options, and bandwagon effects. Mitigate with silent, private, simultaneous voting.
- **NUF test** - rate each idea on New, Useful, and Feasible (1 to 10). It exposes weak points to strengthen, and is explicitly not meant to kill ideas.
- **Impact-effort matrix** - plot impact against effort; prioritize quick wins (high impact, low effort). The grid is unstable: adding one idea repositions the others.

## The kill-gate and convergence discipline

Most ideas should die, by design; the team is a competitive selector, not an archive. A documented design-sprint funnel runs 90 to 30 to 10 to 3 (about a 97 percent cut), and the key is that each gate uses a different mechanism, so no single bias dominates: individual silent scoring, then a silent group review, then an adversarial challenger-versus-supporter debate. Silent individual work precedes group discussion at every step, and the adversarial format gives selection without bias toward the requester's preferred answer. Rule of thumb: cut to roughly a third each round.

## The recommended funnel

Cheap triage (ICE, or NUF, or one silent dot-vote round) to cut the bulk, then RICE if the survivors are heterogeneous or cross-venture, then a pairwise Elo tournament to rank the finalists. Pairwise comes last because it is the most reliable and the only stage independent of shared scale calibration.

## Sources

Bradley and Terry (1952); Thurstone, the law of comparative judgment (1927); the Elo rating system; Intercom (RICE); Sean Ellis (ICE); Nielsen Norman Group (dot voting); Gamestorming (the NUF test); the Design Sprint Academy (the selection funnel).
