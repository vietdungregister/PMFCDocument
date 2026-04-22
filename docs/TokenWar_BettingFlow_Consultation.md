# Token War — Luồng Đi Hệ Thống Bet (Simplified CLOB)

> **Định hướng:** CLOB (giống Polymarket hiện tại) nhưng đơn giản hóa cho Token War. Phí 5% mỗi giao dịch. Tài liệu này chỉ nói về **luồng đi** — chưa đề cập code hay kỹ thuật.

---

## CLOB là gì — giải thích bằng ngôn ngữ thường

CLOB = **Sổ lệnh**. Hoạt động như sàn chứng khoán mini:

- Người mua đặt giá họ sẵn lòng trả → **lệnh mua (bid)**
- Người bán đặt giá họ sẵn lòng bán → **lệnh bán (ask)**
- Khi bid ≥ ask → **khớp lệnh** → giao dịch xảy ra

Không có công thức toán học tự động định giá (như AMM). **Giá do con người đặt và thương lượng với nhau.**

---

## Khái niệm cốt lõi

```
Phiếu A:  "Tôi tin Token A thắng"
           → Nếu A thắng: đổi 1 SOL / phiếu
           → Nếu A thua : đổi 0 SOL / phiếu

Phiếu B:  "Tôi tin Token B thắng"
           → tương tự

Tính chất: Giá phiếu A + Giá phiếu B = 1 SOL (luôn luôn)
           Vì chắc chắn một bên thắng → tổng payout = 1 SOL

Ví dụ:    Phiếu A = 0.65 SOL → thị trường tin A thắng 65%
           Phiếu B = 0.35 SOL → thị trường tin B thắng 35%
```

**Vault (két tiền):** Giữ toàn bộ SOL. Mỗi cặp phiếu lưu hành = đúng 1 SOL trong vault → hệ thống không bao giờ vỡ nợ.

---

## Tổng quan luồng đi

```
┌─────────────┐    ┌──────────────┐    ┌───────────────────┐    ┌─────────────┐
│  ① Mở War   │ →  │  ② MM Bot    │ →  │  ③ Giao dịch      │ →  │  ④ Kết thúc │
│  Khởi tạo   │    │  Tạo thanh   │    │  (thời gian war)  │    │  Thanh toán │
│             │    │  khoản đầu   │    │                   │    │             │
└─────────────┘    └──────────────┘    └───────────────────┘    └─────────────┘
```

---

## ① Mở War

Admin tạo trận A vs B:

```
War: DOGE vs PEPE
Thời lượng: 6 tiếng
Mệnh giá: 1 SOL / phiếu thắng
Phí: 5% / giao dịch

Sổ lệnh ban đầu: TRỐNG
Vault: 0 SOL
```

Sổ lệnh trống → chưa ai mua bán được → cần bước 2.

---

## ② MM Bot — Tạo thanh khoản ban đầu

> **Vấn đề cold start của CLOB:** Sổ lệnh trống → user vào không mua được gì → bỏ đi. Đây là lý do Polymarket phải có Market Maker chuyên nghiệp (Wintermute v.v.). Với Token War, ta dùng **bot tự động của platform**.

### Bot làm gì?

Bot đặt lệnh **2 chiều** tại mức 50/50 (chưa ai biết ai thắng):

```
Sổ lệnh DOGE ngay khi war mở (do bot đặt):

  SELL (ask):  0.52 (5 phiếu) | 0.53 (5 phiếu) | 0.55 (10 phiếu)
  ─────────────────────────────────────────── MID PRICE: 0.50
  BUY  (bid):  0.48 (5 phiếu) | 0.47 (5 phiếu) | 0.45 (10 phiếu)

Spread ban đầu: 0.04 SOL (bot bán @0.52, mua @0.48)
```

### Cách bot "bán" phiếu mà không cần có phiếu trước

Đây là điểm thú vị:

```
Bot đặt SELL DOGE @0.52 ≡ cam kết "Tôi sẵn lòng giữ PEPE nếu bạn giữ DOGE"

Khi có người mua DOGE @0.52:
  → Hệ thống Mint cặp phiếu mới:
      Người mua trả 0.52 SOL → nhận Phiếu DOGE
      Bot trả        0.48 SOL → nhận Phiếu PEPE
      Vault nhận     1.00 SOL tổng

  → Bot không cần có phiếu trước — họ chỉ cam kết bỏ tiền vào bên kia.
```

Bot kiếm tiền từ spread: mua DOGE @0.48, bán @0.52 → lãi 0.04 / phiếu.

### Độ phức tạp của bot: giữ đơn giản

Ở giai đoạn đầu, **bot KHÔNG** cần thông minh:

```
Giản dị nhất: Bot chỉ giữ lệnh tại giá cố định 50/50, không điều chỉnh.
  → User mua hết @0.52 → giá nhảy lên 0.53 (level tiếp theo của bot)
  → Bot không tự chạy theo giá mới

Kết quả: Giá phản ánh thực tế hành vi mua của user, không bị bot can thiệp.
         Platform không bị nghi ngờ thao túng giá.
```

---

## ③ Giao dịch — War chính thức (6 tiếng)

### Luồng 3A: Mua phiếu (Market Order — khớp ngay)

User muốn mua DOGE ngay, không cần chờ:

```
Trạng thái sổ lệnh DOGE:
  SELL: 0.52 (5 phiếu) | 0.53 (5 phiếu) | ...
  BUY:  0.48 (5 phiếu) | ...

User muốn mua 3 phiếu DOGE ngay lập tức (Market Order):
  → Hệ thống khớp với SELL thấp nhất (best ask = 0.52)
  → 3 phiếu @0.52 → Mint xảy ra 3 lần

  User trả:    3 × 0.52 = 1.56 SOL (trước phí)
  Phí 5%:      1.56 × 5% = 0.078 SOL → platform thu
  User trả thực: 1.56 + 0.078 = 1.638 SOL
  User nhận:   3 phiếu DOGE

  Nếu DOGE thắng → 3 × 1 SOL = 3.00 SOL (lãi từ 1.56, không tính phí)
  Nếu DOGE thua  → 0 SOL

Sổ lệnh sau:
  SELL: 0.52 (2 còn lại) | 0.53 (5) | ...
```

### Luồng 3B: Mua phiếu (Limit Order — đặt giá mong muốn)

User muốn mua giá tốt hơn, chấp nhận chờ:

```
Giá hiện tại: DOGE @0.52 (best ask)

User đặt: BUY 5 phiếu DOGE @0.50 SOL (Limit Order)
  → 0.50 < 0.52 (best ask) → KHÔNG khớp ngay
  → Lệnh treo trong sổ:
    BUY: 0.50 (5 phiếu User) | 0.48 (5 phiếu bot) | ...

  Lệnh này khớp khi:
    - Có người SELL DOGE @0.50 hoặc thấp hơn, HOẶC
    - Bot hạ giá xuống 0.50 (không xảy ra với passive bot)

  War kết thúc mà chưa khớp → lệnh huỷ, user lấy lại SOL đã lock.
```

> **Note UX quan trọng:** Phần lớn user thường người dùng sẽ dùng **Market Order** (ấn nút "Mua DOGE ngay"). Limit Order là tính năng nâng cao. Với giai đoạn đầu, **chỉ cần Market Order là đủ**.

### Luồng 3C: Bán phiếu (Thoát sớm)

Đây là điểm khác biệt then chốt với Pari-mutuel. User **có thể exit bất kỳ lúc nào** mà không cần đợi kết thúc war.

```
User đang giữ 3 phiếu DOGE (mua lúc 0.52)
Giá DOGE hiện tại: 0.72 SOL (sentiment nghiêng về DOGE)

User quyết định chốt lời:
  Bán 3 phiếu DOGE (Market Order → sell vào bid cao nhất)

  Best bid: 0.71 SOL (người khác muốn mua DOGE @0.71)
  → Khớp: Direct Match (không Mint, không Burn — chỉ chuyển phiếu)

  User nhận:  3 × 0.71 = 2.13 SOL (trước phí)
  Phí 5%:     2.13 × 5% = 0.107 SOL
  User nhận thực: 2.023 SOL

  Vốn ban đầu: 3 × 0.52 = 1.56 SOL
  Lời: +0.463 SOL — chốt ngay, không cần đợi DOGE thắng hay thua.
```

**Tại sao user bán sớm?**
- Đã lãi, không muốn rủi ro thêm
- Sentiment đang xoay chiều
- Cần tiền cho war khác

**Tại sao user giữ đến cuối?**
- Tin chắc bên mình thắng → mỗi phiếu = 1 SOL > 0.71 SOL bán bây giờ
- Margin cuối cao hơn nếu đúng

### 3 Loại giao dịch trong CLOB — đơn giản hoá

```
Loại 1 — DIRECT MATCH (ưu tiên đầu tiên)
  Người giữ phiếu DOGE muốn bán ↔ Người mới muốn mua DOGE
  → Phiếu chuyển tay trực tiếp, vault không thay đổi

Loại 2 — MINT (khi không có Direct Match)
  Không ai có phiếu DOGE để bán → Bot (hoặc người) BUY PEPE đối ứng
  → Hệ thống in cặp phiếu mới, vault nhận 1 SOL

Loại 3 — MERGE (khi bán không có Direct Match)
  Người giữ DOGE và người giữ PEPE đều muốn thoát đồng thời
  → Hệ thống burn cặp phiếu, trả SOL từ vault

Vault LUÔN cân bằng:
  Mỗi cặp phiếu lưu hành = 1 SOL trong vault → không bao giờ vỡ nợ.
```

### Giá thay đổi thế nào?

```
Giá DOGE = best ask hiện tại (giá rẻ nhất đang mời bán DOGE)
Giá hiển thị = midpoint = (best bid + best ask) / 2

Khi có nhiều lệnh MUA DOGE:
  → Best ask bị ăn hết dần → price walk up
  → Giá DOGE tăng, giá PEPE tự động = 1 − giá DOGE giảm

Khi có nhiều lệnh BÁN DOGE:
  → Best bid bị ăn hết dần → price walk down
  → Giá DOGE giảm, giá PEPE tăng
```

**Ví dụ diễn biến giá trong 6 tiếng:**

```
Giờ    DOGE     Sự kiện
────────────────────────────────────────────
0:00   0.50     War bắt đầu
0:30   0.58     Nhiều người mua DOGE
1:00   0.48     Tin bất lợi cho DOGE → PEPE được mua mạnh
2:00   0.52     Cân bằng lại
4:00   0.70     DOGE áp đảo
6:00   ████     War kết thúc
```

Biểu đồ giá này chính là **"trận đấu" thực sự** user theo dõi trong suốt war.

---

## ④ Kết thúc — Thanh toán

```
War kết thúc, tiêu chí xác định winner được công bố.
Giả sử DOGE thắng:

  → Phiếu DOGE = 1 SOL mỗi phiếu (đổi tự động)
  → Phiếu PEPE = 0 SOL (mất giá trị)

  Lệnh limit chưa khớp khi war kết thúc:
    → Huỷ lệnh, hoàn SOL đã lock (100%, không thu phí)

  Platform thu phí: đã thu từng giao dịch trong suốt war
  Vault: trả hết cho người thắng, cân bằng về 0
```

---

## Đơn giản hóa so với Polymarket đầy đủ

| Tính năng | Polymarket đầy đủ | Phiên bản đơn giản cho Token War |
|---|---|---|
| Market Order | ✅ | ✅ Bắt buộc có |
| Limit Order | ✅ | ⚙️ Có nhưng ẩn, là advanced |
| Order Book UI | ✅ Hiển thị đầy đủ | ❌ Ẩn — chỉ hiện giá + % |
| Market Maker | Wintermute (chuyên nghiệp) | Bot platform passive (đơn giản) |
| Matching Engine | Off-chain tốc độ cao | Off-chain đơn giản |
| Settlement | On-chain Polygon | On-chain Solana |

**Triết lý UX:** User thấy giao diện giống **swap DEX** — chỉ ấn "Mua DOGE" / "Mua PEPE" và thấy giá. Toàn bộ CLOB hoạt động phía sau.

```
Giao diện user thấy:

  ┌─────────────────────────────────────┐
  │  DOGE vs PEPE                       │
  │                                     │
  │  DOGE: 0.62 SOL (62%)    ▲ tăng    │
  │  PEPE: 0.38 SOL (38%)    ▼ giảm    │
  │                                     │
  │  Tôi muốn đặt: [1.00] SOL          │
  │                                     │
  │  [  MUA DOGE  ]   [  MUA PEPE  ]   │
  │                                     │
  │  Nếu DOGE thắng → nhận ~1.53 SOL   │
  │  (sau phí 5%)                       │
  └─────────────────────────────────────┘
```

---

## Revenue Platform

```
Thu phí 5% trên mỗi giao dịch (mua hoặc bán).
Bất kể bên nào thắng → platform luôn có fee.
Platform không bỏ tiền seed → không chịu rủi ro từ kết quả war.

Duy nhất 1 rủi ro: Bot MM của platform cầm phiếu.
  → Bot giữ phiếu và bên đó thua → bot lỗ phần đó.
  → Giới hạn bằng cách bot chỉ đặt lệnh nhỏ (2-5 SOL tổng cộng / war).
```

---

## Những câu hỏi cần quyết định tiếp theo

| # | Câu hỏi | Ảnh hưởng |
|---|---------|-----------|
| 1 | **Tiêu chí thắng thua** là gì? | Buy volume trên DEX? MC? Oracle bên ngoài? |
| 2 | **Giai đoạn 1 có cần Limit Order không?** | Chỉ Market Order đơn giản hơn nhiều để build |
| 3 | **Phí 5% thu khi mua, bán, hay cả hai?** | Cả hai = 10% round trip. Chỉ mua = 5% |
| 4 | **Bot MM đặt bao nhiêu SOL?** | Quyết định độ deep của thanh khoản ban đầu |
| 5 | **Nếu bot bị "tấn công" (whale mua hết lệnh bot)?** | Cần chiến lược bot refill hay để tự nhiên? |
