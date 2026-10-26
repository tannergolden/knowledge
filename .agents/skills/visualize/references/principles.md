# Visualization principles - the durable craft knowledge

The doctrine the Design team works to, grounded in the established authorities. Read before the critique gate. The one standard is **graphical integrity**: the visual never distorts what is true. The craft rule beneath it is **legible and accessible**.

## Form by question (the Lead picks first)

The single highest-leverage call. Choose the form from the question and the data, before anything is drawn.

| The question is about | Form | Notes |
|-----------------------|------|-------|
| Comparison of values across categories | Bar or column | Sorted by value unless the order is inherent (time). Zero baseline. |
| A trend over ordered time | Line | Lines are compared to each other, so a non-zero axis is acceptable if clearly labeled. |
| Correlation between two variables | Scatter | Add a trend line only when it is honest. |
| Part-to-whole | Stacked bar, rarely a pie | A pie only for 2 to 3 slices; a sorted bar reads ranking better. |
| A process or decision logic | Flowchart | One flow direction; label decision branches. |
| Static structure or components | Architecture or entity diagram | Group by subsystem; minimize crossings. |
| Object interaction over time | Sequence diagram | Time down the page; actors across the top. |
| Events along time | Timeline | Consistent scale; label the events, not the gaps. |
| Exploration of many values | Interactive | Overview first, then zoom and filter, then details. |
| A concept or mechanism | Explanatory illustration | One visual language; semantic, not decorative. |

## Graphical integrity (Tufte)

- **Lie factor** = (size of the effect shown in the graphic) / (size of the effect in the data). Honest is near 1. A truncated bar axis or a distorted area inflates it.
- **Proportionality.** The geometry on the page is proportional to the numbers. Bars encode value by length, so the baseline starts at zero; clipping it is the most common lie.
- **Data-ink ratio.** Maximize the share of ink that encodes data; erase decorative grids, heavy frames, and redundant ink.
- **Chartjunk.** Remove ornament that encodes nothing: 3D, moire grids, gratuitous pictograms.
- **Forbidden by default:** truncated or non-zero baselines on bars; dual y-axes (they manufacture spurious correlation); 3D effects (perspective distorts magnitude); area or bubble encoding of a single quantity (radius-versus-area ambiguity).

## Perceptual effectiveness

- **Cleveland and McGill ranking** of how accurately people decode a channel, most to least: position on a common scale; position on nonaligned scales; length, direction, and angle (one rank together); area; volume and curvature; color shading and saturation. Encode the most important quantity with the highest channel available. This is why bars and dot plots beat pies (angle) and bubbles (area).
- **Munzner's effectiveness principle:** match the importance of an attribute to the salience of its channel; the most important attribute gets the most effective channel.
- **Preattentive attributes** (hue, size, orientation) let a viewer spot a target in under about 250 ms without serial search; use one, not five, to mark what matters.
- **Bertin's visual variables** (position, size, shape, value, color, orientation, texture) are the encoding vocabulary.

## Gestalt grouping (especially diagrams and dashboards)

The eye groups marks by **proximity** (nearness), **similarity** (shared color or shape), **enclosure** (a shared border or shaded region), **connectedness** (linked elements read as one, the strongest cue), and **continuity and closure**. Lay panels and clusters out so the grouping the eye sees matches the relationships in the data.

## Accessibility (WCAG 2.2, the blocking floor)

- **1.4.3 Contrast (Minimum), AA:** text at least **4.5:1**; large text at least **3:1**, where large is **18 point, or 14 point bold**.
- **1.4.11 Non-text Contrast, AA:** UI components and the parts of graphics required to understand the content at least **3:1** against adjacent colors (not rounded; 2.99:1 fails).
- **1.4.1 Use of Color, A:** color is never the only means of conveying information; pair it with a label, a pattern, or direct labeling.
- **1.1.1 Non-text Content, A:** every chart or diagram carries a text alternative.
- **Palettes:** Okabe-Ito for categorical (color-vision-deficiency-safe and distinct in grayscale); viridis or ColorBrewer for sequential and continuous data.

## Interactive and dashboards

- **Shneiderman's visual information-seeking mantra:** "Overview first, zoom and filter, then details on demand." The overview is the first thing seen and guides the rest.
- **Stephen Few:** a dashboard fits a single screen; avoid clutter, meaningless variety, excessive precision, and inaccurate encoding. Surface the headline; do not make the user dig for it.
- **Progressive disclosure:** show the primary view by default; reveal depth on request, with discoverable, labeled, keyboard-reachable controls.

## Mode do's and don'ts (the high-leverage few)

- **Charts:** start bars at zero; match the chart type to the task; encode with position and length; sort and direct-label. Do not use a pie for more than 2 to 3 slices, dual y-axes, 3D, or a truncated bar axis.
- **Diagrams:** one flow direction; minimize edge crossings (the single most validated readability lever); conventional, consistent shapes; label decision branches. Do not space unevenly, over-branch, or color decoratively.
- **Interactive:** overview then zoom and filter then details; a sensible default state; discoverable controls. Do not bury the point or hide essential actions behind obscure affordances.
- **Illustration:** one visual language and abstraction level; semantic clarity over decoration; label what carries meaning. Do not substitute a pretty illustration where precision is required.

## The Critic's checklist (in order)

1. **Form-fit (first).** Is this the right form for the question and the data? Wrong form is FATAL even when the execution is flawless.
2. **Integrity, charts:** zero baseline on bars; lie factor near 1; no 3D, dual axis, or area-encoding of one quantity; chartjunk removed; comparisons on a common scale.
3. **Integrity, diagrams:** every real relationship present and no false one; crossings minimized; flow and hierarchy honest; consistent notation.
4. **Accessibility (blocking, enumerated):** text contrast at least 4.5:1 (3:1 large); non-text at least 3:1; never color alone; a color-vision-deficiency-safe palette; a text alternative present; interactive controls keyboard-reachable and labeled.
5. **Clarity:** one takeaway; the title states the so-what; axes, units, and legends labeled; an interactive supports overview, zoom and filter, and details on demand.

## Sources

- Edward Tufte, *The Visual Display of Quantitative Information* (graphical integrity, lie factor, data-ink, chartjunk).
- Cleveland and McGill, "Graphical Perception," JASA, 1984 (the perceptual-accuracy ranking).
- Tamara Munzner, *Visualization Analysis and Design* (the effectiveness principle).
- Jacques Bertin, *Semiology of Graphics* (visual variables).
- Stephen Few, *Information Dashboard Design* (dashboard principles).
- Ben Shneiderman, "The Eyes Have It," 1996 (the visual information-seeking mantra).
- W3C WAI, WCAG 2.2 Understanding documents, success criteria 1.4.3, 1.4.11, 1.4.1, 1.1.1.
- Okabe and Ito, Color Universal Design qualitative palette; viridis and ColorBrewer for sequential schemes.
