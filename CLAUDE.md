f# PUMPFUN CLONE — PROJECT DEFINITION

## Overview

**Platform:** Solana-based meme token launchpad (PumpFun clone)
**Core:** Fair launch with bonding curve → graduation at $69K MC → Raydium DEX
**Status:** Documentation & Design phase complete. Ready for development.

**Geographic Restriction:** Vietnam users BLOCKED (geolocation check)

---

## Project Structure

```
PumpFunCloneDocument/
├── CLAUDE.md                    ← This file — project definition for AI agents
├── README.md                    ← Quick intro & navigation
├── Function Requirements.md     ← Master FR document (all 11 FRs in one file)
├── Function Requirements.pdf    ← PDF version
├── images/                      ← Screenshots referenced by master FR doc
│
├── docs/                        ← Individual FR documents & project specs
│   ├── FR-INDEX.md              ← Index of all FRs with priorities
│   ├── DiscoverScore.md         ← Scoring algorithm for tab Discover (FINALIZED)
│   ├── FR-001_TokenList.md      ← Token List (discovery, filters, search)
│   ├── FR-002_Token_Detail.md   ← Token Detail page
│   ├── FR-003_BuySell.md        ← Trading panel (basic + advanced)
│   ├── FR-004_MyProfile.md      ← Personal dashboard (5 tabs)
│   ├── FR-005_PublicProfile.md  ← Read-only user profiles
│   ├── FR-006_CreatorDashboard.md ← Token management for creators
│   ├── FR-007_CreateToken.md    ← 5-step creation wizard
│   ├── FR-008_Leaderboard.md    ← Top tokens ranking
│   ├── FR-009_Rewards.md        ← Slot machine game
│   ├── FR-010_Referrals.md      ← Referral system & earnings
│   ├── FR-011_Points.md         ← Points & ranking system
│   ├── FR-012_TokenWar_ModelAnalysis.md  ← Token War analysis (2 models)
│   ├── FR-012_TokenWar_ModelAnalysis.pdf
│   ├── PumpFun_Flows_D1_D11.md  ← System flows (D1–D11)
│   └── PUMPFUN_PROJECT_SUMMARY.md ← Complete project context & artifacts
│
├── mockups/                     ← HTML UI mockups (open in browser)
│   ├── home_full_layout.html    ← Main layout (header + sidebar + token list)
│   ├── token_detail_mockup.html
│   ├── trading_panel_mockup.html
│   ├── my_profile_mockup.html
│   ├── public_profile_mockup.html
│   ├── creator_dashboard_mockup.html
│   ├── create_token_mockup.html
│   ├── leaderboard_mockup.html
│   ├── points_mockup.html
│   ├── referrals_mockup.html
│   ├── edit_profile_privacy_mockup.html
│   ├── sidebar_navigation.html
│   ├── FR-012_TokenWar.html
│   └── FR-012b_TokenWar_PredictionMarket.html
│
├── testing/                     ← Test documentation
│   ├── TEST_INDEX.md            ← Index of all test docs
│   ├── TEST_PLAN.md             ← Master test plan (7-week schedule)
│   ├── TEST_CASES_MATRIX.md     ← 217 functional test cases
│   ├── TEST_CASES_BY_CATEGORY.md
│   ├── TEST_CASES_DETAILED.md
│   ├── TEST_CASES_GENERATED.md
│   ├── TEST_E2E_SCENARIOS.md    ← 20 E2E user journey scenarios
│   ├── TEST_API_CASES.md        ← 89 API test cases
│   ├── TEST_PERFORMANCE_SCRIPTS.md ← k6 load test scripts
│   ├── TEST_SECURITY_CHECKLIST.md  ← 139 security checks
│   └── TEST_DATA.md             ← Test accounts, tokens, data sets
│
└── design/                      ← Design system
    └── UI_UX_DESIGN_SYSTEM.md   ← Complete design tokens, components, layouts
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

- **Creator Fee:** 1% on all trades
- **Referral Commission:** 5% of trading fees
- **Bonding Curve:** Fair launch pricing mechanism
- **Graduation:** $69K Market Cap → Raydium DEX with liquidity
- **Trust Score:** LP Lock (+20) + Audit (+30) + Freeze Disabled (+25) = Max 75
- **One-time fields:** Username, Display Name (cannot change after first save)
- **Min trade:** 0.01 SOL (for points eligibility)
- **Points tiers:** 🌱 Seed (0) → 🌿 Sprout (500) → 🌳 Sapling (2K) → 🌲 Tree (10K) → 🪷 Ancient Tree (50K)

---

## Design System (Quick Reference)

**Theme:** "Premium Crypto Dark" — dark theme, glassmorphism, gradient accents
**Full spec:** `design/UI_UX_DESIGN_SYSTEM.md`

```css
/* Core colors */
--primary:    #10b981;   /* Green — Buy, Trust, Success */
--danger:     #ef4444;   /* Red — Sell, Risk, Error */
--warning:    #f59e0b;   /* Amber — Caution */
--accent:     #8b5cf6;   /* Purple — CTAs, Highlights */
--bg:         #0a0e1a;   /* Background */
--surface-1:  #1a1a2e;   /* Cards */
--surface-2:  #16213e;   /* Inputs, nested cards */

/* Layout */
--header-height: 70px;
--sidebar-width: 260px;
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

---

## Tech Stack (Planned)

- **Blockchain:** Solana (Web3.js, SPL Token, Phantom/Solflare wallet adapter)
- **Smart Contract:** Bonding curve + Raydium integration
- **Real-time:** WebSocket for live prices, SSE for notifications
- **AI:** Description generation API, Avatar generation (DALL-E/Midjourney)
- **Security:** Geolocation blocking, wallet signature verification, anti-MEV, rate limiting
