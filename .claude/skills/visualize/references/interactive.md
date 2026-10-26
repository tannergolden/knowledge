# Interactive HTML widgets and charting libraries

How to build a self-contained interactive widget and which charting library to reach for. Use this when the visual is a data chart with axes, or one the reader should explore (hover, zoom, filter). When exploration is not the point, a static SVG (`svg-craft.md`) or a table is better. Interaction is governed by `principles.md` (overview first, then detail) and `inline-aesthetics.md` (flat, restrained, accessible).

## Self-contained widgets

Build one HTML document carrying its own inline `<style>` and `<script>`, so it renders with zero network dependencies. Many inline and sandboxed renderers (iframe `srcdoc`, CSP-restricted embeds) block external scripts entirely, so a widget that loads a CDN script can simply fail. The safe default is dependency-free, or the library's minified source inlined into the document. When you must load from a CDN, use Subresource Integrity: add `integrity="sha384-..."` and `crossorigin="anonymous"`, so the browser refuses a tampered file ([MDN, SRI](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity)).

## Charting library decision matrix

| Library | Best for | Renders | Weight (approx) | Interactivity | Accessibility |
|---------|----------|---------|-----------------|---------------|---------------|
| **Chart.js** | Fast standard charts (line, bar, pie) with little config | Canvas | ~80 KB gzip full, tree-shakeable | Hover, tooltip, animation built in | Manual: canvas is opaque, add `role="img"` plus a label or fallback |
| **D3.js** | Bespoke, fully custom, novel visuals | SVG (also canvas) | ~90 KB gzip full, tiny modular | Build-your-own via DOM events | Strong: SVG nodes are inspectable and labelable |
| **Vega-Lite** | Declarative JSON specs, quick exploratory charts | SVG or canvas | heavier (ships Vega runtime) | First-class selections, pan, zoom | SVG mode helps |
| **ECharts** | Large datasets, dashboards, many chart types | Canvas plus SVG | ~100 KB gzip tree-shaken | Rich: dataZoom, brush, tooltip, legend | Best out of the box: auto ARIA descriptions |
| **Plotly.js** | Scientific, statistical, 3D, publication quality | SVG plus WebGL | heaviest, ~2 MB plus | Zoom, pan, hover built in | Partial; SVG inspectable |
| **Observable Plot** | Concise exploratory charts, grammar of graphics | SVG | light, built on D3 | Lighter than ECharts or Plotly | SVG-based |

Reach for **Chart.js** for a quick standard chart, **Observable Plot** or **Vega-Lite** for concise declarative charts, **ECharts** for a dense dashboard with built-in interaction and the best default accessibility, **D3** only when you need something bespoke no library gives, and **Plotly** for scientific or 3D work where its weight is justified. Chart.js renders on canvas; D3, Observable Plot, and Vega-Lite (in SVG mode) render inspectable SVG ([Chart.js](https://www.chartjs.org/docs/latest/); [D3](https://d3js.org/); [Observable Plot](https://observablehq.com/plot/); [ECharts features](https://echarts.apache.org/en/feature.html)).

## Canvas versus SVG

SVG puts every shape in the DOM, so it slows as node count climbs into the thousands; the practical rule is to start with SVG and switch to canvas around a few thousand elements (hardware-dependent, an order-of-magnitude rule, not a hard number) ([JointJS, SVG vs canvas](https://www.jointjs.com/blog/svg-versus-canvas)). The accessibility tradeoff is decisive: SVG elements are in the DOM, carry semantics, and are exposed to assistive tech; a `<canvas>` is a single opaque element that exposes nothing but its fallback content. Prefer SVG for small, static, inspectable charts; reach for canvas only when node count genuinely demands it ([MDN, canvas](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Optimizing_canvas)).

## Responsive sizing

Size to the container, not the viewport, with `ResizeObserver` (observe the wrapper, read `inlineSize`, redraw); guard against feedback loops by deferring mutations with `requestAnimationFrame` ([MDN, ResizeObserver](https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver)). For crisp canvas on high-DPI screens, multiply the bitmap by `devicePixelRatio` while keeping the CSS size fixed, then `ctx.scale(dpr, dpr)` ([MDN, devicePixelRatio](https://developer.mozilla.org/en-US/docs/Web/API/Window/devicePixelRatio)). Chart.js encodes this: give it a dedicated relatively-positioned container and use `responsive` plus `maintainAspectRatio`, and never put width or height styles directly on the `<canvas>` (it blurs) ([Chart.js responsive](https://www.chartjs.org/docs/latest/configuration/responsive.html)).

## Interaction design

Structure interaction by Shneiderman's mantra: overview first, then zoom and filter, then details on demand ([Shneiderman 1996](https://www.cs.umd.edu/~ben/papers/Shneiderman1996eyes.pdf)). In practice: show the whole shape first, use tooltips and click-to-expand for details, apply progressive disclosure to keep the default view legible, give a sensible default state (no empty or loading dead-ends), and make every control keyboard-focusable and operable. For a canvas chart, add a labeled text or table fallback, since the pixels are opaque to assistive tech ([Chart.js accessibility](https://www.chartjs.org/docs/latest/general/accessibility.html)).

## Performance and failure modes

- A heavy library inlined balloons the document (Plotly is multi-megabyte); a single chart rarely justifies it.
- Oversized canvases: scale up with CSS transforms rather than allocating a huge bitmap, disable transparency when unused, avoid `shadowBlur`, batch draws, and use `requestAnimationFrame` ([MDN, optimizing canvas](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Optimizing_canvas)).
- Layout thrash: a `ResizeObserver` callback that mutates the observed element loops; defer with `requestAnimationFrame`.
- Too many SVG nodes: DOM repaint cost climbs past a few thousand elements; move to canvas.

## When interactive versus static

- Interactive HTML widget: the data rewards exploration (hover for details, zoom or filter dense or multi-series data, what-if controls).
- Static SVG: a fixed, small-node chart that must be inspectable, labelable, and dependency-free. Best for accessibility and reliable inline embedding.
- Static raster image: only when scripts are blocked and the visual will never need interaction, or node counts would choke the DOM.

## Sources

- Official docs: Chart.js (and its responsive and accessibility pages), D3, Vega-Lite, ECharts, Plotly.js, Observable Plot.
- MDN: ResizeObserver, devicePixelRatio, Subresource Integrity, optimizing canvas.
- Shneiderman, "The Eyes Have It," 1996; JointJS (SVG vs canvas).
