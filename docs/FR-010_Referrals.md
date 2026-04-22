# FR-010: GIỚI THIỆU (REFERRALS)

## 1. Mô tả

Chương trình giới thiệu bạn bè, kiếm 5% từ trading fees của người được giới thiệu.

**User Story:**

```
Là một user,
Tôi muốn giới thiệu bạn bè và kiếm thêm thu nhập,
Để tăng earnings từ trading activities của họ.
```

----------

## 2. Giao diện

[To be added]

----------

## 3. ĐIỂM TRUY CẬP (ENTRY POINTS)

Users có thể truy cập Referrals từ:

1. **Main Navigation** - Sidebar menu "Referrals"
2. **Direct URL** - /referrals

**Default:** Hiển thị tất cả sections

----------

## 4. YÊU CẦU CHỨC NĂNG

### 4.1. Page Layout

**FR-REF-010.1: Cấu trúc Trang**

**Mô tả:**  
Layout với stats overview và 3 sections chính.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Page Structure:

1. Header
   - Title: "Referral Program"
   - Subtitle: "Invite friends and earn 5% of their trading fees"

2. Stats Overview (3 cards)
   - Total Referrals
   - Total Earnings
   - This Month

3. Sections (3)
   - Your Referral Link
   - Claimable Rewards
   - Referred Users

VÀ referrals PHẢI:
- Login required
- Real-time updates
- Responsive layout
```

**Acceptance Criteria:**

- [ ] Header displays correctly
- [ ] Stats accurate
- [ ] All sections visible
- [ ] Layout responsive

----------

### 4.2. Stats Overview

**FR-REF-010.2: Thống kê Tổng quan**

**Mô tả:**  
Hiển thị thống kê referral performance.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Stats Cards (3):

1. Total Referrals
   - Value: XX users
   - Sub: "Active users"

2. Total Earnings
   - Value: XX.X SOL
   - Sub: ≈ $X,XXX (USD equivalent)

3. This Month
   - Value: X.X SOL
   - Sub: ≈ $XXX (USD equivalent)

VÀ stats PHẢI:
- Real-time updates
- Accurate calculations
- USD conversion current
```

**Acceptance Criteria:**

- [ ] All stats display correctly
- [ ] Real-time updates work
- [ ] USD conversion accurate
- [ ] Grid responsive

----------

### 4.3. Referral Link Section

**FR-REF-010.3: Link Giới thiệu**

**Mô tả:**  
Copy và share referral link.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Referral Link:

1. Link Box
   - URL: https://pumpfun.io/ref/[username]
   - Read-only input
   - Copy button: "📋 Copy Link"

2. Copy Function
   - Click → Copy to clipboard
   - Show success: "✓ Copied!" (2 seconds)
   - Then revert to "📋 Copy Link"

3. Share Buttons (2)
   - Twitter: "🐦 Share on Twitter"
     → Open Twitter share with pre-filled text
   - Telegram: "✈️ Share on Telegram"
     → Open Telegram share

VÀ referral link PHẢI:
- Generate unique per user
- Based on username
- Copy function works
- Share opens new window
```

**Share Text Templates:**

```
Twitter:
Join me on @PumpFunSOL and start trading meme tokens! 🚀

Use my referral link: [LINK]

#Solana #MemeCoin #Crypto

Telegram:
🚀 Join PumpFun - Trade meme tokens on Solana!

Use my link to get started: [LINK]
```

**Acceptance Criteria:**

- [ ] Link generates correctly
- [ ] Copy function works
- [ ] Success message shows
- [ ] Share buttons work
- [ ] Pre-filled text correct

----------

### 4.4. Claimable Rewards Section

**FR-REF-010.4: Claim Rewards**

**Mô tả:**  
Hiển thị và claim referral earnings.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Claimable Rewards:

1. Claim Box
   - Background: Gradient green
   - Border: Green
   
   Content:
   - Amount: X.X SOL (large, green)
   - USD: ≈ $XXX available to claim
   - Button: "Claim Rewards"

2. Claim Function
   - Requires: Wallet connection
   - Click → Wallet signature
   - Transfer claimable to wallet
   - Update balance
   - Show success message

3. States
   - Has claimable: Button enabled
   - No claimable: Button disabled
   - Claiming: Loading state

VÀ claim PHẢI:
- Accurate balance
- Require wallet
- Update real-time
- Handle errors
```

**Acceptance Criteria:**

- [ ] Balance displays correctly
- [ ] USD conversion accurate
- [ ] Claim button works
- [ ] Wallet connection required
- [ ] Balance updates after claim
- [ ] Error handling works

----------

### 4.5. Referred Users Section

**FR-REF-010.5: Danh sách Người giới thiệu**

**Mô tả:**  
Hiển thị tất cả users đã được giới thiệu.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Referred Users List:

1. Table Header
   - Title: "Referred Users (XX)"
   - Count: Total referred

2. Table Columns (4)
   
   User:
   - Avatar (40px circle)
   - Username
   - Wallet address (truncated)
   
   Joined:
   - Relative time: "2 days ago"
   
   Trade Volume:
   - SOL amount
   - USD equivalent
   
   Your Earnings:
   - SOL earned from this user
   - USD equivalent

3. Sorting
   - Default: Joined date (newest first)
   - Optional: By earnings

4. Click Behavior
   - Click row → Public Profile (FR-005)
   - Cursor: Pointer
   - Hover: Background highlight

5. Empty State
   - "No referrals yet"
   - "Share your link to start earning"

VÀ users list PHẢI:
- Show all referred users
- Real-time trade volume
- Accurate earnings
- Clickable to profile
```

**Earnings Calculation:**

```
User Earnings = User's Total Trade Volume × 5%

Example:
- User trades: 45.8 SOL
- Your earnings: 45.8 × 0.05 = 2.29 SOL
```

**Responsive:**

```
Mobile (< 768px):
- Hide "Trade Volume" column
- Show: User, Joined, Earnings (3 columns)
```

**Acceptance Criteria:**

- [ ] Table displays all users
- [ ] Columns align correctly
- [ ] Trade volume accurate
- [ ] Earnings calculation correct
- [ ] Click navigation works
- [ ] Sorting works
- [ ] Empty state helpful
- [ ] Responsive on mobile

----------

## 5. ĐIỀU KIỆN CHẤP NHẬN (ACCEPTANCE CRITERIA)

**Overall:**

- [ ] Login required
- [ ] All sections display
- [ ] Real-time updates work
- [ ] Responsive layout

**Stats:**

- [ ] Accurate calculations
- [ ] USD conversion current
- [ ] Real-time updates

**Referral Link:**

- [ ] Link generates correctly
- [ ] Copy function works
- [ ] Share buttons work

**Claim:**

- [ ] Balance accurate
- [ ] Claim function works
- [ ] Wallet connection required

**Users List:**

- [ ] All users shown
- [ ] Earnings accurate
- [ ] Navigation works
- [ ] Mobile responsive

----------

**END OF FR-010**
