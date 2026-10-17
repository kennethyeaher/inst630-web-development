# Visual system and artwork

## Direction

The project is named **INST360MSC**: a midsemester checkpoint for **Programming Human-Centered Interfaces**. The cover names the project directly and frames the work as applying the first half of the course.

The collection uses interface specimens: actual project screens arranged to show an implementation decision. The cover introduces the body of work, the atlas shows course progression, and each featured plate answers a different review question. The recipe compares before and after; RSVP compares desktop and mobile; the library lab compares representations of the same data.

## Tokens

| Role | Value | Purpose |
| --- | --- | --- |
| Ink | `#242439` | Main headings and reading contrast |
| Slate | `#56576b` | Supporting text |
| Violet paper | `#eeedf5` | Shared cover and architecture ground |
| Neutral paper | `#f6f7fb` | Project comparison ground |
| Blue | `#3757c8` | Recipe comparison emphasis |
| Violet label | `#625879` | Course and section identification |

Baskerville with Georgia fallback provides the large display role; Avenir Next with Arial fallback supplies labels and supporting text. The exported PNGs retain the actual rendering and do not depend on those fonts being installed on a reader's machine. The README body uses GitHub's native typography.

The desktop cover is 1400 × 640 CSS pixels; a dedicated 720 × 980 version keeps the heading readable in narrow layouts. Project plates use a common 1400px width with heights appropriate to their evidence. Images export at twice their CSS dimensions. Original screenshot files remain unchanged; cropped excerpts are explicitly presented as excerpts in the artwork and source notes.

## Reproduce the assets

The layout source is [showcase.html](showcase.html). It is an artwork source file, not a claim of a hosted portfolio site. It uses local screenshots only, without external fonts or network resources.

Install the existing RSVP project's locked development packages if needed, then run from the collection root:

```sh
cd projects/04-rsvp-interaction
npm ci --ignore-scripts
npx playwright install chromium
cd ../..
node scripts/render_showcase.cjs
```

Use `BROWSER_CHANNEL=chrome node scripts/render_showcase.cjs` to render in installed Chrome. Font fallback can change typography on other systems, so inspect new exports before committing. The renderer stops when an image cannot decode.

## Evidence and reading

The cover and plates use earlier browser screenshots from the seven imported projects. They are presentation compositions, not newly captured application states. No textbook imagery is used. The diagram is a source-backed explanation of the existing shared-filter model. All substantive labels have prose equivalents in the README or case studies.

Krug's hierarchy and noise discussion, Stimac's spacing discussion, and *Designing Interfaces*' Visual Framework pattern support the composition choices. See the [reading register](design-patterns.md#reading-register) for verified locations. The design is a reasoned presentation choice, not a measured improvement in recruiter behavior.
