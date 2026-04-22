# DiscoverScore

## Công thức

```
DiscoverScore = BuyVolume24h × (1 + PriceChange24h / 100) + TrustBonus
```

## TrustBonus

| Badge | Bonus |
|---|---|
| Không có | +0 |
| 1 badge | +10 |
| 2 badges | +20 |
| 3 badges | +30 |

*(3 badges: LP Lock, Audit, Freeze Disabled)*

---

## Ví dụ

| Token | BuyVol24h (SOL) | PriceChange24h | TrustBonus | DiscoverScore |
|---|---|---|---|---|
| BONK2 | 500 | +40% | +30 (3 badges) | 500 × 1.4 + 30 = **730** |
| DOGE3 | 800 | -20% | +0 | 800 × 0.8 + 0 = **640** |
| MOON | 200 | +100% | +10 (1 badge) | 200 × 2.0 + 10 = **410** |
| PEPE9 | 50 | +5% | +20 (2 badges) | 50 × 1.05 + 20 = **72.5** |

→ Xếp hạng: BONK2 > DOGE3 > MOON > PEPE9

**Nhận xét:**
- DOGE3 volume cao nhất nhưng đang dump → bị kéo xuống
- BONK2 thắng nhờ volume tốt + đang tăng + full trust
- MOON tăng gấp đôi nhưng ít người mua → không đủ sức lên top

---

## Cơ chế hiển thị (slot 80/20)

Mỗi trang 20 token:
- **16 slot Hot** → DiscoverScore cao nhất
- **4 slot Big** → Market Cap cao nhất (chưa có trong Hot)
- Xen kẽ đều: cứ 5 token thì 1 token Big

```
Hot Hot Hot Hot [Big] Hot Hot Hot Hot [Big] Hot Hot Hot Hot [Big] Hot Hot Hot Hot [Big]
```

Mục đích: tránh trang Discover toàn token nhỏ, xen vài "cây đa cây đề" tạo uy tín.

---

## Vận hành

- Tính lại mỗi **10 phút**, cache kết quả
- Không có ngưỡng loại — token yếu tự rơi cuối, vẫn hiện làm fallback
