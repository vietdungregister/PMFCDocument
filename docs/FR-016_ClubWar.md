# FR-016: CLUB WAR

## 1. Mô tả

Club War là cơ chế đối kháng giữa 2 clubs. Gồm 2 loại: Passive (Weekly Leaderboard tự động) và Active PvP (Club Leader thách đấu trực tiếp). Members earn War Points qua trade, bet, quest — club nhiều War Points hơn thắng.

**User Story:**

```
Là một Club Leader,
Tôi muốn thách đấu club khác,
Để cạnh tranh, tạo hype cho token, và kiếm prizes cho members.

Là một Club Member,
Tôi muốn đóng góp cho club trong war,
Để giúp club thắng và nhận rewards.
```

----------

## 2. Giao diện

[To be added]

----------

## 3. ĐIỂM TRUY CẬP (ENTRY POINTS)

Users có thể truy cập Club War từ:

1. **Club Detail** — Tab "Wars"
2. **Event List** — Club War events auto-generated
3. **Notification** — Khi club bị thách đấu hoặc war bắt đầu
4. **Direct URL** — /club-war/:id

**Default:** War detail page với live stats

----------

## 4. YÊU CẦU CHỨC NĂNG

### 4.1. Club War PvP — Tạo Challenge

**FR-CW-016.1: Thách đấu Club**

**Mô tả:**
Club Leader tạo thách đấu, chọn đối thủ, stake SOL.

**Yêu cầu:**

```
Điều kiện tạo war:
- Là Club Owner
- Club Level ≥ 10 (unlock tại FR-014)
- Club không đang trong war active khác
- Club đối thủ không đang trong war active

Create Challenge Flow:

1. Chọn đối thủ
   - Search/browse clubs
   - Hiển thị: Club name, Level, Members, Win Rate
   - Không chọn được club đang trong war

2. Chọn Duration
   - Options: [24h] [48h] [72h]
   - Default: 48h

3. Stake
   - Input: số SOL stake (min 1 SOL)
   - Source: Leader bỏ tiền cá nhân
   - Display: "Club đối thủ sẽ phải stake tương đương"
   - Lưu ý: Leader có thể kêu gọi members
     góp vào stake (V2 — treasury system)

4. War Rules Preview
   - Hiển thị scoring rules
   - "Members sẽ bị lock — không thể rời club"
   - "War bắt đầu 1h sau khi đối thủ accept"

5. Confirm & Send Challenge
   - Sign transaction → stake locked
   - Challenge gửi đến Club Leader đối thủ
   - Status: PENDING
   - Auto-expire nếu không accept trong 24h

VÀ challenge PHẢI:
- Validate tất cả điều kiện
- Lock stake SOL
- Notify đối thủ
- Auto-expire sau 24h
```

**Acceptance Criteria:**

- [ ] Club Level ≥ 10 enforced
- [ ] No concurrent wars enforced
- [ ] Opponent search works
- [ ] Stake locked correctly
- [ ] Challenge sent to opponent
- [ ] Auto-expire after 24h
- [ ] Reject returns stake

----------

### 4.2. Accept / Reject Challenge

**FR-CW-016.2: Phản hồi thách đấu**

**Mô tả:**
Club Leader đối thủ nhận và phản hồi thách đấu.

**Yêu cầu:**

```
Notification cho Club Leader đối thủ:

"⚔️ [CLUB_A] thách đấu club bạn!
 Duration: 48h
 Stake: 2 SOL mỗi bên
 [Accept] [Reject]"

ACCEPT:
1. Leader stake SOL tương đương (2 SOL)
2. War status: PREPARING (1h countdown)
3. Cả 2 club nhận notification: "War bắt đầu sau 1h!"
4. Members cả 2 club bị lock membership
5. Sau 1h → War status: ACTIVE

REJECT:
1. Challenge cancelled
2. Stake hoàn lại cho Leader A
3. Notification: "[CLUB_B] từ chối thách đấu"

NO RESPONSE (24h):
1. Auto-reject
2. Stake hoàn lại cho Leader A
3. Notification: "Challenge hết hạn"

VÀ response flow PHẢI:
- Accept → lock stake + start countdown
- Reject → refund immediately
- Timeout → auto-reject + refund
- Lock members khi PREPARING
```

**Acceptance Criteria:**

- [ ] Accept flow works (stake + countdown)
- [ ] Reject returns stake
- [ ] Auto-expire after 24h
- [ ] Members locked on PREPARING
- [ ] Notifications sent to all parties
- [ ] 1h preparation countdown accurate

----------

### 4.3. War Period — Scoring

**FR-CW-016.3: War Points & Scoring**

**Mô tả:**
Trong war period, mọi hành động của members được chấm War Points. Club nhiều điểm hơn thắng.

**Yêu cầu:**

```
War Points Scoring:

┌────────────────────────────────────┬───────────┐
│ Hành động                          │ War Points│
├────────────────────────────────────┼───────────┤
│ Trade token CỦA CLUB MÌNH         │ +20       │
│ Trade token bất kỳ (≥ 0.1 SOL)    │ +5        │
│ Bet Arena bất kỳ (≥ 0.1 SOL)      │ +10       │
│ Bet Arena đúng                     │ +25       │
│ Complete daily quest               │ +15       │
│ Invite friend join club            │ +50       │
│                                    │           │
│ KHÔNG TÍNH:                        │           │
│ - Trade < 0.01 SOL                 │ 0         │
│ - Bet < 0.1 SOL                    │ 0         │
│ - Wash trading (self-trade)        │ 0         │
│ - Trade từ account < 24h tuổi      │ 0         │
└────────────────────────────────────┴───────────┘

Anti-Manipulation:
- Mỗi wallet chỉ tính max 50 trades/ngày cho War Points
- Invite friend: friend phải trade ≥ 0.1 SOL mới tính
- Detect wash trading: mua-bán liên tục cùng token trong 5 phút → không tính

Quy tắc:
- War Points CHỈ tính trong war period
- War Points TÁCH BIỆT với Personal Points và Club Points
  (Personal/Club Points vẫn tính bình thường song song)
- War Points chỉ phục vụ xác định thắng/thua war này
```

**Acceptance Criteria:**

- [ ] All scoring actions tracked correctly
- [ ] Anti-manipulation rules enforced
- [ ] War Points separate from Personal/Club Points
- [ ] Real-time accumulation
- [ ] Only count during war period
- [ ] Wash trading detected

----------

### 4.4. War Live Dashboard

**FR-CW-016.4: Giao diện War Live**

**Mô tả:**
Dashboard real-time hiển thị trạng thái war, điểm, và top contributors.

**Yêu cầu:**

```
War Detail Page:

1. War Header
   - Status badge: [PREPARING] / [LIVE] / [ENDED]
   - Countdown: "Ends in X:XX:XX"
   - VS display:
     [Club A Avatar] [Club A Name]  ⚔️  [Club B Name] [Club B Avatar]
     [Club A Level]                      [Club B Level]

2. Score Board (center, prominent)
   - Club A War Points | VS | Club B War Points
   - Leading indicator: bar chart showing ratio
   - Real-time update animation (pulse on new points)

3. Live Feed
   - Chronological activity feed:
     * "🟢 UserX (Club A) traded 2 SOL PEPE → +20 pts"
     * "🔴 UserY (Club B) bet 1 SOL Arena → +10 pts"
     * "🟢 UserZ joined Club A → +50 pts"
   - Auto-scroll, newest on top
   - Filter by: [All] [Club A] [Club B]

4. Top Contributors
   - Tab: [Club A] [Club B]
   - Table: Rank | User | War Points | Actions
   - Top 3 highlighted
   - Your position highlighted (if member)

5. War Stats
   - Total trades during war
   - Total Arena bets during war
   - Total volume (SOL)
   - New members joined during war

6. Prize Pool Display
   - Total pool: X SOL
   - Breakdown: Stake A + Stake B + Fee contribution
   - "Winner takes: X SOL (80%)"

VÀ live dashboard PHẢI:
- WebSocket real-time updates
- Smooth animations on score changes
- Responsive layout
- Auto-refresh every 5s fallback
```

**Acceptance Criteria:**

- [ ] VS display shows both clubs
- [ ] Score board real-time accurate
- [ ] Live feed updates instantly
- [ ] Top contributors ranked correctly
- [ ] War stats accurate
- [ ] Prize pool calculated correctly
- [ ] Countdown timer accurate
- [ ] Responsive on mobile

----------

### 4.5. War Resolution

**FR-CW-016.5: Kết thúc War & Chia thưởng**

**Mô tả:**
Khi war period kết thúc, xác định thắng/thua/hòa và distribute prizes.

**Yêu cầu:**

```
Kết thúc War:

1. Timer = 0 → War status: RESOLVING

2. Xác định kết quả:
   - Club A War Points > Club B → Club A WINS
   - Club B War Points > Club A → Club B WINS
   - Club A War Points = Club B → DRAW

3. CASE: CÓ WINNER

Prize Pool Calculation:
  Total = Stake_A + Stake_B + Fee_contribution
  Fee_contribution = (Total trades + bets during war) × 10% fee trích

Distribution:
┌────────────────┬─────────────┬──────────────────────────┐
│ Recipient      │ %           │ Mô tả                    │
├────────────────┼─────────────┼──────────────────────────┤
│ Club thắng     │ 80%         │ Chia theo contribution   │
│ Club thua      │ 10%         │ Top 3 contributors       │
│ Platform       │ 10%         │ → Reward Vault           │
└────────────────┴─────────────┴──────────────────────────┘

Club thắng distribution (80%):
  - Option A (Equal): chia đều cho tất cả members
  - Option B (Contribution): theo % War Points đóng góp
  - Club Owner chọn trước khi war bắt đầu (setting trong FR-014)

Club thua consolation (10%):
  - Top 1 contributor: 50% of 10%
  - Top 2: 30% of 10%
  - Top 3: 20% of 10%

Bonus Points:
  - Club thắng: +500 Club Points
  - Club thua: +100 Club Points (tham gia)
  - Members club thắng: +100 Personal Points mỗi người
  - Members club thua: +30 Personal Points mỗi người

4. CASE: HÒA (War Points bằng nhau)

  - Hoàn 100% stake cho cả 2 bên
  - Fee contribution → Reward Vault (100%)
  - Platform KHÔNG thu phí
  - Cả 2 club: +200 Club Points
  - Tất cả members: +50 Personal Points

5. Post-War:
  - Unlock members → tự do chuyển club
  - War status: COMPLETED
  - Result visible trong Club Detail → Tab Wars
  - Notification cho tất cả members với kết quả

VÀ resolution PHẢI:
- Auto-resolve khi timer = 0
- Calculate prize pool accurately
- Distribute SOL to wallets
- Award Points correctly
- Unlock members
- Log everything for audit
```

**Acceptance Criteria:**

- [ ] Auto-resolve at timer end
- [ ] Winner determined correctly
- [ ] Prize pool calculated accurately
- [ ] Distribution per selected method
- [ ] Consolation for losers works
- [ ] Draw handling: full refund, no fee
- [ ] Points awarded correctly
- [ ] Members unlocked
- [ ] Notifications sent
- [ ] Results logged in war history

----------

### 4.6. War Result Screen

**FR-CW-016.6: Màn hình kết quả**

**Mô tả:**
Celebration / Result screen sau khi war kết thúc.

**Yêu cầu:**

```
Result Screen:

1. WINNER Case:
   - Banner: "🏆 [CLUB_A] WINS!"
   - Confetti animation
   - Final score: XXX vs XXX
   - MVP: Top contributor (highlighted card)
   - Prize breakdown:
     * "Club [A] nhận X SOL"
     * "Your share: X SOL"
   - "Claim Reward" button
   - Share: "Share on Twitter"

2. LOSER Case:
   - Banner: "⚔️ War Ended"
   - Final score
   - Consolation: "Top contributors nhận X SOL"
   - Your consolation (if top 3): "You earned X SOL"
   - "View Winning Club" link

3. DRAW Case:
   - Banner: "🤝 It's a Draw!"
   - Final score: XXX vs XXX
   - "Stake hoàn lại: X SOL"
   - Both clubs: "+200 Club Points"
   - "Rematch?" button (tạo challenge mới)

4. War Summary Stats:
   - Duration
   - Total War Points both sides
   - Total trades during war
   - Total Arena bets
   - Total volume
   - New members joined
   - MVP both sides

Twitter Share Text:
"⚔️ [CLUB_A] won Club War vs [CLUB_B]!
 Score: XXX - XXX
 Prize: X SOL
 MVP: @[USER]
 Join the fight on @PumpFunSOL!
 #ClubWar #Solana"

VÀ result screen PHẢI:
- Show immediately when war resolves
- Celebration animation (winner)
- Claim button functional
- Share functional
- Stats accurate
```

**Acceptance Criteria:**

- [ ] Winner screen with celebration
- [ ] Loser screen with consolation
- [ ] Draw screen with refund info
- [ ] Claim reward functional
- [ ] Twitter share works
- [ ] Stats accurate
- [ ] Rematch button works (draw case)

----------

### 4.7. War History & Stats

**FR-CW-016.7: Lịch sử War**

**Mô tả:**
Lịch sử tất cả wars của club, accessible từ Club Detail → Tab Wars.

**Yêu cầu:**

```
War History Table:

Columns:
1. Opponent — Club avatar + name
2. Result — [WON ✅] / [LOST ❌] / [DRAW 🤝]
3. Score — XXX - XXX
4. Prize — X SOL won/lost
5. Duration — 24h / 48h / 72h
6. Date — "Mar 15, 2026"
7. Action — "View Details" → War Detail page

Stats Summary (top of tab):
- Total Wars: X
- Wins: X | Losses: X | Draws: X
- Win Rate: XX%
- Total Prizes Won: X SOL
- Total Prizes Lost: X SOL
- Biggest Win: X SOL vs [CLUB]
- Current Streak: X wins

VÀ war history PHẢI:
- Sorted newest first
- Pagination
- Filter: [All] [Won] [Lost] [Draw]
- Stats calculated accurately
```

**Acceptance Criteria:**

- [ ] History table displays all wars
- [ ] Results accurate
- [ ] Stats summary correct
- [ ] Filter works
- [ ] View Details links to war page
- [ ] Pagination works

----------

## 5. BUSINESS RULES

```
Core Rules:
- Club Level ≥ 10 required để tạo war
- 1 club chỉ 1 active war tại mọi thời điểm
- Members lock khi war PREPARING hoặc ACTIVE
- Minimum stake: 1 SOL per side
- Challenge expires after 24h if no response
- 1h preparation period after accept
- Duration options: 24h / 48h / 72h
- Prize: 80% winner / 10% loser top 3 / 10% platform
- Draw: 100% refund, no platform fee
- Anti-manipulation: max 50 trades/day for War Points
- Wash trading detection: buy-sell same token within 5 min
- New accounts < 24h old: War Points not counted
- War Points are SEPARATE from Personal/Club Points
```

----------

## 6. ĐIỀU KIỆN CHẤP NHẬN (ACCEPTANCE CRITERIA)

**Overall:**

- [ ] Full war lifecycle works (create → accept → active → resolve)
- [ ] Prize pool calculated and distributed correctly
- [ ] Members locked during war
- [ ] Anti-manipulation effective
- [ ] Real-time dashboard functional

**Challenge:**

- [ ] Create challenge works
- [ ] Accept/Reject/Timeout all work
- [ ] Stake locked and refunded correctly

**War Period:**

- [ ] War Points tracked accurately
- [ ] Anti-manipulation rules enforced
- [ ] Live dashboard real-time
- [ ] Live feed shows activities

**Resolution:**

- [ ] Winner determined correctly
- [ ] Prize distributed accurately
- [ ] Draw handled correctly (full refund)
- [ ] Points awarded
- [ ] Members unlocked
- [ ] History recorded

----------

**END OF FR-016**
