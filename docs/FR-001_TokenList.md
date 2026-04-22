# FR-001: DANH SÁCH TOKEN

## 1. Mô tả

Trang chính để users khám phá, lọc và tìm kiếm tokens. Hiển thị danh sách tokens dưới dạng cards hoặc grid với các thông tin quan trọng như giá, market cap, volume, và trust level.

**User Story:**

```
Là một user,
Tôi muốn duyệt danh sách tokens với nhiều cách filter và search khác nhau,
Để có thể tìm được tokens phù hợp để mua.
```

----------

## 2. Giao diện

[To be added]

----------

## 3. ĐIỂM TRUY CẬP (ENTRY POINTS)

Users có thể truy cập Token List từ:

1. **Home page** - Landing page mặc định
2. **Navigation menu** - Click logo của web

**Default:** Tab Discover được active khi vào lần đầu

----------

## 4. YÊU CẦU CHỨC NĂNG

### 4.1. Danh sách các Tabs

**FR-TL-001.1: Hiển thị Tab Navigation**

**Mô tả:**  
Cung cấp 5 tabs để users chọn cách xem tokens khác nhau.

**Yêu cầu:**

```
Hiển thị 5 tabs:
1. Discover (mặc định)
2. Trending
3. Top Volume
4. Graduated
5. Favorite

VÀ tabs PHẢI:
- Active tab có visual indicator rõ ràng
- Chuyển tab reset pagination về page 1
- Chuyển tab giữ nguyên filters và search query

Empty States theo Tab:
- Graduated: "Chưa có token nào đạt graduation ($69K MC)"
- Favorite: "Bạn chưa có token yêu thích nào"
```

**Acceptance Criteria:**

- [ ] 5 tabs hiển thị token đúng theo quy định
- [ ] Discover là tab mặc định
- [ ] Filters giữ nguyên khi chuyển tab

----------

### 4.2. Công thức hiển thị của các tab

**FR-TL-001.2: Tính toán DiscoverScore**

**Mô tả:**  
Tính toán công thức để đưa token vào tab Discover.

**Công thức:**

```
DiscoverScore =
  0.40 * TrendingScore +
  0.20 * LiquidityDepthPoints +
  0.20 * HoldersQualityPoints +
  0.10 * TrustScore +
  0.10 * RecencyPoints

Tất cả scores normalize về 0.0 - 1.0
```

**Chi tiết từng thành phần:**

**1. TrendingScore (40%)**

```
TrendingScore = (Vol24h * 5) + (BuyCount24h * 3) + (PriceChange24h% * 2)
```

**2. LiquidityDepth (20%)**

```
Mapping LiquiditySOL → LiquidityDepthPoints:

0      → 0
0.5    → 6
1      → 12
2      → 20
3      → 26
5      → 35
8      → 45
10     → 52
15     → 62
20     → 70
30     → 82
50     → 95
100    → 108
200+   → 120
```

**3. HoldersQualityScore (20%)**

```
Mapping Holders → HoldersQualityPoints:

1    → 0
3    → 8
5    → 14
10   → 25
20   → 38
30   → 46
50   → 60
80   → 72
100  → 80
150  → 92
200  → 100
300  → 108
500+ → 120
```

**4. TrustScore (10%)**

```
To be decided
```

**5. RecencyScore (10%)**

```
age_hours = (thời_gian_hiện_tại - created_at)

age_hours → RecencyPoints:
<= 6h     → 60
<= 24h    → 50
<= 72h    → 35
<= 168h   → 20   (7 ngày)
<= 720h   → 8    (30 ngày)
> 720h    → 0
```

**Yêu cầu:**

```
- Tính DiscoverScore cho mọi token
- Sắp xếp tokens theo DiscoverScore giảm dần
- Tính lại scores mỗi 10 phút
- Cache scores để tránh tính lại mỗi request
- Update danh sách mà không làm gián đoạn scroll
```

**Acceptance Criteria:**

- [ ] DiscoverScore tính đúng công thức
- [ ] Tokens sắp xếp giảm dần
- [ ] Scores recalculate mỗi 10 phút
- [ ] Cache hoạt động đúng

----------

**FR-TL-001.3: Tab Trending**

**Mô tả:**  
Tính toán công thức để đưa token vào tab Trending.

**Công thức:**

```
TrendingScore = (Vol24h * 5) + (BuyCount24h * 3) + (PriceChange24h% * 2)
```

**Yêu cầu:**

```
- Tính TrendingScore cho mọi token
- Sắp xếp tokens theo TrendingScore giảm dần
- Tính lại scores mỗi 10 phút
- Cache scores
- Update real-time
```

**Acceptance Criteria:**

- [ ] TrendingScore tính đúng
- [ ] Sắp xếp giảm dần
- [ ] Update mỗi 10 phút

----------

**FR-TL-001.4: Tab Top Volume, Graduated, Favorite**

**Mô tả:**  
Hiển thị đúng như tên gọi.

**Yêu cầu:**

```
Top Volume:
- Sắp xếp theo Volume 24h (cao → thấp)

Graduated:
- Chỉ show tokens đã đạt $69K MC
- Đã migrate sang Raydium

Favorite:
- Tokens user đã favorite
- Login required
- Empty state nếu chưa có
```

----------

### 4.3. Hiển thị Token Card

**FR-TL-001.5: Token Card Information**

**Mô tả:**  
Mỗi token hiển thị dưới dạng card.

**Yêu cầu:**

```
Mỗi token card hiển thị:

1. Avatar Token

2. Tên Token
   - Typography: Bold, prominent

3. Symbol Token
   - Chữ hoa, có thể có prefix

4. Token short statement

5. Price
   - Format:
     * < $0.01: 6 decimals ($0.000123)
     * $0.01 - $1: 4 decimals ($0.1234)
     * >= $1: 2 decimals ($12.34)
   - Prefix: $

6. Market Cap
   - Rút gọn K/M/B
   - 2 decimals sau rút gọn
   - Label: "MC: "

7. Volume 24h
   - Format giống Market Cap
   - Label: "Vol: "
   - Update mỗi 30s

8. Price Change 24h
   - Format: ±X.XX%
   - Màu: Green (>0) / Red (<0) / Gray (=0)
   - Icon: ↑ hoặc ↓

9. Trust Level Badges (nếu có)
   - 🔒 LP Locked
   - ✓ Audited
   - 🛡️ Freeze Disabled
   - Tooltip chi tiết khi hover

10. Favorite Button
    - Icon: ♡ (rỗng) / ♥ (đầy)
    - Position: Top-right corner
    - Click toggle favorite

11. Tiến độ tốt nghiệp

VÀ card PHẢI:
- Clickable toàn bộ (trừ favorite icon)
- Hover effect
- Layout responsive
```

**Acceptance Criteria:**

- [ ] Tất cả trường hiển thị đúng
- [ ] Price format theo mức
- [ ] Rút gọn K/M/B chính xác
- [ ] Color coding đúng
- [ ] Performance tốt với 100+ cards

----------

### 4.4. Nút Filter

**FR-TL-001.6: Custom Filters**

**Mô tả:**  
Users có thể áp dụng filters để thu hẹp danh sách.

**Yêu cầu:**

```
Hệ thống có 3 filters:

1. NSFW Content
   - Toggle switch
   - Tùy chọn: Hiện / Ẩn
   - Mặc định: Ẩn (OFF)

2. Market Cap Range
   - Thanh trượt slide + textbox
   - Range: 0 đến 50M+ USD

3. Volume 24h Range
   - Thanh trượt slide + textbox
   - Range: 0 đến 50K+ USD

4. Trust Level (nếu có)
   - Multi-select checkboxes:
     □ LP Locked
     □ Audited
     □ Freeze Authority Disabled
     □ Unverified (hiện tất cả)
   - Mặc định: Tất cả checked
   - Hành vi: OR logic

VÀ filters PHẢI:
- Kết hợp với AND logic
- Áp dụng TRÊN kết quả tab
- Flow: Tab → Filter → Search → Sort → Display
- Trigger refresh ngay
- Reset pagination về page 1
- Hiển thị badge số filters active
- Có nút "Reset Filters"
```

**Acceptance Criteria:**

- [ ] Filters hoạt động đúng
- [ ] AND logic chính xác
- [ ] Badge đếm active filters
- [ ] Reset filters works

----------

### 4.5. Chức năng Sắp xếp

**FR-TL-001.7: Sort Functionality**

**Mô tả:**  
Users có thể sắp xếp danh sách qua Sort Panel.

**Yêu cầu:**

```
Sort Options:
○ Không sắp xếp (default)
○ Giá
○ Market Cap
○ Volume 24h
○ Ngày tạo

Toggle Direction:
- Mặc định: Tăng dần
- Click lần 1: Giảm dần ↓
- Click lần 2: Tăng dần ↑

VÀ sort PHẢI:
- Áp dụng cùng với: Tab → Filter → Search → Sort
- Không reset pagination
- Hiển thị sort hiện tại trên nút Sort
- Khi sort sẽ override hiển thị của tab
```

**Acceptance Criteria:**

- [ ] Sort options hoạt động
- [ ] Direction toggle works
- [ ] Display current sort

----------

### 4.6. Tìm kiếm

**FR-TL-001.8: Search**

**Mô tả:**  
Search và update danh sách khi nhấn Enter.

**Yêu cầu:**

```
Search Behavior:

Khi user nhấn Enter:
- Xóa danh sách hiện tại
- Hiển thị loading skeleton
- Hiển thị kết quả

Kết quả search:
- Bao gồm tất cả tokens khớp query
- Tuân filter constraints

VÀ search PHẢI:
- Hoạt động trên tất cả tabs
- Hỗ trợ ký tự đặc biệt
- Chỉ tokens public
```

**Acceptance Criteria:**

- [ ] Enter updates main list
- [ ] Số kết quả chính xác
- [ ] Filters applied correctly

----------

## 5. ĐIỀU KIỆN CHẤP NHẬN (ACCEPTANCE CRITERIA)

**Overall:**

- [ ] 5 tabs functional
- [ ] Discover default tab
- [ ] Filters work correctly
- [ ] Sort works correctly
- [ ] Search works correctly

**Performance:**

- [ ] Scores cache works
- [ ] Real-time updates smooth
- [ ] 100+ cards perform well

**UX:**

- [ ] Empty states helpful
- [ ] Loading states clear
- [ ] Error handling graceful

----------

**END OF FR-001**
