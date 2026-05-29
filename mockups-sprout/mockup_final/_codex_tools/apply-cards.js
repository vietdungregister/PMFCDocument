const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const markerStart = '/* === Wild Phase 7 - card polaroidization (added by apply-cards.js) === */';
const markerEnd = '/* === end Wild Phase 7 - card polaroidization === */';
const emojiRe = /🌱|🔥|💎|·|\uE076|\uE068|\uE066|\uE06B|\uFF82\uFF77|笨ｨ|験|櫨|虫|噫|国|遂/g;

const PAGES = {
  'FR-012_TokenWar.html': [['.arena-card', 'list_card']],
  'clubs.html': [['.club-card', 'list_card'], ['.pod-card', 'data_frame']],
  'events.html': [['.ev-card', 'list_card']],
  'creator_dashboard.html': [['.metric-card', 'stat_card'], ['.stat-card', 'stat_card']],
  'my_profile.html': [['.section-card', 'list_card'], ['.stat-card', 'stat_card']],
  'public_profile.html': [['.section-card', 'list_card'], ['.stat-card', 'stat_card']],
  'token_detail.html': [
    ['.token-info-card', 'list_card'],
    ['.trade-card', 'list_card'],
    ['.chart-card', 'data_frame'],
    ['.tabs-card', 'data_frame'],
    ['.trust-card', 'list_card'],
  ],
  'referrals.html': [['.link-card', 'list_card'], ['.stat-card', 'stat_card'], ['.table-card', 'table_card']],
  'rewards.html': [['.history-card', 'table_card'], ['.reels-card', 'data_frame']],
  'points.html': [['.history-card', 'table_card'], ['.rank-card', 'stat_card']],
  'leaderboard.html': [['.lb-card-head', 'data_frame']],
  'edit_profile_privacy.html': [['.edit-card', 'list_card']],
};

function listCard(selector) {
  return `
/* === Wild list-card polaroid: ${selector} === */
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

function statCard(selector) {
  return `
/* === Wild stat-card mini polaroid: ${selector} === */
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
`;
}

function dataFrame(selector) {
  return `
/* === Wild data-frame polaroid: ${selector} === */
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

function tableCard(selector) {
  return `
/* === Wild table-card flat dark trim: ${selector} === */
${selector} {
  background: var(--surface-1) !important;
  border: 1px solid var(--border-1) !important;
  border-radius: var(--r-lg) !important;
  padding: 18px !important;
  color: var(--text-1) !important;
}
${selector} > [class*='title'], ${selector} > h2, ${selector} > h3 {
  font-family: var(--font-disp-it) !important;
  font-style: italic !important;
  color: var(--sp-peach-400) !important;
}
${selector} table { color: var(--text-1) !important; }
${selector} th { color: var(--sp-peach-400) !important; }
`;
}

const RECIPES = {
  list_card: listCard,
  stat_card: statCard,
  data_frame: dataFrame,
  table_card: tableCard,
};

function countEmojiDomain(text) {
  return (text.match(emojiRe) || []).length;
}

for (const [file, rules] of Object.entries(PAGES)) {
  const fp = path.join(root, file);
  let html = fs.readFileSync(fp, 'utf8');
  const beforeCount = countEmojiDomain(html);

  const oldStart = html.indexOf(markerStart);
  if (oldStart >= 0) {
    const oldEnd = html.indexOf(markerEnd, oldStart);
    if (oldEnd >= 0) {
      html = html.slice(0, oldStart) + html.slice(oldEnd + markerEnd.length);
    }
  }

  let css = `\n${markerStart}\n`;
  for (const [selector, recipeKey] of rules) {
    css += RECIPES[recipeKey](selector);
  }
  css += `${markerEnd}\n`;

  const idx = html.lastIndexOf('</style>');
  if (idx < 0) {
    console.error(`No </style> found in ${file}`);
    process.exitCode = 1;
    continue;
  }

  html = html.slice(0, idx) + css + html.slice(idx);
  fs.writeFileSync(fp, html, 'utf8');

  const verify = fs.readFileSync(fp, 'utf8');
  const afterCount = countEmojiDomain(verify);
  if (afterCount < beforeCount) {
    console.error(`${file}: emoji/domain count regressed ${beforeCount} -> ${afterCount}`);
    process.exit(1);
  }
  console.log(`${file}: ${rules.map(([selector, recipe]) => `${selector}:${recipe}`).join(', ')} | emoji/domain ${beforeCount}->${afterCount}`);
}
