# Token War — Phân tích Mô hình CLOB (Central Limit Order Book)

---

## Khái niệm CLOB

CLOB hoạt động giống **sàn chứng khoán**: Khớp lệnh mua bán trực tiếp giữa các user.

- User đặt lệnh mua/bán phiếu ở mức giá mình muốn
- Hệ thống ghép lệnh khi giá khớp nhau
- Giá do cung/cầu thực tế quyết định

**Ví dụ — mua lần đầu tiên:**

War DOGE vs PEPE vừa mở.

- Người A nghĩ DOGE thắng → đặt **BUY DOGE @0.63 SOL**
- Người B nghĩ PEPE thắng → đặt **BUY PEPE @0.37 SOL**
- 0.63 + 0.37 = 1.00 SOL → hệ thống **Mint** 1 cặp phiếu mới: A nhận phiếu DOGE, B nhận phiếu PEPE, vault nhận 1 SOL


---

## Các khái niệm cơ bản

**Phiếu (Share):** Chứng nhận quyền nhận thưởng nếu một token thắng war.
- Phiếu DOGE: nhận 1 SOL nếu DOGE thắng, nhận 0 nếu thua
- Phiếu PEPE: nhận 1 SOL nếu PEPE thắng, nhận 0 nếu thua

**Mệnh giá:** Số SOL nhận được khi đổi 1 phiếu thắng. Quy định trước khi war bắt đầu.

**Vault:** Két hệ thống giữ SOL đảm bảo chi trả đủ khi war kết thúc.

**Order Book:** Danh sách toàn bộ lệnh chờ khớp của cả 2 phía.

**Spread:** Khoảng cách giữa giá mua cao nhất (best bid) và giá bán thấp nhất (best ask). Spread càng nhỏ → thị trường càng thanh khoản tốt.

**Probability:** Giá phiếu = xác suất thắng theo đánh giá của thị trường. Phiếu DOGE giá 0.63 SOL → xác suất thắng 63%.

**Tính chất của binary market:**

```
Giá phiếu DOGE + Giá phiếu PEPE = 1 SOL (luôn luôn)
Vì chắc chắn một bên thắng, tổng payout = 1 SOL/cặp phiếu.
```

---

## 3 Loại giao dịch trong CLOB Binary Market

> **Ưu tiên khớp lệnh:** Direct Match trước (nếu có phiếu sẵn trong book) → Mint (nếu BUY không tìm được Direct Match) → Merge (nếu SELL không tìm được Direct Match).

### Loại 1 — Direct Match (Khớp trực tiếp) — ưu tiên cao nhất

Người đang giữ phiếu muốn thoát, bán lại cho người mới muốn mua. Không tạo thêm hay hủy phiếu nào.

Điều kiện: người bán phải **đã có phiếu** từ trước (từ Mint hoặc mua lại trước đó).

```
User A (đang giữ 2 phiếu DOGE):
  SELL 2 phiếu DOGE @0.68 SOL

User C (mới vào, tin DOGE thắng):
  BUY  2 phiếu DOGE @0.68 SOL

→ Khớp trực tiếp: A nhận 1.36 SOL, C nhận 2 phiếu DOGE

Vault: không thay đổi
Phiếu lưu hành: không thay đổi
```

### Loại 2 — Mint (Tạo phiếu mới) — khi BUY không có Direct Match

Khi lệnh BUY không tìm được ai SELL trong book → hệ thống tìm lệnh BUY đối lập để ghép cặp và in phiếu mới. Xảy ra bất kỳ lúc nào trong war khi thiếu thanh khoản sell-side.

Điều kiện: `giá BUY DOGE + giá BUY PEPE = 1.00 SOL (mệnh giá)`

```
User A: BUY 1 phiếu DOGE @0.63 SOL  ← tin DOGE thắng
User B: BUY 1 phiếu PEPE @0.37 SOL  ← tin PEPE thắng

Không ai có phiếu để bán → Direct Match thất bại
→ Hệ thống ghép 2 lệnh BUY đối lập (0.63 + 0.37 = 1.00):
  Thu vào vault: 1.00 SOL
  In ra:         1 phiếu DOGE + 1 phiếu PEPE
  Giao:          phiếu DOGE → A, phiếu PEPE → B

Vault: +1.00 SOL
Phiếu DOGE lưu hành: +1
Phiếu PEPE lưu hành: +1
```

### Loại 3 — Merge (Hủy phiếu) — khi SELL không có Direct Match

Người giữ DOGE và người giữ PEPE đều muốn thoát → hệ thống burn cặp phiếu, trả SOL từ vault.

Điều kiện: `giá SELL DOGE + giá SELL PEPE = 1.00 SOL`

```
User A (giữ phiếu DOGE): SELL 1 phiếu DOGE @0.62 SOL
User B (giữ phiếu PEPE): SELL 1 phiếu PEPE @0.38 SOL

→ Hệ thống ghép 2 lệnh SELL đối lập:
  Burn: 1 phiếu DOGE + 1 phiếu PEPE
  Rút:  1.00 SOL từ vault
  Giao: 0.62 SOL → A, 0.38 SOL → B

Vault: −1.00 SOL
Phiếu lưu hành: mỗi bên −1
```

**Vault luôn cân bằng:** Mỗi cặp phiếu lưu hành = đúng 1 SOL trong vault → hệ thống không bao giờ vỡ nợ.

---

## Bước 1: Khởi tạo war — Không cần seed

Đây là ưu điểm lớn nhất so với AMM.

```
War: DOGE vs PEPE — 6 tiếng
Mệnh giá: 1 SOL/phiếu
Order book ban đầu: trống rỗng

Không có pool, không có seed, không có rủi ro tài chính cho platform.
```

**Nhưng ai đặt lệnh đầu tiên?**

Đây là vấn đề cold start — xem phần "Thách thức lớn nhất" bên dưới.

---

## Bước 2: Market Maker đặt lệnh tạo thanh khoản

Giả sử có 1 Market Maker (MM) — có thể là bot của platform hoặc bên thứ 3.

MM cũng **chưa có phiếu nào**. Vậy MM đặt SELL DOGE bằng cách nào?

> **SELL DOGE @0.51 ≡ cam kết BUY PEPE @0.49** (vì DOGE + PEPE = 1 SOL)
>
> Khi có người mua DOGE @0.51 → hệ thống Mint: người mua nhận DOGE, MM nhận PEPE, vault nhận 1 SOL.
> MM không cần có phiếu trước — họ đang cam kết "tôi sẵn lòng cầm PEPE nếu bạn cầm DOGE".

MM đặt lệnh 2 chiều tại mức 50/50 (chưa có thông tin lệch bên nào):

```
Order Book lúc khởi đầu (MM inject — toàn bộ là Mint commitments):

DOGE:
  BUY  orders: 0.49 (5) | 0.48 (10) | 0.47 (15)  ← MM sẵn lòng cầm DOGE nếu ai bán DOGE rẻ
  SELL orders: 0.51 (5) | 0.52 (10) | 0.53 (15)  ← MM sẵn lòng cầm PEPE nếu ai mua DOGE

Giá thị trường: ~0.50 SOL (spread = 0.02)
Implied probability: DOGE 50% — PEPE 50%
```

MM kiếm tiền từ spread: thu 0.51 khi bán DOGE (cầm PEPE), sau đó bán PEPE @0.49 khi có người cần → lãi 0.02 SOL/vòng.

---

## Bước 3: User tham gia — Lệnh Market vs Limit

### Lệnh Market (khớp ngay) → kích hoạt Mint với MM

**User 1 (U1) muốn mua phiếu DOGE ngay lập tức:**

```
U1: BUY 3 phiếu DOGE (Market Order)

Hệ thống khớp với best ask của MM @0.51 SOL:
  → Mint xảy ra 3 lần: mỗi lần U1 trả 0.51, MM trả 0.49, vault nhận 1.00 SOL
  → U1 nhận phiếu DOGE, MM nhận phiếu PEPE

U1 trả: 3 × 0.51 = 1.53 SOL
MM trả: 3 × 0.49 = 1.47 SOL  (khóa trong vault)
Vault nhận: 3 × 1.00 = 3.00 SOL

U1 nhận: 3 phiếu DOGE → payout nếu DOGE thắng: 3.00 SOL (lãi 1.47 SOL)
MM nhận: 3 phiếu PEPE → payout nếu PEPE thắng: 3.00 SOL (lãi 1.53 SOL)

Order Book sau:
  SELL orders: 0.51 (2 phiếu còn lại) | 0.52 (10) | 0.53 (15)

Implied probability DOGE: ~0.51 (tăng nhẹ vì có người mua)
```

### Lệnh Limit (chờ khớp)

**User 2 (U2) muốn mua DOGE nhưng chỉ chấp nhận giá tối đa 0.55:**

```
U2: BUY 5 phiếu DOGE @0.55 SOL (Limit Order)

Kiểm tra best ask: 0.51 → thấp hơn 0.55 → khớp ngay!

Khớp: 5 phiếu @0.51 SOL (giá của seller, không phải giá U2 đặt)
U2 trả: 5 × 0.51 = 2.55 SOL
U2 nhận: 5 phiếu DOGE

→ U2 được lợi: đặt sẵn lòng trả 0.55 nhưng chỉ phải trả 0.51
```

### Lệnh không khớp ngay — vào Queue

**User 3 (U3) muốn mua DOGE nhưng chờ giá tốt hơn:**

```
U3: BUY 10 phiếu DOGE @0.48 SOL (Limit Order)

Kiểm tra best ask: 0.51 → cao hơn 0.48 → KHÔNG khớp

Lệnh treo trong order book:
  BUY orders: 0.49 (5 MM) | 0.48 (10 U3 mới vào) | 0.47 (15 MM) ...

U3 chờ đến khi có người SELL @0.48 hoặc thấp hơn.
Nếu hết war vẫn chưa khớp → lệnh huỷ, U3 lấy lại SOL.
```

---

## UX Design — Ẩn độ phức tạp CLOB với user

### Vấn đề: CLOB native UX quá phức tạp với retail user

Trong CLOB thuần túy, user phải tự nhập giá cho mỗi lệnh → khó hiểu với người không quen trading.

```
Giao diện CLOB native:
  [Mua DOGE]  Giá: [____] SOL   Số lượng: [____] phiếu   [Đặt lệnh]

→ User không biết nên nhập giá bao nhiêu
→ Không biết lệnh có khớp được không
→ Rào cản cao với user mới
```

### Giải pháp: Hiển thị giá cố định + Auto Market Order

Ẩn toàn bộ CLOB phía sau. Frontend chỉ hiện:

```
Giao diện đơn giản (giống swap DEX):

  ┌─────────────────────────────────────┐
  │  DOGE thắng                    58%  │
  │                                     │
  │  Giá hiện tại:  0.58 SOL/phiếu     │
  │  Số lượng:      [   5   ] phiếu    │
  │                                     │
  │  Bạn trả:       ≈ 2.90 SOL         │
  │  Nếu thắng:     5.00 SOL (+2.10)   │
  │  Slippage ước tính: ~0.8%          │
  │                                     │
  │  [    MUA DOGE NGAY    ]           │
  └─────────────────────────────────────┘
```

Khi user nhấn Mua → hệ thống tự đặt **Market Order** ở best ask hiện tại.

### Vấn đề Slippage khi dùng Market Order

Nếu order book mỏng, user sẽ fill ở nhiều mức giá khác nhau:

```
Order book DOGE (ask side):
  0.58 → 2 phiếu
  0.61 → 2 phiếu
  0.65 → 10 phiếu

User mua 5 phiếu "tại giá 0.58":
  → 2 phiếu @ 0.58
  → 2 phiếu @ 0.61
  → 1 phiếu @ 0.65
  → Giá trung bình thực tế = 0.606 (khác giá hiển thị!)

→ Cần hiển thị cảnh báo slippage và cho phép set slippage tối đa.
```

**Giải pháp:** Giống Uniswap — hiện slippage ước tính, cho phép user set max slippage (mặc định 1%). Nếu slippage thực tế vượt ngưỡng → tx bị từ chối, user không bị mua giá xấu.

### Polymarket: Hỗ trợ cả hai chế độ

Polymarket không chọn một — họ cung cấp **cả market order lẫn limit order**:

```
Tab 1 — Market (mặc định, dành cho user phổ thông):
  Hiện giá hiện tại → user nhập SOL muốn bỏ → mua ngay
  Đơn giản, không cần hiểu order book

Tab 2 — Limit (dành cho trader):
  User tự nhập giá + số lượng → lệnh treo trong book
  Phù hợp khi muốn mua ở giá tốt hơn, hoặc làm MM cá nhân
```

### Gợi ý UX cho Token War

| Phase | Chế độ | Lý do |
|-------|--------|-------|
| Giai đoạn 1 | Market Order only | User chủ yếu là retail, ưu tiên đơn giản |
| Giai đoạn 2 | Market + Limit (tab) | Khi có trader chuyên nghiệp tham gia |
| Giai đoạn 3 | Market + Limit + Order Book UI | Full CLOB experience khi platform trưởng thành |

**Nguyên tắc:** Market Order là default, Limit Order là advanced feature — giống cách Uniswap "Simple" vs Uniswap Pro.

---

## Bước 4: Giá di chuyển theo sentiment

Khi nhiều người mua DOGE liên tục:

```
Trạng thái ban đầu: DOGE @0.50
→ U1 mua market: best ask từ 0.51 → 0.52 (đã ăn hết 0.51)
→ U4 mua thêm: best ask từ 0.52 → 0.53
→ U5 mua thêm: best ask từ 0.53 → 0.54

Giá mới: ~0.53 SOL
Implied probability DOGE: 53% (thị trường tin DOGE đang thắng thế)
Implied probability PEPE: 47%

Implied probability DOGE tăng dần theo từng lệnh mua.
```

---

## Bước 5: Kết thúc war — Token DOGE thắng

```
DOGE thắng (buy volume cao hơn trong thời gian war)

Mỗi phiếu DOGE: đổi được 1 SOL
Mỗi phiếu PEPE: = 0 SOL

Ví dụ user holdings khi war kết thúc:
  U1:  3 phiếu DOGE → nhận 3.00 SOL (vào 1.53 SOL → lãi 1.47 SOL)
  U2:  5 phiếu DOGE → nhận 5.00 SOL (vào 2.55 SOL → lãi 2.45 SOL)
  U3:  0 phiếu (lệnh chưa khớp) → lấy lại toàn bộ SOL đặt cọc
  U6:  4 phiếu PEPE → nhận 0 SOL  (mất toàn bộ 2.08 SOL)
```

**Vault settlement:**
```
Vault thu vào từ Mint: tổng SOL của tất cả cặp phiếu được tạo ra
Vault chi ra:          tổng phiếu DOGE thắng × 1 SOL (mỗi phiếu đổi 1 SOL)
Còn lại:               0 SOL (vault cân bằng tuyệt đối)

Phiếu PEPE thua: hết giá trị, không được đổi, không cần burn.

→ Vault luôn có đủ SOL trả cho bên thắng. Platform không chịu rủi ro từ kết quả war.
```

---

## Thuật toán khớp lệnh — Flowchart

```
                     ╭─────────────────────╮
                     │    Lệnh mới vào     │
                     │ token / side /      │
                     │ price / qty         │
                     ╰──────────┬──────────╯
                                │
                     ╔══════════╧══════════╗
                    ╱                       ╲
                   ╱      BUY hay SELL?      ╲
                   ╲                         ╱
                    ╚═══╤═══════════╤════════╝
                        │           │
                       BUY         SELL
                        │           │
           ┌────────────┘           └────────────┐
           │                                     │
           ▼                                     ▼
  ┌─────────────────┐                 ┌─────────────────┐
  │ Tìm SELL cùng   │                 │ Tìm BUY cùng    │
  │ token @≤ price  │                 │ token @≥ price  │
  │ trong book      │                 │ trong book      │
  └────────┬────────┘                 └────────┬────────┘
           │                                   │
  ╔════════╧════════╗               ╔══════════╧══════════╗
 ╱  Có lệnh khớp?   ╲             ╱   Có lệnh khớp?       ╲
 ╲                   ╱             ╲                       ╱
  ╚══╤══════════╤════╝               ╚═══╤══════════╤══════╝
    YES         NO                      YES         NO
     │           │                       │           │
     ▼           │                       ▼           │
┌──────────┐     │                 ┌──────────┐      │
│  DIRECT  │     │                 │  DIRECT  │      │
│  MATCH   │     │                 │  MATCH   │      │
├──────────┤     │                 ├──────────┤      │
│ swap vé  │     │                 │ swap vé  │      │
│ ↔ tiền   │     │                 │ ↔ tiền   │      │
│ vault ±0 │     │                 │ vault ±0 │      │
└────┬─────┘     │                 └────┬─────┘      │
     │           │                      │            │
  ╔══╧══╗        │                   ╔══╧══╗         │
 ╱ qty   ╲       │                  ╱  qty  ╲        │
╱  còn   ╲      │                 ╱  còn    ╲       │
╲  dư?   ╱      │                 ╲  dư?    ╱       │
 ╲      ╱       │                  ╲        ╱        │
  ╚╤═══╝        │                   ╚╤══════╝        │
  YES  NO        │                  YES     NO        │
   │    └──DONE  │                   │       └──DONE  │
   │             │                   │                │
   ▼             ▼                   ▼                ▼
  ┌──────────────────────┐       ┌───────────────────────┐
  │  Tìm BUY token đối  │       │  Tìm SELL token đối   │
  │  lập @≥ (1 - price) │       │  lập @≥ (1 - price)   │
  └──────────┬───────────┘       └────────────┬──────────┘
             │                                │
  ╔══════════╧══════════╗        ╔════════════╧═══════════╗
 ╱   Có lệnh khớp?      ╲      ╱    Có lệnh khớp?         ╲
 ╲                       ╱      ╲                          ╱
  ╚══╤══════════╤═════════╝       ╚════╤═══════════╤═══════╝
    YES         NO                    YES          NO
     │           │                     │            │
     ▼           │                     ▼            │
┌──────────┐     │                ┌──────────┐      │
│   MINT   │     │                │  MERGE   │      │
├──────────┤     │                ├──────────┤      │
│ in cặp   │     │                │ burn cặp │      │
│ vé mới   │     │                │ vé cũ    │      │
│ vault +1 │     │                │ vault -1 │      │
└────┬─────┘     │                └────┬─────┘      │
     │           │                     │            │
  ╔══╧══╗        │                  ╔══╧══╗         │
 ╱  qty  ╲       │                 ╱  qty  ╲        │
╱  còn   ╲      │                ╱  còn    ╲       │
╲  dư?   ╱      │                ╲  dư?    ╱       │
 ╲      ╱       │                 ╲        ╱        │
  ╚╤════╝        │                  ╚╤══════╝        │
  YES  NO        │                  YES     NO        │
   │    └──DONE  │                   │       └──DONE  │
   │             │                   │                │
   └──────┬──────┘                   └───────┬────────┘
          │                                  │
          └─────────────┬────────────────────┘
                        ▼
           ┌────────────────────────┐
           │   Treo vào order book  │
           │   chờ lệnh đối ứng     │
           └────────────────────────┘


Sau mỗi lần khớp:

  ┌──────────────────────────────────────────────────┐
  │ Cập nhật last traded price                       │
  │                                                  │
  │  ╔══════════════════════════════╗                │
  │ ╱  Book có cả bid VÀ ask?        ╲               │
  │ ╲                                ╱               │
  │  ╚════╤══════════════════╤═══════╝               │
  │      YES                 NO                      │
  │       │                   │                      │
  │       ▼                   ▼                      │
  │ ┌───────────────┐  ┌──────────────────┐          │
  │ │ display =     │  │ display =        │          │
  │ │ (bid+ask) / 2 │  │ last traded price│          │
  │ │ (mid price)   │  │                  │          │
  │ └───────────────┘  └──────────────────┘          │
  └──────────────────────────────────────────────────┘
```

---

## Platform kiếm tiền thế nào trong CLOB?

Khác AMM (thu từ slippage/AMM fee), CLOB thu **maker/taker fee** trên mỗi giao dịch:

```
Taker fee (lệnh khớp ngay — Market Order):  0.2%
Maker fee (lệnh treo chờ — Limit Order):    0.1% (hoặc 0, để khuyến khích MM)

Ví dụ: U1 mua market 3 phiếu @0.51 SOL = 1.53 SOL
  Platform thu: 1.53 × 0.2% = 0.00306 SOL
```

**Tổng revenue = Σ (giá trị giao dịch × fee rate)**

Không phụ thuộc vào bên nào thắng. Platform trung lập 100%.

---

## Thách thức lớn nhất: Cold Start & Liquidity

Đây là lý do CLOB **khó** hơn AMM rất nhiều ở giai đoạn đầu.

### Vấn đề 1 — Không có lệnh = Không trade được

```
War mới tạo, order book trống.
User A muốn mua DOGE @0.60 → không ai bán → lệnh treo mãi → UX tệ
User A bỏ đi.
```

AMM không có vấn đề này vì pool luôn sẵn sàng khớp bất kỳ lúc nào.

### Vấn đề 2 — Spread rộng khi ít liquidity

```
Chỉ có 1 MM với spread 0.10:
  BUY @0.45 | SELL @0.55

User phải trả 0.55 cho thứ giá thực chỉ khoảng 0.50 → lãng phí 10%.
Người dùng thông minh sẽ tránh war có spread rộng.
```

### Vấn đề 3 — Cần bot/MM chuyên nghiệp

Polymarket giải quyết bằng Wintermute và các market maker lớn. Họ chạy bot 24/7, inject hàng triệu USD thanh khoản, thu phí từ spread.

Platform launchpad ở giai đoạn đầu sẽ không có điều này.

---

## Giải pháp cho Cold Start

### Giải pháp A — Platform-run MM Bot (đơn giản nhất)

Platform tự chạy 1 bot đặt lệnh 2 chiều khi war mới tạo.

```
Bot config:
  Initial spread: 0.04 (BUY @0.48, SELL @0.52)
  Depth mỗi level: 2 SOL
  Số level: 5

→ Tổng SOL platform "khóa" trong order book: 5 × 2 = 10 SOL mỗi bên
→ Bot thu lãi spread: mỗi round trip lãi 0.04 SOL/phiếu
→ Bot tự điều chỉnh giá theo flow mua bán của user
```

**Ưu điểm:** UX tốt ngay từ đầu, giống AMM về mặt trải nghiệm.
**Nhược điểm:** Platform tốn vốn khóa trong bot (nhưng không mất — chỉ locked).

### Giải pháp B — Incentivized Liquidity Providers

Platform trả thưởng (Points/phần trăm fee) cho user đặt limit order tại mức giá gần thị trường.

```
LP Reward:
  Đặt limit order trong spread ≤ 0.04: nhận 2x points
  Lệnh nằm trong top 3 best bid/ask: nhận thêm 50% fee rebate

→ User bị incentivize tự nguyện làm MM → platform không cần khóa vốn
```

**Ưu điểm:** Phi tập trung, platform không rủi ro vốn.
**Nhược điểm:** Khởi đầu chậm, cần community đủ lớn trước.

### Giải pháp C — Hybrid CLOB + AMM Fallback

Dùng CLOB khi có đủ thanh khoản, tự động switch sang AMM nếu spread vượt ngưỡng.

```
Nếu spread > 0.10: AMM pool kick in, đảm bảo luôn có giá để khớp
Nếu spread ≤ 0.10: CLOB hoạt động bình thường

→ UX không bao giờ bị "không có người bán"
→ Khi platform lớn lên, AMM fallback ít được dùng dần
```

---

## So sánh trực tiếp — cùng 1 kịch bản

**Kịch bản:** War DOGE vs PEPE — 6 tiếng, 100 user, tổng 20 SOL, DOGE thắng.

| | Pari-mutuel | AMM (k=A×B) | CLOB |
|---|---|---|---|
| **User biết payout lúc vào** | ❌ Ước tính | ✅ Biết giá, không biết giá cuối | ✅ Biết chính xác (limit order) |
| **Slippage** | ❌ N/A | ⚠️ Luôn có | ✅ Không có (nếu đủ thanh khoản) |
| **Platform cần seed/vốn** | ❌ Không | ⚠️ Cần seed nhỏ | ⚠️ Cần MM vốn (hoặc bot) |
| **Platform chịu rủi ro kết quả** | ❌ Không | ⚠️ Có (từ seed) | ✅ Không (trung lập hoàn toàn) |
| **Revenue platform** | Volume × 5% | Volume × 2% + seed P&L | Volume × 0.2–0.3% (fee thấp hơn) |
| **Cold start** | ✅ Không vấn đề | ✅ Pool luôn sẵn | ❌ Cần MM |
| **Chống thao túng giá** | ❌ Yếu | ⚠️ Trung bình (whale dịch giá) | ✅ Khó thao túng hơn |
| **Dữ liệu thú vị** | ❌ Thấp | ✅ Implied probability | ✅✅ Depth + probability + order flow |
| **Trải nghiệm user** | Đơn giản | Đơn giản | ⚠️ Phức tạp hơn (limit order UX) |
| **Độ phức tạp build** | Thấp | Trung bình | Cao |
| **Phù hợp scale** | Nhỏ → vừa | Nhỏ → vừa | Lớn |

---

## Conflict of Interest

CLOB loại bỏ hoàn toàn conflict of interest mà AMM có:

```
AMM: Platform seed → platform có vị thế trong war → nghi ngờ platform chọn token
     để underdog thắng nhằm ăn seed của bên thua

CLOB: Platform chỉ thu fee từ giao dịch → không quan tâm bên nào thắng
      → Không thể bị nghi ngờ gian lận về kết quả
```

Tuy nhiên, CLOB tạo ra **conflict of interest mới** nếu platform chạy MM bot:

```
Bot platform đặt lệnh 2 chiều → bot biết order flow → có thể front-run user
→ Giải pháp: Bot platform chỉ cung cấp thanh khoản tại giá cố định,
             không điều chỉnh theo order flow (passive MM only)
             Công bố minh bạch thuật toán bot.
```

---

## Tham số kỹ thuật — Khi nào CLOB khả thi?

### Điều kiện tối thiểu để CLOB vận hành tốt

```
Số lệnh active trong book:    ≥ 20 lệnh mỗi chiều
Spread trung bình:             ≤ 0.05 SOL (5%)
Volume trung bình mỗi war:     ≥ 50 SOL
Số user active mỗi war:        ≥ 30 người
```

### Fee structure khuyến nghị

| Loại lệnh | Fee | Lý do |
|---|---|---|
| Taker (market order) | 0.25% | Thu từ người "ăn" thanh khoản |
| Maker (limit order) | 0% hoặc −0.05% (rebate) | Khuyến khích inject liquidity |
| Cancel lệnh chưa khớp | 0 SOL | Không phạt cancel → MM thoải mái |

### So sánh revenue theo fee structure

```
Kịch bản: 20 SOL volume, mix 70% taker / 30% maker

Pari-mutuel (5%):       20 × 5%    = 1.000 SOL
AMM (2% fee):           20 × 2%    = 0.400 SOL
CLOB (0.25% taker):     14 × 0.25% = 0.035 SOL

→ CLOB kiếm ít hơn rất nhiều trên cùng volume
→ Cần volume lớn hơn ~14x so với Pari-mutuel mới kiếm tương đương
```

**Bù lại:** CLOB thu hút trader chuyên nghiệp vì fee thấp → volume có thể lớn hơn nhiều.

---

## Kiến trúc kỹ thuật — Off-chain matching, On-chain settlement

CLOB cần infrastructure phức tạp hơn AMM đáng kể:

```
[User đặt lệnh]
      ↓
[Off-chain Matching Engine]  ← Xử lý nhanh như CEX (< 100ms)
      ↓ khi khớp
[Smart Contract on Solana]   ← Settlement atomic, non-custodial
      ↓
[Vault update + Phiếu transfer]

Lệnh chưa khớp: lưu off-chain, có thể cancel bất kỳ lúc nào
Vault: luôn on-chain, không ai (kể cả platform) có thể rút trái phép
```

**Tại sao không full on-chain?**

Solana có throughput cao nhưng cost per tx vẫn phát sinh. Với CLOB, mỗi lần adjust lệnh là 1 tx — trading platform cần cancel/replace hàng trăm lệnh/giây. Full on-chain không thực tế.

Polymarket dùng đúng model này: matching off-chain trên server tốc độ cao, settlement on-chain qua Polygon.

---

## Roadmap thực tế — Khi nào nên dùng CLOB?

### Giai đoạn 1: AMM (hiện tại)
```
Điều kiện: < 500 user active, < 10 SOL/war trung bình
Lý do:     Đơn giản, cold start không vấn đề, UX tốt cho newbie
```

### Giai đoạn 2: Hybrid (scale lên)
```
Điều kiện: 500–5000 user active, war thường xuyên > 50 SOL
Lý do:     AMM vẫn là fallback, CLOB cho advanced user
           Test market maker infrastructure
```

### Giai đoạn 3: CLOB chính (mature)
```
Điều kiện: > 5000 user active, có MM bên ngoài tham gia, > 200 SOL/war
Lý do:     Fee thấp thu hút trader chuyên nghiệp và whale
           AMM fallback giữ nguyên cho war nhỏ/mới
```

---

## Tổng kết

**CLOB là mô hình ưu việt nhất về chất lượng thị trường**, nhưng đòi hỏi điều kiện vận hành phức tạp:

- **Ưu điểm nổi bật:** Không slippage với limit order (market order vẫn có slippage nếu book mỏng), platform trung lập 100%, thu hút trader chuyên nghiệp, dữ liệu thị trường phong phú nhất
- **Nhược điểm cốt lõi:** Cold start khó, cần MM/bot inject liquidity, build phức tạp, fee thấp nên cần volume lớn mới có revenue tốt
- **Phù hợp nhất khi:** Platform đã có community lớn, muốn nâng cấp lên trải nghiệm sàn chuyên nghiệp

**Polymarket đi từ AMM (LMSR) → CLOB vào cuối 2022** sau khi đã có đủ user base và thu hút được MM chuyên nghiệp. Đây là con đường tự nhiên và hợp lý nhất.

**Khuyến nghị cho Token War:** Bắt đầu với AMM (Prediction Market, `k=A×B`) → migrate sang Hybrid khi đạt 1000+ user active → full CLOB khi có MM tự nhiên tham gia.
