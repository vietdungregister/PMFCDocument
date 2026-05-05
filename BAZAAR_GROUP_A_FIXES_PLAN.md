# Bazaar Group A Fixes — Implementation Plan

> **For:** Antigravity AI agent (or any executing agent)
> **Created:** 2026-05-05
> **Estimated effort:** ~1.5h
> **Source spec:** `/BAZAAR_UI_SPEC.md` (already locked with all 5 decisions)

---

## 0. Mission

Fix 5 design polish issues in `/mockups-bazaar/` so the Bazaar theme is solid for team pitch. **Decisions are already locked in `BAZAAR_UI_SPEC.md`** — this plan tells you exactly what to change in code to match the spec.

**Do NOT make new design decisions.** If you find yourself wanting to invent something, STOP and ask the user.

**Do NOT touch:** mobile responsive, accessibility (touch targets, color contrast), Sprout files (`/mockups-sprout/`), Sprout mood demos (`/mockups-sprout/_mood_demos/`). Scope is Bazaar Group A only.

---

## 1. Pre-flight (read these BEFORE editing)

1. `/BAZAAR_UI_SPEC.md` — sections 1.1, 1.5, 4.4, 4.7, 5.4b, and changelog entry "2026-05-05 (Group A pitch-readiness lock)". These are the locked targets.
2. `/CLAUDE.md` — project context, do not break.
3. `/mockups-bazaar/points.html` — canonical reference for app shell, sidebar, connected wallet state.
4. `/mockups-bazaar/leaderboard.html` — to be modified in Task 2 + Task 3.
5. `/mockups-bazaar/rewards.html` — to be modified in Task 5.
6. `/mockups-bazaar/token_list_v4.html` — to be modified in Task 3.
7. `/mockups-bazaar/token_detail.html` — kept untouched in Task 3 (data tables are NOT here).
8. `/mockups-bazaar/create_token.html` — to be modified in Task 1 (creator funnel hero).

---

## 2. Decisions locked (do not deviate)

Reference `/BAZAAR_UI_SPEC.md` for full rationale. Summary:

| # | Decision | Source |
|---|---|---|
| 1 | Tagline split: hero = "Trade memes at the bazaar." / creator funnel = "Open a stall. Pitch your meme." / drop "Open a stall. Trade memes." everywhere | Spec section 1.1 |
| 2 | Mascot sizing tokens `--mascot-sm: 22px / --mascot-md: 30px / --mascot-lg: 40px`. All `.logo-mascot`, `.user-card-avatar`, `.wc-avatar`, `.lb-rank-avatar` etc. round to nearest token | Spec section 1.5 |
| 3 | Drop "stall by" from data tables (leaderboard rows, token list creator labels). Keep "stall by" only on token detail creator-pitch hero | Spec section 4.4 |
| 4 | Rewards subtitle = "The lucky draw." (was "the lucky vendor draw"). Each reel emoji shows its multiplier label below it | Spec section 4.7 |
| 5 | Leaderboard hierarchy: top-3 cards keep amber name, table rows desaturate creator/owner name to `var(--text-1)` (white) | Spec section 5.4b |

---

## 3. Tasks

### Task 1 — Tagline cleanup (5 files)

**Goal:** replace deprecated compound tagline with surface-specific taglines.

**Search-and-destroy:**
- Find every literal occurrence of `Open a stall. Trade memes.` across `/mockups-bazaar/*.html`.
- For each occurrence, decide replacement based on which surface the file represents:

| File | Surface type | Replacement |
|---|---|---|
| `token_list_v4.html` | Hero / marketing-ish (home) | `Trade memes at the bazaar.` |
| `home_full_layout.html` | Deprecated meta-redirect | If string still present, change to `Trade memes at the bazaar.` |
| `create_token.html` (step 1 subtitle, page subtitle) | Creator funnel | `Open a stall. Pitch your meme.` |
| `creator_dashboard.html` (hero subtitle if present) | Creator funnel | `Open a stall. Pitch your meme.` |
| Any other file containing the old tagline | Default to hero version | `Trade memes at the bazaar.` |

**Verification:**
```bash
cd /Users/duongvietdung/Documents/Projects/PMFCDocument
grep -rn "Open a stall. Trade memes." mockups-bazaar/
# expected: 0 matches
grep -rn "Trade memes at the bazaar." mockups-bazaar/
# expected: ≥1 match
```

**Don't touch:** marquee text `"OPEN A STALL · TRADE MEMES · ..."` — that's marquee voice, allowed by spec section 4.2 (different surface from tagline). Only tagline-prose surfaces are in scope.

---

### Task 2 — Mascot sizing tokens (all 18 files)

**Goal:** replace arbitrary mascot SVG dimensions with the 3 locked tokens.

**Step 2a — Add the tokens to canonical CSS:**

Each file's `:root { … }` block currently has `--header-h`, `--marquee-h`, `--sidebar-w` etc. Add these 3 new lines after `--sidebar-w: 240px;`:

```css
--mascot-sm: 22px;
--mascot-md: 30px;
--mascot-lg: 40px;
```

**Step 2b — Replace arbitrary px in mascot-bearing rules:**

Find every CSS rule that sets width/height on a mascot SVG container. Common selectors:

- `.logo-mascot` (header logo) — currently 34px → change to `var(--mascot-lg)` and adjust internal SVG `width: 26px` → keep proportional (26/34 ≈ 0.76, so on 40px container use 30px SVG). Concretely: if `.logo-mascot { width: 34px; height: 34px; }` → change to `var(--mascot-lg)` and make `.logo-mascot svg { width: 30px; height: 30px; }`.
- `.wc-avatar` (connected wallet avatar) — currently 28px → `var(--mascot-md)`.
- `.user-card-avatar` (sidebar bottom user card) — varies → round to nearest token.
- `.lb-rank-avatar` or similar (leaderboard rank cards) — round to nearest token.
- `.profile-avatar` if it embeds mascot — round to nearest token.

**Rounding rule (from spec):** 24→22 (sm), 26→30 (md), 28→30 (md), 32→30 (md), 34→40 (lg), 36→40 (lg).

**Where to find candidates:**
```bash
grep -rn "width: 2[2-9]px\|width: 3[0-9]px\|width: 40px" mockups-bazaar/ | grep -i "mascot\|avatar\|logo"
```

**Verification:**
```bash
# After fix, no mascot/avatar element should have a non-token width
grep -rn "\.logo-mascot\s*{" mockups-bazaar/ -A 3 | grep "width:.*px"
# Should only see "var(--mascot-*)" or no px hardcode in mascot rules
```

**Caveat:** if a single CSS file has multiple `.logo-mascot { … }` blocks (one canonical + one override), reconcile to a single declaration using the token. Don't introduce regressions in visual size — visually 34→40 should look almost identical (4px diff is subtle), but VERIFY by opening file in browser.

---

### Task 3 — Drop "stall by" from data tables (2 files primarily)

**Goal:** "stall by" lives only on token detail creator-pitch hero. Data tables use plain "by alice" or just "alice".

**Files to modify:**

**3a. `/mockups-bazaar/leaderboard.html`:**

Find the table row creator/owner column. Look for patterns like:
- `<td class="lb-row-name">stall by alice</td>` → change to `<td class="lb-row-name">by alice</td>` or `<td class="lb-row-name">alice</td>` (use the form already used in the table — check current code, pick consistent form).
- Top-3 cards: KEEP `stall by alice` IF the top-3 card is hero-styled (creator pitch). Otherwise ALSO drop. Decision: keep on top-3 (these are featured, not data), drop on table rows 4+.

Concretely: in the table `<tbody>` rows, replace `stall by ` with empty string (or `by `) in the creator/owner column. Keep top-3 podium cards as-is.

**3b. `/mockups-bazaar/token_list_v4.html`:**

Find token cards' creator label. Look for patterns:
- `<div class="token-creator">stall by 7xK9…mP3q</div>` → change to `<div class="token-creator">by 7xK9…mP3q</div>`
- Apply across all card instances.

**3c. Don't touch:**
- `/mockups-bazaar/token_detail.html` — the creator-pitch hero (Stall story callout) keeps "stall by alice · Local tier · 12d ago". This is the spec-blessed surface.
- `/mockups-bazaar/creator_dashboard.html` — first-person framing "Your stall · alice" or similar.

**Verification:**
```bash
# Should only appear in token_detail.html (and maybe creator_dashboard for "Your stall")
grep -rn "stall by" mockups-bazaar/
# Expected files: token_detail.html only (plus possibly creator_dashboard if it uses "Your stall · alice")
# leaderboard.html and token_list_v4.html should have ZERO "stall by"
```

---

### Task 4 — Rewards subtitle + reel labels

**File:** `/mockups-bazaar/rewards.html`

**4a. Subtitle text:**
- Find `the lucky vendor draw` (or `Lucky vendor draw`, `lucky vendor draw` — case variants).
- Replace with `The lucky draw.` (capital T, period at end).

**4b. Reel emoji multiplier labels:**

Find the slot reels component. Each reel cell currently displays just an emoji (🪙💰💎🏆👑 etc.). Add a small `<span class="reel-multiplier">×N</span>` directly under each emoji:

```html
<!-- Before -->
<div class="reel-cell">🪙</div>

<!-- After -->
<div class="reel-cell">
  🪙
  <span class="reel-multiplier">×1</span>
</div>
```

Multiplier mapping (from spec section 4.7):
- 🪙 ×1
- 💰 ×2
- 💎 ×3
- 🏆 ×4
- 👑 ×5

CSS for the new label (add to the file's `<style>`):
```css
.reel-multiplier {
  display: block;
  font-family: var(--font-mono, 'JetBrains Mono', monospace);
  font-size: 10px;
  font-weight: 700;
  color: var(--bz-amber-400);
  margin-top: 2px;
  letter-spacing: 0.05em;
}
```

**Verification:**
- Open `rewards.html` in browser. Each reel cell shows emoji + small "×N" amber label.
- `grep -n "lucky vendor" mockups-bazaar/rewards.html` → 0 matches.
- `grep -n "The lucky draw" mockups-bazaar/rewards.html` → ≥1 match.

---

### Task 5 — Leaderboard visual hierarchy

**File:** `/mockups-bazaar/leaderboard.html`

**Goal:** top-3 podium cards keep amber for token/creator name. Table rows desaturate to white.

**5a. Identify the table row name selector:**

Likely classes: `.lb-row-name`, `.lb-row-token`, `.lb-table-row .name`, or similar. Inspect the file to find the actual class.

**5b. Change color rule:**

Currently the rule probably looks like:
```css
.lb-row-name {
  color: var(--bz-amber-400);
  ...
}
```

Change to:
```css
.lb-row-name {
  color: var(--text-1);
  ...
}
```

**5c. Keep top-3 untouched:**

Top-3 podium card name selector (likely `.lb-token-name`, `.lb-rank-card .name`, or `.lb-podium-name`) should retain `var(--bz-amber-400)`. Verify by inspecting the existing CSS.

**5d. Optional: rank number column:**

If the table also colors the rank `#` column in amber, desaturate to `var(--text-2)` per spec section 5.4b. This is a nice-to-have, not mandatory.

**Verification:**
- Open `leaderboard.html`. Top-3 podium cards: token/creator name in amber. Table rows 4+: token/creator name in white.
- Visual contrast between podium and roster is clear.

---

## 4. Cross-task verification (run after all 5 tasks done)

### 4a. Spec compliance grep checks

```bash
cd /Users/duongvietdung/Documents/Projects/PMFCDocument

# Tagline cleanup
echo "[Task 1] Old tagline residue:"
grep -rn "Open a stall. Trade memes." mockups-bazaar/ || echo "  ✓ none"

echo "[Task 1] New hero tagline present:"
grep -rln "Trade memes at the bazaar." mockups-bazaar/ || echo "  ✗ MISSING"

# Mascot tokens declared
echo "[Task 2] --mascot-md token declared:"
grep -rln "\-\-mascot-md:" mockups-bazaar/ | wc -l
# Expected: 18 (one per file)

# stall by purged from data
echo "[Task 3] 'stall by' residue in data files:"
grep -rln "stall by" mockups-bazaar/leaderboard.html mockups-bazaar/token_list_v4.html || echo "  ✓ none in data files"

# Rewards
echo "[Task 4] Old rewards subtitle:"
grep -n "lucky vendor" mockups-bazaar/rewards.html || echo "  ✓ removed"

echo "[Task 4] New rewards subtitle:"
grep -n "The lucky draw" mockups-bazaar/rewards.html || echo "  ✗ MISSING"

echo "[Task 4] Reel multiplier labels:"
grep -c "reel-multiplier" mockups-bazaar/rewards.html
# Expected: ≥5 (one per reel emoji × 5 reels = could be 25+)
```

### 4b. Visual smoke test

Open these files in browser and eyeball:
1. `token_list_v4.html` — hero tagline reads "Trade memes at the bazaar.", token cards say "by alice" not "stall by alice".
2. `create_token.html` — step 1 subtitle reads "Open a stall. Pitch your meme."
3. `leaderboard.html` — top-3 podium names amber, table row names white.
4. `rewards.html` — page subtitle "The lucky draw.", each reel cell shows emoji + small ×N amber label below.
5. `token_detail.html` — creator-pitch hero still reads "stall by alice · Local tier · 12d ago" (intentionally untouched).

### 4c. No regressions check

- All 18 files still load without console errors.
- Sidebar navigation between pages still works (links from points.html → token_list_v4.html etc.).
- Connected wallet state still renders on every file with sidebar.
- No raw amber `#EAB552` literal hex introduced (use the CSS var).

---

## 5. Constraints & non-goals

**MUST NOT:**
- Change Sprout files (`/mockups-sprout/*`).
- Change Bazaar functional behavior (Buy/Sell, Trust Score, Trade panel — these are core trading UI per 3-layer principle).
- Introduce new colors, new fonts, new components.
- Modify the marquee text "OPEN A STALL · TRADE MEMES · ..." — marquee voice is intentional, separate surface from tagline prose.
- Modify FRD files (`/docs/FR-*.md`).

**MAY:**
- Run a CSS formatter to keep diffs clean (Prettier with project config if exists).
- Add a brief HTML comment near major change points (e.g. `<!-- Group A fix 2026-05-05: tagline -->`) IF helpful for future agent. Keep comments terse, don't over-document.

---

## 6. Commit message format (if using git)

One commit per task is preferred for review:

```
bazaar: tagline split (hero vs creator funnel) [Group A #1]

- Replace "Open a stall. Trade memes." with surface-specific taglines
- Hero/marketing surfaces: "Trade memes at the bazaar."
- Creator funnel surfaces: "Open a stall. Pitch your meme."
- Rationale: 95% buyer audience needs buyer-first hero
- Spec: BAZAAR_UI_SPEC.md section 1.1 (locked 2026-05-05)
```

```
bazaar: mascot sizing tokens [Group A #2]
bazaar: drop "stall by" from data tables [Group A #3]
bazaar: rewards subtitle + reel multiplier labels [Group A #4]
bazaar: leaderboard top-3 vs roster hierarchy [Group A #5]
```

---

## 7. When done

1. All grep verifications in section 4a pass.
2. Manual visual smoke test (section 4b) passes.
3. No regressions (section 4c).
4. Update `/BAZAAR_UI_SPEC.md` section 12 (changelog) with a new entry: "2026-05-XX — Group A fixes implemented per BAZAAR_GROUP_A_FIXES_PLAN.md. All 5 tasks pass verification."
5. Report back to user with: files modified count, grep verification output, any edge cases encountered.

---

## 8. Edge cases to watch

- **Multiple `:root` blocks:** if a file accidentally has 2 `:root` declarations (defensive duplicate or merge artifact), add `--mascot-*` to the FIRST one only. Don't duplicate.
- **Inline SVG with hardcoded width attributes:** mascot SVGs may have `width="34"` as an attribute on the `<svg>` element itself, not just CSS. Check and update to match container size after token swap.
- **Top-3 vs table styling shared selector:** if `.lb-row-name` is reused for both top-3 and table rows (bad CSS), refactor to two separate classes (`.lb-podium-name` for top-3, `.lb-row-name` for table) before applying color rule.
- **Rewards reel structure varies:** if reel cells use `<img>` for emoji or background-image, adapt the multiplier-label injection accordingly. The label should appear directly under each visual symbol, not floating elsewhere.
- **Tagline appears in `<title>` or `<meta>`:** check `<title>Stallspot — Token List V4</title>` etc. Don't change the page title; it's not the tagline. Only change tagline prose in body content.

---

## 9. Estimated breakdown

| Task | Effort | Risk |
|---|---|---|
| 1. Tagline cleanup | 15 min | Low — pure search/replace |
| 2. Mascot sizing tokens | 25 min | Medium — 18 files, must verify visual |
| 3. Drop "stall by" data tables | 15 min | Low — string replace |
| 4. Rewards subtitle + reel labels | 25 min | Medium — HTML structure change |
| 5. Leaderboard hierarchy | 10 min | Low — single CSS rule |
| Verification | 15 min | — |
| **Total** | **~1h45m** | — |

---

**End of plan.** Reach out to user via the chat (do NOT make new design decisions silently) if you encounter ambiguity. The spec is your single source of truth.
