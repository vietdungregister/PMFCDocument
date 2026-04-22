# FR-006: BẢNG ĐIỀU KHIỂN CREATOR (CREATOR DASHBOARD)

## 1. Mô tả

Bảng điều khiển cho creators quản lý tokens đã tạo, theo dõi revenue, và tương tác với community. Có 2 levels: Dashboard (quản lý tổng quan) và Token Management (quản lý chi tiết từng token).

**User Story:**

```
Là một creator,
Tôi muốn quản lý các tokens đã tạo và thu revenue,
Để theo dõi performance và tương tác với community.
```

----------

## 2. Giao diện

[To be added]

----------

## 3. ĐIỂM TRUY CẬP (ENTRY POINTS)

Users có thể truy cập Creator Dashboard từ:

1. **Main Navigation** - Sidebar menu "Creator Dashboard"
2. **My Profile** - Created Tokens tab (nếu có tokens)
3. **Direct URL** - /creator/dashboard

**Default:** Mở Level 1 - Created Tokens tab

----------

## 4. YÊU CẦU CHỨC NĂNG

### 4.1. LEVEL 1 - Creator Dashboard

**FR-CD-006.1: Dashboard Overview**

**Mô tả:**  
Trang tổng quan quản lý tất cả tokens đã tạo và revenue.

**Yêu cầu:**

```
Page Structure:

1. Header
   - Title: "Creator Dashboard"

2. Tabs Navigation (2 tabs)
   - Created Tokens
   - Creator Revenue
   
   Default: Created Tokens tab active

VÀ dashboard PHẢI:
- Login required
- Chỉ show cho users đã tạo ít nhất 1 token
```

**Acceptance Criteria:**

- [ ] Header hiển thị đúng
- [ ] 2 tabs functional
- [ ] Default tab correct
- [ ] Access control works

----------

### 4.2. Created Tokens Tab

**FR-CD-006.2: Danh sách Tokens**

**Mô tả:**  
Hiển thị tất cả tokens creator đã tạo với "Manage Token" button.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Token List:

1. Token Items
   Mỗi token hiển thị:
   - Avatar
   - Name + Symbol
   - Created date
   - Status badge: Active / Graduated
   - "Manage Token" button

2. Status Badges
   - Active (green): Token đang trong bonding curve
   - Graduated (yellow): Đã đạt $69K MC

3. Click Behavior
   - Click "Manage Token" → Navigate to Level 2 (Token Management)
   - Click token info → Token Detail (FR-002)

4. Empty State
   - "You haven't created any tokens yet"
   - "Create Token" button → FR-007

VÀ token list PHẢI:
- Show all tokens user created
- Sorted by created date (newest first)
- Real-time status updates
```

**Acceptance Criteria:**

- [ ] List shows all created tokens
- [ ] Status badges accurate
- [ ] Manage Token button navigates to Level 2
- [ ] Empty state helpful

----------

### 4.3. Creator Revenue Tab

**FR-CD-006.3: Quản lý Revenue**

**Mô tả:**  
Hiển thị tổng revenue và cho phép claim earnings.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Revenue Overview:

1. Stats Cards (3)
   - Total Revenue: X SOL (≈ $XXX)
   - Unclaimed Revenue: X SOL (≈ $XXX) - Green
   - Total Claimed: X SOL (≈ $XXX)

2. Claim Section
   - Title: "Claim Your Revenue"
   - Description: "Withdraw your unclaimed earnings to your wallet"
   - Button: "Claim X.X SOL"
   - Requires: Connected wallet
   - Action: Transfer unclaimed revenue to wallet

3. Revenue Breakdown
   - Title: "Revenue by Token"
   - List tokens với revenue per token:
     * Token name + symbol
     * Revenue amount: X SOL (≈ $XXX)
   - Sorted by revenue (highest first)

4. Empty State
   - "No revenue yet"
   - "Start trading to earn creator fees"

VÀ revenue PHẢI:
- Real-time updates
- Accurate calculations
- Wallet connection required for claim
```

**Revenue Sources:**

```
Creator earns from:
- 1% bonding curve fee on all trades
- Distributed to creator wallet

Calculation:
- Track per token
- Aggregate across all tokens
- Update on each trade
```

**Acceptance Criteria:**

- [ ] Stats accurate
- [ ] Claim button works
- [ ] Wallet connection required
- [ ] Revenue breakdown correct
- [ ] Empty state helpful

----------

### 4.4. LEVEL 2 - Token Management

**FR-CD-006.4: Token Detail Management**

**Mô tả:**  
Quản lý chi tiết một token cụ thể với 3 tabs.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Page Structure:

1. Breadcrumb Navigation
   - "Creator Dashboard › [Token Name]"
   - Clickable link back to Dashboard

2. Back Button
   - "← Back to Dashboard"
   - Returns to Level 1

3. Token Header
   - Avatar (large)
   - Name + Symbol
   - Description
   - Status badge

4. Tabs Navigation (3 tabs)
   - Overview
   - Trusted Level
   - Community Management
   
   Default: Overview tab active

VÀ token management PHẢI:
- Clear navigation back to Dashboard
- Show current token context
- All changes save immediately
```

**Acceptance Criteria:**

- [ ] Breadcrumb navigation works
- [ ] Back button returns to Dashboard
- [ ] Token header accurate
- [ ] 3 tabs functional

----------

### 4.5. Overview Tab

**FR-CD-006.5: Token Metrics Overview**

**Mô tả:**  
Hiển thị metrics và thông tin chi tiết của token.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Overview Content:

1. Metrics Grid (6 cards)
   - Market Cap: $XX.XK
   - Price: $X.XXXXX
   - 24h Volume: $XX.XK
   - Holders: XXX
   - Total Supply: XXX
   - Liquidity (SOL): X.X SOL

2. Chart (Future)
   - Placeholder: "📈 Price Chart"
   - "Chart visualization will be displayed here"

3. Token Information Section
   - Token Name (read-only)
   - Symbol (read-only)
   - Description (read-only)
   - Status (read-only)

VÀ overview PHẢI:
- Real-time metrics updates
- Read-only information
- Clear data presentation
```

**Acceptance Criteria:**

- [ ] Metrics accurate
- [ ] Real-time updates work
- [ ] Chart placeholder visible
- [ ] Token info correct

----------

### 4.6. Trusted Level Tab

**FR-CD-006.6: Security Settings**

**Mô tả:**  
Quản lý các security features để tăng trust score.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Security Settings:

1. LP Lock
   - Toggle switch
   - Description: "Lock liquidity pool to prevent rug pulls"
   - Default: OFF
   - Action: Enable/disable LP lock

2. Audit Token
   - Button: "Request Audit"
   - Description: "Get your token audited by verified auditors"
   - Action: Submit audit request
   - Status: Not Audited / Pending / Audited

3. Freeze Authority
   - Toggle switch
   - Description: "Disable freeze authority to increase trust"
   - Default: ON (enabled)
   - Action: Disable freeze authority (permanent)

4. Info Box
   - "ℹ️ Trust Score Impact"
   - Explanation: "Enabling these security features will increase your token's trust score and make it more attractive to traders."

VÀ security settings PHẢI:
- Toggle changes save immediately
- Freeze Authority disable is permanent
- Show confirmation for irreversible actions
- Update trust score accordingly
```

**Trust Score Impact:**

```
LP Lock ON: +20 points
Audit Completed: +30 points
Freeze Disabled: +25 points

Total possible: +75 points
```

**Acceptance Criteria:**

- [ ] Toggles work correctly
- [ ] Audit request submits
- [ ] Freeze Authority confirmation shown
- [ ] Trust score updates
- [ ] Info box clear

----------

### 4.7. Community Management Tab

**FR-CD-006.7: Quản lý Posts**

**Mô tả:**  
Tạo và quản lý community posts.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Community Posts:

1. Create Post Button
   - "+ Create New Post"
   - Opens create post modal

2. Create Post Modal
   - Title field (required, max 100 chars)
   - Content field (required, max 500 chars)
   - "Create" / "Cancel" buttons

3. Posts List
   Mỗi post hiển thị:
   - Title
   - Meta: "Posted X ago" + Pin status
   - Content preview
   - Actions:
     * Pin/Unpin button
     * Edit button
     * Delete button

4. Post Actions
   
   Pin/Unpin:
   - Max 1 pinned post at a time
   - Pinned post shows "📌 Pinned"
   - Pinned post appears first in list
   
   Edit:
   - Opens edit modal
   - Same fields as create
   - Save changes
   
   Delete:
   - Confirmation modal
   - "Are you sure?"
   - Permanent action

5. Empty State
   - "No posts yet"
   - "Create your first post to engage with your community"

VÀ community management PHẢI:
- Posts visible in Token Detail (FR-002)
- Real-time updates
- Clear action buttons
```

**Acceptance Criteria:**

- [ ] Create post works
- [ ] Post list displays correctly
- [ ] Pin/Unpin works (max 1 pinned)
- [ ] Edit saves changes
- [ ] Delete confirmation shown
- [ ] Empty state helpful

----------

## 5. ĐIỀU KIỆN CHẤP NHẬN (ACCEPTANCE CRITERIA)

**Overall:**

- [ ] 2-level navigation works
- [ ] All tabs functional
- [ ] Login required
- [ ] Only accessible by token creators

**Level 1 - Dashboard:**

- [ ] Token list complete
- [ ] Revenue stats accurate
- [ ] Claim function works

**Level 2 - Token Management:**

- [ ] Navigation clear
- [ ] Metrics real-time
- [ ] Security settings work
- [ ] Community posts functional

----------

**END OF FR-006**
