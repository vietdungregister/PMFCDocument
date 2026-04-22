# FR-009: ĐIỂM THƯỞNG (POINTS/REWARDS)

## 1. Mô tả

Hệ thống điểm thưởng khuyến khích users trade và tham gia activities, tiến bộ qua các ranks.

**User Story:**

```
Là một user,
Tôi muốn kiếm điểm và tiến bộ qua các ranks,
Để nhận rewards và unlock benefits.
```

----------

## 2. Giao diện

[To be added]

----------

## 3. ĐIỂM TRUY CẬP (ENTRY POINTS)

Users có thể truy cập Points từ:

1. **Main Navigation** - Sidebar menu "Rewards"
2. **Direct URL** - /points hoặc /rewards

**Default:** Hiển thị current rank và history

----------

## 4. YÊU CẦU CHỨC NĂNG

### 4.1. Page Layout

**FR-PTS-009.1: Cấu trúc Trang**

**Mô tả:**  
Layout với header, rank card, và history table.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Page Structure:

1. Header (2 columns)
   Left:
   - Title: "Points"
   - Subtitle: "Get points for doing stuff : trade, create, stake have fun!"
   
   Right:
   - Label: "Points"
   - Value: XXX / XXX (current / next level)

2. Rank Card
   - Current rank display
   - Progress bar
   - Next rank info

3. History Section
   - Empty state or table
   - Points earning history

VÀ points page PHẢI:
- Login required
- Real-time updates
- Responsive layout
```

**Acceptance Criteria:**

- [ ] Header displays correctly
- [ ] Points value accurate
- [ ] Rank card shows current level
- [ ] Layout responsive

----------

### 4.2. Rank System

**FR-PTS-009.2: Rank Display**

**Mô tả:**  
Hiển thị current rank và progress.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Rank Card:

1. Rank Info
   - Emoji icon: 🌱✨ (Seed)
   - Name: "Seed"
   - Subtitle: "Progress through the ranks"

2. Progress Bar
   - Height: 8px, rounded
   - Background: Dark
   - Fill: Primary green
   - Width: Percentage (current / next level)

3. Progress Text
   - Format: "X.XX SOL away from [Next Rank]"
   - Calculate remaining volume needed

VÀ rank card PHẢI:
- Update progress real-time
- Show accurate calculations
- Smooth progress animation
```

**Rank Levels:**

```
Ranks (5 tiers):

Tier 1: 🌱 Seed
- Points: 0
- Reward: –

Tier 2: 🌿 Sprout
- Points: 500 pts
- Reward: 🎁 1 Ticket + 0.005 SOL

Tier 3: 🌳 Sapling
- Points: 2,000 pts
- Reward: 🎁 3 Tickets + 0.02 SOL

Tier 4: 🌲 Tree
- Points: 10,000 pts
- Reward: 🎁 5 Tickets + 0.05 SOL

Tier 5: 🪷 Ancient Tree
- Points: 50,000 pts
- Reward: 🎁 10 Tickets + 0.2 SOL

Points Calculation:

(A) Referral Points (strongest)
- Formula: NetVolume × 10
- NetVolume = Total BUY - Total SELL
- Examples:
  * 0.1 SOL → 1 point
  * 1 SOL → 10 points
  * 10 SOL → 100 points
- Rules:
  * Only count BUY ≥ 0.01 SOL
  * Do NOT count SELL
  * Only when token is ACTIVE

(B) Trade Points
- Formula: Volume × 5
- Example: 1 SOL trade → 5 points
- Rules:
  * Only count BUY ≥ 0.01 SOL
  * Do NOT count SELL

(C) Token Creation Points
- Create token: 20 pts
- Upload image + full description: 10 pts
- Token Trust Score: 20 pts
- Token reaches 10 first buys: 30 pts
- Rules:
  * Only count when token is ACTIVE
  * ACTIVE = has 2nd buyer ≠ creator
  * 2nd buyer must BUY ≥ 0.05 SOL

Anti-Farm Mechanism:
- Referral: NetVolume (Buy - Sell) blocks wash trading
- Trade: Only BUY ≥ 0.01 SOL, no SELL
- Token Creation: Only when ACTIVE (2nd buyer verified)

Season System:
- Season duration: 3 weeks
- After season: Reset accounts without enough points
- Points accumulate to next season
- SOL rewards: From Marketing Pool
```

**Acceptance Criteria:**

- [ ] Rank displays correctly
- [ ] Progress bar accurate
- [ ] Remaining volume calculated
- [ ] Next rank shown
- [ ] Smooth animations

----------

### 4.3. Points History

**FR-PTS-009.3: Lịch sử Điểm**

**Mô tả:**  
Hiển thị history kiếm điểm.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
History Table:

1. Empty State
   - Title: "NOTHING HERE" (uppercase, bold)
   - Subtitle: "Nothing yet? Switch wallets or trade to earn Seed Points."
   - Empty table with headers
   - Message: "You'll see your point history here"

2. Table Headers (3 columns)
   - DATE (min-width: 140px)
   - TRADING VOLUME (min-width: 200px)
   - POINTS EARNED (min-width: 160px)

3. Data Rows (when has data)
   Each row shows:
   - Date: "Jan 15, 2025"
   - Volume: "2.5 SOL"
   - Points: "+125 points" (green color)

4. Row Behavior
   - Hover: Background highlight
   - Sorted: Newest first

5. Responsive
   - Horizontal scroll on mobile
   - Maintain min-widths

VÀ history PHẢI:
- Show all point-earning activities
- Real-time updates
- Accurate calculations
- Smooth scrolling
```

**Points Earning Activities:**

```
Activities that earn points:

1. Referral (strongest earning)
   - NetVolume × 10
   - NetVolume = Referred user's (Total BUY - Total SELL)
   - Only BUY ≥ 0.01 SOL
   - Only when token ACTIVE

2. Trading
   - Volume × 5
   - Only BUY ≥ 0.01 SOL
   - SELL does not earn points

3. Creating Tokens
   - Create token: 20 pts
   - Upload image + description: 10 pts
   - Token Trust Score: 20 pts
   - Token reaches 10 buys: 30 pts
   - Total possible: 80 pts per token
   - Only count when token ACTIVE
```

**Acceptance Criteria:**

- [ ] Empty state displays correctly
- [ ] Table headers visible
- [ ] Data rows show when available
- [ ] Points calculation accurate
- [ ] Sorting works (newest first)
- [ ] Hover effects smooth
- [ ] Mobile scrollable

----------

## 5. ĐIỀU KIỆN CHẤP NHẬN (ACCEPTANCE CRITERIA)

**Overall:**

- [ ] Login required
- [ ] Points accurate
- [ ] Real-time updates
- [ ] Responsive layout

**Rank System:**

- [ ] Current rank correct
- [ ] Progress bar accurate
- [ ] Next rank displayed
- [ ] Volume calculation correct

**History:**

- [ ] Empty state helpful
- [ ] Table displays correctly
- [ ] All activities logged
- [ ] Points calculation accurate

----------

**END OF FR-009**
