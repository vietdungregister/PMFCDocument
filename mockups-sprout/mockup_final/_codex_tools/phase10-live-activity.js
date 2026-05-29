const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const anchorPath = path.join(root, 'token_list_v4.html');
const detailPath = path.join(root, 'token_detail.html');
const startMarker = '<!-- ╔══════ v0.7 LIVE ACTIVITY right panel ══════╗ -->';
const endMarker = '<!-- ╚══════ end LIVE ACTIVITY ══════╝ -->';
const emojiRe = /🌱|🔥|💎|·/gu;

function countMarkers(text) {
  return (text.match(emojiRe) || []).length;
}

function removeExistingLa(html) {
  let next = html;
  while (true) {
    const start = next.indexOf(startMarker);
    if (start < 0) return next;
    const end = next.indexOf(endMarker, start);
    if (end < 0) throw new Error('Existing Live Activity start marker without end marker');
    next = next.slice(0, start) + next.slice(end + endMarker.length);
  }
}

function laItem({ name, time, verb, verbClass, amount, amountClass, color }) {
  return `
    <div class="la-item">
      <div class="la-row">
        <div class="la-avatar" style="background:linear-gradient(135deg,${color})"></div>
        <span class="la-name">${name}</span>
        <span class="la-time">${time}</span>
      </div>
      <div class="la-body">
        <span class="la-verb ${verbClass}">${verb}</span>
        <span class="la-token">MOON</span>
        <span class="la-amount ${amountClass}">${amount}</span>
      </div>
    </div>
`;
}

function buildMoonFeed() {
  const rows = [
    { name: '@whale_max', time: '8s', verb: 'bought', verbClass: 'buy', amount: '+8.4 SOL', amountClass: 'up', color: '#7cc4a4,#3d7458' },
    { name: '@diamondhands', time: '18s', verb: 'bought', verbClass: 'buy', amount: '+12 SOL 🐋', amountClass: 'up', color: '#e8a87c,#d68a5b' },
    { name: '@apewhale', time: '34s', verb: 'sold', verbClass: 'sell', amount: '-3.5 SOL', amountClass: 'down', color: '#d65a54,#b94842' },
    { name: '@solana_bull', time: '49s', verb: 'bought', verbClass: 'buy', amount: '+1.8 SOL', amountClass: 'up', color: '#9ed8b8,#5ba886' },
    { name: '@moon_farmer', time: '1m', verb: 'bought', verbClass: 'buy', amount: '+2.2 SOL', amountClass: 'up', color: '#d4a256,#8a5e1e' },
    { name: '@trader_x', time: '2m', verb: 'sold', verbClass: 'sell', amount: '-0.7 SOL', amountClass: 'down', color: '#a878ff,#7c5edd' },
    { name: '@sprout_alpha', time: '2m', verb: 'bought', verbClass: 'buy', amount: '+4.0 SOL', amountClass: 'up', color: '#f4cba0,#e8a87c' },
    { name: '@bob', time: '3m', verb: 'sold', verbClass: 'sell', amount: '-1.2 SOL', amountClass: 'down', color: '#5ee2ff,#3aaad4' },
    { name: '@frank', time: '4m', verb: 'bought', verbClass: 'buy', amount: '+0.9 SOL', amountClass: 'up', color: '#ff6b8a,#ff8b5e' },
  ];
  return rows.map(laItem).join('');
}

function transformBlock(block) {
  let next = block
    .replace(/<div class="la-header">[\s\S]*?<\/div>\s*<div class="la-subhead">[\s\S]*?<\/div>/, `<div class="la-header"><span class="la-pulse"></span>Live · MOON token</div>
  <div class="la-subhead">recent moves on this token</div>`)
    .replace(/\/\/ Demo: simulate one new fresh activity every 8s/, '// Demo: simulate one new MOON activity every 8s');

  const feedStart = next.indexOf('<div class="la-feed" id="laFeed">');
  const asideEnd = next.indexOf('\n</aside>', feedStart);
  if (feedStart < 0 || asideEnd < 0) throw new Error('Could not locate Live Activity feed body');
  const feedOpenEnd = next.indexOf('>', feedStart) + 1;
  next = next.slice(0, feedOpenEnd) + '\n' + buildMoonFeed() + '\n  ' + next.slice(asideEnd);

  next = next.replace(
    /const pool = \[[\s\S]*?\];/,
    `const pool = [
    { name: '@whale_max', verb: 'buy', verbTxt: 'bought', token: 'MOON', amount: '+8.4 SOL', amountCls: 'up', color: '#7cc4a4,#3d7458' },
    { name: '@diamondhands', verb: 'buy', verbTxt: 'bought', token: 'MOON', amount: '+12 SOL 🐋', amountCls: 'up', color: '#e8a87c,#d68a5b' },
    { name: '@apewhale', verb: 'sell', verbTxt: 'sold', token: 'MOON', amount: '-3.5 SOL', amountCls: 'down', color: '#d65a54,#b94842' },
    { name: '@solana_bull', verb: 'buy', verbTxt: 'bought', token: 'MOON', amount: '+1.8 SOL', amountCls: 'up', color: '#9ed8b8,#5ba886' },
  ];`
  );

  const nonMoonToken = next.match(/<span class="la-token">(?!(MOON|\$\{x\.token\})<)[^<]+<\/span>|token: '(?!MOON')[^']*'/);
  if (nonMoonToken) throw new Error(`Non-MOON token remains in token_detail LA block: ${nonMoonToken[0]}`);
  return next;
}

const anchor = fs.readFileSync(anchorPath, 'utf8');
const start = anchor.indexOf(startMarker);
const end = anchor.indexOf(endMarker, start);
if (start < 0 || end < 0) throw new Error('Live Activity markers not found in token_list_v4.html');
const block = transformBlock(anchor.slice(start, end + endMarker.length));

let detail = fs.readFileSync(detailPath, 'utf8');
const before = countMarkers(detail);
detail = removeExistingLa(detail);
const bodyIndex = detail.lastIndexOf('</body>');
if (bodyIndex < 0) throw new Error('No </body> found in token_detail.html');
detail = detail.slice(0, bodyIndex) + '\n' + block + '\n\n' + detail.slice(bodyIndex);
fs.writeFileSync(detailPath, detail, 'utf8');

const verify = fs.readFileSync(detailPath, 'utf8');
const after = countMarkers(verify);
if (after < before) {
  throw new Error(`token_detail.html: emoji/domain marker count regressed ${before} -> ${after}`);
}

console.log(`token_detail.html: Live Activity added | markers ${before}->${after}`);
console.log(`aside count: ${(verify.match(/<aside class="live-activity"/g) || []).length}`);
console.log(`MOON token chips: ${(verify.match(/<span class="la-token">MOON<\/span>/g) || []).length}`);
