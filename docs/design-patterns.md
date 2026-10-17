# Design patterns in the work

Reference: Jenifer Tidwell, Charles Brewer, and Aynne Valencia. *Designing Interfaces: Patterns for Effective Interaction Design*, third edition. O’Reilly Media, 2020. ISBN 9781492051961.

The page positions below refer to the supplied PDF viewer, counting its cover as page 1. They are not printed book pages. The explanations are applications of the reading to these projects, rather than claims that the book evaluated this work.

| Pattern | Reading location | Concrete application | Tradeoff or boundary |
| --- | --- | --- | --- |
| Progressive Disclosure | PDF page 365; also discussed in the behavioral patterns on PDF page 168 | The RSVP guest field appears after Going is selected. The layout study keeps its explanation inside a native disclosure. | Keep essentials visible. A hidden field still needs sensible state and validation when the choice changes. |
| Visual Framework | PDF page 372 | Repeated Grid/Flex cards share structure, spacing, type hierarchy, and metadata placement. | The pattern describes consistency across screens. Repeated cards apply the same consistency principle within a page; this is a smaller scope. |
| Dynamic Queries | PDF page 707 | The restaurant explorers combine standard search and filter controls and immediately update matching records. The library lab shares the same selection across views. | Immediate feedback is practical for eight records. A large remote dataset would need a different request and performance strategy. |
| Input Hints | PDF page 753 | The RSVP guest field places its numeric range beside the input. | Guidance must remain readable and should not replace a persistent label. |
| Good Defaults and Smart Prefills | PDF page 795 | Additional guests begin at zero. Optional draft saving and favorite persistence begin off. | Zero guests is a task default; opting out of persistence is a separate privacy choice. Neither assumes attendance. |
| Error Messages | PDF page 801 | Invalid guest counts produce inline correction guidance and block invalid downloads. The async directory explains failed loading and offers retry. | Request failures extend the reading's form-error principle. A useful retry must recover through the real loading path. |

## Reading register

All locations were checked against the supplied textbook copies. PDF page counts include front matter and differ from printed book pages. No textbook pages or PDFs are redistributed in this repository.

| Reference | Verified location | Use in this collection |
| --- | --- | --- |
| Jenifer Tidwell, Charles Brewer, and Aynne Valencia. *Designing Interfaces*, third edition. O’Reilly, 2020. | PDF pages 365, 372, 707, 753, 795, 801 | Conditional controls, coherent visual structure, immediate filtering, input guidance, defaults, and correction |
| Donald A. Norman. *The Design of Everyday Things*, supplied older paperback scan. | Mapping: printed page 23 / PDF page 37. Feedback: printed page 27 / PDF page 41. | Relationships between actions and results; visible selection, request status, and recovery feedback |
| Steve Krug. *Don't Make Me Think, Revisited*, third edition. | PDF page 47; pages 56–58 and 61–62 | Scanning, visual hierarchy, grouping, nesting, and reducing distraction |
| Stephanie Stimac. *Design for Developers*. | PDF page 465 and page 519 | Spacing as a relationship cue; semantic HTML and progressive enhancement |

The Norman copy is an older edition: its paperback preface is dated September 1989. References here use the mapping and feedback sections actually present in that copy, not page numbers or terminology assumed from the later revised edition. The case studies distinguish what the source does from interpretations supported by these readings.

## How the readings shape the presentation

The README leads with selected work, pairs each project with a concrete decision, and moves deeper theory into linked case studies. This applies Krug's hierarchy and scanning guidance to the review task. A restrained violet, slate, and blue visual system groups related material, while before-and-after and desktop/mobile compositions carry evidence rather than decorative imagery. Text links and prose carry the same meaning as the image labels.

The [visual system](visual-system.md) records the palette, type roles, artwork sources, and rendering procedure. The [full course map](course-map.md) includes all 16 supplied components; the [reading companion](reading-companion.md) provides new study synthesis for the discussion topics.

## Three decisions to explain in a review

**Why native HTML first?** The recipe's ingredient checklist is a form, so the browser can provide selection, labeling, keyboard input, and reset behavior. Its interaction still works with scripting disabled. This makes the document structure part of the solution rather than a wrapper around behavior.

**Why a shared selection model?** In the directory and library lab, changing a filter should redefine the same set of records everywhere. Independent filters per surface would make a chart, list, and map appear to disagree. Source records stay unchanged; derived arrays represent the current view.

**Why retain readable fallbacks?** A chart canvas, a map, or an entrance animation is only one representation of the content. Exact values, restaurant lists, and static cards keep the information available when a library fails. Reduced motion also changes whether animation is appropriate.

## Where the evidence stops

These are design rationales grounded in source behavior and the reading. They do not demonstrate improved task speed, reduced errors, or a measured user preference. Those claims would require a study. Browser automation checks selected behavior; keyboard checks and color calculations alone do not establish complete accessibility conformance.

## Inspect the implementations

- [RSVP behavior](../projects/04-rsvp-interaction/tutorial_4_files/script.js)
- [Grid and Flexbox styles](../projects/02-grid-and-flex/css/style.css)
- [Recipe structure](../projects/03-recipe-redesign/index.html)
- [Pure directory selection model](../projects/06-async-directory/tutorial_6_api/directory-model.js)
- [Chart data preparation](../projects/07-external-libraries/tutorial_7_external/chart-data.js)
