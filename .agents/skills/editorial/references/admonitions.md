# Callout (admonition) reference

The complete callout/admonition reference, loaded on demand: GitHub's five
alerts, the only types the vault uses (`AGENTS.md`, Conventions), and
Obsidian's full system, for a piece written for a target that renders it. `references/formatting.md`
is the doctrine (when a callout earns its place, the precedence, the scope by
destination); this file is the full syntax and the type
catalog. The machine-readable alias list lives in `assets/callout-types.json`.
For all other markdown elements see `references/markdown-reference.md`.

## What a callout is

A callout is a blockquote whose first line is a bracketed bang-type marker:
greater-than sign, space, then a square bracket, a bang, the type, and a closing
square bracket. The body is **arbitrary markdown** on the following `>` lines:
lists, code, tables, even nested callouts.

```markdown
> [!note]
> The body is ordinary markdown. A blank line after the type line is not
> required, but keep one before any list or code block inside.
```

The same blockquote-with-a-type-marker syntax is what GitHub calls an **alert**;
GitHub renders only five types and only in uppercase (see the GitHub subset
below).

## The complete built-in type set

Each row is one rendered style. The listed types are interchangeable **aliases**
for that style, and matching is **case-insensitive**. The machine-readable copy is
`assets/callout-types.json`.

| Style | Type and aliases | Use it for |
| :--- | :--- | :--- |
| Note | `note` | a neutral aside |
| Abstract | `abstract`, `summary`, `tldr` | a summary or stop-early line |
| Info | `info` | supporting context |
| Todo | `todo` | an open task |
| Tip | `tip`, `hint`, `important` | advice, a key point |
| Success | `success`, `check`, `done` | a confirmed result |
| Question | `question`, `help`, `faq` | an open question |
| Warning | `warning`, `caution`, `attention` | a hazard, a caveat |
| Failure | `failure`, `fail`, `missing` | a failed check, a gap |
| Danger | `danger`, `error` | a critical risk |
| Bug | `bug` | a known defect |
| Example | `example` | a worked example |
| Quote | `quote`, `cite` | a quotation |

## Worked examples

A few representative types, showing real bodies:

```markdown
> [!tip] Read this first
> Front-load the conclusion. A reader who stops here should still have the point.

> [!warning]
> This operation rewrites history. Back up the file before running it.

> [!success]
> Lint passed: one emoji-prefixed H1, zero em dashes, full frontmatter.

> [!example]
> Input `2026-06-24` returns the ISO week number, not the day of year.
```

## Syntax variants (the full set)

### Foldable callouts

A trailing `-` makes a callout **collapsed by default**; a trailing `+` makes it
**expanded but foldable**; a plain marker with no suffix is **static** (not
foldable). Foldable callouts are the density tool for long documents: depth stays
one click away instead of becoming a wall.

```markdown
> [!note]- Collapsed by default (click to open)
> Hidden until the reader expands it.

> [!note]+ Expanded but foldable (click to collapse)
> Shown by default, but the reader can fold it away.

> [!note] Static, always open
> Cannot be folded.
```

### Custom titles

Text after the type becomes the **title**. A type with a trailing space and no
text renders with the title bar **hidden**.

```markdown
> [!tip] A custom title replaces the default "Tip"

> [!note]
> Default title (the style name).
```

### Nesting

Stack `>` markers to nest one callout inside another. The practical ceiling is
**two levels**; deeper nesting reads worse than it helps.

```markdown
> [!question] Outer
> The outer callout body.
>
> > [!info] Inner
> > A nested callout, two levels deep.
```

### Callouts containing other markdown

The body is full markdown. **Every body line needs its own leading `>`**, blank
separator lines included, or the callout ends early; keep a blank `>` line before
a list or a code block so it renders, and a literal pipe inside a callout table
still escapes as `\|`.

````markdown
> [!example] A callout with a list and code
> Steps to reproduce:
>
> - clear the cache
> - re-run the build
>
> ```bash
> npm run build
> ```
>
> | Field | Value |
> | :---- | :---- |
> | env   | prod  |
````

## Custom types via a CSS snippet

Beyond the built-ins, a vault can define a custom callout type with a CSS
snippet. Match the snippet's data attribute to the type name you use in the
callout, and set the two callout variables: `--callout-color` (an `R, G, B`
triple) and `--callout-icon` (an icon id, for example a Lucide icon name, or an
inline SVG).

```css
.callout[data-callout="decision"] {
  --callout-color: 124, 58, 237;
  --callout-icon: lucide-git-branch;
}
```

With that snippet enabled, a callout whose type is `decision` renders with the
custom color and icon. Custom types are local to the Obsidian vault that defines
them and have no meaning anywhere else.

## The GitHub five (the vault's set)

In a vault note, on a page GitHub renders, and in any piece bound for GitHub, only
five alert types are used, written in **UPPERCASE** with the marker alone on its
line (GitHub takes no title after it, so a title is a bold lead-in on the first
body line):

```markdown
> [!NOTE]
> Useful context.

> [!WARNING]
> Something that can cause data loss.
```

The five types are **NOTE, TIP, IMPORTANT, WARNING, CAUTION**. GitHub advises
limiting alerts to one or two per document, and they **cannot be nested**. These
five are also the only callout vocabulary shared between Obsidian and GitHub.

### Degradation behavior

In any **non-Obsidian, non-GitHub** renderer (plain CommonMark, most static-site
engines, Discord), the bracketed type marker is **not** recognized: the callout
degrades to an ordinary, plain **nested blockquote**, with the marker line
showing as literal text. So a callout never breaks a page; it just loses its
styled box. This is why callouts beyond the GitHub five do not travel: write them
only for a target that renders them, such as an Obsidian vault; everywhere
else, the vault included, keep to the five uppercase types and convert the rest
to plain prose or blockquotes.

## When to use which type

A concise guide; the callout earns its place only when it helps the reader
understand faster than prose would (the beauty principle in
`references/formatting.md`).

Inside the vault, choose among the five: **NOTE** for an aside or a stop-early
summary, **TIP** for advice, **IMPORTANT** for the one point to retain,
**WARNING** for a hazard, and **CAUTION** for a risk of loss or harm. For an
Obsidian target, the full set reads:

- **`note` / `info`** - a neutral aside or supporting context that would clutter
  the main line. The default, low-emphasis choice.
- **`abstract` (`summary`, `tldr`)** - a stop-early summary at the top of a long
  piece, so a reader can leave with the conclusion.
- **`tip` (`hint`, `important`)** - advice or the one key point you most want
  retained.
- **`warning` (`caution`)** - a hazard or caveat: something that bites if
  ignored. **`danger` (`error`)** raises that to a critical, data-loss-grade
  risk.
- **`success` (`check`, `done`)** - a confirmed result, a passed gate.
  **`failure` (`fail`, `missing`)** - a failed check or a gap; **`bug`** - a known
  defect.
- **`question` (`help`, `faq`)** - an open question or an FAQ entry.
- **`todo`** - an open task tracked inline.
- **`example`** - a worked example set off from the prose.
- **`quote` (`cite`)** - a quotation attributed to a source.

Use the lowest-emphasis type that fits, reserve WARNING and CAUTION (Obsidian's
`warning` and `danger`) for genuine hazards so they keep their weight, and in a
long document prefer a `<details>` block (for an Obsidian target, a foldable
callout) over a wall of open boxes.
