# WILD_PHASE2.md — fix gaps from Phase 1

You (Codex) finished Phase 1 (initial Wild rollout in `mockup_final/`) and a mojibake/emoji-restore pass after that. The team has reviewed and found **two classes of gap** that still need fixing. This file is the spec for that fix work.

Read `AGENTS.md` + `WILD_THEME.md` first if you don't have them in context. Then come back here.

---

## 0. What's still broken

### A. `mockup_final/token_list_v4.html` is truncated

The anchor file was supposed to be byte-identical with the gold reference at `../Sửa giao diện html/token_list_v4_wild.html`. It isn't. Verify:

```bash
wc -l mockup_final/token_list_v4.html        # current ≈ 3311 lines
wc -l "../Sửa giao diện html/token_list_v4_wild.html"  # gold ≈ 3647 lines
```

The truncation cuts off the file mid-Card 6 (`<!-- Card 6: Silver SILVER037 -->`) and drops everything after that:
- end of card 6,
- `</div></main>`,
- the helper scripts block (sort/filter/wallet),
- the mascot character HTML + wild-edition chip,
- the Wild v0.2 JS IIFE,
- the **Live Activity panel** (HTML + JS) — this is the one the team noticed visually missing on the right side,
- `</body></html>`.

Root cause was an earlier copy operation that hit a stale file-system cache and silently wrote only the first 127,605 bytes. Don't reproduce that. See §1 for the safe procedure.

### B. ~90 domain-specific cards across 12 pages were never polaroidized

You applied Wild base styles (root tokens, body, marquee, sidebar) to every page. ✅ Good.
You applied polaroid cream-paper treatment to `.token-card` (in the anchor) and `.form-container` (in `create_token.html`). ✅ Good.
You did **not** write polaroid CSS for the page-specific card class names used in the other 12 pages. ❌ Gap.

Concretely, in `mockup_final/` right now, zero of these card classes have `background: var(--w-paper)`:

| Page | Class names | Count |
|------|-------------|-------|
| `FR-012_TokenWar.html` | `.arena-card` | 12 |
| `clubs.html` | `.club-card`, `.pod-card` | 12 + 3 |
| `events.html` | `.ev-card` | 11 |
| `my_profile.html` | `.section-card`, `.stat-card` | 8 + 4 |
| `public_profile.html` | `.section-card`, `.stat-card` | 5 + 4 |
| `creator_dashboard.html` | `.metric-card`, `.stat-card` | 6 + 3 |
| `token_detail.html` | `.token-info-card`, `.trade-card`, `.trust-card`, `.chart-card`, `.tabs-card` | 5 |
| `referrals.html` | `.link-card`, `.table-card`, `.stat-card` | 1 + 1 + 3 |
| `rewards.html` | `.history-card`, `.reels-card` | 1 + 1 |
| `points.html` | `.history-card`, `.rank-card` | 2 + 2 |
| `leaderboard.html` | `.lb-card-head` | 3 |
| `edit_profile_privacy.html` | `.edit-card` | 3 |

Result: those pages render with their original dark surface cards on the new Wild dark-forest background, while the team expected polaroid hero content matching the gold reference's `.token-card`. Visually this reads as "Wild was applied to the chrome but not to the content".

`trading_panel.html`, `FR-012b_TokenWar_PredictionMarket.html`, `sidebar_navigation.html` have no card-named classes that need this fix.

---

## 1. Phase 6 — fix `token_list_v4.html` (do this FIRST)

The fix is a clean copy with byte-count verification. Use **Node.js** (UTF-8 by default), not PowerShell.

```js
// mockup_final/_codex_tools/fix-truncation.js
const fs = require('fs');
const path = require('path');

const SRC = path.resolve(__dirname, '../../../Sửa giao diện html/token_list_v4_wild.html');
const DST = path.resolve(__dirname, '../token_list_v4.html');

const buf = fs.readFileSync(SRC);   // raw bytes, no encoding conversion
console.log('source bytes:', buf.length);

fs.writeFileSync(DST, buf);
const verifyBuf = fs.readFileSync(DST);
console.log('dest bytes:  ', verifyBuf.length);

if (buf.length !== verifyBuf.length) {
  console.error('MISMATCH — copy is truncated.');
  process.exit(1);
}
console.log('OK — byte-identical copy.');
```

Run, then verify:

```bash
node mockup_final/_codex_tools/fix-truncation.js

# Both should report the same byte count and the same line count
wc -c mockup_final/token_list_v4.html
wc -c "../Sửa giao diện html/token_list_v4_wild.html"
wc -l mockup_final/token_list_v4.html        # expect ~3647
grep -c 'class="live-activity"' mockup_final/token_list_v4.html   # expect ≥ 1
grep -c '</body>'              mockup_final/token_list_v4.html    # expect = 1
```

If any line above doesn't match expectations, stop and report what you saw. Don't re-run with a different tool — the source vs dest size mismatch is meaningful.

**Encoding caveat — read this even if it sounds obvious.** Earlier rounds in this project lost every emoji (`🔥🌱💎🚀✨🍑🐋…`) and replaced them with `??` or ASCII fallbacks (`·` → `*`, `—` → `-`, `🌱` → ` `). The team had to do a 400-patch restore pass. The root cause was PowerShell `Get-Content` / `Set-Content` defaulting to Windows-1252 and silently re-encoding. For every file operation in Phase 6 and Phase 7:

- **Use** `node` with `fs.readFileSync` / `fs.writeFileSync` (UTF-8 by default), or `Get-Content -Encoding UTF8` / `Set-Content -Encoding UTF8NoBOM` if you must use PowerShell.
- **Never** use `Get-Content` / `Set-Content` without `-Encoding UTF8`.
- **Never** use `sed -i` on Windows without confirming locale is UTF-8.
- **After every file write**, validate emoji preservation with:
  ```bash
  grep -c '🌱\|🔥\|💎\|·' mockup_final/<file>.html
  ```
  This should return a positive number on any page that had emoji before your edit. If you get 0, you stripped emoji again — stop and audit your tooling.

---

## 2. Phase 7 — polaroidize the 12 pages

Treat this as one CSS-injection task per page. For each page in the table from §0.B:

1. Append a single new `<style>` block at the end of the file's `<style>` (i.e. just before `</style>`).
2. Inside that block, write rules that map the page's existing card class names to the polaroid recipe for their **type** (see §2.1 — there are four types).
3. Save.
4. Verify (see §3).

Don't rename classes. Don't change HTML structure. Don't merge files into a shared stylesheet. Each mockup stays self-contained.

### 2.1 Four card types

You'll see different treatments depending on what the card is showing. Pick the right type for each class.

#### Type 1 — "list-card" (full polaroid)

Use for **the primary content cards** on a list/grid page. They're the hero, they should look like polaroids in the gold reference.

Apply to: `.arena-card`, `.club-card`, `.ev-card`, `.section-card` (the big ones holding charts/tabs), `.token-info-card`, `.trade-card`, `.link-card`, `.history-card`, `.reels-card`, `.lb-card-head`, `.edit-card`.

```css
/* === Wild list-card polaroid (Phase 7) === */
.SELECTOR_HERE {
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
.SELECTOR_HERE:hover {
  transform: translateY(-6px) scale(1.015) !important;
  box-shadow:
    0 22px 44px -10px rgba(0,0,0,0.65),
    0 8px 16px rgba(0,0,0,0.35) !important;
}
/* Washi tape */
.SELECTOR_HERE::before {
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
.SELECTOR_HERE:nth-of-type(even)::before {
  background: var(--w-tape-p) !important;
  left: 60% !important;
  transform: translateX(-50%) rotate(4deg) !important;
}
.SELECTOR_HERE:nth-of-type(3n)::before {
  background: var(--w-tape-g) !important;
}
/* Text inside the card → ink colors (don't override badges/buttons) */
.SELECTOR_HERE,
.SELECTOR_HERE p,
.SELECTOR_HERE span:not(.btn):not([class*='btn']):not([class*='badge']),
.SELECTOR_HERE div:not([class*='btn']):not([class*='banner']):not([class*='avatar']):not([class*='hero']):not([class*='gradient']) {
  color: var(--w-ink) !important;
}
```

Replace `SELECTOR_HERE` with the actual class. If the page has two list-card classes, you can comma-separate them in one ruleset.

#### Type 2 — "stat-card" (mini polaroid)

Use for **small number/KPI cards** — usually 100-200px wide, showing one stat each.

Apply to: `.stat-card`, `.metric-card`, `.rank-card`.

```css
/* === Wild stat-card mini polaroid === */
.SELECTOR_HERE {
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
.SELECTOR_HERE:hover { transform: translateY(-2px) !important; }
.SELECTOR_HERE::before {
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
.SELECTOR_HERE:nth-of-type(even)::before {
  background: var(--w-tape-p) !important;
  left: 60% !important;
  transform: translateX(-50%) rotate(3deg) !important;
}
.SELECTOR_HERE,
.SELECTOR_HERE > * {
  color: var(--w-ink) !important;
}
/* The big number stays mono-bold ink */
.SELECTOR_HERE [class*='value'], .SELECTOR_HERE [class*='big'] {
  font-family: var(--font-mono) !important;
  font-weight: 700 !important;
  color: var(--w-ink) !important;
}
.SELECTOR_HERE [class*='label'], .SELECTOR_HERE [class*='sub'] {
  color: var(--w-ink-2) !important;
}
```

#### Type 3 — "data-frame" (polaroid wrap, dark inside)

Use for **a card that contains a chart, an order book, or any dense data display.** The outer card gets polaroid treatment; the inner data area stays dark for legibility.

Apply to: `.chart-card`, `.tabs-card`, `.pod-card` (it's the 1/2/3 club podium, has data + ranks).

```css
/* === Wild data-frame polaroid (outer cream, inner dark) === */
.SELECTOR_HERE {
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
.SELECTOR_HERE::before {
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
/* Card label / title inside → ink */
.SELECTOR_HERE > h2, .SELECTOR_HERE > h3,
.SELECTOR_HERE > [class*='title'], .SELECTOR_HERE > [class*='label'] {
  color: var(--w-ink) !important;
  font-family: var(--font-disp-it) !important;
  font-style: italic !important;
}
/* But the inner dense-data canvas stays dark */
.SELECTOR_HERE canvas,
.SELECTOR_HERE [class*='canvas'],
.SELECTOR_HERE [class*='chart-body'],
.SELECTOR_HERE [class*='reel-cell'],
.SELECTOR_HERE [class*='reels-row'] {
  background: var(--surface-1) !important;
  color: var(--text-1) !important;
  border-radius: 10px !important;
  padding: 10px !important;
}
```

#### Type 4 — "table-card" (flat dark, no polaroid)

Use for **wide tabular data with many rows** (history table, leaderboard table). Polaroid cream paper makes mono digit columns hard to read at scale.

Apply to: `.history-card` (the one in `rewards.html` and `points.html` that holds a `<table>`), `.table-card`, `.trust-card` (when it's a list of multiple trust scores rather than a single big number).

Don't add polaroid CSS here at all. Instead, lightly Wild-trim it:

```css
/* === Wild table-card (kept flat dark, just trimmed) === */
.SELECTOR_HERE {
  background: var(--surface-1) !important;
  border: 1px solid var(--border-1) !important;
  border-radius: var(--r-lg) !important;
  padding: 18px !important;
  color: var(--text-1) !important;
}
.SELECTOR_HERE > [class*='title'], .SELECTOR_HERE > h2, .SELECTOR_HERE > h3 {
  font-family: var(--font-disp-it) !important;
  font-style: italic !important;
  color: var(--sp-peach-400) !important;
}
.SELECTOR_HERE table { color: var(--text-1) !important; }
.SELECTOR_HERE th { color: var(--sp-peach-400) !important; }
```

### 2.2 Page-by-page assignment

This is the **authoritative mapping**. Don't deviate without a reason.

| Page | Class | Type | Notes |
|------|-------|------|-------|
| `FR-012_TokenWar.html` | `.arena-card` | 1 list-card | "?" icon + title + bar + back buttons. Polaroid the outer; keep the bar gradient + YES/NO pill buttons as-is. |
| `clubs.html` | `.club-card` | 1 list-card | Keep `.club-banner` inline gradient as a colored hero strip (don't blank it). Polaroid only the card frame. |
| `clubs.html` | `.pod-card` | 3 data-frame | The top-3 podium cards. They show inline rank ribbon + stats; the inline gradient banner stays. |
| `events.html` | `.ev-card` | 1 list-card | Date + title + RSVP. Sticker the date area; polaroid the card. |
| `creator_dashboard.html` | `.metric-card` | 2 stat-card | Small KPIs. |
| `creator_dashboard.html` | `.stat-card` | 2 stat-card | Same. |
| `my_profile.html` | `.section-card` | 1 list-card | Holds tabs + content. |
| `my_profile.html` | `.stat-card` | 2 stat-card | The 4 quick stats. |
| `public_profile.html` | `.section-card` | 1 list-card | Same shape as my_profile. |
| `public_profile.html` | `.stat-card` | 2 stat-card | Same. |
| `token_detail.html` | `.token-info-card` | 1 list-card | The hero info card. |
| `token_detail.html` | `.trade-card` | 1 list-card | The buy/sell form (stays light, buttons keep their green/red). |
| `token_detail.html` | `.chart-card` | 3 data-frame | Outer cream, inner chart canvas stays dark. |
| `token_detail.html` | `.tabs-card` | 3 data-frame | Tabs label is ink, inner tab content body inherits page. |
| `token_detail.html` | `.trust-card` | 1 list-card | If it shows a single trust score block. |
| `referrals.html` | `.link-card` | 1 list-card | The big share-link block at top. |
| `referrals.html` | `.stat-card` | 2 stat-card | The 3 stat boxes. |
| `referrals.html` | `.table-card` | 4 table-card | The wide referral history table. |
| `rewards.html` | `.history-card` | 4 table-card | Wide history table — keep flat dark. |
| `rewards.html` | `.reels-card` | 3 data-frame | Slot reel area — outer cream, reels themselves dark squares (already are). |
| `points.html` | `.history-card` | 4 table-card | Same as rewards. |
| `points.html` | `.rank-card` | 2 stat-card | The 2 mini rank widgets. |
| `leaderboard.html` | `.lb-card-head` | 3 data-frame | The 3 podium heads at top. The flat list rows below stay as-is. |
| `edit_profile_privacy.html` | `.edit-card` | 1 list-card | Each settings group is a polaroid block. |

### 2.3 Tooling tip

Don't paste these CSS rules by hand 12 times. Write one small Node script that, for each page, appends the right rules. Keep it under `mockup_final/_codex_tools/`.

```js
// mockup_final/_codex_tools/apply-cards.js  (sketch — adapt as needed)
const fs = require('fs');
const path = require('path');

const RECIPES = {
  list_card:   `/* paste type 1 rules with SELECTOR_HERE swapped to {S} */`,
  stat_card:   `/* type 2 */`,
  data_frame:  `/* type 3 */`,
  table_card:  `/* type 4 */`,
};

// per page: list of [class, recipeKey]
const PAGES = {
  'FR-012_TokenWar.html': [['.arena-card', 'list_card']],
  'clubs.html':           [['.club-card',  'list_card'], ['.pod-card', 'data_frame']],
  // ... etc, from §2.2 ...
};

for (const [file, rules] of Object.entries(PAGES)) {
  const fp = path.join(__dirname, '..', file);
  let html = fs.readFileSync(fp, 'utf8');
  let css = '\n/* === Wild Phase 7 — card polaroid (added by apply-cards.js) === */\n';
  for (const [cls, recipe] of rules) {
    css += RECIPES[recipe].replaceAll('SELECTOR_HERE', cls) + '\n';
  }
  // Inject just before the LAST </style>
  const idx = html.lastIndexOf('</style>');
  if (idx < 0) { console.error(`no </style> in ${file}`); continue; }
  html = html.slice(0, idx) + css + html.slice(idx);
  fs.writeFileSync(fp, html);
  console.log(`✓ ${file}: ${rules.length} card classes polaroidized`);
}
```

---

## 3. Verification

Run after Phase 6 and after Phase 7. Update `_codex_screenshots/` with fresh captures for the affected pages.

### 3.1 Phase 6 verify

```bash
# token_list_v4 must match gold reference exactly
diff -q mockup_final/token_list_v4.html "../Sửa giao diện html/token_list_v4_wild.html"
# (expected: no output = files are identical)

# Live Activity panel present
grep -c '<aside class="live-activity"' mockup_final/token_list_v4.html  # ≥ 1
grep -c 'class="la-feed"'              mockup_final/token_list_v4.html  # ≥ 1
grep -c 'class="la-item"'              mockup_final/token_list_v4.html  # ≥ 8

# Closing tags present
grep -c '</body>' mockup_final/token_list_v4.html  # = 1
grep -c '</html>' mockup_final/token_list_v4.html  # = 1

# Emoji preserved (earlier round stripped them)
grep -c '🌱\|🔥\|💎\|·' mockup_final/token_list_v4.html  # > 30
```

### 3.2 Phase 7 verify

For every page touched, the matching card class should now resolve to cream paper:

```bash
# Example — clubs
grep -A2 '\.club-card[^a-z-]' mockup_final/clubs.html | grep -c 'var(--w-paper)'  # ≥ 1

# Run the existing verify.js to re-screenshot
node mockup_final/_codex_tools/verify.js
```

Open the new screenshots in `mockup_final/_codex_screenshots/` and confirm each affected page now reads visually like the gold reference (cream polaroid hero content on dark forest background). If a page still looks dark after the CSS injection, find where the original `background: var(--surface-1)` rule lives in that file and add a more specific selector or `!important` until the polaroid wins.

### 3.3 Re-check: did you strip emoji while editing?

After Phase 7, on every modified page:

```bash
# count emojis present before vs after — must be ≥ pre-edit count
grep -c '🌱\|🔥\|💎\|🚀\|✨\|🍑\|🥇\|🐋\|·' mockup_final/<file>.html
```

If any file regresses, audit your CSS-injection step's encoding — see §1 caveat.

---

## 4. Update the report

When Phases 6 and 7 are done, append a new section to `mockup_final/WILD_APPLY_REPORT.md`:

```markdown
## Phase 6 + 7 — anchor restore + card polaroidization

### Phase 6 — token_list_v4 truncation fix
- byte-identical copy from gold reference: yes / no
- Live Activity panel present: yes / no
- emoji count preserved: <N>

### Phase 7 — polaroidize 12 pages
| File | Classes treated | Type assignments |
|------|-----------------|------------------|
| FR-012_TokenWar.html | .arena-card | 1×list-card |
| ... |
```

Then, in the existing "Open questions" section, append anything genuinely ambiguous you hit. Don't carry over the old open questions (mascot mobile threshold was already accepted at 900px).

---

## 5. What NOT to do

- Don't touch `.token-card` styling — it already works, fixing what isn't broken just risks regression.
- Don't apply polaroid Type 1 to `.history-card` even though the name fits the pattern. History is a wide table; keep it Type 4.
- Don't refactor `.section-card` etc. by renaming them to `.card.polaroid`. The team explicitly wants to preserve existing class names so backend hooks keep working.
- Don't try to "improve" hero banners on `.club-card` (the inline gradient strip is a deliberate per-club brand color — keep it).
- Don't add the Live Activity panel to any page besides `token_list_v4.html`. It belongs on the trending list only.
- Don't use PowerShell `Get-Content` / `Set-Content` without `-Encoding UTF8`. See §1 encoding caveat.

You have everything you need. Start at §1.
