# Inline visual formats - choosing and using each one

The format-selection layer: which renderable format to reach for, and the key craft and gotchas of each. The quality bar (graphical integrity, perceptual effectiveness, the accessibility floor) is in `principles.md` and applies whatever the format. Deep craft for the two primary formats is in `svg-craft.md` (hand-authored SVG) and `interactive.md` (HTML widgets and charting libraries).

## Which format for which job

| The visual is | Reach for | Why |
|---------------|-----------|-----|
| A diagram, badge, or small static chart (few data points) you can enumerate as shapes | Hand-authored **SVG** | Theme-reactive, crisp at any size, no runtime JS, accessible and inspectable |
| A process, architecture, or relationship graph with many nodes, or one that changes often | **Mermaid** (diagram-as-code) | Auto-layout beats hand-routing edges; renders inline in markdown; diffs cleanly |
| A data chart with axes, scales, legends, or many series | A **charting library** in an HTML widget | Hand-authoring axis and tick math is error-prone; libraries handle scales and interaction |
| Data the reader should explore (hover, zoom, filter) | An **interactive HTML widget** | Details-on-demand needs runtime behavior |
| Exact values, mixed units, or a small lookup | A **Markdown table** | A table beats a chart when readers look up or compare individual values |
| A formula or mathematical relationship | **Math** (KaTeX / MathML, `$...$`) | The relationship itself is the content |
| Something inherently geographic | A **map** (GeoJSON via D3-geo or Observable Plot) | Only when geography is the question; otherwise a bar or table is more precise |
| A word-sized magnitude in a list or a plain-text surface | **Unicode** block-element sparkline | When the medium is text-only and a real chart cannot render |

Default to the simplest format that carries the meaning. A static SVG or a table beats an interactive widget whenever exploration is not the point.

## Hand-authored SVG (the primary format)

Best for diagrams, flowcharts, architecture and state diagrams, badges, icons, annotated illustrations, and small bar/line/pie charts with a handful of points: anything enumerable as shapes that must be theme-reactive and crisp with no runtime JS ([CSS-Tricks, scale SVG](https://css-tricks.com/scale-svg/)). Renders inline anywhere SVG is allowed. Fully craftable for accessibility and dark mode. Full craft in `svg-craft.md`. Reach past it to a charting library when data is dynamic or dense and needs axes, scales, legends, or tooltips, since SVG text does not wrap and tick math is error-prone by hand ([MDN, SVG text](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/text)).

## Interactive HTML widgets and charting libraries

Best for data charts with axes and for visuals the reader should explore. Build a self-contained single file with inline CSS and JS; many inline and sandboxed renderers block external scripts, so prefer dependency-free or inlined code, and when loading a CDN library use Subresource Integrity ([MDN, SRI](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity)). Library selection, the canvas-versus-SVG crossover, responsive sizing, and interaction patterns are in `interactive.md`.

## Diagram-as-code (Mermaid and alternatives)

**Mermaid** is the diagram-as-code format that renders inline in markdown (GitHub since 2022, Obsidian, many chat UIs) via a fenced ` ```mermaid ` block ([Mermaid intro](https://mermaid.js.org/intro/); [GitHub diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams)). It covers flowchart, sequence, class, state, entity-relationship, gantt, pie, mindmap, timeline, gitgraph, and more. Prefer it over hand-SVG when topology is large or generated, when the diagram changes often (text diffs cleanly), or when it must render inline in markdown. Prefer hand-SVG when the diagram is a designed artifact needing pixel-precise layout and full color control.

Clean-Mermaid checklist:
- Pick direction by shape: `TD`/`TB` for hierarchies and decision trees, `LR` for pipelines and process flows.
- Group with `subgraph id [title] ... end`; note that if a subgraph node links outside, its internal `direction` is ignored.
- Reduce crossings: keep flow one-directional and declare nodes in flow order.
- Encode meaning in edge type: `-->` normal, `-.->` dotted (optional or async), `==>` thick (primary path); label edges sparingly.
- Style via `classDef` and `class ...:::name`, not per-node inline styles; target a link with `linkStyle`.
- Theme with `%%{init: {'theme':'base'}}%%` then `themeVariables` (`primaryColor`, `lineColor`, `fontFamily`); the five built-in themes are default, neutral, dark, forest, and base, and base is the customizable one ([Mermaid theming](https://mermaid.js.org/config/theming.html)).
- Always add `accTitle:` and `accDescr:` for the accessible title and description ([Mermaid accessibility](https://mermaid.js.org/config/accessibility.html)).

Alternatives, none of which render natively in markdown (they need a build step or plugin): **Graphviz/DOT** has best-in-class auto-layout for large or dense graphs (`dot` for hierarchies, `sfdp` for big force-directed graphs) ([Graphviz layouts](https://graphviz.org/docs/layouts/)); **D2** produces polished modern architecture diagrams with themes, sketch mode, and automatic dark mode ([d2lang.com](https://d2lang.com/)); **PlantUML** has the broadest UML coverage ([plantuml.com](https://plantuml.com/)).

## Markdown tables

A table communicates better than a chart when readers look up individual values, compare individual values rather than a whole series, need precise numbers, mix more than one unit, or want summary and detail together (Stephen Few, *Show Me the Numbers*; [Few, Effective Chart Design](https://www.perceptualedge.com/images/Effective_Chart_Design.pdf)). Use GitHub-Flavored-Markdown syntax: a header row, a delimiter row (`:---` left, `---:` right, `:---:` center), then data rows, with a blank line before the table ([GFM spec](https://github.github.com/gfm/)). Make it beautiful: right-align numeric columns so decimals line up, left-align text, keep headers terse, and stay near 3 to 6 columns so it does not wrap on narrow surfaces. The header row gives screen readers row and column relationships, so a real table is also the recommended text alternative for a complex chart or map. Gotchas: no block content, rowspan, colspan, nested tables, or multi-line cells; escape literal pipes as `\|`.

## Unicode and ASCII text-art

For a word-sized magnitude beside a number, or any genuinely text-only surface where SVG cannot render. The lower eighth-blocks U+2581 to U+2588 (`one eighth block` to `full block`) give eight steps of vertical resolution for inline bar charts and sparklines; the left eighth-blocks do the same horizontally for progress bars; Braille Patterns (U+2800 to U+28FF) pack a 2x4 dot grid per character for the densest text plots ([Block Elements](https://en.wikipedia.org/wiki/Block_Elements); [Braille Patterns](https://en.wikipedia.org/wiki/Braille_Patterns)). This requires a monospace font with the glyphs, or the bars smear out of alignment. Always pair the art with the literal value (`▇▇▅ 73%`) because screen readers may announce these code points as gibberish. Use it only when a real chart or table cannot render; otherwise it is a crutch.

## Math

Show a formula when the relationship or definition itself is the content; chart it when you are showing how the quantity behaves. Convention is `$...$` inline and `$$...$$` display (own line, centered); GitHub renders both in markdown, and many chat UIs render via KaTeX ([GitHub math](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)). **KaTeX** renders synchronously with no page reflow and ships a small bundle, but covers fewer LaTeX features; **MathJax** has broader LaTeX coverage and stronger accessibility (exploration and voicing). KaTeX was historically faster, but MathJax 3 has largely closed that gap, so choose KaTeX for synchronous rendering and light weight, MathJax for coverage and accessibility ([KaTeX](https://katex.org/); [MathJax](https://www.mathjax.org/)). Native **MathML Core** reached cross-browser Baseline in January 2023, so dependency-free, semantic math is now viable ([MDN, MathML](https://developer.mozilla.org/en-US/docs/Web/MathML)). Prefer display mode for tall constructs; keep inline math short; escape literal `$`.

## Maps

Reach for a map only when geography is the question (spatial clustering, adjacency, region-to-region pattern); if you are ranking magnitudes, a bar or table is more precise, because a choropleth distorts perceived magnitude by region area. Data is **GeoJSON** (RFC 7946: coordinate order is longitude then latitude, default CRS WGS 84 in decimal degrees) or **TopoJSON** (shares boundaries as arcs for much smaller files) ([RFC 7946](https://www.rfc-editor.org/rfc/rfc7946.html)). Render with **D3-geo** (`geoPath` turns GeoJSON into SVG paths) or **Observable Plot**'s `geo` mark (choropleth via `fill`, projection via the `projection` option) ([d3-geo](https://d3js.org/d3-geo); [Observable Plot geo](https://observablehq.com/plot/marks/geo)). Use an equal-area projection (Albers, Equal Earth) when comparing magnitudes across regions, never raw Mercator. The lon-then-lat order is the classic bug. Accessibility is hardest for maps: always provide a data-table alternative.

## Sources

- W3C and MDN: SVG text and SRI, MathML Baseline. CSS-Tricks, scale SVG.
- Mermaid official docs (intro, theming, accessibility); Graphviz, D2, PlantUML official docs; GitHub and Obsidian markdown docs.
- GFM table spec; Stephen Few, *Show Me the Numbers* and *Effective Chart Design*.
- Unicode Block Elements and Braille Patterns; KaTeX, MathJax, MDN MathML; GeoJSON RFC 7946, d3-geo, Observable Plot.
