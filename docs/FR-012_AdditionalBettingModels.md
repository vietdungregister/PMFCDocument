# Token War — Các Mô hình Bổ sung & Mô hình Đề xuất Riêng (Custom)

> **Bối cảnh:** File này bổ sung thêm cho [FR-012_BettingModels_Presentation.md](file:///c:/Users/duongvietdung/Downloads/PumpFunCloneDocument/docs/FR-012_BettingModels_Presentation.md), nơi đã phân tích 4 mô hình: Parimutuel, AMM/LMSR, CLOB Orderbook, House Betting.

---

## Tổng quan — Thêm 3 mô hình + 1 Custom

| # | Tên mô hình | Ý tưởng cốt lõi | Độ phức tạp |
|---|-------------|-----------------|-------------|
| 5 | Dynamic Parimutuel (DPM) + Bonding Curve | Parimutuel + giá động theo bonding curve | Trung bình |
| 6 | Fixed-Odds Pool (Commitment Round) | User biết odds cố định lúc đặt, gom pool | Thấp |
| 7 | Dutch Auction Betting | Odds giảm dần theo thời gian, user "chộp" lúc vừa ý | Trung bình |
| **★** | **TokenWar Hybrid (Custom)** | **DPM + Time-Weighted + Anti-Whale — thiết kế riêng** | **Trung bình** |

---

## Chấm điểm tổng hợp (bao gồm 4 mô hình cũ)

| Mô hình | Dễ build | UX người dùng | An toàn cho platform | Bảo mật | **Tổng** |
|---------|:--------:|:-------------:|:--------------------:|:-------:|:---------:|
| 1. Parimutuel           | ★★★★★ | ★★☆☆☆ | ★★★★★ | ★★★★★ | **4.3** |
| 2. AMM/LMSR             | ★★★☆☆ | ★★★★☆ | ★★★☆☆ | ★★★★☆ | **3.5** |
| 3. CLOB Orderbook       | ★☆☆☆☆ | ★★★★☆ | ★★★★★ | ★★★☆☆ | **3.3** |
| 4. House betting         | ★★★★☆ | ★★★★★ | ★☆☆☆☆ | ★★☆☆☆ | **3.0** |
| 5. DPM + Bonding Curve  | ★★★☆☆ | ★★★★☆ | ★★★★☆ | ★★★★☆ | **3.8** |
| 6. Fixed-Odds Pool      | ★★★★★ | ★★★★☆ | ★★★★★ | ★★★★☆ | **4.5** |
| 7. Dutch Auction Betting | ★★★☆☆ | ★★★☆☆ | ★★★★★ | ★★★★☆ | **3.8** |
| **★ TokenWar Hybrid**   | **★★★★☆** | **★★★★★** | **★★★★★** | **★★★★★** | **★ 4.8** |

---

## Mô hình 5: Dynamic Parimutuel Market (DPM) + Bonding Curve

### Ý tưởng
> Kết hợp Parimutuel (gom nồi, bên thắng chia tiền bên thua) với **bonding curve** (giá vé tăng dần khi có nhiều người mua). User MUA VÉ, giá vé thay đổi tự động — **mua sớm được giá rẻ, mua muộn giá đắt**.

Khác với Parimutuel truyền thống (ai cũng cùng giá), DPM tạo ra **dynamic pricing** — mỗi vé mua ở mức giá khác nhau.

### Cách hoạt động

```
Bước 1: War mở — PEPE vs WOJAK (24h)
        Pool ban đầu: 0 SOL
        Giá vé PEPE: 0.01 SOL (rẻ nhất)
        Giá vé WOJAK: 0.01 SOL

        Bonding Curve: Giá vé thứ N = 0.01 × (1 + N/100) SOL
        (Mỗi vé mới đắt hơn vé cũ 1%)

Bước 2: Alice mua 10 vé PEPE
        Trả: ~0.115 SOL (tổng 10 vé, giá tăng dần)
        Pool: 0.115 SOL

Bước 3: Bob mua 10 vé WOJAK
        Trả: ~0.115 SOL
        Pool: 0.23 SOL

Bước 4: Charlie mua 20 vé PEPE (muộn hơn)
        Giá vé PEPE bắt đầu từ 0.011 SOL (đã có 10 vé trước)
        Trả: ~0.28 SOL (đắt hơn Alice nhiều)
        Pool: 0.51 SOL

Bước 5: War kết thúc — PEPE thắng
        Platform fee: 3% = 0.015 SOL
        Nồi chia: 0.495 SOL

        Chia theo SỐ VÉ (không phải số SOL bỏ vào):
        Alice: 10 vé / 30 vé PEPE = 33% → 0.165 SOL (lãi 43%)
        Charlie: 20 vé / 30 vé PEPE = 67% → 0.33 SOL (lãi 18%)

        → Alice mua sớm, giá rẻ hơn → % lãi cao hơn Charlie
```

### Ưu điểm
- ✅ **Khuyến khích vào sớm** — incentive tự nhiên, không cần thêm mechanism
- ✅ Platform không chịu rủi ro (chỉ ăn fee)
- ✅ User thấy giá vé thay đổi → cảm giác thị trường sống động
- ✅ Không cần seed

### Nhược điểm
- ❌ User vẫn **không biết chính xác payout cuối** (giống Parimutuel)
- ❌ Bonding curve cần thiết kế kỹ — nếu slope quá dốc, vé cuối quá đắt
- ❌ Phức tạp hơn Parimutuel thuần (cần bonding curve logic)

### So sánh với Parimutuel thuần

| | Parimutuel | DPM + Bonding Curve |
|--|-----------|---------------------|
| Giá vé | Cố định (ai cũng trả như nhau) | Tăng dần (mua sớm rẻ hơn) |
| Incentive vào sớm | Không có | Rất mạnh |
| User biết payout | ❌ | ❌ (nhưng biết giá vé) |
| Độ phức tạp | Thấp | Trung bình |
| Anti-whale | Yếu | Tốt hơn (whale mua nhiều → giá tăng nhanh) |

---

## Mô hình 6: Fixed-Odds Pool (Commitment Round)

### Ý tưởng
> Platform chia war thành **nhiều round ngắn**, mỗi round có **odds cố định**. User biết chính xác sẽ ăn bao nhiêu khi đặt cược. Odds thay đổi giữa các round dựa trên tỷ lệ cược round trước.

Giống bet thể thao truyền thống, nhưng **không có nhà cái** — tiền vẫn gom vào pool.

### Cách hoạt động

```
War: PEPE vs WOJAK — 24h, chia 4 round (mỗi round 6h)

══════════════════════════════════════════════════
Round 1 (0-6h) — Odds mở đầu: PEPE 2.0x | WOJAK 2.0x (50/50)

  Alice cược 1 SOL vào PEPE @ 2.0x
    → Nếu PEPE thắng: Alice nhận 2.0 SOL (biết chắc!)
  Bob cược 2 SOL vào WOJAK @ 2.0x
    → Nếu WOJAK thắng: Bob nhận 4.0 SOL

  Pool Round 1: PEPE 1 SOL | WOJAK 2 SOL
  → WOJAK được cược nhiều hơn

══════════════════════════════════════════════════
Round 2 (6-12h) — Odds điều chỉnh dựa trên Round 1

  WOJAK được đặt nhiều → giảm odds WOJAK, tăng odds PEPE
  Odds mới: PEPE 2.5x | WOJAK 1.6x

  Charlie cược 1 SOL vào PEPE @ 2.5x
    → Nếu PEPE thắng: Charlie nhận 2.5 SOL
  Dave cược 1 SOL vào WOJAK @ 1.6x
    → Nếu WOJAK thắng: Dave nhận 1.6 SOL

══════════════════════════════════════════════════
Round 3-4: Tương tự, odds tiếp tục điều chỉnh

══════════════════════════════════════════════════
Kết thúc — PEPE thắng!

  Platform trả theo odds đã lock:
    Alice:   1 × 2.0 = 2.0 SOL ← odds Round 1  ✅
    Charlie: 1 × 2.5 = 2.5 SOL ← odds Round 2  ✅
    Bob:     0 SOL (thua)
    Dave:    0 SOL (thua)

  Platform fee: 3% trên tổng pool
  Pool: 1 + 2 + 1 + 1 = 5 SOL
  Chi trả: 2.0 + 2.5 = 4.5 SOL
  Platform giữ: 5 - 4.5 = 0.5 SOL (10%!)
```

### Vấn đề: Platform có thể lỗ?

```
Worst case: Tất cả cược cùng 1 bên ở odds cao → Chi trả > Pool

Ví dụ: 10 người cược PEPE @ 2.0x, 0 người cược WOJAK
  Pool = 10 SOL
  Nếu PEPE thắng: trả 20 SOL ← VỠ NỢ!

Giải pháp: Tự động cân bằng odds
  → Khi 1 bên được cược quá nhiều, odds bên đó giảm
  → Giới hạn: Odds bên A × Tổng cược bên A ≤ 90% tổng pool
  → Nếu vượt: đóng nhận cược bên A cho đến round tiếp
```

### Ưu điểm
- ✅ **User biết chính xác payout** (giải quyết nhược điểm lớn nhất của Parimutuel)
- ✅ Đơn giản — dễ hiểu, dễ build
- ✅ Rounds tạo nhiều thời điểm engagement

### Nhược điểm
- ❌ **Platform có rủi ro** nếu odds không cân bằng tốt (cần thuật toán adjust tốt)
- ❌ Ít "thị trường" hơn — không có mua bán phiếu liên tục
- ❌ Round bị đóng sớm nếu 1 bên bị cược quá nhiều → UX không tốt

---

## Mô hình 7: Dutch Auction Betting

### Ý tưởng
> Odds bắt đầu **rất cao** (hấp dẫn) và **giảm dần** theo thời gian. User tự chọn thời điểm "chốt" — vào sớm được odds tốt nhưng rủi ro cao (ít thông tin), vào muộn odds thấp nhưng có nhiều thông tin hơn.

Giống đấu giá Hà Lan: giá giảm dần cho đến khi có người chấp nhận.

### Cách hoạt động

```
War: PEPE vs WOJAK — 24h

Odds giảm liên tục theo thời gian:

Thời điểm    │  Odds PEPE  │  Odds WOJAK  │  Ghi chú
─────────────┼─────────────┼──────────────┼────────────
0h (mở cửa) │   5.0x      │    5.0x      │  High risk, high reward
3h           │   4.0x      │    4.0x      │
6h           │   3.0x      │    3.0x      │  Trung bình
12h          │   2.5x      │    2.5x      │
18h          │   2.0x      │    2.0x      │  Thấp hơn
23h          │   1.5x      │    1.5x      │  Gần kết thúc, ít lời
24h          │   War kết thúc              │

Odds cũng bị điều chỉnh bởi tỷ lệ cược:
  Nếu PEPE nhận nhiều cược hơn → Odds PEPE giảm nhanh hơn
  → Odds WOJAK giảm chậm hơn (vì ít được chọn → underdog)

Ví dụ:
  T=1h: Alice cược 1 SOL vào PEPE @ 4.8x → Nếu thắng: +3.8 SOL
  T=6h: Bob cược 1 SOL vào WOJAK @ 3.2x → Nếu thắng: +2.2 SOL
  T=20h: Charlie cược 1 SOL vào PEPE @ 1.7x → Nếu thắng: +0.7 SOL

  Pool tổng: 3 SOL
  PEPE thắng → trả Alice 4.8 + Charlie 1.7 = 6.5 SOL

  → Pool không đủ! (3 SOL < 6.5 SOL)
```

### Giải pháp cân bằng pool

```
Phương án A — Cap tổng liability (như House Betting):
  Tổng chi trả tối đa = 95% Pool hiện tại
  → Khi gần cap: odds giảm nhanh về 1.0x (không nhận thêm)

Phương án B — Hybrid Parimutuel:
  Odds chỉ là "tỷ lệ chia pool" thay vì cam kết cố định
  → Alice mua ở odds 4.8x → nhận 4.8 "shares"
  → Charlie mua ở odds 1.7x → nhận 1.7 "shares"
  → Tổng shares PEPE = 6.5, tổng pool = 2.85 SOL (sau fee)
  → Alice nhận: (4.8 / 6.5) × 2.85 = 2.10 SOL
  → Charlie nhận: (1.7 / 6.5) × 2.85 = 0.745 SOL
  → Vẫn incentive vào sớm, nhưng pool không bao giờ vỡ
```

### Ưu điểm
- ✅ **Gamification cực mạnh** — "chốt odds" tạo cảm giác hồi hộp
- ✅ Tạo FOMO tự nhiên — odds tốt giảm dần, user muốn vào sớm
- ✅ Platform an toàn (nếu dùng Hybrid Parimutuel)

### Nhược điểm
- ❌ Nếu dùng fixed odds → platform chịu rủi ro (như House Betting)
- ❌ Nếu dùng hybrid → user không thực sự biết chính xác payout
- ❌ Odds giảm liên tục → user cuối cùng không muốn chơi (tỷ lệ quá thấp)

---

## ★ Mô hình Custom: TokenWar Hybrid

### Triết lý thiết kế

> Lấy nền Parimutuel (platform an toàn 100%), kết hợp Time-Weighted Shares từ DPM (khuyến khích vào sớm), thêm cơ chế Anti-Whale và hiển thị "Estimated Odds" cho user.

**Mục tiêu:**
1. Platform **KHÔNG BAO GIỜ** chịu rủi ro tài chính (không seed, không nhà cái)
2. User thấy **odds ước tính** lúc đặt cược (giải quyết nhược điểm lớn nhất của Parimutuel)
3. **Vào sớm = lời nhiều hơn** (incentive tự nhiên)
4. **Chống whale** dump cược đè bên cuối war
5. Đơn giản để build — **không cần bonding curve, orderbook, hay seed**

---

### Cơ chế core: Time-Weighted Pool Shares (TWPS)

```
Quy tắc:
  Cược vào thời điểm T (% thời gian war đã trôi) → nhận SHARES = SOL × Multiplier(T)

  Multiplier(T) = max(0.5, 1.5 − T)

  ┌─────────────────────────────────────────────┐
  │  T = 0%   (mới mở)   → Multiplier = 1.50   │
  │  T = 25%  (¼ war)    → Multiplier = 1.25   │
  │  T = 50%  (nửa war)  → Multiplier = 1.00   │
  │  T = 75%  (¾ war)    → Multiplier = 0.75   │
  │  T = 100% (sắp hết)  → Multiplier = 0.50   │
  └─────────────────────────────────────────────┘

  → Cược 1 SOL lúc đầu war → 1.5 shares
  → Cược 1 SOL lúc giữa war → 1.0 shares
  → Cược 1 SOL lúc cuối war → 0.5 shares
```

### Anti-Whale: Progressive Fee

```
Fee cơ bản: 3%
Fee bổ sung khi bet lớn:
  Bet ≤ 1 SOL    → 3%
  Bet 1-5 SOL    → 3% + 1% = 4%
  Bet 5-10 SOL   → 3% + 3% = 6%
  Bet > 10 SOL   → 3% + 5% = 8%

→ Whale vẫn chơi được, nhưng phải trả phí cao hơn
→ Retail user được bảo vệ, fee thấp
→ Platform thu được nhiều hơn từ whale

Hoặc giới hạn tối đa mỗi lệnh: max 5% tổng pool hiện tại
```

### Estimated Odds — Hiển thị trực quan

```
Tại thời điểm T, user thấy:

  ┌─────────────────────────────────────────┐
  │  🔥 PEPE vs WOJAK — còn 8h             │
  │                                         │
  │  Pool:  PEPE 45 SOL  |  WOJAK 30 SOL   │
  │                                         │
  │  Estimated payout nếu cược 1 SOL:      │
  │                                         │
  │  PEPE thắng → ~1.56 SOL  (+56%)        │
  │  WOJAK thắng → ~2.13 SOL (+113%)       │
  │                                         │
  │  ⚡ Bonus Early Bird: +25% Shares       │
  │                                         │
  │  ⚠️ Lưu ý: Payout thay đổi khi có     │
  │     người cược thêm                     │
  │                                         │
  │  [  CƯỢC PEPE  ]    [  CƯỢC WOJAK  ]   │
  └─────────────────────────────────────────┘

Công thức estimated payout:
  Tổng pool (sau fee) × (Shares bạn / Tổng shares bên bạn)
```

---

### Ví dụ đầy đủ

```
War: PEPE vs WOJAK — 24h, fee cơ bản 3%

══════════════════════════════════════════════════
T=2h (8% war): Multiplier = 1.42

  Alice cược 2 SOL vào PEPE
    Fee: 3% → 0.06 SOL
    SOL vào pool: 1.94 SOL
    Shares nhận: 1.94 × 1.42 = 2.75 shares PEPE

  Bob cược 1 SOL vào WOJAK
    Fee: 3% → 0.03 SOL
    SOL vào pool: 0.97 SOL
    Shares nhận: 0.97 × 1.42 = 1.38 shares WOJAK

  Pool: PEPE 1.94 SOL (2.75 shares) | WOJAK 0.97 SOL (1.38 shares)
  Tổng pool: 2.91 SOL

══════════════════════════════════════════════════
T=12h (50% war): Multiplier = 1.00

  Charlie cược 3 SOL vào PEPE
    Fee: 3% → 0.09 SOL
    SOL vào pool: 2.91 SOL
    Shares nhận: 2.91 × 1.00 = 2.91 shares PEPE

  Diana cược 5 SOL vào WOJAK
    Fee: 4% (bet 1-5 SOL) → 0.20 SOL
    SOL vào pool: 4.80 SOL
    Shares nhận: 4.80 × 1.00 = 4.80 shares WOJAK

  Pool: PEPE 4.85 SOL (5.66 shares) | WOJAK 5.77 SOL (6.18 shares)
  Tổng pool: 10.62 SOL

══════════════════════════════════════════════════
T=20h (83% war): Multiplier = 0.67

  Eve cược 2 SOL vào PEPE
    Fee: 3% → 0.06 SOL
    SOL vào pool: 1.94 SOL
    Shares nhận: 1.94 × 0.67 = 1.30 shares PEPE

  Pool cuối: PEPE 6.79 SOL (6.96 shares) | WOJAK 5.77 SOL (6.18 shares)
  Tổng pool: 12.56 SOL
  Tổng fee platform: 0.06 + 0.03 + 0.09 + 0.20 + 0.06 = 0.44 SOL

══════════════════════════════════════════════════
SETTLEMENT — PEPE THẮNG

  Nồi chia: 12.56 SOL (toàn bộ pool — fee đã trừ trước)
  Chia theo shares PEPE:

  Alice:   2.75 / 6.96 × 12.56 = 4.96 SOL  (bỏ 2 SOL → lãi 2.96 SOL = +148%) ⭐
  Charlie: 2.91 / 6.96 × 12.56 = 5.25 SOL  (bỏ 3 SOL → lãi 2.25 SOL = +75%)
  Eve:     1.30 / 6.96 × 12.56 = 2.35 SOL  (bỏ 2 SOL → lãi 0.35 SOL = +17.5%)

  Bob:     0 SOL (thua, mất 1 SOL)
  Diana:   0 SOL (thua, mất 5 SOL)

  Platform: 0.44 SOL fee ← thu chắc chắn, không phụ thuộc kết quả

══════════════════════════════════════════════════
Kiểm tra:
  4.96 + 5.25 + 2.35 = 12.56 SOL ✓
  Alice vào sớm → lãi % cao nhất
  Eve vào muộn → lãi ít nhất (cùng bỏ 2 SOL nhưng lời 17.5% thay vì 148%)
```

---

### Bảng so sánh tổng hợp tất cả mô hình

| Tiêu chí | Parimutuel | AMM | CLOB | House | DPM | Fixed-Odds | Dutch | **★ TokenWar Hybrid** |
|----------|:---------:|:---:|:----:|:-----:|:---:|:----------:|:-----:|:-------------------:|
| Platform chịu rủi ro | ❌ | ⚠️ Seed | ❌ | ❌ Rất cao | ❌ | ⚠️ Có thể | ⚠️ Tùy | **❌ Không bao giờ** |
| Cần seed/vốn | ❌ | ⚠️ | ⚠️ MM | ❌ | ❌ | ❌ | ❌ | **❌** |
| User biết payout | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅/❌ | **⚠️ Estimated** |
| Incentive vào sớm | ❌ | ✅ Nhẹ | ❌ | ❌ | ✅ Mạnh | ✅ Nhẹ | ✅ Rất mạnh | **✅ Rất mạnh** |
| Anti-whale | ❌ | ⚠️ Slippage | ✅ | ❌ | ⚠️ | ❌ | ❌ | **✅ Progressive fee** |
| Dễ build | ★★★★★ | ★★★ | ★ | ★★★★ | ★★★ | ★★★★★ | ★★★ | **★★★★** |
| Dễ hiểu cho user | ★★★★ | ★★★ | ★★ | ★★★★★ | ★★★ | ★★★★ | ★★★ | **★★★★** |
| Gamification | ★★ | ★★★ | ★★ | ★★ | ★★★★ | ★★★ | ★★★★★ | **★★★★★** |

---

### Tại sao chọn TokenWar Hybrid?

```
1. AN TOÀN TUYỆT ĐỐI
   = Parimutuel (tiền bên thua → bên thắng)
   + Platform chỉ ăn fee, KHÔNG seed, KHÔNG nhà cái
   + KHÔNG BAO GIỜ vỡ pool

2. GAMIFICATION TỐI ĐA
   = Time-weighted shares (Early Bird bonus tự nhiên)
   + Estimated odds hiển thị trực quan
   + Progressive fee tạo fairness

3. ĐƠN GIẢN ĐỂ BUILD
   = Parimutuel core (đã biết cách build)
   + Thêm 1 multiplier tuyến tính (vài dòng code)
   + Thêm 1 bảng fee tier (vài dòng code)
   + KHÔNG cần: bonding curve, orderbook, matching engine, MM bot, seed fund

4. MỞ RỘNG DỄ DÀNG
   Giai đoạn 1: TokenWar Hybrid (như mô tả trên)
   Giai đoạn 2: Thêm Early Exit (bán shares trước khi war kết thúc — AMM nhỏ)
   Giai đoạn 3: Thêm Secondary Market (CLOB cho shares)
```

---

### Tham số đề xuất cho Token War Hybrid

| Tham số | Giá trị đề xuất | Ghi chú |
|---------|-----------------|---------|
| Fee cơ bản | 3% | Cân bằng giữa revenue và UX |
| Fee whale (>5 SOL) | 6% | Anti-whale |
| Fee whale (>10 SOL) | 8% | Hạn chế whale last-minute |
| Time multiplier | `max(0.5, 1.5 - T)` | T = % war đã trôi |
| Min bet | 0.01 SOL | Accessible |
| Max bet per tx | 5% tổng pool hiện tại | Anti-manipulation |
| War duration | 24h | Đủ dài để có volume |
| Hiển thị pool | Real-time | Minh bạch |
| Hiển thị estimated odds | Real-time | UX tốt |

---

### Rủi ro và Mitigation

| Rủi ro | Mức độ | Mitigation |
|--------|--------|-----------|
| Pool một bên quá lớn → bên thắng ít lời | Trung bình | Hiển thị cảnh báo khi tỷ lệ > 80/20 |
| Whale split nhiều ví để tránh progressive fee | Thấp | Giới hạn max bet per tx = 5% pool |
| Creator token thao túng kết quả | Cao | Chọn token bằng thuật toán, không cho creator tham gia war token mình |
| War ít volume → payout không hấp dẫn | Trung bình | Minimum pool threshold: war chỉ "activate" khi pool ≥ 5 SOL mỗi bên |
| User cuối cùng vào bên ít người → odd thay đổi nhiều | Thấp | Multiplier 0.5x cuối war → impact của late bet giảm 50% |

