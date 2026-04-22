# FR-009: PHẦN THƯỞNG & TRÒ CHƠI (REWARDS & GAMES)

## 1. Mô tả

Hệ thống phần thưởng với slot machine game, cho phép users dùng tickets để chơi và win SOL rewards.

**User Story:**

```
Là một user,
Tôi muốn dùng tickets để chơi game và win SOL,
Để tăng thêm thu nhập và có trải nghiệm vui.
```

----------

## 2. Giao diện

[To be added]

----------

## 3. ĐIỂM TRUY CẬP (ENTRY POINTS)

Users có thể truy cập Rewards từ:

1. **Main Navigation** - Sidebar menu "Rewards"
2. **Direct URL** - /rewards

**Default:** Hiển thị slot machine game

----------

## 4. YÊU CẦU CHỨC NĂNG

### 4.1. Page Layout

**FR-RWD-009.1: Cấu trúc Trang**

**Mô tả:**  
Layout với broadcast banner, stats cards, slot machine, và history.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Page Structure:

1. Broadcast Banner (Marquee)
   - Live feed của winners
   - Auto-scroll horizontally
   - Pause on hover

2. Stats Cards (2 cards - grid 2 columns)
   - Reward Balance (left)
   - Your Tickets (right)

3. Slot Machine (5 reels)
   - Center display area
   - Spin animation

4. Game Info (2 columns)
   - Multipliers table (left)
   - Rules (right)

5. History Table
   - Past spins và payouts

VÀ rewards page PHẢI:
- Login required
- Real-time updates
- Responsive layout
```

**Acceptance Criteria:**

- [ ] All sections display
- [ ] Marquee scrolls smoothly
- [ ] Slot machine renders correctly
- [ ] Layout responsive

----------

### 4.2. Broadcast Banner

**FR-RWD-009.2: Winners Feed**

**Mô tả:**  
Marquee banner hiển thị live winners.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Marquee Banner:

1. Content Items
   Each item shows:
   - Dot indicator: ⚪ (white)
   - Username: "Guest #XXXXXXX" (green, bold)
   - Action: "bet X tickets won X.XXXXXX SOL"
   - Time: "Xd/h/m ago"
   
   Format example:
   "⚪ Guest #9308943 bet 1 ticket won 0.003916 SOL 5d ago"

2. Behavior
   - Auto-scroll left continuously
   - Infinite loop (items duplicate)
   - Pause on hover
   - Smooth animation (~30s per full cycle)

3. Styling
   - Gradient fade on left/right edges
   - Rounded pills for each item
   - Background: semi-transparent card
   - Border: subtle

VÀ marquee PHẢI:
- Real-time updates when new wins
- Smooth continuous scrolling
- No gaps or jumps
```

**Acceptance Criteria:**

- [ ] Marquee scrolls continuously
- [ ] Pause on hover works
- [ ] Gradient fades visible
- [ ] Real-time winners appear
- [ ] No visual glitches

----------

### 4.3. Stats Cards

**FR-RWD-009.3: Reward & Tickets Display**

**Mô tả:**  
Hiển thị claimable rewards và available tickets.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Stats Cards (Grid 2 columns):

Card 1: Reward Balance
- Label: "Reward" (uppercase, gray, small)
- Value: X.XXX SOL (large 32px, green)
- Button: "CLAIM" (full width)
- States:
  * Disabled (gray, 60% opacity) when balance = 0
  * Enabled (green) when balance > 0
- Action: Transfer SOL to wallet
- Requires: Connected wallet

Card 2: Your Tickets
- Label: "Your Tickets" (uppercase, gray, small)
- Value: X tickets (large 32px, green)
- Bet Controls (center, flex):
  * [-] button: 40x40px square (disabled when bet = 1)
  * Display: Current bet amount (center box)
  * [+] button: 40x40px square (disabled when bet = max)
- Button: "BET" (full width)
- States:
  * Disabled when tickets < bet amount
  * Disabled during spin
  * Enabled when can bet

VÀ stats cards PHẢI:
- Real-time balance updates
- Ticket count accurate
- Claim requires wallet connection
- Bet amount: 1-5 tickets max or available
```

**Bet Controls Logic:**

```
Min bet: 1 ticket
Max bet: min(5, available_tickets)

[-] button:
- Disabled when bet_amount = 1
- Click: bet_amount -= 1

[+] button:
- Disabled when bet_amount = max
- Click: bet_amount += 1

Center display:
- Shows current bet_amount
- Width: 64px, height: 40px
- Border, centered text
```

**Acceptance Criteria:**

- [ ] Balance displays correctly
- [ ] Tickets count accurate
- [ ] Claim button functional
- [ ] +/- controls work
- [ ] BET button validates state
- [ ] Wallet connection checked

----------

### 4.4. Slot Machine

**FR-RWD-009.4: Game Reels**

**Mô tả:**  
5-reel slot machine với emoji symbols.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Slot Machine:

1. Reels (5 columns)
   - Each reel: 84x84px
   - Border radius: 16px
   - Background: Dark card2
   - Border: 1px solid card-border
   - Gap: 24px between reels
   - Shadow: Inner shadow
   - Centered horizontally

2. Symbols (5 types)
   🌱 Seed (x1 multiplier)
   🌿 Sprout (x2 multiplier)
   🌳 Tree (x3 multiplier)
   🍀 Clover (x4 multiplier)
   🌼 Flower (x5 multiplier)
   
   Display: 54px font size, centered

3. Spin Animation
   - Click BET → Deduct tickets
   - All 5 reels spin simultaneously
   - Vertical scroll animation (loop symbols)
   - Random duration: 1.5-3s per reel
   - Stop order: Left to right (reel 1 → 5)
   - Delay between stops: 200ms
   - Screen freezes: Disable all controls

4. Result Calculation
   After all reels stop:
   - Count each symbol across 5 reels
   - Check winning condition (3+ matching)
   - Calculate payout
   - Update reward balance
   - Show result (visual feedback)

VÀ slot machine PHẢI:
- Smooth spin animation
- Random fair results (server-side)
- Visual feedback clear
- Disable all controls during spin
- Re-enable after complete
```

**Symbol Distribution:**

```
Each reel has equal probability for all 5 symbols
Probability per symbol: 20% (1/5)
```

**Acceptance Criteria:**

- [ ] 5 reels display correctly
- [ ] Spin animation smooth
- [ ] Results random and fair
- [ ] Symbols visible and clear
- [ ] Controls disabled during spin

----------

### 4.5. Game Rules & Payouts

**FR-RWD-009.5: Payout Logic**

**Mô tả:**  
Game rules và payout calculation.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Game Rules:

1. How to Play
   - Press BET to spin all 5 reels
   - The screen will freeze until the spin completes
   - Single payout per spin if you have 3+ of the same symbol
   - Symbols NOT required to be adjacent

2. Winning Conditions
   - 3 of a kind: Win
   - 4 of a kind: Win  
   - 5 of a kind: Jackpot

3. Payout Formula
   
   For 3 or 4 of a kind:
   Reward = 0.001 SOL × symbol multiplier
   
   Examples:
   - 3x 🌱 (x1) = 0.001 SOL × 1 = 0.001 SOL
   - 4x 🌿 (x2) = 0.001 SOL × 2 = 0.002 SOL
   - 3x 🌳 (x3) = 0.001 SOL × 3 = 0.003 SOL
   - 4x 🍀 (x4) = 0.001 SOL × 4 = 0.004 SOL
   - 3x 🌼 (x5) = 0.001 SOL × 5 = 0.005 SOL
   
   For 5 of a kind (Jackpot):
   Reward = 0.01 SOL (fixed, ignores multiplier)
   
   Example:
   - 5x any symbol = 0.01 SOL

4. Claiming Rewards
   - Press CLAIM to collect your SOL
   - Requires connected wallet
   - Transfers to wallet address
   - Balance resets to 0 after claim

VÀ payout PHẢI:
- Accurate calculations
- Fair and transparent
- Instant balance update
- Single payout per spin (highest)
```

**Multipliers Table:**

```
Display as grid (5 columns):

🌱  |  🌿  |  🌳  |  🍀  |  🌼
x1  |  x2  |  x3  |  x4  |  x5
```

**Acceptance Criteria:**

- [ ] Rules clear and complete
- [ ] Payout formula accurate
- [ ] Multipliers table visible
- [ ] Examples helpful
- [ ] Claim process explained

----------

### 4.6. History Table

**FR-RWD-009.6: Spin History**

**Mô tả:**  
Table hiển thị past winning spins.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
History Table:

Columns (4):
1. Time: "HH:MM:SS"
2. Bet: Number of tickets used
3. Result: Winning symbols (emojis only)
4. Payout: X.XXXXXX SOL

Display Rules:
- Shows only WINNING spins
- Last 20 wins maximum
- Sorted: Newest first (top)
- Empty state: "No wins yet. Try your luck!"

Row Examples:
Time     | Bet | Result      | Payout
---------|-----|-------------|-------------
12:00:00 | 1   | 🌱🌱🌱       | 0.001 SOL
12:05:00 | 2   | 🌿🌿🌿🌿     | 0.004 SOL  
12:10:00 | 3   | 🌳🌳🌳       | 0.003 SOL

VÀ history PHẢI:
- Real-time updates (prepend new wins)
- Only winning spins shown
- Accurate timestamps
- Horizontal scroll on mobile
- Max 20 rows displayed
```

**Acceptance Criteria:**

- [ ] Table displays correctly
- [ ] Shows last 20 wins only
- [ ] Timestamps accurate
- [ ] Results match payouts
- [ ] Mobile scrollable
- [ ] Real-time updates work

----------

## 5. ĐIỀU KIỆN CHẤP NHẬN (ACCEPTANCE CRITERIA)

**Overall:**

- [ ] Login required for all actions
- [ ] All sections functional
- [ ] Real-time updates work
- [ ] Responsive on all devices

**Broadcast Banner:**

- [ ] Marquee scrolls continuously
- [ ] Winners update live
- [ ] Pause on hover works
- [ ] No visual glitches

**Stats Cards:**

- [ ] Reward balance accurate
- [ ] Tickets count correct
- [ ] Claim function works
- [ ] Bet controls functional
- [ ] Wallet connection required

**Slot Machine:**

- [ ] 5 reels display properly
- [ ] Spin animation smooth
- [ ] Results fair and random
- [ ] Payout calculated correctly
- [ ] Controls disable during spin

**Rules & Payouts:**

- [ ] Rules clear and complete
- [ ] Multipliers displayed
- [ ] Payout formula accurate

**History:**

- [ ] Table shows winning spins
- [ ] Data accurate and current
- [ ] Real-time updates work
- [ ] Mobile responsive

----------

**END OF FR-009**
