# WILD_RECOVERY.md — STRICT recovery after Phase 8 disaster

You (Codex) ran Phase 8 and destroyed 16 of 18 files in `mockup_final/`. Audit:

| | `<body>` | `</body>` | `</html>` |
|---|---|---|---|
| `token_list_v4.html` | ✓ | ✗ | ✗ |
| `home_full_layout.html` | ✓ | ✓ | ✓ |
| **other 16 files** | **✗** | **✗** | **✗** |

The Phase 8 script you wrote used a "find the last `</style>` and inject after it" pattern that, due to a bug (likely a regex catastrophic backtrack, a substring boundary error, or `String.replace` consuming downstream content), **replaced** the body section instead of inserting before/after it. The entire `<body>…</body>` of 16 files is gone. Only the `<head>` survived. Those files are unrecoverable from their current state.

This recovery doc undoes that damage and re-applies the work safely. **Read this entire file before touching any other file.**

---

## 0. Hard rules (read twice)

These are non-negotiable. Violating any one of them is grounds for stopping the recovery and reporting back without committing the change.

1. **INSERT only. Never REPLACE.** Any code path that mutates a file must produce `new = head + new_chunk + tail` — never `new = head + new_chunk` and never anything based on a single `String.replace` call against the file body. The Phase 8 disaster was exactly this.
2. **Every file write is bracketed by a precondition check and a postcondition check.** Both must pass; if either fails, restore the file from backup and report.
   - Precondition: file currently has both `<body` and `</html>` tokens.
   - Postcondition: file still has both `<body` and `</html>` tokens, line count is `previous ± expected_delta` (you state the delta up front), and `</style>` count is unchanged (the head is intact).
3. **Backup before every phase.** `cp -r mockup_final/ mockup_final.bak-<phase>-<utc-timestamp>/` so each phase can be rolled back independently.
4. **Test on one file before scaling.** You run the new operation on one specified test file, the user confirms visually, then you run on the rest.
5. **No PowerShell file I/O.** Use Node's `fs.readFileSync` / `fs.writeFileSync` (UTF-8 by default). PowerShell `Get-Content` / `Set-Content` without `-Encoding UTF8` strips emoji and corrupts multibyte characters — this project has already lost 400+ emojis to that.
6. **Pre-flight self-audit.** First thing you do is print: Node version, OS, cwd, encoding of a sample file, and the contents of `_codex_tools/` from any prior phase. Stop and report if any prior tool looks like it would re-introduce the Phase 8 bug.
7. **One phase per run.** Do not chain Phase 8 → 9 → 10 in one go. After each phase, stop, post screenshots, get a verification ack, then continue.

---

## 1. Phase R0 — Pre-flight + backup

Before any restoration:

```bash
# In the mockups-sprout/ folder (project root). Confirm you're in the right place.
pwd
ls -la mockup_final/ | head
node --version  # need ≥ 18

# Backup whatever's left of the broken state (even if useless, keep evidence)
cp -r mockup_final/ mockup_final.bak-broken-$(date -u +%Y%m%dT%H%M%SZ)/
```

Then prove every original mockup is intact (these are your source of truth):

```bash
for f in ./*.html; do
  body=$(grep -c '<body' "$f")
  closebody=$(grep -c '</body>' "$f")
  closehtml=$(grep -c '</html>' "$f")
  echo "$f  body=$body  /body=$closebody  /html=$closehtml"
done | head -20
```

Every file in `./` (not `mockup_final/`) should report `body=1 /body=1 /html=1`. If any doesn't, **stop and report** — your originals are also damaged and we need to recover from elsewhere before continuing.

---

## 2. Phase R1 — Restore mockup_final from originals

This is the foundation. Throw away the broken `mockup_final/*.html`. Re-copy fresh from `./*.html`.

```js
// _codex_tools/r1-restore.js
const fs = require('fs');
const path = require('path');

const SRC = path.resolve(__dirname, '..');                  // project root
const DST = path.resolve(__dirname, '..', 'mockup_final');  // recovery target

const FILES = fs.readdirSync(SRC).filter(f => f.endsWith('.html'));

let mismatches = 0;
for (const f of FILES) {
  const src = path.join(SRC, f);
  const dst = path.join(DST, f);

  const buf = fs.readFileSync(src);  // raw bytes — no string coercion
  fs.writeFileSync(dst, buf);

  const back = fs.readFileSync(dst);
  if (back.length !== buf.length) {
    console.error(`MISMATCH ${f}: src=${buf.length} dst=${back.length}`);
    mismatches++;
    continue;
  }
  const txt = back.toString('utf8');
  if (!txt.includes('</body>') || !txt.includes('</html>')) {
    console.error(`MALFORMED ${f}: missing closing tags after copy`);
    mismatches++;
    continue;
  }
  console.log(`✓ ${f} (${buf.length} bytes)`);
}

if (mismatches > 0) process.exit(1);
console.log('R1 OK — all originals restored');
```

Verification after running:

```bash
node _codex_tools/r1-restore.js
# Sanity: every file in mockup_final now has body+/body+/html
for f in mockup_final/*.html; do
  b=$(grep -c '<body'   "$f")
  cb=$(grep -c '</body>' "$f")
  ch=$(grep -c '</html>' "$f")
  [ "$b" -ge 1 ] && [ "$cb" -ge 1 ] && [ "$ch" -ge 1 ] || echo "BAD: $f"
done
# Expected: zero "BAD" lines
```

After R1, `mockup_final/` is identical to the originals — i.e. the **pre-Wild** state. None of the Wild theme is applied yet. That's intentional. We re-apply in order.

**Stop here. Get explicit user ack before continuing to R2.**

---

## 3. Phase R2 — Re-apply Wild base (root tokens + body bg + marquee)

This is the smallest Wild change: each page gets the canonical `:root` tokens, the body gradient mesh, and the marquee styles. None of these affect the body's HTML structure — they're all `<style>` additions.

### 3.1 Source of truth

Extract the canonical blocks from `../Sửa giao diện html/token_list_v4_wild.html` once into named CSS files under `_codex_tools/`:

- `_codex_tools/base-root.css` — the `:root { … }` block (Mood B + Wild ext tokens)
- `_codex_tools/base-body.css` — the `body { background: …; }` rules including the radial-gradient mesh
- `_codex_tools/base-marquee.css` — the `.marquee` + `.marquee-track` + `@keyframes scroll` block
- `_codex_tools/base-fonts.html` — the Google Fonts `<link>` tag(s) for Inter + Plus Jakarta + JetBrains Mono + Fraunces (italic) + Caveat

Use Node to slice these out by their explicit comment markers in the gold reference. Confirm each extracted file is non-empty and has the expected selectors.

### 3.2 Inject pattern (safe)

For each page in `mockup_final/`:

```js
function safeInjectIntoStyle(html, css, marker) {
  // Locate the FIRST <style> opening tag. Insert immediately after it.
  // This is INSERT, not REPLACE: head + insertion + tail.
  const styleOpen = html.indexOf('<style>');
  if (styleOpen < 0) throw new Error('no <style> tag — file is malformed');
  const afterOpen = styleOpen + '<style>'.length;
  const head = html.slice(0, afterOpen);
  const tail = html.slice(afterOpen);
  const wrapped = `\n/* === ${marker} === */\n${css}\n/* === end ${marker} === */\n`;
  return head + wrapped + tail;
}
```

Then for every file:

```js
const before = fs.readFileSync(file, 'utf8');
// Precondition
if (!before.includes('<body') || !before.includes('</html>')) {
  throw new Error(`precondition fail ${file}`);
}
const beforeLines = before.split('\n').length;

const after = safeInjectIntoStyle(before, baseCss, 'Recovery R2 base');

// Postcondition
if (!after.includes('<body') || !after.includes('</html>')) {
  throw new Error(`postcondition fail ${file} — body/html got dropped`);
}
const afterLines = after.split('\n').length;
const delta = afterLines - beforeLines;
const expectedDelta = baseCss.split('\n').length + 3;
if (Math.abs(delta - expectedDelta) > 3) {
  throw new Error(`line-delta sanity fail ${file}: got ${delta}, expected ~${expectedDelta}`);
}

fs.writeFileSync(file, after);
console.log(`✓ ${file}  Δlines=${delta}`);
```

The pattern above is the **safe pattern** for every CSS-injection step in this recovery. Use it verbatim. Do not write your own variant without explicit user approval.

### 3.3 Test on one file, then scale

1. Run R2 on **only** `mockup_final/clubs.html`.
2. Stop. Print to chat: line count before, line count after, delta, and the result of `grep -c '</body>'` (must be ≥ 1).
3. Wait for user ack.
4. Then run on the other 14 functional pages (skip `home_full_layout.html`, skip `token_list_v4.html` which already has all this).

### 3.4 R2 verification

```bash
for f in mockup_final/*.html; do
  has_root=$(grep -c -- '--sp-peach-400' "$f")
  has_body=$(grep -c '</body>' "$f")
  printf '%-50s root:%d body:%d\n' "$f" "$has_root" "$has_body"
done
# Every functional page: root>=1 AND body>=1
```

Take fresh screenshots of 2 pages (`clubs.html` + `events.html`). Confirm they render with body content intact and Wild colors visible.

**Stop here. Get user ack before R3.**

---

## 4. Phase R3 — Canonical sidebar (safe injection)

Same safe-insert pattern. The sidebar CSS block is extracted exactly as in WILD_PHASE3.md §1.1. The difference here: you insert it at the **end** of the last `<style>` block on the page, just before that block's closing `</style>`, so it overrides any earlier sidebar CSS.

### 4.1 Safe insertion before `</style>`

```js
function safeInjectBeforeStyleClose(html, css, marker) {
  // Locate the LAST </style>. Insert immediately before it.
  const styleClose = html.lastIndexOf('</style>');
  if (styleClose < 0) throw new Error('no </style> in file');
  const head = html.slice(0, styleClose);
  const tail = html.slice(styleClose); // starts at '</style>'
  const wrapped = `\n/* === ${marker} === */\n${css}\n/* === end ${marker} === */\n`;
  return head + wrapped + tail;
}
```

**Critical check** — print the length of `tail` before injection. It must be `>= 9` (length of `</style>` plus a newline). If `tail` is shorter than the body content you expect, something is wrong; stop.

Also verify that `tail` ITSELF contains `</body>` and `</html>`. If it doesn't, the file is malformed before you even start (the body is upstream of where you're injecting, not downstream).

### 4.2 Apply pattern

Same as R2.3 — test on `clubs.html` first, stop for user ack, then scale to the other 14 functional pages. Skip `token_list_v4.html` (already has the canonical sidebar) and `home_full_layout.html`.

### 4.3 R3 verification

Use the same puppeteer check as WILD_PHASE3.md §1.3 — every page's `getComputedStyle(.sidebar).backgroundImage` must start with the radial-gradient signature.

**Stop here. Get user ack before R4.**

---

## 5. Phase R4 — Tier system

Re-apply WILD_PHASE3.md §2 (Phase 9 tier system) but using the safe insertion pattern. The original Phase 9 spec is correct; only the execution was buggy.

### 5.1 The CSS bug to fix from the prior attempt

In the prior Phase 9 output, Codex produced selectors like:

```css
.club-card, .pod-card::before { content: none !important; }
.club-card, .pod-card::after { content: ''; position: absolute; … }
```

This expands to:
- `.club-card` (the whole card element) gets `position: absolute; left: 0; …`
- `.pod-card::after` gets the same

Result: every `.club-card` becomes a 3px-wide absolutely-positioned bar, which is invisible to users.

When you substitute multiple selectors for `SELECTOR_HERE` in a recipe, you must wrap each selector substitution in parentheses-equivalent grouping. Practically that means: **use a single class per recipe instance, not a comma-separated list**. Repeat the recipe block once per class:

```css
/* WRONG (prior attempt) */
.club-card, .pod-card::before { content: none !important; }

/* RIGHT (per-class block) */
.club-card::before { content: none !important; }
.pod-card::before { content: none !important; }
```

When generating CSS from the recipe templates, expand the substitution one class at a time. If a page has two classes that share a tier, emit two complete copies of the recipe.

### 5.2 Apply pattern

Use `safeInjectBeforeStyleClose` from §4.1. Per-tier CSS, per-page class list, copy from WILD_PHASE3.md §2.3 (authoritative assignment table).

Test on `clubs.html` first (`.club-card` + `.pod-card`, Tier 2 with the per-class fix). Stop. User screenshot ack. Then scale.

### 5.3 R4 verification

```bash
# Each .club-card etc. should now be position:static (or relative), not absolute
node -e "
const puppeteer = require('puppeteer-core');
(async () => {
  const b = await puppeteer.launch({ headless: true, args: ['--no-sandbox','--disable-setuid-sandbox','--disable-dev-shm-usage'] });
  const p = await b.newPage();
  await p.goto('file://' + require('path').resolve('mockup_final/clubs.html'));
  await new Promise(r => setTimeout(r, 1000));
  const info = await p.evaluate(() => {
    const cs = document.querySelectorAll('.club-card');
    if (!cs.length) return 'NO CARDS IN DOM';
    return {
      count: cs.length,
      pos: getComputedStyle(cs[0]).position,
      width: cs[0].getBoundingClientRect().width,
    };
  });
  console.log(info);
  await b.close();
})();
"
# Expected: { count: 12, pos: 'relative', width: ≥ 200 }
```

If `count: 0` or `width: 3` you re-introduced the bug. Roll back, fix, retry.

**Stop here. User ack before R5.**

---

## 6. Phase R5 — Emoji restoration

The originals have intact UTF-8 emojis. R1 copied originals verbatim, so emojis should be preserved through R2/R3/R4 as long as you used Node fs (UTF-8 default).

Sanity check after R4:

```bash
for f in mockup_final/*.html; do
  cnt=$(grep -c '🌱\|🔥\|💎\|🚀\|✨\|🍑\|🥇\|🐋\|·' "$f")
  echo "$f: $cnt"
done
```

Every functional page should report ≥ pre-R1 emoji count. If any page regressed (lost emojis), audit the script that wrote that file — somewhere your tooling re-encoded UTF-8 → cp1252 → UTF-8 and stripped multibyte sequences. Common cause: PowerShell `Set-Content`. Fix the tool, redo the affected file.

No new file writes needed if checks pass.

---

## 7. Phase R6 — LA panel on token_detail

Per WILD_PHASE3.md §3. Lowest-risk step; do it last.

Copy the entire LA panel block (HTML + script) from `mockup_final/token_list_v4.html` into `mockup_final/token_detail.html` right before `</body>`. Use safe insertion:

```js
function safeInjectBeforeBodyClose(html, snippet, marker) {
  const closeBody = html.lastIndexOf('</body>');
  if (closeBody < 0) throw new Error('no </body>');
  const head = html.slice(0, closeBody);
  const tail = html.slice(closeBody); // starts at '</body>'
  return head + `\n<!-- === ${marker} === -->\n${snippet}\n<!-- === end ${marker} === -->\n` + tail;
}
```

Then modify the script's `pool` array in token_detail.html so every entry's `tk` value is `'MOON'`. And change the panel header text:

```html
<div class="la-header"><span class="la-pulse"></span>Live · MOON token</div>
<div class="la-subhead">recent moves on this token</div>
```

Verify:

```bash
grep -c '<aside class="live-activity"' mockup_final/token_detail.html  # = 1
grep -c '<aside class="live-activity"' mockup_final/token_list_v4.html # = 1
# No third page has it
for f in mockup_final/*.html; do
  c=$(grep -c '<aside class="live-activity"' "$f")
  if [ "$c" -gt 0 ] && [[ "$f" != *token_list_v4* ]] && [[ "$f" != *token_detail* ]]; then
    echo "STRAY: $f"
  fi
done
```

---

## 8. Phase R7 — Final verification

Run the existing `_codex_tools/verify.js` to regenerate all desktop + mobile screenshots into `mockup_final/_codex_screenshots/`.

For each page, check:

- File ends with `</body>\n</html>\n` (or close to it; allow trailing whitespace).
- Browser console: zero errors (puppeteer `pageerror` listener).
- `<aside class="sidebar">` is in DOM and `getComputedStyle(.sidebar)` has the radial-gradient signature.
- Tier 2 cards (e.g. `.club-card`, `.ev-card`) are `position: relative`, `display: block` (or whatever they were originally), and have a visible bounding box.
- Tier 1 polaroid pages (`token_list_v4`, `token_detail`) still show cream `.token-card` polaroids.
- Emoji counts haven't regressed (re-run §6 grep).
- `<body>` and `</body>` and `</html>` all present in every file.

Append a fresh section to `mockup_final/WILD_APPLY_REPORT.md`:

```markdown
## Recovery R1–R7 — restoration after Phase 8 disaster

| Page | R1 restored | R2 base | R3 sidebar | R4 tier | R5 emoji | R6 LA |
|------|-------------|---------|------------|---------|----------|-------|
| ... | | | | | | |

## Lessons / new guardrails
- Phase 8 disaster root cause: `String.replace` consumed downstream content. 
  All future CSS injection uses `safeInjectBeforeStyleClose` / `safeInjectIntoStyle` 
  with explicit precondition + postcondition checks.
- Test-on-one-file protocol added: every batch operation now runs against 
  one named test file first, user acks, then scales.
```

---

## 9. What you (Codex) must report at the end of every phase

Don't say "done" without producing this paragraph. The team needs the diagnostics, not vibes.

```
Phase Rn — <one-line summary>
Files touched: N
For each touched file: before lines → after lines (Δ)
Pre/post checks: PASS (or list which failed and what you did)
Emoji counts: <range> (lowest → highest)
Sidebar bg signature: matches anchor / DIFFERS on <list>
Screenshots updated: yes / no
Next required ack: <what user needs to confirm>
```

---

## 10. If a check fails

Stop. Don't "fix forward." Restore the file from `mockup_final.bak-<phase>/`. Write a one-paragraph note explaining which check failed and what the file looked like, and ask for guidance.

You ran out of trust budget after Phase 8. Earn it back by being conservative and explicit, not clever.

Begin at §1 (Phase R0 pre-flight + backup).
