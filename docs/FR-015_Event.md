# FR-015: EVENT & QUEST SYSTEM

## 1. Mô tả

Hệ thống Event & Quest tạo động lực hàng ngày cho user quay lại platform. Gồm Daily Quest (tự động), Weekly Challenge (admin), và Seasonal Event (admin). Rewards tự tài trợ từ Reward Vault ("mỡ nó rán nó").

**User Story:**

```
Là một user,
Tôi muốn hoàn thành daily quests và tham gia events,
Để kiếm Points, SOL rewards, và duy trì streak bonus.
```

----------

## 2. Giao diện

[To be added]

----------

## 3. ĐIỂM TRUY CẬP (ENTRY POINTS)

Users có thể truy cập Events từ:

1. **Main Navigation** — Sidebar menu "Events"
2. **Home Page** — Banner event đang diễn ra
3. **Notification** — Push khi có event mới hoặc quest chưa hoàn thành
4. **Direct URL** — /events, /events/:id

**Default:** Hiển thị tab "Live" với các event đang diễn ra

----------

## 4. YÊU CẦU CHỨC NĂNG

### 4.1. Event List Page

**FR-EVT-015.1: Danh sách Event**

**Mô tả:**
Trang chính hiển thị tất cả events theo trạng thái.

**Yêu cầu:**

```
Page Structure:

1. Header
   - Title: "Events"
   - Stats: "X live · X upcoming"

2. Filter Tabs
   - [All] [Live (badge count)] [Upcoming] [Ended]

3. Event Cards (full-width, stacked)
   - Each card:
     * Status badge: [NEW] (green) / [HOT] (red) / [ENDING] (amber)
     * Event name (bold, large)
     * Description (1 line)
     * Event icon (right side)
     * Stats: "● Live · X joined · ⏱ Xd left"
     * "Join >" button (primary)
   - Gradient background per event type:
     * Quest: warm orange gradient
     * Challenge: purple gradient
     * Seasonal: teal gradient
     * Club War: red gradient

4. Event Types:
   - Daily Quest (auto-generated)
   - Weekly Challenge (admin-created)
   - Seasonal Event (admin-created)
   - Club War Event (auto-generated from Club War)

VÀ event list PHẢI:
- Sort by: Live first, then Upcoming, then Ended
- Auto-update status when event starts/ends
- Real-time participant count
- Responsive layout
```

**Acceptance Criteria:**

- [ ] Filter tabs work
- [ ] Status badges accurate
- [ ] Participant count real-time
- [ ] Auto-update when event status changes
- [ ] Gradient backgrounds per type
- [ ] Responsive layout

----------

### 4.2. Daily Quest

**FR-EVT-015.2: Daily Quest System**

**Mô tả:**
Hệ thống quest tự động, reset mỗi ngày 00:00 UTC. Không cần admin tạo.

**Yêu cầu:**

```
Daily Quests (auto-generated mỗi ngày):

┌──────────────────────────────────┬────────────┬───────────┐
│ Quest                            │ Personal Pts│ Club Pts  │
├──────────────────────────────────┼────────────┼───────────┤
│ Login vào platform               │ +5         │ +2        │
│ Trade 1 lần (≥ 0.1 SOL)         │ +10        │ +5        │
│ Bet 1 Arena                      │ +15        │ +10       │
│ Trade token của club mình         │ +20        │ +20       │
├──────────────────────────────────┼────────────┼───────────┤
│ DAILY COMBO (hoàn thành tất cả)  │ +50 BONUS  │ +30 BONUS │
│                                  │ + 0.01 SOL │           │
└──────────────────────────────────┴────────────┴───────────┘

Quest UI (inside Event Detail):

1. Quest List
   - Each quest = 1 row
   - Left: Icon + Quest name
   - Right: Reward info + Status
   - Status: [ ] Incomplete → [✓] Complete (green check)
   - Progress: "0/1" → "1/1"
   - Auto-mark complete khi detect hành động

2. Daily Combo Bar
   - Progress: "2/4 quests completed"
   - Progress bar (segments, not continuous)
   - Khi 4/4: celebration animation + auto-claim rewards
   - Hiển thị: "🎁 Daily Combo: +50 pts + 0.01 SOL"

3. Streak Counter
   - "🔥 Streak: X days"
   - Streak = số ngày liên tiếp hoàn thành Daily Combo
   - Streak milestones:
     * 7 ngày: thưởng gấp 2x ngày thứ 7
     * 14 ngày: thưởng gấp 3x ngày thứ 14
     * 30 ngày: badge "30-Day Warrior" + 0.1 SOL bonus
   - Mất streak nếu miss 1 ngày

4. Timer
   - Countdown: "Resets in X:XX:XX"
   - Reset: 00:00 UTC daily

VÀ daily quest PHẢI:
- Auto-generate mỗi ngày, không cần admin
- Auto-detect completion (trade, bet, login)
- Auto-reset 00:00 UTC
- Track streak accurately
- Claim rewards tự động khi complete
- Quest 4 (trade token club) chỉ hiện nếu user đã join club
```

**Streak Rewards:**

```
Streak tính khi user hoàn thành DAILY COMBO (tất cả 4 quest):

┌─────────────┬────────────────────────────────┐
│ Streak Day  │ Bonus                          │
├─────────────┼────────────────────────────────┤
│ Day 1-6     │ Normal rewards                 │
│ Day 7       │ 2x Points + 2x SOL bonus       │
│ Day 8-13    │ Normal rewards                 │
│ Day 14      │ 3x Points + 3x SOL bonus       │
│ Day 15-29   │ Normal rewards                 │
│ Day 30      │ Badge + 0.1 SOL bonus          │
│ Day 31+     │ Normal + permanent 1.5x mult   │
└─────────────┴────────────────────────────────┘

Miss 1 ngày → streak reset về 0.
SOL bonus từ Reward Vault.
Nếu Vault < 5 SOL → chỉ thưởng Points, không SOL.
```

**Acceptance Criteria:**

- [ ] 4 quests generated daily
- [ ] Auto-detect completion accurate
- [ ] Daily Combo triggers at 4/4
- [ ] SOL reward claimed from Vault
- [ ] Streak tracking accurate
- [ ] Streak milestones trigger bonus
- [ ] Streak reset on miss
- [ ] Timer countdown accurate
- [ ] Quest 4 conditional on club membership
- [ ] Vault safety rule enforced

----------

### 4.3. Weekly Challenge

**FR-EVT-015.3: Weekly Challenge**

**Mô tả:**
Event do admin tạo, kéo dài 1 tuần, với mục tiêu cụ thể và leaderboard.

**Yêu cầu:**

```
Admin tạo Weekly Challenge:

1. Challenge Info
   - Title * (max 60 chars)
   - Description * (max 200 chars)
   - Duration: auto 7 days (Monday → Sunday)
   - Reward Pool: X SOL (từ Reward Vault hoặc admin set)

2. Challenge Type (chọn 1):
   - TRADING: "Trade X tokens khác nhau"
   - ARENA: "Bet X kèo Arena"
   - VOLUME: "Đạt X SOL trading volume"
   - REFERRAL: "Mời X người mới"
   - CLUB: "Club đạt X points tuần này"

3. Goal Setting
   - Target: số lượng cần đạt (ví dụ: 10 trades)
   - Tiers (optional):
     * Bronze: hoàn thành 50% → reward nhỏ
     * Silver: hoàn thành 100% → reward vừa
     * Gold: hoàn thành 200% → reward lớn

Challenge UI (Event Detail page):

1. Challenge Header
   - Title + description
   - Time remaining: "X days Xh left"
   - Participants: "X joined"
   - Your progress: "X/Y completed"

2. Progress Section
   - Progress bar
   - Tier badges: [Bronze ✓] [Silver ...] [Gold ...]
   - Current tier highlight

3. Challenge Leaderboard
   - Top participants ranked by progress
   - Columns: Rank | User | Progress | Reward
   - Your rank highlighted

4. Rewards
   - Tier rewards (for reaching milestone)
   - Leaderboard rewards (top 10):
     * #1: 30% pool
     * #2: 20% pool
     * #3: 15% pool
     * #4-10: chia 35% còn lại
   - Auto-distribute khi challenge ends

VÀ weekly challenge PHẢI:
- Admin tạo trước, schedule start time
- Auto-start / auto-end
- Track progress real-time
- Auto-distribute rewards khi kết thúc
- Leaderboard real-time
```

**Acceptance Criteria:**

- [ ] Admin can create challenge
- [ ] Challenge types all functional
- [ ] Progress tracking real-time
- [ ] Tier system works
- [ ] Leaderboard accurate
- [ ] Rewards auto-distributed
- [ ] Challenge auto-starts/ends

----------

### 4.4. Seasonal Event

**FR-EVT-015.4: Seasonal Event**

**Mô tả:**
Event lớn do admin tạo, gắn với sự kiện thực (World Cup, Bull Market...), kéo dài nhiều tuần, chứa nhiều sub-events.

**Yêu cầu:**

```
Admin tạo Seasonal Event:

1. Event Info
   - Title * (e.g., "World Cup 2026 Festival")
   - Description *
   - Banner image *
   - Duration: custom (ví dụ 30 ngày)
   - Reward Pool: X SOL

2. Sub-Events (admin tạo bên trong seasonal)
   - Mỗi seasonal chứa nhiều sub-events:
     * Weekly Challenges
     * Special Quests (one-time)
     * Club War Tournament (bracket)
     * Prediction Leaderboard

3. Seasonal Quests (one-time, special):
   Ví dụ World Cup:
   ┌──────────────────────────────────┬────────┐
   │ Quest                            │ Reward │
   ├──────────────────────────────────┼────────┤
   │ Bet đúng 5 kèo bóng đá          │ NFT Badge │
   │ Bet đúng 10 kèo liên tiếp       │ 0.5 SOL   │
   │ Đạt top 10 prediction accuracy   │ 1 SOL     │
   │ Club rank top 3 trong seasonal   │ 2 SOL     │
   └──────────────────────────────────┴────────┘

Seasonal Event UI:

1. Event Landing Page
   - Banner (full-width, hero image)
   - Title + countdown: "Ends in X days"
   - Overall progress: "You completed X/Y quests"
   - Reward pool display

2. Sub-Event List
   - Cards for each sub-event
   - Status: [Active] [Upcoming] [Completed]
   - Click → sub-event detail

3. Seasonal Leaderboard
   - Tổng hợp points từ tất cả sub-events
   - Top performers overall
   - Club leaderboard (club nào tham gia mạnh nhất)

4. Reward Tiers
   - Overall completion tiers:
     * 25% quests done → Bronze badge
     * 50% → Silver badge
     * 75% → Gold badge
     * 100% → Legendary badge + SOL bonus

VÀ seasonal event PHẢI:
- Support nhiều sub-events
- Track overall progress across sub-events
- Seasonal leaderboard aggregated
- Auto-distribute rewards khi event ends
- Banner hiển thị trên Home page khi active
```

**Acceptance Criteria:**

- [ ] Admin can create seasonal event
- [ ] Sub-events manageable
- [ ] Overall progress tracking works
- [ ] Seasonal leaderboard accurate
- [ ] Reward tiers trigger correctly
- [ ] Banner on Home page when active
- [ ] Auto-distribute rewards

----------

### 4.5. Reward Vault

**FR-EVT-015.5: Reward Vault (Mỡ nó rán nó)**

**Mô tả:**
Vault tự tài trợ, thu phí từ Arena/Trading, chi trả rewards cho Events/Quests/Club Leaderboard.

**Yêu cầu:**

```
NGUỒN VÀO:

┌──────────────────────────────────┬────────────────┐
│ Nguồn                            │ Tỷ lệ          │
├──────────────────────────────────┼────────────────┤
│ Arena fee                        │ 1% tổng pool   │
│ (trích từ 5% rake)              │ (= 20% of rake)│
│                                  │                │
│ Trading fee                      │ 0.1% volume    │
│ (trích từ 1% creator fee)       │ (= 10% of fee) │
│                                  │                │
│ Club War platform cut            │ 10% prize pool │
│                                  │                │
│ Arena/War void (không có winner) │ 100% pool      │
└──────────────────────────────────┴────────────────┘

NGUỒN RA:

┌──────────────────────────────────┬─────────────┐
│ Chi                              │ Tần suất    │
├──────────────────────────────────┼─────────────┤
│ Daily Combo reward (0.01 SOL)    │ Per user/day│
│ Streak milestone bonus           │ Per trigger │
│ Weekly Club Leaderboard top 3    │ Weekly      │
│ Weekly Challenge prizes          │ Weekly      │
│ Club War prize pool contribution │ Per war     │
│ Seasonal Event prize pool        │ Per season  │
└──────────────────────────────────┴─────────────┘

SAFETY RULES:

1. Vault Balance < 5 SOL:
   → Tạm ngưng thưởng SOL
   → Chỉ thưởng Points
   → Badge: "Reward Vault low — Points only"
   → Resume SOL khi Vault > 5 SOL

2. Daily SOL Payout Cap:
   → Max payout per day = 10% Vault balance
   → Tránh drain vault trong 1 ngày
   → Nếu vượt cap → queue, trả ngày hôm sau

3. Vault Dashboard (admin only):
   - Current balance
   - Income chart (daily/weekly/monthly)
   - Expense chart
   - Projected runway (bao lâu nữa hết tiền)
   - Manual top-up option

VÀ vault PHẢI:
- Auto-collect fees real-time
- Auto-distribute rewards
- Never go negative
- Admin dashboard accessible
- Transparent logging
```

**Acceptance Criteria:**

- [ ] Fee collection from Arena accurate
- [ ] Fee collection from Trading accurate
- [ ] Club War cut collected
- [ ] Safety rule triggers at < 5 SOL
- [ ] Daily payout cap enforced
- [ ] Admin dashboard shows accurate data
- [ ] Vault never goes negative
- [ ] Resume SOL rewards when > 5 SOL

----------

### 4.6. Points Integration (Dual System)

**FR-EVT-015.6: Tích hợp 2 hệ Points**

**Mô tả:**
Mọi hành động trong Event/Quest đồng thời tạo Personal Points và Club Points.

**Yêu cầu:**

```
Points Mapping — mỗi hành động feed CẢ 2 hệ:

┌──────────────────────────────────┬────────────┬───────────┐
│ Hành động                        │ Personal   │ Club      │
├──────────────────────────────────┼────────────┼───────────┤
│ Trade token (per 0.1 SOL)        │ +10        │ +5        │
│ Trade token CỦA CLUB (per 0.1)  │ +10        │ +20       │
│ Bet Arena (per 0.1 SOL)          │ +15        │ +10       │
│ Bet Arena đúng                    │ +50        │ +30       │
│ Daily login                       │ +5         │ +2        │
│ Complete daily quest              │ +20        │ +15       │
│ Daily Combo                       │ +50        │ +30       │
│ Referral (người mới trade)        │ +100       │ +50       │
│ Tham gia Club War                 │ +30        │ +30       │
│ Club War — club thắng             │ +100       │ +500      │
│ Weekly Challenge completion       │ varies     │ varies    │
│ Seasonal Quest completion         │ varies     │ varies    │
└──────────────────────────────────┴────────────┴───────────┘

Quy tắc:
- Personal Points: tích lũy vĩnh viễn, dùng cho tier system
  (🌱 Seed → 🌿 Sprout → 🌳 Sapling → 🌲 Tree → 🪷 Ancient Tree)
- Club Points: all-time (cho Level) + weekly (cho Leaderboard)
- Nếu user KHÔNG ở club nào → chỉ nhận Personal Points
- Nếu user ở club → nhận CẢ HAI
- Anti-farm: chỉ tính trade ≥ 0.01 SOL, bet ≥ 0.1 SOL

Personal Tier Benefits (mở rộng từ FR-011):
┌────────────────┬──────────────────────────────┐
│ Tier           │ Benefit                      │
├────────────────┼──────────────────────────────┤
│ 🌱 Seed        │ —                            │
│ 🌿 Sprout      │ Daily Combo SOL enabled      │
│ 🌳 Sapling     │ Fee discount -0.5%           │
│ 🌲 Tree        │ Fee discount -1% + tạo War   │
│ 🪷 Ancient Tree │ Exclusive Arena + 1.5x pts  │
└────────────────┴──────────────────────────────┘

VÀ points integration PHẢI:
- Đồng bộ cả 2 hệ khi action xảy ra
- Hiển thị dual reward: "+10 pts | +5 club pts"
- Anti-farm rules consistent
- Tier benefits applied automatically
```

**Acceptance Criteria:**

- [ ] Both point systems update on every action
- [ ] Dual display works (personal + club)
- [ ] No club → only personal points
- [ ] Anti-farm rules enforced
- [ ] Tier benefits auto-applied
- [ ] Points accurate across all sources

----------

## 5. BUSINESS RULES

```
Core Rules:
- Daily Quest reset 00:00 UTC, auto-generated
- Streak = consecutive Daily Combo completions
- Streak reset nếu miss 1 ngày
- Reward Vault tự tài trợ — không marketing budget
- Vault < 5 SOL → only Points, no SOL
- Daily payout cap = 10% Vault balance
- Weekly Challenge auto-start/end
- Seasonal Event admin-managed
- All rewards logged and auditable
- Points anti-farm: trade ≥ 0.01 SOL, bet ≥ 0.1 SOL
```

----------

## 6. ĐIỀU KIỆN CHẤP NHẬN (ACCEPTANCE CRITERIA)

**Overall:**

- [ ] Event list page functional
- [ ] All 4 event types work
- [ ] Rewards distributed correctly
- [ ] Points dual system accurate
- [ ] Responsive on all devices

**Daily Quest:**

- [ ] Auto-generated daily
- [ ] Auto-detect completion
- [ ] Daily Combo works
- [ ] Streak tracking accurate
- [ ] Streak milestones trigger

**Weekly Challenge:**

- [ ] Admin creation works
- [ ] Progress tracking real-time
- [ ] Leaderboard accurate
- [ ] Auto-distribution works

**Seasonal Event:**

- [ ] Sub-events manageable
- [ ] Overall progress aggregated
- [ ] Banner on Home page

**Reward Vault:**

- [ ] Auto-collect fees
- [ ] Safety rules enforced
- [ ] Admin dashboard accurate
- [ ] Never negative balance

----------

**END OF FR-015**
