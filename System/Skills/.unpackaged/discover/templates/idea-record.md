<!--
title: "[short idea title]"
description: "[the idea in one sentence, restated as a description]"
type: "record"
id: "in-idea-[YYYYMMDD]-[4hex]"
statement: "[the idea in one sentence]"
lifecycle: "raw"        # raw | shortlisted | developed | promoted | parked | killed
ice: { impact: 0, confidence: 0, ease: 0, value: 0 }   # 1 to 10 each; value is the product
elo: 1500               # relative rank from the pairwise tournament; default 1500
elo_games: 0            # comparisons played; low means the rank is unsettled
lens: "[the generative lens that produced it]"
parents: []             # ids this idea evolved or combined from (plain ids, not links)
serves: "[venture, project, or topic path; a plain path, not a link]"
-->

# [Idea title]

[A short paragraph: the idea, why it might work, and the open question or assumption it rests on. Keep it lightweight until it earns development. The id is the stable dedup and lineage key and is never reused; lifecycle, ice, and elo are maintained by the Discovery team as the idea moves through the pool. Idea records are leaves: parents are plain ids and serves is a plain path, so the record links to nothing in the graph.]
