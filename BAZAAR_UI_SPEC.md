# Bazaar UI Spec — Stallspot Theme

> **Single source of truth** cho thiết kế giao diện Bazaar variant.
> Bất kỳ AI agent nào làm task liên quan đến UI/UX/doc cho hệ thống Stallspot đều phải đọc file này trước.
> **Last updated:** 2026-05-04 · **Status:** active

---

## 0. Quick context

- **Project:** PumpFun Clone (Solana meme token launchpad)
- **Theme variant:** Stallspot · the meme bazaar (alternative to current Sprout/Garden)
- **Mockups location:** `/mockups-bazaar/` (parallel to `/mockups/` Sprout)
- **Source-of-truth hierarchy** for any UI question:
  1. Live MVP at `https://fe-dev.pumpfunclone2025.win/` (functional ground truth)
  2. `/docs/FRD_Updated.md` (functional spec, MVP-aligned)
  3. **This file** (`BAZAAR_UI_SPEC.md`) — design system + theme
  4. Existing Bazaar mockups in `/mockups-bazaar/` (reference patterns)
  5. Sprout mockups in `/mockups/` and `/mockups-v2/_preview/` (REFERENCE ONLY, do not treat as functional spec)

When in doubt, **MVP wins**. When MVP can't be accessed, **request user screenshot**, do NOT guess.

---

## 1. Brand identity (locked)

### 1.1 Names & taglines

| Element | Value | Where used |
|---|---|---|
| Brand name | **Stallspot** | Always |
| Subtitle | the meme bazaar | Brand bar (under logo) |
| Tagline (hero / marketing) | **"Trade memes at the bazaar."** | Marketing landing, OG card, app store |
| Tagline (creator funnel) | "Open a stall. Pitch your meme." | Onboarding creator step, empty creator dashboard, Create token wizard hero |
| Tagline (alt, short) | "The meme bazaar." | Tight space (favicon caption, mobile splash) |
| Brand archetype | Everyman + Creator | — |

**Why surface-specific taglines:** target market = ~95% buyers, ~5% creators. Hero tagline must be buyer-first. Creator-action tagline reserved for surfaces where user is already in creation context. Avoids dual-audience compound that confuses on first impression.

**❌ Banned tagline patterns:**
- "Open a stall. Trade memes." — deprecated 2026-05-05; mixed audience hurt first-impression clarity. Replace everywhere it appears.
- "Open a stall." standalone in hero contexts (creator-only bias).
- Any Anglo slang ("Hawk your memes", "Buzz the bazaar", "Hook a deal").

### 1.2 Mascot — Cat hawker

Cat behind a stall counter with awning. 8 expression states (default smile / wink / wide-eyed shock / sad / whispering / megaphone / money-eyes / sleeping). See section 7.1 for SVG reference.

**Banned:** cat without counter, mascot with hat/clothes, breed-specific cat, religious symbols.

### 1.3 Color palette

```css
:root {
  /* Surface (dark crypto convention — KEEP) */
  --bg:        #0a0e1a;      /* page bg */
  --surface-1: #131826;      /* card surface */
  --surface-2: #1a2138;      /* nested surface */
  --surface-3: #232b46;
  --border-1:  #1f2640;
  --border-2:  #2a3456;

  /* Bazaar primary — amber (warm bazaar lantern) */
  --bz-amber-100: #F5DBA8;   /* lightest, gradient top */
  --bz-amber-200: #FAC775;   /* hover */
  --bz-amber-400: #EAB552;   /* primary CTA, brand color */
  --bz-amber-500: #C49152;   /* darker shade */
  --bz-amber-soft: rgba(234, 181, 82, 0.10);
  --bz-amber-glow: rgba(234, 181, 82, 0.18);

  /* Bazaar secondary — brown (counter, structural) */
  --bz-brown-300: #8B5A3C;
  --bz-brown-500: #5a3818;
  --bz-brown-700: #3a2410;
  --bz-cream:    #F5DBA8;

  /* Teal — preserved from Sprout for SUCCESS / OK semantics */
  --bz-teal-300: #9ED8B8;
  --bz-teal-400: #7CC4A4;    /* success, "Just opened", buy color */
  --bz-teal-500: #5BA886;
  --bz-teal-soft: rgba(124, 196, 164, 0.10);

  /* Crimson — danger / sell */
  --bz-crimson:  #D65A54;

  /* Text */
  --text-1: #f4f4f5;
  --text-2: #a1a1aa;
  --text-3: #71717a;
  --text-mute: #52525b;
}
```

### 1.4 Typography

```css
--font-display: 'Plus Jakarta Sans', system-ui, sans-serif;  /* brand, headlines */
--font-body:    'Inter', system-ui, sans-serif;              /* body */
--font-mono:    'JetBrains Mono', 'SF Mono', monospace;      /* prices, addresses, code */
```

Sizes (canonical scale):
- h1 (page title): 32px / 800 weight / amber color
- h2 (section title): 18-22px / 800 / amber
- Body: 14px / 400 / text-1
- Small: 12px-13.5px / 400-600
- Mono small: 11-12.5px / 600

### 1.5 Layout constants

```css
--header-h:    60px;
--marquee-h:   30px;
--sidebar-w:   240px;
--r-sm:  6px;
--r-md:  10px;
--r-lg:  14px;
--r-pill: 999px;
--ease: cubic-bezier(0.4, 0, 0.2, 1);

/* Mascot sizing tokens (locked 2026-05-05) */
--mascot-sm:   22px;   /* table row avatar, inline data */
--mascot-md:   30px;   /* user card avatar, sidebar mini, rank card medium */
--mascot-lg:   40px;   /* hero illustration, large rank card, header logo container inner */
```

**Mascot sizing rule:** any mascot SVG render MUST use one of these 3 tokens — not arbitrary px values. Existing files using 24/30/22/34/26 must round to nearest token (24→22, 26→30, 34→40).

---

## 2. Three-layer theme principle (MOST IMPORTANT — read carefully)

This rule decides every microcopy decision. **Internalize before writing any UI text.**

### Layer 1 — Brand identity (THEME 100%)

Where: logo, brand name, tagline, marquee, mascot, brand voice in marketing/social, page subtitles giới thiệu.

**Test:** "User cần parse text này trong <2 giây để quyết định trade không?" → KHÔNG → có thể theme.

### Layer 2 — Gamification + signature moments (THEME có chọn lọc)

Where:
- Tier ladder names (user card, profile, leaderboard)
- Standalone celebration screens (graduation event banner)
- "Stall story" callout (token detail creator pitch)
- Token War event names
- Slot Rewards naming
- Referral copy ("Bring a friend to the bazaar")
- Onboarding flow ("Welcome to the bazaar")
- Page subtitles có flavor

**Test:** User encounter slowly, có context buffer → có thể theme.

### Layer 3 — Core trading UI (STANDARD, không đổi)

KHÔNG được theme:
- CTAs critical: "Create token", "Connect wallet", "Buy", "Sell", "Claim"
- Status badges affecting trade decisions: "New", "Almost graduated", "Live", "Graduated"
- Data labels: Volume 24h, Market cap, Liquidity, Holders, Total supply, Current price, 24h % change
- Trades log labels: BUY / SELL
- Trust Score & breakdown: Bronze/Silver/Gold + Liquidity/Distribution/Creator (per FR-013)
- Chart toolbar: 5m, 1h, 1d, MA, EMA, BOLL, RSI, SOL/USD
- Trade panel: Slippage, You pay, You receive, MAX, Balance
- Tab navigation: Trending, Market Cap, New, Graduated, Trending Arena
- Address fields: Contract, Deployer

**Test:** "User cần parse <2 giây để quyết định?" → CÓ → standard.

### Anti-patterns (DO NOT)

- ❌ "Stop by" thay "Buy" — Buy là core, never theme
- ❌ "Footfall" thay "Volume"
- ❌ "Vendor reputation / Stock quality / Fair pricing" thay Liquidity/Distribution/Creator (FR-013)
- ❌ "Wood / Brass / Gold seal" thay Bronze/Silver/Gold (FR-013)
- ❌ "Almost franchised" thay "Almost graduated" — status badge core
- ❌ Anglo-American slang: "Hawk", "buzz", "hook", "alpha" ở user-facing copy
- ❌ Religious/cultural insensitive: pig imagery (Indonesia), gambling visuals overdone, cowboy/Wild West (American-coded)

---

## 3. Tier ladder (FR-011 Points)

Locked decision — role-neutral, B1 ESL safe, works for buyers + sellers.

| Tier index | Name | Points threshold | Sub-narrative |
|---|---|---|---|
| 1 | **Newcomer** | 0 | Just arrived at the bazaar. |
| 2 | **Regular** | 500 | Coming back often. |
| 3 | **Local** | 2,000 | You belong here. |
| 4 | **Insider** | 10,000 | You know the deals. |
| 5 | **Legend** | 50,000 | Everyone knows your name. |

Migration mapping from Sprout: 1-1 by tier index. Points không đổi.

---

## 4. Microcopy library

### 4.1 Brand bar (themed)

- Brand: `Stallspot` + subtitle `the meme bazaar`
- Search placeholder: `Search the bazaar — tokens, vendors, addresses…`
- Tagline: see section 1.1 — surface-specific (hero vs creator funnel). Brand bar itself shows ONLY the subtitle `the meme bazaar` under the logo, no tagline (subtitle suffices in this tight space).

### 4.2 Marquee (themed)

```
OPEN A STALL · TRADE MEMES · WATCH THE CROWD · NO RIGGED SCALES · BIGGEST CROWD WINS · TIPS WHISPERED HERE
```

Color rules:
- "OPEN A STALL", "WATCH THE CROWD", "TIPS WHISPERED HERE" → `var(--bz-amber-400)`
- "BIGGEST CROWD WINS" → `var(--bz-teal-400)`
- Others → `var(--text-3)`

### 4.3 Status badges (STANDARD — never theme)

- Newly launched token: `New` (teal background, border-radius top-corners)
- Near-graduation token: `Almost graduated` (amber gradient bar, NOT a separate badge)
- Graduated token: `Graduated` (purple/teal pill)

### 4.4 Creator attribution — surface-restricted rule (locked 2026-05-05)

The "stall by" framing is **theme flavor** and lives ONLY on hero/pitch surfaces. In data-dense contexts (tables, list rows, leaderboard), use plain `by alice` standard attribution.

| Surface | Format | Rationale |
|---|---|---|
| Token detail — creator pitch hero | `stall by alice · Local tier · 12d ago` | User is in slow-read context, story flavor lands |
| Token list card — creator label | `by alice` | Scanning context, "stall by" reads cluttered |
| Leaderboard table row — creator/owner | `by alice` (or just `alice`) | Tabular density, no metaphor noise |
| Public profile header | `alice · Local tier` | Profile is the noun, no need to re-frame as "stall" |
| Creator dashboard hero | `Your stall · alice` | First-person, possessive framing |

**❌ Banned:** "stall by 7xK9…mP3q" appearing in any data table row. Drop "stall" from the leaderboard row creator/owner column entirely.

### 4.5 Stall story callout (NEW component, themed)

Use on token detail page, between chart and trades. Replaces plain token description with creator pitch framing. See section 6.6 for HTML/CSS.

### 4.6 Graduation moment (signature event)

```
GRADUATED · NOW ON RAYDIUM
[Token Name] has franchised across the bazaar. Trading on Raydium DEX.
```

- Headline: standard "GRADUATED · NOW ON RAYDIUM"
- Subtitle line 1: themed "X has franchised across the bazaar"
- Subtitle line 2: standard "Trading on Raydium DEX"
- Mascot: cat hawker money-eyes state
- Background: amber + teal gradient

### 4.7 Slot Rewards (FR-009)

Page title: `Rewards` (standard) + subtitle **"The lucky draw."** (locked 2026-05-05 — was "the lucky vendor draw" which mixed bazaar metaphor with slot machine; cleaner without "vendor" and reads universally)
- Spin CTA: `Bet`
- Claim CTA: `Claim`
- Symbols (escalating value): 🪙 ×1 → 💰 ×2 → 💎 ×3 → 🏆 ×4 → 👑 ×5

**Multiplier labels:** each reel emoji must show its multiplier directly underneath in micro-text (e.g. `🪙\n×1`). Don't expect users to memorize the multiplier table from a separate panel.

**❌ Banned:** "Lucky vendor draw", "Hawker's wheel", "Stall lottery" — all mix bazaar with slot/casino. Slot machine is universal enough; don't theme it.

### 4.8 Referrals (FR-010)

- Page subtitle: "Bring a friend to the bazaar. Earn when they trade."
- How it works: "Hand out your stall card. When a friend joins and trades, you earn `20%` of their trading fees automatically."
- Referral link prefix: `https://stallspot.app/join/@`
- Stat labels: `Total referrals`, `Total volume`, `Unclaimed rewards` (standard)

### 4.9 Token War / Arena (FR-012)

- Feature page title: `Arena` (keep, universal)
- Sub-title: "Showdown row · back winners · the crowd predicts" (themed)
- Match-up labels: `Stall A vs Stall B` for token war, `[Team A] vs [Team B]` for football, `Yes / No` for events
- Voting CTA: `Back A` / `Back B` (universal, soft, religiously safer than "Bet")

### 4.10 Onboarding & empty states

- Welcome screen: "Welcome to the bazaar — where memes get traded."
- Empty profile: "You're a Newcomer at the bazaar. Make your first trade or open a stall to start earning points."
- Empty token list: "No stalls match. Try a different filter."
- 404: "This stall doesn't exist. Maybe it never opened — or maybe it franchised away."

---

## 5. Component library (canonical patterns)

All Bazaar pages must use the same shell unless explicitly standalone. Canonical reference: `/mockups-bazaar/points.html` and `/mockups-bazaar/leaderboard.html`.

### 5.1 App shell layers

```
[Header (fixed, 60px)]   ← logo + search + wallet (connected/disconnected state) + Create token CTA
[Marquee (fixed, 30px)]  ← branded scroll
[Sidebar (fixed, 240px)] ← Discover/Personal/Earn nav groups + user card at bottom
[Main content]           ← page-specific
```

### 5.2 Sidebar nav structure (canonical — UPDATED)

```
DISCOVER
  · Discover       → token_list_v4.html
  · Arena          → FR-012_TokenWar.html
  · Clubs          → clubs.html
  · Events         → events.html
  · Leader Board   → leaderboard.html       ← MOVED from Personal (logic: public ranking, not personal)

PERSONAL
  · My Profile     → my_profile.html  (with badge if notifications)

EARN
  · Points         → points.html
  · Rewards        → rewards.html
  · Referrals      → referrals.html
  · Stake          → # (no file, placeholder)

[User card at bottom: cat hawker mini avatar + name + tier · pts]
[onclick → my_profile.html]
```

Active state: `class="nav-item active"` — color `var(--bz-amber-400)` + bg `var(--bz-amber-soft)`.

### 5.3 Header wallet state (NEW)

Header bên phải có 2 states. **Default cho mockups = connected** (most flows assume wallet attached).

#### State A: Disconnected

```html
<button class="btn-ghost">Connect wallet</button>
```

Plain ghost button. Click → opens wallet selector modal (Phantom/Solflare/etc — out of scope mockup).

#### State B: Connected (default in mockups)

Pill-shaped component với cat hawker mini avatar + balance + truncated address + network dot + chevron. Click → dropdown menu.

```html
<div class="wallet-connected" onclick="toggleWalletMenu(event)">
  <div class="wc-avatar"><svg>[cat hawker mini]</svg></div>
  <div class="wc-info">
    <div class="wc-balance">12.45 SOL</div>
    <div class="wc-addr">7xK9…mP3q</div>
  </div>
  <span class="wc-net-dot"></span>     <!-- teal = Solana mainnet OK; crimson = wrong network -->
  <svg class="wc-chevron">[chevron-down]</svg>

  <div class="wc-menu">
    <div class="wc-menu-head">
      <div class="wc-menu-net"><span class="wc-net-dot"></span> Solana mainnet</div>
      <div class="wc-menu-bal">12.45 SOL</div>
    </div>
    <a class="wc-item" href="my_profile.html">[icon] My profile</a>
    <button class="wc-item">[icon] Copy address</button>
    <a class="wc-item" href="edit_profile_privacy.html">[icon] Settings</a>
    <div class="wc-divider"></div>
    <button class="wc-item danger">[icon] Disconnect</button>
  </div>
</div>
```

CSS:
- Container: `--surface-2` bg, `--border-2` border, pill radius, height 36px
- Hover: amber border + amber-soft bg
- Avatar: 28px circle với cat hawker (gradient amber bg)
- Balance: amber 400, mono 12.5px bold
- Address: text-3, mono 10.5px
- Net dot: 7px circle, teal (OK) / crimson (wrong network), with halo glow box-shadow
- Chevron: rotate 180° when menu open
- Menu: surface-1 bg, 8px shadow, 220px wide, items có icon + label

Wrong network state: thay class `.wc-net-dot` → `.wc-net-dot.wrong` + có thể add warning text trong `.wc-menu-net`.

Canonical reference file: `/mockups-bazaar/points.html` (đã apply connected state).

### 5.4 Stat card (used in Referrals, Profile, Dashboard)

### 5.3 Stat card (used in Referrals, Profile, Dashboard)

```html
<div class="stat-card">
  <div class="stat-icon"><svg .../></div>
  <div class="stat-meta">
    <div class="stat-label">[STANDARD label]</div>
    <div class="stat-value">[value]<span class="unit">[unit]</span></div>
  </div>
</div>
```

### 5.4 Page header

Two patterns:

**Pattern A — title + subtitle (used on Points, Rewards, Referrals):**
```html
<div class="page-header">
  <h1 class="page-title">[Title — STANDARD]</h1>
  <p class="page-sub">[Subtitle — themed flavor OK]</p>
</div>
```

**Pattern B — title left + value right (used on Points "0/500" pattern):**
```html
<div class="page-header">
  <div class="ph-left">
    <h1>[Title]</h1>
    <p class="ph-sub">[Subtitle]</p>
  </div>
  <div class="ph-right">
    <div class="ph-points-label">[LABEL]</div>
    <div><span class="ph-points-value">N</span><span class="ph-points-next"> / M</span></div>
  </div>
</div>
```

### 5.4b Leaderboard visual hierarchy (locked 2026-05-05)

Top-3 rank cards và table rows hiện cùng dùng `--bz-amber-400` cho creator/owner name → no visual distinction giữa featured vs ranked. Rule:

| Element | Color | Reason |
|---|---|---|
| Top-3 rank card — token/creator name | `var(--bz-amber-400)` | Featured tier — amber commands attention |
| Table row (rank 4+) — token/creator name | `var(--text-1)` (white) | Tabular data — neutral, scan-friendly |
| Table row — rank number column | `var(--text-2)` | De-emphasize ordinal, focus on name |
| Table row — value columns (volume/MC) | `var(--text-1)` mono | Standard data formatting |

This 1-line change creates a clear "podium vs roster" hierarchy without adding new components.

### 5.5 Trust score (FR-013, UNCHANGED)

Bronze/Silver/Gold ladder + Liquidity/Distribution/Creator breakdown. Reuse pattern from `/mockups-v2/_preview/05_token_detail_preview.html`. Do NOT theme tier names or breakdown labels.

### 5.6 Trade panel (FR-003, UNCHANGED)

Buy/Sell tabs, Slippage, You pay, You receive, MAX, Balance, execute button. Canonical pattern in `/mockups-bazaar/token_detail.html`.

---

## 6. Routing map (canonical)

| Element | Target |
|---|---|
| Logo / Stallspot brand | `token_list_v4.html` |
| Sidebar Discover | `token_list_v4.html` |
| Sidebar Arena | `FR-012_TokenWar.html` |
| Sidebar Clubs | `clubs.html` |
| Sidebar Events | `events.html` |
| Sidebar My Profile | `my_profile.html` |
| Sidebar Leader Board | `leaderboard.html` |
| Sidebar Points | `points.html` |
| Sidebar Rewards | `rewards.html` |
| Sidebar Referrals | `referrals.html` |
| Sidebar Stake | `#` (no file) |
| Header Create Token CTA | `create_token.html` |
| User card (sidebar bottom) | `my_profile.html` |
| Token card click | `token_detail.html` |
| Buy button on card | `token_detail.html` |

When implementing new pages, follow the same routing.

---

## 7. SVG asset library

### 7.1 Cat hawker logo (32x32 to 64x64)

```svg
<svg viewBox="0 0 32 32" fill="none">
  <path d="M3 12L16 5L29 12L26 13L16 8L6 13Z" fill="#3a2410" stroke="#3a2410" stroke-linejoin="round" stroke-width="0.5"/>
  <line x1="9" y1="11.5" x2="11" y2="10" stroke="#F5DBA8" stroke-width="0.8"/>
  <line x1="15" y1="9.5" x2="17" y2="8" stroke="#F5DBA8" stroke-width="0.8"/>
  <line x1="21" y1="11" x2="23" y2="9.5" stroke="#F5DBA8" stroke-width="0.8"/>
  <rect x="6" y="13" width="20" height="14" rx="1.5" fill="#3a2410"/>
  <path d="M11 16.5L13 13L15 16.5Z" fill="#EAB552" stroke="#3a2410" stroke-width="0.4"/>
  <path d="M17 16.5L19 13L21 16.5Z" fill="#EAB552" stroke="#3a2410" stroke-width="0.4"/>
  <circle cx="16" cy="20" r="5" fill="#EAB552" stroke="#3a2410" stroke-width="0.5"/>
  <ellipse cx="14.5" cy="19.5" rx="0.7" ry="1" fill="#3a2410"/>
  <ellipse cx="17.5" cy="19.5" rx="0.7" ry="1" fill="#3a2410"/>
  <path d="M15 22 Q16 22.8 17 22" stroke="#3a2410" stroke-width="0.6" fill="none" stroke-linecap="round"/>
</svg>
```

### 7.2 Cat hawker mini (24x24, for user card / inline)

```svg
<svg viewBox="0 0 24 24" fill="none">
  <path d="M3 9L12 5L21 9" fill="#3a2410"/>
  <rect x="5" y="9" width="14" height="11" rx="1" fill="#3a2410"/>
  <circle cx="9.5" cy="14" r="1" fill="#EAB552"/>
  <circle cx="14.5" cy="14" r="1" fill="#EAB552"/>
  <path d="M9 16.5 Q12 17.5 15 16.5" stroke="#EAB552" stroke-width="0.8" fill="none" stroke-linecap="round"/>
</svg>
```

### 7.3 Mascot expression states (TODO for AI gen)

Variations beyond default smile to be created via AI gen, following design brief in `BAZAAR_IMPLEMENTATION_PLAN.md` section 4.3. List: wink, wide-eyed shock, sad, whispering, megaphone hawking, money-eyes, sleeping.

---

## 8. Page inventory & status

Status legend:
- ✅ Built and Bazaar-themed
- ⚠️ Built but needs rework (still PumpFun/Sprout themed)
- ❌ Not built
- 🔄 Deprecated / merge candidate

| Page | File | Status | Notes |
|---|---|---|---|
| Token List (home) | `token_list_v4.html` | ✅ | Canonical home page; gold reference |
| Token Detail | `token_detail.html` | ✅ | Includes Stall story callout |
| Trading Panel | `trading_panel.html` | ✅ | Standalone component, has back-nav |
| My Profile | `my_profile.html` | ✅ | AI-generated, properly themed |
| Public Profile | `public_profile.html` | ✅ | Full app shell, alice_trader profile, 4 tabs, no edit affordances |
| Edit Profile | `edit_profile_privacy.html` | ✅ | Full app shell, avatar + form + privacy toggles, one-time warnings |
| Creator Dashboard | `creator_dashboard.html` | ✅ | Standalone, has back-nav |
| Create Token (wizard) | `create_token.html` | ✅ | 3-step wizard (Create → Trust Score → Finalize), full app shell |
| Leaderboard | `leaderboard.html` | ✅ | Full Bazaar themed |
| Points | `points.html` | ✅ | Includes empty + data state toggle |
| Rewards (slot machine) | `rewards.html` | ✅ | 5 reels with treasure progression |
| Referrals | `referrals.html` | ✅ | Stat cards + link card + table |
| Sidebar (preview only) | `sidebar_navigation.html` | ✅ | Component preview file |
| Token War | `FR-012_TokenWar.html` | ✅ | Has Bazaar shell |
| Token War — Prediction | `FR-012b_TokenWar_PredictionMarket.html` | ✅ | Has Bazaar shell |
| Clubs | `clubs.html` | ✅ | Has Bazaar shell |
| Events | `events.html` | ✅ | Has Bazaar shell |
| Home full layout | `home_full_layout.html` | ✅ | Deprecated — meta-redirect to token_list_v4.html |
| Stake | — | ❌ | No file. Sidebar links to `#`. Build later khi feature ready |

---

## 9. Pending pages — implementation specs

> ✅ **All 4 pending pages are now built** as of 2026-05-04 update. Specs below are kept as historical reference + reusable templates if features need expansion.

### 9.1 `create_token.html` — 3-step wizard (HIGH PRIORITY)

**Source of truth:** 3 MVP screenshots provided by user. Reference also `mockups/create_token_mockup.html` for component patterns (current standalone single-form).

**Structure:** 3-step wizard với progress indicator, fixed at top of main content.

#### Step 1: Create New Token

**Title:** "Create New Token" (centered)
**Above title:** "ⓘ Deployment Cost Info" pill (small) + settings gear icon top-right

**Form fields:**
- Token Name (text input, required)
- Token Symbol (text input, required, side-by-side với Name in 2-col)
- Token Description (textarea)
- Token Image (upload zone with cloud icon + "Upload a file" / "or drag and drop", validation "PNG, JPG, GIF up to 1MB")
- Social Media Links (Optional) — collapsible accordion với chevron-down, default collapsed

**CTA:** "Next" button at bottom (full width, gradient amber on hover state). Disabled until name + symbol filled.

#### Step 2: Trust Score Setting

**Title:** "Trust Score Setting" (centered)

**Sub-section 1: Vesting Plan — Tokenomics**
- Right-aligned: "Complete all → 🥉 Bronze"
- Initial Supply (text input, default 1000000000)
- Mint Authority (text input, "Wallet address / program id" placeholder)
- 3 sliders side-by-side với % display:
  - Creator % (default 40%)
  - Community % (default 40%)
  - Liquidity % (default 20%)
- Validation: "Sum: 100% (must be 100%)" — green nếu = 100%, red nếu khác
- Checkbox: "Renounce mint authority"

**Sub-section 2: Freeze Authority**
- Right-aligned: "Complete → 🥈 Silver (+20% trust)"
- Radio: Enable / Disable + info icon

**Sub-section 3: LP Lock**
- Right-aligned: "Complete → 🥇 Gold"
- 3 pill buttons: "No lock" (active default amber pill) / "1 month" / "6 months"

**Bottom row:**
- Left: "Check Trust Score" link button + "Badge: —" text (updates as user completes sections)
- Right: "Back" button + "Next" button (gradient amber)

#### Step 3: Finalize

**Title:** "Finalize" (centered)

**Tip section:**
"Tip:
Optional: Make an initial buy to gain the most from your token"

**Initial buy input:**
- Big "0.00" placeholder (centered, large 80px font)
- Quick amount buttons row: "0.1" | "0.5" | "1" | "MAX"
- Below: "BUY" button (full width, disabled state until amount entered)

**Bottom:**
- "Back" button
- "Create Without Buying" button (gradient amber, primary action)

**Microcopy notes:**
- All labels (Token Name, Symbol, etc.) → STANDARD
- Title "Create New Token" → KEEP standard (user needs to know what they're doing)
- Button labels (Next, Back, Buy, Create Without Buying) → STANDARD
- Trust Score badges (Bronze/Silver/Gold) → STANDARD per FR-013
- Tip text "Make an initial buy" → STANDARD
- Sub-section header "Vesting Plan — Tokenomics" → STANDARD
- Validation message "must be 100%" → STANDARD

**Theme touches (light):**
- Page subtitle on Step 1 (small, below title): "Open your stall. Pitch your meme to the bazaar." — themed flavor, optional
- Welcome empty state (before user starts wizard): can be themed

**Layout:** App shell với header + marquee + sidebar (Create Token nav active in sidebar — but Stallspot doesn't have Create Token in sidebar, it's the header CTA. Just keep Discover or no active state).

**Code template:** Use `points.html` or `referrals.html` shell. Form patterns: refer `mockups/create_token_mockup.html` (older Sprout) for input/textarea/upload styling — apply Bazaar palette.

#### Step indicator (top of all 3 steps)

Optional but recommended: show "Step 1 of 3" or visual breadcrumb at top so user knows progress.

---

### 9.2 `public_profile.html` — REWORK

**Current state:** Title "Public Profile - PumpFun", body wrapped only with floating back-nav. No app shell.

**Action:** Replace entire file with full app shell + page content. Reference structure from `my_profile.html` (already Bazaar themed).

**Differences from My Profile:**
- No "edit" buttons
- No private settings
- "Follow / Unfollow" button if applicable
- Show only public-facing stats (created tokens, holdings if public, referral count, badges)
- Title format: `[Username]` (without "My")
- Header subtitle: e.g. "alice · Vendor tier · joined 12d ago"

**Source MVP:** Request screenshot from user if MVP `/profile/[wallet]` view exists, or reuse my_profile structure with edit affordances removed.

---

### 9.3 `edit_profile_privacy.html` — REWORK

**Current state:** Title "Edit Profile - PumpFun", body wrapped only với floating back-nav. No app shell.

**Action:** Replace với full app shell + form sections. Reference `mockups/edit_profile_privacy_mockup.html` for fields list, apply Bazaar palette.

**Sections:**
- Display name (input, one-time editable per CLAUDE.md rules — show warning)
- Username (input, one-time editable)
- Bio (textarea)
- Avatar (upload)
- Privacy section (toggles: profile public/private, show holdings, show referral activity, etc.)
- Notification preferences

**Microcopy:** all labels STANDARD (these are critical user settings). Page title: "Edit profile" — standard.

---

### 9.4 `home_full_layout.html` — DEPRECATE

**Current state:** Title "Home - PumpFun", h1 "Discover Tokens" — same as `token_list_v4.html`.

**Decision:** Replace content with simple meta-redirect or message:
```html
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="refresh" content="0; url=token_list_v4.html">
  <title>Stallspot</title>
</head>
<body>
  Redirecting to <a href="token_list_v4.html">home</a>...
</body>
</html>
```

Or delete the file entirely if no other file references it. Routing map already points to `token_list_v4.html` as home.

---

## 10. File structure (current)

```
PMFCDocument/
├── BAZAAR_UI_SPEC.md                       ← THIS FILE (single source of truth for design)
├── BAZAAR_IMPLEMENTATION_PLAN.md           ← Migration process plan
├── CLAUDE.md                               ← Project context
├── Function Requirements.md                ← Sprout FRD (older)
├── Function Requirements - Bazaar.md       ← (to be created by agent — diff of FRD_Updated)
├── docs/
│   ├── FRD_Updated.md                      ← MVP-aligned FRD (use as functional spec)
│   ├── FR-001…FR-016 individual specs
│   └── ...
├── images/                                 ← MVP screenshots
├── mockups/                                ← Sprout (older)
├── mockups-v2/_preview/                    ← Sprout (newer, gold reference for layout)
└── mockups-bazaar/                         ← Bazaar mockups (this design system applies here)
    ├── token_list_v4.html                  ✅
    ├── token_detail.html                   ✅
    ├── trading_panel.html                  ✅
    ├── my_profile.html                     ✅
    ├── public_profile.html                 ⚠️ rework needed
    ├── edit_profile_privacy.html           ⚠️ rework needed
    ├── creator_dashboard.html              ✅
    ├── create_token.html                   ⚠️ rework to 3-step wizard
    ├── leaderboard.html                    ✅
    ├── points.html                         ✅
    ├── rewards.html                        ✅
    ├── referrals.html                      ✅
    ├── sidebar_navigation.html             ✅
    ├── FR-012_TokenWar.html                ✅
    ├── FR-012b_TokenWar_PredictionMarket.html ✅
    ├── clubs.html                          ✅
    ├── events.html                         ✅
    └── home_full_layout.html               🔄 deprecate
```

---

## 11. Working with this spec — for AI agents

### When implementing a new page

1. **Read this file in full first.**
2. **Reference live MVP** at `https://fe-dev.pumpfunclone2025.win/` (or request screenshot from user if can't access).
3. **Reuse app shell** (header + marquee + sidebar) from canonical files: `points.html`, `leaderboard.html`, `referrals.html`, `rewards.html`.
4. **Apply 3-layer principle** (section 2): theme only at brand + gamification + signature moments. Core UI stays standard.
5. **Use color palette + typography** (section 1) without modification. Don't introduce new tokens.
6. **Test microcopy** against the 5 questions:
   - Will user parse this in <2s for trade decision? → STANDARD
   - Is this in chart/trade panel/trust score? → STANDARD
   - Is this tier name / achievement / brand voice? → can theme
   - Will B1 ESL reader (Turkey/Nigeria/Indonesia) parse in 2s? → if no, simplify
   - Does FRD say one thing and MVP show another? → follow MVP

### When extending microcopy

- Add new strings to section 4 (microcopy library) of this file.
- Search-replace existing files for consistency.

### When unsure

- **STOP and ASK user**. Don't guess. Cost of one question = 5 minutes. Cost of guessing wrong = redoing entire page.

### When refactoring file structure

- Update this spec's section 10 (file structure) to reflect changes.
- Update routing map (section 6) if any path changes.

---

## 12. Changelog

- **2026-05-04 (initial)** — Spec created. Pages built: token_list, token_detail, trading_panel, my_profile, creator_dashboard, leaderboard, points, rewards, referrals, sidebar_nav, FR-012/012b, clubs, events. Pending: create_token rework (3-step wizard), public_profile rework, edit_profile_privacy rework, home_full_layout deprecate.
- **2026-05-04 (update)** — All 4 pending pages completed by AI agent. PumpFun residue cleaned in creator_dashboard + sidebar_navigation. **Sidebar restructured**: Leader Board moved from Personal → Discover group (logic: public ranking, not personal). **Connected wallet state component added** to all 14 sidebar-equipped files (replaces "Connect wallet" button). New section 5.3 documents both wallet states + dropdown menu structure. Status updated below.
- **2026-05-04** — Completed all 4 pending pages. create_token.html: 3-step wizard (Create New Token → Trust Score Setting → Finalize) with step indicator, sliders, pill buttons, upload zone. public_profile.html: full app shell, 4 tabs (Profile Info / Holding / Created / TX), alice_trader sample data. edit_profile_privacy.html: full app shell, avatar upload, one-time-editable warnings for Username/Display Name, privacy toggles. home_full_layout.html: deprecated with meta-redirect. All pages pass routing and PumpFun=0 brand checks.
- **2026-05-05 (Group A pitch-readiness lock)** — 5 design decisions locked from `/design:design-critique` review:
  - **Tagline split by surface** (section 1.1): hero = "Trade memes at the bazaar.", creator funnel = "Open a stall. Pitch your meme.". Compound "Open a stall. Trade memes." deprecated.
  - **Mascot sizing tokens** (section 1.5): `--mascot-sm/md/lg` = 22/30/40px. All future renders use tokens, not arbitrary px.
  - **Creator attribution surface-restricted** (section 4.4): "stall by" only on hero/pitch surfaces; data tables use plain "by alice".
  - **Rewards subtitle simplified** (section 4.7): "The lucky draw." Multiplier labels required under each reel emoji.
  - **Leaderboard visual hierarchy** (new section 5.4b): top-3 keep amber name, table rows desaturate to `--text-1`.
  - Implementation tracked via `BAZAAR_GROUP_A_FIXES_PLAN.md`.
- **2026-05-06 — Group A fixes implemented** per `BAZAAR_GROUP_A_FIXES_PLAN.md`. All 5 tasks pass verification.
  - Task 1: `create_token.html` wiz-sub → `"Open a stall. Pitch your meme."`. `token_list_v4.html` page-subtitle → `"Trade memes at the bazaar."`. Zero residue of deprecated `"Open a stall. Trade memes."` across all 18 files.
  - Task 2: `--mascot-sm/md/lg` (22/30/40px) tokens added to all 17 CSS-bearing HTML files. `.logo-mascot` 34px → `var(--mascot-lg)`, `.user-mascot` 34px → `var(--mascot-lg)`, `.wc-avatar` 28px → `var(--mascot-md)`. `FR-012b` edge: required standalone `:root` block (no `--sidebar-w` pattern to anchor on).
  - Task 3: `"stall by"` replaced with `"by"` in all 6 token cards in `token_list_v4.html`. Leaderboard top-3 podium cards retain `"stall by"` (spec 4.4 hero surface rule). No residue in data table rows.
  - Task 4: `rewards.html` subtitle `"lucky vendor draw"` → `"The lucky draw."`. `.reel-multiplier` CSS added; `×1–×5` labels injected under each reel emoji. `.reel-cell` updated to flex column layout for stacking.
  - Task 5: `leaderboard.html` `.lb-row-name` color `var(--bz-amber-400)` → `var(--text-1)`. Top-3 `.lb-token-name` (podium cards) unmodified — retains amber.
- **2026-05-06 — Sidebar polish mirrored from Sprout (17 files):** footer utility block added below user card (Telegram + X icons, Doc/FAQ/How-it-works pills, `© 2026 Stallspot` copyright); active item amber glow (`box-shadow: 0 0 16px rgba(234,181,82,0.18)`); group label amber dot (`.nav-label::before` 4px dot, `letter-spacing: 0.12em`); user card amber border-top + glow (`border-top: 1px solid rgba(234,181,82,0.20)`, `box-shadow: 0 0 20px rgba(234,181,82,0.10)`); hover lift on inactive nav items (`translateY(-1px)` + amber-soft bg, `transform: none` on active); stat badges 642/12 removed if present. Icons remain amber per brand — no teal icon change. Architecture parity with Sprout sidebar maintained. Applied via `scripts/final_sidebar_polish.py`.

---

## 13. Cross-references

- **Sprout variant spec:** `/SPROUT_UI_SPEC.md` (parallel theme, mirror architecture)
- **Process plan for migration:** `/BAZAAR_IMPLEMENTATION_PLAN.md` (section 5 = three-layer principle, section 6 = full microcopy library, section 7 = reusable code snippets)
- **Functional spec:** `/docs/FRD_Updated.md` (MVP-aligned, 16/04/2026)
- **Project context:** `/CLAUDE.md`
- **Brand-swap script:** `/scripts/clone_to_sprout.py` (regenerate `/mockups-sprout/` from `/mockups-bazaar/`)
- **Sprout reference (older):** `/mockups-v2/_preview/04_token_list_preview_v4.html` (token list), `/mockups-v2/_preview/05_token_detail_preview.html` (detail) — REFERENCE ONLY for layout patterns

---

**End of spec.** Future updates: append to changelog (section 12), update sections in place, never duplicate content. Keep this file as the canonical reference.
