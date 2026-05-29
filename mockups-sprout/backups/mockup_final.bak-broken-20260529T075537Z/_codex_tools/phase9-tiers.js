const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const phase7Start = '/* === Wild Phase 7 - card polaroidization (added by apply-cards.js) === */';
const phase7End = '/* === end Wild Phase 7 - card polaroidization === */';
const phase9Start = '/* === Wild Phase 9 - tier system (added by phase9-tiers.js) === */';
const phase9End = '/* === end Wild Phase 9 - tier system === */';
const emojiRe = /🌱|🔥|💎|·/gu;

function countMarkers(text) {
  return (text.match(emojiRe) || []).length;
}

function removeBlock(html, startMarker, endMarker) {
  let next = html;
  while (true) {
    const start = next.indexOf(startMarker);
    if (start < 0) return next;
    const end = next.indexOf(endMarker, start);
    if (end < 0) throw new Error(`Found ${startMarker} without matching end marker`);
    next = next.slice(0, start) + next.slice(end + endMarker.length);
  }
}

function listPolaroid(selector) {
  return `
/* === Wild Phase 9 - Tier 1 hero polaroid: ${selector} === */
${selector} {
  background: var(--w-paper) !important;
  color: var(--w-ink) !important;
  border: none !important;
  border-radius: var(--r-lg) !important;
  padding: 20px 18px 22px !important;
  position: relative !important;
  overflow: visible !important;
  box-shadow:
    0 14px 28px -8px rgba(0,0,0,0.55),
    0 4px 8px rgba(0,0,0,0.3),
    inset 0 0 0 1px rgba(0,0,0,0.04) !important;
  transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1),
              box-shadow 0.25s !important;
}
${selector}:hover {
  transform: translateY(-6px) scale(1.015) !important;
  box-shadow:
    0 22px 44px -10px rgba(0,0,0,0.65),
    0 8px 16px rgba(0,0,0,0.35) !important;
}
${selector}::before {
  content: '' !important;
  position: absolute !important;
  top: -10px !important;
  left: 32% !important;
  transform: translateX(-50%) rotate(-3deg) !important;
  width: 80px !important;
  height: 18px !important;
  background: var(--w-tape-y) !important;
  box-shadow: inset 0 0 0 1px rgba(255,255,255,0.5) !important;
  z-index: 4 !important;
}
${selector}:nth-of-type(even)::before {
  background: var(--w-tape-p) !important;
  left: 60% !important;
  transform: translateX(-50%) rotate(4deg) !important;
}
${selector}:nth-of-type(3n)::before {
  background: var(--w-tape-g) !important;
}
${selector},
${selector} p,
${selector} span:not(.btn):not([class*='btn']):not([class*='badge']),
${selector} div:not([class*='btn']):not([class*='banner']):not([class*='avatar']):not([class*='hero']):not([class*='gradient']) {
  color: var(--w-ink) !important;
}
`;
}

function dataFrame(selector) {
  return `
/* === Wild Phase 9 - Tier 1 data-frame polaroid: ${selector} === */
${selector} {
  background: var(--w-paper) !important;
  color: var(--w-ink) !important;
  border: none !important;
  border-radius: var(--r-lg) !important;
  padding: 18px 16px 18px !important;
  position: relative !important;
  overflow: visible !important;
  box-shadow:
    0 14px 28px -8px rgba(0,0,0,0.55),
    0 4px 8px rgba(0,0,0,0.3) !important;
}
${selector}::before {
  content: '' !important;
  position: absolute !important;
  top: -10px !important;
  left: 30% !important;
  transform: translateX(-50%) rotate(-3deg) !important;
  width: 70px !important;
  height: 16px !important;
  background: var(--w-tape-y) !important;
  z-index: 4 !important;
}
${selector} > h2, ${selector} > h3,
${selector} > [class*='title'], ${selector} > [class*='label'] {
  color: var(--w-ink) !important;
  font-family: var(--font-disp-it) !important;
  font-style: italic !important;
}
${selector} canvas,
${selector} [class*='canvas'],
${selector} [class*='chart-body'],
${selector} [class*='reel-cell'],
${selector} [class*='reels-row'] {
  background: var(--surface-1) !important;
  color: var(--text-1) !important;
  border-radius: 10px !important;
  padding: 10px !important;
}
`;
}

function miniPolaroid(selector) {
  return `
/* === Wild Phase 9 - Tier 5 mini polaroid: ${selector} === */
${selector} {
  background: var(--w-paper) !important;
  color: var(--w-ink) !important;
  border: none !important;
  border-radius: var(--r-md) !important;
  padding: 14px 16px 16px !important;
  position: relative !important;
  overflow: visible !important;
  box-shadow:
    0 8px 18px -6px rgba(0,0,0,0.45),
    0 2px 4px rgba(0,0,0,0.25) !important;
  transition: transform 0.25s var(--ease) !important;
}
${selector}:hover { transform: translateY(-2px) !important; }
${selector}::before {
  content: '' !important;
  position: absolute !important;
  top: -6px !important;
  left: 30% !important;
  transform: translateX(-50%) rotate(-3deg) !important;
  width: 50px !important;
  height: 12px !important;
  background: var(--w-tape-y) !important;
  z-index: 4 !important;
}
${selector}:nth-of-type(even)::before {
  background: var(--w-tape-p) !important;
  left: 60% !important;
  transform: translateX(-50%) rotate(3deg) !important;
}
${selector},
${selector} > * {
  color: var(--w-ink) !important;
}
${selector} [class*='value'], ${selector} [class*='big'] {
  font-family: var(--font-mono) !important;
  font-weight: 700 !important;
  color: var(--w-ink) !important;
}
${selector} [class*='label'], ${selector} [class*='sub'] {
  color: var(--w-ink-2) !important;
}
${selector} canvas,
${selector} [class*='chart'],
${selector} [class*='canvas'] {
  background: var(--surface-1) !important;
  color: var(--text-1) !important;
  border-radius: 10px !important;
}
`;
}

function cleanFunctional(selectors) {
  return `
/* === Wild Phase 9 - Tier 2 clean functional card: ${selectors} === */
${selectors} {
  background: var(--surface-1) !important;
  color: var(--text-1) !important;
  border: 1px solid var(--border-1) !important;
  border-radius: var(--r-md) !important;
  padding: 16px !important;
  position: relative !important;
  transition: border-color 0.18s var(--ease), transform 0.18s var(--ease),
              box-shadow 0.18s var(--ease) !important;
  overflow: hidden !important;
  box-shadow: none !important;
}
${selectors}::before { content: none !important; }
${selectors}:hover {
  border-color: var(--sp-peach-400) !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 8px 20px -8px rgba(232,168,124,0.18) !important;
}
${selectors}::after {
  content: '' !important;
  position: absolute !important;
  left: 0; top: 14px; bottom: 14px;
  width: 3px !important;
  background: var(--sp-peach-400) !important;
  border-radius: 0 2px 2px 0 !important;
}
${selectors} [class*='name']:not([class*='sub']),
${selectors} [class*='title']:not([class*='sub']) {
  font-family: var(--font-disp-it) !important;
  font-style: italic !important;
  font-weight: 900 !important;
  color: var(--sp-peach-400) !important;
}
${selectors},
${selectors} p,
${selectors} span:not([class*='btn']):not([class*='badge']):not([class*='delta']) {
  color: var(--text-2) !important;
}
${selectors} [class*='value'], ${selectors} [class*='price'] {
  color: var(--text-1) !important;
  font-family: var(--font-mono) !important;
  font-weight: 700 !important;
}
${selectors} [class*='delta'], ${selectors} [class*='change'] {
  color: var(--sp-teal-400) !important;
  background: transparent !important;
  padding: 0 !important;
  font-family: var(--font-mono) !important;
  font-weight: 600 !important;
}
${selectors} [class*='down'], ${selectors} .negative {
  color: var(--sp-crimson) !important;
}
`;
}

function specDoc() {
  return `
/* === Wild Phase 9 - Tier 6 spec doc === */
body { background: var(--bg) !important; color: var(--text-1) !important; }
h1, h2 {
  font-family: var(--font-disp-it) !important;
  font-style: italic !important;
  font-weight: 900 !important;
  color: var(--sp-peach-400) !important;
}
h3 { color: var(--sp-peach-200) !important; font-weight: 700 !important; }
code, pre {
  background: var(--surface-2) !important;
  color: var(--sp-teal-300) !important;
  border-radius: 6px !important;
  padding: 2px 6px !important;
  font-family: var(--font-mono) !important;
}
table th { color: var(--sp-peach-400) !important; }
.arena-card {
  background: var(--surface-1) !important;
  color: var(--text-1) !important;
  border: 1px solid var(--border-1) !important;
  border-radius: var(--r-md) !important;
  padding: 16px !important;
  box-shadow: none !important;
}
.arena-card::before { content: none !important; }
`;
}

const tierCss = {
  'token_detail.html': [
    listPolaroid('.token-info-card'),
    listPolaroid('.trade-card'),
    listPolaroid('.trust-card'),
    dataFrame('.chart-card'),
    dataFrame('.tabs-card'),
  ].join(''),
  'clubs.html': cleanFunctional('.club-card, .pod-card'),
  'events.html': cleanFunctional('.ev-card'),
  'leaderboard.html': cleanFunctional('.lb-card-head'),
  'rewards.html': cleanFunctional('.history-card, .reels-card'),
  'points.html': cleanFunctional('.history-card, .rank-card'),
  'my_profile.html': [
    listPolaroid('.profile-hero'),
    listPolaroid('.section-card:first-of-type'),
    cleanFunctional('.section-card:not(:first-of-type), .stat-card'),
  ].join(''),
  'public_profile.html': [
    listPolaroid('.profile-hero'),
    listPolaroid('.section-card:first-of-type'),
    cleanFunctional('.section-card:not(:first-of-type), .stat-card'),
  ].join(''),
  'referrals.html': [
    listPolaroid('.link-card'),
    cleanFunctional('.stat-card, .table-card'),
  ].join(''),
  'edit_profile_privacy.html': [
    listPolaroid('.edit-card:first-of-type'),
    cleanFunctional('.edit-card:not(:first-of-type)'),
  ].join(''),
  'creator_dashboard.html': [
    miniPolaroid('.metric-card'),
    miniPolaroid('.stat-card'),
  ].join(''),
  'FR-012_TokenWar.html': specDoc(),
  'FR-012b_TokenWar_PredictionMarket.html': specDoc(),
};

const files = fs.readdirSync(root).filter((file) => file.endsWith('.html'));

for (const file of files) {
  const fp = path.join(root, file);
  let html = fs.readFileSync(fp, 'utf8');
  const before = countMarkers(html);
  html = removeBlock(html, phase7Start, phase7End);
  html = removeBlock(html, phase9Start, phase9End);

  if (tierCss[file]) {
    const idx = html.lastIndexOf('</style>');
    if (idx < 0) throw new Error(`No </style> found in ${file}`);
    const injection = `\n${phase9Start}\n${tierCss[file]}${phase9End}\n`;
    html = html.slice(0, idx) + injection + html.slice(idx);
  }

  fs.writeFileSync(fp, html, 'utf8');
  const verify = fs.readFileSync(fp, 'utf8');
  const after = countMarkers(verify);
  if (after < before) {
    throw new Error(`${file}: emoji/domain marker count regressed ${before} -> ${after}`);
  }
  const action = tierCss[file] ? 'tier CSS injected' : 'Phase 7 removed/none';
  console.log(`${file}: ${action} | markers ${before}->${after}`);
}
