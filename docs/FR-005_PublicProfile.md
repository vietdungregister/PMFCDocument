# FR-005: HỒ SƠ CÔNG KHAI (PUBLIC PROFILE)

## 1. Mô tả

Trang hồ sơ công khai hiển thị thông tin của một user bất kỳ, cho phép xem holdings, created tokens, và limit orders (tất cả read-only).

**User Story:**

```
Là một user,
Tôi muốn xem thông tin công khai của users khác,
Để tìm hiểu về traders/creators và quyết định có follow strategies của họ không.
```

----------

## 2. Giao diện

[To be added]

----------

## 3. ĐIỂM TRUY CẬP (ENTRY POINTS)

Users có thể truy cập Public Profile từ:

1. **Token Detail (FR-002)** - Click creator info hoặc holder name
2. **Community Chat (FR-002)** - Click username trong chat
3. **Holders List (FR-002)** - Click holder name
4. **Transaction History (FR-002)** - Click trader name
5. **Referrals (FR-010)** - Click referred user
6. **Direct URL** - /profile/[username] hoặc /profile/[wallet]

**Default:** Mở tab "Profile Info"

----------

## 4. YÊU CẦU CHỨC NĂNG

### 4.1. Page Layout

**FR-PP-005.1: Cấu trúc Trang**

**Mô tả:**  
Layout trang public profile - entirely read-only.

**Yêu cầu:**

```
Page Structure:

1. Header Section (Read-only)
   - Avatar (large)
   - Username
   - Display name
   - Wallet address (rút gọn)
   - Copy wallet button
   - Badge (nếu có):
     * 👑 Creator (nếu đã tạo token)
     * 🐋 Whale (nếu có holdings lớn)

2. Stats Overview (Below header)
   - Total Portfolio Value (nếu public)
   - Tokens Created: X
   - Total Trades: X
   - Member Since: Date

3. Tabs Navigation (4 tabs)
   - Profile Info
   - Holding Tokens
   - Created Tokens
   - Transaction History
   
   Default: Profile Info tab active

VÀ page PHẢI:
- Entirely read-only
- No login required to view
- Show privacy message nếu user hide data
- Handle private profiles gracefully
```

**Acceptance Criteria:**

- [ ] Header hiển thị đúng user info
- [ ] Badges accurate
- [ ] Stats overview correct
- [ ] 4 tabs accessible (if profile is public)
- [ ] All content read-only
- [ ] Private profile handled correctly

----------

### 4.1.1. Private Profile Handling

**FR-PP-005.1.1: Private Profile Display**

**Mô tả:**  
Xử lý hiển thị khi user đã set profile thành private.

**Yêu cầu:**

```
Private Profile Check:

1. Profile Visibility Check
   
   IF user.hiddenProfile === ON (Hidden):
   → Show Private Profile View (see below)
   → Hide all tabs except Created Tokens
   
   IF user.hiddenProfile === OFF (Public):
   → Show Full Profile View
   → Respect granular privacy settings

2. Private Profile View Layout
   
   A. Header (Still Visible)
      - Avatar (default/placeholder if not set)
      - Username
      - Wallet address (rút gọn)
      - Copy wallet button
      - No badges shown
   
   B. Main Content Area
      - Large lock icon 🔒 (centered)
      - Title: "This profile is private"
      - Subtitle: "This user has chosen to keep their profile private"
      - Spacing: Generous padding, centered layout
   
   C. Created Tokens Section (Always Visible)
      - Separator line
      - Section title: "Created Tokens"
      - Token count: "X tokens created"
      - Token list (same format as Created Tokens tab)
      - If no tokens: "This user hasn't created any tokens yet"

3. What's Hidden When Private
   - Stats overview (Portfolio value, Total trades, etc.)
   - Profile Info tab
   - Holdings tab
   - Transaction History tab
   - All badges (Creator, Whale)

4. What's Always Visible (Even When Private)
   - Username
   - Wallet address
   - Created tokens list (transparency requirement)

VÀ private profile PHẢI:
- Clear privacy message with lock icon
- Respect user's privacy choice completely
- Still show created tokens (cannot hide)
- Clean, centered layout for privacy message
- No access to any personal data
```

**Acceptance Criteria:**

- [ ] Private profile shows lock icon and message
- [ ] All tabs hidden except created tokens
- [ ] Created tokens always visible
- [ ] Stats overview hidden when private
- [ ] Clear, user-friendly privacy message
- [ ] Wallet address still copyable

----------

### 4.2. Profile Info Tab

**FR-PP-005.2: Thông tin Cá nhân**

**Mô tả:**  
Hiển thị metadata của user (read-only).

**Yêu cầu:**

```
Profile Info Display:

1. Basic Info
   - Username
   - Display Name
   - Bio
   - Member Since: Date

2. Social Links (nếu có)
   - Twitter/X (clickable)
   - Telegram (clickable)
   - Email (hiển thị hoặc "Hidden")
   - Website (nếu có)

3. Wallet Info
   - Wallet Address (full, với copy button)
   - Total Transactions: X

4. Activity Stats
   - Tokens Held: X
   - Tokens Created: X

VÀ profile info PHẢI:
- Read-only (không có edit button)
- Social links open in new tab
- Privacy-aware (hide sensitive data if user set)
```

**Acceptance Criteria:**

- [ ] All info displayed correctly
- [ ] Social links work
- [ ] Copy wallet works
- [ ] Stats accurate
- [ ] Privacy settings respected

----------

### 4.3. Holding Tokens Tab

**FR-PP-005.3: Token đang Nắm giữ**

**Mô tả:**  
Hiển thị tokens mà user này đang nắm giữ (read-only).

**Yêu cầu:**

```
Holding Tokens List (Read-only):

1. Privacy Control
   IF user set holdings private:
   - Show: "🔒 Holdings are private"
   - No token list visible
   
   IF user set holdings public:
   - Show token list

2. Token List
   Mỗi token hiển thị:
   - Avatar
   - Name + Symbol
   - Balance (số lượng)
   - Value (USD) - nếu public
   - Current Price

3. Sorting
   - By Value (default)
   - By Balance

4. Click Behavior
   - Click token → Token Detail (FR-002)

Note:
- This tab is HIDDEN if profile visibility is PRIVATE
- This tab shows privacy message if holdings visibility is OFF
- NO P&L (private info)
- NO portfolio stats (private)
- Chỉ show holdings, không show cost basis

VÀ holdings PHẢI:
- Respect privacy settings
- Real-time prices
- Read-only
```

**Acceptance Criteria:**

- [ ] Privacy message if private
- [ ] Token list if public
- [ ] Balance accurate
- [ ] Sorting works
- [ ] Click navigates correctly

----------

### 4.4. Created Tokens Tab

**FR-PP-005.4: Token đã Tạo**

**Mô tả:**  
Hiển thị tokens mà user này đã tạo (always public).

**Yêu cầu:**

```
Created Tokens List (Always Public):

1. Token Cards
   Mỗi token hiển thị:
   - Avatar
   - Name + Symbol
   - Created date
   - Status: Active / Graduated
   - Current Market Cap
   - Current Price
   - Total Volume
   - Holders count

2. Sorting
   - By Created Date (newest) - Default
   - By Market Cap
   - By Volume

3. Empty State
   - "This user hasn't created any tokens yet"

4. Click Behavior
   - Click token → Token Detail (FR-002)

VÀ created tokens PHẢI:
- Always public (cannot hide)
- Real-time metrics
```

**Acceptance Criteria:**

- [ ] List shows all created tokens
- [ ] Metrics accurate
- [ ] Sorting works
- [ ] Empty state helpful
- [ ] Click navigates correctly

----------

### 4.5. Transaction History Tab

**FR-PP-005.5: Lịch sử Giao dịch**

**Mô tả:**  
Hiển thị lịch sử giao dịch BUY/SELL của user này (read-only).

**Yêu cầu:**

```
Transaction History List (Read-only):

1. Privacy Control
   IF user set transactions private:
   - Show: "🔒 Transaction history is private"
   
   IF user set transactions public:
   - Show transaction list

2. Transaction Items
   Mỗi transaction hiển thị:
   
   - Type Badge:
     * BUY (green)
     * SELL (red)
   
   - Token Info:
     * Avatar
     * Name
   
   - Timestamp:
     * Relative time: "2h ago", "1 day ago"
   
   - Transaction Details:
     * Amount: +10,000 PSEED (BUY) hoặc -10,000 PSEED (SELL)
     * Value: 0.5 SOL
     * TX Hash (rút gọn): 7xK9...mP3q

3. TX Hash Link
   - Click → Solana Explorer (new tab)

4. Sorting
   - Newest first (default)

5. Empty State
   - "No transactions yet"

6. Click Behavior
   - Click TX hash → Solana Explorer
   - Click token → Token Detail (FR-002)

Note:
- This tab is HIDDEN if profile visibility is PRIVATE
- This tab shows privacy message if transaction visibility is OFF

VÀ transaction history PHẢI:
- Read-only view only
- Respect privacy settings
- Show up to 50 recent transactions
```

**Acceptance Criteria:**

- [ ] Privacy respected
- [ ] Transaction list if public
- [ ] Type badges correct
- [ ] TX hash links work
- [ ] Timestamps accurate
- [ ] Click token navigates correctly

----------

## 5. ĐIỀU KIỆN CHẤP NHẬN (ACCEPTANCE CRITERIA)

**Overall:**

- [ ] Entirely read-only
- [ ] No login required to view
- [ ] All tabs functional
- [ ] Privacy settings respected
- [ ] Responsive layout

**Privacy:**

- [ ] Holdings privacy works
- [ ] Transactions privacy works
- [ ] Profile info respects settings
- [ ] Clear privacy messages

**Navigation:**

- [ ] All clicks work
- [ ] External links open new tab
- [ ] Token navigation correct

----------

**END OF FR-005**
