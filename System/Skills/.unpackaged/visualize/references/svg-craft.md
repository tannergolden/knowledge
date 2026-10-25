# SVG craft - beautiful, reliable, theme-reactive hand-authored SVG

Hand-authored SVG is the primary inline format (see `formats.md` for when to use it). This is how to make it beautiful and reliable: it scales crisply, adapts to light and dark, never overflows its text, and carries a text alternative. The aesthetic bar is in `inline-aesthetics.md`; the quality standard is in `principles.md`.

## Setup and scaling

- Set `viewBox`, not pixel `width`/`height`. `viewBox="min-x min-y width height"` maps the user-space rectangle to the rendered element, and all inner coordinates resolve against it ([MDN viewBox](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/viewBox)). Let the host size it (`width: 100%; height: auto`) so it stays fluid and crisp at any DPI ([CSS-Tricks, scale SVG](https://css-tricks.com/scale-svg/)).
- `preserveAspectRatio` controls fit when the container ratio differs; the default `xMidYMid meet` scales uniformly and keeps the whole graphic visible. It has no effect without a `viewBox`.
- Draw no full-canvas background rect. SVG has no background by default, so it inherits the chat surface and stays transparent.

## Theming for light and dark

- Use `fill="currentColor"` and `stroke="currentColor"` so shapes inherit the host CSS `color` and recolor automatically when the theme flips ([Hidde de Vries, dark-mode SVG](https://hidde.blog/making-single-color-svg-icons-work-in-dark-mode/)).
- A hardcoded fill breaks dark mode. An unstyled or explicitly black shape stays invisibly dark on a dark surface, because the SVG default fill is black and dark-mode engines recolor CSS, not baked-in markup attributes ([MDN fill](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill)).
- For multi-color art, layer CSS custom properties with a `currentColor` fallback: `fill: var(--accent, currentColor)`, and respond to the OS preference with `@media (prefers-color-scheme: dark)` ([MDN prefers-color-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme)).

## Markers and arrowheads

Define arrowheads as a `<marker>` in `<defs>` and reference them with `marker-end` (or `marker-start`/`marker-mid`) on a line or path ([MDN marker](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/marker)).
- `markerUnits` defaults to `strokeWidth`, so the head scales with line weight.
- `orient="auto-start-reverse"` lets a single marker definition serve both ends pointing outward when it is referenced by both `marker-start` and `marker-end`; it reverses only the start marker, and on `marker-mid`/`marker-end` it otherwise behaves like `auto`.
- Set `fill="context-stroke"` on the marker path so the arrowhead matches the line color and tracks `currentColor` across themes; this is the detail most hand-SVG gets wrong (a black arrowhead on a themed line). `context-stroke` in markers is recent (Chrome and Edge 124, April 2024) and works in current webviews; when broad or older compatibility matters, set the marker's `stroke` and `fill` to `currentColor` directly as the fallback.

## Text that never overflows

SVG `<text>` does not wrap by default; the content area is otherwise treated as infinite ([MDN text](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/text); [W3C SVG2 text](https://www.w3.org/TR/SVG/text.html)). So:
- Keep labels short and size boxes from estimated text width: budget about 0.55 to 0.6em per character at the chosen font size, plus padding. A 20-character label at 14px is roughly 180px wide, so a box needs about 180 plus 2x the padding.
- Constrain a single line with `textLength` plus `lengthAdjust`. The user agent ensures the text does not extend past that width, which also keeps width stable even if a web font fails to load ([MDN textLength](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/textLength)). Use `lengthAdjust="spacingAndGlyphs"` only when you accept glyph scaling.
- For multi-line, stack `<tspan>` children with an incremental `dy`. Reserve `foreignObject` (real HTML wrapping) for genuinely long passages; it is a heavier dependency.
- Color text with `fill`, never `color` (the `color` property is for HTML).

## Accessibility

- For a meaningful graphic use `role="img"` on the `<svg>`, a short `<title>` (first child) and a longer `<desc>`, wired with `aria-labelledby="titleID descID"`. The explicit `aria-labelledby` link is the reliable pattern because browser and assistive-tech auto-exposure of bare title and desc is inconsistent ([CSS-Tricks, accessible SVGs](https://css-tricks.com/accessible-svgs/); [Smashing, accessible SVG patterns](https://www.smashingmagazine.com/2021/05/accessible-svg-patterns-comparison/)).
- For a purely decorative graphic, add `aria-hidden="true"` ([W3C WAI images](https://www.w3.org/WAI/tutorials/images/)).
- Add `focusable="false"` to avoid stray tab stops in legacy engines.

## Style and the common gotchas

- Stay flat and chartjunk-free: no gradients, drop shadows, or 3D (see `inline-aesthetics.md`).
- Fill inherits through `<g>`, so set color on a group and override only where needed. Beware that `opacity` does not inherit while `fill-opacity` does.
- Keep hairlines crisp under transform scaling with `vector-effect="non-scaling-stroke"` (it applies under `transform`, not plain CSS resize) ([MDN vector-effect](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/vector-effect)).
- Assume no installed fonts; use a system stack: `font-family="system-ui, -apple-system, Segoe UI, Roboto, sans-serif"`.
- The y axis grows downward; only the `viewBox` clips, so keep stroked shapes inside the box by half the stroke width to avoid edge clipping.

## A minimal setup skeleton

```
<svg viewBox="0 0 W H" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="t d">
  <title id="t">short title</title>
  <desc id="d">one-sentence description of what the visual shows</desc>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6"
            orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5"
            stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
  </defs>
  <!-- shapes use fill/stroke="currentColor" or a CSS var; text is short and pre-sized -->
</svg>
```

## Do and don't

- Do set `viewBox` plus fluid sizing; don't hardcode pixel `width`/`height`.
- Do use `currentColor` or CSS vars; don't bake in black or a fixed hex (default fill is black, invisible in dark mode).
- Do give markers `context-stroke` and `orient="auto-start-reverse"`; don't hardcode the arrowhead color.
- Do keep labels short, pre-size boxes, and use `textLength`/`tspan`; don't assume text wraps or a font exists.
- Do add `role="img"` plus `aria-labelledby` to title and desc, or `aria-hidden` if decorative; don't ship an unlabeled meaningful graphic.

## Sources

- MDN SVG references: viewBox, preserveAspectRatio, marker, orient, textLength, text, fill, vector-effect, prefers-color-scheme.
- W3C SVG 2 text spec; W3C WAI images tutorial.
- CSS-Tricks (accessible SVGs, scale SVG); Smashing Magazine (accessible SVG patterns); Hidde de Vries (single-color SVG icons in dark mode).
