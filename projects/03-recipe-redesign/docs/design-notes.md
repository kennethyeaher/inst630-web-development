# Design notes

## Organizing the cooking task

The redesign separates orientation from cooking. The title introduces the recipe, the timing row answers basic planning questions, and two clearly titled sections hold the ingredients and method. Each step starts with an action and uses bold text for temperatures, time, or spacing that someone might need to find quickly.

This applies the visual hierarchy discussion in *Designing Interfaces*, third edition, by Jenifer Tidwell, Charles Brewer, and Aynne Valencia (2020), pages 210–211, and the **Titled Sections** pattern on pages 238–239. The pattern supports grouping related content under strong headings and separating those groups with spacing. These page numbers refer to the printed book, not the PDF viewer.

On phones, the timing summary appears before the photo so planning information is available earlier. Ingredients remain before the instructions in the document. The native checklist avoids requiring scripts and uses the whole label as a target, following the [W3C guidance on labeling controls](https://www.w3.org/WAI/tutorials/forms/labels/).

## Assignment requirements

| Requirement | Implementation |
| --- | --- |
| Page layout with Grid | `.recipe` uses named `header`, `summary`, `photo`, `ingredients`, `instructions`, and `footer` areas |
| Mobile breakpoint | One column below `48rem`; two columns at `48rem` and above |
| Flexbox components | Timing row, section headings, ingredient labels, and numbered instruction rows |
| Responsive size range | Flexible columns, wrapping components, constrained page width, and text wrapping |
| Typography | Two font families; distinct title, section, step, and body sizes |
| Color | Five shared CSS color properties; no patterned background behind body text |
| Cooking usability | Ten labeled checkboxes, clear action, eight numbered steps, visible recipe metadata |
| Accessibility | Main landmark, heading hierarchy, native lists and controls, keyboard focus, skip link, image alternative |
| Code organization | Grouped CSS with comments, descriptive classes, spacing and typography properties |

## Verification record

Checked September 24, 2026, in Chrome 153.0.8010.54 against a local HTTP preview.

| Check | Result |
| --- | --- |
| Viewport widths | 320, 375, 480, 767, 768, 1024, 1200, and 1440 pixels: no horizontal overflow |
| Breakpoint | One column at 767 pixels and two columns at 768 pixels |
| Content | One main landmark, one primary heading, ten ingredients, eight instructions |
| Assets and links | Local photo loaded; internal jump targets resolved; no failed resource responses |
| Console | No warnings or errors during the browser checks |
| Checklist | Clicking the label checks the ingredient and strikes the text; clear action resets the list |
| Keyboard | Tab reaches skip link; Enter moves to ingredients; Space checks an item; Enter activates clear action |
| Accessible names | Browser accessibility tree contains names for all ten checkboxes |
| Touch targets | Every ingredient label is at least 44 CSS pixels tall |
| Enlarged text | 200% root font size at 320 pixels: no horizontal overflow after fixing long heading wrapping |
| Forced colors | Native checkbox remained operable in the simulated mode |
| Scripts disabled | Checklist and clear action remained functional |
| Print | Two Letter pages; all ingredients and steps retained; photo and navigation removed |
| Code whitespace | `git diff --check` passed |

The text enlargement check changes the root font size. It is not a claim that every browser zoom implementation was tested. Browser checks do not replace a full assistive technology audit. VoiceOver, NVDA, physical phones, Safari, Firefox, and physical printing have not been tested.

### Text contrast

Ratios were calculated from the CSS colors using relative luminance. All used text pairings exceed the [WCAG AA minimum of 4.5:1 for normal text](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).

| Text and background | Ratio |
| --- | --- |
| Ink on paper | 13.88:1 |
| Blue on paper | 8.49:1 |
| Ink on pale blue | 12.01:1 |
| Blue on pale blue | 7.34:1 |
| Ink on butter yellow | 8.64:1 |
| Paper on blue | 8.49:1 |
| Paper on ink | 13.88:1 |

These are text contrast measurements, not a claim of complete WCAG conformance. Decorative separators do not convey control states. Checkbox appearance follows the browser and operating system.

## Repeat the checks

1. Start the local server using the README instructions.
2. Inspect the page at 320, 375, 767, 768, 1200, and 1440 pixels. Confirm that content stays inside the viewport.
3. Click an ingredient label and confirm both its checked state and crossed text. Clear the list.
4. Reload, press Tab, and use the skip link. Toggle a checkbox with Space and activate Clear checks with Enter.
5. Disable JavaScript and repeat the checklist interaction.
6. Open print preview and confirm that all ten ingredients and eight steps remain readable.
7. Check the browser console and network panel for errors or missing assets.
8. Run `git diff --check` before committing.

## Published site

The [live recipe](https://kennethyeaher.github.io/uglyPageCute/) is published through GitHub Pages. The live page passed the same Chrome checks at all eight listed widths. The HTML, CSS, photograph, and icon returned HTTP 200 and matched the tested local files byte for byte.

The W3C Nu HTML validator reported no errors and two advisory warnings about explicit `list` roles on the ingredient and instruction lists. Those roles are retained intentionally: Safari can remove list semantics when `list-style: none` is applied. [MDN documents this accessibility behavior and the explicit role workaround](https://developer.mozilla.org/en-US/docs/Web/CSS/list-style#accessibility). This is a compatibility precaution, not a claim of a completed Safari test.
