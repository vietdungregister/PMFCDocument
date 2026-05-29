const fs = require('fs');
const path = require('path');
const files = process.argv.slice(2);

for (const file of files) {
  const html = fs.readFileSync(file, 'utf8');
  const scripts = [...html.matchAll(/<script\b[^>]*>([\s\S]*?)<\/script>/gi)];
  scripts.forEach((match, index) => {
    const code = match[1];
    try {
      new Function(code);
    } catch (err) {
      const before = html.slice(0, match.index + err.lineNumber);
      const line = html.slice(0, match.index).split(/\r?\n/).length + (err.lineNumber || 0);
      console.log(`${path.basename(file)} script ${index + 1}: ${err.message}`);
      console.log(`  approx line: ${line}`);
      const lines = code.split(/\r?\n/);
      const start = Math.max(0, (err.lineNumber || 1) - 4);
      const end = Math.min(lines.length, (err.lineNumber || 1) + 3);
      for (let i = start; i < end; i++) {
        console.log(`${String(i + 1).padStart(4)}: ${lines[i]}`);
      }
    }
  });
}
