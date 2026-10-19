---
title: "[Document Title]"
description: "[One or two task-shaped sentences: what this document is and when to read it. Do not echo the title.]"
status: "active"
tags: ["[folder tag]", "[file role tag]", "[freshness tag if Library]"]
aliases: []
keywords: ["[4 to 8 lowercase search terms a person would type that are not already in the title]"]
created: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
type: "[guide | information | reference | record]"
folder: "[library | projects | ventures | inbox | ...]"
layer: [0-4]
policy: false
author: "Tanner Golden"
path: "BRAIN/[full path from root]/[Document Title].md"
id: "[two-letter folder prefix]-[hyphenated-slug]"
---

# [emoji] [Document Title]

<!-- A vault-internal document. Single emoji-prefixed H1 (Constitution 9.6); the YAML title stays plain.
     No em dash anywhere (9.1). No slop (9.2). Format per references/formatting.md: restraint by default,
     every rich element earns its place. Lint is the exit gate: `python3 .github/scripts/lint-notes.py`. -->

[The bottom line or one-line summary, so a reader can stop early. Put the conclusion above the fold.]

## [First section]

[One idea per paragraph, led with the idea. Short paragraphs. Plain, direct prose.]

> [!tip] [A callout earns its place only where it helps the reader understand faster than prose]
> [Use a callout, table, or diagram where it does real work, not for decoration. Foldable `[!type]-`
> manages density in a long doc. Owner can override the default density per document.]

## [Second section]

[Reach for a table only when the data is genuinely tabular:]

| [Column] | [Column] |
|----------|----------|
| [cell]   | [cell]   |

[Reach for a fenced code block, tagged with a language, for code or literal output. Reach for a
`mermaid` fence for a diagram whose relationship is genuinely structural or sequential.]

## [Closing section]

[End on the last real point. No generic uplift conclusion, no "in conclusion", no zoom-out to nothing.]
