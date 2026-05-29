const fs = require('fs');
const path = require('path');

const toolsDir = __dirname;
const mockupFinalDir = path.resolve(toolsDir, '..');
const workspaceDir = path.resolve(mockupFinalDir, '..', '..');

const candidates = fs.readdirSync(workspaceDir, { withFileTypes: true })
  .filter(entry => entry.isDirectory())
  .map(entry => path.join(workspaceDir, entry.name, 'token_list_v4_wild.html'))
  .filter(file => fs.existsSync(file));

if (candidates.length === 0) {
  console.error('Could not find token_list_v4_wild.html in workspace sibling folders.');
  process.exit(1);
}

const SRC = candidates[0];
const DST = path.resolve(mockupFinalDir, 'token_list_v4.html');

const before = fs.existsSync(DST) ? fs.readFileSync(DST, 'utf8') : '';
const beforeEmoji = (before.match(/🌱|🔥|💎|·|\uE076|\uE068|\uE066|\uFF82\uFF77/g) || []).length;

const buf = fs.readFileSync(SRC);
console.log('source:', SRC);
console.log('source bytes:', buf.length);
console.log('dest before emoji/domain count:', beforeEmoji);

fs.writeFileSync(DST, buf);

const verifyBuf = fs.readFileSync(DST);
const after = fs.readFileSync(DST, 'utf8');
const afterEmoji = (after.match(/🌱|🔥|💎|·|\uE076|\uE068|\uE066|\uFF82\uFF77/g) || []).length;

console.log('dest bytes:  ', verifyBuf.length);
console.log('dest after emoji/domain count:', afterEmoji);

if (buf.length !== verifyBuf.length) {
  console.error('MISMATCH: copy is truncated.');
  process.exit(1);
}
if (afterEmoji < beforeEmoji) {
  console.error('MISMATCH: emoji/domain count regressed.');
  process.exit(1);
}

console.log('OK: byte-identical copy.');
