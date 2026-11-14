<!--
title: "[Facet Name]"
description: "[What this facet of the owner holds, in a sentence or two, and when to read it.]"
type: "template"
keywords: ["[synonym]", "template"]
-->

<!-- On copying: this makes a flat facet, one file read as a whole, saved as Profile/<Facet>.md, such as Profile/Focus.md. A facet that holds many separate items is a folder instead, and its README.md is made from Folder Facet.md. Then:
- Only with the owner's yes: Profile/ is read-only unless the owner asks or confirms (Profile/README.md, Rules). A new facet is a structural change, registered in FACETS in .github/scripts/profile-coverage.py, so it is scored, and in the facet table in Profile/README.md. It also changes the count of twelve in Profile/README.md's description and tagline and in .github/scripts/test_profile_coverage.py, which CI runs.
- Set type to "reference". Give the copy its real title, the facet's name as in the H1, a description of what it holds and when to read it, and keywords a search would use: lowercase, at most eight, each distinct, none already in the title, with "template" dropped.
- Replace [Facet Name] in the H1 behind a fitting emoji, and each [bracketed] prompt in the owner's own words, or delete it.
- One H2 for each fact that can be asked about on its own, its subject named in the heading, so each section reads as a complete answer when retrieved alone; discrete facts go in lists and tables. The Snapshot is written last.
- Write only what the owner said, or what was observed directly. A stated fact carries no marker. An inference ends its line with the provenance marker Profile/README.md defines (Provenance And Freshness), an HTML comment that reads observed YYYY-MM-DD · confidence: low|medium|high · unconfirmed, and it stays unconfirmed until the owner approves it. The most private facts are kept terse (Profile/README.md, Sensitivity).
- Name other files by plain path; a facet note carries no wikilinks.
- Once filed, lint-notes.py checks it, and profile-coverage.py scores it.
- Delete this note from the copy.
-->

# 🪪 [Facet Name]

[One paragraph: what this facet holds, and where the nearest things live instead, each named by path.]

## Snapshot

[One short paragraph a reader can lift as it is: the part most worth reading at a glance. Written last.]

## [Aspect]

[A field or a cluster of related facts. One H2 for each aspect.]
