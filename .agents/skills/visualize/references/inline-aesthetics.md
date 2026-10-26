# Inline aesthetics and native feel

What makes an inline visual beautiful and feel like a native part of the conversation, across every format. This is the aesthetic craft layer. The quality standard (graphical integrity, perceptual effectiveness) and the WCAG accessibility floor with its exact contrast numbers live in `principles.md` and are enforced by the Design Critic; this reference does not repeat them, it adds the typography, color, layout, and motion craft.

## Typography

- Use a restrained type scale and only two weights: a normal weight (400 to 500) for body and labels, and one heavier weight for emphasis. Build hierarchy through size, weight, and color, not by piling on weights. To de-emphasize, use a lighter color or smaller size, not a thinner weight ([Refactoring UI, color](https://refactoringui.com/previews/building-your-color-palette/)).
- Prefer sentence case over Title Case or ALL CAPS, everywhere including chart labels and diagram headings. Sentence case is the most readable and is the modern UI standard ([Every Interaction, title vs sentence case](https://www.everyinteraction.com/articles/title-case-vs-sentence-case-in-ui/)).
- Use a system font stack (`system-ui, -apple-system, Segoe UI, Roboto, sans-serif`) so nothing has to download and the visual matches the host platform.

## Color and theming

- Use flat, restrained palettes: reserve color for emphasis, hold to roughly two or three hues plus grays, and de-emphasize the surrounding elements rather than over-saturating the focal one ([Refactoring UI, building your color palette](https://refactoringui.com/previews/building-your-color-palette/)).
- Theme via CSS custom properties and `currentColor` so a visual inherits the host text color and adapts on its own; support dark mode with `@media (prefers-color-scheme: dark)`, and use the `color-scheme` property for embedded SVG or iframes ([MDN, prefers-color-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme)).
- For categorical data use a colorblind-safe qualitative ramp: Okabe-Ito's eight colors `#E69F00 #56B4E9 #009E73 #F0E442 #0072B2 #D55E00 #CC79A7 #000000`, distinguishable under the common color-vision deficiencies and distinct in grayscale ([Okabe-Ito guide](https://vizcept.com/blog/okabe-ito-palette-guide)). For continuous data use a perceptually uniform sequential map (viridis, or magma, plasma, inferno), uniform even in black and white, or a ColorBrewer scheme ([viridis](https://cran.r-project.org/web/packages/viridis/vignettes/intro-to-viridis.html)).
- Never carry meaning by color alone: back semantic color with a redundant label, icon, shape, or pattern (this is the WCAG 1.4.1 rule enforced via `principles.md`).
- The concrete palette library to pick from (categorical, sequential, and diverging, with colorblind-safe defaults) is in `palette.md` and `assets/palettes.json`.

## Layout and signal-scarcity

- Build on a grid: align elements, give generous whitespace, and keep the piece compact so it sits cleanly in a chat bubble.
- Establish hierarchy through size, weight, and color, and actively de-emphasize secondary content so the focal point wins.
- Stay sparse. Emphasis is zero-sum: if everything is emphasized, nothing is. Remove competing elements rather than adding accents ([NN/g, clutter-free charts](https://www.nngroup.com/articles/clutter-charts/)).

## Data-ink and minimalism

Maximize the data-ink ratio, the share of ink that encodes information: erase non-data ink (decorative gridlines, frames, tick clutter, fills) and redundant data ink, within reason ([Tufte, data-ink](https://usefuldatatips.com/tips/visualization/data-ink-ratio)). Stephen Few operationalizes this for screens: remove non-data pixels (borders, fill colors, gradients, 3D, non-essential gridlines) and enhance the data pixels. Gradients, drop shadows, and 3D are chartjunk; flat surfaces read as native.

## Motion (interactive pieces only)

- Keep transitions short and standard: Material specifies about 150 to 200 ms for small transitions, with easing that decelerates longer than it accelerates ([Material, duration and easing](https://m3.material.io/styles/motion/easing-and-duration)). Motion should clarify a change, never decorate.
- Honor `prefers-reduced-motion`: inside `@media (prefers-reduced-motion: reduce)`, gate or replace scaling and panning animations (for example, swap a scaling pulse for an opacity fade) ([MDN, prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion)).

## Native feel versus failure modes

Native feel is a flat, compact extension of the conversation: flat surfaces with no gradients, shadows, or noise; colors host-matched via `currentColor` or custom properties; sentence-case, two-weight type; right-sized to the bubble; high data-ink; and a text alternative present.

The failure modes, each the inverse of a rule above:
- Chartjunk and overcrowding (violates data-ink and signal-scarcity).
- Low contrast below the floor in `principles.md` (violates WCAG 1.4.3 and 1.4.11).
- Oversized or broken rendering that overflows the bubble.
- Gradients, drop shadows, and 3D that break flatness.
- Color-only encoding with no redundant cue.
- Explanatory prose stuffed inside the graphic instead of in the chat text or the description: it is non-data ink and invisible to assistive tech. Text goes in the response; the visual carries the visual.

## Sources

- Refactoring UI (color and typography); Every Interaction and USAGov (sentence case); EightShapes (typography in design systems).
- MDN: prefers-color-scheme, prefers-reduced-motion. Material Design (duration and easing).
- Okabe-Ito palette guide; viridis (CRAN); ColorBrewer. Nielsen Norman Group (clutter-free charts).
- Tufte (data-ink ratio); Stephen Few (information dashboard design).
