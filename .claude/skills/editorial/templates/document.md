<!--
title: "[Document Title]"
description: "[One or two task-shaped sentences: what this document is and when to read it. Do not echo the title.]"
type: "[guide | index | reference | record]"
-->

# [emoji] [Document Title]

<!-- A vault note. Single emoji-led H1 (AGENTS.md, Conventions); the YAML title stays plain.
     No em dash anywhere (DOC-002). No slop (DOC-003). Format per references/formatting.md: restraint by default,
     every rich element earns its place. Lint is the exit gate: `python3 .github/scripts/lint-notes.py`. -->

[The bottom line or one-line summary, so a reader can stop early. Put the conclusion above the fold.]

## [First section]

[One idea per paragraph, led with the idea. Short paragraphs. Plain, direct prose.]

> [!TIP]
> **[A callout earns its place only where it helps the reader understand faster than prose]**
> [Use a callout, table, or diagram where it does real work, not for decoration. A collapsible `<details>`
> block manages density in a long doc. Owner can override the default density per document.]

## [Second section]

[Reach for a table only when the data is genuinely tabular:]

| [Column] | [Column] |
|----------|----------|
| [cell]   | [cell]   |

[Reach for a fenced code block, tagged with a language, for code or literal output. Reach for a
`mermaid` fence for a diagram whose relationship is genuinely structural or sequential.]

## [Closing section]

[End on the last real point. No generic uplift conclusion and no zoom-out to nothing.]
