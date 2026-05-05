f# PUMPFUN CLONE — PROJECT DEFINITION

## Overview

**Platform:** Solana-based meme token launchpad (PumpFun clone)
**Core:** Fair launch with bonding curve → graduation at $69K MC → Raydium DEX
**Status:** Documentation & Design phase complete. Ready for development.

**Geographic Restriction:** Vietnam users BLOCKED (geolocation check)

---

## Theme Variants

Project hiện có 2 theme variant đang được team đánh giá:

**Sprout (default theme):**
- Mascot: cây con với 2 lá (sprout in pot)
- Brand: "Sprout · the meme garden"
- Tagline: "Plant your seed in the memeconomy."
- Palette: peach + forest green on green-tinted twilight surface (Mood B "Living Garden", locked 2026-05-05). Teal kept as bloom accent.
- Signature: subtle radial glow on logo / CTA / featured cards / marquee accent text — visual differentiator vs Bazaar
- Tier ladder (FR-011): Seed → Sprout → Sapling → Tree → Ancient Tree
- Files: `/Function Requirements.md`, `/docs/FRD_Updated.md`, `/mockups/`, `/mockups-v2/`, `/mockups-sprout/`
- Spec: `/SPROUT_UI_SPEC.md`
- Glow implementation plan: `/SPROUT_MOOD_B_IMPLEMENTATION_PLAN.md`

**Bazaar (variant for evaluation):**
- Mascot: cat hawker behind quầy hàng
- Brand: "Stallspot · the meme bazaar"
- Tagline (hero): "Trade memes at the bazaar." · Tagline (creator funnel): "Open a stall. Pitch your meme." (locked 2026-05-05; old "Open a stall. Trade memes." deprecated)
- Palette: amber + brown (teal kept as success accent)
- Tier ladder (FR-011): Newcomer → Regular → Local → Insider → Legend
- Files: `/Function Requirements - Bazaar.md`, `/mockups-bazaar/`
- Spec: `/BAZAAR_UI_SPEC.md` (single source of truth; FRD-Bazaar + BAZAAR_IMPLEMENTATION_PLAN.md tagline references are historical and not authoritative)
- Group A pitch-readiness fixes plan: `/BAZAAR_GROUP_A_FIXES_PLAN.md`
- Migration plan (historical): `/BAZAAR_IMPLEMENTATION_PLAN.md`

**Brand swap script:** `/scripts/clone_to_sprout.py` regenerates `/mockups-sprout/` from `/mockups-bazaar/`. Run when Bazaar updates need to propagate to Sprout.

**FRD file landscape (important for new contributors):**

Project có 4 file FRD với mức độ current khác nhau. Đây là provenance:

| File | Status | Notes |
|---|---|---|
| `/Function Requirements.md` | Original (oldest) | 11 FRs, missing Arena/Clubs/Staking |
| `/FRD_20260418.md` | 18/04/2026 | 15 FRs, formal spec |
| `/docs/FRD_Updated.md` | 16/04/2026 | **MVP-aligned, recommended source** when comparing FRD ↔ MVP |
| `/docs/FRD_MVP_Reality_Check.md` | 16/04/2026 | Duplicate of FRD_Updated |
| `/Function Requirements - Bazaar.md` | NEW | Bazaar theme diff of FRD_Updated |

**Important:** Both Sprout and Bazaar variants share identical functional requirements, BE/FE architecture, layout, and core trading UI. They differ only in brand identity, microcopy at brand+gamification layers, and tier names. See `/BAZAAR_IMPLEMENTATION_PLAN.md` for the three-layer principle that governs theme application.

**MVP is ground truth.** When FRDs disagree với MVP behavior live tại `https://fe-dev.pumpfunclone2025.win/`, MVP wins. Both theme variants must match MVP functionally; only theme/brand layer differs.

---

## Project Structure

```
PumpFunCloneDocument/
├── CLAUDE.md                              ← This file
├── README.md
├── BAZAAR_IMPLEMENTATION_PLAN.md          ← Bazaar theme migration plan
├── Function Requirements.md               ← Sprout theme FRD (default)
├── Function Requirements - Bazaar.md      ← Bazaar theme FRD variant
├── Function Requirements.pdf
├── images/                                ← MVP screenshots
│
├── docs/                                  ← Individual FRs (theme-agnostic)
│   ├── FR-INDEX.md
│   ├── FR-001_TokenList.md … FR-016_ClubWar.md
│   ├── DiscoverScore.md
│   └── ...
│
├── mockups/                               ← Sprout HTML mockups (default)
├── mockups-v2/                            ← Sprout newer previews
├── mockups-bazaar/                        ← Bazaar HTML mockups (variant)
│
├── testing/                               ← Test docs (theme-agnostic for now)
│
└── design/UI_UX_DESIGN_SYSTEM.md          ← Design system (Sprout default)
```

---

## Discover Tab — Scoring System (FINALIZED)

> Full spec: `docs/DiscoverScore.md`

**Công thức:**
```
DiscoverScore = BuyVolume24h × (1 + PriceChange24h% / 100) + TrustBonus
```

- `BuyVolume24h` — tổng volume phía mua trong 24h (SOL)
- `PriceChange24h%` — % thay đổi giá trong 24h (e.g. +40, -20)
- `TrustBonus` — +0 / +10 / +20 / +30 tương ứng 0/1/2/3 trust badges

**Cơ chế hiển thị (slot 80/20):** Mỗi trang 20 token → 16 Hot (DiscoverScore cao nhất) + 4 Big (MC cao nhất, chưa có trong Hot), xen kẽ đều.

**Lý do thiết kế:**
- Không dùng công thức cũ trong FR-001 (5 thành phần + bảng mapping) — đã thay thế hoàn toàn
- MC không vào công thức, thay vào đó dùng slot riêng để tránh Discover toàn token nhỏ
- Tính lại mỗi 10 phút, cache kết quả

---

## Key Business Rules

> Theme-specific naming variants noted in `Function Requirements.md` (Sprout) and `Function Requirements - Bazaar.md` (Bazaar). Mechanics and values below apply to both.

- **Creator Fee:** 1% on all trades
- **Referral Commission:** 5% of trading fees (Bazaar copy: "5% commission when they trade at your stall")
- **Bonding Curve:** Fair launch pricing mechanism
- **Graduation:** $69K Market Cap → Raydium DEX with liquidity
- **Trust Score:** LP Lock (+20) + Audit (+30) + Freeze Disabled (+25) = Max 75
- **One-time fields:** Username, Display Name (cannot change after first save)
- **Min trade:** 0.01 SOL (for points eligibility)
- **Points tiers (Sprout):** 🌱 Seed (0) → 🌿 Sprout (500) → 🌳 Sapling (2K) → 🌲 Tree (10K) → 🪷 Ancient Tree (50K)
- **Points tiers (Bazaar):** Newcomer (0) → Regular (500) → Local (2K) → Insider (10K) → Legend (50K)

---

## Design System (Quick Reference)

**Theme:** "Premium Crypto Dark" — dark theme, glassmorphism, gradient accents
**Full spec:** `design/UI_UX_DESIGN_SYSTEM.md` (Sprout default)
**Bazaar variant spec:** `BAZAAR_IMPLEMENTATION_PLAN.md` section 3-7

### Sprout palette (default)
```css
--primary:    #10b981;   /* Green — Buy, Trust, Success */
--peach-400:  #e8a87c;   /* Brand */
--teal-400:   #7cc4a4;   /* Accent */
--danger:     #ef4444;
--bg:         #0a0e1a;
--surface-1:  #1a1a2e;
```

### Bazaar palette (variant)
```css
--bz-amber-400:  #EAB552;  /* Brand primary */
--bz-amber-100:  #F5DBA8;  /* Light gradient */
--bz-brown-700:  #3a2410;  /* Counter dark */
--bz-teal-400:   #7CC4A4;  /* Success accent (preserved) */
--bz-crimson:    #D65A54;  /* Sell, danger */
--bg:            #0a0e1a;  /* Same surface */
--surface-1:     #131826;
```

### Layout (both variants)
```css
--header-height: 60px;
--marquee-h: 30px;
--sidebar-width: 240px;
```

---

## Development Priority

| Phase | FRs | Description |
|-------|-----|-------------|
| 1 (Core) | FR-001, 002, 003, 007 | Token list, detail, trading, creation |
| 2 (Users) | FR-004, 005, 006 | Profiles, creator dashboard |
| 3 (Engage) | FR-008, 010, 011 | Leaderboard, referrals, points |
| 4 (Gamify) | FR-009 | Rewards & slot machine |
| 5 (Advanced) | FR-012 | Token War (prediction market) |

---

## Conventions

- **Docs language:** Vietnamese descriptions + English code/technical terms
- **FR naming:** `FR-XXX_FeatureName.md`
- **Mockup naming:** `feature_name_mockup.html`
- **Documentation style:** Compact, developer-focused, no verbose explanations
- **Acceptance criteria:** Always at end of each FR section
- **Theme variants:** Brand-layer microcopy varies between Sprout and Bazaar. Core trading UI (Buy/Sell, Volume, Market Cap, Trust Score, Chart) is identical across themes. See `BAZAAR_IMPLEMENTATION_PLAN.md` section 5 for the three-layer principle.

---

## Tech Stack (Planned)

- **Blockchain:** Solana (Web3.js, SPL Token, Phantom/Solflare wallet adapter)
- **Smart Contract:** Bonding curve + Raydium integration
- **Real-time:** WebSocket for live prices, SSE for notifications
- **AI:** Description generation API, Avatar generation (DALL-E/Midjourney)
- **Security:** Geolocation blocking, wallet signature verification, anti-MEV, rate limiting
