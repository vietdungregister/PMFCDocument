# FR-013: TRUST SCORE & TOKEN LOCK

## Tổng quan

```
TrustScore = Token Lock (45) + Creator (25) + Holder (30) = 100 điểm
```

| Trụ | Max | Tính bởi |
|-----|-----|----------|
| Token Lock | 45 | Hệ thống tự động |
| Creator | 25 | 15đ tự động + 10đ admin audit |
| Holder | 30 | Hệ thống tự động |

| Điểm | Shield |
|------|--------|
| 0 – 29 | 🥉 Bronze — Token mới |
| 30 – 59 | 🥈 Silver — Có tín hiệu tích cực |
| 60 – 100 | 🥇 Gold — Đáng tin cậy |

Không cảnh báo rủi ro. Mọi level đều tích cực.

----------

## 1. Token Lock (45 điểm)

### Chức năng

Creator khóa **token của mình** vào vault/PDA. Trong thời gian khóa, creator không thể bán phần locked. Khác với LP Lock khi graduation.

- Lock ratio: 10% – 50% balance của creator
- Lock duration: 30 – 365 ngày
- Creator có thể extend (gia hạn), claim khi hết hạn
- State: Draft → Active → Claimable → Released

### Công thức

```
tokenDays    = tokenLockAmount × durationSec
maxTokenDays = totalSupply × 50% × (365 × 86400)
lockIndex    = clamp(tokenDays / maxTokenDays, 0, 1)

S_TokenLock  = round(45 × lockIndex ^ 0.3)

Ngoại lệ:
  - Lock < 30 ngày     → 0đ
  - Đã claim/released  → 0đ
```

### Bảng tra

| Lock | Score |
|------|-------|
| 10% / 30 ngày | 13/45 |
| 10% / 90 ngày | 18/45 |
| 25% / 90 ngày | 24/45 |
| 50% / 180 ngày | 36/45 |
| 50% / 365 ngày | 45/45 |
| Đã claim | 0/45 |

### Frontend Flow

```
Chỉ creator (wallet tạo token) mới được tạo Token Lock.

Step A: Chọn Lock Duration
  Preset: 30d / 90d / 180d / 365d
  Custom: min 30d, max 365d

Step B: Chọn Lock Ratio
  Quick buttons: [10%] [25%] [50%]
  Custom: min 10%, max 50% của balance creator
  Hiển thị: Lock amount = creatorBalance × ratio

Step C: Confirm → Sign transaction → Token vào vault

Trên Token Detail:
  - Mọi user thấy: Lock status, Locked amount, Locked until
  - Creator thấy: nút Extend Lock / Claim Tokens
```

----------

## 2. Creator (25 điểm)

### Initial Buy (15 điểm)

```
≥ 1 SOL         → 15đ
0.5 – 0.99 SOL  → 10đ
0.1 – 0.49 SOL  → 5đ
< 0.1 hoặc skip → 0đ

Hệ thống check từ giao dịch on-chain đầu tiên.
```

### Admin Audit (10 điểm)

```
Creator gửi audit request → Admin review → Admin chấm 0-10đ
Một lần, cố định. Chỉ super-admin mới sửa.

Admin xem xét: profile, social, mục tiêu dự án, v.v.
Không có audit: Creator tối đa 15/25 tự động.
Audit là BONUS.
```

----------

## 3. Holder (30 điểm)

### Unique Buyers (20 điểm)

Số ví khác nhau đã từng BUY token.

```
< 5 unique buyers  → 0đ
≥ 5                → 4đ
≥ 10               → 8đ
≥ 25               → 12đ
≥ 50               → 16đ
≥ 100              → 20đ

Anti-gaming: chỉ tính buyer có tổng mua ≥ 0.01 SOL.
```

### Holder Distribution (10 điểm)

```
Top 10 holders chiếm < 30% supply → 10đ
30% – 50%                         → 5đ
> 50%                              → 0đ

Loại LP/vault wallets khỏi tính toán.
```

----------

## Scenarios

### Tại T=0 (vừa tạo token)

```
Không làm gì                              →  0   🥉 Bronze
Mua 1 SOL                                 → 15   🥉 Bronze
Mua 1 SOL + lock 10%/30d                  → 28   🥉 Bronze
Mua 1 SOL + lock 10%/90d                  → 33   🥈 Silver ✓
Mua 1 SOL + lock 25%/90d                  → 39   🥈 Silver
Mua 1 SOL + lock 50%/180d                 → 51   🥈 Silver
Mua 1 SOL + lock 50%/365d                 → 60   🥇 Gold   ✓
```

### Sau khi có community

```
Silver (39đ) + 50 unique buyers + dist đều → 65   🥇 Gold
Silver (39đ) + 25 buyers + dist + audit 8đ → 59   🥈 Silver
Silver (33đ) + 100 buyers + dist đều       → 63   🥇 Gold
Silver (39đ) + 50 buyers + dist + audit 10đ → 75  🥇 Gold
```

----------

## Anti-Gaming

```
1. Unique Buyers: chỉ tính ví có tổng mua ≥ 0.01 SOL
2. Token Lock: min 30 ngày, on-chain enforcement (vault/PDA)
3. Holder Distribution: loại LP/vault wallets
4. Initial Buy: check từ giao dịch on-chain (không fake được)
5. Admin Audit: con người review (không game được)
```

----------

## Tính toán & Cache

```
Token Lock score : mỗi giờ (batch) + khi có event lock/extend/claim
Holder score     : mỗi giờ (batch snapshot)
Creator auto     : khi initial buy ghi nhận lúc tạo token
Creator audit    : một lần khi admin chấm
Cache TTL        : ~10 phút, stale-while-revalidate
```

----------

**END OF FR-013**
