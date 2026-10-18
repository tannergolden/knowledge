---
title: "Markdown Style Guide"
description: "An opinionated house style for writing clean, readable, portable markdown: document structure, headings, core elements, diagrams and math, platform deltas (CommonMark, GFM, Obsidian, Discord), and a markdownlint/Prettier/Vale toolchain with ready-to-use configs."
status: "active"
tags: ["library", "reference", "current"]
aliases: ["Markdown Best Practices", "Markdown Formatting Guide", "Markdown House Style"]
keywords: ["commonmark", "github flavored markdown", "markdownlint", "vale", "mermaid", "form/howto", "level/intermediate", "class/technology-applied-science", "div/applied-computing-software"]
created: 2026-06-21
updated: 2026-06-21
type: "reference"
folder: "library"
layer: 3
policy: false
author: "Tanner Golden"
path: "BRAIN/Library/Technology & Applied Science/Applied Computing & Software/Markdown Style Guide.md"
id: "li-markdown-style-guide"
---

# 📝 Markdown Style Guide

An opinionated, copy-pasteable house style for writing markdown that is clean,
readable, and portable. It targets a **CommonMark + GitHub Flavored Markdown
(GFM)** core and calls out where Obsidian and Discord differ. The Tooling section
includes ready-to-use markdownlint, Prettier, and Vale configs that enforce most
of it automatically.

## Contents

- [Principles](#principles)
- [1. Document structure](#1-document-structure)
- [2. Headings](#2-headings)
- [3. Prose and line breaks](#3-prose-and-line-breaks)
- [4. Lists](#4-lists)
- [5. Code](#5-code)
- [6. Tables](#6-tables)
- [7. Links and images](#7-links-and-images)
- [8. Callouts and alerts](#8-callouts-and-alerts)
- [9. Diagrams and math](#9-diagrams-and-math)
- [10. Emoji](#10-emoji)
- [11. Platform deltas](#11-platform-deltas)
- [12. Tooling](#12-tooling)
- [Quick checklist](#quick-checklist)
- [See also and sources](#see-also-and-sources)

## Principles

1. **Structure before style.** A clean heading hierarchy is the single highest-leverage habit, for readers and for assistive technology.
2. **Whitespace is structural.** Blank lines around blocks and short paragraphs do more for readability than any decoration.
3. **The right element for the job.** Reach for a table, list, code block, or diagram because it fits the content, not for variety.
4. **Restraint with rich content.** Diagrams, math, HTML, and emoji earn their place or they leave.
5. **Keep the source readable.** The raw `.md` should read cleanly as plain text, because that is what survives across renderers and diffs.

## 1. Document structure

- Start every document with a single H1 that names it, then never use H1 again.
- Order long documents so a reader can stop early: title, one-line summary, then detail. Put the conclusion above the fold.
- Add a table of contents and "back to top" links once a document passes roughly two screens.
- Use collapsible sections for optional depth (GFM and Obsidian render raw HTML):

  ```html
  <details>
  <summary>Show the long version</summary>

  Content here, with a blank line after the summary so markdown inside renders.

  </details>
  ```

- Keep paragraphs to three to seven lines. A wall of text is a structure problem, not a length problem.

## 2. Headings

| Rule | Do | Don't |
| --- | --- | --- |
| One H1 | `# Project name` once | Multiple H1s in one file |
| No skipped levels | `##` then `###` | `##` then `####` |
| Style | ATX (`##`), sentence case | Setext (`---`), Title Case, trailing `:` |
| Punctuation | No trailing period | `## Setup.` |
| Phrasing | Front-load the key word, keep parallel | Vague or inconsistent grammar |

Skipping heading levels breaks screen-reader navigation, and most screen-reader
users move through a page by its headings. Treat the hierarchy as the document's
spine.

## 3. Prose and line breaks

- Write one idea per paragraph and lead with it.
- Pick a line-wrapping policy and hold it across the repo:
  - **Semantic line breaks** (recommended for prose-heavy docs): start a new
    source line after each sentence. Markdown joins them with a space, so the
    rendered output is unchanged but diffs stay sentence-level and clean.
  - **One long line per paragraph** (let the editor soft-wrap): also fine.
  - Do not mix the two in the same file.
- Never rely on trailing-whitespace line breaks. Use a blank line for a new
  paragraph, or an explicit `<br>` if you truly need a hard break inside one.

## 4. Lists

- Use one marker for unordered lists across the project (`-` recommended; it is
  the most common and reads cleanly).
- Use `1.` for ordered lists. You may keep every item `1.` and let the renderer
  number them, which makes reordering diff-free.
- Indent nested items by two spaces.
- Put a blank line before and after every list.
- Task lists (`- [ ]` / `- [x]`) are GFM, not CommonMark. Use them on GitHub,
  not in portable docs.

## 5. Code

- Always use fenced code blocks (triple backticks), not indented blocks.
- Tag every fence with a language so it highlights: ```` ```python ````, ```` ```bash ````, ```` ```json ````.
- Use ```` ```text ```` for plain output and ```` ```diff ```` for diffs.
- Put a blank line before and after each fenced block.
- Use inline `code` for identifiers, filenames, flags, and literal values in prose.

## 6. Tables

- Tables are a GFM extension. They do not render in plain CommonMark or in Discord.
- Set alignment in the delimiter row: `:---` left, `:---:` center, `---:` right.
- Keep tables narrow. If a table needs horizontal scrolling, a list is usually better.
- Escape a literal pipe inside a cell as `\|`.
- Cells need not be padded to equal width in the source, but a formatter
  (Prettier) will align them for you, which makes the raw table readable.

```markdown
| Name  | Type   | Required |
| :---- | :----: | -------: |
| id    | string |      yes |
| label | string |       no |
```

## 7. Links and images

- Prefer descriptive link text. Never link the words "here" or "click here".
- Use inline links for one-offs; switch to reference-style links when the same
  URLs repeat or when link-heavy prose gets hard to read in source:

  ```markdown
  See the [spec][cm] and the [GitHub docs][gh].

  [cm]: https://spec.commonmark.org/
  [gh]: https://docs.github.com/
  ```

- Every meaningful image needs alt text that states its **function in context**,
  not a generic label. Decorative images take empty alt (`![](path)`), so
  assistive tech skips them.

## 8. Callouts and alerts

- GitHub alerts use blockquote syntax with a type marker, and there are exactly
  five types:

  ```markdown
  > [!NOTE]
  > Useful context.

  > [!WARNING]
  > Something that can cause data loss.
  ```

  Types: `NOTE`, `TIP`, `IMPORTANT`, `WARNING`, `CAUTION`. Limit them to one or
  two per document, and do not nest them.
- Obsidian callouts look similar but use lowercase types and support many more
  (`> [!note]`, `> [!info]`, `> [!bug]`, foldable with `> [!note]-`). They do
  **not** render on GitHub.

## 9. Diagrams and math

- Keep diagrams in version control as code, not as binary images, where the
  platform supports it. GitHub and GitLab render Mermaid in a ```` ```mermaid ````
  fence; Obsidian renders it with the Mermaid core plugin.
- Match the Mermaid diagram type to the relationship: `flowchart` for process,
  `sequenceDiagram` for interactions over time, `classDiagram` for structure,
  `stateDiagram` for transitions, `gantt` for schedules.
- Math is LaTeX. GitHub and Obsidian render it via MathJax; inline `$E = mc^2$`,
  block `$$ ... $$`. GitLab and Hugo use KaTeX. Confirm the engine on your target.
- Diagrams and math are platform-dependent. In a portable document, link to an
  image fallback or note that rendering requires a specific platform.

## 10. Emoji

- Use emoji sparingly and never as the sole carrier of meaning (a screen reader
  announces them by name, which gets noisy).
- Prefer Unicode emoji (paste the character) over `:shortcode:` forms; shortcodes
  are not portable and many editors leave them as raw text.

## 11. Platform deltas

| Feature | CommonMark | GitHub (GFM) | Obsidian | Discord |
| --- | :---: | :---: | :---: | :---: |
| Tables | no | yes | yes | no |
| Task lists | no | yes | yes | no |
| Strikethrough `~~` | no | yes | yes | yes |
| Alerts / callouts | no | yes (UPPER) | yes (lower) | no |
| Footnotes | no | yes (renderer) | yes | no |
| Wikilinks `[[ ]]` | no | no | yes | no |
| Mermaid / math | no | yes | yes (plugins) | no |
| Images | yes | yes | yes | no |
| Spoilers `\|\|text\|\|` | no | no | no | yes |

Notes:

- **GFM the spec vs GitHub the renderer.** The frozen 2019 GFM spec adds only
  five things (tables, task lists, strikethrough, autolinks, raw-HTML filtering).
  Alerts, footnotes, emoji shortcodes, and `@mentions` are GitHub's live
  renderer, not the spec, so they will not work on a generic GFM engine.
- **Obsidian** layers wikilinks, embeds (`![[ ]]`), highlights (`==text==`),
  comments (`%% %%`), block refs (`^id`), and YAML "properties" frontmatter on
  top of CommonMark + GFM.
- **Discord** is a minimal chat subset: bold, italic, underline, strikethrough,
  spoilers, inline and block code, three heading levels, subtext (`-# `), lists,
  block quotes, and masked links (in bots and embeds only). No tables, images,
  footnotes, or horizontal rules.

**Portability rule:** target CommonMark plus the one platform you publish to.
Avoid extensions you do not need, and keep a plain-text fallback in mind for
anything platform-specific.

## 12. Tooling

Wire these into the editor and CI so style is automatic, not manual. The full
configs follow.

| Tool | Job |
| --- | --- |
| markdownlint (markdownlint-cli2) | Structural rules: heading levels, list style, fenced-code language, blank lines |
| Prettier (or dprint) | Auto-format: spacing, list markers, table alignment |
| Vale | Prose style: enforces a Google or Microsoft style package |

Typical run:

```bash
npx markdownlint-cli2 "**/*.md"   # lint structure
npx prettier --write "**/*.md"    # auto-format
vale sync && vale .               # prose lint (after fetching the style package)
```

### markdownlint (`.markdownlint.jsonc`)

```jsonc
// markdownlint configuration (markdownlint-cli2 and the VS Code extension).
// Rule reference: https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md
{
  "default": true,
  "MD003": { "style": "atx" },                 // ATX headings ("## Heading")
  "MD004": { "style": "dash" },                // one unordered-list marker
  "MD007": { "indent": 2 },                    // nested lists indent by 2
  "MD013": false,                              // line length: leave to the writer/Prettier
  "MD024": { "siblings_only": true },          // duplicate headings only across sections
  "MD025": true,                               // exactly one H1
  "MD033": { "allowed_elements": ["details", "summary", "br", "sub", "sup", "kbd", "img"] },
  "MD040": true,                               // every fence declares a language
  "MD041": true,                               // first line is an H1
  "MD046": { "style": "fenced" },              // fenced code blocks, never indented
  "MD048": { "style": "backtick" },            // backtick fences
  "MD049": { "style": "asterisk" },            // italic uses asterisks
  "MD050": { "style": "asterisk" }             // bold uses asterisks
}
```

### Prettier (`.prettierrc.json`)

```json
{
  "printWidth": 80,
  "tabWidth": 2,
  "proseWrap": "preserve",
  "overrides": [
    { "files": "*.md", "options": { "proseWrap": "preserve" } }
  ]
}
```

`proseWrap: "preserve"` matters: some renderers (notably GitHub comments) are
linebreak-sensitive, so Prettier should not reflow prose by default.

### Vale (`.vale.ini`)

```ini
StylesPath = styles
MinAlertLevel = warning
Packages = Google

[*.md]
BasedOnStyles = Vale, Google
```

Run `vale sync` once to fetch the style package, then `vale .`. Swap `Google` for
`Microsoft` to use that style instead.

## Quick checklist

- [ ] Exactly one H1, no skipped heading levels, sentence case.
- [ ] Blank lines around headings, lists, code fences, and tables.
- [ ] Every code fence has a language tag.
- [ ] Descriptive link text; alt text on meaningful images.
- [ ] Tables and task lists only where the target platform renders them.
- [ ] At most one or two alerts; emoji used sparingly.
- [ ] One line-wrapping policy, applied consistently.
- [ ] `markdownlint`, `prettier`, and `vale` pass.

## See also and sources

Primary references behind this guide (verify platform-specific features against
current docs):

- CommonMark specification: https://spec.commonmark.org/
- GitHub Flavored Markdown spec: https://github.github.com/gfm/
- Basic writing and formatting syntax (GitHub Docs): https://docs.github.com/en/get-started/writing-on-github
- Google developer documentation style guide: https://developers.google.com/style
- Microsoft Writing Style Guide: https://learn.microsoft.com/en-us/style-guide/
- W3C WAI (headings, alt text): https://www.w3.org/WAI/tutorials/
- Mermaid documentation: https://mermaid.js.org/
- markdownlint rules: https://github.com/DavidAnson/markdownlint
- Prettier options: https://prettier.io/docs/options
- Vale: https://vale.sh/
- Obsidian Help (Obsidian Flavored Markdown): https://help.obsidian.md/
