<!--
title: '🔑 KEYWORDS'
description: 'How a note is found without tags: its path, its title and a few keywords, and the controlled tokens the Library filters on.'
type: standard
keywords: [search, discovery, freshness, facets]
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🔑 KEYWORDS

<a name="top"></a>

**How a note is found: its path, its title and a few keywords.**

_No tags. The subject lives in the path._

</div>

---

## 🎯 The Rule

There are no tags. The folder a note sits in is its subject
(`Library/Society & Social Sciences/Economics/`), so the path says what it is about, and full-text
search finds the rest. `keywords` carries what neither the path nor the title says: other names,
acronyms, former titles, and the words a person would actually type, including how they would
phrase the problem.

`.github/scripts/lint-notes.py` checks every note's keywords on each edit and in CI.

---

## ✍️ How Keywords Are Written

- Up to eight per note: the ones that best find it.
- Lowercase, each one distinct, and none already in the title.
- An inline array: `keywords: ["working memory", "capture stream"]`.
- Left out when nothing needs saying.

---

## 🔍 Controlled Tokens

A few keywords are controlled tokens, slash-namespaced so a script can filter on an exact match.
They come first in the list:

| Token                                                           | Carried by                           | Means                                                       |
| :-------------------------------------------------------------- | :----------------------------------- | :---------------------------------------------------------- |
| `freshness/timeless`, `freshness/enduring`, `freshness/current` | Every Library holding, exactly one   | How long it stays true (`Library/Library.md`, Rules)        |
| `form/`, `level/`, `period/`, `place/`, `class/`, `div/`        | A Library holding, where they help   | The catalog facets `Library/Library.md` defines             |

---

## 🧭 Where The Tags Went

| Tag             | Now                                                                                |
| :-------------- | :--------------------------------------------------------------------------------- |
| Folder          | The path                                                                           |
| File Role       | `type` ([Note Schema](Note-Schema.md))                                             |
| `startup`       | `STARTUP` in `.github/scripts/vault.py`, listed in `AGENTS.md`, Start here         |
| `sensitive`     | The path: everything under `Profile/` is personal                                  |
| Freshness       | A `freshness/` token, on Library holdings                                          |
| `policy` field  | The note's own Rules section says when it holds a policy                           |

---

<div align="center">

**The path says what. The keywords say what else.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
