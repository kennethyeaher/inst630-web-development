/** Render the collection's presentation artboards using the RSVP project's locked Playwright dependency. */
const { chromium } = require('../projects/04-rsvp-interaction/node_modules/playwright');
const { pathToFileURL } = require('node:url');
const path = require('node:path');
const root = path.resolve(__dirname, '..');

/** Export each fixed artboard after local images and fonts are ready; fail if an image is missing. */
async function renderShowcase() {
  const browser = await chromium.launch({ channel: process.env.BROWSER_CHANNEL || undefined });
  try {
    const page = await browser.newPage({ viewport: { width: 1480, height: 1100 }, deviceScaleFactor: 2 });
    await page.goto(pathToFileURL(path.join(root, 'docs/showcase.html')).href);
    await page.evaluate(async () => { await document.fonts.ready; await Promise.all([...document.images].map(image => image.decode())); });
    for (const id of ['cover', 'cover-mobile', 'library', 'rsvp', 'recipe', 'atlas', 'data-flow']) {
      await page.locator(`#${id}`).screenshot({ path: path.join(root, `docs/assets/${id}.png`) });
    }
    console.log('Rendered seven presentation artboards.');
  } finally {
    await browser.close();
  }
}
renderShowcase().catch(error => { console.error(error); process.exitCode = 1; });
