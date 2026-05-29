# WILD_PHASE3.md — tier system + sidebar fix

You (Codex) finished Phase 7 (card polaroidization on 12 pages). Team review found two more issues:

1. **Sidebar regression** — the sidebar on non-anchor pages is visually different from `token_list_v4.html`. Codex wrote a simpler sidebar CSS variant on those pages instead of reusing the gold reference's cream-pill sticker sidebar.
2. **Vibe monotony** — polaroid applied to every list-card across 12 pages made cards in `clubs`, `events`, `leaderboard`, etc. visually compete with `token_list_v4` cards. Team chose to **differentiate by tier** so token list stays the hero and other pages quietly support it.

This file is the spec for fixing both. Three phases: 8 (sidebar), 9 (revert + re-tier cards), 10 (LA on token_detail).

Read `AGENTS.md` + `WILD_THEME.md` + `WILD_PHASE2.md` first if you don't have them in context.

---

## 0. What "tier" means

Each page now has one of 4 visual tiers. Treatment is determined by tier, not by which `*-card` class the page happens to use.

| Tier | Visual | Pages |
|------|--------|-------|
| **1 — Hero polaroid** | Cream paper polaroid + washi tape + sticker badges | `token_list_v4.html`, `token_detail.html` |
| **2 — Clean functional** | Dark surface card + 3px peach left accent + peach name | `clubs.html`, `events.html`, `leaderboard.html`, `rewards.html`, `points.html` |
| **3 — Personal hybrid** | 1 polaroid hero card at top + dark sections below | `my_profile.html`, `public_profile.html`, `referrals.html`, `edit_profile_privacy.html` |
| **4 — Form polaroid** | Cream paper form container + cream inputs + peach pill submit | `create_token.html`, `trading_panel.html` |
| **5 — Hybrid mixed** | Mini polaroid stat cards + dark chart areas | `creator_dashboard.html` |
| **6 — Spec doc** | Clean dark with peach headings, no polaroid | `FR-012_TokenWar.html`, `FR-012b_TokenWar_PredictionMarket.html` |
| n/a — Skip | Redirect stub | `home_full_layout.html` |
| n/a — Component preview | Component preview, just keep current sidebar treatment | `sidebar_navigation.html` |

Goal: when a user clicks from token list to a club / event / leaderboard, the polaroid grid doesn't follow them — the chrome stays consistent (sidebar, marquee, mascot) but the content area visibly steps down to "support" treatment. The token list stays the loudest screen in the product.

---

## 1. Phase 8 — fix sidebar consistency

Right now `token_list_v4.html` has the full Wild cream-pill sticker sidebar (gold reference v0.4 + v0.5 + v0.6 + v0.8 layers). Other pages have a simpler dark linear gradient sidebar with transparent nav-items.

The fix is to give every page the same sidebar CSS as the anchor.

### 1.1 Extract the canonical sidebar CSS

From `mockup_final/token_list_v4.html`, copy **everything** between these comment markers (inclusive):

```
/* ╔═══════════════════════════════════════════════════════════╗
   ║ "STICKER + TEXT" — sidebar v0.4 (2026-05-27)              ║
   ║ Combo: small sticker icon LEFT + italic label RIGHT.       ║
   ║ Overrides v0.3 dock-only-icon styles.                      ║
   ╚═══════════════════════════════════════════════════════════╝ */
... ~250 lines of sidebar CSS ...
/* ╚═══ end "STICKER + TEXT" sidebar v0.4 ═══╝ */

/* ╔═══════════════════════════════════════════════════════════╗
   ║ v0.5 SIMPLIFY (2026-05-28) — user feedback                ║
   ╚═══════════════════════════════════════════════════════════╝ */
... ~40 lines ...
/* ╚═══ end v0.5 SIMPLIFY ═══╝ */

/* (4) v0.6 FIX — unify nav-item PILL background */
... ~25 lines ...

/* ╔═══ v0.8 — unify sidebar nav icon bg (one color) ═══╗ */
... ~14 lines ...
/* ╚═══ end v0.8 ═══╝ */
```

This is the **authoritative sidebar** the team has signed off on. Don't modify it; just transplant it.

Use Node to do the extraction once, store it as a string constant in your tooling, then inject.

```js
// mockup_final/_codex_tools/extract-sidebar.js
const fs = require('fs');
const path = require('path');

const anchor = fs.readFileSync(
  path.resolve(__dirname, '../token_list_v4.html'),
  'utf8'
);

// Pick the contiguous block from the v0.4 comment header through the last v0.8 end marker
const startMarker = '/* ╔═══════════════════════════════════════════════════════════╗\n     ║ "STICKER + TEXT" — sidebar v0.4';
const endMarker   = '/* ╚═══ end v0.8 ═══╝ */';

const start = anchor.indexOf(startMarker);
const end   = anchor.indexOf(endMarker);
if (start < 0 || end < 0) { console.error('markers not found'); process.exit(1); }

const sidebarBlock = anchor.slice(start, end + endMarker.length);
fs.writeFileSync(
  path.resolve(__dirname, 'sidebar-block.css'),
  sidebarBlock
);
console.log('extracted', sidebarBlock.length, 'bytes →', '_codex_tools/sidebar-block.css');
```

Run it once. Confirm `sidebar-block.css` is non-empty and contains references to `.nav-item`, `.user-card`, `--w-paper`, `cream`. If not, your markers don't match — read the anchor file with a hex dumper and find the correct unicode versions of `═` and `╝` (they may have been replaced earlier).

### 1.2 Apply the block to every other page

For each page **except** `token_list_v4.html` and `home_full_layout.html`:

1. **Delete** the existing Codex sidebar CSS in that page. Look for:
   - Any `.sidebar {` rule whose `background:` is `linear-gradient(180deg, #131f18 0%, #0e1a13 100%)` — that's Codex's variant.
   - Any rules under `.sidebar::before`, `.logo`, `.logo-name`, `.logo-sub`, `.logo-mascot`, `.nav-item`, `.nav-item svg`, `.nav-item:hover`, `.nav-item.active`, `.nav-badge`, `.user-card`, `.sidebar-footer` that Codex added in earlier phases.
   - You can spot them: they're contiguous, they're outside any `/* === Wild Phase 7 === */` markers, and the `.sidebar` rule uses the linear gradient.
2. **Insert** the extracted sidebar block in its place. Position it inside `<style>`, late enough that it overrides any earlier Codex sidebar rules.

```js
// mockup_final/_codex_tools/fix-sidebar.js  (sketch)
const fs = require('fs');
const path = require('path');

const sidebarBlock = fs.readFileSync(
  path.resolve(__dirname, 'sidebar-block.css'),
  'utf8'
);

const PAGES = fs.readdirSync(path.resolve(__dirname, '..'))
  .filter(f => f.endsWith('.html'))
  .filter(f => f !== 'token_list_v4.html' && f !== 'home_full_layout.html');

for (const file of PAGES) {
  const fp = path.resolve(__dirname, '..', file);
  let html = fs.readFileSync(fp, 'utf8');

  // 1) Remove the Codex sidebar block
  //    Identify by the `linear-gradient(180deg, #131f18 0%, #0e1a13 100%)` signature
  //    and walk forward until the next non-sidebar selector.
  //    This is page-specific; consider matching the Codex block with a regex anchored
  //    on `.sidebar { position: fixed` and ending at a clean break before another section.
  //    Be conservative — if you can't cleanly excise, just OVERRIDE by appending the
  //    extracted block at the end of the last <style> tag (CSS order wins).
  //
  //    Safer minimum: just append. !important inside the extracted block will override.

  const idx = html.lastIndexOf('</style>');
  if (idx < 0) { console.error('no </style>', file); continue; }
  const inject = '\n/* === Wild Phase 8 — canonical sidebar (from anchor) === */\n'
               + sidebarBlock + '\n';
  html = html.slice(0, idx) + inject + html.slice(idx);

  fs.writeFileSync(fp, html);
  console.log('✓', file);
}
```

The "safer minimum" approach (append at the end of the last `<style>`) works because the extracted block uses `!important` on its overrides — it'll win the cascade even if Codex's older variant is still upstream. Use that if surgical excision is risky.

### 1.3 Phase 8 verification

```bash
# Computed sidebar background should match across all pages (modulo body-color variance)
cd /tmp && node -e "
const puppeteer = require('puppeteer-core');
(async () => {
  const browser = await puppeteer.launch({ headless: true,
    args: ['--no-sandbox','--disable-setuid-sandbox','--disable-dev-shm-usage'] });
  const FILES = require('fs').readdirSync('mockup_final').filter(f => f.endsWith('.html'));
  for (const f of FILES) {
    const page = await browser.newPage();
    await page.goto('file://' + require('path').resolve('mockup_final', f));
    const sbBg = await page.evaluate(() => {
      const sb = document.querySelector('.sidebar');
      return sb ? getComputedStyle(sb).backgroundImage.slice(0, 80) : 'no sidebar';
    });
    console.log(f, '→', sbBg);
    await page.close();
  }
  await browser.close();
})();
"
```

All non-stub pages must report the **same** `backgroundImage` start (the radial-gradient signature from the v0.4 sidebar). If any page still reports `linear-gradient(rgb(19, 31, 24)...` you missed it.

Also visually: open one Tier 2 page (e.g. `clubs.html`) next to `token_list_v4.html` in two browser tabs. Compare the left sidebar pixel-for-pixel — same cream pill nav, same "today's garden" sticker note, same user-card polaroid, same sidebar-footer pills.

---

## 2. Phase 9 — revert Phase 7 polaroid where tier ≠ 1, then apply tier CSS

### 2.1 Find and remove Phase 7 polaroid CSS where it shouldn't be

For every page **except `token_list_v4.html`, `create_token.html`, `trading_panel.html`**:

1. Locate the Phase 7 block in that file:
   ```
   /* === Wild Phase 7 - card polaroidization (added by apply-cards.js) === */
   ...
   /* === end Wild Phase 7 - card polaroidization === */
   ```
2. **Delete** the entire block between (and including) those markers.

After this pass, the only pages still containing Phase 7 polaroid CSS should be: none. Phase 7 will be replaced by the tier-specific CSS from §2.2.

```bash
# Verify Phase 7 block is gone from all pages
grep -l 'Wild Phase 7' mockup_final/*.html
# (expected: no output)
```

### 2.2 Tier CSS recipes (the new application)

Each recipe is **one CSS block to inject just before the last `</style>`** on the page's HTML. Replace `SELECTOR_HERE` with the actual card class.

#### Recipe T1 — Hero polaroid

Same as the WILD_PHASE2.md Type 1 recipe. **Do not re-apply on `token_list_v4.html` and `token_detail.html` if it's already there** — verify first with `grep 'Hero polaroid'`.

Already applied to `.token-card` in the anchor. For `token_detail.html` you need to apply it to:
- `.token-info-card` (Type 1)
- `.trade-card` (Type 1)
- `.trust-card` (Type 1)
- `.chart-card` (Type 3 data-frame — outer polaroid, chart canvas stays dark)
- `.tabs-card` (Type 3 data-frame)

Use the recipes from WILD_PHASE2.md §2.1 verbatim.

#### Recipe T2 — Clean functional dark card

**This replaces the Phase 7 polaroid on Tier 2 pages.** Apply to: `.club-card`, `.ev-card`, `.lb-card-head`, `.history-card`, `.rank-card`.

```css
/* === Wild Phase 9 — Tier 2 clean functional card === */
.SELECTOR_HERE {
  background: var(--surface-1) !important;
  color: var(--text-1) !important;
  border: 1px solid var(--border-1) !important;
  border-radius: var(--r-md) !important;
  padding: 16px !important;
  position: relative !important;
  transition: border-color 0.18s var(--ease), transform 0.18s var(--ease),
              box-shadow 0.18s var(--ease) !important;
  /* clear any leftover Phase 7 ::before washi */
  overflow: hidden !important;
  box-shadow: none !important;
}
.SELECTOR_HERE::before { content: none !important; }
.SELECTOR_HERE:hover {
  border-color: var(--sp-peach-400) !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 8px 20px -8px rgba(232,168,124,0.18) !important;
}

/* Left accent bar (3px peach) — gives the card identity without polaroid */
.SELECTOR_HERE::after {
  content: '' !important;
  position: absolute !important;
  left: 0; top: 14px; bottom: 14px;
  width: 3px !important;
  background: var(--sp-peach-400) !important;
  border-radius: 0 2px 2px 0 !important;
}

/* Title / token name → italic Fraunces peach (this is the wild touch) */
.SELECTOR_HERE [class*='name']:not([class*='sub']),
.SELECTOR_HERE [class*='title']:not([class*='sub']) {
  font-family: var(--font-disp-it) !important;
  font-style: italic !important;
  font-weight: 900 !important;
  color: var(--sp-peach-400) !important;
}

/* Make sure all text is light again (Phase 7 left them as ink) */
.SELECTOR_HERE,
.SELECTOR_HERE p,
.SELECTOR_HERE span:not([class*='btn']):not([class*='badge']):not([class*='delta']) {
  color: var(--text-2) !important;
}
.SELECTOR_HERE [class*='value'], .SELECTOR_HERE [class*='price'] {
  color: var(--text-1) !important;
  font-family: var(--font-mono) !important;
  font-weight: 700 !important;
}

/* Inline delta (e.g. ↑ 38.5%) → teal text, no pill */
.SELECTOR_HERE [class*='delta'], .SELECTOR_HERE [class*='change'] {
  color: var(--sp-teal-400) !important;
  background: transparent !important;
  padding: 0 !important;
  font-family: var(--font-mono) !important;
  font-weight: 600 !important;
}
.SELECTOR_HERE [class*='down'], .SELECTOR_HERE .negative {
  color: var(--sp-crimson) !important;
}
```

Apply once per card class on the page. Comma-separate selectors if multiple classes share the recipe.

#### Recipe T3 — Personal hybrid (one polaroid hero + dark sections)

Apply to `my_profile.html`, `public_profile.html`, `referrals.html`, `edit_profile_privacy.html`.

These pages have a hero block (user identity / referral code / settings header) plus content sections (info table, stats grid, settings rows). Tier 3 = the hero is polaroid, the sections are Tier 2 clean.

**For the hero card** — pick the topmost `.section-card` (the one containing user avatar + name + tier on profile pages, the link-display block on referrals, the page header on settings). Apply **Recipe T1** to it.

**For the rest of the cards** — apply Recipe T2 to `.section-card` (excluding the hero by `:not(:first-of-type)`) and `.stat-card`.

```css
/* === Wild Phase 9 — Tier 3 personal hybrid === */
/* (a) First .section-card on the page is the hero — keep Tier 1 treatment */
.section-card:first-of-type {
  /* paste Recipe T1 polaroid body here with class .section-card:first-of-type */
}
/* (b) Other section-cards + stat-cards revert to Tier 2 clean */
.section-card:not(:first-of-type),
.stat-card {
  /* paste Recipe T2 dark-card body here */
}
```

Note `:first-of-type` only matches the first within a parent — confirm with the actual DOM. If the hero is identified by a different class (e.g. `.section-card.hero`), use that instead.

#### Recipe T4 — Form polaroid

Already applied on `create_token.html` via the existing `.form-container` polaroid. For `trading_panel.html`, the buy/sell form panel is already cream paper. **No change needed for Tier 4 pages** — just verify with screenshots that they still look polaroid (Phase 7 may have removed earlier rules).

#### Recipe T5 — Hybrid mixed (creator_dashboard)

Apply to `.metric-card` and `.stat-card` in `creator_dashboard.html`:

Use the WILD_PHASE2.md Type 2 stat-card mini polaroid recipe.

Any chart container inside a stat — let the chart canvas stay `var(--surface-1)` so the line data is legible. The outer card is cream paper, the inner chart is dark. Same pattern as Type 3 data-frame.

#### Recipe T6 — Spec doc

`FR-012_TokenWar.html` and `FR-012b_TokenWar_PredictionMarket.html` are documentation / spec pages, not real product UI. They have prose with Vietnamese explanations + code blocks + comparison tables.

Apply this minimal treatment — keep everything dark but Wild-tune the typography:

```css
/* === Wild Phase 9 — Tier 6 spec doc === */
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

/* The Phase 7 polaroid arena-card was incorrect here — undo it */
.arena-card {
  background: var(--surface-1) !important;
  color: var(--text-1) !important;
  border: 1px solid var(--border-1) !important;
  border-radius: var(--r-md) !important;
  padding: 16px !important;
  box-shadow: none !important;
}
.arena-card::before { content: none !important; }
```

### 2.3 Per-page assignments (authoritative)

This supersedes the WILD_PHASE2.md §2.2 table for Phase 9. Use it as the single source of truth.

| Page | Tier | Apply to |
|------|------|----------|
| `token_list_v4.html` | T1 | `.token-card` (already there — verify, don't re-apply) |
| `token_detail.html` | T1 + T3 dataframe | `.token-info-card` T1 · `.trade-card` T1 · `.trust-card` T1 · `.chart-card` Type 3 data-frame · `.tabs-card` Type 3 data-frame |
| `clubs.html` | T2 | `.club-card` + `.pod-card` |
| `events.html` | T2 | `.ev-card` |
| `leaderboard.html` | T2 | `.lb-card-head` |
| `rewards.html` | T2 | `.history-card` · `.reels-card` |
| `points.html` | T2 | `.history-card` · `.rank-card` |
| `my_profile.html` | T3 | `.section-card:first-of-type` → T1 · the rest of `.section-card` + `.stat-card` → T2 |
| `public_profile.html` | T3 | Same as my_profile |
| `referrals.html` | T3 | `.link-card` → T1 · `.stat-card` + `.table-card` → T2 |
| `edit_profile_privacy.html` | T3 | First `.edit-card` → T1 · rest → T2 |
| `create_token.html` | T4 | Already polaroid — verify only |
| `trading_panel.html` | T4 | Already polaroid form — verify only |
| `creator_dashboard.html` | T5 | `.metric-card` + `.stat-card` → mini polaroid (Type 2 from PHASE2) |
| `FR-012_TokenWar.html` | T6 | Apply T6 doc style; undo Phase 7 `.arena-card` polaroid |
| `FR-012b_TokenWar_PredictionMarket.html` | T6 | Apply T6 doc style |
| `sidebar_navigation.html` | n/a | Component preview. Apply Phase 8 sidebar canon, skip card work. |
| `home_full_layout.html` | n/a | Redirect stub. Skip. |

### 2.4 Phase 9 verification

Per page:

```bash
# Phase 7 block gone? (only Tier 1/4 may keep something polaroid-shaped)
grep -L 'Wild Phase 7' mockup_final/*.html
# All except polaroid pages should appear here

# Tier 2 pages: cards are dark surface-1, not cream paper
for f in clubs events leaderboard rewards points; do
  echo -n "$f: "
  grep -aoc '\.club-card[^{]*{[^}]*var(--surface-1)\|\.ev-card[^{]*{[^}]*var(--surface-1)' "mockup_final/$f.html"
done
```

Visually, open every page and confirm:

- **Tier 1**: token_list_v4 + token_detail still loud polaroid.
- **Tier 2**: clubs, events, leaderboard, rewards, points = dark surface cards with 3px left peach bar, italic peach name, mono light prices. No washi tape. No sticker badges. Border-peach on hover.
- **Tier 3**: profile pages have ONE polaroid hero block at the top, everything below is Tier 2 dark.
- **Tier 4**: form pages unchanged from previous polaroid form look.
- **Tier 5**: creator_dashboard stat cards are mini cream polaroids; the dashboard charts are dark inside the polaroid frame.
- **Tier 6**: FR-012 + FR-012b are dark prose with italic peach headings, no polaroid cards.

---

## 3. Phase 10 — Live Activity on `token_detail.html`

The team decided LA panel stays on token_list_v4 but **also goes on token_detail**, filtered to show activity for the current token only.

### 3.1 Copy the LA panel HTML from `token_list_v4.html`

In `token_list_v4.html`, the LA HTML lives between:

```
<!-- ╔══════ v0.7 LIVE ACTIVITY right panel ══════╗ -->
<aside class="live-activity" id="liveActivity">
  ...
</aside>
<script>
  // pool of mock items, setInterval push new one every 8s
</script>
<!-- ╚══════ end LIVE ACTIVITY ══════╝ -->
```

Copy that whole block into `token_detail.html`, place it just before `</body>`.

### 3.2 Filter the mock pool to one token

In the script `pool` array inside the copied block, change the entries so every mock entry references the token shown on the detail page. For `token_detail.html` the team uses **Moon Token / MOON** as the example token. Replace all `token: '...'` values with `'MOON'`.

Original (token list shows variety):

```js
const pool = [
  { n:'@whale_max',   v:'buy',  vt:'bought',    tk:'MOON',     a:'+8.4 SOL',  ac:'up',   c:'#7cc4a4,#3d7458' },
  { n:'@charlie',     v:'sell', vt:'sold',      tk:'FIRE094',  a:'-1.1 SOL',  ac:'down', c:'#d65a54,#b94842' },
  { n:'@whale_zen',   v:'buy',  vt:'bought',    tk:'PUMP',     a:'+25 SOL 🐋',ac:'up',   c:'#d4a256,#8a5e1e' },
  { n:'STAR023',      v:'grad', vt:'graduated', tk:'',         a:'to DEX 🌳', ac:'',     c:'#f4cba0,#e8a87c' },
];
```

Detail page (filtered to MOON):

```js
const pool = [
  { n:'@whale_max',     v:'buy',  vt:'bought',    tk:'MOON', a:'+8.4 SOL',  ac:'up',   c:'#7cc4a4,#3d7458' },
  { n:'@diamondhands',  v:'buy',  vt:'bought',    tk:'MOON', a:'+12 SOL 🐋',ac:'up',   c:'#e8a87c,#d68a5b' },
  { n:'@apewhale',      v:'sell', vt:'sold',      tk:'MOON', a:'-3.5 SOL',  ac:'down', c:'#d65a54,#b94842' },
  { n:'@solana_bull',   v:'buy',  vt:'bought',    tk:'MOON', a:'+1.8 SOL',  ac:'up',   c:'#9ed8b8,#5ba886' },
];
```

Also rewrite the static 9 initial `.la-item` entries at the top of the panel so they're all MOON-token activity. Same logic — change the token chip in each `<div class="la-body">…<span class="la-token">…` to `MOON`.

Update the panel header:

```html
<div class="la-header"><span class="la-pulse"></span>Live · MOON token</div>
<div class="la-subhead">recent moves on this token</div>
```

### 3.3 Phase 10 verification

```bash
grep -c '<aside class="live-activity"' mockup_final/token_detail.html  # = 1
grep -c '<aside class="live-activity"' mockup_final/token_list_v4.html # = 1
# No other pages have LA panel:
for f in $(ls mockup_final/*.html); do
  c=$(grep -c '<aside class="live-activity"' "$f")
  if [ "$c" -gt 0 ] && [[ "$f" != *token_list_v4* ]] && [[ "$f" != *token_detail* ]]; then
    echo "STRAY LA: $f"
  fi
done
```

Visually: open token_detail and confirm the LA panel is docked on the right; all entries say `MOON`; the header reads `Live · MOON token`.

---

## 4. Update the report

Append to `mockup_final/WILD_APPLY_REPORT.md`:

```markdown
## Phase 8 + 9 + 10 — sidebar canon, tier system, LA on detail

### Phase 8 — sidebar consistency
- Extracted canonical sidebar block from `token_list_v4.html` (cream pill v0.4 + v0.5 + v0.6 + v0.8)
- Injected into 15 other pages (excluding token_list_v4 and home_full_layout)
- All pages now render identical sidebar (cream pill nav, sticker icons, today's garden banner, polaroid user-card)

### Phase 9 — tier system
- Removed Phase 7 polaroid CSS from 12 pages
- Re-applied per tier:
| Page | Tier | Cards touched |
| ... |

### Phase 10 — LA on token_detail
- Copied LA panel from token_list_v4
- Filtered mock pool to MOON token
- Header updated: "Live · MOON token"

## Resolved questions
- Sidebar variant: cream pill (gold reference) — applied consistently across all pages.
- Tier system: 4 main + 2 special tiers (T5 hybrid, T6 spec).
- LA scope: token_list_v4 + token_detail (with per-page contextual filtering).

## Remaining open
- Mascot mobile threshold: still 900px hide. Team has not objected since Phase 1 — assumed accepted.
```

---

## 5. DON'T

- **Don't undo** the `.token-card` polaroid on `token_list_v4.html`. It's the hero — that's the look every other page is now arranging around.
- **Don't apply** Tier 1 polaroid to a Tier 2 card class even if "polaroid would look nice here." Visual hierarchy is the point.
- **Don't strip emoji again.** After every file write, sanity check:
  ```bash
  grep -c '🌱\|🔥\|💎\|·' mockup_final/<file>.html
  ```
  must be ≥ the pre-edit count. Earlier rounds in this project lost 400 emojis to PowerShell `Set-Content` defaulting to Windows-1252. Use Node fs (UTF-8 default) or `Set-Content -Encoding UTF8NoBOM`. **Never** plain `Set-Content`.
- **Don't merge files** into shared CSS. Each mockup stays standalone.
- **Don't rename classes**, ids, or data-attributes. The fix is CSS overrides only.
- **Don't add LA panel** to any page except `token_list_v4.html` and `token_detail.html`.
- **Don't widen scope** beyond what's in this file. If you discover another inconsistency, write it in §6 of WILD_APPLY_REPORT.md as an open question — don't fix it speculatively.
- **Don't trust the FUSE mount byte count** when copying large files. After every `fs.readFileSync` → `fs.writeFileSync`, verify `dst.length === src.length` (see WILD_PHASE2.md §1 for the truncation history).

---

## 6. Order of operations

Don't interleave. Do them in this order:

1. **Phase 8 first.** Sidebar parity. Verify with `getComputedStyle` script in §1.3. If anything still reports the wrong `backgroundImage`, fix before moving on.
2. **Phase 9 next.** Remove Phase 7 blocks, then inject tier-specific CSS per the §2.3 assignment table. Verify per-tier visually before moving on.
3. **Phase 10 last.** Copy LA, filter pool, update header. Lowest-risk step; do it after the larger refactors are stable.
4. Re-run `_codex_tools/verify.js` to regenerate all screenshots.
5. Append to WILD_APPLY_REPORT.md (§4 template).

Begin at §1.1.
