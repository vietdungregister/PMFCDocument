# PUMPFUN - FUNCTIONAL REQUIREMENTS INDEX

**Last Updated:** April 6, 2026  
**Total FRs:** 14  
**Status:** Core Complete ✅ | New FRs in progress

---

## 📋 DANH SÁCH FUNCTIONAL REQUIREMENTS

### FR-001: Token List (8.4K)
**File:** `FR-001_TokenList.md`  
**Features:**
- 5 tabs: Discover, Trending, Top Volume, Graduated, Favorite
- DiscoverScore algorithm
- TrendingScore algorithm
- Filters: NSFW, Market Cap, Volume, Trust Level
- Sort options
- Search functionality

**Entry Points:** Home page, Navigation menu

---

### FR-002: Token Detail (12K)
**File:** `FR-002_Token_Detail.md`  
**Features:**
- Token metadata display
- Price chart (TradingView)
- Market metrics
- Trust level badges
- Community chat room
- Holders list (top 100)
- Transaction history (50 latest)
- Trading panel (fixed right)

**Entry Points:** Token List, My Profile, Public Profile, Leaderboard

---

### FR-003: Buy/Sell Trading Panel (24K)
**File:** `FR-003_BuySell.md`  
**Features:**
- Market Order (instant trade)
- Limit Order (target price)
- Buy/Sell toggle
- Amount input with currency switch
- Slippage tolerance settings
- Anti-MEV protection
- Priority fee (Normal/Fast/Instant)
- Auto-retry
- Risk assessment
- Real-time updates

**Entry Points:** Token Detail page (fixed panel)

---

### FR-004: My Profile (12K)
**File:** `FR-004_MyProfile.md`  
**Features:**
- 5 tabs: Holding Tokens, Created Tokens, Transaction History, Edit Profile, Limit Orders
- Portfolio stats with P&L
- One-time username/display name setup
- Social links management
- Active limit orders management

**Entry Points:** Main Navigation, Header dropdown

---

### FR-005: Public Profile (6.5K)
**File:** `FR-005_PublicProfile.md`  
**Features:**
- 4 tabs: Profile Info, Holding Tokens, Created Tokens, Transaction History
- Read-only view
- Privacy-aware (can hide Holdings & Transactions)
- Activity stats
- Social links

**Entry Points:** Token Detail, Community Chat, Holders List, Transaction History, Referrals

---

### FR-006: Creator Dashboard (8.7K)
**File:** `FR-006_CreatorDashboard.md`  
**Features:**

**Level 1 - Dashboard:**
- Created Tokens tab (with "Manage Token" button)
- Creator Revenue tab (Total/Unclaimed/Claimed + Claim)

**Level 2 - Token Management:**
- Overview tab (Metrics, chart, token info)
- Trusted Level tab (LP Lock, Audit, Freeze Authority)
- Community Management tab (Create/Edit/Delete/Pin posts)

**Entry Points:** Sidebar menu

---

### FR-007: Create Token (9.0K)
**File:** `FR-007_CreateToken.md`  
**Features:**
- 5-step wizard with progress indicator
- Step 1: Basic Info (Name, Symbol, Statement, Description + AI Assist)
- Step 2: Avatar (Upload or AI Generate)
- Step 3: Security Settings (LP Lock, Audit, Freeze)
- Step 4: Initial Buy (Optional, 0.1-1 SOL)
- Step 5: Review & Create → Success screen

**Entry Points:** Sidebar menu, Header button

---

### FR-008: Leaderboard (4.6K)
**File:** `FR-008_Leaderboard.md`  
**Features:**
- Top 3 featured cards (large display)
- Table list (rank #4+)
- Ranked by Market Cap
- Columns: Token, Creator, Holders, Market Cap, Buy button

**Entry Points:** Sidebar menu

---

### FR-009: Rewards & Games (9.2K)
**File:** `FR-009_Rewards.md`  
**Features:**
- Broadcast banner (Winners marquee)
- Stats cards: Reward Balance + Your Tickets
- Slot Machine (5 reels, 5 symbols: 🌱🌿🌳🍀🌼)
- Payout rules: 3-4 of kind = 0.001 SOL × multiplier, 5 of kind = 0.01 SOL
- Multipliers table
- Rules display
- History table (winning spins)

**Entry Points:** Sidebar menu (Earn section)

---

### FR-010: Referrals (6.2K)
**File:** `FR-010_Referrals.md`  
**Features:**
- Stats overview: Total Referrals, Total Earnings
- Referral link with Copy + Share (Twitter/Telegram)
- Claimable rewards section
- Referred users table (User, Joined, Trade Volume, Your Earnings)
- 5% commission on trading fees

**Entry Points:** Sidebar menu (Earn section)

---

### FR-011: Points & Ranking (5.9K)
**File:** `FR-011_Points.md`  
**Features:**
- Points display: Current / Next Level
- Rank card with progress bar
- 5 Tiers: 🌱 Seed (0), 🌿 Sprout (500), 🌳 Sapling (2K), 🌲 Tree (10K), 🪷 Ancient Tree (50K)
- Points calculation: Referral (NetVolume × 10), Trade (Volume × 5), Token Creation (20-80 pts)
- History table
- Anti-farm mechanisms

**Entry Points:** Sidebar menu

---

### FR-013: Trust Score & Token Lock
**File:** `FR-013_TrustScore.md`  
**Features:**
- Trust Score 0-100 (Token Lock 35 + Creator 35 + Holder 30)
- 3 Shield levels: Bronze / Silver / Gold
- Token Lock system (creator locks own tokens 10-50%, 30-365 days)
- Creator scoring: Initial Buy + Profile + Admin Audit
- Holder scoring: Unique Buyers (Fibonacci) + Distribution
- Anti-gaming measures

**Entry Points:** Token Detail, Token List, Creator Dashboard

---

### FR-014: Club
**File:** `FR-014_Club.md`  
**Features:**
- Club creation (1 token = 1 club, stake 0.5 SOL)
- Club membership (1 user = 1 club, owner approval)
- Club Points & Level system (Lv.1–Lv.20)
- Club Leaderboard (weekly, rewards from Vault)
- Club Owner management panel
- Join/Leave/Kick flows with cooldowns

**Entry Points:** Sidebar menu, Token Detail, My Profile

---

### FR-015: Event & Quest System
**File:** `FR-015_Event.md`  
**Features:**
- Daily Quest (auto-generated, 4 quests + Daily Combo)
- Streak system (7/14/30 day milestones)
- Weekly Challenge (admin-created, tiered rewards)
- Seasonal Event (multi-week, sub-events, World Cup)
- Reward Vault ("mỡ nó rán nó" — self-funded)
- Dual Points integration (Personal + Club)

**Entry Points:** Sidebar menu, Home page banner, Notifications

---

### FR-016: Club War
**File:** `FR-016_ClubWar.md`  
**Features:**
- Club War PvP (Leader challenge → accept/reject)
- War Points scoring (separate from Personal/Club Points)
- Live War Dashboard (real-time feed, score, contributors)
- War Resolution (winner/loser/draw + prize distribution)
- Anti-manipulation (wash trading detection, daily caps)
- War History & Stats

**Entry Points:** Club Detail, Event List, Notifications

---

## 📊 FILE SIZES SUMMARY

```
Total: 12 files, ~121K

FR-003 (Buy/Sell):          24K ████████████████████████
FR-004 (My Profile):        12K ████████████
FR-002 (Token Detail):      12K ████████████
FR-009 (Rewards):            9.2K █████████
FR-007 (Create Token):       9.0K █████████
FR-006 (Creator Dashboard):  8.7K ████████
FR-001 (Token List):         8.4K ████████
FR-005 (Public Profile):     6.5K ██████
FR-010 (Referrals):          6.2K ██████
FR-011 (Points):             5.9K █████
FR-008 (Leaderboard):        4.6K ████
```

---

## 🎯 DEVELOPMENT PRIORITY

### Phase 1: Core Features (High Priority)
1. **FR-001** - Token List (Home page)
2. **FR-002** - Token Detail (View tokens)
3. **FR-003** - Buy/Sell Trading (Main revenue)
4. **FR-007** - Create Token (Content creation)

### Phase 2: User Management (Medium Priority)
5. **FR-004** - My Profile
6. **FR-005** - Public Profile
7. **FR-006** - Creator Dashboard

### Phase 3: Engagement Features (Medium Priority)
8. **FR-008** - Leaderboard
9. **FR-010** - Referrals
10. **FR-011** - Points System

### Phase 4: Gamification (Lower Priority)
11. **FR-009** - Rewards & Games

### Phase 5: Social & Engagement (New)
12. **FR-014** - Club
13. **FR-015** - Event & Quest System
14. **FR-016** - Club War

---

## ✅ COMPLETION STATUS

**Documents:**
- [x] FR-001: Token List
- [x] FR-002: Token Detail
- [x] FR-003: Buy/Sell
- [x] FR-004: My Profile
- [x] FR-005: Public Profile
- [x] FR-006: Creator Dashboard
- [x] FR-007: Create Token
- [x] FR-008: Leaderboard
- [x] FR-009: Rewards & Games
- [x] FR-010: Referrals
- [x] FR-011: Points & Ranking
- [x] FR-014: Club (base draft)
- [x] FR-015: Event & Quest System (base draft)
- [x] FR-016: Club War (base draft)

**HTML Mockups:**
- [x] Home Full Layout
- [x] Token Detail
- [x] Trading Panel
- [x] My Profile
- [x] Public Profile
- [x] Creator Dashboard
- [x] Create Token
- [x] Leaderboard
- [x] Points
- [x] Referrals

---

## 📝 NOTES

### Style Guide:
- Compact format, developer-focused
- Vietnamese descriptions + English code
- Code blocks for requirements
- Clear acceptance criteria
- No verbose explanations

### Key Business Rules:
- Vietnam users BLOCKED (geolocation)
- Creator fee: 1% on all trades
- Referral commission: 5% of trading fees
- Graduation: $69K MC → Raydium
- One-time fields: Username, Display Name

---

**END OF FR INDEX**
