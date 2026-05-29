const fs = require('fs');
const path = require('path');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));
const screenshotDir = path.join('.', '_codex_screenshots');
fs.mkdirSync(screenshotDir, { recursive: true });
const delay = ms => new Promise(resolve => setTimeout(resolve, ms));

function findChrome() {
  const candidates = [
    process.env.PUPPETEER_EXECUTABLE_PATH,
    'C:/Program Files/Google/Chrome/Application/chrome.exe',
    'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe',
    'C:/Program Files/Microsoft/Edge/Application/msedge.exe',
    'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
  ].filter(Boolean);
  return candidates.find(p => fs.existsSync(p));
}

(async () => {
  let puppeteer;
  try {
    puppeteer = await import('puppeteer-core');
  } catch (err) {
    console.error('Puppeteer unavailable: ' + err.message);
    process.exit(2);
  }
  const executablePath = findChrome();
  if (!executablePath) {
    console.error('No Chromium/Chrome/Edge executable found.');
    process.exit(3);
  }
  const browser = await puppeteer.launch({
    headless: true,
    executablePath,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage']
  });
  const results = [];
  for (const file of files) {
    const page = await browser.newPage();
    const errors = [];
    page.on('pageerror', e => errors.push(e.message));
    page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
    await page.setViewport({ width: 1440, height: 900 });
    await page.goto('file://' + path.resolve(file), { waitUntil: 'load', timeout: 30000 });
    await delay(800);
    await page.screenshot({ path: path.join(screenshotDir, file.replace('.html', '_desktop.png')), fullPage: true });
    await page.setViewport({ width: 390, height: 844, deviceScaleFactor: 2 });
    await delay(400);
    await page.screenshot({ path: path.join(screenshotDir, file.replace('.html', '_mobile.png')), fullPage: true });
    results.push({ file, errors });
    console.log(file + ': ' + (errors.length ? 'ERRORS: ' + errors.join('; ') : 'OK'));
    await page.close();
  }
  await browser.close();
  fs.writeFileSync(path.join(screenshotDir, 'verify-results.json'), JSON.stringify(results, null, 2));
})();
