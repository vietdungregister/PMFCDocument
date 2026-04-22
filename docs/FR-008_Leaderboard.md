# FR-008: BẢNG XẾP HẠNG (LEADERBOARD)

## 1. Mô tả

Bảng xếp hạng tokens theo Market Cap, hiển thị top 3 nổi bật và danh sách đầy đủ.

**User Story:**

```
Là một user,
Tôi muốn xem các tokens xếp hạng cao nhất,
Để phát hiện và trade các tokens tiềm năng.
```

----------

## 2. Giao diện

[To be added]

----------

## 3. ĐIỂM TRUY CẬP (ENTRY POINTS)

Users có thể truy cập Leaderboard từ:

1. **Main Navigation** - Sidebar menu "Leaderboard"
2. **Direct URL** - /leaderboard

**Default:** Hiển thị tất cả tokens ranked by Market Cap

----------

## 4. YÊU CẦU CHỨC NĂNG

### 4.1. Page Layout

**FR-LB-008.1: Cấu trúc Trang**

**Mô tả:**  
Layout với top 3 featured cards và table list.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Page Structure:

1. Header
   - Title: "Leaderboard"

2. Top 3 Featured Cards
   - Grid layout (3 columns)
   - Ranks: #001, #002, #003
   - Large, prominent display
   - Gradient background

3. Table List
   - Ranks: #004 onwards
   - Compact table format
   - 5 columns

VÀ leaderboard PHẢI:
- Rank by Market Cap (highest first)
- Real-time updates
- Responsive layout
```

**Acceptance Criteria:**

- [ ] Header displays correctly
- [ ] Top 3 cards prominent
- [ ] Table shows rank #4+
- [ ] Layout responsive

----------

### 4.2. Top 3 Featured Cards

**FR-LB-008.2: Top 3 Tokens**

**Mô tả:**  
Hiển thị 3 tokens xếp hạng cao nhất dạng featured cards.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Featured Card Content:

1. Rank Badge
   - Position: Top-left corner
   - Format: #001, #002, #003
   - Semi-transparent

2. Token Header
   - Avatar (80x80, rounded 16px)
   - Name (20px, bold)
   - Statement/Tagline (12px, truncated)
   - Buy button (primary green)

3. Metrics (2 rows)
   Row 1: mc [change%] [value]
   - Example: mc +3.54% $7.08M
   
   Row 2: 24h vol [change%] [value]
   - Example: 24h vol +48.45% $10K

4. Creator Info
   - Creator avatar (32px circle)
   - "by" label
   - Wallet address (truncated)
   - Created time: "• Xmos Xd Xh ago"

5. Visual Design
   - Gradient background (warm tones)
   - Border: var(--card-border)
   - Hover: Lift effect + border highlight

VÀ featured cards PHẢI:
- Click anywhere → Token Detail (FR-002)
- Buy button → Trading Panel (FR-003)
- Real-time metrics updates
- Responsive grid
```

**Color Coding:**

```
% Change Colors:
- Positive: Green (#10b981)
- Negative: Red (#ef4444)
- Zero: Gray (#9ca3af)
```

**Acceptance Criteria:**

- [ ] Top 3 cards display correctly
- [ ] Metrics accurate
- [ ] Click navigation works
- [ ] Buy button functions
- [ ] Hover effects smooth
- [ ] Responsive on mobile

----------

### 4.3. Table List

**FR-LB-008.3: Full Rankings Table**

**Mô tả:**  
Hiển thị tất cả tokens từ rank #4 trở đi dạng table.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Table Structure:

Header: "TOKEN" (uppercase, small, gray)

Columns (5):

1. Token (40% width)
   - Avatar (40x40, rounded 12px)
   - Name (bold)
   - Rank: #XXX (below name, small, gray)

2. Creator (30% width)
   - Avatar (28px circle)
   - Wallet address (truncated)

3. Holders (15% width)
   - Count: X,XXX
   - Format with comma separator

4. Market Cap (20% width)
   - Value: $XXX or $X.XXM
   - % Change (below, small)
   - Color coded: Green/Red/Gray

5. Action (15% width)
   - Buy button (secondary style)
   - Right aligned

Row Behavior:
- Hover: Background change
- Click anywhere → Token Detail (FR-002)
- Buy button → Trading Panel (FR-003)

VÀ table PHẢI:
- Show all tokens ranked by MC
- Real-time updates
- Smooth hover transitions
- Pagination (load more)
```

**Responsive Behavior:**

```
Mobile (< 768px):
- Hide Creator column
- Hide Holders column
- Show: Token, MC, Buy button (3 columns)
```

**Acceptance Criteria:**

- [ ] Table displays all tokens
- [ ] Columns align correctly
- [ ] Holders formatted with commas
- [ ] MC values accurate
- [ ] % changes color coded
- [ ] Click navigation works
- [ ] Buy button functions
- [ ] Hover effects work
- [ ] Responsive on mobile
- [ ] Pagination works

----------

## 5. ĐIỀU KIỆN CHẤP NHẬN (ACCEPTANCE CRITERIA)

**Overall:**

- [ ] Leaderboard loads quickly
- [ ] Rankings accurate
- [ ] Real-time updates work
- [ ] Responsive on all devices

**Top 3 Cards:**

- [ ] Featured prominently
- [ ] Metrics accurate
- [ ] Navigation works

**Table:**

- [ ] All tokens listed
- [ ] Sorting by MC correct
- [ ] Pagination smooth
- [ ] Mobile responsive

----------

**END OF FR-008**
