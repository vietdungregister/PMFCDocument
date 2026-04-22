# Token War — Công thức mô hình Parimutuel + Time-Tranche

---

## Tổng quan

Parimutuel thuần túy có nhược điểm: không ai muốn vào sớm vì không biết odds cuối.
Time-Tranche giải quyết bằng cách **nhân hệ số** vào số shares được cấp — vào sớm → shares nhiều hơn → nhận thưởng nhiều hơn.

---

## Tham số cấu hình

| Tham số | Ký hiệu | Mặc định | Ghi chú |
|---------|---------|----------|---------|
| Thời lượng war | `T` | 24h | tính bằng giờ |
| Phí platform | `f` | 5% | tính trên tổng pool |
| Hệ số sớm | `m_early` | 1.2 | 0h → 8h đầu |
| Hệ số bình thường | `m_normal` | 1.0 | 8h → 22h |
| Hệ số muộn | `m_late` | 0.8 | 22h → 24h (2h cuối) |

---

## Công thức

### Bước 1 — Xác định hệ số theo thời gian

```
multiplier(t) =
  m_early   nếu  0h ≤ t < 8h
  m_normal  nếu  8h ≤ t < 22h
  m_late    nếu  22h ≤ t ≤ 24h
```

---

### Bước 2 — Tính Pool Shares cho từng lệnh cược

```
shares_i = amount_i × multiplier(t_i)

  amount_i  : số SOL user i đặt cược
  t_i       : thời điểm đặt cược (giờ kể từ khi war mở)
  shares_i  : số "cổ phần" trong prize pool mà user i được cấp
```

---

### Bước 3 — Tính Prize Pool

```
total_pool  = Σ amount_i                (tổng SOL cả 2 phe, không nhân hệ số)
fee         = total_pool × f
prize_pool  = total_pool × (1 - f)
```

> Hệ số time-tranche **không** ảnh hưởng đến total_pool hay prize_pool.
> Nó chỉ quyết định tỷ lệ chia thưởng trong phe thắng.

---

### Bước 4 — Xác định phe thắng

```
PEPE_return  = (PEPE_price_end  - PEPE_price_start) / PEPE_price_start
WOJAK_return = (WOJAK_price_end - WOJAK_price_start) / WOJAK_price_start

winner = phe có return cao hơn
```

---

### Bước 5 — Tính tổng shares phe thắng

```
total_winning_shares = Σ shares_i    (chỉ tính user thuộc phe thắng)
```

---

### Bước 6 — Tính payout từng user

```
Nếu user i thuộc phe THẮNG:
  payout_i = prize_pool × (shares_i / total_winning_shares)

Nếu user i thuộc phe THUA:
  payout_i = 0
```

**Rút gọn:**

```
payout_i = prize_pool × (amount_i × multiplier(t_i)) / total_winning_shares
         = amount_i × base_rate × multiplier(t_i)

  base_rate = prize_pool / total_winning_shares
```

`base_rate` là giá trị quy đổi của 1 pool share — như nhau cho mọi user trong cùng war.

---

### Bước 7 — Tỷ lệ lợi nhuận thực tế

```
ROI_i = (payout_i - amount_i) / amount_i
      = base_rate × multiplier(t_i) - 1
```

Vào sớm (multiplier 1.2) → ROI cao hơn vào muộn (multiplier 0.8), cùng một base_rate.

---

## Ví dụ số

### Thông số war

| | Giá trị |
|--|--|
| Tổng pool | 1,000 SOL |
| Phe PEPE | 600 SOL |
| Phe WOJAK | 400 SOL |
| Fee (5%) | 50 SOL |
| Prize pool | 950 SOL |
| Kết quả | PEPE thắng |

### Phân bổ cược phe PEPE theo tranche

| Tranche | SOL đặt | Hệ số | Shares |
|---------|---------|-------|--------|
| Sớm (0–8h) | 200 SOL | 1.2 | 240 |
| Bình thường (8–22h) | 300 SOL | 1.0 | 300 |
| Muộn (22–24h) | 100 SOL | 0.8 | 80 |
| **Tổng** | **600 SOL** | — | **620 shares** |

```
base_rate = 950 / 620 = 1.532 SOL/share
```

### Payout 3 user đặt cùng 100 SOL, khác thời điểm

| User | Thời điểm | Hệ số | Shares | Payout | ROI |
|------|-----------|-------|--------|--------|-----|
| A | 2h (sớm) | 1.2 | 120 | 120 × 1.532 = **183.9 SOL** | +83.9% |
| B | 12h (bình thường) | 1.0 | 100 | 100 × 1.532 = **153.2 SOL** | +53.2% |
| C | 23h (muộn) | 0.8 | 80 | 80 × 1.532 = **122.6 SOL** | +22.6% |

### Kiểm tra tổng

```
Tổng payout PEPE = 950 SOL (prize pool) ✓
  (vì tổng shares = 620, base_rate = 950/620,
   tổng payout = 620 × 950/620 = 950 ✓)

WOJAK → 0 SOL

Platform thu: 50 SOL (fee)
```

---

## Pseudo-code

```python
def compute_shares(amount, bet_time_hours, m_early=1.2, m_normal=1.0, m_late=0.8):
    if bet_time_hours < 8:
        return amount * m_early
    elif bet_time_hours < 22:
        return amount * m_normal
    else:
        return amount * m_late

def settle(bets, winner_side, fee_rate=0.05):
    # bets: list of { user, side, amount, time_hours }

    total_pool = sum(b["amount"] for b in bets)
    prize_pool = total_pool * (1 - fee_rate)
    fee        = total_pool * fee_rate

    # tính shares cho phe thắng
    winning_bets = [b for b in bets if b["side"] == winner_side]
    for b in winning_bets:
        b["shares"] = compute_shares(b["amount"], b["time_hours"])

    total_winning_shares = sum(b["shares"] for b in winning_bets)
    base_rate = prize_pool / total_winning_shares

    payouts = {}
    for b in bets:
        if b["side"] == winner_side:
            payouts[b["user"]] = b["shares"] * base_rate
        else:
            payouts[b["user"]] = 0

    return payouts, fee
```

---

## Edge Cases

| Tình huống | Xử lý |
|------------|-------|
| Một phe không có ai đặt cược | War hủy, hoàn tiền toàn bộ |
| Cả 2 phe return bằng nhau (hòa) | Hoàn tiền toàn bộ (không thu phí) |
| User đặt đúng lúc giáp ranh tranche (t = 8h chính xác) | Tính vào tranche kế tiếp (`8h ≤ t < 22h` → m_normal) |
| Total winning shares = 0 (không ai đặt phe thắng) | Không thể xảy ra nếu war hợp lệ (có 2 phe) |
