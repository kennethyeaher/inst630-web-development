# Reading companion

New study synthesis for the course topics. These notes connect the available source code with the supplied textbooks; they are not the original submitted responses or a reconstruction of the instructor's reading prompts. Full references and PDF page locations appear in [design patterns](design-patterns.md#reading-register).

## HTML history

**The connection:** HTML began as a document language and developed alongside the browser platform into a language for documents and applications. The HTML Standard's [background and history](https://html.spec.whatwg.org/multipage/introduction.html#history-2) describes the early CERN/IETF period, later W3C work, the WHATWG effort, and the 2019 agreement to collaborate on one version of HTML.

**Why it matters here:** the course begins with a letter and later adds behavior, data loading, and external libraries. The richer interface still depends on document structure, links, forms, and a meaningful reading order. Adding a script does not remove those responsibilities.

**Practice:** distinguish HTML, CSS, JavaScript, the DOM, and HTTP in the restaurant directory. Which describes meaning, which controls presentation, which changes behavior, which represents the document in memory, and which carries the JSON request?

## Reading 1: HTML

**The connection:** structure is an interface decision. In [Correspondence](../projects/01-semantic-html/companion/index.html), headings introduce content, paragraphs establish reading order, and a native disclosure keeps optional notes available. In Stimac's discussion of progressive enhancement (PDF page 519), semantic HTML provides the baseline when richer resources fail.

**Inspect:** disable styles and read the invitation. The hierarchy should still be understandable even though the two-column composition is gone. This is a useful check, not a full accessibility audit.

**Practice:** explain why a large styled paragraph is not interchangeable with a heading, and why an interactive action needs an appropriate native control.

## Reading 2: Grids and Flexboxes

**The connection:** layout should make relationships visible. Krug's visual hierarchy discussion (PDF pages 56–58) connects prominence, grouping, and nesting to how a page is understood. The [layout study](../projects/02-grid-and-flex/css/style.css) uses Grid for page regions and Flexbox for the smaller groups inside each card.

**Inspect:** compare the row above 64rem with the stack at or below it. The arrangement changes, but each card keeps its image, metadata, content, and sample discussion together.

**Practice:** explain when a two-dimensional layout benefits from Grid, when a one-dimensional group benefits from Flexbox, and how gap differs from margin and padding. Test an awkward width near the breakpoint rather than only a preset phone size.

## Reading 3: Designing a readable page

The exact title of Reading Assignment 3 was not supplied. This companion connects the adjacent recipe redesign to the available visual-design readings.

**The connection:** visual emphasis should match the task. Krug (PDF pages 56–58, 61–62) discusses hierarchy and noise. Stimac (PDF page 465) explains how spacing signals relationships. In the [recipe](../projects/03-recipe-redesign/index.html), planning information, ingredients, and ordered instructions have distinct roles.

**Inspect:** compare the [before-and-after case study](case-studies.md#recipe-redesign). Then inspect the native ingredient form. The redesign uses layout and structure as well as color.

**Practice:** identify one element that deserves greater prominence, one grouping that helps scanning, and one decoration that could be removed without weakening the cooking task. Describe a change you can observe instead of claiming faster performance without a study.

## Reading 4: JavaScript intro

**The connection:** state should have a visible result. Norman's feedback principle (printed page 27; PDF page 41) concerns information about an action and its result. The [RSVP script](../projects/04-rsvp-interaction/tutorial_4_files/script.js) updates button state, guest visibility, confirmation, and the response summary together.

**Inspect:** a text input starts as a string. Converting a guest count to a number is separate from validating a whole-number range. `textContent` displays an entered name as text. `aria-pressed` communicates the selected response through more than color.

**Practice:** trace the booleans after Going, Can't make it, and Reset. Explain what happens if the guest field contains an invalid value when the person switches to declining.

## Reading 5: Arrays and objects

**The connection:** a data method should fit the question. The [array exercise](../projects/05-array-methods/tutorial_5_arrays/script.js) demonstrates actions with `forEach`, subsets with `filter`, transformed output with `map`, and a first match with `find`. The later explorers use these ideas to support Dynamic Queries (*Designing Interfaces*, PDF page 707).

**Inspect:** compare a restaurant record with the array containing all records. Describe each method's return shape, and distinguish an empty result array from an undefined first match. In the [pure directory model](../projects/06-async-directory/tutorial_6_api/directory-model.js), filtering produces an array that can be sorted without reordering the original source.

**Practice:** predict the output for zero matches, two matches, and a missing lookup. Explain why `forEach` is not a replacement for `map` when you need a transformed array.

## Reading 6: Async/Await

**The connection:** a request creates several interface states. The [directory loader](../projects/06-async-directory/tutorial_6_api/script.js) distinguishes pending work, successful data, an empty result, and failure. Norman's feedback principle supports making those distinctions visible. *Designing Interfaces*' Error Messages pattern (PDF page 801) supports useful guidance near the problem; applying that form pattern to a request failure is a design extension.

**Inspect:** `await fetch()` does not make every HTTP status successful. The code checks status, parses JSON, validates the records, and renders only usable data. Cleanup in `finally` is separate from deciding whether browsing should be enabled.

**Practice:** explain what happens for a 404 response, malformed JSON, valid JSON with the wrong shape, and an empty array. Follow Retry through the real loading function.

## Reading 7: External libraries

**The connection:** a library is a representation choice with dependencies and failure modes. The [library lab](../projects/07-external-libraries/tutorial_7_external/script.js) uses a shared filtered collection for charts, a map, and cards. Text alternatives preserve information when a library fails, applying Stimac's progressive-enhancement reasoning (PDF page 519) within the JavaScript application.

**Inspect:** the exact-value table, restaurant list, and static cards survive the loss of their presentation library. The application itself still requires JavaScript; these fallbacks do not mean the entire data explorer works with scripting disabled. The map positions are illustrative because the course data has no coordinates.

**Practice:** identify the data each library requires, its visible failure state, and a nonvisual route to the same information. Explain why repeated chart or animation actions should replace or cancel previous work instead of accumulating it.

## Turn a note into a response

Use one concrete implementation, explain the user problem it addresses, connect it to a reading concept, then identify a question or limitation. Add your own reaction and course-specific evidence before using these notes in an assignment. They are study material, not a substitute for an original submitted reflection.
