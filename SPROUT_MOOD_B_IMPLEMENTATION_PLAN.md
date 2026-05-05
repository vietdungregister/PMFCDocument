# Sprout Mood B (Living Garden) — Implementation Plan

> **For:** Antigravity AI agent (or any executing agent)
> **Created:** 2026-05-05
> **Estimated effort:** ~3-4h
> **Source spec:** `/SPROUT_UI_SPEC.md` sections 1.3, 1.3a, 1.3b (locked Mood B)

---

## 0. Mission

Apply **Mood B (Living Garden)** signature glow treatment to all 18 Sprout pages in `/mockups-sprout/`. The surface palette is already mostly Mood B (green-tinted twilight `#0a1610`) — what's missing is the **8 signature glow rules** that make Sprout feel "garden alive at night" instead of just "Sprout-colored Bazaar".

**Decisions are already locked in `SPROUT_UI_SPEC.md`** — this plan tells you exactly what CSS to inject. Do NOT make new design decisions.

**Do NOT touch:** Bazaar files (`/mockups-bazaar/`), Sprout mood demos (`/mockups-sprout/_mood_demos/` — preserved as historical reference), FRD files, MVP screenshots.

---

## 1. Pre-flight (read these BEFORE editing)

1. `/SPROUT_UI_SPEC.md` — sections 1.3 (palette), **1.3a (signature glow treatment — THE 8 RULES)**, 1.3b (mood archive), 9 (script integration). Read top to bottom.
2. `/BAZAAR_UI_SPEC.md` — to understand what stays SAME (architecture, components, routing) vs. what's DIFFERENT (surface palette, brand color, glow).
3. `/mockups-sprout/_mood_demos/mood_b_living.html` — **canonical visual reference** for the glow treatment. Open in browser. The glow CSS rules in section 1.3a of the spec are extracted from this file.
4. `/mockups-sprout/token_list_v4.html` and `/mockups-sprout/points.html` — these are already partially Mood B (correct surface palette but missing glow). Use them as the "before" state.
5. `/scripts/clone_to_sprout.py` — the brand-swap script. May need a small refinement (Task 3) but its core logic stays.

---

## 2. Locked palette + glow rules (cite, don't reinvent)

### 2a. CSS variables (must be present in `:root` of every file)

```css
:root {
  /* Surface palette — green-tinted twilight (Sprout signature) */
  --bg:        #0a1610;
  --surface-1: #131f18;
  --surface-2: #1a2a20;
  --surface-3: #243528;
  --border-1:  #1f2d24;
  --border-2:  #2d4234;

  /* Sprout primary — peach */
  --sp-peach-100: #f4cba0;
  --sp-peach-200: #f4c099;   /* glow brighter variant */
  --sp-peach-400: #e8a87c;
  --sp-peach-500: #d68a5b;
  --sp-peach-soft: rgba(232, 168, 124, 0.12);
  --sp-peach-glow: rgba(232, 168, 124, 0.18);

  /* Sprout secondary — forest */
  --sp-forest-300: #5ba886;
  --sp-forest-500: #3d7458;
  --sp-forest-700: #3d7458;
  --sp-cream:     #f4cba0;

  /* Teal — accents */
  --sp-teal-300: #94d6b8;
  --sp-teal-400: #7cc4a4;
  --sp-teal-500: #5ba886;
  --sp-teal-soft: rgba(124, 196, 164, 0.14);
  --sp-teal-glow: rgba(124, 196, 164, 0.22);

  /* Crimson */
  --sp-crimson:  #D65A54;

  /* Text — slightly warmer than Bazaar */
  --text-1: #f5f7f4;
  --text-2: #a3b0a7;
  --text-3: #6f7d74;
  --text-mute: #4a5650;

  /* Mascot tokens (same as Bazaar) */
  --mascot-sm: 22px;
  --mascot-md: 30px;
  --mascot-lg: 40px;
}
```

### 2b. Signature glow CSS (THE 8 RULES — inject into every file)

```css
/* GLOW 1 — body ambient garden glow (2 radial gradients) */
body {
  background: var(--bg);
  background-image:
    radial-gradient(ellipse 800px 400px at 20% 0%, rgba(232,168,124,0.06), transparent 60%),
    radial-gradient(ellipse 600px 400px at 90% 30%, rgba(124,196,164,0.05), transparent 60%);
  background-attachment: fixed;
}

/* GLOW 2 — logo container peach glow + inset highlight */
.logo-mascot {
  background: linear-gradient(180deg, var(--sp-peach-100), var(--sp-peach-400));
  box-shadow: 0 0 24px rgba(232,168,124,0.35), inset 0 1px 0 rgba(255,255,255,0.2);
}

/* GLOW 3 — primary CTA peach glow */
.btn-primary {
  background: linear-gradient(180deg, var(--sp-peach-100), var(--sp-peach-400));
  box-shadow: 0 0 20px rgba(232,168,124,0.30);
}

/* GLOW 4 — marquee accent text-shadow */
.marquee-track .peach { color: var(--sp-peach-200); text-shadow: 0 0 12px rgba(232,168,124,0.4); }
.marquee-track .teal  { color: var(--sp-teal-300);  text-shadow: 0 0 12px rgba(124,196,164,0.4); }

/* GLOW 5 — featured token card radial + bright border */
.token-card.featured,
.tk-card.featured,
.card.featured {
  border-color: rgba(232,168,124,0.55);
  background:
    radial-gradient(ellipse 300px 200px at 100% 0%, rgba(232,168,124,0.10), transparent 70%),
    var(--surface-1);
  box-shadow: 0 0 32px rgba(232,168,124,0.18), inset 0 1px 0 rgba(255,255,255,0.04);
}

/* GLOW 6 — token card hover subtle teal glow */
.token-card:hover,
.tk-card:hover,
.card:hover {
  box-shadow: 0 0 24px rgba(124,196,164,0.08);
  border-color: var(--border-2);
}

/* GLOW 7 — token avatar soft teal halo */
.token-av,
.tk-av {
  box-shadow: 0 0 16px rgba(124,196,164,0.15);
}

/* GLOW 8 — bar fill (progress to DEX) peach inner glow */
.bar-fill {
  background: linear-gradient(90deg, var(--sp-peach-400), var(--sp-teal-400));
  box-shadow: 0 0 10px rgba(232,168,124,0.5);
}
```

### 2c. Glow restraint rule (LOCKED, do NOT violate)

Glow ONLY on the 8 surfaces above. **Never add glow to:**
- Data tables (`<table>`, `.lb-row-*`, leaderboard table rows)
- Sidebar nav items (`.nav-item`, `.sidebar-link`)
- Form inputs (`<input>`, `<textarea>`, `<select>`)
- Dropdowns, modals, tooltips, popovers
- Body text, page titles, section headers
- Status badges (New / Almost graduated / Graduated — these are core, never themed)
- Trust score breakdown
- Trade panel inputs

If you find yourself adding `box-shadow: 0 0 …` to anything not in the 8 list, STOP and ask the user.

---

## 3. Tasks

### Task 1 — Refine canonical files (token_list_v4.html, points.html)

These two are already partially Mood B (correct base palette). Apply the missing glow + palette refinements.

**File 1: `/mockups-sprout/token_list_v4.html`**

3 surgical changes:

**1a. Update `:root` palette to lock 2026-05-05 values:**

Current file has:
```css
--surface-1: #13201a;
--surface-2: #1a2a22;
--surface-3: #23332b;
--border-1:  #1f2a23;
--border-2:  #2a3a30;
```

Change to (more refined Mood B values from spec):
```css
--surface-1: #131f18;
--surface-2: #1a2a20;
--surface-3: #243528;
--border-1:  #1f2d24;
--border-2:  #2d4234;
```

Also update text palette to slightly-warmer values:
```css
--text-1: #f5f7f4;   /* was #f4f4f5 */
--text-2: #a3b0a7;   /* was #a1a1aa */
--text-3: #6f7d74;   /* was #71717a */
--text-mute: #4a5650; /* was #52525b */
```

Add Mascot tokens:
```css
--mascot-sm: 22px;
--mascot-md: 30px;
--mascot-lg: 40px;
```

Update peach palette:
```css
--sp-peach-200: #f4c099;   /* was #e8a87c — needs to be brighter glow variant */
```

Add teal-glow variable:
```css
--sp-teal-300: #94d6b8;    /* was #9ED8B8 — brighter for glow */
--sp-teal-glow: rgba(124, 196, 164, 0.22);
```

**1b. Inject the 8 glow rules** (section 2b above) into the file's `<style>` block. Place AFTER `:root { … }` and BEFORE existing component styles.

**1c. Verify visually:**
Open `/mockups-sprout/token_list_v4.html` in browser. Should see:
- Subtle peach + teal radial glow on body (not solid bg)
- Logo container has peach halo
- Create token CTA has peach halo
- Marquee accent text glows
- Featured "Almost graduated" token card has radial glow + brighter border + outer halo
- Token avatars have soft teal halo
- Bar-fill progress has subtle peach inner glow

If side-by-side with `_mood_demos/mood_b_living.html`, the token_list page should feel like the same atmosphere.

---

**File 2: `/mockups-sprout/points.html`**

Apply same 3 changes (1a, 1b, 1c). Note: points page may not have featured cards / marquee variants — apply only the rules whose selectors are present in the file.

Specifically for `points.html`:
- GLOW 1 (body) — apply
- GLOW 2 (logo) — apply
- GLOW 3 (CTA) — apply
- GLOW 4 (marquee) — apply if marquee present
- GLOW 5 (featured card) — skip if no featured token card on this page
- GLOW 6 (card hover) — apply to whatever generic card class is used (likely `.card` or `.stat-card`)
- GLOW 7 (token avatar) — skip if no token avatar on this page
- GLOW 8 (bar-fill) — apply if there's a tier progress bar (likely YES on points page — it tracks current tier progress)

---

### Task 2 — Generate the remaining 16 Sprout files

Two paths. Pick A (preferred — automated) or B (fallback — manual).

#### Path A: Re-run `clone_to_sprout.py` after refinement

The script `/scripts/clone_to_sprout.py` clones `/mockups-bazaar/*` into `/mockups-sprout/*` with brand swap. Mood B refinements (palette + glow) need to be added to the script's output transform.

**2a. Update the script's `HEX_SWAPS` (preserve surface swaps — Sprout uses green-tinted twilight):**

The current script's `HEX_SWAPS` already contains the 6 surface swaps (`#0a0e1a` → `#0a1610` etc.). KEEP THEM. But refine the values to match locked Mood B (some are slightly off):

```python
# Surface palette swaps — Mood B locked 2026-05-05
HEX_SWAPS_SURFACE = [
    ('#0a0e1a', '#0a1610'),     # bg                                 (already correct)
    ('#131826', '#131f18'),     # surface-1   (was #13201a, refine)
    ('#1a2138', '#1a2a20'),     # surface-2   (was #1a2a22, refine)
    ('#232b46', '#243528'),     # surface-3   (was #23332b, refine)
    ('#1f2640', '#1f2d24'),     # border-1    (was #1f2a23, refine)
    ('#2a3456', '#2d4234'),     # border-2    (was #2a3a30, refine)
]
```

Plus the brand color swaps (amber→peach, brown→forest) stay as-is.

Also add text palette refinements (slightly warmer for Sprout):
```python
HEX_SWAPS_TEXT = [
    ('#f4f4f5', '#f5f7f4'),     # text-1
    ('#a1a1aa', '#a3b0a7'),     # text-2
    ('#71717a', '#6f7d74'),     # text-3
    ('#52525b', '#4a5650'),     # text-mute
]
```

**2b. Add a glow injection step:**

After the script finishes hex/text swaps, add a new step that injects the 8 glow rules into each `<style>` block.

Easiest approach: define the glow CSS as a Python string constant, find the closing `}` of the `:root { … }` block in each output file, and insert the glow CSS right after.

```python
GLOW_CSS = """
/* === Mood B signature glow (locked 2026-05-05, do not modify without spec update) === */
body {
  background: var(--bg);
  background-image:
    radial-gradient(ellipse 800px 400px at 20% 0%, rgba(232,168,124,0.06), transparent 60%),
    radial-gradient(ellipse 600px 400px at 90% 30%, rgba(124,196,164,0.05), transparent 60%);
  background-attachment: fixed;
}
.logo-mascot {
  box-shadow: 0 0 24px rgba(232,168,124,0.35), inset 0 1px 0 rgba(255,255,255,0.2);
}
.btn-primary {
  box-shadow: 0 0 20px rgba(232,168,124,0.30);
}
.marquee-track .peach { color: var(--sp-peach-200); text-shadow: 0 0 12px rgba(232,168,124,0.4); }
.marquee-track .teal  { color: var(--sp-teal-300);  text-shadow: 0 0 12px rgba(124,196,164,0.4); }
.token-card.featured, .tk-card.featured, .card.featured {
  border-color: rgba(232,168,124,0.55);
  background: radial-gradient(ellipse 300px 200px at 100% 0%, rgba(232,168,124,0.10), transparent 70%), var(--surface-1);
  box-shadow: 0 0 32px rgba(232,168,124,0.18), inset 0 1px 0 rgba(255,255,255,0.04);
}
.token-card:hover, .tk-card:hover, .card:hover {
  box-shadow: 0 0 24px rgba(124,196,164,0.08);
}
.token-av, .tk-av { box-shadow: 0 0 16px rgba(124,196,164,0.15); }
.bar-fill { box-shadow: 0 0 10px rgba(232,168,124,0.5); }
/* === end Mood B glow === */
"""

def inject_glow(content):
    """Inject Mood B glow CSS after the first :root {…} block."""
    import re
    pattern = r'(:root\s*\{[^}]*\})'
    match = re.search(pattern, content)
    if match:
        insert_pos = match.end()
        return content[:insert_pos] + '\n' + GLOW_CSS + '\n' + content[insert_pos:]
    return content
```

Call `inject_glow()` after all string swaps and before file write.

**2c. Add mascot sizing tokens:**

Inside the `:root { … }` block of each file, ensure these 3 lines exist (insert after `--sidebar-w: 240px;`):

```css
--mascot-sm: 22px;
--mascot-md: 30px;
--mascot-lg: 40px;
```

If Bazaar files already have these (after `BAZAAR_GROUP_A_FIXES_PLAN.md` Task 2 runs), they'll be cloned automatically. If Bazaar Group A hasn't run yet, the script should inject them as a separate step. Check Bazaar files first:

```bash
grep -c "\-\-mascot-md" /Users/duongvietdung/Documents/Projects/PMFCDocument/mockups-bazaar/token_list_v4.html
# If ≥1: tokens are present in Bazaar, will clone automatically
# If 0: need to inject
```

**2d. Run the script:**

```bash
cd /Users/duongvietdung/Documents/Projects/PMFCDocument
python3 scripts/clone_to_sprout.py
```

The script will overwrite all 18 files in `/mockups-sprout/`. Then **manually re-apply Task 1 refinements** to `token_list_v4.html` and `points.html` because those were hand-tuned. (Or — better — make the script idempotent so it produces identical output regardless of run count.)

#### Path B: Manual edit each of 16 remaining files

If Path A is too complex, fall back to manually applying changes to each file. The list:

```
/mockups-sprout/token_detail.html
/mockups-sprout/trading_panel.html
/mockups-sprout/my_profile.html
/mockups-sprout/public_profile.html
/mockups-sprout/edit_profile_privacy.html
/mockups-sprout/creator_dashboard.html
/mockups-sprout/create_token.html
/mockups-sprout/leaderboard.html
/mockups-sprout/rewards.html
/mockups-sprout/referrals.html
/mockups-sprout/sidebar_navigation.html
/mockups-sprout/FR-012_TokenWar.html
/mockups-sprout/FR-012b_TokenWar_PredictionMarket.html
/mockups-sprout/clubs.html
/mockups-sprout/events.html
/mockups-sprout/home_full_layout.html
```

For each file:
1. Update `:root` palette to locked Mood B values (section 2a).
2. Inject the 8 glow rules (section 2b).
3. Verify visually in browser.

**Recommendation:** start with Path A. Fall back to Path B only if script approach has issues.

---

### Task 3 — Cross-theme parity for Bazaar Group A fixes

Bazaar is being polished in parallel via `/BAZAAR_GROUP_A_FIXES_PLAN.md`. Sprout must mirror those fixes (architecture parity rule from spec):

**3a. Tagline (Sprout's equivalent of Bazaar Task 1):**

Sprout's existing tagline is "Plant your seed in the memeconomy." — keep this for hero, no change needed. But check if Sprout files have a deprecated compound tagline that needs split treatment. Review with user before changing — Sprout tagline split was NOT explicitly locked in spec.

**Decision required from user before this sub-task.** If user hasn't specified, leave Sprout taglines alone for now and flag in your report.

**3b. Mascot sizing tokens (mirrors Bazaar Task 2):**

Same as Bazaar — every Sprout file's `:root` gets `--mascot-sm/md/lg`. Already covered in Task 1 (canonical files) + Task 2 (script). Just verify all 18 files have them.

**3c. "stall by" → "by" (mirrors Bazaar Task 3):**

Sprout doesn't use "stall" metaphor — uses plain "by" attribution per spec section 4.4. Already correct in current Sprout files. Verify with grep:

```bash
grep -rln "stall by" /Users/duongvietdung/Documents/Projects/PMFCDocument/mockups-sprout/
# Expected: 0 matches (Sprout doesn't use "stall" metaphor)
```

If any leak found, replace with `by ` (or remove).

**3d. Rewards subtitle (mirrors Bazaar Task 4):**

Sprout's Rewards subtitle is "the daily harvest" per spec section 4.7 — that's the Sprout-specific themed flavor. Different from Bazaar's "The lucky draw." (which is universal). Keep as-is.

But DO add the reel emoji multiplier labels (this is universal UX improvement, not Bazaar-only). Mirror the same `<span class="reel-multiplier">×N</span>` injection in `/mockups-sprout/rewards.html`. Use peach color for the label:

```css
.reel-multiplier {
  display: block;
  font-family: var(--font-mono, 'JetBrains Mono', monospace);
  font-size: 10px;
  font-weight: 700;
  color: var(--sp-peach-400);   /* peach for Sprout, amber for Bazaar */
  margin-top: 2px;
  letter-spacing: 0.05em;
}
```

**3e. Leaderboard hierarchy (mirrors Bazaar Task 5):**

Same rule applies to Sprout leaderboard — top-3 podium peach, table rows white. Apply identical CSS change to `/mockups-sprout/leaderboard.html`:

```css
/* Top-3 cards keep peach */
.lb-token-name { color: var(--sp-peach-400); }   /* unchanged */

/* Table rows desaturate */
.lb-row-name { color: var(--text-1); }   /* was peach, change to white */
```

---

## 4. Cross-task verification

### 4a. CSS token + glow presence check

```bash
cd /Users/duongvietdung/Documents/Projects/PMFCDocument

echo "Surface palette correct:"
grep -rln "\-\-surface-1: #131f18" mockups-sprout/ | wc -l
# Expected: 18

echo "Mascot tokens present:"
grep -rln "\-\-mascot-md: 30px" mockups-sprout/ | wc -l
# Expected: 18

echo "Glow signature comment present:"
grep -rln "Mood B signature glow" mockups-sprout/ | wc -l
# Expected: 18

echo "Body radial gradient present:"
grep -rln "radial-gradient(ellipse 800px 400px at 20%" mockups-sprout/ | wc -l
# Expected: 18

echo "No 'stall by' leakage:"
grep -rln "stall by" mockups-sprout/ || echo "  ✓ none"

echo "Mood demos preserved:"
ls mockups-sprout/_mood_demos/ | grep -c "\.html$"
# Expected: 3 (mood_a_calm, mood_b_living, mood_c_wild)
```

### 4b. Visual smoke test

Open all 18 files in browser. For each:
1. Body has subtle peach + teal radial gradient (not solid).
2. Logo container has peach halo.
3. Primary CTA (Create token / Connect wallet etc.) has peach halo.
4. If page has marquee, accent text glows.
5. If page has token cards, hover triggers subtle teal glow.
6. If page has featured/highlighted card, it has radial glow + bright border.
7. No glow on: tables, form inputs, sidebar nav, modals, body text.

### 4c. Bazaar parity check

Open `/mockups-bazaar/token_list_v4.html` and `/mockups-sprout/token_list_v4.html` side by side. Should feel like:
- Same skeleton (header, sidebar, marquee, content grid, card structure all identical).
- Different atmosphere (Bazaar = lantern lit dark navy + amber; Sprout = garden twilight green + peach with glow).
- Sprout feels more "alive at night", Bazaar feels more "marketplace lit".

### 4d. Mood demo archive intact

Verify `/mockups-sprout/_mood_demos/` still contains 3 files unchanged:
```
mood_a_calm.html
mood_b_living.html
mood_c_wild.html
```

Mood B demo is the visual reference — must NOT be modified or deleted.

---

## 5. Constraints & non-goals

**MUST NOT:**
- Touch Bazaar files (`/mockups-bazaar/*`).
- Modify mood demos in `/mockups-sprout/_mood_demos/`.
- Add glow to surfaces NOT in the 8-rule list (data tables, sidebar nav, forms, etc.).
- Introduce new color values not in spec section 1.3.
- Change Sprout tagline "Plant your seed in the memeconomy." without explicit user approval.
- Modify FRD files or BAZAAR_UI_SPEC.md.

**MAY:**
- Refine `clone_to_sprout.py` to be idempotent.
- Add HTML comment markers like `<!-- Mood B glow injected 2026-05-05 -->` if helpful for future agents.
- Run a CSS formatter to keep diffs clean.

---

## 6. When done

1. All grep verifications in section 4a pass.
2. Visual smoke test (section 4b) passes for all 18 files.
3. Bazaar parity check (section 4c) confirms shared shell + distinct atmosphere.
4. Mood demo archive intact (section 4d).
5. Update `/SPROUT_UI_SPEC.md` section 12 (changelog) with a new entry: "2026-05-XX — Mood B glow signature implemented per SPROUT_MOOD_B_IMPLEMENTATION_PLAN.md. All 18 files pass verification."
6. Report back to user with: files modified count, grep verification output, before/after screenshot pair (token_list_v4 Sprout side-by-side with Bazaar), any edge cases.

---

## 7. Edge cases to watch

- **Body bg already has gradient:** if any file's `body { background: … }` rule already has a gradient (e.g. for a hero), preserve the existing gradient and APPEND the Mood B ambient gradients via comma. Don't blow away existing.
- **`.btn-primary` linear-gradient already has glow:** spec adds glow on top of existing gradient. If you find `.btn-primary { background: linear-gradient…; }` without glow, ADD `box-shadow:`. If glow is already different/wrong, replace with locked spec values.
- **Featured card class names vary:** spec selector is `.token-card.featured, .tk-card.featured, .card.featured` — covers known variants. If a file uses a custom class like `.featured-token-card`, add it to the selector list in that file's rule (or rename the class to match canonical).
- **Marquee classes `.peach` vs `.teal`:** if a file uses `.amber` or `.green` instead, rename classes to `.peach` / `.teal` for consistency. The clone script's `CLASS_SWAPS` should handle this — verify.
- **Script idempotency:** if `clone_to_sprout.py` is re-run after manual edits, manual edits get blown away. Solution: either (a) re-apply manual edits inside the script, or (b) skip the script and edit files manually. Decide before starting.
- **Linter modifying files:** if a linter or formatter auto-runs on save, it may re-flow the injected glow CSS. That's fine — formatting isn't semantic. Don't fight the linter.

---

## 8. Estimated breakdown

| Task | Effort | Risk |
|---|---|---|
| 1. Refine canonical files (token_list_v4, points) | 30 min | Low |
| 2a-c. Update `clone_to_sprout.py` (Path A) | 60 min | Medium — needs Python regex for glow injection |
| 2d. Run script + verify | 15 min | Low |
| 3. Cross-theme parity (mascot tokens, leaderboard, rewards reel labels) | 45 min | Medium — depends on Bazaar Group A status |
| Verification + visual QA | 30 min | — |
| **Total** | **~3h** | — |

If using Path B (manual) instead of Path A (script): add ~1.5h.

---

## 9. Coordination with Bazaar Group A plan

This Sprout plan and `/BAZAAR_GROUP_A_FIXES_PLAN.md` can run in parallel BUT prefer this order:

1. **First:** run Bazaar Group A Tasks 1-5 (those changes need to land in Bazaar files).
2. **Then:** run this Sprout plan, including Task 3 cross-theme parity.

Reason: Bazaar Group A introduces `--mascot-*` tokens, leaderboard hierarchy CSS, and reel multiplier labels into Bazaar files. The clone script will then propagate those into Sprout automatically. If Sprout runs first, Task 3 has to manually mirror.

If parallel is required (different agents, different timelines), each plan is self-contained — both plans tell their executor to handle the parity items, with cross-references.

---

**End of plan.** Reach out to user via the chat (do NOT make new design decisions silently) if you encounter ambiguity. The spec at `/SPROUT_UI_SPEC.md` is your single source of truth.
