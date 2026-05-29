const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const anchorPath = path.join(root, 'token_list_v4.html');
const outPath = path.join(__dirname, 'sidebar-block.css');
const phase8Start = '/* === Wild Phase 8 - canonical sidebar (from anchor) === */';
const phase8End = '/* === end Wild Phase 8 - canonical sidebar === */';
const emojiRe = /🌱|🔥|💎|·/gu;

function countMarkers(text) {
  return (text.match(emojiRe) || []).length;
}

function extractSidebarBlock() {
  const anchor = fs.readFileSync(anchorPath, 'utf8');
  const label = '"STICKER DOCK" — sidebar redesign v0.3';
  const labelIndex = anchor.indexOf(label);
  const endMarker = '/* ╚═══ end v0.8 ═══╝ */';
  const endIndex = anchor.indexOf(endMarker, labelIndex);
  if (labelIndex < 0 || endIndex < 0) {
    throw new Error('Canonical sidebar markers not found in token_list_v4.html');
  }

  const startIndex = anchor.lastIndexOf('/*', labelIndex);
  if (startIndex < 0) {
    throw new Error('Could not find opening comment for canonical sidebar block');
  }

  const block = anchor.slice(startIndex, endIndex + endMarker.length);
  if (!block.includes('.nav-item') || !block.includes('.user-card') || !block.includes('--w-paper') || !block.includes('radial-gradient(circle at 50% 12%')) {
    throw new Error('Extracted sidebar block is missing expected canonical sidebar tokens');
  }
  fs.writeFileSync(outPath, block, 'utf8');
  console.log(`extracted sidebar block: ${Buffer.byteLength(block, 'utf8')} bytes -> ${path.relative(root, outPath)}`);
  return block;
}

function removePreviousPhase8(html) {
  let next = html;
  while (true) {
    const start = next.indexOf(phase8Start);
    if (start < 0) return next;
    const end = next.indexOf(phase8End, start);
    if (end < 0) throw new Error('Found Phase 8 start marker without end marker');
    next = next.slice(0, start) + next.slice(end + phase8End.length);
  }
}

function applySidebar(block) {
  const pages = fs.readdirSync(root)
    .filter((file) => file.endsWith('.html'))
    .filter((file) => file !== 'token_list_v4.html' && file !== 'home_full_layout.html');

  for (const file of pages) {
    const fp = path.join(root, file);
    let html = fs.readFileSync(fp, 'utf8');
    const before = countMarkers(html);
    html = removePreviousPhase8(html);

    const styleIndex = html.lastIndexOf('</style>');
    if (styleIndex < 0) throw new Error(`No </style> found in ${file}`);

    const forceImportantBackground = `
/* Force the anchor sidebar background over the earlier Codex linear-gradient !important rule. */
.sidebar {
  background:
    radial-gradient(circle at 50% 12%, rgba(255,211,94,0.18), transparent 45%),
    radial-gradient(circle at 50% 85%, rgba(255,107,138,0.14), transparent 45%),
    rgba(20, 32, 24, 0.85) !important;
}
`;
    const injection = `\n${phase8Start}\n${block}\n${forceImportantBackground}${phase8End}\n`;
    html = html.slice(0, styleIndex) + injection + html.slice(styleIndex);
    fs.writeFileSync(fp, html, 'utf8');

    const verify = fs.readFileSync(fp, 'utf8');
    const after = countMarkers(verify);
    if (after < before) {
      throw new Error(`${file}: emoji/domain marker count regressed ${before} -> ${after}`);
    }
    console.log(`${file}: sidebar canon injected | markers ${before}->${after}`);
  }
}

const block = extractSidebarBlock();
applySidebar(block);
