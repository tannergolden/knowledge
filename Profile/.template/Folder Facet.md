<!--
title: '[emoji] [FACET]'
description: '[What this facet of the owner holds, with one entry per item, in a sentence or two.] Read it [when this facet bears on the work, such as when weighing options].'
type: 'template'
keywords: ["[synonym]", "[another synonym]", "template"]
-->

<!-- On copying: this makes the README of a facet that is a folder, saved as Profile/<Facet>/README.md, never as a note named after the folder: the facet's overview, a page, above one entry file per item. A facet read as a whole is a flat file instead, made from Facet Overview.md. Then:
- Only with the owner's yes: Profile/ is read-only unless the owner asks or confirms (Profile/README.md, Rules). A new folder facet, or a flat one that has grown entries and moves its overview here, is a structural change registered in three places: FACETS in .github/scripts/profile-coverage.py, so it is scored; PROFILE_COLLECTIONS in .github/scripts/vault.py, so update-vault.py lists its entries; and the facet table in Profile/README.md, which links this README (Profile/README.md, How The Facets Are Built). A new facet, rather than a flat one moving here, also changes every count of the facets: the twelve, and the eleven of the stable self, in Profile/README.md's description and tagline; the twelve in .docs/references/Glossary.md, .docs/introduction/Setting-Up-A-Vault.md and .github/scripts/profile-coverage.py; and the count .github/scripts/test_profile_coverage.py checks, which CI runs.
- Set type to "reference". Replace [emoji] and [FACET] in the title and the H1 alike with a fitting emoji and the facet's name, fully capped, and give the copy its real description and keywords: lowercase, at most eight, each distinct, none already in the title, with "template" dropped.
- Replace every [bracketed] placeholder: the one-line description and the tagline under the H1, each section, the entries section's heading and text, and the closing phrase, each the facet's own, as Profile/Values/README.md shows. A section with nothing to say yet goes, and no prompt is kept, one carried over from the flat facet a folder grew from included.
- One section for each fact that can be asked about on its own, its subject named in the heading behind an emoji, with a rule between sections. The Snapshot is written last.
- Write only what the owner said, or what was observed directly. A stated fact carries no marker. An inference ends its line with the provenance marker Profile/README.md defines (Provenance And Freshness), an HTML comment that reads observed YYYY-MM-DD · confidence: low|medium|high · unconfirmed, and it stays unconfirmed until the owner approves it. The most private facts are kept terse, each in an entry of its own (Profile/README.md, Sensitivity).
- Leave the entries block to update-vault.py, which draws it once the folder is in PROFILE_COLLECTIONS; it is never edited by hand. Name other files by plain path.
- Once filed, lint-notes.py checks it, update-vault.py draws its entries, and profile-coverage.py scores it.
- Delete this note from the copy.
-->

<div align="center">

# [emoji] [FACET]

<a name="top"></a>

**[One line: what this facet holds about the owner, and when it is read.]**

_[A principle of this facet's own, shorter than the line above.]_

</div>

---

## 💡 What This Folder Is For

[What this facet holds, and where the nearest things live instead, each named by path.]

---

## 📸 Snapshot

[A few lines on the whole facet. Written last.]

---

## [emoji] [Aspect]

[A field or a cluster of related facts. One section for each aspect.]

---

## 🗂️ [Entries, named for what they are]

[One entry per item. Add one by copying `Profile/.template/[Scaffold].md` here as `<Title>.md`; `update-vault.py` keeps the list below.]

<!-- brain:profile-entries (drawn by .github/scripts/update-vault.py - do not edit by hand) -->
_None recorded yet._
<!-- /brain:profile-entries -->

---

<div align="center">

**[A closing phrase of this facet's own.]**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
