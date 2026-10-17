# Midterm practice through the projects

Use this as source-based practice alongside the course slides and exam instructions. The [full course map](course-map.md) covers all 16 listed components; the [reading companion](reading-companion.md) connects the discussion topics with the available textbooks. It covers the collected exercises, not a confirmed list of exam topics. Try each prompt before opening its answer check.

## 1. Structure before style

Open [the letter](../projects/01-semantic-html/index.html) and [the original companion](../projects/01-semantic-html/companion/index.html). Explain how headings, paragraphs, lists, dates, and landmarks communicate meaning. Which choices would still matter without CSS?

<details><summary>Answer check</summary>

HTML communicates relationships and document order. Headings organize sections; lists group related items; a time element can provide a machine-readable date. A landmark helps navigation. A class name only supplies a hook unless behavior or styling gives it another role. Visual size alone does not create a semantic heading.

</details>

## 2. Grid, Flexbox, and the box model

Open [the layout stylesheet](../projects/02-grid-and-flex/css/style.css). Identify one page-level Grid responsibility and one Flexbox responsibility inside a card. Predict the layout immediately above and below 64rem. Explain how padding differs from margin and gap.

<details><summary>Answer check</summary>

Grid assigns page regions and shared columns; Flexbox aligns groups within regions. The cards form a row above 64rem and stack at or below it. At the default 16px root size, 64rem is 1024px. Padding is inside a border, margin is outside, and gap separates items in a layout container. With border-box, declared width includes padding and border. Test content and enlarged text as well as viewport width.

</details>

## 3. Native behavior and responsive order

Inspect [the recipe HTML](../projects/03-recipe-redesign/index.html) and [styles](../projects/03-recipe-redesign/style.css). How can the ingredient checklist reset without JavaScript? Why should document order remain sensible when the two-column layout becomes one column?

<details><summary>Answer check</summary>

Native checkboxes hold their own checked state and a form reset control restores their defaults. Associated labels provide names and larger activation areas. CSS can change spatial placement, but reading and keyboard order still depend heavily on document structure. The print stylesheet is a separate presentation of the same content.

</details>

## 4. DOM events, values, and state

Inspect [the RSVP script](../projects/04-rsvp-interaction/tutorial_4_files/script.js). Trace what happens after choosing Going, typing a name, entering 1.5 guests, then choosing Can't make it. Explain the roles of boolean, string, and number values. Why use textContent for the name?

<details><summary>Answer check</summary>

An event changes the response state, then rendering updates controls and messages. Input values begin as strings; numeric conversion alone does not establish that a value is an allowed whole number. Invalid guest counts block an attending confirmation and download. A declining response does not need a valid guest count. textContent displays a supplied name as literal text instead of interpreting markup.

</details>

## 5. Choose the array method

In [the array exercise](../projects/05-array-methods/tutorial_5_arrays/script.js), find a case for each method. Predict the return shape before reading the implementation: forEach, filter, map, find. Why copy an array before sorting it?

<details><summary>Answer check</summary>

forEach performs work for each item and returns undefined. filter returns an array containing every match. map returns a transformed array with one result per item. find returns the first match or undefined. sort mutates the array it acts on, so sorting a copy protects the original order. A missing match and an empty result list require different checks.

</details>

## 6. Follow a request through failure

Open [the async script](../projects/06-async-directory/tutorial_6_api/script.js). Explain the sequence from clicking Load restaurants to enabled browsing. Why check response.ok if fetch already uses try/catch? What belongs in finally?

<details><summary>Answer check</summary>

Disable dependent actions, request the JSON, check the HTTP status, parse it, validate its shape, then render and enable appropriate actions. fetch can resolve successfully for an HTTP error such as 404; response.ok catches that distinction. Parsing can fail, and valid JSON can still have an invalid schema. finally clears request cleanup such as a timeout and restores request controls. It should not enable browsing after failed validation.

</details>

## 7. Integrate libraries without losing the content

Inspect [chart preparation](../projects/07-external-libraries/tutorial_7_external/chart-data.js) and [integration](../projects/07-external-libraries/tutorial_7_external/script.js). What changes when Chart.js, Leaflet, or GSAP is unavailable? Why do all cuisine bars initially have equal height? Are map coordinates source data?

<details><summary>Answer check</summary>

The exact-value table, filtered restaurant list, and static cards remain useful representations. The eight-record fixture has one record per cuisine, so each original cuisine count is one. Illustrative map positions are derived because the source has no coordinates; they must not be presented as real restaurant locations. Replaying animation should cancel obsolete work. Reduced-motion preferences should preserve visible content.

</details>

## 8. Connect behavior to a design pattern

Choose an example of Progressive Disclosure, Dynamic Queries, or Error Messages from [the pattern notes](design-patterns.md). Explain the user problem, the implemented behavior, one tradeoff, and a test that could fail. Avoid claiming an improvement that has not been measured.

<details><summary>Answer check</summary>

For example: guest input is irrelevant until someone attends, so reveal it after Going. The tradeoff is managing its state when someone switches to declining. A behavior test can enter an invalid guest value, switch responses, and check that a valid decline is still downloadable. This verifies a rule; a usability study would be needed to establish whether people complete the task more easily.

</details>

## Final practice pass

Run one project, predict a visible change, trace the event or CSS rule, then explain the result aloud without reading the code. Repeat with an empty result, an invalid value, and a failed request. Use the [verification record](verification.md) to distinguish source checks, browser tests, and manual checks.
