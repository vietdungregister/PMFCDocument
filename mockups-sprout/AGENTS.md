# AGENTS.md — Sprout Wild Theme Application

You are an AI coding agent (Codex). Your job is to apply the **"Wild" visual theme** uniformly to all 18 mockup HTML files in this folder.

This document is your starting point. Read it fully, then read the linked references, then execute the work plan in order.

---

## 0. Output location — read this first

**Do NOT modify any file in this folder (`mockups-sprout/`) directly.** The originals must stay untouched as a safety baseline.

Create a sibling subfolder `mockup_final/` inside `mockups-sprout/` and put **all** of your output there:
- The 18 modified `.html` files
- The `_codex_tools/` scripts
- The `_codex_screenshots/` images
- The final `WILD_APPLY_REPORT.md`

When the work plan says "fix this file" or "overwrite this file", read it as **"copy the original from `./` to `./mockup_final/`, then apply edits there"**.

If `./mockup_final/` already exists when you start, ask the user before continuing (don't blow away prior work).

---

## 1. Project context (60-second read)

**Sprout** = a meme token platform on Solana (think pump.fun + community/garden theme). Tagline: "the meme garden". The brand voice plays on garden / plant / harvest metaphors ("plant your seed", "tallest tree wins", "graduate to DEX").

This folder (`mockups-sprout/`) holds **18 standalone HTML mockup files** representing different screens (token list, detail, dashboard, profile, leaderboard, etc.). Each file is **fully self-contained** — its own `<style>` block, its own `<script>`, no shared CSS/JS file. Stack is HTML + inline CSS + vanilla JS. **No framework, no bundler.**

The screens were originally built with a darker, more restrained "Mood B Living Garden" treatment. After a long design conversation with the product owner, the team chose a new direction called **"Wild"**: cream polaroid cards on a dark forest background, washi tape, sticker badges, italic display serif (Fraunces) and handwritten (Caveat) fonts mixed with the original Inter / Plus Jakarta Sans / JetBrains Mono. The full visual target is a single reference file (see §2).

Your job: make every other screen look like it lives in the same product as the reference.

---

## 2. Required reading (do this FIRST, before any edits)

These files are NOT in this folder — they live in a sibling workspace folder. Read them carefully before starting.

| # | File | Why |
|---|------|-----|
| 1 | `../Sửa giao diện html/token_list_v4_wild.html` | **Gold reference.** This is the canonical Wild treatment. Open it in a browser (any modern browser, no server needed). This is what every other screen should "rhyme with". |
| 2 | `../Sửa giao diện html/sprout-ui-audit.html` | Audit of existing files: tech stack, file inventory, design tokens, **5 files with broken CSS variables** (you must fix these). Read sections 3, 4, 5, 6 closely. |
| 3 | `./WILD_THEME.md` | Design system reference — every CSS token + component pattern + copy-paste-ready code block you need. **This is your cheat sheet.** |

You may also `cat` (or Read) the existing files in this folder before modifying them to understand their current structure. Don't skip this — some files have domain-specific components (trading panel, prediction market) that need careful preservation of behavior.

---

## 3. Mental model — Wild theme philosophy

Three rules you must internalize before writing CSS:

1. **Hero content = cream polaroid, chrome = dark forest.**
   Token cards, detail pages, "the thing the user came for" → cream paper polaroid with washi tape + sticker badges (`#fdf8ec` bg, ink text `#2a1505`).
   Sidebar, header, marquee, panels → dark surface (`#131f18`, `#0a1610`).

2. **Italic Fraunces is for display + branding only.**
   Headlines, token names, button labels, mascot speech. NOT body text. Body stays Inter / Plus Jakarta Sans. Mono for numbers. Caveat for handwritten labels ("today's garden", small captions).

3. **Don't tilt rectangles, do tilt stickers.**
   Cards, buttons, tabs are **straight (0°)**. Only stickers (washi tape, sticker badges, NEW badge) get a slight rotation (±3° max). This was a hard-learned lesson — earlier iterations tilted everything and it felt like a game. Don't repeat that.

---

## 4. Tools

You have a normal Linux shell. Useful things:
- `cat`, `head`, `tail`, `wc -l` for inspecting files
- `grep -n` for finding selectors / class names
- A `sed -i` / `awk` pass can speed up token migration across many files
- For verification: install `puppeteer-core` + a headless Chromium and screenshot before/after. Example one-liner is in `WILD_THEME.md` §11.

Do not install npm packages globally. Use a local `node_modules/` under a `_codex_tools/` subfolder so it doesn't pollute the mockups.

---

## 5. Work plan (4 phases — do in order)

### Phase 1 — Fix the 5 broken files (CSS variables undefined)

The audit (§4.1) lists 5 files where CSS uses tokens like `var(--card)`, `var(--primary)`, `var(--text-primary)` that **were never declared**, so the page renders broken (no card background, wrong color, missing borders). Fix these FIRST so you have a working baseline.

For each of:
- `sidebar_navigation.html`
- `creator_dashboard.html`
- `trading_panel.html`
- `FR-012b_TokenWar_PredictionMarket.html`
- `token_detail.html`

…do the **alias approach** (safer than search-and-replace): append the alias block from `WILD_THEME.md` §2 to the `:root` of each file. This declares `--card`, `--primary`, etc. as pointing to the new tokens (`--surface-1`, `--sp-peach-400`, etc.), so the broken references resolve without you touching the existing CSS rules.

`FR-012b_TokenWar_PredictionMarket.html` additionally is missing the core token `--bg` — copy the full `:root` block from `WILD_THEME.md` §1 into it.

**Exit criteria for Phase 1:** every file opens in a browser with no `var(--undefined)` issues. Visually they still look like the OLD Mood B treatment — that's fine for now. Phase 2 changes the look.

### Phase 2 — Treat the gold reference as truth

`./token_list_v4.html` is the **original** version of the trending list page. The **Wild-styled** version lives at `../Sửa giao diện html/token_list_v4_wild.html`.

Copy `../Sửa giao diện html/token_list_v4_wild.html` to `./mockup_final/token_list_v4.html`. (Use `cp` or read+write.)

After this:
- Open both `./mockup_final/token_list_v4.html` and `../Sửa giao diện html/token_list_v4_wild.html` — they should be byte-identical.
- This is now your "anchor" screen. Every other screen in `mockup_final/` must look like it belongs in the same product.

### Phase 3 — Roll Wild theme out to the other 12 functional screens

For each of the screens listed in §6 below, follow the **per-file recipe** noted in the table. The shared pattern is:

1. **Replace the `:root` block** with the Wild tokens from `WILD_THEME.md` §1. Keep any file-specific tokens that aren't conflicting.
2. **Replace the `body { ... }` rules** with the Wild body style (`WILD_THEME.md` §3) — dark mesh background.
3. **Replace the marquee block** (`.marquee`, `.marquee-track`) — `WILD_THEME.md` §4.
4. **Replace the sidebar block** (`.sidebar`, `.nav-item`, `.user-card`, `.sidebar-footer`) — `WILD_THEME.md` §5. **Note**: the team has NOT chosen between two sidebar variants (current cream-pill vs. flat-dark Option A). Use the **current cream-pill version** by default. See §9 below.
5. **Replace the header block** (if file has one) — `WILD_THEME.md` §6.
6. **For pages with token cards / lists** (token list, leaderboard, rewards, clubs, events): apply the polaroid card treatment from `WILD_THEME.md` §7 and inject sticker badges via JS (`WILD_THEME.md` §7d).
7. **For form pages** (create_token, edit_profile_privacy): apply Wild form inputs from `WILD_THEME.md` §8.
8. **For detail / dashboard pages with stats and charts** (token_detail, creator_dashboard, trading_panel, my_profile, public_profile, points): apply Wild stat-card treatment from `WILD_THEME.md` §9.
9. **Universally** add the Mascot Character + Chat affordance from `WILD_THEME.md` §10 to every functional screen (NOT to redirect stubs).
10. **Live Activity panel** (`WILD_THEME.md` §11) belongs ONLY on the trending list page (`token_list_v4.html`). Do not add it to other screens.
11. **Preserve every page's own logic.** Existing `id`s, `data-*` attributes, `onclick` handlers, fetch calls — don't rename or remove them. The theme is a visual swap, not a refactor.

### Phase 4 — Cross-cutting fixes

After Phase 3, run a pass over all 18 files:

- **Viewport meta**: 14 files are missing `<meta name="viewport" content="width=device-width, initial-scale=1.0">`. Add it to every file that doesn't have it.
- **`<html lang>` standardization**: pick `vi` (the team is Vietnamese-speaking) and apply to all.
- **Placeholder `href="#"`** in sidebar nav items: replace with the correct target HTML file name based on the nav label. (e.g. "Arena" → `FR-012_TokenWar.html`, "My Profile" → `my_profile.html`.)

### Phase 5 — Verify + report

For each file:
1. Open it in headless Chromium.
2. Take a desktop screenshot (1440×900) and a mobile screenshot (390×844).
3. Check the browser console for errors (`page.on('pageerror', ...)`).
4. Confirm the screenshot visibly matches the gold reference style (cream polaroid cards for content, dark sidebar, sticker treatment).

Write `WILD_APPLY_REPORT.md` in this folder summarizing:
- Files modified (with diff line counts)
- Files skipped and why (e.g. `home_full_layout.html` is a 0-second meta-refresh redirect, no UI to theme — just add viewport meta)
- Screenshots index (paths to before/after pairs)
- Any blocker or open question

---

## 6. Per-file work plan

Notation: ✱ = critical-broken (Phase 1), ★ = anchor (Phase 2), ✓ = standard Wild roll-out (Phase 3), • = stub / minimal change (Phase 4 only).

| # | File | Type | What to do |
|---|------|------|------------|
| 1 | `home_full_layout.html` | • redirect stub | Add viewport meta. Nothing else (it's a 0-second `meta refresh` → `token_list_v4.html`). |
| 2 | `token_list_v4.html` | ★ anchor | Overwrite with `../Sửa giao diện html/token_list_v4_wild.html`. |
| 3 | `token_detail.html` | ✱ → ✓ | Phase 1: alias 2 missing tokens (`--crimson-soft`, `--teal-soft`). Phase 3: apply Wild detail page — polaroid hero card with token icon + name in italic Fraunces, sticker "GOLD/SILVER/BRONZE" trust badge, dark sidebar, Wild buttons. Chart container becomes cream paper panel with washi tape on top. |
| 4 | `trading_panel.html` | ✱ → ✓ | Phase 1: alias all 10 legacy tokens (`--card`, `--card2`, `--card-boarder`, `--card-hover`, `--primary`, `--primary-hover`, `--accent`, `--danger`, `--danger-hover`, `--text-primary/secondary/tertiary`). Phase 3: apply Wild — dark sidebar; order form panel becomes cream paper polaroid (form inputs stay readable on cream); buy/sell buttons: green polaroid pill for buy, crimson for sell. Order book stays dark (it's high-density data — DO NOT polaroid it, it'd be unreadable). |
| 5 | `creator_dashboard.html` | ✱ → ✓ | Phase 1: alias the 9 legacy tokens + `--danger`. Phase 3: dark sidebar, then each KPI/stat card becomes a small cream polaroid with washi tape + sticker badge ("📈 trending", "🌱 new", etc.). Charts stay on dark surface inside a polaroid frame. |
| 6 | `create_token.html` | ✓ | Wild form treatment: cream paper polaroid form container; input fields with cream bg + ink-color border; submit button = "🌱 Plant a seed" italic Fraunces pill with peach gradient. |
| 7 | `leaderboard.html` | ✓ | Wild leaderboard rows: each row = mini polaroid (cream bg, washi tape on rank #1/2/3, sticker badge "🥇/🥈/🥉"), avatar tròn viền đen, name italic Fraunces, points mono. |
| 8 | `rewards.html` | ✓ | Wild reward cards: each reward = polaroid card with washi tape + sticker badge ("🎁 NEW", "✨ LIMITED"). "Claim" button = green polaroid pill. |
| 9 | `points.html` | ✓ | Big points number in italic Fraunces gradient (sunshine → peach → pink) on dark. History list rows as flat-dark or mini polaroids (your choice — flat is cleaner). |
| 10 | `public_profile.html` | ✓ | Profile hero = big polaroid (avatar + name + tier badge + bio) with washi tape. Tabs (Tokens / Activity / Holdings) as Wild pill chips. Token grid below uses same polaroid treatment as anchor. |
| 11 | `FR-012b_TokenWar_PredictionMarket.html` | ✱ → ✓ | Phase 1: insert the full `:root` block from `WILD_THEME.md` §1 (file is missing `--bg` entirely, body renders white). Phase 3: prediction cards as polaroid with washi tape; YES/NO buttons as green/crimson polaroid pills; odds in mono. |
| 12 | `edit_profile_privacy.html` | ✓ | Wild form: each setting row as a flat dark row; toggle switches stay (current style fine, just retint accent to peach); save button = peach polaroid pill. |
| 13 | `my_profile.html` | ✓ | Same hero treatment as `public_profile.html` but with "Edit" button visible. Tabs identical. |
| 14 | `referrals.html` | ✓ | Referral code display = giant polaroid in center with washi tape and copy-to-clipboard button. Stat cards below (referred count, earnings) as polaroid pills. |
| 15 | `clubs.html` | ✓ | Club cards = polaroid (same shape as token cards), avatar 60×60 viền đen, member count chip, "Join" button as peach polaroid pill. |
| 16 | `FR-012_TokenWar.html` | ✓ | Arena/battle UI: VS layout with two competing tokens as polaroids facing each other. Voting bars in peach gradient. Vote button = polaroid pill. |
| 17 | `events.html` | ✓ | Event cards = polaroid with date sticker top-left (washi tape style), "RSVP" button. List or grid both OK; prefer grid for visual consistency with token list. |
| 18 | `sidebar_navigation.html` | ✱ → • | Phase 1: alias the 9 legacy tokens. Phase 4: this file appears to be a component / template, not a real page. Verify with the user / docs. If it's a component, just sync its sidebar to match the Wild sidebar from `WILD_THEME.md` §5. Do not add header/main/marquee unless the file already had them. |

---

## 7. Definition of done

A file is "done" when **all** of these are true:

- [ ] Opens in a fresh Chrome tab with **zero** browser console errors.
- [ ] No `var(--xyz)` references that resolve to `initial` (i.e. no undeclared tokens).
- [ ] Has `<meta name="viewport" content="width=device-width, initial-scale=1.0">` in `<head>`.
- [ ] Sidebar, header, marquee match the gold reference (`token_list_v4_wild.html`) visually.
- [ ] Page-specific content (form / chart / list) follows the per-file recipe in §6.
- [ ] Mascot character + chat affordance is present at bottom-right (unless explicitly skipped per §6).
- [ ] Cards/items with sticker badges have those badges injected via JS as in the anchor.
- [ ] Existing JS function names, `id`s, and `data-*` attributes are unchanged.
- [ ] Side-by-side screenshot (anchor on left, your file on right) shows consistent visual language.

---

## 8. Constraints — what NOT to do

- **Don't introduce a framework.** No React, Tailwind, Bootstrap, build step. Keep files self-contained HTML+inline CSS+vanilla JS.
- **Don't merge files into shared CSS/JS.** Each mockup file remains independently openable. (If the team later wants to extract a shared `tokens.css`, that's a separate refactor.)
- **Don't rename `id`s, `data-*` attributes, or existing JS function names.** Backend integration hooks may depend on them.
- **Don't delete existing CSS classes** even if they look unused — they may be toggled by JS at runtime.
- **Don't apply polaroid cream to dense data displays** (order books, large tables, dense charts). Cream paper makes mono digit columns hard to read. Keep those on dark surface, wrap them in a polaroid frame only if you need visual separation.
- **Don't add features.** No new pages, no new navigation items beyond what's already in the sidebar HTML. Theme application only.
- **Don't run any sed/regex pass without testing on 1 file first.** A bad regex across 18 files is a long cleanup.

---

## 9. Open decisions

**Resolved before you started:**
- **Sidebar style**: ✅ **cream-pill** (the default in the gold reference). The flat-dark Option A variant at `../Sửa giao diện html/token_list_v4_wild_A.html` is NOT to be used. Do not consider it; do not produce alternative versions.

**Still open — flag in your report, don't decide yourself:**
1. **Mascot helper character on dense screens**: kept by default. If a screen is very dense (`trading_panel.html`, `creator_dashboard.html`) and the mascot blocks important UI on small viewports, you may move it to top-right or hide on `<1100px` viewports — note this choice in your report.

---

## 10. Reporting

When all phases are done, write `mockups-sprout/mockup_final/WILD_APPLY_REPORT.md` with:

```
# Wild theme application — report

## Summary
- Files modified: N / 18
- Files skipped: M (list with reason)
- Total lines changed: X
- Time to verify: Y minutes

## Files
| File | Phase 1 fix | Phase 3 theme | Mascot added | LA added | Screenshot |
| --- | --- | --- | --- | --- | --- |
| token_list_v4.html | n/a | ★ anchor | yes | yes | screenshots/token_list_v4.png |
| ... | | | | | |

## Open questions for the team
1. ...

## Known issues / TODOs
1. ...
```

Place screenshots in `mockups-sprout/mockup_final/_codex_screenshots/` (before + after pairs).

---

## 11. Quick orientation commands

To get oriented fast:

```bash
# See the 18 files and their sizes
ls -la *.html

# See which files have viewport meta
grep -l 'viewport' *.html

# See which files have the broken legacy tokens (audit §4.1)
grep -l '\-\-card\|\-\-primary\|\-\-text-primary' *.html

# Open the gold reference (macOS)
open '../Sửa giao diện html/token_list_v4_wild.html'
# or (Linux)
xdg-open '../Sửa giao diện html/token_list_v4_wild.html'

# Find a CSS selector across all mockups
grep -n '\.token-card' *.html | head
```

---

## 12. If you get stuck

If a screen's existing structure is too different from the gold reference and you can't see a clean mapping, **stop and flag it** in `WILD_APPLY_REPORT.md` under "Open questions for the team" with a screenshot of the current state and a 1-paragraph description of what's ambiguous. Do not invent a treatment for novel UI patterns — wait for design input.

You're ready. Start with §2 (required reading), then §5 phase 1.
