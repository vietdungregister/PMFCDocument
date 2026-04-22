# FR-004: HỒ SƠ CỦA TÔI (MY PROFILE)

## 1. Mô tả

Trang hồ sơ cá nhân cho phép user xem các token đang nắm giữ, token đã tạo, token đang stake, chỉnh sửa thông tin cá nhân, và quản lý các limit orders đang hoạt động.

**User Story:**

```
Là một user,
Tôi muốn xem và quản lý hồ sơ cá nhân của mình,
Để theo dõi portfolio, chỉnh sửa thông tin, và quản lý các lệnh đang chờ.
```

----------

## 2. Giao diện

[To be added]

----------

## 3. ĐIỂM TRUY CẬP (ENTRY POINTS)

Users có thể truy cập My Profile từ:

1. **Main Navigation** - Click avatar/username hoặc "My Profile" menu
2. **Direct URL** - /profile hoặc /me

**Default:** Mở tab "Holding Tokens"

----------

## 4. YÊU CẦU CHỨC NĂNG

### 4.1. Page Layout

**FR-MP-004.1: Cấu trúc Trang**

**Mô tả:**  
Layout trang profile với tabs navigation.

**Yêu cầu:**

```
Page Structure:

1. Header Section
   - Avatar (large)
   - Username
   - Display name (nếu có)
   - Wallet address (rút gọn)
   - Copy wallet button

2. Tabs Navigation (5 tabs)
   - Holding Tokens
   - Created Tokens
   - Transaction History
   - Edit Profile
   - Limit Orders
   
   Default: Holding Tokens tab active

VÀ page PHẢI:
- Login required (redirect if not)
```

**Acceptance Criteria:**

- [ ] Header hiển thị đúng thông tin user
- [ ] 5 tabs hiển thị đầy đủ
- [ ] Tab switching mượt
- [ ] Default tab là Holding Tokens

----------

### 4.2. Holding Tokens Tab

**FR-MP-004.2: Danh sách Token đang Nắm giữ**

**Mô tả:**  
Hiển thị tất cả tokens mà user đang nắm giữ (balance > 0).

**Yêu cầu:**

```
Holding Tokens List:

1. Portfolio Stats (Top)
   - Total Value: $XXX,XXX
   - 24h Change: ±X.XX%
   - Total P&L: +$XXX (+X.X%)

2. Token List
   Mỗi token hiển thị:
   - Avatar
   - Name + Symbol
   - Balance (số lượng)
   - Value (USD)
   - Current Price
   - 24h Change (%)
   - P&L (Profit/Loss):
     * Amount: +$XXX hoặc -$XXX
     * %: +X.X% hoặc -X.X%
     * Color: Green/Red/Gray

3. Sorting Options
   - By Value (high to low) - Default
   - By Balance
   - By P&L %
   - By 24h Change

4. Empty State
   - "You don't have any tokens yet"
   - "Explore Tokens" button → Token List

5. Click Behavior
   - Click token → Token Detail (FR-002)

VÀ holding list PHẢI:
- Real-time price updates
- P&L calculation accurate
```

**P&L Calculation:**

```
Cost Basis = Average purchase price × Balance
Current Value = Current price × Balance
P&L = Current Value - Cost Basis
P&L % = (P&L / Cost Basis) × 100
```

**Acceptance Criteria:**

- [ ] List hiển thị tokens với balance > 0
- [ ] Portfolio stats chính xác
- [ ] P&L calculation đúng
- [ ] Sorting works
- [ ] Click navigate đúng

----------

### 4.3. Created Tokens Tab

**FR-MP-004.3: Danh sách Token đã Tạo**

**Mô tả:**  
Hiển thị tất cả tokens mà user đã tạo (read-only view).

**Yêu cầu:**

```
Created Tokens List:

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
   - By Created Date (newest first) - Default
   - By Market Cap
   - By Volume
   - By Holders

3. Empty State
   - "You haven't created any tokens yet"
   - "Create Token" button → Create Token (FR-007)

4. Click Behavior
   - Click token → Token Detail (FR-002)

Note: 
- Đây chỉ là list view, READ-ONLY
- KHÔNG có "Manage Token" button
- Management ở Creator Dashboard (FR-006)

VÀ created list PHẢI:
- Show all tokens user created
- Status badge accurate
```

**Acceptance Criteria:**

- [ ] List hiển thị all created tokens
- [ ] Status badge correct
- [ ] Sorting works
- [ ] Click navigate đúng
- [ ] Empty state với CTA

----------

### 4.4. Transaction History Tab

**FR-MP-004.4: Lịch sử Giao dịch**

**Mô tả:**  
Hiển thị lịch sử giao dịch BUY/SELL của user.

**Yêu cầu:**

```
Transaction History List:

1. Transaction Items
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
   
2. TX Hash Link
   - Click → Solana Explorer (new tab)

3. Sorting
   - Mặc định: Newest first
   - Load more: Infinite scroll hoặc pagination

4. Empty State
   - "No transactions yet"
   - "Start trading to see your history"

5. Click Behavior
   - Click transaction → Token Detail (optional)
   - Click TX hash → Solana Explorer

VÀ transaction history PHẢI:
- Real-time updates khi có transaction mới
- Show cả Market Order và Limit Order executed
```

**Acceptance Criteria:**

- [ ] List hiển thị transactions chính xác
- [ ] Type badges (BUY/SELL) đúng màu
- [ ] TX hash links work
- [ ] Timestamps accurate
- [ ] Sorting newest first
- [ ] Empty state helpful

----------

### 4.5. Edit Profile Tab

**FR-MP-004.5: Chỉnh sửa Thông tin**

**Mô tả:**  
Form để user setup username/display name (one-time), chỉnh sửa thông tin cá nhân, và quản lý privacy settings.

**Yêu cầu:**

```
Edit Profile Page Structure:

SECTION 1: Privacy Settings (Đầu tiên)
SECTION 2: Profile Information Form
SECTION 3: Actions (Save/Cancel buttons)
```

----------

### 4.5.1. Privacy Settings

**FR-MP-004.5.1: Profile Privacy Controls**

**Mô tả:**  
Cho phép user kiểm soát ai có thể xem thông tin profile công khai của mình.

**Yêu cầu:**

```
Privacy Settings Section:

1. Section Header
   - Title: "Privacy Settings"
   - Icon: 🔒
   - Subtitle: "Control who can view your profile"

2. Privacy Settings Toggle
   
   A. Settings Group
      - Label: "Privacy Settings"
      - Toggle Label: "Public" (default) / "Private"
      - Default: Public (Unchecked)
      
      States:
      * Unchecked (Public): "Anyone can view your profile"
      * Checked (Private): "Only you can view your profile"
   
   B. Helper Text (Description)
      - Public State: "Anyone can view your profile"
      - Private State: "Only you can view your profile"

3. Granular Privacy Controls
   
   Note: Chỉ hiển thị khi Profile Visibility = ON (Public)
   
   A. Holdings Visibility
      - Checkbox: ☑ "Show my token holdings"
      - Default: Checked (visible)
      - When unchecked: Holdings tab shows "🔒 Holdings are private"
   
   B. Transaction History Visibility
      - Checkbox: ☑ "Show my transaction history"
      - Default: Checked (visible)
      - When unchecked: Transactions tab shows "🔒 Transaction history is private"

4. Always Public Notice
   - Info box (blue background):
     * Icon: ℹ️
     * Text: "Tokens you create are always public for transparency"
     * Cannot be changed

5. Behavior
   - Settings saved when user clicks "Save Changes" button (cùng với profile info)
   - No auto-save
   - No preview needed

VÀ privacy settings PHẢI:
- Clearly labeled and easy to understand
- Default: Public profile with all info visible
- Granular controls only show when profile is public
- Save together with profile info via "Save Changes" button
```

**Privacy Logic:**

```
IF hiddenProfile === ON (Hidden):
  → Hide entire profile on Public Profile page
  → Show "This profile is private 🔒" message
  → Exception: Created tokens always visible
  → Granular settings (Holdings, Transactions) are hidden/disabled

IF hiddenProfile === OFF (Public):
  → Show profile normally
  → Respect granular settings:
    * IF showHoldings === OFF → Hide holdings tab
    * IF showTransactions === OFF → Hide transactions tab
    * Created tokens always visible
```

**Acceptance Criteria:**

- [ ] Privacy settings section displays at top of Edit Profile
- [ ] Hidden Profile toggle works (OFF/ON)
- [ ] Granular controls only visible when profile is public (toggle OFF)
- [ ] Default state is OFF (Public) with all info visible
- [ ] Settings save with "Save Changes" button
- [ ] Clear helper text for each state
- [ ] Info box about created tokens displays

----------

### 4.5.2. Profile Information Form

**FR-MP-004.5.2: Edit Profile Form**

**Mô tả:**

```
Edit Profile Form:

IMPORTANT: Mixed Setup
- Username & Display Name: One-time only (không thể đổi sau khi save)
- Avatar, Bio, Social Links: Có thể edit bao nhiêu lần cũng được

1. Warning Banner
   - ⚠️ "Username & Display Name - One-time Setup"
   - "You can only set your username and display name once. Choose carefully!"
   - Background: Warning color (yellow/orange)

2. EDITABLE Fields (Có thể update bao giờ cũng được)
   
   A. Avatar
      - Upload button
      - Max 5MB, JPG/PNG/GIF
      - Crop/resize tool
      - Preview current avatar
   
   B. Bio
      - Optional
      - Max 200 characters
      - Character counter
      - Multi-line textarea
   
   C. Social Links
      - Twitter/X: URL validation
      - Telegram: Username or URL
      - Email: Email validation
      - All optional

3. ONE-TIME Fields (Chỉ set được 1 lần)
   
   A. Username *
      - Required, Unique
      - 3-20 characters
      - Alphanumeric + underscore/hyphen
      - Label: "Username * (One-time only)"
      - Helper: "Cannot change later"
      - Availability check on blur
      - After saved: Grayed out với lock icon 🔒
   
   B. Display Name
      - Optional
      - 1-50 characters
      - Label: "Display Name (One-time only)"
      - Helper: "Cannot change later"
      - After saved: Grayed out với lock icon 🔒

4. Read-only Fields
   - Wallet Address (cannot edit)
   - Created Date (auto)

5. Actions
   - "Save Changes" button
     * IF username/display name chưa setup:
       → Show confirmation modal
       → "Username & Display Name will be locked after save"
     * IF đã setup rồi (chỉ edit avatar/bio/social):
       → Save normally, no confirmation
   - "Cancel" button

6. Info Note
   - Show note box:
     * "Username and Display Name can only be set once"
     * "Avatar, Bio, and Social Links can be updated anytime"
     * "Contact support if you need to change locked fields"

VÀ form PHẢI:
- Warning rõ ràng cho one-time fields
- Confirmation modal chỉ khi save username/display name lần đầu
- Lock username/display name sau khi saved
- Avatar/Bio/Social links luôn editable
```

**Setup States:**

```
STATE 1: First Time (chưa setup username/display name)
────────────────────────────────────────
Avatar: [Editable]
Username: [Empty input] (One-time only)
Display Name: [Empty input] (One-time only)
Bio: [Editable]
Social Links: [Editable]

Save button: "Save Changes"
→ Confirmation modal: "Username & Display Name will be locked"

STATE 2: After Setup (đã set username/display name)
────────────────────────────────────────
Avatar: [Editable]
Username: dungdev 🔒 (Grayed out, locked)
Display Name: Dung - Crypto Trader 🔒 (Grayed out, locked)
Bio: [Editable]
Social Links: [Editable]

Save button: "Save Changes"
→ No confirmation modal, save directly
```

**Validation:**

```
Username (one-time):
- Check uniqueness on blur
- 3-20 characters
- Only alphanumeric, underscore, hyphen
- Cannot contain spaces

Display Name (one-time):
- 1-50 characters
- Can contain spaces and special chars

Bio (always editable):
- Max 200 characters
- Character counter updates real-time

Social Links (always editable):
- Twitter/X: Must be valid URL or empty
- Telegram: @username or full URL or empty
- Email: Valid email format or empty
```

**Acceptance Criteria:**

- [ ] Warning banner visible for one-time fields
- [ ] Username uniqueness check works
- [ ] Confirmation modal shows on first save
- [ ] Username/Display Name locked after first save
- [ ] Avatar upload works
- [ ] Bio character counter accurate
- [ ] Social links validation correct
- [ ] Can update Avatar/Bio/Social anytime
- [ ] Cannot update Username/Display after first save
- [ ] Clear messaging about what's editable

----------

### 4.6. Limit Orders Tab

**FR-MP-004.6: Quản lý Limit Orders**

**Mô tả:**  
Hiển thị và quản lý ACTIVE limit orders.

**Yêu cầu:**

```
Limit Orders List:

1. Order Cards (ACTIVE only)
   Mỗi order hiển thị:
   
   - Token Info (Clickable):
     * Avatar
     * Name + Symbol
     * Click → Navigate to Token Detail
   
   - Order Type:
     * BUY (green badge)
     * SELL (red badge)
   
   - Order Details:
     * Amount: 1.0 SOL or 50,000 tokens
     * Target Price: $0.00150
     * Current Price: $0.00123
   
   - Created: "2h ago"
   
   - Actions:
     * "Cancel Order" button (red)

2. Sorting & Filtering
   - Sort:
     * Created Date (newest) - Default
   - Filter:
     * All / BUY / SELL

3. Empty State
   - "You don't have any active limit orders"
   - "Explore Tokens" button

4. Cancel Order Flow
   - Click "Cancel"
   - Confirmation modal:
     * Order details
     * "Confirm" / "Cancel"
   - On confirm:
     * Cancel order
     * Release reserved balance
     * Remove from list

5. Click Behavior
   - Click token info (avatar/name) → Token Detail (FR-002)
   - Click Cancel → Confirmation modal

VÀ limit orders PHẢI:
- Show ACTIVE orders only
- Current price updates real-time
- Simple, clean layout
```

**Acceptance Criteria:**

- [ ] List shows active orders only
- [ ] Order details accurate
- [ ] Current price updates real-time
- [ ] Cancel works
- [ ] Balance released after cancel
- [ ] Sorting/filtering works
- [ ] Click token info navigates to Token Detail
- [ ] Empty state helpful

----------

## 5. ĐIỀU KIỆN CHẤP NHẬN (ACCEPTANCE CRITERIA)

**Overall:**

- [ ] Page loads < 2s
- [ ] All tabs functional
- [ ] Tab switching smooth
- [ ] Login required
- [ ] Responsive layout

**Data:**

- [ ] Lists complete and accurate
- [ ] Calculations correct
- [ ] Real-time updates work

**Interactions:**

- [ ] All clicks work
- [ ] Forms validate
- [ ] Sort/filter works
- [ ] Empty states helpful

----------

**END OF FR-004**
