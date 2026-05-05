# Sprout UI Spec — Garden Theme

> **Single source of truth** cho thiết kế giao diện Sprout variant.
> Mirror của `BAZAAR_UI_SPEC.md` — same architecture, different brand layer.
> **Last updated:** 2026-05-04 · **Status:** active

---

## 0. Quick context

- **Project:** PumpFun Clone (Solana meme token launchpad)
- **Theme variant:** Sprout · the meme garden (default theme, original)
- **Mockups location:** `/mockups-sprout/` (parallel to `/mockups-bazaar/`)
- **Source-of-truth hierarchy:**
  1. Live MVP at `https://fe-dev.pumpfunclone2025.win/`
  2. `/docs/FRD_Updated.md` (functional spec, MVP-aligned)
  3. **This file** (`SPROUT_UI_SPEC.md`) — Sprout design system
  4. Existing Sprout mockups in `/mockups-sprout/`
  5. Sprout v1/v2 references in `/mockups/` and `/mockups-v2/_preview/`

When in doubt, **MVP wins**. Both Sprout and Bazaar variants must match MVP functionally; only theme/brand layer differs.

---

## 1. Brand identity (locked)

### 1.1 Names & taglines

| Element | Value |
|---|---|
| Brand name | **Sprout** |
| Subtitle | the meme garden |
| Tagline (primary) | "Plant your seed in the memeconomy." |
| Tagline (alt) | "The meme garden." |
| Brand archetype | Caregiver + Innocent (gentle growth, organic, safe-feeling) |

### 1.2 Mascot — Sprout (cây con với 2 lá)

Cây non trong chậu đất, 2 lá teal-green vươn ra hai bên, thân cây xanh đậm, có mặt cười mộc mạc trong chậu. Visual gentle, growing, friendly.

**Banned:** mascot withered/dead, religious symbols, animals (Sprout là plant-based identity).

### 1.3 Color palette — Mood B "Living Garden" (locked 2026-05-05)

After exploring 3 mood directions (Calm / Living / Wild Garden), team locked **Mood B — Living Garden**: green-tinted twilight surface (different from Bazaar's dark navy — intentional brand differentiation), full-saturation peach + teal accents, **signature radial glow treatment** on logo, CTA, featured cards, and marquee accent text. The glow treatment is what makes Sprout feel "alive at night" vs Bazaar's "lantern lit".

**Why Mood B won:**
- Green-tinted surface (`#0a1610`) gives Sprout its own atmosphere → instantly distinguishable from Bazaar even at thumbnail scale
- Signature radial glow on featured cards = "garden alive at night" → screenshotable wow moment for pitch deck
- Full-saturation peach + teal (vs Mood A's muted) → brand stays vibrant, doesn't disappear into bg
- Rejected Mood A (Calm — too muted, featured cards don't pop) and Mood C (Wild — bg same as Bazaar loses Sprout's atmospheric identity)

```css
:root {
  /* Surface palette — green-tinted twilight (Sprout signature, NOT Bazaar's navy) */
  --bg:        #0a1610;
  --surface-1: #131f18;
  --surface-2: #1a2a20;
  --surface-3: #243528;
  --border-1:  #1f2d24;
  --border-2:  #2d4234;

  /* Sprout primary — peach (warm sunset over garden, full saturation) */
  --sp-peach-100: #f4cba0;
  --sp-peach-200: #f4c099;   /* glow brighter */
  --sp-peach-400: #e8a87c;   /* primary CTA, brand color */
  --sp-peach-500: #d68a5b;
  --sp-peach-soft: rgba(232, 168, 124, 0.12);
  --sp-peach-glow: rgba(232, 168, 124, 0.18);

  /* Sprout secondary — forest green (stem, leaf base, mascot) */
  --sp-forest-300: #5ba886;
  --sp-forest-500: #3d7458;
  --sp-forest-700: #3d7458;
  --sp-cream:    #f4cba0;

  /* Teal — leaf/bloom accents (SUCCESS semantic, full saturation) */
  --sp-teal-300: #94d6b8;    /* glow brighter */
  --sp-teal-400: #7cc4a4;    /* "Just sprouted", buy color, success */
  --sp-teal-500: #5ba886;
  --sp-teal-soft: rgba(124, 196, 164, 0.14);
  --sp-teal-glow: rgba(124, 196, 164, 0.22);

  /* Crimson — danger / sell */
  --sp-crimson:  #D65A54;

  /* Text — slightly warmer than Bazaar's neutral grays (greenish tint OK) */
  --text-1: #f5f7f4;
  --text-2: #a3b0a7;
  --text-3: #6f7d74;
  --text-mute: #4a5650;

  /* Mascot sizing tokens — SAME as Bazaar */
  --mascot-sm:   22px;
  --mascot-md:   30px;
  --mascot-lg:   40px;
}
```

### 1.3a Signature glow treatment (Mood B locked rules)

Glow is the visual signature of Sprout — Bazaar does NOT have it. These rules apply to every Sprout page.

```css
/* 1. Body background — subtle ambient garden glow (2 radial gradients) */
body {
  background: var(--bg);
  background-image:
    radial-gradient(ellipse 800px 400px at 20% 0%, rgba(232,168,124,0.06), transparent 60%),
    radial-gradient(ellipse 600px 400px at 90% 30%, rgba(124,196,164,0.05), transparent 60%);
  background-attachment: fixed;
}

/* 2. Logo container — peach glow + inset highlight */
.logo-mascot {
  background: linear-gradient(180deg, var(--sp-peach-100), var(--sp-peach-400));
  box-shadow: 0 0 24px rgba(232,168,124,0.35), inset 0 1px 0 rgba(255,255,255,0.2);
}

/* 3. Primary CTA — peach glow */
.btn-primary {
  background: linear-gradient(180deg, var(--sp-peach-100), var(--sp-peach-400));
  box-shadow: 0 0 20px rgba(232,168,124,0.30);
}

/* 4. Marquee accent text — text-shadow glow */
.marquee-track .peach { color: var(--sp-peach-200); text-shadow: 0 0 12px rgba(232,168,124,0.4); }
.marquee-track .teal  { color: var(--sp-teal-300);  text-shadow: 0 0 12px rgba(124,196,164,0.4); }

/* 5. Featured card — radial glow + brighter border */
.token-card.featured {
  border-color: rgba(232,168,124,0.55);
  background:
    radial-gradient(ellipse 300px 200px at 100% 0%, rgba(232,168,124,0.10), transparent 70%),
    var(--surface-1);
  box-shadow: 0 0 32px rgba(232,168,124,0.18), inset 0 1px 0 rgba(255,255,255,0.04);
}

/* 6. Token card hover — subtle teal glow */
.token-card:hover {
  box-shadow: 0 0 24px rgba(124,196,164,0.08);
  border-color: var(--border-2);
}

/* 7. Token avatar — soft teal halo */
.token-av { box-shadow: 0 0 16px rgba(124,196,164,0.15); }

/* 8. Bar fill (progress to DEX) — peach inner glow */
.bar-fill {
  background: linear-gradient(90deg, var(--sp-peach-400), var(--sp-teal-400));
  box-shadow: 0 0 10px rgba(232,168,124,0.5);
}
```

**Glow restraint rule:** glow only on the 8 surfaces listed above. Do NOT add glow to: data tables, sidebar nav items, form inputs, dropdowns, modals, tooltips. Over-glow looks cheap; restrained glow = premium signature.

### 1.3b Historical mood demos (reference only)

Three mood explorations preserved at `/mockups-sprout/_mood_demos/` for design history:
- `mood_a_calm.html` — Calm Garden (deep forest bg, muted accents) — REJECTED (too quiet)
- `mood_b_living.html` — Living Garden (twilight green bg, glow effects) — **LOCKED 2026-05-05**
- `mood_c_wild.html` — Wild Garden (dark navy bg, full saturation + amber sub-accent) — REJECTED (lost Sprout's atmospheric identity)

Do not reference mood A/C in new code. They exist for archival comparison only.

### 1.4 Typography & layout

Identical with Bazaar — see `BAZAAR_UI_SPEC.md` sections 1.4 and 1.5. Same font scales, same layout constants (header 60px, marquee 30px, sidebar 240px). All themes share architecture.

---

## 2. Three-layer theme principle

**Identical principle as Bazaar** — read `BAZAAR_UI_SPEC.md` section 2 for full guidance. Applied to Sprout:

- **Layer 1 (theme 100%):** logo, brand name "Sprout", tagline "Plant your seed", marquee, mascot
- **Layer 2 (theme có chọn lọc):** tier ladder, "Token story" callout (renamed from Bazaar's "Stall story"), graduation moment, slot rewards naming, page subtitles
- **Layer 3 (standard, không đổi):** all CTAs, all data labels, status badges, Trust Score breakdown, chart toolbar, trade panel — IDENTICAL to Bazaar

Same anti-patterns apply. Specifically for Sprout: ❌ KHÔNG dùng "Just sprouted" cho status badge "New" — vẫn giữ standard "New". KHÔNG dùng "Almost there" cho "Almost graduated" — giữ "Almost graduated".

---

## 3. Tier ladder (FR-011 Points) — Sprout

| Tier index | Name | Points threshold | Sub-narrative |
|---|---|---|---|
| 1 | **Seed** | 0 | A fresh seed in the soil. |
| 2 | **Sprout** | 500 | Sprouting roots. |
| 3 | **Sapling** | 2,000 | Growing strong in the garden. |
| 4 | **Tree** | 10,000 | A sturdy tree. |
| 5 | **Ancient Tree** | 50,000 | An ancient tree of legend. |

Migration mapping: 1-1 by tier index with Bazaar (Newcomer↔Seed, Regular↔Sprout, Local↔Sapling, Insider↔Tree, Legend↔Ancient Tree). Points không đổi giữa 2 themes.

---

## 4. Microcopy library — Sprout-specific

### 4.1 Brand bar (themed)

- Brand: `Sprout` + subtitle `the meme garden`
- Search placeholder: `Search the garden — tokens, creators, addresses…`
- Tagline: `Plant your seed in the memeconomy.`

### 4.2 Marquee (themed)

```
PLANT YOUR SEED · WATCH WHAT'S BLOOMING · MAKE MONEY ON THE MEMECONOMY · NO BOT DRAMA · TALLEST TREE WINS · SEEDS PLANTED HERE
```

Color rules:
- "PLANT YOUR SEED", "MAKE MONEY ON THE MEMECONOMY", "SEEDS PLANTED HERE" → `var(--sp-peach-400)`
- "TALLEST TREE WINS" → `var(--sp-teal-400)`
- Others → `var(--text-3)`

### 4.3 Status badges — STANDARD

Identical with Bazaar. **Do NOT theme**: "New" / "Almost graduated" / "Graduated".

(Original Sprout v2 đã dùng "Just sprouted" / "Almost there" — but per 3-layer principle, these are decision-critical → revert to standard.)

### 4.4 Creator info on token detail

Format: `by alice · Sapling tier · 12d ago`
- "by" → simple attribution (no theming, since no "stall" metaphor)
- Tier name from ladder section 3

### 4.5 Token story callout (NEW component)

Same component as Bazaar's "Stall story" but renamed `Token story`. Used on token detail between chart and trades. Creator pitch text in italic, peach border-left, peach-soft background.

### 4.6 Graduation moment

```
GRADUATED · NOW ON RAYDIUM
[Token Name] has bloomed in the garden. Trading on Raydium DEX.
```

- Headline: standard "GRADUATED · NOW ON RAYDIUM"
- Themed subtitle: "[Token Name] has bloomed in the garden."
- Standard fact: "Trading on Raydium DEX."
- Mascot: sprout (with sparkles around to signify growth/celebration)

### 4.7 Slot Rewards (FR-009)

Page title: `Rewards` + subtitle `the daily harvest` (themed flavor)
- Symbols (escalating value): 🪙 ×1 → 💰 ×2 → 💎 ×3 → 🏆 ×4 → 👑 ×5 (same as Bazaar)
- Rules text: standard (functional)

### 4.8 Referrals (FR-010)

- Page subtitle: "Plant a friend in the garden. Earn when they trade."
- How it works: "Share your seed packet. When a friend joins and trades, you earn `20%` of their trading fees automatically."
- Referral link prefix: `https://sprout.app/join/@`
- Stat labels: standard (Total referrals / Total volume / Unclaimed rewards)

### 4.9 Token War / Arena (FR-012)

- Feature page title: `Arena` (universal, keep)
- Sub-title: "Garden arena · back winners · the garden predicts"
- Voting CTA: `Back A` / `Back B`
- Match-up: same `Token A vs Token B` for token war, `[Team A] vs [Team B]` for football, `Yes / No` for events

### 4.10 Onboarding & empty states

- Welcome: "Welcome to the garden — where memes get planted and traded."
- Empty profile: "You're a Seed in the garden. Make your first trade or plant a token to start earning points."
- Empty token list: "No seeds match. Try a different filter."
- 404: "This seed never sprouted. Maybe it's still underground — or maybe it's been pulled out."

---

## 5. Component library

**All component patterns identical với Bazaar** — see `BAZAAR_UI_SPEC.md` sections 5.1–5.5 for full canonical structure. The only differences:

- App shell uses Sprout brand (logo, marquee text, palette)
- Sidebar nav structure: identical (Discover / Personal / Earn — Leader Board moved to Discover)
- Header wallet state: identical structure, sprout mini avatar in `.wc-avatar` instead of cat hawker
- Stat card: identical
- Page header: identical patterns A & B
- Trust score (FR-013): identical, untouched
- Trade panel (FR-003): identical, untouched

---

## 6. Routing map

**Identical with Bazaar.** See `BAZAAR_UI_SPEC.md` section 6. All file names match (token_list_v4.html, token_detail.html, points.html, etc.) — same routes, parallel file in `/mockups-sprout/` instead of `/mockups-bazaar/`.

---

## 7. SVG asset library

### 7.1 Sprout mascot 32x32 (header logo)

```svg
<svg viewBox="0 0 32 32" fill="none">
  <ellipse cx="16" cy="24" rx="9" ry="6" fill="#8B4513"/>            <!-- pot -->
  <ellipse cx="11" cy="14" rx="3" ry="6" transform="rotate(-25 11 14)" fill="#7cc4a4"/>  <!-- left leaf -->
  <ellipse cx="21" cy="14" rx="3" ry="6" transform="rotate(25 21 14)" fill="#5ba886"/>   <!-- right leaf -->
  <rect x="15" y="16" width="2" height="8" fill="#3d7458"/>          <!-- stem -->
  <circle cx="13" cy="25" r="0.8" fill="#1a1208"/>                   <!-- left eye -->
  <circle cx="19" cy="25" r="0.8" fill="#1a1208"/>                   <!-- right eye -->
  <path d="M 13 27 Q 16 28.5 19 27" stroke="#1a1208" stroke-width="0.7" fill="none" stroke-linecap="round"/>  <!-- smile -->
</svg>
```

### 7.2 Sprout mini 24x24 (user card / connected wallet)

```svg
<svg viewBox="0 0 24 24" fill="none">
  <ellipse cx="12" cy="18" rx="7" ry="4" fill="#8B4513"/>
  <ellipse cx="8" cy="10" rx="2.5" ry="5" transform="rotate(-25 8 10)" fill="#7cc4a4"/>
  <ellipse cx="16" cy="10" rx="2.5" ry="5" transform="rotate(25 16 10)" fill="#5ba886"/>
  <rect x="11" y="12" width="2" height="6" fill="#3d7458"/>
  <circle cx="10" cy="19" r="0.6" fill="#1a1208"/>
  <circle cx="14" cy="19" r="0.6" fill="#1a1208"/>
  <path d="M 10 20.5 Q 12 21.5 14 20.5" stroke="#1a1208" stroke-width="0.5" fill="none" stroke-linecap="round"/>
</svg>
```

### 7.3 Sprout 64x64 (large mascot, hero illustration)

```svg
<svg viewBox="0 0 64 64" fill="none">
  <ellipse cx="32" cy="46" rx="16" ry="11" fill="#8B4513"/>
  <ellipse cx="24" cy="28" rx="6" ry="11" transform="rotate(-25 24 28)" fill="#7cc4a4"/>
  <ellipse cx="40" cy="28" rx="6" ry="11" transform="rotate(25 40 28)" fill="#5ba886"/>
  <rect x="30" y="30" width="4" height="14" fill="#3d7458"/>
  <circle cx="27" cy="48" r="1.5" fill="#1a1208"/>
  <circle cx="37" cy="48" r="1.5" fill="#1a1208"/>
  <path d="M 27 51 Q 32 53.5 37 51" stroke="#1a1208" stroke-width="1.2" fill="none" stroke-linecap="round"/>
</svg>
```

### 7.4 Mascot expression states

Same 8 states as Bazaar's cat hawker (default smile / wink / wide-eyed shock / sad / whispering / megaphone / money-eyes / sleeping) but expressed via sprout's leaf-and-eye combinations. Default smile (current) is canonical reference. Other states: AI-gen variations following design brief in `BAZAAR_IMPLEMENTATION_PLAN.md` section 4.3 (adapted for sprout silhouette).

---

## 8. Page inventory & status

Same structure as `/mockups-bazaar/` (see `BAZAAR_UI_SPEC.md` section 8). All 18 files mirrored:

| Page | File | Status |
|---|---|---|
| Token List (home) | `token_list_v4.html` | ✅ |
| Token Detail | `token_detail.html` | ✅ |
| Trading Panel | `trading_panel.html` | ✅ |
| My Profile | `my_profile.html` | ✅ |
| Public Profile | `public_profile.html` | ✅ |
| Edit Profile | `edit_profile_privacy.html` | ✅ |
| Creator Dashboard | `creator_dashboard.html` | ✅ |
| Create Token (wizard) | `create_token.html` | ✅ |
| Leaderboard | `leaderboard.html` | ✅ |
| Points | `points.html` | ✅ |
| Rewards (slot machine) | `rewards.html` | ✅ |
| Referrals | `referrals.html` | ✅ |
| Sidebar (preview) | `sidebar_navigation.html` | ✅ |
| Token War | `FR-012_TokenWar.html` | ✅ |
| Token War Prediction | `FR-012b_TokenWar_PredictionMarket.html` | ✅ |
| Clubs | `clubs.html` | ✅ |
| Events | `events.html` | ✅ |
| Home full layout | `home_full_layout.html` | ✅ (deprecated meta-redirect) |

(Status reflects post-clone-script run. Verify by opening `mockups-sprout/token_list_v4.html` in browser.)

---

## 9. How Sprout was built

Sprout pages are generated by **brand-swapping** Bazaar pages via script `/scripts/clone_to_sprout.py`. The script applies:

1. **SVG mascot swap**: cat hawker → sprout (32x32, 24x24, 64x64 variants)
2. **CSS variable rename**: `--bz-amber-*` → `--sp-peach-*`, `--bz-brown-*` → `--sp-forest-*`, etc.
3. **Hex color swap**: amber values → peach values, brown → forest green
4. **Brand text swap**: Stallspot → Sprout, "the meme bazaar" → "the meme garden", taglines, marquee
5. **Tier ladder rename**: Newcomer/Regular/Local/Insider/Legend → Seed/Sprout/Sapling/Tree/Ancient Tree
6. **Microcopy swap**: "stall by" → "by", "Stall story" → "Token story", "the lucky draw" → "the daily harvest", etc.

**Mood B refinement (2026-05-05):** the script's `HEX_SWAPS` keep the 6 surface palette swaps (Sprout uses green-tinted twilight surface, distinct from Bazaar's dark navy). The script does NOT inject glow signature CSS — that's added per-page by the Antigravity agent following section 1.3a rules. See `SPROUT_MOOD_B_IMPLEMENTATION_PLAN.md` for the exact glow injection diff per file.

**Architecture, layout, components, routing, 3-layer principle, connected wallet, sidebar grouping** — IDENTICAL with Bazaar. **Surface palette + signature glow** — distinct (Sprout's brand layer). Same skeleton, different atmosphere.

To re-run / refresh:

```bash
cd /path/to/PMFCDocument
python3 scripts/clone_to_sprout.py
```

Output: `/mockups-sprout/` — 18 HTML files cloned + brand-swapped.

---

## 10. File structure

```
PMFCDocument/
├── BAZAAR_UI_SPEC.md           ← Bazaar design system
├── SPROUT_UI_SPEC.md           ← THIS FILE (Sprout design system)
├── BAZAAR_IMPLEMENTATION_PLAN.md  ← Migration process plan (parent)
├── CLAUDE.md                   ← project context
├── docs/                       ← functional FRD docs
├── images/                     ← MVP screenshots
├── mockups/                    ← Sprout v1 (older reference)
├── mockups-v2/_preview/        ← Sprout v2 (newer reference)
├── mockups-bazaar/             ← Bazaar themed mockups
├── mockups-sprout/             ← Sprout themed mockups (this spec applies here)
└── scripts/
    └── clone_to_sprout.py      ← brand-swap script
```

---

## 11. Working with this spec — for AI agents

1. **Read this file** + `BAZAAR_UI_SPEC.md` (shared sections 2/5/6 are theme-agnostic)
2. **Reference live MVP** for functional truth
3. **Reuse app shell** from canonical `mockups-sprout/points.html` or `mockups-sprout/leaderboard.html`
4. **Apply 3-layer principle** — same rules as Bazaar
5. **Use Sprout palette + SVGs** (sections 1.3, 7.x) without modification
6. **When extending microcopy**: add Sprout-specific copy to section 4 of this file. If both themes need new copy, add to both BAZAAR_UI_SPEC and SPROUT_UI_SPEC sections.
7. **When in doubt**: STOP and ASK user. Don't guess.

---

## 12. Changelog

- **2026-05-04** — Initial spec created. Sprout cloned from Bazaar via `scripts/clone_to_sprout.py`. All 18 pages mirror Bazaar architecture with Sprout brand layer (peach palette, sprout mascot, garden microcopy).
- **2026-05-05 (Mood B lock)** — After exploring 3 mood directions (Calm/Living/Wild Garden), team locked **Mood B — Living Garden**. Surface palette refined to twilight green-tint (`#0a1610` bg, `#131f18` surface-1) — different from Bazaar's dark navy, intentional brand differentiation. Full-saturation peach + teal accents. **Signature radial glow treatment** added (section 1.3a): body bg gradients, logo glow, CTA glow, marquee text-shadow, featured card radial + bright border, hover glow, token avatar halo, bar-fill inner glow. Glow restraint rule: only 8 specified surfaces, never on data tables/sidebar/forms. Mascot sizing tokens (`--mascot-sm/md/lg`) added to match Bazaar. Three mood demos archived at `/mockups-sprout/_mood_demos/`. Implementation tracked via `SPROUT_MOOD_B_IMPLEMENTATION_PLAN.md`.

---

## 13. Cross-references

- **Bazaar variant spec:** `BAZAAR_UI_SPEC.md` (parent, contains shared sections)
- **Migration plan:** `BAZAAR_IMPLEMENTATION_PLAN.md`
- **Functional spec:** `docs/FRD_Updated.md`
- **Project context:** `CLAUDE.md`
- **Clone script:** `scripts/clone_to_sprout.py`

---

**End of spec.** Sprout is parallel theme to Bazaar — both share architecture, differ only in brand layer. Team can compare side-by-side: open `mockups-bazaar/token_list_v4.html` next to `mockups-sprout/token_list_v4.html` to feel the difference.
