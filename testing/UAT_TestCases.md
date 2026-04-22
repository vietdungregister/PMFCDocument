# UAT TEST CASES — PumpFun Clone

---

## Quy ước

| Ký hiệu | Ý nghĩa |
|---|---|
| 🔴 Critical | Phải pass — core flow |
| 🟡 High | Nên pass — chức năng quan trọng |
| 🟢 Medium | Nice to have — UX, edge case |
| ⛔ MVP chưa có | FRD yêu cầu nhưng MVP chưa build |
| ✅ | Pass |
| ❌ | Fail |
| ⏭️ | Skip (chưa test được) |

---

# GLOBAL COMPONENTS

## G.1 — Sidebar Navigation

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| G1-01 | 🟡 | Sidebar hiển thị đầy đủ menu items | 1. Mở trang chủ<br>2. Nhìn sidebar trái | Có đủ: Logo, My Profile, Arena, Events, Clubs, Leaderboard, Point System, Rewards, Referrals, Stake, Create Token, Connect Wallet | |
| G1-02 | 🟡 | Logo click về trang chủ | 1. Vào trang token detail bất kỳ<br>2. Click logo trên sidebar | Quay về trang chủ (Token List) | |
| G1-03 | 🟢 | CTA buttons hiển thị đúng | 1. Nhìn sidebar | "Create Token" (xanh lá), "Connect Wallet" (xanh lá) hiển thị nổi bật | |
| G1-04 | 🟢 | Auth status hiển thị đúng | 1. Khi chưa connect wallet → check sidebar<br>2. Connect wallet → check lại | Chưa connect: "Auth: Not authenticated"<br>Đã connect: "Auth: Authenticated" | |
| G1-05 | 🟢 | Sidebar navigation hoạt động | 1. Click lần lượt từng menu item | Mỗi item navigate tới đúng trang tương ứng | |

## G.2 — Wallet Connection

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| G2-01 | 🔴 | Connect wallet Phantom | 1. Click "Connect Wallet"<br>2. Chọn Phantom<br>3. Approve trên Phantom | Wallet connected, hiển thị địa chỉ ví (rút gọn), auth status đổi sang Authenticated | |
| G2-02 | 🔴 | Chức năng bị block khi chưa connect | 1. KHÔNG connect wallet<br>2. Thử click Create Token<br>3. Thử mở Point System<br>4. Thử mở Rewards | Mỗi chức năng đều yêu cầu connect wallet trước (hiện prompt/modal) | |
| G2-03 | 🟡 | Disconnect wallet | 1. Khi đã connected<br>2. Tìm nút disconnect/logout<br>3. Click disconnect | Wallet disconnected, auth status quay lại "Not authenticated" | |
| G2-04 | 🟡 | Connect wallet Solflare | 1. Click "Connect Wallet"<br>2. Chọn Solflare<br>3. Approve | Wallet connected tương tự Phantom | |

## G.3 — Theme System

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| G3-01 | 🟢 | Dark/Light toggle | 1. Tìm toggle Dark/Light trên sidebar<br>2. Switch từ Dark → Light<br>3. Switch lại Light → Dark | Giao diện thay đổi đúng theme, không bị vỡ layout | |
| G3-02 | 🟢 | Color palette selector | 1. Tìm palette selector<br>2. Lần lượt chọn: Seed, Sprout, Bud, Bloom, Canopy | Tone màu chủ đạo thay đổi cho mỗi palette, không bị lỗi | |

## G.4 — Top Banner

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| G4-01 | 🟢 | Banner marquee chạy | 1. Mở trang chủ<br>2. Nhìn banner trên cùng | Text marquee chạy liên tục (MEMECONOMY, FAIR LAUNCH...) | |
| G4-02 | 🟢 | Token carousel | 1. Nhìn phía dưới marquee | Token list carousel hiển thị và có thể scroll | |

---

# FR-001: DANH SÁCH TOKEN

## 1.1 — Tabs Navigation

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-001 | 🔴 | Trang chủ load danh sách token | 1. Mở trang chủ | Danh sách tokens hiển thị dạng card/grid, có data thật | |
| TC-002 | 🟡 | 5 tabs hiển thị đúng | 1. Nhìn tab bar trên danh sách token | Có 5 tabs: Discover, Trending, Top Volume, Graduated, Favorite.<br>⛔ MVP đang hiển thị: Trending/Market Cap/Finalized/New/Trending Arena — note sự khác biệt | |
| TC-003 | 🟡 | Tab default đúng | 1. Mở trang chủ lần đầu | Tab Discover active (theo FRD).<br>⛔ MVP hiện default là Trending | |
| TC-004 | 🟡 | Switch tab hoạt động | 1. Click từng tab lần lượt | Mỗi tab load danh sách khác nhau, có visual indicator cho tab active | |
| TC-005 | 🟢 | Switch tab reset pagination | 1. Scroll xuống hoặc tới page 2 ở tab hiện tại<br>2. Switch sang tab khác | Danh sách quay về đầu / page 1 | |
| TC-006 | 🟢 | Tab Graduated — empty state | 1. Click tab Graduated (nếu chưa có token nào graduated) | Hiển thị: "Chưa có token nào đạt graduation ($69K MC)" hoặc tương tự | |
| TC-007 | 🟢 | Tab Favorite — empty state | 1. Connect wallet (Account A)<br>2. Click tab Favorite (chưa yêu thích token nào) | Hiển thị: "Bạn chưa có token yêu thích nào"<br>⛔ MVP chưa có Favorite | |

## 1.2 — Token Card

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-008 | 🔴 | Token card hiển thị đủ thông tin | 1. Nhìn bất kỳ token card nào | Có: Avatar, Tên, Symbol, Market Cap (MC:), Volume (Vol:), Progress bar (to DEX), Created time | |
| TC-009 | 🟡 | Market Cap format rút gọn | 1. Tìm token có MC > 1K<br>2. Tìm token có MC > 1M (nếu có) | MC hiển thị: $12.5K, $1.2M... (rút gọn đúng) | |
| TC-010 | 🟡 | Click card → Token Detail | 1. Click vào một token card | Navigate tới trang Token Detail của token đó | |
| TC-011 | 🟢 | Card hover effect | 1. Di chuột vào token card | Card có hiệu ứng hover (shadow hoặc scale nhẹ) | |
| TC-012 | 🟢 | Price Change 24h hiển thị đúng màu | 1. Tìm token có price change dương<br>2. Tìm token có price change âm | Dương: xanh lá + ↑, Âm: đỏ + ↓<br>⛔ MVP chưa hiển thị Price Change 24h trên card | |
| TC-013 | 🟢 | Token Statement hiển thị | 1. Nhìn token card | Có dòng statement dưới tên<br>⛔ MVP chưa hiển thị Statement trên card | |
| TC-014 | 🟢 | Favorite button trên card | 1. Nhìn token card, góc phải trên | Có icon ♡, click toggle thành ♥<br>⛔ MVP chưa có Favorite | |
| TC-015 | 🟢 | Trust Level Badges | 1. Nhìn token card | Token đủ điều kiện hiển thị badge: 🔒 LP Locked, ✓ Audited, 🛡️ Freeze Disabled<br>⛔ MVP chưa có Trust Badges | |

## 1.2B — Token Card Data Accuracy (Logic)

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-015B | 🟡 | MC rút gọn K/M/B chính xác | 1. Tìm token MC = $500 (< 1K)<br>2. Tìm token MC = $12,500 (>= 1K)<br>3. Tìm token MC = $1,200,000 (>= 1M) | < 1K: full number ($500)<br>>= 1K: $12.50K (2 decimals)<br>>= 1M: $1.20M (2 decimals) | |
| TC-015C | 🟡 | Volume 24h auto-refresh | 1. Mở Token List<br>2. Đợi 30-60 giây<br>3. Quan sát Volume trên card | Volume cập nhật mà không cần F5 (FRD: refresh mỗi 30s) | |
| TC-015D | 🟢 | Created time relative format | 1. Tạo token mới<br>2. Xem card của token đó | Hiển thị "a few seconds ago" hoặc "1m ago" (relative, không phải timestamp tuyệt đối) | |
| TC-015E | 🟢 | Performance với nhiều cards | 1. Scroll qua danh sách token (load nhiều cards)<br>2. Quan sát tốc độ render | Không lag/giật khi hiển thị 50+ cards | |

## 1.3 — Filter

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-016 | 🟡 | NSFW filter toggle | 1. Mở Filter panel<br>2. Toggle NSFW ON<br>3. Toggle OFF | ON: hiện cả NSFW tokens, OFF: ẩn NSFW | |
| TC-017 | 🟡 | Live toggle | 1. Mở Filter<br>2. Toggle Live ON | Chỉ hiện tokens đang có giao dịch active | |
| TC-018 | 🟢 | MC/Volume Range filter | 1. Mở Filter<br>2. Kéo slider MC range | Danh sách chỉ hiện tokens trong range<br>⛔ MVP chưa có MC/Volume Range filter | |
| TC-019 | 🟢 | Trust Level filter | 1. Mở Filter<br>2. Check/uncheck trust badges | Danh sách filter theo OR logic<br>⛔ MVP chưa có Trust Level filter | |
| TC-020 | 🟢 | Reset Filters | 1. Bật vài filters<br>2. Click "Reset Filters" | Tất cả filters quay về mặc định | |
| TC-021 | 🟢 | Badge đếm active filters | 1. Bật 2 filters | Nút Filter hiển thị badge "2" | |

## 1.4 — Sort

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-022 | 🟢 | Sort panel hiển thị | 1. Click nút Sort | Sort panel mở với options: Giá, Market Cap, Volume 24h, Ngày tạo<br>⛔ MVP chưa có nút Sort riêng | |
| TC-023 | 🟢 | Sort theo Market Cap giảm dần | 1. Chọn Market Cap<br>2. Click 1 lần (giảm dần) | Tokens sắp xếp MC cao → thấp<br>⛔ MVP chưa có Sort UI | |

## 1.5 — Search

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-024 | 🔴 | Search token bằng tên | 1. Gõ tên token vào search field (ví dụ: "Pepe")<br>2. Nhấn Enter | Danh sách chỉ hiện tokens có tên chứa "Pepe" | |
| TC-025 | 🟡 | Search không tìm thấy | 1. Gõ "xyzabc123notexist"<br>2. Nhấn Enter | Hiển thị "No results" hoặc danh sách trống | |
| TC-026 | 🟢 | Search kết hợp với filter | 1. Bật NSFW filter OFF<br>2. Search "test" | Kết quả chỉ bao gồm tokens khớp "test" VÀ không phải NSFW | |

---

# FR-002: CHI TIẾT TOKEN

## 2.1 — Token Metadata

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-027 | 🔴 | Trang Token Detail load đúng | 1. Từ Token List, click vào token bất kỳ | Trang Token Detail mở, hiển thị: Avatar, Tên + Symbol, Price, Contract Address | |
| TC-028 | 🟡 | Contract Address copy | 1. Vào Token Detail<br>2. Click nút Copy bên cạnh Contract Address | Address copied, paste ra kiểm tra đúng | |
| TC-029 | 🟡 | Solscan link hoạt động | 1. Vào Token Detail<br>2. Click link Solscan (nếu có) | Mở tab mới tới Solscan với đúng address | |
| TC-030 | 🟡 | Progress to DEX hiển thị | 1. Nhìn phần header Token Detail | Progress bar từ 0-100% hiển thị tỷ lệ hoàn thành graduation | |
| TC-031 | 🟢 | Creator Info hiển thị | 1. Vào Token Detail<br>2. Tìm "Created by" | Avatar creator + username/wallet rút gọn, click → navigate Public Profile<br>⛔ MVP chưa hiển thị Creator Info | |
| TC-032 | 🟢 | Token Description | 1. Vào Token Detail | Hiển thị mô tả token<br>⛔ MVP chưa hiển thị Description | |
| TC-033 | 🟢 | Social Links | 1. Vào Token Detail (token có social links) | Website, Twitter, Telegram icons, click → mở tab mới<br>⛔ MVP chưa hiển thị Social Links | |
| TC-034 | 🟢 | Favorite button | 1. Vào Token Detail<br>2. Click ♡ | Toggle thành ♥, token thêm vào Favorite list<br>⛔ MVP chưa có | |
| TC-035 | 🟡 | Share button | 1. Vào Token Detail<br>2. Click Share | Mở share options / copy link | |

## 2.2 — Price Chart

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-036 | 🔴 | Chart hiển thị | 1. Vào Token Detail | Biểu đồ giá hiển thị, có data | |
| TC-037 | 🟡 | Timeframe switch | 1. Vào Token Detail<br>2. Click các timeframe (1m, 5m, 15m, 1h...) | Chart update theo timeframe tương ứng | |

## 2.3 — Tabs dưới chart (Trades / Chat / Holders)

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-038 | 🔴 | 3 tabs hiển thị | 1. Vào Token Detail<br>2. Scroll xuống dưới chart | Có 3 tabs: Trades, Chat, Holders | |

### Trades (Transaction History)

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-039 | 🔴 | Transaction list hiển thị | 1. Click tab Trades | Danh sách transactions: Type (BUY/SELL), Timestamp, Trader, Amount, Value, TX Hash | |
| TC-040 | 🟡 | BUY/SELL badge đúng màu | 1. Nhìn transaction list | BUY = xanh, SELL = đỏ | |
| TC-041 | 🟡 | TX Hash link → Explorer | 1. Click TX Hash trong transaction | Mở tab mới tới Solana Explorer đúng transaction | |
| TC-042 | 🟢 | Click trader → Profile | 1. Click username/address của trader | Navigate tới Public Profile của trader đó | |
| TC-042A | 🟢 | Whale transaction highlight 🐋 | 1. Nhìn danh sách Trades<br>2. Tìm transaction có volume > 5% of 24h volume | Transaction đó có icon 🐋 | |
| TC-042B | 🟢 | First trade highlight ⭐ | 1. Tìm transaction đầu tiên của token | Transaction đó có icon ⭐ | |

### Chat

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-043 | 🟡 | Chat tab hiển thị messages | 1. Click tab Chat | Danh sách messages (nếu có) hoặc "No comments yet" | |
| TC-044 | 🔴 | Gửi message (đã connect wallet) | 1. Connect wallet (Account A)<br>2. Click tab Chat<br>3. Gõ "Hello UAT test" vào input<br>4. Nhấn Enter | Message hiển thị trong chat: avatar, username, nội dung, timestamp | |
| TC-045 | 🟡 | Gửi message (chưa connect wallet) | 1. KHÔNG connect wallet<br>2. Thử gõ vào chat input | Hiện prompt yêu cầu connect wallet | |
| TC-046 | 🟢 | Click username trong chat → Profile | 1. Click username của người chat | Navigate tới Public Profile | |

### Holders

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-047 | 🟡 | Holders list hiển thị | 1. Click tab Holders | Danh sách holders: Rank, Avatar/Username/Address, Balance, % of supply | |
| TC-048 | 🟢 | Click holder → Profile | 1. Click tên holder | Navigate tới Public Profile | |

## 2.4 — Trading Panel

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-049 | 🔴 | Trading panel hiển thị | 1. Vào Token Detail | Panel Buy/Sell hiển thị bên phải, có nút BUY và SELL | |
| TC-050 | 🟡 | Panel sticky khi scroll | 1. Scroll trang Token Detail xuống | Trading panel vẫn visible (sticky/fixed) | |

---

# FR-003: CHỨC NĂNG BUY/SELL

## 3.1 — Market Order BUY

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-051 | 🔴 | BUY flow thành công | 1. Connect wallet (Account A) — đảm bảo có ≥ 0.1 SOL<br>2. Vào Token Detail (chọn token có liquidity)<br>3. Click BUY tab<br>4. Nhập 0.05 SOL<br>5. Click nút Buy<br>6. Approve transaction trên Phantom | ✅ Transaction thành công<br>Success modal hiện: "Transaction Successful!", TX hash, You Paid, You Received<br>Balance SOL giảm, token balance tăng | |
| TC-052 | 🔴 | BUY — chưa connect wallet | 1. KHÔNG connect wallet<br>2. Vào Token Detail<br>3. Thử click BUY | Hiện modal yêu cầu Connect Wallet | |
| TC-053 | 🟡 | BUY — insufficient balance | 1. Connect wallet (Account A)<br>2. Nhập số SOL lớn hơn balance<br>3. Click Buy | Hiện lỗi: "Insufficient SOL balance" hoặc button disabled | |
| TC-054 | 🟡 | BUY — input validation | 1. Để trống amount<br>2. Nhập 0<br>3. Nhập số âm | Button Buy disabled hoặc hiện validation error | |
| TC-055 | 🟡 | BUY — "You Receive" auto-calculate | 1. Nhập 0.05 SOL vào amount | Trường "You Receive" tự tính và hiển thị số token ước tính | |
| TC-056 | 🟡 | BUY — MAX button | 1. Click nút MAX | Amount tự điền = balance - estimated fees | |
| TC-057 | 🟡 | BUY — success modal actions | 1. Sau khi BUY thành công<br>2. Click TX hash trong modal | Mở Solana Explorer (devnet) đúng transaction | |
| TC-058 | 🟢 | BUY — Quick Amount buttons | 1. Click 0.1 SOL / 0.5 SOL / 1 SOL | Amount input tự điền đúng giá trị<br>⛔ MVP chỉ có MAX, chưa có buttons riêng | |

## 3.2 — Market Order SELL

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-059 | 🔴 | SELL flow thành công | 1. Connect wallet (Account A) — đảm bảo đang hold token (đã BUY ở TC-051)<br>2. Vào Token Detail cùng token<br>3. Click SELL tab<br>4. Nhập số token muốn bán (hoặc nhấn MAX)<br>5. Click nút Sell<br>6. Approve on Phantom | ✅ Transaction thành công<br>Token balance giảm, SOL balance tăng | |
| TC-060 | 🟡 | SELL — không có token để bán | 1. Connect wallet<br>2. Vào token mà mình KHÔNG hold<br>3. Click SELL tab | SELL button disabled hoặc hiện thông báo "No balance" | |
| TC-061 | 🟡 | SELL — switch từ BUY sang SELL | 1. Đang ở BUY tab, đã nhập số liệu<br>2. Click SELL | Form clear, switch sang SELL mode | |

## 3.3 — Advanced Settings

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-062 | 🟡 | Slippage Tolerance settings | 1. Tìm Settings icon (⚙️)<br>2. Click mở<br>3. Chọn slippage 2% | Slippage được set, panel hiển thị giá trị đang chọn | |
| TC-063 | 🟢 | Slippage warning — quá thấp | 1. Set slippage < 0.5% | Hiện warning: "May fail" | |
| TC-064 | 🟢 | Slippage warning — quá cao | 1. Set slippage > 10% | Hiện warning: "High slippage risk" | |
| TC-065 | 🟡 | Anti-MEV Protection toggle | 1. Mở settings<br>2. Toggle Anti-MEV ON | Anti-MEV bật, fee có thể tăng thêm | |
| TC-066 | 🟡 | Priority Fee (Speed) | 1. Mở settings<br>2. Chọn Normal / Fast / Instant | Priority fee thay đổi tương ứng<br>⛔ MVP hiện hiển thị Auto/Manual thay vì Normal/Fast/Instant | |

## 3.4 — Error Handling

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-067 | 🟡 | Slippage exceeded | 1. Set slippage 0.1% (rất thấp)<br>2. BUY token có volatility | Transaction fail, hiện: "Price moved too much. Transaction failed." + Retry button | |
| TC-068 | 🟢 | Auto-retry khi fail | 1. Enable Auto-retry trong settings<br>2. Tạo tình huống fail | Hệ thống retry tự động, hiện "Retry 1/3..."<br>⛔ MVP chưa có Auto-retry | |

## 3.5 — Kiểm chứng giao dịch thật (Transaction Verification)

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-069A | 🔴 | BUY — balance thay đổi đúng | 1. Ghi lại SOL balance trước khi BUY (trên Phantom)<br>2. Ghi lại token balance trước (0 nếu chưa hold)<br>3. BUY 0.05 SOL<br>4. Sau khi thành công, check lại SOL balance trên Phantom<br>5. Check token balance | SOL giảm ≈ 0.05 + fees (network + priority nếu có)<br>Token balance tăng ≈ số hiển thị ở "You Received" trong success modal | |
| TC-069B | 🔴 | SELL — balance thay đổi đúng | 1. Ghi lại SOL balance + token balance trước<br>2. SELL toàn bộ token (nhấn MAX)<br>3. Check lại cả 2 balance sau khi thành công | Token balance = 0<br>SOL tăng ≈ số hiển thị ở success modal (trừ fees) | |
| TC-069C | 🔴 | "You Receive" dự đoán đúng | 1. Nhập 0.05 SOL vào BUY<br>2. Ghi lại số token ở "You Receive" (ước tính)<br>3. Execute BUY<br>4. So sánh "You Received" (thật) vs "You Receive" (ước tính) | Sai lệch ≤ slippage tolerance đã set (mặc định 2%).<br>Ví dụ: ước tính 10,000 tokens, thực nhận 9,800 - 10,200 là OK | |
| TC-069D | 🟡 | Transaction hiện trong history sau khi trade | 1. BUY 0.05 SOL token<br>2. Vào tab Trades dưới chart<br>3. Tìm transaction vừa thực hiện | Transaction mới nhất hiện đầu tiên, đúng: Type (BUY), Amount, Value, Timestamp, TX hash | |
| TC-069E | 🟡 | TX hash on-chain khớp với UI | 1. Sau khi BUY thành công, copy TX hash từ success modal<br>2. Mở Solana Explorer (devnet), paste TX hash<br>3. So sánh on-chain vs UI | On-chain hiển thị: đúng sender (wallet), đúng amount SOL, đúng token received, đúng program | |
| TC-069F | 🟡 | Balance trên Profile khớp sau khi trade | 1. BUY token<br>2. Vào My Profile → Holding Tokens tab | Token vừa mua hiện trong danh sách, balance đúng, value ≈ đúng | |
| TC-069G | 🟡 | Holders list cập nhật sau khi BUY | 1. BUY token (lần đầu mua token này)<br>2. Vào Token Detail → tab Holders | Wallet của mình hiện trong Holders list, balance + % of supply đúng | |
| TC-069H | 🟢 | Multiple BUY — balance cộng dồn | 1. BUY 0.02 SOL token → ghi balance_1<br>2. BUY thêm 0.03 SOL cùng token → ghi balance_2 | balance_2 > balance_1, tổng token nhận ≈ tổng 2 lần BUY | |

## 3.6 — Chi tiết Phí & Settings

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-069I | 🔴 | Slippage thật sự hoạt động | 1. Set slippage = 0.5% (thấp)<br>2. BUY 0.05 SOL<br>3. Nếu PASS → ghi nhận<br>4. Set slippage = 0.1% (rất thấp)<br>5. BUY 0.05 SOL trong lúc có người trade (giá biến động) | Slippage 0.5%: có thể thành công<br>Slippage 0.1%: dễ fail hơn nếu giá biến động → hiện error "Price moved too much" | |
| TC-069J | 🟡 | Anti-MEV — phí tăng thêm khi bật | 1. Ghi lại SOL balance<br>2. BUY 0.05 SOL với Anti-MEV **OFF** → ghi lại SOL bị trừ (= amount + fees_1)<br>3. BUY 0.05 SOL lần nữa với Anti-MEV **ON** → ghi lại SOL bị trừ (= amount + fees_2) | fees_2 > fees_1 (Anti-MEV charge thêm ≈ 0.005 SOL hoặc 0.5%)<br>⛔ MVP: Fees section chưa hiển thị breakdown — cần kiểm tra qua SOL balance thật | |
| TC-069K | 🟡 | Priority Fee — speed levels ảnh hưởng phí | 1. BUY 0.05 SOL với Priority = Normal (Free) → ghi SOL bị trừ<br>2. BUY 0.05 SOL với Priority = Fast → ghi SOL bị trừ<br>3. BUY 0.05 SOL với Priority = Instant → ghi SOL bị trừ | Normal < Fast < Instant (SOL bị trừ tăng dần)<br>Fast thêm ≈ +0.0001 SOL, Instant thêm ≈ +0.0005 SOL<br>⛔ MVP hiện là Auto/Manual, chưa phải Normal/Fast/Instant | |
| TC-069L | 🟡 | Fees breakdown hiển thị đúng | 1. Expand Fees section (nếu có chevron ▼)<br>2. Check nội dung | Hiển thị: Solana network fee (~0.00001 SOL), Anti-MEV fee (nếu ON), Priority fee (nếu Fast/Instant)<br>⛔ MVP chưa có Fees section | |
| TC-069M | 🔴 | Real-time price update | 1. Mở Token Detail, nhìn giá hiện tại trên Trading Panel<br>2. Dùng Account B BUY/SELL token đó (để tạo biến động giá)<br>3. Quay lại Account A, nhìn giá | Giá trên Trading Panel cập nhật (không cần F5), phản ánh giao dịch của Account B | |
| TC-069N | 🟡 | "You Receive" cập nhật khi giá thay đổi | 1. Nhập 0.05 SOL vào BUY → ghi "You Receive" = X<br>2. Đợi vài giây (hoặc Account B trade để tạo biến động)<br>3. Xem "You Receive" có thay đổi không | "You Receive" auto-update khi giá thay đổi, không cần re-type amount | |
| TC-069O | 🟡 | Currency Switch SOL ↔ Token | 1. Nhập 0.05 ở mode SOL<br>2. Click nút switch currency (SOL ⇄ TOKEN)<br>3. Nhập số token ở mode Token | Mode SOL: "You Receive" hiện tokens<br>Mode Token: "You Pay" hiện SOL<br>⛔ MVP chưa có Currency Switch | |
| TC-069P | 🟡 | Ticket reward sau khi trade | 1. BUY token thành công<br>2. Check success modal | Success modal hiện: "🎟️ +1 Reward Ticket earned"<br>Vào Rewards → YOUR TICKETS tăng 1 | |

## 3.7 — Bonding Curve & Graduation (Logic)

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-069Q | 🔴 | Bonding curve — giá tăng sau khi BUY | 1. Ghi lại giá hiện tại của token (Price_1)<br>2. BUY 0.1 SOL<br>3. Ghi lại giá mới (Price_2) | Price_2 > Price_1 (giá tăng theo bonding curve) | |
| TC-069R | 🔴 | Bonding curve — giá giảm sau khi SELL | 1. Ghi lại giá hiện tại (Price_1)<br>2. SELL toàn bộ token<br>3. Ghi lại giá mới (Price_2) | Price_2 < Price_1 (giá giảm khi supply giảm) | |
| TC-069S | 🟡 | Graduation threshold — Progress bar | 1. Xem Progress to DEX bar trên Token Detail<br>2. BUY thêm token → check progress | Progress bar tăng khi MC tăng. Graduation = 100% tại MC $69K | |

---

# FR-004: HỒ SƠ CỦA TÔI (MY PROFILE)

## 4.1 — Page Layout & Access

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-069 | 🔴 | Truy cập My Profile | 1. Connect wallet (Account A)<br>2. Click "My Profile" trên sidebar | Trang Profile mở, hiển thị: Avatar, Username, Wallet address | |
| TC-070 | 🔴 | Redirect khi chưa login | 1. KHÔNG connect wallet<br>2. Truy cập trang Profile | Redirect hoặc yêu cầu connect wallet | |
| TC-071 | 🟡 | Header hiển thị đúng | 1. Vào My Profile | Hiển thị: Avatar, Username (hoặc placeholder), Wallet address rút gọn, Copy button | |
| TC-072 | 🟡 | Copy wallet address | 1. Click Copy button bên cạnh wallet address | Address copied, paste ra đúng | |
| TC-073 | 🟡 | Stats bar hiển thị | 1. Nhìn stats bar | Hiển thị: Portfolio Value, Tokens Created, Total Trades, Member Since | |
| TC-074 | 🟡 | 6 tabs hiển thị đầy đủ | 1. Nhìn tab bar | Có: Profile Info, Holding Tokens, Created Tokens, Transaction History, Arena History, Notifications | |

## 4.2 — Profile Info Tab

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-075 | 🔴 | Edit Profile — set Username | 1. Vào Profile Info tab<br>2. Click "Edit Profile"<br>3. Nhập Username: "uat_tester_01"<br>4. Save | Username được set, hiển thị trên profile. Chỉ set được 1 lần | |
| TC-075A | 🔴 | Username lock — không đổi được sau khi set | 1. Đã set username ở TC-075<br>2. Mở Edit Profile lại<br>3. Thử sửa Username | Field Username bị disabled/locked, không cho sửa | |
| TC-076 | 🟡 | Edit Profile — Bio | 1. Click Edit Profile<br>2. Nhập Bio: "UAT tester bio"<br>3. Save | Bio hiển thị đúng | |
| TC-077 | 🟡 | Edit Profile — Social Links | 1. Click Edit Profile<br>2. Nhập Twitter: "https://x.com/test"<br>3. Nhập Telegram: "https://t.me/test"<br>4. Save | Social links hiển thị icon + URL | |
| TC-078 | 🟡 | Privacy toggle | 1. Vào Profile Info<br>2. Tìm Privacy toggle<br>3. Toggle Private ON<br>4. Toggle Public | Toggle hoạt động, label thay đổi: "Anyone can view..." ↔ Private | |
| TC-079 | 🟡 | Wallet Information hiển thị | 1. Vào Profile Info tab | Hiển thị: Full Wallet Address + COPY, Trading Stats (Total Buys, Total Sells, Total Volume) | |
| TC-080 | 🟡 | Member Since hiển thị | 1. Vào Profile Info | Hiển thị đúng tháng/năm (ví dụ: "Apr 2026") | |

## 4.3 — Holding Tokens Tab

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-081 | 🔴 | Hiển thị tokens đang hold | 1. Đảm bảo Account A đang hold ≥ 1 token (đã BUY ở TC-051)<br>2. Vào Holding Tokens tab | Danh sách tokens: Avatar, Name + Symbol, Balance, Value, Current Price, 24h Change, P&L | |
| TC-082 | 🟡 | P&L hiển thị đúng màu | 1. Nhìn P&L column | Profit: xanh lá + dấu +, Loss: đỏ + dấu -, Neutral: xám | |
| TC-082A | 🔴 | P&L tính đúng công thức | 1. Ghi lại: giá lúc BUY (avg purchase price), số token hold (balance), giá hiện tại<br>2. Tính tay: Cost Basis = avg price × balance, Current Value = current price × balance, P&L = Current Value - Cost Basis, P&L% = (P&L / Cost Basis) × 100<br>3. So sánh với P&L hiển thị trên UI | P&L amount và P&L % khớp với tính tay (sai lệch chấp nhận ≤ 1%) | |
| TC-083 | 🟡 | Click token → Token Detail | 1. Click vào token trong danh sách | Navigate tới Token Detail | |
| TC-084 | 🟢 | Empty state | 1. Dùng account chưa hold token nào | Hiển thị "No holding tokens." | |
| TC-085 | 🟢 | Portfolio Stats | 1. Nhìn phía trên danh sách | Total Value, 24h Change, Total P&L hiển thị | |

## 4.4 — Created Tokens Tab

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-086 | 🟡 | Hiển thị tokens đã tạo | 1. Vào Created Tokens tab (sau khi đã tạo token ở FR-007) | Danh sách: Avatar, Name + Symbol, Created date, Status, MC, Holders, Volume | |
| TC-087 | 🟢 | Join Arena toggle | 1. Tìm toggle "Join Arena" bên cạnh token | Toggle ON/OFF, sub-label thay đổi | |
| TC-088 | 🟢 | Empty state | 1. Account chưa tạo token nào | Hiển thị "No created tokens." | |

## 4.5 — Transaction History Tab

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-089 | 🟡 | Transaction history hiển thị | 1. Vào Transaction History tab (sau khi đã trade) | Danh sách: BUY/SELL badge, Token info, Timestamp, Amount, Value, TX Hash | |
| TC-090 | 🟡 | TX Hash link | 1. Click TX Hash | Mở Solana Explorer đúng transaction | |
| TC-091 | 🟢 | Empty state | 1. Account chưa trade | "No transactions yet" + "Start trading to see your history" | |

## 4.6 — Arena History Tab

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-092 | 🟡 | Arena history hiển thị | 1. Vào Arena History tab | Hiển thị: Stats (Total Bets, Wins, Losses, Total Payout) + Bet list | |
| TC-093 | 🟢 | Bet item hiển thị đúng | 1. Xem bet item (nếu có) | Icon trạng thái (WON/LOST/LIVE), title, pick, bet amount, payout | |
| TC-094 | 🟢 | Empty state | 1. Chưa bet | "No arena bets yet" | |

## 4.7 — Notifications Tab

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-095 | 🟡 | Notifications hiển thị | 1. Vào Notifications tab | Danh sách notifications: icon, title, description, timestamp | |
| TC-096 | 🟡 | Badge count unread | 1. Nhìn tab Notifications | Badge hiển thị số unread | |
| TC-097 | 🟢 | Click notification → mark as read | 1. Click vào notification unread | Background đổi, red dot biến mất | |
| TC-098 | 🟢 | Empty state | 1. Chưa có notification | "No notifications yet" | |

---

# FR-005: HỒ SƠ CÔNG KHAI (PUBLIC PROFILE)

## 5.1 — Xem Profile người khác

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-099 | 🔴 | Truy cập Public Profile | 1. Từ Token Detail, click vào tên trader trong tab Trades (hoặc holder trong tab Holders) | Trang profile người đó mở, hiển thị: Avatar, Username, Wallet, Stats | |
| TC-100 | 🔴 | Không cần login để xem | 1. KHÔNG connect wallet<br>2. Truy cập trực tiếp URL /profile/[wallet_address] | Trang hiển thị bình thường, không yêu cầu login | |
| TC-101 | 🔴 | Owner vs Visitor — ẩn Edit Profile | 1. Connect wallet Account A<br>2. Truy cập profile Account B | KHÔNG hiển thị nút "Edit Profile"<br>KHÔNG hiển thị Trading Stats (Total Buys/Sells/Volume)<br>⛔ MVP hiện chưa phân biệt owner vs visitor | |
| TC-102 | 🟡 | 4 tabs hiển thị | 1. Vào public profile người khác | Có 4 tabs: Profile Info, Holding Tokens, Created Tokens, Transaction History<br>(KHÔNG có Arena History, Notifications) | |

## 5.2 — Private Profile

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-103 | 🔴 | Private Profile handling | 1. Account B: set profile Private<br>2. Account A: truy cập Public Profile của Account B | Hiển thị: Avatar + Username + Wallet + Lock icon 🔒<br>Message: "This profile is private"<br>Ẩn toàn bộ tabs + stats<br>⛔ MVP chưa implement logic ẩn profile | |
| TC-104 | 🟡 | Wallet address vẫn copyable khi private | 1. Ở private profile<br>2. Click Copy wallet | Vẫn copy được wallet address | |

---

# FR-006: CREATOR DASHBOARD


## 6.1 — Dashboard Overview (MVP chưa làm)

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-105 | 🟡 ⛔ | Truy cập Creator Dashboard | 1. Connect wallet<br>2. Click "Creator Dashboard" trên sidebar | Trang mở, hiển thị: Title "Creator Dashboard", 2 tabs (Created Tokens, Creator Revenue). Default: Created Tokens | |
| TC-106 | 🟡 ⛔ | Login required | 1. KHÔNG connect wallet<br>2. Truy cập Dashboard | Redirect / yêu cầu connect wallet | |

## 6.2 — Created Tokens Tab

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-107 | 🟡 ⛔ | Danh sách tokens đã tạo | 1. Vào Created Tokens tab | Danh sách: Avatar, Name + Symbol, Created date, Status badge (Active/Graduated), "Manage Token" button | |
| TC-108 | 🟡 ⛔ | Click Manage Token | 1. Click "Manage Token" | Navigate tới Token Management page | |

## 6.3 — Creator Revenue Tab

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-109 | 🟡 ⛔ | Revenue overview | 1. Click tab Creator Revenue | Hiển thị: Total Revenue, Unclaimed Revenue, Total Claimed | |
| TC-110 | 🟡 ⛔ | Claim Revenue | 1. Khi có unclaimed revenue<br>2. Click "Claim X.X SOL"<br>3. Approve wallet | SOL chuyển về wallet, Unclaimed giảm, Total Claimed tăng | |

## 6.4 — Token Management

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-111 | 🟡 ⛔ | Token Management — 3 tabs | 1. Vào Token Management | Có 3 tabs: Overview, Trusted Level, Community Management | |
| TC-112 | 🟡 ⛔ | Overview tab — Metrics | 1. Click tab Overview | Hiển thị 6 metrics: MC, Price, 24h Volume, Holders, Total Supply, Liquidity | |
| TC-113 | 🟡 ⛔ | Trusted Level — LP Lock | 1. Click tab Trusted Level<br>2. Toggle LP Lock ON | LP Lock enabled, confirmation hiện | |
| TC-114 | 🟡 ⛔ | Trusted Level — Freeze Authority | 1. Toggle Disable Freeze Authority ON | Warning: permanent action. Sau confirm → freeze disabled | |
| TC-115 | 🟡 ⛔ | Community — Create Post | 1. Click tab Community Management<br>2. Click "+ Create New Post"<br>3. Title: "Welcome to TestSeed"<br>4. Content: "This is our first community post"<br>5. Click Create | Post xuất hiện trong list | |
| TC-116 | 🟢 ⛔ | Community — Pin Post | 1. Click Pin trên post<br>2. Pin thêm 1 post khác | Post pinned hiện đầu, pin post mới → post cũ unpin (max 1) | |
| TC-117 | 🟢 ⛔ | Community — Delete Post | 1. Click Delete trên post<br>2. Confirm | Post bị xoá, confirmation modal hiện trước khi xoá | |

---

# FR-007: TẠO TOKEN

## 7.1 — Overall Flow

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-118 | 🔴 | Truy cập Create Token | 1. Connect wallet (Account A)<br>2. Click "Create Token" trên sidebar | Trang Create Token mở, hiển thị Step 1 (Basic Info), progress indicator | |
| TC-119 | 🔴 | Yêu cầu login | 1. KHÔNG connect wallet<br>2. Click Create Token | Yêu cầu connect wallet | |

## 7.2 — Step 1: Basic Info

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-120 | 🔴 | Nhập đầy đủ Basic Info | 1. Token Name: "TestSeed UAT"<br>2. Symbol: "TSUAT"<br>3. Statement: "The best test token ever made"<br>4. Description: "Token tạo để UAT, không có giá trị thật"<br>5. Upload Avatar (chọn ảnh bất kỳ)<br>6. (Tuỳ chọn) Website: "https://example.com"<br>7. Click Next | Pass validation, chuyển sang Step 2 | |
| TC-121 | 🟡 | Validation — Token Name trống | 1. Để Token Name trống<br>2. Click Next | Hiện error inline, không cho Next | |
| TC-122 | 🟡 | Validation — Symbol trống | 1. Để Symbol trống<br>2. Click Next | Hiện error, không cho Next | |
| TC-122A | 🟡 | Validation — Symbol đã tồn tại | 1. Nhập Symbol trùng với token đã có trên hệ thống<br>2. Click Next | Hiện error: "Symbol already exists" hoặc tương tự. Không cho tạo trùng | |
| TC-122B | 🟡 | Avatar upload bắt buộc | 1. Điền đầy đủ Name, Symbol, Statement, Description<br>2. KHÔNG upload avatar<br>3. Click Next | Hiện error: avatar là bắt buộc, không cho Next | |
| TC-123 | 🟡 | Validation — Symbol quá dài | 1. Nhập Symbol > 10 ký tự<br>2. Click Next | Không cho nhập quá 10 ký tự hoặc hiện error | |
| TC-124 | 🟡 | Symbol auto uppercase | 1. Nhập symbol: "tsuat" (chữ thường) | Tự động chuyển thành "TSUAT" | |
| TC-125 | 🟡 | Character counter | 1. Nhập Token Name<br>2. Nhập Statement<br>3. Nhập Description | Mỗi ô hiển thị số ký tự đã nhập / số ký tự tối đa (VD: Token Name 10/32, Statement 10/60, Description 10/200) | |
| TC-126 | 🟢 | NSFW toggle | 1. Check "Mark as NSFW" | Toggle ON, token sẽ bị ẩn với user chưa bật NSFW | |
| TC-126A | 🟡 | NSFW token bị ẩn trong Token List | 1. Tạo token với NSFW = ON<br>2. Về Token List với NSFW filter = OFF | Token vừa tạo KHÔNG hiện trong list.<br>Bật NSFW filter ON → token hiện lại | |
| TC-127 | 🟢 | Social Links — URL validation | 1. Nhập Website: "abcxyz" (không phải URL) | Hiện error: invalid URL format | |

## 7.3 — Step 2: Security Settings (Advance Info)

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-128 | 🟡 | Security Settings hiển thị | 1. Hoàn thành Step 1<br>2. Click Next → Step 2 | Hiển thị toggles: LP Lock (default ON), Request Audit (default OFF), Disable Freeze Authority (default OFF) | |
| TC-129 | 🟡 | Toggle LP Lock | 1. Toggle LP Lock OFF rồi ON lại | Toggle hoạt động, trust score impact hiển thị | |
| TC-130 | 🟢 | Freeze Authority warning | 1. Toggle Disable Freeze Authority ON | Hiện warning: permanent action | |

## 7.4 — Step 3: Initial Buy

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-131 | 🔴 | Initial Buy — nhập amount | 1. Hoàn thành Step 2 → Next<br>2. Nhập: 0.1 SOL | "You will receive ~XXX,XXX tokens" hiển thị | |
| TC-132 | 🟡 | Quick amounts | 1. Click 0.1 SOL / 0.5 SOL / 1 SOL | Amount tự điền | |
| TC-133 | 🟡 | Skip initial buy | 1. Click Skip | Không mua, chuyển sang bước tiếp (hoặc tạo luôn) | |
| TC-134 | 🟡 | Balance check | 1. Nhập số SOL lớn hơn balance | Hiện error hoặc button disabled | |

## 7.5 — Review & Create

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-135 | 🔴 | Review screen hiển thị | 1. Hoàn thành Step 3 → Next | Summary card hiển thị: Avatar, Token Name, Symbol, Statement, LP Lock status, Initial Buy amount<br>⛔ MVP không có Review step — tạo luôn sau Step 3 | |
| TC-136 | 🔴 | Create Token thành công | 1. Click "Create Token 🚀" (hoặc final button)<br>2. Approve transaction trên Phantom | ✅ Token được tạo thành công<br>Success screen: 🎉 "Token Created Successfully!", contract address, actions | |
| TC-137 | 🟡 | Success — View Token Detail | 1. Sau khi tạo thành công<br>2. Click "View Token Detail" | Navigate tới Token Detail page của token vừa tạo | |
| TC-138 | 🟢 | Success — Copy address | 1. Click Copy bên cạnh contract address | Address copied đúng | |

## 7.6 — Navigation

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-139 | 🟡 | Previous button | 1. Ở Step 2<br>2. Click Previous | Quay lại Step 1 với data đã nhập giữ nguyên | |
| TC-140 | 🟡 | Progress indicator | 1. Đi qua từng step | Progress bar update đúng: Active (current), Completed (checkmark), Pending (grey) | |

---

# FR-008: BẢNG XẾP HẠNG (LEADERBOARD)

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-141 | 🟡 | Truy cập Leaderboard | 1. Click "Leaderboard" trên sidebar | Trang mở, title "Leaderboard" | |
| TC-142 | 🟡 | Top 3 featured cards | 1. Nhìn phần trên trang | 3 cards nổi bật: #1, #2, #3 (nếu có data) | |
| TC-143 | 🟡 | Table list #4+ | 1. Scroll xuống dưới Top 3 | Bảng compact: Rank, Token info, MC, Volume... cho tokens xếp hạng #4 trở đi | |
| TC-144 | 🟡 | Click token → Detail | 1. Click vào token trong leaderboard | Navigate tới Token Detail | |
| TC-145 | 🟢 | Empty state | 1. Nếu chưa có data | Hiển thị "No data" hoặc tương tự | |

---

# FR-009: PHẦN THƯỞNG & GAMES (REWARDS)

## 9.1 — Page Layout

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-146 | 🟡 | Truy cập Rewards | 1. Connect wallet<br>2. Click "Rewards" trên sidebar | Trang mở: Broadcast banner, Title "Rewards", 3 tabs (Slot Machine, Lucky Wheel, Club Rewards) | |
| TC-147 | 🟢 | Broadcast banner | 1. Nhìn banner trên cùng | Scrolling text: "[user] won X.XXX SOL Xd ago" | |

## 9.2 — Slot Machine

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-148 | 🟡 | Slot Machine tab hiển thị | 1. Click tab Slot Machine | Hiển thị: SLOT REWARD card + YOUR TICKETS card + 5 reels | |
| TC-149 | 🔴 | Spin slot machine | 1. Đảm bảo có ≥ 1 ticket<br>2. Click SPIN | 5 reels quay, dừng, hiện kết quả. Win/Lose hiển thị đúng | |
| TC-149A | 🟡 | Spin — không có ticket | 1. Đảm bảo tickets = 0<br>2. Click SPIN | SPIN button disabled hoặc hiện "Not enough tickets" | |
| TC-149B | 🟡 | Spin — payout tính đúng khi thắng | 1. Spin và thắng (3+ symbols giống nhau)<br>2. Ghi lại: symbol nào, bao nhiêu match<br>3. Tính tay: base reward × symbol multiplier × match multiplier<br>4. So sánh với payout hiển thị | Payout khớp công thức:<br>3 same = 1× match, 4 same = 2× match, 5 same = 5× match<br>Symbol multipliers: Seed ×1, Leaf ×1.5, Clover ×2, Flower ×3, Flame ×5, Gem ×10, Star ×25 | |
| TC-150 | 🟡 | Claim reward | 1. Khi có slot reward > 0<br>2. Click CLAIM<br>3. Approve wallet signature | SOL chuyển về wallet (check Phantom balance tăng), SLOT REWARD reset về 0 | |
| TC-151 | 🟡 | Convert Points → Tickets | 1. Có đủ points<br>2. Tìm section Convert<br>3. Click Convert | Points giảm, Tickets tăng | |
| TC-151A | 🟡 | Convert — không đủ points | 1. Points = 0 hoặc quá thấp<br>2. Thử Convert | Hiện "Not enough points to convert tickets." | |
| TC-152 | 🟢 | Spin history | 1. Scroll xuống History | Table: Time, Bet, Result, Payout hiển thị | |
| TC-153 | 🟢 | Winning rules hiển thị | 1. Tìm section Rules | 7 symbols và multipliers hiển thị đúng | |

## 9.3 — Club Rewards

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-154 | 🟡 | Club Rewards tab hiển thị | 1. Click tab Club Rewards | 3 stats: Club Points, Redeemed, Available | |
| TC-155 | 🟢 | Auto Rewards tiers | 1. Nhìn Auto Rewards section | 8 tiers hiển thị: từ Extra Spin Ticket (100pts) đến Club Treasury Share (3000pts) | |
| TC-156 | 🟢 | Reward History | 1. Scroll xuống | Table: Date, Reward, Contribution, Status | |

---

# FR-010: GIỚI THIỆU (REFERRALS)

## 10.1 — Page Layout & Generate Link

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-157 | 🔴 | Truy cập Referrals | 1. Connect wallet (Account A)<br>2. Click "Referrals" trên sidebar | Trang mở: Title "Referrals", 3 stats cards, Referral Link section | |
| TC-158 | 🔴 | Generate Referral Link | 1. Click "🔗 GENERATE LINK" | Link unique được tạo, hiển thị https://[domain]/ref/[code] | |
| TC-159 | 🟡 | Copy referral link | 1. Click Copy bên cạnh link | Link copied, hiện "✓ Copied!" (2 giây) | |

## 10.2 — Referral Flow

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-160 | 🔴 | Referred user đăng ký qua link | 1. Account A tạo referral link<br>2. Account B mở link referral<br>3. Account B connect wallet | Account B được ghi nhận là referred. Referrals table hiện Account B | |
| TC-161 | 🟡 | Stats cards cập nhật | 1. Account B trade (mua token)<br>2. Account A vào Referrals | Total Referrals tăng 1, Total Volume cập nhật | |
| TC-162 | 🟡 | Claim Reward | 1. Khi có Unclaimed Rewards > 0<br>2. Click "CLAIM REWARD"<br>3. Approve wallet | SOL chuyển về wallet | |
| TC-162A | 🔴 | Earnings tính đúng công thức | 1. Account B trade 1 SOL (via referral link Account A)<br>2. Tính tay: Trading fee = 1 SOL × 1% = 0.01 SOL, Referrer earnings = 0.01 × 20% = 0.002 SOL<br>3. Account A vào Referrals → check Unclaimed Rewards | Unclaimed Rewards ≈ 0.002 SOL (có thể ± do rounding).<br>Công thức: Volume × 1% (fee) × 20% (referrer share) | |

## 10.3 — Referred Users Table

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-163 | 🟡 | Table hiển thị đúng | 1. Vào Referrals (đã có referred user) | 4 columns: Date Joined, Wallet, Trading Volume, Your Rewards | |
| TC-164 | 🟢 | Empty state | 1. Chưa refer ai | "Share your referral link to start earning" | |

---

# FR-011: ĐIỂM THƯỞNG (POINTS)

## 11.1 — Page Layout

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-165 | 🟡 | Truy cập Point System | 1. Connect wallet<br>2. Click "Point System" trên sidebar | Trang mở: Title, Wallet, 3 tabs (Daily Point, Trading Volume, Club Mission), Rank Card | |
| TC-166 | 🟡 | Rank Card hiển thị | 1. Nhìn Rank Card | Tier + Rank Name + Progress bar + "X points away from next tier" | |
| TC-167 | 🟡 | Header stats thay đổi theo tab | 1. Click Daily Point → check header stats<br>2. Click Trading Volume → check header stats<br>3. Click Club Mission → check header stats | Stats thay đổi phù hợp từng tab | |

## 11.2 — Daily Point Tab

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-168 | 🟡 | Daily Point history | 1. Click tab Daily Point | Table: DATE, TYPE, POINTS hiển thị | |
| TC-168A | 🔴 | Trade Points tính đúng công thức | 1. Account A BUY 0.1 SOL token<br>2. Đợi hệ thống tính points<br>3. Vào Daily Point tab → check record mới | Trade Points = Volume × 5.<br>Ví dụ: trade 0.1 SOL → nhận 0.5 pts (hoặc theo tỷ giá USD nếu volume tính USD) | |
| TC-168B | 🟡 | Token Creation Points tính đúng | 1. Tạo token mới (đã upload avatar + full description)<br>2. Check Daily Points | Nhận ≈ 30 pts (20 create + 10 upload+description).<br>Max 80 pts nếu đạt cả Trust Score + 10 first buys | |
| TC-168C | 🔴 | Tier progression — lên rank khi đủ points | 1. Kiếm đủ 500 points (Tier 2: Sprout threshold)<br>2. Xem Rank Card | Rank đổi từ 🌱 Seed → 🌿 Sprout.<br>Nhận reward: 🎁 1 Ticket + 0.005 SOL | |
| TC-169 | 🟢 | Empty state | 1. Chưa có hoạt động | "You'll see your point history here" + "Nothing yet? Switch wallets or trade to earn Seed Points." | |

## 11.3 — Trading Volume Tab

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-170 | 🟡 | Trading Volume stats | 1. Click tab Trading Volume | 4 stats cards: MY VOLUME, MY TRADES, MY RANK, TRADING POINTS | |
| TC-171 | 🟡 | Volume Milestones | 1. Nhìn Milestones section | 5 tiers với progress bars: Starter, Active Trader, Power Trader, Whale, Legend | |
| TC-172 | 🟡 | Volume Leaderboard | 1. Scroll xuống | Table: RANK, WALLET, VOLUME, TRADES, REWARD — top 10 | |
| TC-173 | 🟢 | Rewards Banner → Go to Wheel | 1. Click "Go to Wheel" trong banner | Navigate tới Rewards page, Lucky Wheel tab | |

## 11.4 — Club Mission Tab

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-174 | 🟡 | Club Mission hiển thị | 1. Click tab Club Mission (cần đang ở trong 1 club) | Club info card, 7 Weekly Missions với progress bars | |
| TC-175 | 🟢 | Mission progress bar | 1. Nhìn missions | Mỗi mission: tên + mô tả + points + progress X/Y + time left | |
| TC-176 | 🟢 | Club Mission Leaderboard | 1. Scroll xuống | Table: RANK, CLUB, POINTS, MISSIONS, MEMBERS | |

---

# FR-012: ARENA / PREDICTION MARKET

> ⛔ Có thể chưa đầy đủ các loại Arena

## 12.1 — Page Layout

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-177 | 🔴 | Truy cập Arena | 1. Click "Arena" trên sidebar | Trang mở, hiển thị 6 tabs: Live, Duel, Target, Sports, Higher/Lower, Events | |
| TC-178 | 🟡 | Tab Live (default) | 1. Tab Live active mặc định | Hiển thị tất cả kèo đang diễn ra, có Arena Cards | |

## 12.2 — Arena Card

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-179 | 🟡 | Arena Card hiển thị đúng | 1. Nhìn Arena Card trong tab Live | Có: Tiêu đề câu hỏi, Loại kèo badge, Progress bar tỷ lệ, Pool size, Time remaining, Bet buttons | |

## 12.3 — Đặt cược

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-180 | 🔴 | Đặt cược vào kèo | 1. Connect wallet (Account A)<br>2. Chọn kèo bất kỳ đang LIVE<br>3. Chọn cửa (ví dụ: YES)<br>4. Nhập 0.05 SOL<br>5. Confirm bet | ✅ Bet placed, SOL trừ từ wallet, tỷ lệ pool cập nhật | |
| TC-181 | 🟡 | Min bet = 0.01 SOL | 1. Nhập 0.005 SOL<br>2. Submit | Không cho bet, hiện lỗi: minimum 0.01 SOL | |
| TC-182 | 🟡 | Odds floor 1.3x | 1. Trong kèo, nếu 1 cửa chiếm > 73% pool | Cửa đó bị đóng (không cho bet thêm) | |

## 12.4 — Các tab Arena

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-183 | 🟡 | Tab Duel | 1. Click tab ⚔️ Duel | Hiển thị các kèo 2 token đua nhau, format Race | |
| TC-184 | 🟡 | Tab Target | 1. Click tab 🎯 Target | Hiển thị kèo dự đoán 1 token, có 3 sub-format: Yes/No, Where, When | |
| TC-185 | 🟡 | Tab Sports | 1. Click tab ⚽ Sports | Hiển thị kèo thể thao (nếu có) | |
| TC-186 | 🟡 | Tab Higher/Lower | 1. Click tab 📈 Higher/Lower | Hiển thị kèo giá crypto: up/down, timeframe 1h/4h/24h | |
| TC-187 | 🟡 | Tab Events | 1. Click tab 🎭 Events | Hiển thị kèo sự kiện thế giới: binary hoặc multi-choice | |

## 12.5 — Resolution & Payout

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-188 | 🔴 | Kèo resolved — WIN | 1. Sau khi kèo kết thúc và bạn thắng | Payout tính đúng: (bet / winning side total) × total pool × 0.95 (trừ 5% fee) | |
| TC-189 | 🟡 | Kèo resolved — LOSE | 1. Sau khi kèo kết thúc và bạn thua | Mất SOL đã bet, status "LOST" | |

---

# FR-013: EVENTS & QUESTS

## 13.1 — Page Layout

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-190 | 🟡 | Truy cập Events | 1. Click "Events" trên sidebar | Trang mở: Title "Events", Stats "X live · Y upcoming", 4 tabs (All, Live, Upcoming, Ended) | |
| TC-191 | 🟡 | 4 tabs hoạt động | 1. Click từng tab | All: tất cả events, Live: đang diễn ra, Upcoming: sắp tới, Ended: đã kết thúc | |
| TC-192 | 🟡 | Live badge count | 1. Nhìn tab Live | Badge hiển thị số event đang live | |

## 13.2 — Event Cards

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-193 | 🟡 | Event Card hiển thị đúng | 1. Nhìn Event Card bất kỳ | Có: Gradient background, Badge (NEW/HOT), Tên event, Mô tả, Status, Joined count, "Join >" button | |
| TC-194 | 🔴 | Join event | 1. Connect wallet<br>2. Click "Join >" trên event card | Tham gia event thành công, Joined count tăng | |
| TC-195 | 🟢 | Event mẫu hiển thị | 1. Tìm trong danh sách | Có: Daily Quest, Daily Referrals, Trading Volume Challenge (hoặc tương tự) | |

---

# FR-014: CLUBS

## 14.1 — Page Layout

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-196 | 🟡 | Truy cập Clubs | 1. Click "Clubs" trên sidebar | Trang mở: Title "Clubs", Stats "X clubs · X.XK members", Top 3 banner, Category tabs, Sort + Search | |
| TC-197 | 🟡 | Top 3 Banner | 1. Nhìn phần trên trang | 3 cards: #1 #2 #3 với Avatar, Name, Tag, Stats (Members, WR, Pts/Week) | |
| TC-198 | 🟡 | 7 Category tabs | 1. Click từng tab | All, Token Club, Creator, Meme, Football, Anime, Shitpost — mỗi tab filter đúng | |
| TC-199 | 🟡 | Search clubs | 1. Gõ tên club vào search<br>2. Enter | Kết quả filter theo tên | |

## 14.2 — Club Card

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-200 | 🟡 | Club Card hiển thị đúng | 1. Nhìn Club Card | Có: Avatar, Rank #X, Name + Tag, Description, Tags, 4 stats (Members, Win Rate, Pts/Week, Level) | |
| TC-201 | 🟢 | Age badge | 1. Nhìn góc trên phải Card | Badge hiển thị tuổi club: "Xw" | |

## 14.3 — Create Club

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-202 | 🔴 | Create Club | 1. Connect wallet<br>2. Click "+ Create Club"<br>3. Điền: Name: "UAT Test Club", Tag: "UAT", Description: "Club để test UAT", Category: Meme<br>4. Upload avatar<br>5. Submit | Club được tạo, hiển thị trong danh sách Clubs | |
| TC-203 | 🟡 | Vào Club đã tạo | 1. Click vào club vừa tạo | Trang club detail mở (nếu có) | |

---

# CROSS-MODULE TEST CASES (E2E)

## E2E — End-to-End Happy Path

| # | Priority | Test Case | Steps | Expected | Kết quả |
|---|---|---|---|---|---|
| TC-E01 | 🔴 | Full flow: Connect → Create Token → Buy → Sell → Check Profile | 1. Connect wallet Account A<br>2. Create Token "TestSeed UAT" (TSUAT), initial buy 0.1 SOL<br>3. Vào Token Detail → verify chart, metadata<br>4. BUY thêm 0.05 SOL<br>5. SELL 50% holdings<br>6. Vào My Profile → Holding Tokens tab<br>7. Check transaction history | Mỗi bước hoàn thành, data đồng bộ giữa các trang | |
| TC-E02 | 🔴 | Referral flow: Account A refer Account B | 1. Account A: Generate referral link<br>2. Account B: Mở link, connect wallet<br>3. Account B: BUY token 0.1 SOL<br>4. Account A: Vào Referrals, check stats | Account B hiện trong table, volume + rewards cập nhật | |
| TC-E03 | 🟡 | Chat flow: 2 accounts chat | 1. Account A: Vào token detail → Chat → gửi "Hello from A"<br>2. Account B: Vào cùng token → Chat → gửi "Hi from B" | Cả 2 messages hiển thị, đúng username, đúng timestamp | |
| TC-E04 | 🟡 | Profile Privacy flow | 1. Account B: Set profile Private<br>2. Account A: Truy cập profile Account B | Account A chỉ thấy: Avatar + Username + Wallet + 🔒 "This profile is private"<br>⛔ MVP chưa implement logic ẩn | |
| TC-E05 | 🟡 | Rewards flow: Trade → Earn Ticket → Spin | 1. Account A: BUY token (earn trading points)<br>2. Vào Point System → verify points tăng<br>3. Vào Rewards → Convert points → tickets<br>4. Spin slot machine | Points → Tickets → Spin → kết quả hiển thị đúng | |
| TC-E06 | 🔴 | Data consistency — MC/Volume/Holders khớp giữa các trang | 1. Vào Token Detail → ghi MC, Volume, Holders<br>2. Quay lại Token List → tìm cùng token → ghi MC, Volume<br>3. Vào Leaderboard (nếu token nằm trong top) → ghi MC | MC, Volume, Holders phải khớp nhau giữa Token Detail, Token List, và Leaderboard (cho phép delay vài giây) | |
| TC-E07 | 🟡 | Token graduation flow | 1. Tạo token<br>2. BUY đủ để MC đạt gần $69K<br>3. BUY thêm để vượt $69K | Token graduated:<br>- Progress bar = 100%<br>- Status đổi thành "Graduated"<br>- Token hiện trong tab Graduated trên Token List<br>- Token hiện trên Leaderboard (nếu đủ rank) | |
| TC-E08 | 🟡 | Notification sinh ra sau actions | 1. BUY token → check Notifications tab<br>2. Spin reward → check Notifications<br>3. Join event → check Notifications | Mỗi action tạo notification tương ứng:<br>📈 Trading (Buy/Sell), 🎁 Rewards (Spin), ○ Events (Join) | |

---

# TÓM TẮT

| Module | Số Test Cases | Critical | High | Medium |
|---|---|---|---|---|
| Global Components (G1-G4) | 13 | 1 | 5 | 7 |
| FR-001: Token List | 33 | 3 | 11 | 19 |
| FR-002: Token Detail | 24 | 5 | 10 | 9 |
| FR-003: Buy/Sell | 37 | 11 | 18 | 8 |
| FR-004: My Profile | 32 | 6 | 16 | 10 |
| FR-005: Public Profile | 6 | 3 | 1 | 2 |
| FR-006: Creator Dashboard ⛔ | 13 | 0 | 12 | 1 |
| FR-007: Create Token | 26 | 5 | 15 | 6 |
| FR-008: Leaderboard | 5 | 0 | 4 | 1 |
| FR-009: Rewards | 14 | 1 | 8 | 5 |
| FR-010: Referrals | 9 | 4 | 3 | 2 |
| FR-011: Points | 15 | 2 | 8 | 5 |
| FR-012: Arena ⛔ concept | 13 | 3 | 8 | 2 |
| FR-013: Events | 6 | 1 | 4 | 1 |
| FR-014: Clubs | 8 | 1 | 6 | 1 |
| E2E Cross-Module | 8 | 3 | 5 | 0 |
| **TỔNG** | **~262** | **~49** | **~134** | **~79** |

---


