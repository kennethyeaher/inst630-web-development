# Companion verification

Reviewed locally and after publication on September 12, 2026. These checks cover
the original `companion/` extension. The course letter has its own
[verification report](verification.md).

## Results

| Check | Observed result |
| --- | --- |
| HTML | W3C Nu checker 26.9.9 returned no messages for the final public companion URL. |
| Local structure | One main landmark, one level-one heading, one invitation article, unique IDs, and no scripts. All relative file links and fragment targets resolve. |
| Responsive layout | At 320, 768, and 1280 CSS pixels, the document width matched the viewport without page-wide overflow. Mobile invitation, details, preparation steps, and design notes were visually inspected. Tablet layout was rechecked after moving the stacking breakpoint to 900px. |
| Skip navigation | The first Tab revealed the skip link. Enter moved focus to the invitation article. The visible Read the invitation link reached the same target. |
| Disclosures | Enter opened and closed a native design-note disclosure. The focused summary had a 3px blue outline with a 5px offset. |
| Color contrast | Calculated from the final CSS colors: body text on white 15.15:1; muted text on the page background 5.69:1; accent text on the tinted details panel 8.25:1; blue focus outline on the page background 7.30:1. These are specific color-pair checks, not a whole-site accessibility certification. |
| Printing | Safari Save as PDF produced one US Letter page at 100%, with browser headers, footers, and background printing off. The rendered page was visually inspected; the invitation, event details, all preparation steps, and closing were present with no visible clipping. |
| Deployment | [Pages run 34688472882](https://github.com/kennethyeaher/KY_htmlLab/actions/runs/34688472882) succeeded for application commit `9c77e67`. Both HTML pages, both stylesheets, the microscope, and the print preview returned HTTP 200 and matched local bytes. Browser inspection confirmed the companion stylesheet, a working keyboard disclosure, and navigation to the styled course letter with its loaded image. |
| Assignment preservation | The root HTML, supplied CSS, and microscope PNG retained the SHA-256 values recorded in the course verification report. |

[View the actual print preview](companion-print.png). The temporary PDF and
verification scripts are not repository dependencies.

## Why these choices matter

- An `article` keeps the invitation together; headings and a description list
  express its structure.
- A media query stacks the layout when two columns become cramped. It changes
  presentation while keeping the same reading order.
- Native `details` and `summary` provide disclosure behavior without scripting.
- `@media print` removes the surrounding page interface and adjusts spacing for
  paper. The invitation content remains in the HTML.

## Repeat the checks and cover the remaining limits

1. Open `companion/index.html` or serve the repository with VS Code Live Server.
2. Inspect the complete page at 320, 768, and 1280 pixels. Check the stylesheet
   request and applied rules in Developer Tools.
3. Reload and press Tab, then Enter, to reach the invitation. Navigate to each
   design-note summary and open and close it with the keyboard.
4. Use the browser's Print command with the settings above. Check that the
   invitation is complete and the surrounding navigation is absent.
5. Check actual 200% browser zoom and listen to the page with VoiceOver. These
   checks have not been completed; viewport resizing and an accessibility tree
   do not replace them.
6. Run the [W3C Nu checker](https://validator.w3.org/nu/) against the
   [live companion](https://kennethyeaher.github.io/KY_htmlLab/companion/) after
   future HTML changes. Local path and structure checks do not replace it.
7. After future deployments, verify the companion URL, CSS response, navigation
   back to the course letter, and the preview image.

Safari print output can differ from other browsers and paper settings. No
physical print, user study, cross-browser survey, or full accessibility audit
has been claimed.
