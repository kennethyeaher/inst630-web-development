# Verification record

Collection assembled October 17, 2026. The seven applications are committed-source snapshots, not newly rewritten assignments. Older verification records inside the project folders retain their original dates and scope.

## Collection checks

| Check | Result | Scope |
| --- | --- | --- |
| Snapshot integrity | PASS | Seven recorded revisions; 115 copied files checked by SHA-256 against `catalog.json` |
| JavaScript syntax | PASS | Every copied JavaScript source and test file parsed with Node |
| Collection documentation targets | PASS | 167 local file, image, and heading-fragment targets resolve, including responsive image sources and presentation source files |
| Original demo links | PASS | All seven linked demo URLs returned HTTP 200 on October 17, 2026; this is availability, not a fresh behavior test of the hosted copies |
| README visual review | PASS | GitHub-processed Markdown reviewed locally in Chrome at 1280px and 390px; all eight displayed images loaded, the responsive cover switched correctly, and neither viewport had horizontal page overflow |
| Browser and model suites | See results below | Fresh runs against the copied projects, using each original suite |

The source snapshots omit original root workflows and a separate supplied answer file, as listed in the catalog. They exclude untracked local files and installed packages. Original repositories were not edited.

## Fresh project results

Fresh runs used Node.js 26.10.0, Python 3.14.7, and installed Chrome on macOS. All four lockfile installs succeeded and each npm audit summary reported zero vulnerabilities at installation time.

| Project | Project check | Tests | Result |
| --- | --- | --- | --- |
| RSVP | JavaScript and test syntax | 10 browser tests | PASS |
| Array methods | JavaScript syntax and Prettier | 16 browser tests | PASS |
| Async directory | ESLint, Prettier, script syntax | 6 model tests and 26 browser tests | PASS |
| External libraries | JavaScript syntax and 3 data/model tests | 20 browser tests | PASS |

Total: 81 passing tests across the existing suites, zero failures and zero skipped tests. At initial assembly, the snapshot validator passed for all 115 copied files and 70 local documentation targets. The expanded course presentation now checks 167 local targets. The same checks are configured in the root GitHub Actions workflow; hosted results are independent of this local run.

The [hosted run at `80d89d8`](https://github.com/kennethyeaher/inst630-web-development/actions/runs/39003956612) passed all five jobs: collection integrity plus all four project checks and test suites. This used Chromium on Ubuntu 24.04 with Node.js 24. A clean temporary clone also passed collection validation. A pattern scan of reachable source and commit text found no credential patterns or unwanted tool attribution. Pattern scanning is a limited check, not a guarantee that every possible secret format is detected.

## Repeat the checks

Use Python 3 and Node.js 24 or newer. From the collection root:

```sh
python3 scripts/check_collection.py
python3 scripts/run_checks.py --install
```

The runner uses `npm ci --ignore-scripts` in each of the four JavaScript folders, followed by its existing `npm run check` and `npm test`. It installs Playwright Chromium unless `BROWSER_CHANNEL` selects an installed browser. On Linux, system libraries may be needed; the CI workflow uses `npx playwright install --with-deps chromium` for that setup.

The first three projects are static HTML/CSS. They have preserved historical verification notes; no new claim of complete browser coverage is made for those projects. No extra test cases were invented to increase a test count.

## Expanded course presentation

The current presentation pass adds seven exported artboards, a dedicated mobile cover, three source-backed case studies, and a map of all 16 supplied course components. All 115 copied project files still match their original hashes. Application source and project tests are unchanged by this presentation pass.

The textbook locations were checked in the supplied copies. Norman's older scan required page inspection; its mapping and feedback references use printed pages 23 and 27 (PDF pages 37 and 41). No textbook pages are committed. Original reading and HTML History submissions were not supplied, so new companions are labeled as study synthesis.

The renderer completed with every local screenshot decoded. The GitHub Markdown API preserved the picture/source markup. The local desktop/mobile review confirmed that the correct cover file was selected at each width. A live GitHub page review is a separate final publishing check.

## Limits

The README images were captured in earlier project work and are labeled as such. The collection visual review uses a local Markdown renderer, which approximates GitHub styling. Full manual accessibility review, VoiceOver, Safari, Firefox, physical devices, physical printing, usability studies, and production load testing were not performed for this collection. Existing tests that check keyboard behavior or color settings cover those selected cases only.

External library browser tests require working CDNs and map services for their normal-path scenarios. Their blocked-resource tests exercise fallbacks. Sample restaurant data is unchanged, map coordinates are illustrative, and no live restaurant API is claimed.
