# Verification record

Collection assembled October 17, 2026. The seven applications are committed-source snapshots, not newly rewritten assignments. Older verification records inside the project folders retain their original dates and scope.

## Collection checks

| Check | Result | Scope |
| --- | --- | --- |
| Snapshot integrity | PASS | Seven recorded revisions; 115 copied files checked by SHA-256 against `catalog.json` |
| JavaScript syntax | PASS | Every copied JavaScript source and test file parsed with Node |
| Collection documentation targets | PASS | Relative file and image targets in the root README, project index, and new docs resolve |
| Original demo links | PASS | All seven linked demo URLs returned HTTP 200 on October 17, 2026; this is availability, not a fresh behavior test of the hosted copies |
| README visual review | PASS | A local Markdown rendering reviewed in Chrome at 1280px and 390px, with all 13 images loaded; GitHub's own rendering remains a separate check |
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

Total: 81 passing tests across the existing suites, zero failures and zero skipped tests. The snapshot validator also passed for all 115 copied files and 70 local documentation targets. The same checks are configured in the root GitHub Actions workflow; hosted results are independent of this local run.

The [hosted run at `80d89d8`](https://github.com/kennethyeaher/inst630-web-development/actions/runs/39003956612) passed all five jobs: collection integrity plus all four project checks and test suites. This used Chromium on Ubuntu 24.04 with Node.js 24. A clean temporary clone also passed collection validation. A pattern scan of reachable source and commit text found no credential patterns or unwanted tool attribution. Pattern scanning is a limited check, not a guarantee that every possible secret format is detected.

## Repeat the checks

Use Python 3 and Node.js 24 or newer. From the collection root:

```sh
python3 scripts/check_collection.py
python3 scripts/run_checks.py --install
```

The runner uses `npm ci --ignore-scripts` in each of the four JavaScript folders, followed by its existing `npm run check` and `npm test`. It installs Playwright Chromium unless `BROWSER_CHANNEL` selects an installed browser. On Linux, system libraries may be needed; the CI workflow uses `npx playwright install --with-deps chromium` for that setup.

The first three projects are static HTML/CSS. They have preserved historical verification notes; no new claim of complete browser coverage is made for those projects. No extra test cases were invented to increase a test count.

## Limits

The README images were captured in earlier project work and are labeled as such. The collection visual review uses a local Markdown renderer, which approximates GitHub styling. Full manual accessibility review, VoiceOver, Safari, Firefox, physical devices, physical printing, usability studies, and production load testing were not performed for this collection. Existing tests that check keyboard behavior or color settings cover those selected cases only.

External library browser tests require working CDNs and map services for their normal-path scenarios. Their blocked-resource tests exercise fallbacks. Sample restaurant data is unchanged, map coordinates are illustrative, and no live restaurant API is claimed.
