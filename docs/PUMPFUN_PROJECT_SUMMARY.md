# PUMPFUN PROJECT - COMPLETE CONTEXT & ARTIFACTS

**Last Updated:** February 3, 2026  
**Status:** Active Development - FRs Phase Complete

---

## 🎯 PROJECT OVERVIEW

**Platform:** Solana-based meme token launchpad  
**Model:** Fair launch with bonding curve  
**Core Value:** Easy token creation + Community-driven trading

**Key Features:**
- 5-step token creation wizard (no coding)
- Bonding curve trading mechanism
- Graduation system ($69K MC → Raydium)
- Gamification (Points, Ranks, Slot Machine)
- Revenue sharing (1% creator + 5% referral)
- Anti-MEV protection

**Geographic Restriction:**
- ❌ Vietnam users BLOCKED (geolocation check)
- ✅ All other regions allowed

---

## 📋 MASTER FUNCTIONAL REQUIREMENTS DOCUMENT

**Document:** `Function Requirements.md`

This is the comprehensive master document containing all functional requirements for the PumpFun platform. It includes:

- **FR-001:** Token List - Discovery, filtering, search, and tabs
- **FR-002:** Token Detail - Complete token information page
- **FR-003:** Buy/Sell - Trading panel with basic and advanced modes
- **FR-004:** My Profile - Personal dashboard with 5 tabs
- **FR-005:** Public Profile - Read-only user profiles
- **FR-006:** Creator Dashboard - Token management for creators
- **FR-007:** Create Token - 5-step wizard
- **FR-008:** Leaderboard - Top tokens ranking
- **FR-009:** Rewards - Slot machine game
- **FR-010:** Referrals - Referral system and earnings
- **FR-011:** Points - Ranking and points system

All images are located in the `images/` folder with references updated.

---

## 📚 COMPLETED FUNCTIONAL REQUIREMENTS

### FR-002: Token Detail Page
**Documents:** `FR-002_TokenDetail.md` + `token_detail_mockup.html`

**Key Sections:**
- Header: Avatar, Name, Symbol, Statement, Description
- Stats: MC, Price, Volume, Holders, Liquidity, Trust Score
- Chart: TradingView integration placeholder
- Community: Posts (like, reply), Chat room
- Holders List → Click → Public Profile
- Transaction History
- Actions: Buy, Sell, Add to Favorite

**Entry Points:** Token List, Leaderboard, Search, My Profile, Public Profile

---

### FR-003: Buy/Sell (Trading Panel)
**Documents:** `FR-003_BuySell.md` + `trading_panel_mockup.html`

**Two Modes:**

**Basic Mode:**
- Quick trade interface
- Amount input (SOL or Token)
- Slippage: 0.5% / 1% / 3% / Custom
- Priority: Normal / Fast / Turbo
- Risk Check: Red (block) / Yellow (warning) / Green (ok)
- Settings: Anti-MEV, Auto-retry
- Success → +1 reward ticket

**Advanced Mode:**
- Limit orders
- Target price setting
- Active orders list
- Cancel functionality

**Entry Point:** Token Detail page

---

### FR-004: My Profile (Personal Dashboard)
**Documents:** `FR-004_MyProfile.md` + `my_profile_mockup.html`

**5 Tabs:**
1. **Holding Tokens** - Owned tokens list
2. **Created Tokens** - Created by user (read-only)
3. **Staking** - Staked tokens
4. **Edit Profile:**
   - Username (one-time, cannot change)
   - Display Name (one-time, cannot change)
   - Avatar, Bio (editable anytime)
   - Social: Twitter, Telegram, Email
   - Wallet: Read-only
5. **Limit Orders** - Active advanced orders only

**Entry Points:** Sidebar menu, Header dropdown

---

### FR-005: Public Profile
**Documents:** `FR-005_PublicProfile.md` + `public_profile_mockup.html`

**Entirely Read-Only**

**4 Tabs:**
1. **Profile Info** - Basic info, social, activity stats
2. **Holding Tokens** - Can be hidden (privacy)
3. **Created Tokens** - Always public
4. **Transaction History** - Can be hidden (privacy)

**Badges:**
- Creator Badge (has created tokens)
- Whale Badge (high holdings value)

**Entry Points:** Token Detail (creator), Community Chat, Holders List, Transaction History, Referrals List

---

### FR-006: Creator Dashboard
**Documents:** `FR-006_CreatorDashboard.md` + `creator_dashboard_mockup.html`

**2-Level Navigation:**

**Level 1 - Dashboard (2 tabs):**
1. **Created Tokens:**
   - List with "Manage Token" button
   - Click → Token Management (Level 2)

2. **Creator Revenue:**
   - Stats: Total Revenue, Unclaimed, Total Claimed
   - Claim section (requires wallet)
   - Revenue breakdown by token

**Level 2 - Token Management (3 tabs):**
1. **Overview** - Metrics, chart, token info
2. **Trusted Level** - LP Lock, Audit, Freeze Authority
3. **Community Management** - Create/edit/delete/pin posts

**Entry Point:** Sidebar menu (Personal section)

---

### FR-007: Create Token (5-Step Wizard)
**Documents:** `FR-007_CreateToken.md` + `create_token_mockup.html`

**Wizard Steps:**

**Step 1: Basic Info**
- Name (required, max 32 chars)
- Symbol (required, max 10 chars, uppercase)
- Statement (required, max 60 chars) + AI Assist
- Description (required, max 500 chars) + AI Assist

**Step 2: Avatar**
- Upload image (PNG/JPG, max 5MB, square)
- AI Generate (describe → generate)

**Step 3: Security Settings**
- LP Lock (ON default) → +20 trust score
- Audit Token (OFF default) → +30 trust score
- Freeze Authority (OFF default) → +25 trust score

**Step 4: Initial Buy (Optional)**
- Quick buttons: 0.1 / 0.5 / 1 SOL or Skip
- Custom amount input
- Calculates tokens received

**Step 5: Review & Create**
- Summary card
- Create button → Deploy → Success screen
- Success: View Token Detail or Share on Twitter

**Entry Points:** Sidebar menu, Header button, Home CTA

---

### FR-008: Leaderboard
**Documents:** `FR-008_Leaderboard.md` + `leaderboard_mockup.html`

**Layout:**

**Top 3 Featured Cards:**
- Rank badge (#001, #002, #003)
- Gradient warm background
- Token avatar (80x80px)
- Name + Statement
- MC change % + value
- 24h Volume change % + value
- Buy button
- Creator info + time ago
- Hover: Lift + border highlight

**Table List (Rank #4+):**
- Columns: Token (40%), Creator (30%), Holders (15%), Market Cap (20%), Buy (15%)
- Color coding: Green (+%), Red (-%), Gray (0%)
- Click row → Token Detail
- Buy button → Trading Panel

**Ranking:** By Market Cap (highest first)

**Entry Point:** Sidebar menu

---

### FR-009: Rewards & Games (Slot Machine)
**Documents:** `FR-009_Rewards.md` + `points_mockup.html` (needs slot machine update)

**Page Sections:**

**1. Broadcast Banner (Marquee)**
- Live winners feed
- Format: "⚪ Guest #XXXXXXX bet X tickets won X.XXXXXX SOL Xd ago"
- Auto-scroll, pause on hover
- Gradient fade edges

**2. Stats Cards (2 columns)**

**Card 1: Reward Balance**
- Value: X.XXX SOL
- CLAIM button (disabled when 0)

**Card 2: Your Tickets**
- Value: X tickets
- Controls: [-] [amount] [+]
- BET button (bet 1-5 tickets)

**3. Slot Machine (5 reels)**
- Symbols: 🌱(x1) 🌿(x2) 🌳(x3) 🍀(x4) 🌼(x5)
- Each reel: 84x84px
- Spin animation: Vertical scroll
- Win: 3+ matching symbols (not adjacent required)

**4. Game Info (2 columns)**
- Multipliers table
- Rules

**5. History Table**
- Columns: Time, Bet, Result, Payout
- Shows only winning spins
- Last 20 wins

**Payout Formula:**
- 3-4 of a kind: `0.001 SOL × multiplier`
- 5 of a kind: `0.01 SOL` (jackpot, ignores multiplier)

**Entry Point:** Sidebar menu (Earn section)

---

### FR-010: Referrals
**Documents:** `FR-010_Referrals.md` + `referrals_mockup.html`

**Page Sections:**

**1. Stats Overview (3 cards)**
- Total Referrals: X Active users
- Total Earnings: X.X SOL (≈ $XXX)
- This Month: X.X SOL (≈ $XXX)

**2. Your Referral Link**
- Link: `https://pumpfun.io/ref/[username]`
- Copy button: "📋 Copy Link" → "✓ Copied!" (2s)
- Share: Twitter, Telegram (pre-filled text)

**3. Claimable Rewards**
- Amount: X.X SOL (large, green)
- USD equivalent: ≈ $XXX
- CLAIM button (requires wallet)

**4. Referred Users Table**
- Columns: User (avatar + name + wallet), Joined, Trade Volume, Your Earnings
- Click row → Public Profile
- Sort: Joined date (newest first)

**Commission:** 5% of referred user's trading fees
**Calculation:** `User Earnings = User's Trade Volume × 5%`

**Entry Point:** Sidebar menu (Earn section)

---

### FR-011: Points & Ranking System
**Documents:** `points_mockup.html` exists, MD needs creation

**Page Sections:**

**1. Header**
- Title: "Points"
- Subtitle: "Get points for doing stuff : trade, create, stake have fun!"
- Points display: XXX / XXX (current / next level)

**2. Rank Card**
- Current rank: Emoji + Name
- Progress bar (percentage)
- Text: "X.XX SOL away from [Next Rank]"

**3. History Table**
- Columns: Date, Trading Volume, Points Earned
- Shows all point-earning activities
- Sorted: Newest first
- Empty state: "Nothing yet? Switch wallets or trade to earn points."

**5 Rank Tiers:**

| Tier | Name | Points Required | Rewards |
|------|------|-----------------|---------|
| 1 | 🌱 Seed | 0 | – |
| 2 | 🌿 Sprout | 500 | 🎁 1 Ticket + 0.005 SOL |
| 3 | 🌳 Sapling | 2,000 | 🎁 3 Tickets + 0.02 SOL |
| 4 | 🌲 Tree | 10,000 | 🎁 5 Tickets + 0.05 SOL |
| 5 | 🪷 Ancient Tree | 50,000 | 🎁 10 Tickets + 0.2 SOL |

**Points Calculation:**

**(A) Referral Points (strongest):**
- Formula: `NetVolume × 10`
- NetVolume = Total BUY - Total SELL
- Examples: 0.1 SOL → 1 pt, 1 SOL → 10 pts, 10 SOL → 100 pts

**(B) Trade Points:**
- Formula: `Volume × 5`
- Example: 1 SOL trade → 5 pts

**(C) Token Creation Points:**
- Create token: 20 pts
- Upload image + description: 10 pts
- Token Trust Score: 20 pts
- Token reaches 10 buys: 30 pts
- **Total possible:** 80 pts per token

**Anti-Farm Rules:**
- Only BUY ≥ 0.01 SOL counts
- SELL does not earn points
- NetVolume (Buy - Sell) blocks wash trading
- Token must be ACTIVE (2nd buyer ≠ creator, BUY ≥ 0.05 SOL)

**Season System:**
- Duration: 3 weeks
- After season: Reset accounts without enough points
- Points accumulate to next season
- SOL rewards: From Marketing Pool

**Entry Point:** Sidebar menu (could be under Earn or separate)

---

## 🎨 HTML MOCKUPS CREATED

### Core Layout:
1. **home_full_layout.html** - Complete layout (Header + Sidebar + Token List)
   - Fixed header: Logo, Search, [Login] [Create Token]
   - Fixed sidebar: Navigation + User profile
   - Main content: Token list with tabs, Sort/Filter buttons
   - Token grid: Cards with Buy buttons

2. **landing_page_mockup.html** - Marketing landing page
3. **sidebar_navigation.html** - Sidebar component standalone

### Feature Pages (11 mockups):
1. **token_detail_mockup.html** - FR-002
2. **trading_panel_mockup.html** - FR-003
3. **my_profile_mockup.html** - FR-004
4. **public_profile_mockup.html** - FR-005
5. **creator_dashboard_mockup.html** - FR-006
6. **create_token_mockup.html** - FR-007
7. **leaderboard_mockup.html** - FR-008
8. **points_mockup.html** - FR-009/011 (Points system)
9. **referrals_mockup.html** - FR-010

**Note:** Slot machine mockup needs to be created to match FR-009 spec.

---

## 📐 DESIGN SYSTEM

### Colors:
```css
--primary: #10b981        /* Green - Primary actions, highlights */
--accent: #ffffff         /* White - Text on dark */
--card: #1a1a2e          /* Dark blue - Cards, panels */
--card2: #16213e         /* Darker blue - Nested cards */
--card-hover: #0f1729    /* Hover state */
--card-border: #2d3748   /* Border gray */
--bg: #0a0e1a            /* Background */
--text-primary: #ffffff   /* Primary text */
--text-secondary: #9ca3af /* Secondary text */
--text-tertiary: #6b7280  /* Tertiary text */
```

### Layout Constants:
```css
--sidebar-width: 260px
--header-height: 70px
```

### Typography:
- **Font Family:** -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto
- **Page Title:** 28-32px, font-weight: 800
- **Section Title:** 20-24px, font-weight: 700
- **Body:** 14px, font-weight: 400-600
- **Small:** 12px

### Component Styles:
- **Border Radius:** 8-16px (buttons 8px, cards 12-16px)
- **Buttons:** padding: 10-16px, font-weight: 600
- **Cards:** padding: 20-24px, border: 1px solid
- **Inputs:** padding: 12px, border-radius: 8px
- **Gaps:** 12px (small), 24px (medium), 32px (large)

### Responsive Breakpoints:
```
Mobile: < 768px
Tablet: 768px - 1024px
Desktop: > 1024px
```

---

## 🔑 KEY BUSINESS RULES

### Token Economics:
- **Creator Fee:** 1% on all trades
- **Referral Commission:** 5% of trading fees (not 5% of trade volume)
- **Bonding Curve:** Fair launch pricing mechanism
- **Graduation:** $69K Market Cap → Migrate to Raydium DEX with liquidity

### Trust Score System:
- LP Lock: +20 points
- Audit: +30 points
- Freeze Authority Disabled: +25 points
- **Max Score:** 75 points

### Trading Rules:
- **Risk Check:**
  - Red: Block BUY, allow SELL only
  - Yellow: Warning, requires confirmation
  - Green: Proceed normally
- **Min Trade:** 0.01 SOL (for points)
- **Slippage Options:** 0.5% / 1% / 3% / Custom
- **Priority Fee:** Normal / Fast / Turbo

### Profile Rules:
- **One-time Fields:** Username, Display Name (cannot change after first save)
- **Editable Anytime:** Avatar, Bio, Social links
- **Privacy Controls:** Can hide Holdings and Transaction History
- **Always Public:** Created Tokens, Username, Wallet address

### Points Anti-Farm:
1. Only BUY ≥ 0.01 SOL counts
2. SELL does not earn points
3. NetVolume (Buy - Sell) prevents wash trading
4. Token must be ACTIVE:
   - Has 2nd buyer ≠ creator
   - 2nd buyer must BUY ≥ 0.05 SOL

---

## 🗺️ NAVIGATION STRUCTURE

### Header (Fixed Top):
- **Left:** Logo 🚀 PumpFun + Search bar
- **Right:** [Login] [Create Token] buttons

### Sidebar (Fixed Left):

**Main Section:**
- 📊 Token List
- 🏆 Leaderboard
- ➕ Create Token

**Personal Section:**
- 👤 My Profile
- ⚙️ Creator Dashboard

**Earn Section:**
- 🎁 Rewards
- 👥 Referrals

**Bottom:**
- User Profile Card (avatar, name, wallet)

### Main Content Area:
- Margin-left: 260px
- Margin-top: 70px
- Responsive padding

---

## 🎯 USER FLOWS

### Flow 1: Create Token
```
1. Click "Create Token" (Header or Sidebar)
2. Step 1: Fill Basic Info (with AI assist)
3. Step 2: Upload/Generate Avatar
4. Step 3: Configure Security Settings
5. Step 4: Optional Initial Buy
6. Step 5: Review & Confirm
7. Deploy Transaction
8. Success Screen → View Token or Share
```

### Flow 2: Trade Token
```
1. Browse Token List or Leaderboard
2. Click Token → Token Detail
3. Click Buy/Sell → Trading Panel
4. Select Mode (Basic/Advanced)
5. Enter Amount & Configure Settings
6. Risk Check (Red/Yellow/Green)
7. Execute Transaction
8. Success → +1 Reward Ticket
```

### Flow 3: Earn via Referrals
```
1. Go to Referrals page
2. Copy unique referral link
3. Share on Twitter/Telegram
4. Friend signs up via link
5. Friend trades → You earn 5% of their fees
6. Accumulate earnings
7. Claim to wallet
```

### Flow 4: Play Slot Machine
```
1. Go to Rewards page
2. Check ticket balance
3. Select bet amount (1-5 tickets)
4. Click BET → Reels spin
5. Wait for result (3+ matching)
6. Win → Reward added to balance
7. Claim rewards to wallet
```

### Flow 5: Rank Up
```
1. Earn points via Trade, Referral, Token Creation
2. Progress bar fills up
3. Reach next tier threshold
4. Receive tier rewards (Tickets + SOL)
5. Continue to next tier
```

---

## 📋 SYSTEM FLOWS (D1-D11)

From specification document `PumpFun_Flows_D1_D11.md`:

**D1:** System Overview - Entry point to all flows  
**D2:** Token List - 6 tabs, filters, search  
**D3:** Token Detail - Chart, stats, community  
**D4:** Trading - Buy/Sell, Advanced Orders  
**D5:** Search - Inline in Token List  
**D6:** My Profile - 5 tabs  
**D7:** Public Profile - Read-only  
**D8:** Creator Dashboard - 2-level navigation  
**D8.1:** Token Management Detail - 3 tabs  
**D9:** Create Token - 5 steps  
**D10:** Rewards - Games, Missions, Balance  
**D11:** Referrals - Link, Users, Earnings  

---

## 🔧 TECHNICAL CONSIDERATIONS

### Blockchain Integration:
- Solana Web3.js
- Wallet adapter (Phantom, Solflare, etc.)
- SPL Token program
- Bonding curve smart contract
- Raydium integration for graduation

### Real-time Updates:
- WebSocket for live prices
- Polling for token stats
- Server-sent events for notifications

### AI Integration:
- Description generation API
- Avatar generation API (DALL-E, Midjourney, etc.)

### Storage:
- User profiles
- Token metadata
- Transaction history
- Points tracking
- Referral relationships

### Security:
- Geolocation blocking (Vietnam)
- Wallet signature verification
- Anti-MEV protection
- Rate limiting
- Input validation

---

## ✅ COMPLETED WORK

### Documents (10 FRs):
- ✅ FR-002: Token Detail
- ✅ FR-003: Buy/Sell
- ✅ FR-004: My Profile
- ✅ FR-005: Public Profile
- ✅ FR-006: Creator Dashboard
- ✅ FR-007: Create Token
- ✅ FR-008: Leaderboard
- ✅ FR-009: Rewards & Games
- ✅ FR-010: Referrals
- ✅ System Spec (D1-D11)

### HTML Mockups (11):
- ✅ Home full layout
- ✅ Token detail
- ✅ Trading panel
- ✅ My profile
- ✅ Public profile
- ✅ Creator dashboard
- ✅ Create token
- ✅ Leaderboard
- ✅ Points (needs slot update)
- ✅ Referrals
- ✅ Landing page

---

## 🚧 PENDING WORK

### High Priority:
1. **FR-001:** Token List (MD document)
2. **FR-011:** Points System (rename & document)
3. **Slot Machine:** Update mockup to match FR-009 spec
4. **Token List:** Create HTML mockup

### Medium Priority:
5. **FR-005 Search:** Document inline search requirements
6. **D10 Missions:** Define mission types and rewards
7. **Technical Specs:** Bonding curve formula, API endpoints

### Low Priority:
8. Image placeholders for all FRs
9. Additional mockup states (loading, error, empty)
10. Responsive variants documentation

---

## 📁 FILE ORGANIZATION

```
PumpFunCloneDocument/
├── CLAUDE.md                          # Project definition for AI agents
├── README.md                          # Quick intro & navigation
├── Function Requirements.md           # Master FR document
├── Function Requirements.pdf
├── images/                            # Screenshots for master FR doc
│
├── docs/                              # Individual FR documents & specs
│   ├── FR-INDEX.md
│   ├── FR-001_TokenList.md ... FR-012_TokenWar_ModelAnalysis.md
│   ├── PumpFun_Flows_D1_D11.md
│   └── PUMPFUN_PROJECT_SUMMARY.md     # This file
│
├── mockups/                           # HTML UI mockups
│   ├── home_full_layout.html
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
├── testing/                           # Test documentation
│   ├── TEST_INDEX.md
│   ├── TEST_PLAN.md
│   ├── TEST_CASES_MATRIX.md ... TEST_DATA.md
│   └── TEST_SECURITY_CHECKLIST.md
│
└── design/                            # Design system
    └── UI_UX_DESIGN_SYSTEM.md
```

---

## 📝 IMPORTANT NOTES

### Style Guide for New FRs:
1. Use compact format (see existing FRs)
2. Vietnamese for "Mô tả"
3. Code blocks for requirements
4. Concise, developer-focused
5. Clear acceptance criteria
6. No verbose explanations

### Naming Conventions:
- FRs: `FR-XXX_FeatureName.md`
- Mockups: `feature_name_mockup.html`
- Use underscores for file names
- PascalCase for FR titles in documents

### Common Patterns:
- Entry points always listed first
- Acceptance criteria always at end
- Giao diện section for screenshots/mockups
- Code blocks for technical requirements

---

## 🎯 PROJECT GOALS

**Phase 1 (Current):** Complete all FRs and mockups ✅ (~95% done)  
**Phase 2:** Technical architecture and smart contracts  
**Phase 3:** Frontend implementation  
**Phase 4:** Backend and blockchain integration  
**Phase 5:** Testing and launch  

---

## 📞 CONTEXT FOR NEW PROJECT

When moving to new project, provide:

1. **This summary document** - Complete context
2. **All FR markdown files** - Functional requirements
3. **All HTML mockups** - UI references
4. **System spec document** - Flow overview
5. **Design system** - Colors, typography, components

**Key Points to Remember:**
- Vietnam users blocked
- Compact documentation style
- Vietnamese + English mix
- Developer-focused, no fluff
- All files in `/outputs/` directory

---

**END OF PROJECT SUMMARY**

*Ready to transfer to new Claude Project*
