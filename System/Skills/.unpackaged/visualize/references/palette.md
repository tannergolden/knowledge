# Color palettes - the library and how to pick one

The skill ships a curated library of the most established data-visualization palettes (about 87) in `assets/palettes.json`, drawn verbatim from the canonical sources: ColorBrewer, the viridis family (matplotlib), Tableau, D3, Plotly, CARTOColors, Paul Tol, and Okabe-Ito. The Visualization Designer picks one palette per visual at creation, matched to the data; the Design Critic still enforces the accessibility gate on the choice. This reference is how to choose and apply; the colors live in the asset.

## Pick by data type first

The palette type is decided by what the data IS, not by what looks nice. `palettes.json` is split into the three types for exactly this reason.

- **categorical** (qualitative): distinct, unordered series with no ranking. Bars grouped by category, multi-line charts (one hue per line), pie or donut slices, maps of discrete classes. Color encodes identity, so hues must be maximally distinct with no implied order.
- **sequential**: ordered data running low to high in one direction. Heatmaps, choropleths of one quantity, density, counts. More reads as darker or more saturated. Color encodes amount.
- **diverging**: data with a meaningful midpoint and two directions away from it. Deviation from zero or a mean, surplus and deficit, correlation, z-scores, change. The neutral center marks the reference value; the two saturated ends mark the extremes. Align the data's reference point to the palette's midpoint, or the visual misleads.

## Prefer a colorblind-safe default

Unless a specific look is requested, default to a colorblind-safe palette (the `cvd_safe_defaults` block in the asset):

- **categorical:** Okabe-Ito (8 colors, the safest qualitative default), Tol Bright or Tol Muted, or Tableau Color Blind 10. Each was engineered and tested against red-green deficiency.
- **sequential:** viridis (perceptually uniform, monotonic lightness, legible under all color-vision deficiencies and in grayscale) or cividis (optimized for deficiency). Monotonic lightness is what keeps the order readable even when hue discrimination fails.
- **diverging:** ColorBrewer RdBu or BrBG, or Tol sunset. Two arms on opposite, distinguishable hue axes with a light neutral center.

A palette flagged `cvd_safe: false` (Set1, Spectral, Material, most Plotly and CARTO sets) is for when beauty or a specific brand mood outranks strict accessibility, and only after the Critic confirms the encoding still passes contrast and is not color-only.

## How to apply

- **categorical:** assign the palette's colors to series in order. Cap distinct series at about 8; Okabe-Ito and Tol Bright top out there because more hues stop being reliably distinguishable. Beyond 8, group the long tail into an "other" bucket, use small multiples, or direct-label the series instead of a color legend.
- **sequential:** map the ordered values across the ramp low to high; use the ramp's stops or interpolate between them for a continuous scale.
- **diverging:** put the data's zero or reference at the palette's neutral center, and scale the two arms symmetrically so equal deviations read as equal color distance.

## Palette for data, host tokens for chrome

The palette colors the data marks (bars, lines, slices, regions). The visual's chrome (text, axes, gridlines, borders) should still use the host theme via `currentColor` and CSS variables so it adapts to light and dark (see `svg-craft.md` and `inline-aesthetics.md`). Do not hardcode a palette color for text or axes. A categorical palette is for the series, not the frame.

## The Critic still gates

Picking from this library does not bypass the accessibility gate. The Design Critic checks the chosen palette in context: text and meaningful-graphics contrast meet the WCAG floor in `principles.md`, information is never carried by color alone (pair with labels, shapes, or direct labeling), and for multi-series categorical work the adjacent colors are actually distinguishable at the rendered size. A beautiful palette that fails these is sent back, not shipped.

## Sources

All hex in `assets/palettes.json` was copied verbatim from canonical sources and uppercased: ColorBrewer (colorbrewer2.org), the viridis family and coolwarm (matplotlib / the BIDS colormap project), Tableau's palette reference, d3-scale-chromatic, Plotly's qualitative color modules, CARTOColors (the CartoColor repo), Paul Tol's technical note, and the Okabe-Ito Color Universal Design set.
