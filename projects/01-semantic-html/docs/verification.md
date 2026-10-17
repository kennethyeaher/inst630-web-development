# Letter verification

Reviewed on September 12, 2026 against commit `e2dfd1f`. These results describe
specific checks, not a full accessibility certification.

## Results

| Check | Result and evidence |
| --- | --- |
| HTML conformance | W3C Nu checker version 26.9.9 returned an empty messages list for the live letter. |
| Content preservation | Body text matched the supplied letter after normalizing whitespace. |
| Classes | All 26 supplied class names were present, with no undefined classes. Major elements carried classes; list items matched descendant selectors. |
| Applied styles | Browser inspection reported subject color `rgb(44, 90, 160)` and sender alignment `right`. The supplied stylesheet loaded with 29 top-level rules. |
| Image | Browser reported `complete: true`, natural width 90, and natural height 112. |
| Narrow layout | At 320 CSS pixels, document width was 320 with no page overflow. The mobile rule reduced main padding to 16px and subject text to 20.8px. The top of the page was visually reviewed. |
| Tablet layout | At 768 CSS pixels, document width was 768 with no page overflow. |
| Desktop layout | At 1280 CSS pixels, document width was 1280 with no page overflow. Earlier Safari screenshots also show the styled letter through its closing. |
| Keyboard focus | Tab reached the email link; its computed outline was solid yellow, 2px wide, with a 2px offset. The mail application was not opened. |
| Browser semantics | The accessibility tree exposed one level-one heading, three level-two headings, lists, and the image description. This is not a VoiceOver listening test. |
| Deployment | Rechecked on September 12 after publishing the companion: the letter HTML, CSS, and PNG each returned HTTP 200 and matched local bytes. Browser inspection confirmed the blue subject heading and loaded 90 by 112 pixel image. |

## Limits and observations

- The supplied yellow focus outline has approximately 1.6:1 contrast against the
  light sender panel. Its presence is verified; that does not establish adequate
  focus contrast. The assignment stylesheet has been preserved.
- Browser zoom shortcuts did not change the observed viewport, so a real 200%
  zoom check remains unverified. Narrow viewport checks do not replace it.
- VoiceOver reading and heading navigation remain untested.
- Only the supplied email address is linked. University dates and dance research
  have no supplied destinations; the letter retains their text without inventing URLs.

## Repeat the checks

1. Open the [live letter](https://kennethyeaher.github.io/KY_htmlLab/) in Safari.
2. Open Web Inspector, select Network, and reload. Inspect the CSS and PNG requests.
3. Inspect the subject heading under Elements and find the `.letter-subject`
   rule. Inspect the greeting and confirm both of its class rules contribute.
4. Tab to the email link and check its focus indicator without activating it.
5. Test browser widths of 320, 768, and 1280 pixels; inspect the whole letter for
   clipping. Use actual browser zoom at 200% as a separate check.
6. With VoiceOver, read the page and navigate its headings. Confirm the order,
   image description, and lists make sense when heard.
7. Run the [W3C HTML checker](https://validator.w3.org/nu/) against the live URL.

## Preserved submission files

SHA-256 values before the portfolio extension:

```text
0363a72c8287aa23bf9985d9be264448ccb8efdc479861d55699faf52aa52445  index.html
ad4b9193ea860a64133ac0141de94a92f27d71324cd8b70ea60f7d0c30d72e1b  tutorial_1_letter_styles.css
4a626d379634f98ed4a4b6f75dbbd64754e8e70b546be60b2ca35d1ab01cec12  microscope.png
```
