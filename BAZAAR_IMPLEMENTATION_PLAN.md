# BAZAAR Theme — Implementation Plan

> **For:** Antigravity AI agent (Claude Opus 4.6) with full file access to project directory
> **Goal:** Tạo phiên bản Bazaar parallel với Sprout hiện có, để team compare 2 themes và chọn 1
> **Scope:** Re-skin theme only — KHÔNG thay đổi BE/FE function. Layout/component/architecture giữ 100%
> **Read this file in full before starting any work.**

---

## 0. Mission

Hiện project đang dùng theme **Sprout / Garden** (mascot cây con, palette peach + teal). Đề xuất parallel theme **Stallspot / Bazaar** (mascot cat hawker, palette amber + brown). Cần tạo bản Bazaar đầy đủ song song với bản Sprout hiện có để team so sánh và quyết định.

**Outcomes (file deliverables):**

1. Folder `/mockups-bazaar/` chứa 14+ HTML mockups re-skin từ `/mockups/` và `/mockups-v2/_preview/`
2. File `/Function Requirements - Bazaar.md` ở root level (mirror naming của `/Function Requirements.md`), source diff từ `/docs/FRD_Updated.md` (MVP-aligned)
3. Update `/CLAUDE.md` để aware về 2 theme variants + clarify rằng có nhiều FRD files với mức độ current khác nhau
4. Optional: `/themes-bazaar/BRAND_GUIDELINES.md` nếu agent thấy có giá trị tách riêng

**KHÔNG cần làm:**

- Update `/testing/` folder (skip cho giờ — tests đang theme-agnostic)
- Update existing Sprout files (Sprout giữ 100% như đang có)
- Build/compile bất kỳ thứ gì — đây là document & mockup only

---

## 1. Context

### Existing project structure

```
PMFCDocument/
├── CLAUDE.md                    ← Project context (sẽ update)
├── Function Requirements.md     ← Sprout-themed FRD (giữ nguyên)
├── README.md
├── /docs/                       ← Individual FRs
│   ├── FR-001_TokenList.md … FR-016_ClubWar.md
│   ├── DiscoverScore.md
│   ├── PUMPFUN_PROJECT_SUMMARY.md
│   └── ...
├── /design/UI_UX_DESIGN_SYSTEM.md
├── /mockups/                    ← Sprout HTML mockups (14 files, giữ nguyên)
├── /mockups-v2/_preview/        ← Sprout mockups newer (5 files, giữ nguyên)
├── /images/                     ← MVP screenshots (image-1.png … image-25.png)
├── /testing/                    ← Test docs (skip)
└── /BAZAAR_IMPLEMENTATION_PLAN.md  ← THIS FILE
```

### After implementation

```
PMFCDocument/
├── CLAUDE.md                                    ← Updated multi-theme aware
├── Function Requirements.md                     ← Sprout (unchanged)
├── Function Requirements - Bazaar.md            ← NEW
├── /mockups/                                    ← Sprout (unchanged)
├── /mockups-v2/_preview/                        ← Sprout (unchanged)
├── /mockups-bazaar/                             ← NEW (14+ files)
└── ...
```

### CRITICAL: Source of truth hierarchy

**Source of truth = MVP live + FRD_Updated.md. Sprout mockups chỉ là REFERENCE cho layout/component patterns, KHÔNG phải source of truth.**

| Priority | Source | Use for |
|---|---|---|
| **1 (highest)** | **MVP live** tại `https://fe-dev.pumpfunclone2025.win/` | **Functional ground truth**: cái gì thực sự có/không có trong UI, trạng thái nào, behavior ra sao |
| **2** | **`/docs/FRD_Updated.md`** | Functional spec (16/04/2026, MVP-aligned). Cross-reference với MVP khi cần |
| **3** | **User-provided screenshots** (request khi agent cần) | Khi MVP feature không thể access trực tiếp — STOP và ASK user gửi screenshot, KHÔNG đoán |
| **4** | `/images/image-*.png` (existing MVP screenshots) | Backup reference nếu đã có sẵn |
| **5 (reference only)** | `/mockups-v2/_preview/*.html`, `/mockups/*.html` | **REFERENCE ONLY** cho layout/component/spacing. KHÔNG phải authority về functionality. Có thể đã drift khỏi MVP |

**Anti-pattern:** Agent dùng Sprout mockup để quyết định "MVP có feature X không" — sai. Sprout mockup là design exploration, không phải spec. Always check MVP live hoặc FRD_Updated first.

**Uncertainty handling:** Khi agent không sure về MVP behavior (vd: state X trông thế nào, button Y có không, flow Z ra sao), agent **STOP và ASK USER** gửi screenshot trực tiếp. KHÔNG inference từ Sprout mockup. KHÔNG guess.

### Reference materials — recommended reading order

**Phase 1 (foundation — MVP first):**
1. **Visit MVP live**: `https://fe-dev.pumpfunclone2025.win/` — agent thử WebFetch hoặc browser tool. Nếu có web access → screenshot key pages. Nếu không → request user gửi screenshots.
2. **Read `/docs/FRD_Updated.md`** thoroughly — MVP-aligned functional spec, source for Bazaar FRD diff.
3. Browse `/images/image-*.png` — existing screenshots if any pages.
4. **List uncertainties**: trước khi bắt tay re-skin, agent compile danh sách screens/states không chắc về MVP behavior, request user gửi screenshots.

**Phase 2 (reference — for layout/component patterns ONLY):**
5. `/mockups-v2/_preview/04_token_list_preview_v4.html` — Sprout token list. **Use cho:** layout, spacing, component structure. **KHÔNG use cho:** quyết định feature có/không.
6. `/mockups-v2/_preview/05_token_detail_preview.html` — Sprout token detail. Same caveat.
7. `/mockups/home_full_layout.html`, `/mockups/sidebar_navigation.html` — header + sidebar layout reference.
8. Other files in `/mockups/` for component patterns.

**Phase 3 (project context):**
9. `/CLAUDE.md` — project overview.

---

## 2. Locked decisions (DO NOT REOPEN)

These were decided through extensive discussion. Agent should not re-debate:

| Element | Locked value |
|---|---|
| Theme name | **Stallspot** |
| Theme subtitle | **the meme bazaar** |
| Tagline | **"Open a stall. Trade memes."** |
| Mascot direction | **Cat hawker behind quầy hàng** (single character, multiple expression states) |
| Tier ladder (FR-011) | **Newcomer → Regular → Local → Insider → Legend** |
| Trust Score (FR-013) | **UNCHANGED** — Bronze/Silver/Gold + Liquidity/Distribution/Creator |
| Trade panel (FR-003) | **UNCHANGED** — Buy/Sell + standard crypto vocab |
| Layout & components | **UNCHANGED** — same header 60px, marquee 30px, sidebar 240px, token grid 320px+ |
| Target market | Nigeria / Indonesia / Philippines / Thailand (newbie + retail), with global readability requirement |

---

## 3. Brand specification

### 3.1 Brand identity

| Field | Value |
|---|---|
| Brand name | Stallspot |
| Subtitle | the meme bazaar |
| Tagline (primary) | Open a stall. Trade memes. |
| Tagline (alt for marketing) | The meme bazaar. |
| Brand archetype | Everyman + Creator (welcoming, hustle, attention-as-currency) |

### 3.2 Color palette

```css
:root {
  /* Brand primary — amber/gold (warm, vendor lantern) */
  --bz-amber-100: #F5DBA8;   /* lightest, gradient top */
  --bz-amber-200: #FAC775;   /* hover */
  --bz-amber-400: #EAB552;   /* primary CTA, brand color */
  --bz-amber-500: #C49152;   /* darker shade, brass seal */
  --bz-amber-soft: rgba(234, 181, 82, 0.10);  /* tints */

  /* Brand secondary — brown (counter, structural) */
  --bz-brown-300: #8B5A3C;   /* wood seal */
  --bz-brown-500: #5a3818;   /* counter shadow */
  --bz-brown-700: #3a2410;   /* counter, eyes/dark elements */

  /* Cream highlight */
  --bz-cream: #F5DBA8;       /* awning stripes accent */

  /* Accent green (preserved from Sprout for SUCCESS / "OK" semantics) */
  --bz-teal-300: #9ED8B8;
  --bz-teal-400: #7CC4A4;    /* success, "Just opened" badge, buy color */
  --bz-teal-500: #5BA886;

  /* Crimson — danger / sell */
  --bz-crimson: #D65A54;

  /* Surface dark theme (UNCHANGED from Sprout - dark crypto convention) */
  --bg:        #0a0e1a;      /* page bg */
  --surface-1: #131826;      /* card surface */
  --surface-2: #1a2138;      /* nested surface */
  --surface-3: #232b46;
  --border-1:  #1f2640;
  --border-2:  #2a3456;

  /* Text (unchanged) */
  --text-1: #f4f4f5;
  --text-2: #a1a1aa;
  --text-3: #71717a;
  --text-mute: #52525b;
}
```

**Replacement map từ Sprout:**

- `--peach-300/400/500` → `--bz-amber-100/200/400`
- `--peach-soft` → `--bz-amber-soft`
- `--teal-*` giữ nguyên (Bazaar reuse cho success states)
- `--amber-400` cũ (Sprout dùng cho "amber gradient almost there") → `--bz-amber-400` (cùng giá trị, đổi tên)

### 3.3 Typography (UNCHANGED from Sprout)

```css
--font-display: 'Plus Jakarta Sans', system-ui, sans-serif;  /* brand, headlines */
--font-body:    'Inter', system-ui, sans-serif;              /* body */
--font-mono:    'JetBrains Mono', 'SF Mono', monospace;      /* prices, addresses */
```

Weights, sizes, scales: giữ nguyên 100% như Sprout.

### 3.4 Iconography rules

- Status indicator dots / pills / shields: **standard semantic colors** (teal=success, amber=caution, crimson=danger). KHÔNG đổi.
- Brand icon (logo): cat hawker (xem section 4)
- Decorative elements: minimal — UI là financial product, không decorate quá đà.

---

## 4. Mascot brief — Cat hawker

### 4.1 Concept

Một con mèo (cat) đứng sau quầy hàng truyền thống có mái hiên (awning), hai mắt to expressive, đầu hơi nghiêng dễ thương kiểu meme. Mèo là vendor friendly đang chào mời khách. Quầy hàng có 2 tai mèo nhô lên trên counter (nhận diện thương hiệu chính), counter dark brown, awning amber.

### 4.2 Logo — primary mark (32x32 to 64x64 SVG)

Đã có reference SVG trong các show_widget mockups. Design:

```svg
<svg viewBox="0 0 64 64" fill="none">
  <!-- Awning -->
  <path d="M5 22L32 12L59 22L54 24L32 16L10 24Z" fill="#3a2410" stroke="#3a2410" stroke-linejoin="round" stroke-width="0.5"/>
  <!-- Awning stripes (cream highlights) -->
  <line x1="14" y1="20" x2="20" y2="17" stroke="#F5DBA8" stroke-width="1.2"/>
  <line x1="26" y1="15" x2="32" y2="13" stroke="#F5DBA8" stroke-width="1.2"/>
  <line x1="38" y1="13" x2="44" y2="15" stroke="#F5DBA8" stroke-width="1.2"/>
  <line x1="50" y1="17" x2="56" y2="20" stroke="#F5DBA8" stroke-width="1.2"/>
  <!-- Counter (dark brown) -->
  <rect x="10" y="24" width="44" height="32" rx="2" fill="#3a2410"/>
  <!-- Cat ears (peeking above counter) -->
  <path d="M24 30L26 25L28 30Z" fill="#EAB552" stroke="#3a2410" stroke-width="0.5"/>
  <path d="M36 30L38 25L40 30Z" fill="#EAB552" stroke="#3a2410" stroke-width="0.5"/>
  <!-- Cat face (round, amber) -->
  <circle cx="32" cy="40" r="9" fill="#EAB552" stroke="#3a2410" stroke-width="0.7"/>
  <!-- Eyes -->
  <ellipse cx="28.5" cy="38.5" rx="1.3" ry="1.7" fill="#3a2410"/>
  <ellipse cx="35.5" cy="38.5" rx="1.3" ry="1.7" fill="#3a2410"/>
  <!-- Mouth (small smile) -->
  <path d="M30 43 Q32 44.5 34 43" stroke="#3a2410" stroke-width="1" fill="none" stroke-linecap="round"/>
  <!-- Whiskers -->
  <line x1="22" y1="40" x2="27" y2="40" stroke="#3a2410" stroke-width="0.5"/>
  <line x1="37" y1="40" x2="42" y2="40" stroke="#3a2410" stroke-width="0.5"/>
</svg>
```

Logo dùng trong header (32-34px tile), favicon (16x16, có thể simplify).

### 4.3 Mascot expression states (8 variants)

Cho marketing / sticker pack / signature moments. Agent có thể AI-gen 8 expression states hoặc viết SVG cho từng state. Mỗi state là cùng cat hawker nhưng đổi biểu cảm:

| # | State | Use case | Visual cue |
|---|---|---|---|
| 1 | Default smile | Logo, default avatar | Eyes regular, small smile |
| 2 | Wink + smile | Welcome / onboarding | Một mắt nhắm, smile rộng hơn |
| 3 | Wide-eyed shock | Token pumping / big move | Mắt to tròn, mouth open |
| 4 | Sad face | Token rugged / down | Mắt droopy, mouth turned down |
| 5 | Whispering (paw to mouth) | Alpha / tips state, "TIPS WHISPERED HERE" marquee | Paw raised to side of mouth, eyes half-closed |
| 6 | Megaphone hawking | Promotional / launch state | Cat with megaphone or paw cupped to mouth, eyes wide |
| 7 | Money eyes (dollar signs) | Win / graduation moment | $ in eyes |
| 8 | Sleeping | Idle / "no activity" state | Eyes closed, slight Z |

Mascot signature đặc điểm:
- Always cat behind quầy hàng (counter visible)
- Awning amber với cream stripes
- Two tail/ear silhouettes giống nhận diện
- Color palette stick: amber face/ears, brown counter, cream stripes

### 4.4 Banned mascot variations

- KHÔNG cat without counter (mất bazaar context)
- KHÔNG add hat / clothing (over-design, hard to AI-gen consistently)
- KHÔNG breed-specific cat (just generic cute cat)
- KHÔNG religious symbols, alcohol, gambling references (Indonesia Muslim majority concern)

---

## 5. Three-layer theme principle (CRITICAL — read carefully)

Đây là quy tắc governance cho TẤT CẢ microcopy decisions. Agent phải apply nguyên tắc này khi re-skin từng mockup.

### 5.1 Layer 1 — Brand identity (THEME 100%)

**Áp dụng:** logo, brand name, tagline, marquee, mascot, brand voice trong marketing/social.

**Test:** "User có cần parse trong <2 giây để quyết định trade không?" → KHÔNG → có thể theme.

### 5.2 Layer 2 — Gamification identity & signature moments (THEME có chọn lọc)

**Áp dụng:**
- Tier ladder names trên user card / profile / leaderboard
- Stand-alone celebration moments (graduation event banner)
- Stall story callout trên token detail (creator pitch)
- Token War event naming (FR-012)
- Slot Rewards naming (FR-009)
- Referral copy (FR-010)
- Onboarding flow microcopy ("Welcome to the bazaar")

**Test:** User encounters this slowly, has context buffer → có thể theme.

### 5.3 Layer 3 — Core trading UI (STANDARD, không đổi)

**KHÔNG ĐƯỢC THEME:**
- CTAs critical: "Create token", "Connect wallet", "Buy", "Sell"
- Status badges affecting trade decisions: "New", "Almost graduated", "Live", "Graduated"
- Data labels: Volume 24h, Market cap, Liquidity, Holders, Total supply, Current price, 24h % change
- Trades log labels: BUY / SELL
- Trust Score & breakdown: Bronze/Silver/Gold + Liquidity/Distribution/Creator (per FR-013)
- Chart toolbar: 5m, 1h, 1d, MA, EMA, BOLL, RSI, SOL/USD, MarketCap/Price
- Trade panel: Slippage, You pay, You receive, MAX, Balance
- Tab navigation: Trending, Market Cap, New, Graduated, Trending Arena
- Address fields: Contract, Deployer

**Test:** "User cần parse trong <2 giây để quyết định trade?" → CÓ → standard, không đổi.

---

## 6. Microcopy library (exhaustive)

Tất cả strings themed cần thay. Strings không có trong list này → KHÔNG thay.

### 6.1 Brand bar

| Element | Sprout (current) | → | Bazaar (new) |
|---|---|---|---|
| Brand name | Sprout | → | Stallspot |
| Brand subtitle | (none) | → | the meme bazaar |
| Logo SVG | Sprout cây con | → | Cat hawker (xem section 4.2) |
| Tagline | Plant your seed in the memeconomy | → | Open a stall. Trade memes. |
| Search placeholder | Search the garden — tokens, creators, addresses… | → | Search the bazaar — tokens, vendors, addresses… |

### 6.2 Marquee text

**Sprout (current):**
```
PLANT YOUR SEED · WATCH WHAT'S BLOOMING · NO BOT DRAMA · MAKE MONEY ON THE MEMECONOMY
```

**Bazaar (new):**
```
OPEN A STALL · TRADE MEMES · WATCH THE CROWD · NO RIGGED SCALES · BIGGEST CROWD WINS · TIPS WHISPERED HERE
```

**Color rules:**
- "OPEN A STALL", "WATCH THE CROWD", "TIPS WHISPERED HERE" → amber primary (`#EAB552`)
- "BIGGEST CROWD WINS" → teal accent (`#7cc4a4`)
- Others → muted gray (`#71717a`)

### 6.3 Tier ladder (FR-011 Points System)

| Tier index | Sprout name | Sprout pts | → | Bazaar name | Bazaar pts |
|---|---|---|---|---|---|
| 1 | 🌱 Seed | 0 | → | Newcomer | 0 |
| 2 | 🌿 Sprout | 500 | → | Regular | 500 |
| 3 | 🌳 Sapling | 2,000 | → | Local | 2,000 |
| 4 | 🌲 Tree | 10,000 | → | Insider | 10,000 |
| 5 | 🪷 Ancient Tree | 50,000 | → | Legend | 50,000 |

**Migration mapping:** 1-1 by index. Points không đổi. User existing ở tier 3 (Sapling) sẽ thành Local.

**KHÔNG dùng emoji** trong Bazaar tier names. Sprout emoji là tree/plant emoji. Bazaar tier dùng plain text. Nếu muốn icon, dùng small SVG hawker silhouette (tier 1 mặt mèo nhỏ → tier 5 mặt mèo lớn + crown small detail).

### 6.4 Status badges (token card)

| Sprout | → | Bazaar | Layer | Notes |
|---|---|---|---|---|
| "Just sprouted" | → | **"New"** | core | Đổi sang STANDARD vì status ảnh hưởng trade decision |
| "Almost there" (amber gradient) | → | **"Almost graduated"** | core | Standard term across all post-PumpFun launchpads |
| (no specific badge for hovered) | → | (no change) | — | |

### 6.5 Token detail — creator info

| Sprout | → | Bazaar |
|---|---|---|
| "by alice" | → | "stall by alice · Local tier · 12d ago" |

Format breakdown:
- "stall by" — themed framing (gamification layer)
- "alice" — username (data, unchanged)
- "Local tier" — themed tier name (gamification layer)
- "12d ago" — standard relative time

### 6.6 Token detail — Stall story (NEW component)

Add small callout component giữa chart card và trades table. Format:

```
┌───────────────────────────────────────────────┐
│ [cat icon]  STALL STORY                       │
│             "Real degen energy on Solana.     │
│              Built for the crowd, by the      │
│              crowd. Stop by, stay for the     │
│              buzz." — alice                   │
└───────────────────────────────────────────────┘
```

CSS reference (themed, amber border-left, italic body):

```html
<div class="story">
  <div class="story-icon"><!-- cat hawker mini --></div>
  <div class="story-body">
    <span class="story-label">STALL STORY</span>
    <p class="story-text">"<creator's pitch text>" — <span class="by">alice</span></p>
  </div>
</div>
```

```css
.story {
  background: rgba(234,181,82,0.06);
  border: 1px solid rgba(234,181,82,0.2);
  border-radius: 10px;
  padding: 10px 12px;
  display: flex; gap: 10px; align-items: flex-start;
}
.story-label { font-size: 10px; color: #EAB552; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; }
.story-text { font-size: 12px; color: #f4f4f5; margin-top: 3px; line-height: 1.55; font-style: italic; }
.story-text .by { color: #a1a1aa; font-style: normal; }
```

**Content source:** dùng existing token description từ FR-007 Create Token wizard. Field name: `token.description` được hiển thị trong format này thay vì plain paragraph.

### 6.7 Graduation moment (signature event)

**Sprout current:** likely simple "Graduated to DEX" notification.

**Bazaar new:**

```
GRADUATED · NOW ON RAYDIUM
[cat hawker money-eyes mascot]
[Token Name] has franchised across the bazaar. Trading on Raydium DEX.
```

Bao gồm:
- Headline: "GRADUATED · NOW ON RAYDIUM" (standard, factual)
- Subtitle line 1: "[Token Name] has franchised across the bazaar." (themed flavor)
- Subtitle line 2: "Trading on Raydium DEX." (standard fact)
- Visual: cat hawker mascot money-eyes state (state #7)
- Color: amber gradient background với teal accent
- Trigger: bonding curve hits $69K MC threshold

### 6.8 Slot Rewards (FR-009)

| Element | Sprout current | → | Bazaar new |
|---|---|---|---|
| Feature name | Slot Rewards / Slot Machine | → | Lucky Vendor Draw |
| CTA button | Spin / Play | → | Roll the dice (or Spin if matching ngắn hơn) |
| Win message | You won X! | → | The bazaar smiles on you — X! |
| Lose message | Try again | → | The crowd's distracted — try again |

Mechanics: KHÔNG đổi. Probability, payout, rotation logic giữ nguyên.

### 6.9 Referrals (FR-010)

| Element | Sprout | → | Bazaar |
|---|---|---|---|
| Headline | Refer friends, earn rewards | → | Bring a friend to the bazaar |
| Body copy | Earn 5% of trading fees | → | Earn 5% commission when they trade at your stall |
| Referral code label | Your referral code | → | Your stall card |
| Share CTA | Share link | → | Hand out your stall card |

Mechanics: 5% commission unchanged.

### 6.10 Token War (FR-012)

| Element | Sprout | → | Bazaar |
|---|---|---|---|
| Feature name | Token War / Arena | → | Bazaar Showdown (or keep "Arena" + flavor copy) |
| Match-up label | Token A vs Token B | → | Stall A vs Stall B |
| Voting CTA | Bet on A / Bet on B | → | Back A / Back B (more universal than "bet") |
| Outcome | Winner | → | Crowd favorite |

Mechanics, betting model, payout: KHÔNG đổi (per FR-012 Mixed Model).

### 6.11 Onboarding flow

**Welcome screen (first-time user):**
- Headline: "Welcome to the bazaar"
- Subtitle: "Where memes get traded — open to all"
- CTA: "Connect wallet" (standard)

**Empty profile state:**
- "You're a Newcomer at the bazaar."
- "Make your first trade or open a stall to start earning points."

### 6.12 Empty states & 404

- 404: "This stall doesn't exist. Maybe it never opened — or maybe it franchised away."
- Empty token list: "No stalls match. Try a different filter."
- Empty user portfolio: "You haven't bought from any stalls yet."

### 6.13 What stays standard (do NOT theme)

Reminder list:

- Connect wallet, Create token (CTAs)
- Buy, Sell (trade panel buttons + tabs)
- BUY/SELL labels in trades log
- Volume 24h, Market cap, Liquidity, Holders, Total supply, Current price, 24h Volume
- ↑ % / ↓ % change indicators
- Slippage, You pay, You receive, MAX, Balance
- Trust Score [n]/100 + Bronze/Silver/Gold tier shields
- Trust breakdown: Liquidity, Distribution, Creator
- Tabs: Trending, Trending Arena, Market Cap, New, Graduated
- Chart toolbar: 5m, 1h, 1d, MA, EMA, BOLL, RSI, SOL/USD, MarketCap/Price
- Contract, Deployer (and copy buttons)
- Status: New, Almost graduated, Live, Graduated
- All numerical data
- Time labels: 2m ago, 12 min ago, 12d ago, 3mo ago

---

## 7. Reusable code snippets

Agent có thể dùng các snippet này như building blocks cho từng mockup.

### 7.1 Header brand bar (replace Sprout header)

```html
<header class="header">
  <a class="logo">
    <div class="logo-mascot">
      <!-- Cat hawker SVG (xem section 4.2) -->
      <svg viewBox="0 0 64 64" fill="none">
        <path d="M5 22L32 12L59 22L54 24L32 16L10 24Z" fill="#3a2410" stroke="#3a2410" stroke-linejoin="round" stroke-width="0.5"/>
        <line x1="14" y1="20" x2="20" y2="17" stroke="#F5DBA8" stroke-width="1.2"/>
        <line x1="26" y1="15" x2="32" y2="13" stroke="#F5DBA8" stroke-width="1.2"/>
        <line x1="38" y1="13" x2="44" y2="15" stroke="#F5DBA8" stroke-width="1.2"/>
        <line x1="50" y1="17" x2="56" y2="20" stroke="#F5DBA8" stroke-width="1.2"/>
        <rect x="10" y="24" width="44" height="32" rx="2" fill="#3a2410"/>
        <path d="M24 30L26 25L28 30Z" fill="#EAB552" stroke="#3a2410" stroke-width="0.5"/>
        <path d="M36 30L38 25L40 30Z" fill="#EAB552" stroke="#3a2410" stroke-width="0.5"/>
        <circle cx="32" cy="40" r="9" fill="#EAB552" stroke="#3a2410" stroke-width="0.7"/>
        <ellipse cx="28.5" cy="38.5" rx="1.3" ry="1.7" fill="#3a2410"/>
        <ellipse cx="35.5" cy="38.5" rx="1.3" ry="1.7" fill="#3a2410"/>
        <path d="M30 43 Q32 44.5 34 43" stroke="#3a2410" stroke-width="1" fill="none" stroke-linecap="round"/>
        <line x1="22" y1="40" x2="27" y2="40" stroke="#3a2410" stroke-width="0.5"/>
        <line x1="37" y1="40" x2="42" y2="40" stroke="#3a2410" stroke-width="0.5"/>
      </svg>
    </div>
    <span class="logo-text">Stallspot</span>
  </a>

  <div class="header-search">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
    <input type="text" placeholder="Search the bazaar — tokens, vendors, addresses…">
  </div>

  <div class="header-actions">
    <button class="btn-ghost">Connect wallet</button>
    <button class="btn-primary">Create token</button>
  </div>
</header>
```

CSS variables already updated section 3.2. Replace `--peach-*` with `--bz-amber-*` throughout. The `.logo-text` color → `var(--bz-amber-400)`. The `.btn-primary` background gradient → amber.

### 7.2 Marquee

```html
<div class="marquee">
  <div class="marquee-track">
    <span class="amber">OPEN A STALL</span><span>·</span>
    <span>TRADE MEMES</span><span>·</span>
    <span class="amber">WATCH THE CROWD</span><span>·</span>
    <span>NO RIGGED SCALES</span><span>·</span>
    <span class="teal">BIGGEST CROWD WINS</span><span>·</span>
    <span>TIPS WHISPERED HERE</span><span>·</span>
    <!-- repeat for seamless loop -->
    <span class="amber">OPEN A STALL</span><span>·</span>
    <span>TRADE MEMES</span><span>·</span>
    <span class="amber">WATCH THE CROWD</span><span>·</span>
    <span>NO RIGGED SCALES</span><span>·</span>
    <span class="teal">BIGGEST CROWD WINS</span><span>·</span>
    <span>TIPS WHISPERED HERE</span>
  </div>
</div>
```

Class `.marquee-track .amber { color: var(--bz-amber-400); }` and `.teal { color: var(--bz-teal-400); }`.

### 7.3 User card sidebar (cat hawker mini avatar)

```html
<div class="user-card">
  <div class="user-mascot">
    <!-- Mini cat hawker (24x24) -->
    <svg viewBox="0 0 24 24" width="22" height="22" fill="none">
      <path d="M3 9L12 5L21 9" fill="#3a2410"/>
      <rect x="5" y="9" width="14" height="11" rx="1" fill="#3a2410"/>
      <circle cx="9.5" cy="14" r="1" fill="#EAB552"/>
      <circle cx="14.5" cy="14" r="1" fill="#EAB552"/>
      <path d="M9 16.5 Q12 17.5 15 16.5" stroke="#EAB552" stroke-width="0.8" fill="none" stroke-linecap="round"/>
    </svg>
  </div>
  <div class="user-info">
    <div class="user-name">NobleFlame</div>
    <div class="user-tier">Local · 642 pts</div>  <!-- tier name from new ladder -->
  </div>
</div>
```

### 7.4 Status badge

```html
<!-- New token -->
<span class="badge-new">New</span>

<!-- Almost graduated -->
<span class="badge-near-graduation">Almost graduated</span>
```

```css
.badge-new {
  position: absolute; top: -1px; left: 16px;
  background: var(--bz-teal-400);
  color: #0a3320;
  font-size: 9.5px; font-weight: 700;
  padding: 4px 10px 4px 8px;
  border-radius: 0 0 var(--r-sm) var(--r-sm);
  letter-spacing: 0.03em;
  font-family: var(--font-display);
}

/* "Almost graduated" appears as label color on graduation bar, not as separate badge */
.graduation-label.amber { color: var(--bz-amber-400); }
.graduation-fill.amber { background: linear-gradient(90deg, var(--bz-amber-400), var(--bz-amber-100)); }
```

### 7.5 Stall story callout (NEW component)

See section 6.6 above.

### 7.6 Graduation banner (signature moment)

```html
<div class="grad-banner">
  <div class="grad-mas">
    <!-- Cat hawker money-eyes state -->
    <svg viewBox="0 0 32 32" width="32" height="32" fill="none">
      <circle cx="16" cy="17" r="9" fill="#EAB552"/>
      <path d="M11 14L13 17L11 20" stroke="#3a2410" stroke-width="1.4" fill="none" stroke-linecap="round"/>
      <path d="M21 14L19 17L21 20" stroke="#3a2410" stroke-width="1.4" fill="none" stroke-linecap="round"/>
      <path d="M12 21 Q16 24 20 21" stroke="#3a2410" stroke-width="1.4" fill="none" stroke-linecap="round"/>
      <!-- Sparkles around to signify celebration -->
      <path d="M9 8L11 12M23 8L21 12" stroke="#7cc4a4" stroke-width="1.6" stroke-linecap="round"/>
      <path d="M16 5L16 9" stroke="#7cc4a4" stroke-width="1.6" stroke-linecap="round"/>
    </svg>
  </div>
  <div class="grad-content">
    <div class="grad-headline">GRADUATED · NOW ON RAYDIUM</div>
    <div class="grad-msg">[Token Name] has franchised across the bazaar. Trading on Raydium DEX.</div>
  </div>
</div>
```

```css
.grad-banner {
  background: linear-gradient(180deg, rgba(234,181,82,0.18), rgba(124,196,164,0.15));
  border: 1px solid var(--bz-amber-400);
  border-radius: 10px;
  padding: 12px 14px;
  display: flex; align-items: center; gap: 12px;
}
.grad-headline {
  font-family: var(--font-display);
  font-size: 12px; font-weight: 800;
  color: var(--bz-amber-400);
  letter-spacing: 0.04em;
}
.grad-msg { font-size: 11px; color: var(--text-1); margin-top: 3px; line-height: 1.4; }
```

### 7.7 Tier shield SVG (FR-013, UNCHANGED — for reference)

Trust Score uses the same Bronze/Silver/Gold shields as Sprout. Re-use Sprout's `.trust-shields` and `.trust-tier` classes verbatim. No changes here.

---

## 8. Mockup re-skin checklist

Agent processes 14 mockup files. For each, follow this checklist.

### 8.1 General checklist (apply per file)

**Process per file:**

1. **First, view the live MVP page tương ứng** (vd: token list page → visit `/` của MVP URL). Cross-reference với `/docs/FRD_Updated.md` cho functional spec. Nếu không thể access MVP → **STOP, request user gửi screenshot của page đó**, KHÔNG inference từ Sprout mockup.
2. **Then, look at Sprout v2 mockup** for layout/component patterns ONLY (spacing, header position, card structure, etc.). KHÔNG dùng Sprout mockup để quyết định functional behavior.
3. **CSS variable rename:** `--peach-*` → `--bz-amber-*` (keep teal, crimson, surface, text, border vars)
4. **Logo SVG replace:** Sprout sprout/leaf SVG → cat hawker SVG (section 4.2)
5. **Brand text replace:** "Sprout" → "Stallspot"
6. **Add subtitle:** Below brand name add ".bsub" subtitle "the meme bazaar" if header has space
7. **Search placeholder:** "Search the garden…" → "Search the bazaar — tokens, vendors, addresses…"
8. **Marquee text replace:** Sprout marquee → Bazaar marquee (section 6.2)
9. **CTA button:** "Plant a token" → "Create token"
10. **Tier names** (where shown): Sprout ladder → Bazaar ladder (section 6.3)
11. **Status badges** (where shown): "Just sprouted" → "New", "Almost there" → "Almost graduated"
12. **Creator info format** (where shown): "by alice" → "stall by alice · [Tier] tier · [time]"
13. **Trust Score** (where shown): UNCHANGED, do NOT modify
14. **Buy/Sell + trade UI** (where shown): UNCHANGED
15. **Data labels** (Volume, MC, Liquidity, etc.): UNCHANGED

**MVP-conflict rule:** Bazaar mockup phải match **MVP live behavior**, không phải Sprout mockup behavior. Sprout mockup có thể đã drift khỏi MVP — đó là design exploration, không phải spec. Khi nghi ngờ, ALWAYS check MVP live + FRD_Updated.md + request user screenshot. KHÔNG default to Sprout mockup as authority.

**Uncertainty rule:** Khi agent thấy có state/feature/element mà không chắc MVP có hay không → STOP và list ra. Request user gửi screenshot (hoặc confirm) trước khi continue. Tuyệt đối KHÔNG đoán.

### 8.2 Per-file checklist

**Output naming convention** (for `/mockups-bazaar/`): keep same filename as source for 1-1 traceability.

#### File 1: `home_full_layout.html`

Source: `/mockups/home_full_layout.html`
Output: `/mockups-bazaar/home_full_layout.html`

Changes:
- All general checklist items
- Header brand bar → cat hawker
- Sidebar nav items: keep names (Discover, Arena, Clubs, Events, My Profile, Leaderboard, Point System, Rewards, Referrals, Stake) — these are STANDARD per 3-layer principle. Sub-categories like "DISCOVER", "PERSONAL", "EARN" stay.
- Footer links if any: minimal change

#### File 2: `token_detail_mockup.html` (and the v2 version 05_token_detail_preview.html)

Source: `/mockups-v2/_preview/05_token_detail_preview.html` (use this as primary structural reference — it's the cleanest)
Output: `/mockups-bazaar/token_detail.html`

Changes:
- All general items
- Page header creator line: add tier "stall by alice · Local tier · 12d ago" format
- ADD new component: Stall story callout between chart card và trades table (section 6.6)
- Trust score card: UNCHANGED structure, just CSS variable swap
- Trade panel: UNCHANGED text, just CSS variable swap

#### File 3: `trading_panel_mockup.html`

Source: `/mockups/trading_panel_mockup.html`
Output: `/mockups-bazaar/trading_panel.html`

Changes:
- General items
- Buy/Sell, Slippage, You pay, You receive, MAX: ALL UNCHANGED
- Just CSS variable swap for amber theming

#### File 4: `my_profile_mockup.html`

Source: `/mockups/my_profile_mockup.html`
Output: `/mockups-bazaar/my_profile.html`

Changes:
- General items
- Tier display: use new ladder names + appropriate icon (cat hawker silhouette small, scaled by tier)
- Achievement badges if any: themed names per gamification layer
- Activity history: keep standard data labels (Volume, Trades, etc.)

#### File 5: `public_profile_mockup.html`

Source: `/mockups/public_profile_mockup.html`
Output: `/mockups-bazaar/public_profile.html`

Changes:
- General items
- Same tier display treatment as my_profile
- Public stats keep standard data labels

#### File 6: `creator_dashboard_mockup.html`

Source: `/mockups/creator_dashboard_mockup.html`
Output: `/mockups-bazaar/creator_dashboard.html`

Changes:
- General items
- Page title: "Your stalls" instead of "Your tokens" (themed framing OK here — gamification layer for creators)
- Per-token row: keep standard data, add small "stall by you" prefix if applicable
- Empty state: "Open your first stall to get started"

#### File 7: `create_token_mockup.html`

Source: `/mockups/create_token_mockup.html`
Output: `/mockups-bazaar/create_token.html`

Changes:
- General items
- Wizard headline: "Open your stall" (themed welcome — first screen has context buffer)
- Step labels: KEEP STANDARD (e.g., "Token info", "Image", "Description", "Settings", "Review")
- Field labels inside wizard: STANDARD (Token name, Symbol, Description, etc.)
- Final CTA: "Open the stall" or "Launch token" (your choice — recommend "Launch token" for consistency with crypto convention)

#### File 8: `leaderboard_mockup.html`

Source: `/mockups/leaderboard_mockup.html`
Output: `/mockups-bazaar/leaderboard.html`

Changes:
- General items
- Page title: keep "Leaderboard"
- Rank display: tier name next to user (Local, Insider, Legend etc.)
- Categories tabs: UNCHANGED (e.g., "Top traders", "Top creators", "Top referrers")

#### File 9: `points_mockup.html`

Source: `/mockups/points_mockup.html`
Output: `/mockups-bazaar/points.html`

Changes:
- General items
- Tier ladder display: 5 new Bazaar tier names (Newcomer → Legend) with descriptions:
  - Newcomer (0): "Just arrived at the bazaar."
  - Regular (500): "Coming back often."
  - Local (2K): "You belong here."
  - Insider (10K): "You know the deals."
  - Legend (50K): "Everyone knows your name."
- Earning points section: UNCHANGED data (action → points value)

#### File 10: `referrals_mockup.html`

Source: `/mockups/referrals_mockup.html`
Output: `/mockups-bazaar/referrals.html`

Changes:
- General items
- Headline: "Bring a friend to the bazaar"
- Body copy: "Earn 5% commission when they trade at your stall"
- Referral code → "Your stall card"
- Share CTA → "Hand out your stall card"
- Earnings table: UNCHANGED (Friend, Volume, Commission, Date)

#### File 11: `edit_profile_privacy_mockup.html`

Source: `/mockups/edit_profile_privacy_mockup.html`
Output: `/mockups-bazaar/edit_profile_privacy.html`

Changes:
- General items
- Section headers: standard (Privacy, Display, Notifications)
- Field labels: standard
- This is mostly utility — minimal theming

#### File 12: `sidebar_navigation.html`

Source: `/mockups/sidebar_navigation.html`
Output: `/mockups-bazaar/sidebar_navigation.html`

Changes:
- General items
- Nav item names: KEEP (Discover, Arena, Clubs, Events, My Profile, Leaderboard, Point System, Rewards, Referrals, Stake) — these are core navigation, standard
- User card at bottom: cat hawker mascot + tier display new ladder

#### File 13: `FR-012_TokenWar.html`

Source: `/mockups/FR-012_TokenWar.html`
Output: `/mockups-bazaar/FR-012_TokenWar.html`

Changes:
- General items
- Event banner / title: "Bazaar Showdown" (themed event name)
- Match-up labels: "Stall A vs Stall B" (light theming, gamification layer)
- Voting buttons: "Back A" / "Back B"
- Outcome message: "Crowd favorite: [winner]"
- Mechanics, odds display, payout: UNCHANGED

#### File 14: `FR-012b_TokenWar_PredictionMarket.html`

Source: `/mockups/FR-012b_TokenWar_PredictionMarket.html`
Output: `/mockups-bazaar/FR-012b_TokenWar_PredictionMarket.html`

Changes:
- General items
- Event title: same as FR-012
- Outcome shares display: keep standard (X shares of "A wins" at $0.42)
- Mechanics: UNCHANGED

#### Bonus: re-skin token list v4

Source: `/mockups-v2/_preview/04_token_list_preview_v4.html`
Output: `/mockups-bazaar/token_list_v4.html`

(This is the gold reference — agent should put extra care here as it's the main listing page team will scrutinize)

Changes apply general checklist plus:
- Token grid layout: UNCHANGED
- Status badge "Just sprouted" → "New"
- Graduation bar label "Almost there" → "Almost graduated"
- Token name link styling: keep but use amber color

### 8.3 Verification per mockup

After re-skinning each file, agent verifies:

- [ ] CSS variables consistent (no leftover `--peach-*` or Sprout color hex references)
- [ ] Logo SVG = cat hawker (not sprout)
- [ ] Brand text = "Stallspot"
- [ ] Marquee = Bazaar marquee
- [ ] All Buy/Sell, Volume, Market Cap, Liquidity strings unchanged
- [ ] Trust Score component unchanged structurally
- [ ] Trade panel layout/text unchanged
- [ ] Tier names (where shown) = Newcomer/Regular/Local/Insider/Legend
- [ ] Status badges = "New" / "Almost graduated"
- [ ] No leftover "Plant a token" / "garden" / "seed" / "blooming" references

---

## 9. Function Requirements - Bazaar.md

### 9.0 Source file selection — IMPORTANT

Project có **4 file FRD** với mức độ current khác nhau:

| File | Status | Use for Bazaar diff |
|---|---|---|
| `/Function Requirements.md` | Original 11 FRs, oldest, missing Arena/Clubs/Staking | ❌ KHÔNG dùng |
| `/FRD_20260418.md` | 15 FRs, dated 18/04/2026, comprehensive | ❌ KHÔNG dùng |
| **`/docs/FRD_Updated.md`** | 14 modules + MVP status indicators, dated 16/04/2026, references MVP URL | ✅ **DÙNG cái này làm source** |
| `/docs/FRD_MVP_Reality_Check.md` | Same as FRD_Updated (different title) | ❌ Duplicate, skip |

**Source for Bazaar diff:** `/docs/FRD_Updated.md` (MVP-aligned, most current of all FRDs)
**Output:** `/Function Requirements - Bazaar.md` at root level (parallel naming với existing `/Function Requirements.md`)

### 9.1 Approach

Don't rewrite from scratch. Instead:

1. **Copy `/docs/FRD_Updated.md` → `/Function Requirements - Bazaar.md`** (move from /docs/ to root level, rename)
2. Apply theme diff (search-and-replace + section-specific updates) per sections 9.2-9.4 below

### 9.0.5 Both FRDs may still drift from MVP

Even FRD_Updated.md (most MVP-aligned) is dated 16/04/2026 — MVP có thể đã drift sau ngày đó. Khi tạo Bazaar FRD:

- Apply theme strings only — KHÔNG cố reconcile FRD content với MVP behavior
- Cleanup FRD vs MVP là separate task, không scope của work này
- Bazaar FRD inherits same drift-vs-MVP risk as source FRD_Updated.md — that's OK, both apples-to-apples

### 9.2 Search-and-replace pass

Apply these replacements globally:

| Find | Replace |
|---|---|
| Sprout (when referring to brand) | Stallspot |
| sprout (when referring to brand) | stallspot |
| garden (when referring to platform) | bazaar |
| Garden | Bazaar |
| Plant a token | Create token |
| Plant your seed | Open a stall |
| 🌱 Seed | Newcomer |
| 🌿 Sprout | Regular |
| 🌳 Sapling | Local |
| 🌲 Tree | Insider |
| 🪷 Ancient Tree | Legend |
| Just sprouted | New |
| Almost there (status) | Almost graduated |
| WATCH WHAT'S BLOOMING | WATCH THE CROWD |
| NO BOT DRAMA | NO RIGGED SCALES |
| PLANT YOUR SEED | OPEN A STALL |

### 9.3 Section-specific updates

After global search-and-replace, agent reviews these sections specifically and applies extra updates:

- **FR-001 (Token List):** status badge naming, tab "Finalized" → "Graduated" (note: this is also crypto-standard improvement, not just rename)
- **FR-002 (Token Detail):** add Stall story callout component spec
- **FR-007 (Create Token):** wizard welcome screen "Open your stall" headline
- **FR-009 (Rewards):** rename "Slot Rewards" → "Lucky Vendor Draw" (mechanics unchanged)
- **FR-010 (Referrals):** copy rewrite (section 6.9 above)
- **FR-011 (Points):** full tier ladder rebrand with descriptions (section 8.2 file 9)
- **FR-012 (Token War):** event naming "Bazaar Showdown", betting CTA "Back" instead of "Bet" (mechanics unchanged)
- **FR-013 (Trust Score):** ZERO changes — explicit note in section
- **FR-014 (Club):** light naming review — keep "Club" or rename to "Guild" (recommend keeping "Club")
- **FR-015 (Event):** consider "Bazaar days" framing for events
- **FR-016 (ClubWar):** "Guild showdown" or keep "Club War"

### 9.4 Top section header

At top of `Function Requirements - Bazaar.md`, add this header block:

```markdown
# Function Requirements — Bazaar Theme Variant

> **This is the Bazaar theme variant** of the FRD. The Sprout theme variant lives in `/Function Requirements.md`.
> Both variants share identical functional requirements, BE/FE behavior, and architecture. They differ only in:
> - Brand identity (logo, name, tagline, color palette)
> - Microcopy at brand and gamification layers
> - Tier ladder names (FR-011)
>
> Core trading UI (Buy/Sell, Volume, Market Cap, Trust Score, Chart) is identical between variants.
>
> ⚠️ **Both FRDs (Sprout and Bazaar) may be out of sync with the live MVP behavior.** When functional behavior matters,
> reference the live MVP, not these documents. This applies to both theme variants equally.
>
> **Source provenance:** This Bazaar FRD was diffed from `/docs/FRD_Updated.md` (dated 16/04/2026, the most MVP-aligned of project's 4 FRD files). Sprout's master FRD is `/Function Requirements.md` at root.
>
> See `/BAZAAR_IMPLEMENTATION_PLAN.md` for the rationale and detailed migration scope.
```

---

## 10. CLAUDE.md updates

Update existing `/CLAUDE.md` to be aware of multi-theme. Apply these changes:

### 10.1 Replace project structure section

Find the existing "## Project Structure" section. Replace with:

```markdown
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

### 10.2 Add new section: Theme variants

Add this section after "## Overview" and before "## Project Structure":

```markdown
## Theme Variants

Project hiện có 2 theme variant đang được team đánh giá:

**Sprout (default, currently in use):**
- Mascot: cây con với 2 lá
- Tagline: "Plant your seed in the memeconomy."
- Palette: peach + teal
- Tier ladder (FR-011): Seed → Sprout → Sapling → Tree → Ancient Tree
- Files: `/Function Requirements.md`, `/docs/FRD_Updated.md`, `/mockups/`, `/mockups-v2/`

**Bazaar (variant for evaluation):**
- Mascot: cat hawker behind quầy hàng
- Brand: "Stallspot · the meme bazaar"
- Tagline: "Open a stall. Trade memes."
- Palette: amber + brown (teal kept as success accent)
- Tier ladder (FR-011): Newcomer → Regular → Local → Insider → Legend
- Files: `/Function Requirements - Bazaar.md`, `/mockups-bazaar/`
- Plan: `/BAZAAR_IMPLEMENTATION_PLAN.md`

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
```

### 10.3 Update Discover Tab section

The existing "## Discover Tab — Scoring System" section is theme-agnostic. KHÔNG đổi.

### 10.4 Update Key Business Rules

Existing section is functional. KHÔNG đổi major content. Add at the top:

```markdown
> Theme-specific naming variants noted in `Function Requirements.md` (Sprout) and `Function Requirements - Bazaar.md` (Bazaar). Mechanics and values below apply to both.
```

### 10.5 Update Design System section

Replace the existing "## Design System (Quick Reference)" section with:

```markdown
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
```

### 10.6 Add Conventions clarification

In existing "## Conventions" section, add:

```markdown
- **Theme variants:** Brand-layer microcopy varies between Sprout and Bazaar. Core trading UI (Buy/Sell, Volume, Market Cap, Trust Score, Chart) is identical across themes. See `BAZAAR_IMPLEMENTATION_PLAN.md` section 5 for the three-layer principle.
```

---

## 11. Acceptance criteria

Implementation is done when ALL of these pass:

### 11.1 File deliverables present

- [ ] `/mockups-bazaar/` folder exists
- [ ] `/mockups-bazaar/` contains 14+ HTML files (one per existing Sprout mockup, plus token_list_v4 from /mockups-v2/)
- [ ] `/Function Requirements - Bazaar.md` exists at root
- [ ] `/CLAUDE.md` updated with theme variants section, structure section, design system section

### 11.2 Visual consistency check

For 3 randomly chosen files from `/mockups-bazaar/`, open in browser and verify:

- [ ] Header shows "Stallspot · the meme bazaar" (or just "Stallspot" if subtitle doesn't fit)
- [ ] Header logo is cat hawker SVG (not sprout)
- [ ] CTA button reads "Create token" (not "Plant a token")
- [ ] Marquee text contains "OPEN A STALL" / "TRADE MEMES" / "WATCH THE CROWD" / "NO RIGGED SCALES"
- [ ] No leftover "Plant", "seed", "garden", "blooming", "sprout" references
- [ ] Color accents are amber/gold (not peach)

### 11.3 Three-layer principle compliance

For token list and token detail mockup, verify:

- [ ] Buy / Sell button text unchanged
- [ ] Volume 24h, Market cap, Liquidity, Holders, Total supply labels unchanged
- [ ] Trust Score 64/100 + Bronze/Silver/Gold + Liquidity/Distribution/Creator structure unchanged
- [ ] BUY / SELL labels in trades log unchanged
- [ ] Chart timeframe pills (1m/5m/15m/1h/4h/1d) unchanged
- [ ] Slippage, You pay, You receive, MAX, Balance text unchanged
- [ ] Tier name in user card uses new ladder (Newcomer/Regular/Local/Insider/Legend)
- [ ] Status badges read "New" or "Almost graduated" (not "Just sprouted" / "Almost there")

### 11.4 FRD compliance

Open `/Function Requirements - Bazaar.md`:

- [ ] Header block notes this is Bazaar variant
- [ ] All Sprout brand references replaced (search the file for "Sprout", "garden", "seed", "🌱" — should find ~0 results outside historical/explanatory mentions)
- [ ] FR-011 tier ladder shows new names with same point thresholds
- [ ] FR-013 Trust Score section unchanged
- [ ] FR-003 Buy/Sell section unchanged
- [ ] Functional requirements (mechanics, formulas, values) unchanged from Sprout FRD

### 11.5 CLAUDE.md compliance

Open `/CLAUDE.md`:

- [ ] "Theme Variants" section exists describing both Sprout and Bazaar
- [ ] Project structure tree shows `/mockups-bazaar/` and `Function Requirements - Bazaar.md`
- [ ] Design System section shows both palettes side-by-side
- [ ] Reference to `/BAZAAR_IMPLEMENTATION_PLAN.md` exists

---

## 12. Anti-patterns to avoid

### 12.1 Over-theming (DO NOT)

- ❌ "Stop by" instead of "Buy" — buy/sell verbs are core trading UI, never theme
- ❌ "Footfall" instead of "Volume" — data labels are standard
- ❌ "Vendor reputation" / "Stock quality" / "Fair pricing" instead of Liquidity/Distribution/Creator — Trust Score breakdown is per FR-013, never theme
- ❌ "Wood / Brass / Gold seal" instead of Bronze/Silver/Gold — Trust Score tier names are per FR-013, never theme
- ❌ "Almost franchised" instead of "Almost graduated" — status badge affecting trading decision, must be standard

### 12.2 Anglo-American slang (DO NOT)

Target market includes Turkey, Nigeria, Indonesia, Philippines, Thailand. Use B1 ESL-friendly English everywhere user-facing.

- ❌ "Catch the buzz" — US slang
- ❌ "Hawk your meme" — niche verb
- ❌ "Hook the crowd" — idiom
- ❌ "Pitch a meme" — sales jargon
- ❌ "Alpha whispered" — crypto jargon at brand layer

Use universal verbs: open, trade, watch, see, win, find.

### 12.3 Religious / cultural insensitivity (DO NOT)

- ❌ Pig imagery (Indonesia majority Muslim)
- ❌ Alcohol references (Muslim concern)
- ❌ Gambling imagery / slot machine visuals overdone (saloon aesthetic conflicts with Islamic markets)
- ❌ Cowboys / Wild West imagery (American-coded, not local for SEA/Africa)
- ❌ Religious symbols in mascot or art

### 12.4 Mascot inconsistency (DO NOT)

- ❌ Cat in different art styles across mockups — keep one consistent illustration approach
- ❌ Cat without counter (loses bazaar context)
- ❌ Adding hat / clothing variations beyond the 8 expression states
- ❌ Other animals appearing without prior approval (no dog mascot, no raccoon mascot)

### 12.5 Layout / structural changes (DO NOT)

- ❌ Changing header height from 60px
- ❌ Changing sidebar width from 240px
- ❌ Changing token grid `repeat(auto-fill, minmax(320px, 1fr))`
- ❌ Adding new components beyond what's specified (Stall story is the ONLY new component)
- ❌ Reordering sections in token detail layout

### 12.6 Functional changes (DO NOT)

- ❌ Modifying any logic, formula, threshold, or mechanic from FRD
- ❌ Changing graduation threshold ($69K MC stays)
- ❌ Changing fee structure (1% creator fee, 5% referral commission)
- ❌ Changing point earning rules
- ❌ Changing Trust Score scoring (FR-013 untouched)

---

## 13. Recommended execution order

Suggested sequence for implementation agent:

**Phase 1 — Foundation (MVP first, mockups là reference only):**
1. **Visit MVP live**: `https://fe-dev.pumpfunclone2025.win/`. Try WebFetch or browser tool. Walk through every page (home/token list, token detail, profile, leaderboard, create token, points, referrals, arena, events, clubs, stake). Take screenshots if tool supports. **This is functional ground truth.**
2. **Read `/docs/FRD_Updated.md`** thoroughly — functional spec aligned to MVP, source for Bazaar FRD diff.
3. **List your uncertainties.** Agent compile list of MVP states/screens không thể access (vd: locked behind wallet connection, dynamic states, error pages, etc.). **Request user gửi screenshots** cho từng item trong list TRƯỚC KHI bắt tay re-skin.
4. **Browse `/images/image-*.png`** — existing screenshots if available, supplementary reference.
5. **Open Sprout v2 mockups** as REFERENCE for layout/component patterns ONLY: `/mockups-v2/_preview/04_token_list_preview_v4.html`, `/mockups-v2/_preview/05_token_detail_preview.html`. **KHÔNG** treat these as functional spec — they may have drifted from MVP. Use for: spacing, header structure, card layout, color system reference.
6. Browse `/mockups/` for additional layout patterns.
7. Read `/CLAUDE.md` for project context.
8. Re-read this plan section 4 (mascot) and section 7 (code snippets).

**Phase 2 — FRD & docs first (text easier than HTML):**
5. Copy `/docs/FRD_Updated.md` → `/Function Requirements - Bazaar.md` (move to root level + rename)
6. Apply global search-and-replace per section 9.2
7. Apply section-specific updates per section 9.3
8. Add header block per section 9.4
9. Update `/CLAUDE.md` per section 10

**Phase 3 — Gold reference mockups (high care):**
10. Re-skin `/mockups-v2/_preview/04_token_list_preview_v4.html` → `/mockups-bazaar/token_list_v4.html`
    - This is the most-scrutinized file. Apply section 7 code snippets carefully.
11. Re-skin `/mockups-v2/_preview/05_token_detail_preview.html` → `/mockups-bazaar/token_detail.html`
    - Add the new Stall story callout component.
12. **Self-check:** open both files, run section 11.2 + 11.3 verification checks. Iterate if issues found.

**Phase 4 — Remaining mockups (mechanical):**
13. Re-skin remaining 12 files from `/mockups/` per section 8.2 checklist
14. Each file: apply general checklist (section 8.1) + per-file specifics (section 8.2)

**Phase 5 — Verification:**
15. Run full acceptance criteria checklist (section 11)
16. Open `/mockups-bazaar/token_list_v4.html` and `/mockups-bazaar/token_detail.html` side-by-side with Sprout originals — visual diff sanity check
17. Search the entire `/mockups-bazaar/` folder for leftover Sprout strings:
    - `grep -r "Sprout" mockups-bazaar/` — should find 0
    - `grep -ri "garden" mockups-bazaar/` — should find 0
    - `grep -ri "plant" mockups-bazaar/` — should find 0 (except "plantar" or unrelated words if any)
    - `grep -ri "seed" mockups-bazaar/` — should find 0
    - `grep -ri "blooming" mockups-bazaar/` — should find 0

**Phase 6 — Wrap-up:**
18. Create a brief CHANGELOG entry at the bottom of `/BAZAAR_IMPLEMENTATION_PLAN.md` noting completion date and any deviations from this plan
19. Verify `/CLAUDE.md` references all new files correctly

---

## 13.5 Asking user for help — protocol

Khi nào agent SHOULD/MUST ask user:

**MUST ask (block work until answered):**
- Cannot access MVP URL via any tool → request screenshots cho specific pages
- See feature in Sprout mockup but cannot verify against MVP → request screenshot
- FRD_Updated says one thing, MVP shows another, agent unsure which is current → ask user
- Encounter ambiguity về mascot expression cho specific signature moment

**SHOULD ask (work can continue with default if no answer in reasonable time):**
- Wizard "Open your stall" headline OK to use cho Create Token? (default: yes)
- Optional: include `/themes-bazaar/BRAND_GUIDELINES.md` separate file? (default: no, keep in plan)

**NO need to ask (use plan default):**
- Microcopy strings already specified in section 6
- Color palette hex values
- Mascot SVG details
- File naming conventions

**Format khi request user help:**

```markdown
🛑 PAUSED — need user input

**Blocking:** I'm re-skinning [file_name.html] for Bazaar theme but cannot verify [specific_thing] against MVP.

**What I tried:**
- [tool/method 1] → [result]
- [tool/method 2] → [result]

**What I need:**
[Specific question — 1 sentence] OR
[Screenshot of: which MVP page, what state]

**Will resume after user reply.**
```

Agent nên batch multiple questions vào 1 ask khi possible (vd: list 5 uncertainties cùng lúc) thay vì hỏi rời rạc nhiều lần.

---

## 14. Out of scope (DO NOT do)

- ❌ Build any frontend code (React, Vue, etc.) — this is mockups + docs only
- ❌ Modify `/testing/` folder
- ❌ Modify `/docs/` individual FR files (they're theme-agnostic)
- ❌ Modify `/design/UI_UX_DESIGN_SYSTEM.md` (it's the Sprout-default design system; create a separate design doc only if needed)
- ❌ Delete or modify Sprout files in `/mockups/` and `/mockups-v2/`
- ❌ Modify `/Function Requirements.md` (Sprout FRD stays as-is)
- ❌ Generate marketing assets (sticker pack PNGs, Telegram banners, etc.) — that's a future implementation phase
- ❌ Modify backend specs, smart contract docs, or Solana integration files

---

## Appendix A — Quick reference: 4 questions agent must always ask

When in doubt about whether to theme a string or keep standard, ask:

1. **Will user need to parse this in <2 seconds to make a trading decision?**
   - YES → STANDARD (keep Sprout's standard string or use crypto convention)
   - NO → can theme

2. **Is this string in the chart/trade panel/trust score module?**
   - YES → STANDARD always
   - NO → check next question

3. **Is this a tier name, achievement, signature event, or ambient brand voice?**
   - YES → can theme (gamification + brand layer)
   - NO → likely standard

4. **Will an ESL B1 reader from Turkey/Nigeria/Indonesia parse this in 2 seconds?**
   - YES → OK to use
   - NO → simplify or revert to standard

**Plus 2 questions for FUNCTIONAL/UI scope (not microcopy):**

5. **Does Sprout mockup show feature X but I haven't verified MVP has it?**
   - YES → STOP. Sprout mockup là reference only, không phải spec. Verify against MVP live + FRD_Updated.md trước. Nếu vẫn không sure → ASK user gửi screenshot.
   - NO → proceed.

6. **Does FRD_Updated.md say one thing and MVP show another?**
   - YES → follow MVP. FRD lags reality. Bazaar mockup must match MVP.
   - Same applies if Sprout mockup conflicts with MVP — follow MVP.

**Default behavior under uncertainty: ASK USER, do NOT guess.** Cost của 1 question là 5 phút. Cost của guessing wrong = re-do toàn bộ mockup file. Always ask.

---

## Appendix B — Sprout → Bazaar quick replacement table

| Concept | Sprout | Bazaar |
|---|---|---|
| Brand name | Sprout | Stallspot |
| Subtitle | (none) | the meme bazaar |
| Mascot | Cây con + 2 lá | Cat hawker + quầy hàng |
| Tagline | Plant your seed in the memeconomy | Open a stall. Trade memes. |
| Marquee phrase 1 | PLANT YOUR SEED | OPEN A STALL |
| Marquee phrase 2 | WATCH WHAT'S BLOOMING | WATCH THE CROWD |
| Marquee phrase 3 | NO BOT DRAMA | NO RIGGED SCALES |
| Marquee phrase 4 | MAKE MONEY ON THE MEMECONOMY | TRADE MEMES |
| Search placeholder | Search the garden | Search the bazaar |
| CTA primary | Plant a token | Create token |
| Tier 1 (0 pts) | 🌱 Seed | Newcomer |
| Tier 2 (500) | 🌿 Sprout | Regular |
| Tier 3 (2K) | 🌳 Sapling | Local |
| Tier 4 (10K) | 🌲 Tree | Insider |
| Tier 5 (50K) | 🪷 Ancient Tree | Legend |
| Status: just launched | Just sprouted | New |
| Status: graduating soon | Almost there | Almost graduated |
| Token desc framing | (plain) | Stall story (italic callout) |
| Creator label | by [name] | stall by [name] · [tier] tier · [time] |
| Slot rewards | Slot Rewards | Lucky Vendor Draw |
| Token War event | Token War / Arena | Bazaar Showdown (or keep Arena) |
| War CTA | Bet on A | Back A |
| Referral copy | Refer friends, earn rewards | Bring a friend to the bazaar |
| Referral 5% framing | 5% of trading fees | 5% commission when they trade at your stall |
| Graduation message | Graduated to DEX | GRADUATED · NOW ON RAYDIUM (+ themed flavor line) |
| Empty state generic | (varies) | "No stalls match. Try a different filter." |
| 404 page | (default) | "This stall doesn't exist. Maybe it never opened — or maybe it franchised away." |
| Welcome onboarding | (varies) | "Welcome to the bazaar — where memes get traded." |

---

## Appendix C — Decision rationale (short version)

For team review reference. Why Bazaar was chosen as the variant to evaluate:

1. **Tagline alignment.** Existing platform tagline already says "MAKE MONEY ON THE MEMECONOMY". Bazaar literally is a memeconomy → 1-1 metaphor mapping. Sprout's plant metaphor is one step removed.

2. **Target market resonance.** Nigeria/Indonesia/Philippines/Thailand all have rich bazaar/market cultures (warung, sari-sari, talad, naija market) that are central to daily life. Bazaar mental model is hyper-local; plant metaphor is more generic.

3. **Energy match.** Meme tokens pump in hours. Bazaar has matching fast cadence (crowded vs empty stalls). Plants grow over weeks — wrong rhythm for memecoin pump cycle.

4. **Creator-first framing.** "Stall by alice" elevates the creator's voice (KOL-driven culture in SEA), differentiating from PumpFun's faceless spam vibe.

5. **Religious safety.** Bazaar imagery is religion-neutral. Pure Garden/Sprout also is, but Bazaar adds commercial energy without conflict.

6. **Sticker pack viability.** Cat hawker has clear emotion states (8 variations easy to AI-gen). Sprout has fewer expression states — leaf doesn't emote.

For team comparison: open `/mockups-v2/_preview/04_token_list_preview_v4.html` (Sprout) side-by-side with `/mockups-bazaar/token_list_v4.html` (Bazaar) to feel the difference.

---

**End of plan.**

> Plan version 1.0 · Created from chat session with theme decision-maker
> Read this entire document before starting any work.
> When in doubt, refer to section 5 (three-layer principle) and Appendix A (4 questions agent must always ask).

---

## CHANGELOG

### v1.0 — Completed 2026-05-03

**Executed by:** Antigravity AI agent

**Deliverables:**
1. `/mockups-bazaar/` — 15 HTML mockup files re-skinned from Sprout source:
   - From `/mockups/` (14 files): home_full_layout, token_detail, trading_panel, my_profile, public_profile, creator_dashboard, create_token, leaderboard, points, referrals, edit_profile_privacy, sidebar_navigation, FR-012_TokenWar, FR-012b_TokenWar_PredictionMarket
   - From `/mockups-v2/_preview/` (2 files, override token_detail): token_list_v4 (gold reference), token_detail (primary from v2)
2. `/Function Requirements - Bazaar.md` — Bazaar FRD diffed from `/docs/FRD_Updated.md`
3. `/CLAUDE.md` — Updated with Theme Variants section, updated Project Structure, dual-palette Design System

**MVP verification:** Live MVP visited at `https://fe-dev.pumpfunclone2025.win/`. Confirmed:
- Tab names: Trending, Trending Arena, Market Cap, New, Finalized (mockups match)
- CTAs: "Create Token" + "Connect Wallet" (standard, unchanged)
- Sidebar: My Profile, Arena, Events, Clubs, Leader Board, Point System, Rewards, Referrals, Stake

**Deviations from plan:**
- `home_full_layout.html` source uses different logo structure (`.logo-icon` emoji, no `.logo-mascot`) — fixed with full logo block replacement
- FR-012 source uses `sidebar-logo` class with `🌱 PumpFun` — replaced with `🐱 Stallspot`
- `trading_panel.html`, `leaderboard.html`, and other isolated component mockups don't have top-level header — no brand text needed, consistent with source design
- "Finalized" tab kept as-is (matches MVP live), per three-layer principle (standard tab nav)
