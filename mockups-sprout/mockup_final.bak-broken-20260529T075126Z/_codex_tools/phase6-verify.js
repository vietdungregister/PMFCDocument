const fs = require('fs');

const s = fs.readFileSync('token_list_v4.html', 'utf8');
const countLiteral = needle => s.split(needle).length - 1;
const countRegex = re => (s.match(re) || []).length;

console.log('live-activity', countLiteral('<aside class="live-activity"'));
console.log('la-feed', countLiteral('class="la-feed"'));
console.log('la-item', countLiteral('class="la-item'));
console.log('body-close', countLiteral('</body>'));
console.log('html-close', countLiteral('</html>'));
console.log('emoji-domain', countRegex(/\uE076|\uE068|\uE066|\uE06B|\uFF82\uFF77|🌱|🔥|💎|·/g));
