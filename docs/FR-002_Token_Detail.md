# FR-002: CHI TIẾT TOKEN

## 1. Mô tả

Trang chi tiết token hiển thị đầy đủ thông tin về một token cụ thể bao gồm chart giá, metrics, trust level, community chat, danh sách holders, lịch sử giao dịch, và trading panel.

**User Story:**

```
Là một trader,
Tôi muốn xem chi tiết đầy đủ về một token,
Để đánh giá và quyết định có nên mua/bán token này không.
```

----------

## 2. ĐIỂM TRUY CẬP (ENTRY POINTS)

Users có thể truy cập Token Detail từ:

1. **Token List (FR-001)** - Click vào token card
2. **Search Results** - Click vào kết quả tìm kiếm
3. **My Profile (FR-004)** - Holdings/Created/Staking tabs
4. **Public Profile (FR-005)** - Holdings/Created tabs
5. **Leaderboard (FR-008)** - Click vào token trong bảng xếp hạng
6. **Direct URL** - /token/[address]

**Default:** Tất cả sections được load khi vào trang

----------

## 3. YÊU CẦU CHỨC NĂNG

### 3.1. Header Token

**FR-TD-002.1: Thông tin Token Header**

**Mô tả:**  
Hiển thị thông tin cơ bản của token ở đầu trang.

**Yêu cầu:**

```
Header hiển thị:

1. Avatar Token
   - Ảnh đại diện token
   - Fallback: Default avatar nếu không có

2. Tên Token + Symbol
   - Format: "Token Name ($SYMBOL)"
   - Typography: Large, prominent

3. Creator Info
   - Avatar creator (nhỏ)
   - Username hoặc wallet address (rút gọn)
   - Click → Navigate to Public Profile (FR-005)
   - Label: "Created by"

4. Contract Address
   - Display: Rút gọn (0x1234...5678)
   - Copy button
   - Click copy → Toast "Copied!"

5. Favorite Button
   - Icon: ♡ (chưa favorite) / ♥ (đã favorite)
   - Click toggle → Update state
   - Login required
   - Sync với danh sách Favorite

6. Social Links (nếu có)
   - Website, Twitter, Telegram, Discord
   - Icon buttons
   - Click → Open in new tab

VÀ header PHẢI:
- Sticky on scroll (optional)
- Responsive layout
```

**Acceptance Criteria:**

- [ ] Header hiển thị đầy đủ thông tin
- [ ] Creator link navigate đúng
- [ ] Copy contract address hoạt động
- [ ] Favorite toggle sync đúng
- [ ] Social links mở đúng

----------

### 3.2. Biểu đồ Giá

**FR-TD-002.2: Price Chart**

**Mô tả:**  
Hiển thị biểu đồ giá token với các timeframe khác nhau.

**Yêu cầu:**

```
Chart hiển thị:

1. Chart Types
   - Candlestick (default)
   - Line chart
   - Toggle để switch

2. Timeframes
   - Options: 5m / 15m / 1h / 4h / 1d / 1w
   - Default: 1d
   - Click để switch timeframe

3. Data Display
   - OHLC (Open, High, Low, Close)
   - Volume bars dưới chart
   - Current price highlight
   - Tooltip khi hover

4. Interactions
   - Zoom in/out
   - Pan (drag to move)
   - Crosshair cursor
   - Real-time updates

VÀ chart PHẢI:
- Load nhanh (<1s)
- Smooth interactions
- Real-time updates (10s - 2min tùy timeframe)
```

**Library gợi ý:** TradingView Lightweight Charts hoặc Recharts

**Acceptance Criteria:**

- [ ] Chart hiển thị chính xác
- [ ] Timeframe switch hoạt động
- [ ] Interactions mượt
- [ ] Real-time updates đúng

----------

### 3.3. Market Metrics

**FR-TD-002.3: Chỉ số Thị trường**

**Mô tả:**  
Hiển thị các chỉ số quan trọng của token.

**Yêu cầu:**

```
Metrics hiển thị:

1. Price (USD)
   - Current price
   - Update: Real-time (10s)
   - Pulse animation khi thay đổi

2. 24h Price Change
   - Format: ±X.XX%
   - Màu: Green (dương) / Red (âm) / Gray (0)
   - Icon: ↑ / ↓

3. Market Cap (USD)
   - Format: Rút gọn K/M/B
   - Update: 30s

4. 24h Volume (USD)
   - Format: Rút gọn K/M/B
   - Update: 1 phút

5. Total Holders
   - Số lượng holders
   - Update: 5 phút
   - Trend indicator: ↑ tăng / ↓ giảm / → không đổi

6. Liquidity (SOL)
   - Số SOL trong bonding curve
   - Progress bar đến graduation ($69K MC)

7. Total Supply
   - Fixed supply
   - Static (không update)

VÀ metrics PHẢI:
- Grid layout: 2 cột (desktop)
- Real-time updates theo frequency
- Animation khi số thay đổi
```

**Acceptance Criteria:**

- [ ] 7 metrics hiển thị đúng
- [ ] Format K/M/B chính xác
- [ ] Update frequencies đúng
- [ ] Colors và icons đúng
- [ ] Progress bar graduation chính xác

----------

### 3.4. Trust Level

**FR-TD-002.4: Mức độ Tin cậy**

**Mô tả:**  
Hiển thị overall trust score và các badges bảo mật.

**Yêu cầu:**

```
Trust Level hiển thị:

1. Overall TrustScore
   - Score: 0-100
   - Visual: Progress bar hoặc score badge
   - Color coding:
     * 0-49: Low (Red)
     * 50-79: Medium (Yellow)
     * 80-100: High (Green)

2. Trust Badges
   Hiển thị badges nếu đạt tiêu chí:
   
   A. LP Locked 🔒
      - % LP locked
      - Lock duration
      - Unlock date
   
   B. Audited ✓
      - Audit firm name
      - Audit date
      - Link to audit report
   
   C. Freeze Authority Disabled 🛡️
      - Confirmation status

3. Badge Details
   - Click badge → Modal với chi tiết
   - Tooltip on hover

VÀ trust display PHẢI:
- Clear visual hierarchy
- Badges prominent nếu có
- Overall score dễ hiểu
```

**TrustScore Formula:**

```
TrustScore = 
  0.40 × LP_Lock_Score +
  0.40 × Audit_Score +
  0.20 × Freeze_Authority_Score

LP_Lock_Score:
  - 100% locked > 30 days = 100 points
  - 50-99% locked = 50 points
  - < 50% locked = 0 points

Audit_Score:
  - Audited by reputable firm = 100 points
  - Self-audited = 50 points
  - No audit = 0 points

Freeze_Authority_Score:
  - Disabled = 100 points
  - Enabled = 0 points
```

**Acceptance Criteria:**

- [ ] TrustScore tính đúng
- [ ] Badges hiển thị chính xác
- [ ] Color coding đúng
- [ ] Modal details hoạt động
- [ ] Tooltips clear

----------

### 3.5. Community Chat

**FR-TD-002.5: Chat Room**

**Mô tả:**  
Chat room real-time để users thảo luận về token.

**Yêu cầu:**

```
Chat Room bao gồm:

1. Message List
   - Hiển thị 50 messages gần nhất
   - Auto-scroll to bottom khi có message mới
   - Infinite scroll up để load history
   - Format message:
     * Avatar user (nhỏ)
     * Username (click → Public Profile)
     * Message content
     * Timestamp (relative: "2m ago")

2. Send Message
   - Input field dưới cùng
   - Max length: 200 characters
   - Login required
   - Rate limiting: 5 messages/phút
   - Enter to send

3. Features
   - Profanity filter (auto-enabled)
   - Click username → Public Profile (FR-005)
   - Online user count
   - Message reactions (optional - future)

4. Real-time Updates
   - WebSocket connection
   - New messages appear instantly
   - "User is typing..." indicator (optional)

VÀ chat PHẢI:
- Real-time (<500ms latency)
- Handle high traffic
- Profanity filter active
- Rate limiting enforced
```

**WebSocket Events:**

```
Client → Server:
- CONNECT
- SEND_MESSAGE
- DISCONNECT

Server → Client:
- MESSAGE_RECEIVED
- USER_JOINED
- USER_LEFT
- ONLINE_COUNT
```

**Acceptance Criteria:**

- [ ] Chat real-time hoạt động
- [ ] Messages hiển thị đúng format
- [ ] Rate limiting work
- [ ] Profanity filter active
- [ ] Navigate to profile work
- [ ] Online count accurate

----------

### 3.6. Holders List

**FR-TD-002.6: Danh sách Holders**

**Mô tả:**  
Hiển thị top holders của token với thông tin chi tiết.

**Yêu cầu:**

```
Holders List hiển thị:

1. Summary Stats
   - Total holders
   - Top 10 concentration % (risk indicator)
   - Average holding
   - New holders (24h)

2. Top 100 Holders Table
   Columns:
   - Rank
   - Avatar + Username/Address
   - Balance (số lượng tokens)
   - % of supply
   - Badges:
     * 👑 Creator
     * 🐋 Whale (>5% supply)
     * 💎 Diamond Hands (hold >30 days)

3. Features
   - Pagination: 20 holders/page
   - Click holder → Public Profile (FR-005)
   - Search by address
   - Filter: All / Top 10 / Top 50 / Whales only

4. Updates
   - Refresh every 5 minutes
   - Show loading state khi update

VÀ holders list PHẢI:
- Top 100 only (performance)
- Exclude dead wallets (0x000...000)
- Badge logic chính xác
```

**Top 10 Concentration Risk:**

```
Concentration % → Risk Level
< 40%           → Low (Green)
40-60%          → Medium (Yellow)
> 60%           → High (Red)
```

**Acceptance Criteria:**

- [ ] Summary stats chính xác
- [ ] Top 100 hiển thị đúng
- [ ] % of supply tính đúng
- [ ] Badges hiển thị đúng
- [ ] Click navigate đúng
- [ ] Filters hoạt động
- [ ] Updates mỗi 5 phút

----------

### 3.7. Transaction History

**FR-TD-002.7: Lịch sử Giao dịch**

**Mô tả:**  
Hiển thị 50 transactions gần nhất của token.

**Yêu cầu:**

```
Transaction History hiển thị:

1. Transaction List (50 gần nhất)
   Columns:
   - Type: BUY (green) / SELL (red)
   - Timestamp (relative: "5m ago")
   - Trader:
     * Username (nếu có)
     * Address rút gọn (nếu không có username)
     * Click → Public Profile (FR-005)
   - Amount (số tokens)
   - Price ($/token tại thời điểm đó)
   - Total Value (USD)
   - TX Hash:
     * Rút gọn
     * Click → Solana Explorer (new tab)

2. Filters
   - Type: All / Buys / Sells
   - Time: 1h / 24h / 7d / All

3. Highlights
   - Whale transactions (>5% of 24h volume):
     * 🐋 icon
     * Yellow background highlight
   - First trade ever:
     * ⭐ icon

4. Updates
   - Real-time: WebSocket hoặc polling (10s)
   - New transaction appear at top
   - Smooth animation khi insert

VÀ transaction history PHẢI:
- Real-time updates
- Clickable links work
- Filter logic đúng
- Performance tốt (50 rows)
```

**Acceptance Criteria:**

- [ ] 50 transactions load đúng
- [ ] Type colors đúng
- [ ] Trader links navigate đúng
- [ ] TX hash links đúng explorer
- [ ] Filters hoạt động
- [ ] Real-time updates work
- [ ] Whale highlights đúng

----------

### 3.8. Trading Panel

**FR-TD-002.8: Panel Giao dịch**

**Mô tả:**  
Trading panel hiển thị cố định bên phải để user có thể buy/sell ngay.

**Yêu cầu:**

```
Trading Panel:
- Position: Fixed bên phải màn hình
- Luôn visible khi scroll
- Chi tiết xem FR-003: Chức năng Buy/Sell

Buttons:
- BUY button: Enabled luôn (login + wallet required)
- SELL button: Enabled khi user có balance > 0

VÀ trading panel PHẢI:
- Sync với token hiện tại
- Display current price real-time
- Risk warnings nếu có (Yellow/Red risk)
```

**Acceptance Criteria:**

- [ ] Panel hiển thị cố định bên phải
- [ ] BUY/SELL buttons state đúng
- [ ] Navigate đến trading flow (FR-003)
- [ ] Token context đúng
- [ ] Risk warnings hiển thị

----------

## 4. ĐIỀU KIỆN CHẤP NHẬN (ACCEPTANCE CRITERIA)

**Overall Page:**

- [ ] Page load < 2s
- [ ] All sections hiển thị đúng
- [ ] Real-time updates hoạt động
- [ ] Navigation links đúng
- [ ] Responsive layout
- [ ] Error states handled
- [ ] Loading states clear

**Data Accuracy:**

- [ ] Price và metrics chính xác
- [ ] Chart data đúng
- [ ] Holders list accurate
- [ ] Transaction history complete
- [ ] TrustScore tính đúng

**Interactions:**

- [ ] Favorite toggle work
- [ ] Copy address work
- [ ] Social links open correct
- [ ] Chat real-time
- [ ] Filters hoạt động
- [ ] All navigation links work

----------

**END OF FR-002**
