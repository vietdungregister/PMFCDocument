# Token War — Phân tích 2 mô hình cơ chế cá cược


---

## Mô hình 1 — Pari-mutuel

### Giải thích bằng ngôn ngữ thường

Tất cả tiền cược gom vào một pool chung. Khi war kết thúc, pool đó chia hết cho bên thắng — theo tỷ lệ ai bỏ vào bao nhiêu. Platform lấy một phần nhỏ (có thể khoảng 5%) trước khi chia.

### Ví dụ cụ thể

```
War: DOGE vs PEPE — 6 tiếng
Platform rake: 5%

Kết quả đặt cược:
  Team DOGE: 80 người, tổng 8 SOL
  Team PEPE: 50 người, tổng 5 SOL
  Total pool: 13 SOL

Platform lấy 5%: 0.65 SOL
Còn lại: 12.35 SOL → chia hết cho bên thắng

PEPE thắng (buy volume nhiều hơn):
  → 50 người PEPE chia nhau 12.35 SOL
  → Người chơi A đặt 0.1 SOL (= 2% của 5 SOL PEPE)
  → Bạn nhận 2% × 12.35 = 0.247 SOL (~2.47x)

DOGE thua → mất toàn bộ tiền cược
```

### Vấn đề lớn nhất

**User không biết sẽ ăn bao nhiêu lúc bỏ tiền vào.**

Lý do: pool thay đổi liên tục khi có người vào thêm. Do số tiền ăn được sẽ thay đổi tùy vào lượng người vào và số tiền vào ở cả 2 bên. Chỉ khi war kết thúc mới biết chính xác.

Nếu minh bạch số tiền vào kèo của cả 2 bên, user có thể tự tính toán để thấy platform đơn giản là lấy tiền của bên thắng, ăn 5%, rồi chia cho bên thua, sẽ nghĩ platform không có vai trò gì.

### Ưu điểm
- Đơn giản để hiểu về mặt vận hành
- Platform không bao giờ lỗ (chỉ ăn %, không bỏ tiền ra)
- Không cần seed vốn ban đầu
- Dễ build hơn

### Nhược điểm
- User không biết payout chính xác lúc vào
- Odds thay đổi suốt war 
- Ít "thú vị về mặt nền tảng"

---

## Mô hình 2 — Prediction Market

### Tổng quan

Thay vì gom tiền vào pool rồi chia, user **mua phiếu của một kết quả**. Mỗi phiếu có giá thị trường thay đổi theo cung cầu. Nếu thắng, mỗi phiếu đổi được đúng **1 SOL (mệnh giá -  cái này platform quyết định)**. Người mua sớm (giá thấp) ăn nhiều hơn người mua muộn (giá cao).

---

### Các khái niệm cơ bản

**Mệnh giá:** Số SOL nhận được khi đổi 1 phiếu thắng. Do platform quy định khi tạo war. Ví dụ này dùng **1 SOL**.

**Vault:** Két của hệ thống — giữ toàn bộ SOL đảm bảo đủ tiền trả cho người thắng. Vault luôn bằng tổng phiếu đang lưu hành × mệnh giá — nghĩa là một quỹ để bảo chứng cho hệ thống không bao giờ vỡ nợ.

**Pool:** Kho phiếu. Ban đầu do platform tạo ra từ seed. Phiếu trong pool thuộc quyền quản lý của hệ thống.

**k (hằng số thị trường):** Tích số phiếu A và phiếu B trong pool. **Không bao giờ thay đổi** sau mỗi giao dịch. Đây là cơ chế tự động điều chỉnh giá — khi một bên tăng, bên kia phải giảm để giữ k.

**Công thức giá:**
```
Giá phiếu A = (Số phiếu B trong pool / Tổng phiếu trong pool) × Mệnh giá
Giá phiếu B = (Số phiếu A trong pool / Tổng phiếu trong pool) × Mệnh giá

→ Giá A + Giá B = Mệnh giá (luôn luôn, vì một trong hai chắc chắn thắng)
→ Giá = xác suất thắng theo đánh giá thị trường
```

---

### Bước 1: Khởi tạo thị trường (Seed)

Admin nạp vốn mồi để tạo thanh khoản ban đầu.

**Hành động:** Nạp 10 SOL.

**Hệ thống thực hiện:** In ra 10 phiếu A và 10 phiếu B, bỏ vào pool. (10 SOL chỉ đủ trả cho tối đa 10 phiếu thắng — đúng bằng số phiếu mỗi bên).

```
Số phiếu mỗi bên = Seed / Mệnh giá = 10 / 1 = 10 phiếu
Hằng số k = 10 × 10 = 100
Vault = 10 SOL

Giá ban đầu:
  Phiếu A = (10 / 20) × 1 = 0.50 SOL  (50% tỉ lệ thắng)
  Phiếu B = (10 / 20) × 1 = 0.50 SOL  (50% tỉ lệ thắng)
```

---

### Bước 2: Người dùng mua phiếu

Giả sử **User 1 (U1) nạp 2 SOL để mua phiếu A.**

**A. Nạp tiền và In phiếu:**

Hệ thống lấy 2 SOL của U1 bỏ vào vault, rồi in thêm 2 cặp phiếu mới để đảm bảo vault luôn đủ tiền trả dù bên nào thắng.

```
Vault: 10 + 2 = 12 SOL

Phiếu A tạm thời: 10 (cũ) + 2 (mới in) = 12
Phiếu B tạm thời: 10 (cũ) + 2 (mới in) = 12
```

**B. Tính số phiếu trả cho khách:**

Hệ thống giữ lại (giảm đi) một phần phiếu A trong pool để đảm bảo k = A × B = 100 không đổi.

```
Phiếu B sau khi thêm vào pool: 12
Phiếu A phải giữ lại trong pool: k / B_temp = 100 / 12 = 8.33
Phiếu A đưa cho U1: A_temp − A_new = 12 − 8.33 = 3.67 phiếu
```

**C. Kết quả:**

```
U1 nhận: 3.67 phiếu A
Payout nếu A thắng: 3.67 × 1 SOL = 3.67 SOL

Pool cập nhật: A = 8.33 | B = 12
Giá A mới = (12 / 20.33) × 1 = 0.59 SOL ↑  (59% tỉ lệ thắng)
Giá B mới = (8.33 / 20.33) × 1 = 0.41 SOL ↓ (41% tỉ lệ thắng)
```

Giá A tăng vì nhiều người mua A → thị trường đang tin A thắng hơn.

---

### Bước 3: Người dùng mua bên ngược lại

**User 2 (U2) nạp 2 SOL mua phiếu B:**

```
Vault: 12 + 2 = 14 SOL

Phiếu A tạm thời: 8.33 + 2 = 10.33
Phiếu B tạm thời: 12 + 2   = 14

Phiếu B phải giữ lại trong pool: k / A_temp = 100 / 10.33 = 9.68
Phiếu B đưa cho U2: B_temp − B_new = 14 − 9.68 = 4.32 phiếu

Pool cập nhật: A = 10.33 | B = 9.68
Giá A mới = (9.68 / 20.01) × 1 = 0.48 SOL ↓ (48%)
Giá B mới = (10.33 / 20.01) × 1 = 0.52 SOL ↑ (52%)
```

---

### Bước 4: Mua số lượng lớn

**User 3 (U3) nạp 5 SOL mua phiếu A:**

```
Vault: 14 + 5 = 19 SOL

Phiếu A tạm thời: 10.33 + 5 = 15.33
Phiếu B tạm thời: 9.68 + 5  = 14.68

Phiếu A phải giữ lại trong pool: k / B_temp = 100 / 14.68 = 6.81
Phiếu A đưa cho U3: A_temp − A_new = 15.33 − 6.81 = 8.52 phiếu

Pool cập nhật: A = 6.81 | B = 14.68
Giá A mới = (14.68 / 21.49) × 1 = 0.68 SOL ↑ (68%)
Giá B mới = (6.81 / 21.49) × 1  = 0.32 SOL ↓ (32%)
```

---

### Bước 5: Kết thúc — Token A thắng

Mỗi phiếu A đổi được 1 SOL. Phiếu B = 0.

| Người dùng | Loại phiếu | Số lượng | Nhận về |
|---|---|---|---|
| U1 | A | 3.67 | **3.67 SOL** |
| U2 | B | 4.32 | **0 SOL** |
| U3 | A | 8.52 | **8.52 SOL** |

**Kiểm tra Vault:**

```
Tổng SOL đã vào: 10 (Seed) + 2 (U1) + 2 (U2) + 5 (U3) = 19 SOL
Tổng chi trả:    3.67 + 8.52 = 12.19 SOL
Còn lại:         19 − 12.19 = 6.81 SOL → Admin nhận lại (từ 6.81 phiếu A còn trong pool)
```

Số tiền còn lại đúng bằng số phiếu A trong pool (6.81) × 1 SOL. **Hệ thống luôn cân bằng tuyệt đối.**

**P&L của Admin trong ví dụ này:**
```
Admin bỏ vào (seed): 10 SOL
Admin nhận lại:       6.81 SOL
Admin lỗ:            −3.19 SOL  ← vì A thắng (bên được đặt nhiều)

Nếu B thắng: Admin nhận lại 14.68 SOL → lời +4.68 SOL
```

Admin lỗ khi bên được đặt nhiều thắng, lời khi bên ít người đặt thắng. Đây là rủi ro từ seed.

---

### Incentive tự nhiên: Vào sớm ăn nhiều hơn

```
U1 mua phiếu A lúc giá 0.50 SOL:
  Bỏ 2 SOL → nhận 3.67 phiếu → payout = 3.67 SOL → lãi 1.67 SOL (83%)

U3 mua phiếu A lúc giá 0.59 SOL (sau khi U1 đẩy giá lên):
  Bỏ 5 SOL → nhận 8.52 phiếu → payout = 8.52 SOL → lãi 3.52 SOL (70%)

→ Cùng chọn đúng bên thắng, nhưng U1 vào sớm hơn → % lãi cao hơn.
→ Đây là incentive tự nhiên để người dùng vào sớm và quyết đoán.
```

---

### Seed — ai bỏ tiền tạo pool ban đầu?

**Platform là người seed.** Platform bỏ S SOL tạo giá ban đầu 50/50.

```
Seed = 10 SOL → 10 phiếu mỗi bên → giá ban đầu: A 0.50 | B 0.50
```

**Seed ảnh hưởng platform thế nào sau war?**

Platform hold cả 2 loại phiếu từ seed (trong pool). Sau war, chỉ 1 loại có giá trị:

```
Ví dụ seed = 1 SOL, user bỏ vào A SOL bên thắng, B SOL bên thua:

Platform P&L = Fee thu được + Payout seed bên thắng − 1 SOL
             = (A+B)×2% + (0.5)/(0.5+A) × (1+A+B) − 1
```

Phân tích theo kịch bản (cố định A+B = 20 SOL, Seed = 1 SOL, fee = 5%):

| Tỷ lệ A:B (thắng:thua) | Seed P&L | Fee | Platform tổng |
|---|---|---|---|
| 50:50 (cân bằng) | 0 | +1.00 SOL | **+1.00 SOL** ✅ |
| 70:30 (lệch nhẹ) | −0.28 SOL | +1.00 SOL | **+0.72 SOL** ✅ |
| 90:10 (lệch nặng) | −0.43 SOL | +1.00 SOL | **+0.57 SOL** ✅ |
| 30:70 (underdog thắng) | +0.62 SOL | +1.00 SOL | **+1.62 SOL** ✅✅ |
| 10:90 (underdog thắng mạnh) | +3.20 SOL | +1.00 SOL | **+4.20 SOL** ✅✅✅ |


**Nhưng nếu volume nhỏ hơn thì sao?**

Seed P&L tệ nhất (toàn bộ user dồn vào bên thắng) là khoảng 50% của Seed. Để hòa vốn cần:

```
Volume × fee% ≥ Seed / 2

→ Breakeven Volume = Seed / (2 × fee%)
```

**Breakeven Volume theo fee và seed:**

| Fee | Breakeven = Seed × bao nhiêu lần | Seed = 1 SOL | Seed = 5 SOL | Seed = 10 SOL |
|---|---|---|---|---|
| 5% | × 9.5 | 9.5 SOL | 47.5 SOL | 95 SOL |

**Dải P&L có thể xảy ra — fee 5% cố định:**

Công thức tổng quát (Seed = S):
```
P&L = Volume × 5% + (S/2) / (S/2 + V_win) × (S + Volume) − S

V_win = phần volume đổ vào bên thắng
```

**Seed = 1 SOL (Breakeven = 9.5 SOL):**

| Volume | 50:50 | 70:30 | 90:10 | 100:0 (xấu nhất) | 10:90 (tốt nhất) |
|---|---|---|---|---|---|
| 4.75 SOL (½ BE) | +0.24 | +0.00 | **−0.16** | **−0.21** | +2.19 |
| 9.5 SOL (= BE) | +0.48 | +0.21 | +0.05 | **0.00** | +3.10 |
| 14.25 SOL (1.5× BE) | +0.71 | +0.44 | +0.28 | +0.23 | +3.67 |
| 28.5 SOL (3× BE) | +1.43 | +1.15 | +0.99 | +0.93 | +4.83 |

**Seed = 2 SOL (Breakeven = 19 SOL):**

| Volume | 50:50 | 70:30 | 90:10 | 100:0 (xấu nhất) | 10:90 (tốt nhất) |
|---|---|---|---|---|---|
| 9.5 SOL (½ BE) | +0.48 | +0.00 | **−0.32** | **−0.43** | +4.37 |
| 19 SOL (= BE) | +0.95 | +0.42 | +0.11 | **0.00** | +6.19 |
| 28.5 SOL (1.5× BE) | +1.43 | +0.88 | +0.57 | +0.46 | +7.35 |
| 57 SOL (3× BE) | +2.85 | +2.18 | +1.98 | +1.87 | +9.66 |

**Chú thích:**
- Cột "100:0" = toàn bộ volume dồn vào bên thắng → worst case platform
- Cột "10:90" = underdog thắng ngược → best case platform (ăn cả seed bên thua của user)
- Hàng "= BE" (breakeven): worst case P&L = 0, mọi tình huống còn lại đều có lãi
- Dưới breakeven: chỉ kịch bản 50:50 hoặc underdog thắng là an toàn
- Seed=2 SOL không cho % lợi nhuận cao hơn Seed=1 SOL (cùng volume/BE ratio), nhưng số tuyệt đối lớn hơn gấp đôi

**Rút ra:**
- Seed càng lớn → cần volume càng lớn mới hòa vốn — rủi ro tăng tuyến tính
- Seed = 1 SOL + fee 5% → chỉ cần war thu được ≥ 9.5 SOL là platform không lỗ
- Khi underdog thắng → platform ăn to từ cả fee lẫn seed position

**→ Giữ seed nhỏ (0.5–1 SOL/war). Seed lớn hơn không giúp platform kiếm thêm khi war cân bằng, chỉ tăng rủi ro khi war lệch.**

---

### Về Seed và Mệnh giá


```
Seed      → kiểm soát rủi ro tài chính + slippage
Mệnh giá  → kiểm soát mệnh giá vé + UX của user
```

**Seed to có ưu điểm gì?**

| Seed nhỏ (0.5–1 SOL) | Seed lớn (5–10 SOL) |
|---|---|
| Breakeven dễ đạt hơn | Breakeven cần volume lớn hơn |
| Rủi ro vốn thấp | Rủi ro vốn cao |
| Giá biến động mạnh khi bet lớn | **Giá ổn định hơn, khó thao túng** |
| Whale bet 1 SOL → slippage 20% | **Whale bet 1 SOL → slippage chỉ 5%** |
| Chỉ hút được user nhỏ | **Hút được user lớn, war volume cao hơn** |
| Pool mỏng → dễ bị một người lệch giá | **Pool dày → tỷ lệ phản ánh sentiment thực** |

**Tóm lại:** Seed to giúp war có chất lượng hơn — giá phiếu ổn định, khó manipulate, thu hút được whale vào. Nhược điểm là rủi ro vốn và Breakeven cao hơn. 

**N = Seed / Mệnh giá** là số phiếu ban đầu mỗi bên — "độ sâu" của pool. N càng lớn → pool càng dày → giá biến động ít hơn.

**Slippage phụ thuộc vào Seed:**

```
Slippage = X / (2 × Seed + X)     (X = số SOL user bỏ vào)
```

| Bet so với Seed | Slippage |
|---|---|
| 1% | ~0.5% |
| 5% | ~2.4% |
| 10% | ~4.8% |
| 20% | ~9.1% |
| 50% | ~20% |

---

**Tương quan Seed và Max bet:**

Từ công thức slippage, rút ra max bet một lần để giữ slippage không vượt ngưỡng S:

```
Max bet = 2 × Seed × S / (1 − S)

→ Slippage 20% :  Max bet = 0.5 × Seed
→ Slippage 10% :  Max bet ≈ 0.22 × Seed
```

| Seed | Max bet (slippage ≤ 20%) | Max bet (slippage ≤ 10%) | War tier phù hợp |
|---|---|---|---|
| 0.5 SOL | 0.25 SOL | 0.11 SOL | War micro — chỉ retail rất nhỏ |
| 1 SOL | 0.50 SOL | 0.22 SOL | War nhỏ — retail thông thường |
| 2 SOL | 1.00 SOL | 0.44 SOL | War vừa — hút được user vừa |
| 5 SOL | 2.50 SOL | 1.11 SOL | War lớn — whale bắt đầu tham gia |
| 10 SOL | 5.00 SOL | 2.22 SOL | War major — whale thoải mái |

**Ứng dụng:** Nên giới hạn max bet per transaction = 20% Seed trong product rules để tránh 1 user phá vỡ cả thị trường. Bet lớn hơn vẫn được, nhưng phải chia nhiều lần.

---

**Bảng kết hợp tham số — fee 5% cố định:**

| Seed | Mệnh giá | Breakeven | Max bet | Điểm |
|---|---|---|---|---|
| 0.5 SOL | 0.05 SOL | 4.75 SOL | 0.25 SOL | ★★ |
| 1 SOL | 0.1 SOL | 9.5 SOL | 0.50 SOL | ★★★ |
| 1 SOL | 0.05 SOL | 9.5 SOL | 0.50 SOL | ★★★★ |
| 2 SOL | 0.1 SOL | 19 SOL | 1.00 SOL | ★★★★ |
| 5 SOL | 0.25 SOL | 47.5 SOL | 2.50 SOL | ★★★ |
| 5 SOL | 0.5 SOL | 47.5 SOL | 2.50 SOL | ★★ |
| 10 SOL | 0.5 SOL | 95 SOL | 5.00 SOL | ★★ |
| 10 SOL | 1 SOL | 95 SOL | 5.00 SOL | ★ |

---

**Giải thích cách chấm điểm:**

Điểm dựa trên 4 tiêu chí:

**1. Rủi ro platform — Breakeven dễ đạt không?**
- ★★ nếu Breakeven ≤ 10 SOL → war nhỏ cũng đủ hòa vốn
- ★ nếu Breakeven 10–50 SOL → cần war vừa
- ✗ nếu > 50 SOL → cần war lớn, rủi ro cao

**2. UX — số vé nhận được từ 0.1 SOL bet:**
- ★★ nếu ≥ 2 vé → cảm giác "mua được nhiều vé", gamified
- ★ nếu ~1 vé → tạm chấp nhận
- ✗ nếu < 1 vé → mua fraction vé, UX kém, không cảm giác game

**3. Pool stability — slippage khi bet 0.5 SOL:**
```
Seed = 0.5 SOL → slippage 33%  → dễ thao túng giá       ✗
Seed = 1 SOL   → slippage 20%  → chấp nhận (meme vibes)  ★
Seed = 2 SOL   → slippage 11%  → tốt                     ★★
Seed = 5 SOL   → slippage  5%  → rất tốt                 ★★
Seed = 10 SOL  → slippage  2%  → xuất sắc                ★★
```

**4. Max bet — có hút được whale không?**
- ★★ nếu Max bet ≥ 1 SOL → whale và mid-tier user vào được
- ★ nếu Max bet 0.25–1 SOL → chỉ retail nhỏ
- ✗ nếu Max bet < 0.25 SOL → gần như ai bet decent cũng bị slippage cao

**Giải thích từng dòng:**

- **0.5 SOL / 0.05 SOL — ★★:** Breakeven cực thấp ✓, nhiều vé ✓, nhưng max bet chỉ 0.25 SOL và slippage 33% → thị trường mỏng, dễ bị 1 user phá vỡ hoàn toàn chỉ với vài SOL.

- **1 SOL / 0.1 SOL — ★★★:** Minimum viable. Breakeven tốt ✓, 2 vé/0.1 SOL ✓, max bet 0.5 SOL đủ cho retail. N=10 ở mức tối thiểu.

- **1 SOL / 0.05 SOL — ★★★★:** Sweet spot cho war nhỏ. Cùng Seed=1 nên Breakeven, slippage, max bet giống dòng trên, nhưng N=20 sâu hơn ✓ và 4 vé/0.1 SOL → cảm giác game tốt hơn rõ rệt.

- **2 SOL / 0.1 SOL — ★★★★:** Sweet spot cho war vừa. Breakeven 19 SOL khả thi ✓, slippage 11% với 0.5 SOL bet ✓, N=20 ✓, max bet 1 SOL — bắt đầu hút được whale nhỏ.

- **5 SOL / 0.25 SOL — ★★★:** Max bet 2.5 SOL → whale tham gia được ✓, slippage tốt ✓, N=20 ✓. Điểm trừ: Breakeven 47.5 SOL cần community lớn, và UX kém (0.8 vé/0.1 SOL).

- **5 SOL / 0.5 SOL — ★★:** Cùng Breakeven cao như trên, nhưng N=10 thấp so với seed lớn. Vé càng ít (0.4 vé/0.1 SOL). Không nên dùng combo này.

- **10 SOL / 0.5 SOL — ★★:** Max bet 5 SOL → whale thoải mái ✓, slippage xuất sắc ✓. Nhưng Breakeven 95 SOL gần như không thực tế cho war thông thường.

- **10 SOL / 1 SOL — ★:** Breakeven 95 SOL + N=10 thấp + UX tệ nhất (0.2 vé/0.1 SOL). Không có lý do để chọn combo này.

**→ Công thức tối ưu:** Mệnh giá = Seed / 20 (N=20), Seed giữ ở 1–2 SOL/war. Giới hạn max bet = 20% Seed mỗi transaction.


## So sánh trực tiếp — cùng 1 kịch bản

**Kịch bản:** 100 người tham gia war DOGE vs PEPE, tổng 20 SOL user bỏ vào, 60% vào DOGE, 40% vào PEPE. PEPE thắng bất ngờ.

| | Pari-mutuel | Prediction Market |
|---|---|---|
| **User biết payout lúc vào** | ❌ Không, chỉ thấy ước tính | ✅ Biết chính xác |
| **Platform cần set odds** | ❌ Không cần | ❌ Không cần |
| **Platform chịu rủi ro tài chính** | ❌ Không (nếu không seed) | ⚠️ Có (từ phần seed) |
| **Platform cần seed vốn** | ❌ Không | ⚠️ Cần (nhỏ) |
| **Platform revenue** | 20 × 5% = 1 SOL | 20 × 2% = 0.4 SOL + seed P&L |
| **Độ phức tạp build** | Thấp | Trung bình |
| **Dễ giải thích cho user** | Cao | Trung bình |
| **Dữ liệu thú vị** | Thấp | Cao (implied probability) |

---

## Vấn đề seed trong Prediction Market

Đây là điểm mấu chốt nhất.

### Seed để làm gì?

Prediction Market cần có pool ban đầu để:
1. Tạo initial price (50/50 khi mới bắt đầu)
2. Cho user đầu tiên có thể mua share ngay lập tức

Nếu không seed → không có giá → user đầu tiên không biết mua ở đâu.

### Seed ảnh hưởng platform thế nào?

Platform đặt cược 2 bên đều nhau (S/2 mỗi bên). Sau war:
- **Bên thắng:** platform lấy lại phần seed tương ứng
- **Bên thua:** mất S/2 SOL

**Kết quả phụ thuộc vào tỷ lệ user betting:**

```
Khi 2 bên cân bằng (50/50):
  → Seed P&L = 0, platform chỉ ăn fee
  → An toàn nhất

Khi áp đảo về 1 bên (ví dụ 90% vào DOGE):
  → Nếu DOGE thắng: platform lỗ seed
  → Nếu PEPE thắng (underdog): platform ăn to từ seed

Khi 1 bên hoàn toàn không có user:
  → Seed trở thành "người chơi duy nhất" bên đó
  → Nếu bên đó thắng: platform ăn rất to
  → Nếu bên đó thua: platform mất S/2
```

### Breakeven

Platform hòa vốn trên seed khi:

```
Worst case (toàn bộ user vào bên thắng), fee = 5%:
  Cần volume ≥ 9.5 × Seed để fee bù lỗ seed

Seed = 0.5 SOL → cần ≥ 4.75 SOL volume
Seed = 1 SOL   → cần ≥ 9.5 SOL volume
Seed = 5 SOL   → cần ≥ 47.5 SOL volume
```

**→ Giữ seed nhỏ (0.5–1 SOL/war) để rủi ro tối thiểu.**

### Giải pháp không cần platform seed: Commitment Model

```
War chỉ start khi cả 2 bên có đủ user tự commit
(ví dụ: mỗi bên tối thiểu 1 SOL)

→ Platform không bỏ tiền ra
→ User tự tạo initial liquidity
→ Platform chỉ thu fee, rủi ro = 0

Nhược điểm: War có thể không start nếu không đủ người
→ Fix bằng early bird bonus (fee discount, points)
   và countdown timer tạo FOMO
```

---

## Conflict of Interest (quan trọng)

Khi platform seed và underdog thắng → platform ăn to. Điều này tạo ra câu hỏi:

> *"Platform có chọn cặp token mà biết trước underdog sẽ thắng không?"*

Ngay cả khi platform không làm vậy, user vẫn có thể nghi ngờ.

**Cách xử lý:**
- Dùng Commitment Model (platform không seed) → conflict biến mất hoàn toàn
- Hoặc công bố minh bạch thuật toán chọn token
- Platform không được biết kết quả war trước khi công bố


---

## Tổng kết

**Pari-mutuel:** Đơn giản, an toàn, nhưng user không biết ăn bao nhiêu lúc vào.

**Prediction Market:** Phức tạp hơn một chút, user biết chính xác payout, platform có chịu rủi ro mất tiền, trừ khi không cần chịu rủi ro nếu dùng Commitment Model. Cần tính toán số seed, mệnh giá sao cho giảm thiểu rủi ro mà user vẫn hứng thú, một lần mua phiếu ko làm giao động thị trường nhiều.
