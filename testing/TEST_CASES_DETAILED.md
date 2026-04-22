# TEST CASES CHI TIẾT - PUMPFUN CLONE

**Tổng:** ~290 TCs | **Format:** Điều kiện → Bước thực hiện → Kết quả mong đợi

---

## TỔNG QUAN CATEGORIES

| # | Category | TCs | Mục đích |
|---|----------|-----|----------|
| 1 | [Chức năng](#1-kiểm-thử-chức-năng) | ~230 | Verify FR-001 → FR-011 |
| 2 | [Bảo mật](#2-kiểm-thử-bảo-mật) | ~27 | XSS, Injection, Auth, Blockchain |
| 3 | [Hiệu năng](#3-kiểm-thử-hiệu-năng) | 10 | Load, Stress, Response time |
| 4 | [Tương thích Ví](#4-kiểm-thử-tương-thích-ví) | 1 | Phantom, Solflare, Backpack, Ledger |
| 5 | [Hồi quy](#5-kiểm-thử-hồi-quy-20-tcs) | 20 | Ngăn regression critical path |

---

# 1. KIỂM THỬ CHỨC NĂNG

---

## FR-001: Token List (20 TCs)

**TC-TL-001: Hiển thị danh sách mặc định**
- **Pre:** Có ≥20 tokens trong hệ thống
- **Steps:** Mở trang Token List
- **Expected:**
  - Tab "Discover" đang active
  - Hiển thị 20 tokens dạng grid
  - Mỗi card có: Avatar, Name, Symbol, Statement, MC, Price, Volume, Creator, nút Buy
  - Có pagination

**TC-TL-002: Chuyển tab**
- **Pre:** Đã Connect Wallet (cho tab Favorites)
- **Steps:** Lần lượt click các tab: Trending → New → Graduated → My Favorites
- **Expected:**
  - Trending: Sort theo volume giảm dần
  - New: Sort theo ngày tạo mới nhất
  - Graduated: Chỉ tokens MC ≥ $69K
  - Favorites: Chỉ tokens đã favorite

**TC-TL-003: Tìm kiếm theo tên**
- **Pre:** Token "Pepe Coin" tồn tại
- **Steps:** Nhập "Pepe" vào search box → Enter
- **Expected:** Chỉ hiển thị tokens có "pepe" trong tên (case-insensitive), kết quả real-time

**TC-TL-004: Tìm kiếm theo symbol**
- **Pre:** Token symbol "PEPE" tồn tại
- **Steps:** Nhập "PEPE" vào search → Enter
- **Expected:** Hiển thị token có symbol "PEPE"

**TC-TL-005: Lọc theo MC range**
- **Steps:** Click Filter → Set Min MC: 10,000 / Max MC: 50,000 → Apply
- **Expected:** Chỉ hiển thị tokens MC trong khoảng $10K-$50K

**TC-TL-006: Sắp xếp theo MC**
- **Steps:** Click Sort → "Market Cap (High to Low)"
- **Expected:** Tokens sắp xếp MC giảm dần

**TC-TL-007: Lọc NSFW**
- **Pre:** Có tokens NSFW
- **Steps:** Filter → Toggle "Show NSFW" OFF → Apply
- **Expected:** Ẩn tất cả tokens NSFW

**TC-TL-008: Click card → Token Detail**
- **Steps:** Click vào token card
- **Expected:** Navigate đến trang Token Detail đúng token

**TC-TL-009: Quick Buy từ card**
- **Pre:** Đã Connect Wallet, có ≥0.1 SOL
- **Steps:** Click nút "Buy" trên card
- **Expected:** Mở Trading Panel modal, token info đã điền sẵn, tab Buy active

**TC-TL-010: Kết quả tìm kiếm rỗng**
- **Steps:** Search "xyz123abc"
- **Expected:** Message "No tokens found", gợi ý clear filters

**TC-TL-011: Lọc theo Trust Score**
- **Steps:** Filter → Min Trust Score: 50 → Apply
- **Expected:** Chỉ tokens Trust Score ≥50

**TC-TL-012: Sắp xếp theo Volume 24h**
- **Steps:** Sort → "Volume 24h (High to Low)"
- **Expected:** Sort theo volume giảm dần

**TC-TL-013: Sắp xếp theo Price**
- **Steps:** Sort → "Price (High to Low)"
- **Expected:** Sort theo giá giảm dần

**TC-TL-014: Pagination**
- **Pre:** Có >20 tokens
- **Steps:** Click "Next" → Click "Previous"
- **Expected:** Chuyển trang đúng, data load đúng

**TC-TL-015: Refresh danh sách**
- **Steps:** Click nút Refresh
- **Expected:** Reload danh sách với data mới nhất

**TC-TL-016: Filter kết hợp**
- **Steps:** Filter: MC 10K-50K + Trust Score ≥50 → Apply
- **Expected:** Tokens thỏa cả 2 điều kiện

**TC-TL-017: Clear all filters**
- **Pre:** Đã apply filters
- **Steps:** Click "Clear All"
- **Expected:** Xóa tất cả filters, hiển thị full list

---

## FR-002: Token Detail

**TC-TD-001: Hiển thị đầy đủ thông tin**
- **Steps:** Mở trang Token Detail
- **Expected:**
  - Header: Avatar, Name, Symbol, Statement, Description
  - Stats: MC, Price, 24h Volume, Holders, Liquidity, Trust Score
  - Chart, Community chat, Holders list, Transaction history
  - Nút Buy/Sell

**TC-TD-002: Xem Trust Score breakdown**
- **Pre:** Token có trust settings
- **Steps:** Hover vào Trust Score badge
- **Expected:** Tooltip hiển thị: LP Locked (+20), Audited (+30), Freeze Disabled (+25), tổng điểm

**TC-TD-003: Thêm Favorites**
- **Pre:** Đã Connect Wallet, token chưa favorite
- **Steps:** Click icon heart (outline)
- **Expected:** Heart đổi filled, toast "Added to favorites", token xuất hiện tab Favorites

**TC-TD-004: Bỏ Favorites**
- **Pre:** Token đã favorite
- **Steps:** Click icon heart (filled)
- **Expected:** Heart đổi outline, toast "Removed from favorites"

**TC-TD-005: Xem danh sách Holders**
- **Pre:** Token có ≥10 holders
- **Steps:** Scroll đến section Holders
- **Expected:** Top 100 holders, mỗi row: Rank, Wallet (truncated), Amount, %

**TC-TD-006: Xem Transaction History**
- **Steps:** Scroll đến Transaction History
- **Expected:** 50 giao dịch gần nhất, mỗi row: Type (BUY/SELL), User, Amount, Price, Time. BUY xanh, SELL đỏ

**TC-TD-007: Gửi chat message**
- **Pre:** Đã Connect Wallet
- **Steps:** Nhập "Hello community!" → Click Send
- **Expected:** Message xuất hiện với avatar, name, timestamp

**TC-TD-008: Chat validation - rỗng**
- **Steps:** Gửi message rỗng
- **Expected:** Nút Send disabled

**TC-TD-009: Chat validation - quá dài**
- **Steps:** Nhập message >200 ký tự → Gửi
- **Expected:** Error "Message must be 200 characters or less", counter hiển thị

**TC-TD-010: Click creator → Public Profile**
- **Steps:** Click creator name/avatar
- **Expected:** Navigate đến Public Profile của creator

**TC-TD-011: Xem bonding curve chart**
- **Steps:** Quan sát chart section
- **Expected:** Chart hiển thị bonding curve, X: Supply, Y: Price, real-time update

**TC-TD-012: Copy token address**
- **Steps:** Click icon copy bên cạnh token address
- **Expected:** Address copied, toast "Address copied"

**TC-TD-013: Xem Trust Score settings**
- **Steps:** Quan sát phần Trust Score trên Token Detail
- **Expected:** Hiển thị đầy đủ 3 mục với icon check/cross: "LP Locked", "Audited", "Freeze Disabled"

**TC-TD-014: Real-time price update**
- **Pre:** Token đang có giao dịch
- **Steps:** Quan sát price trong 30s
- **Expected:** Price update real-time khi có trade

**TC-TD-015: Real-time holder count**
- **Expected:** Holder count update khi có holder mới

**TC-TD-016: Real-time MC update**
- **Expected:** MC update theo price thay đổi

**TC-TD-017: Holder click → Public Profile**
- **Steps:** Click vào holder trong list
- **Expected:** Navigate đến Public Profile

**TC-TD-018: Transaction click → Explorer**
- **Steps:** Click vào transaction hash
- **Expected:** Mở Solana Explorer trong tab mới

**TC-TD-019: Graduated badge**
- **Pre:** Token MC ≥$69K
- **Expected:** Badge "Graduated" hiển thị

**TC-TD-020: Raydium pool link**
- **Pre:** Token đã graduated
- **Expected:** Link "View on Raydium" hiển thị

---

## FR-003: Mua/Bán Token

### Market Orders

**TC-BS-001: Mua token hợp lệ**
- **Pre:** Đã Connect Wallet, có ≥1 SOL
- **Steps:**
  1. Nhập amount: 0.5 SOL
  2. Chọn slippage: 1%
  3. Chọn priority: Normal
  4. Click "Buy" → Confirm trong wallet
- **Expected:**
  - Toast "Buy successful! +1 reward ticket"
  - Token balance tăng đúng số lượng (= SOL amount / price theo bonding curve)
  - SOL balance giảm đúng 0.5 SOL

**TC-BS-002: Bán token hợp lệ**
- **Pre:** Có ≥100 tokens
- **Steps:** Tab Sell → Nhập 50 tokens → Slippage 1% → Sell → Confirm
- **Expected:**
  - Transaction success
  - SOL nhận = tokens × price (không trừ fee người bán)
  - Token balance giảm đúng 50

**TC-BS-003: Mua - Không đủ SOL**
- **Pre:** Có 0.1 SOL
- **Steps:** Nhập amount: 10 SOL → Click Buy
- **Expected:** Error "Insufficient SOL balance", nút Buy disabled

**TC-BS-004: Bán - Không đủ token**
- **Pre:** Có 10 tokens
- **Steps:** Tab Sell → Nhập 100 tokens → Click Sell
- **Expected:** Error "Insufficient token balance", nút Sell disabled

**TC-BS-005: Chọn slippage preset**
- **Steps:** Lần lượt click 0.5% → 1% → 3%
- **Expected:** Option được highlight, tính toán price cập nhật

**TC-BS-006: Chọn slippage custom**
- **Steps:** Click "Custom" → Nhập 2.5% → Confirm
- **Expected:** Custom slippage accepted, price cập nhật

**TC-BS-007: Priority fee Normal**
- **Steps:** Chọn "Normal"
- **Expected:** Estimated time ~30s, không có extra fee

**TC-BS-008: Priority fee Fast**
- **Steps:** Chọn "Fast"
- **Expected:** Estimated time ~10s, extra fee hiển thị

**TC-BS-009: Priority fee Turbo**
- **Steps:** Chọn "Turbo"
- **Expected:** Estimated time ~5s, higher extra fee

**TC-BS-010: Bật Anti-MEV**
- **Steps:** Settings → Toggle "Anti-MEV Protection" ON
- **Expected:** Anti-MEV enabled, icon indicator ON

**TC-BS-011: Bật Auto-retry**
- **Steps:** Settings → Toggle "Auto-retry" ON
- **Expected:** Failed transactions sẽ retry tối đa 3 lần

**TC-BS-012: Validation min trade**
- **Ghi chú:** *Chưa chốt giá trị min trade*
- **Steps:** Nhập amount < minimum → Try buy
- **Expected:** Error hiển thị minimum, nút Buy disabled

**TC-BS-013: Tính toán tokens nhận được (Mua)**
- **Steps:** Nhập amount: 1 SOL → Quan sát
- **Expected:**
  - "You will receive" hiển thị số tokens
  - Số tokens = tính theo bonding curve formula
  - Verify bằng cách so sánh trước/sau khi mua

**TC-BS-014: Tính toán SOL nhận được (Bán)**
- **Steps:** Tab Sell → Nhập 100 tokens
- **Expected:**
  - "You will receive" hiển thị SOL
  - SOL = tokens × price × (1 - slippage)

**TC-BS-015: Phí mua 1% (creator fee)**
- **Steps:** Mua 1 SOL tokens, quan sát fee breakdown
- **Expected:** Fee = 0.01 SOL (1%), hiển thị rõ trong confirm popup

**TC-BS-016: Xác nhận giao dịch**
- **Steps:** Click Buy
- **Expected:** Popup confirm: Amount, Price, Slippage, Fee, nút Confirm/Cancel

**TC-BS-017: Giao dịch thất bại → retry**
- **Pre:** Auto-retry enabled
- **Expected:** Auto retry max 3 lần, toast hiển thị retry count

**TC-BS-018: Xem giao dịch trên explorer**
- **Steps:** Sau transaction success, click "View on Explorer"
- **Expected:** Mở Solana Explorer với transaction hash đúng

### Limit Orders (9 TCs)

**TC-BS-019: Tạo Buy limit order**
- **Pre:** Đã Connect Wallet, Advanced mode ON
- **Steps:** Chọn "Limit Order" → Target price: 0.04 SOL → Amount: 1 SOL → "Create Order"
- **Expected:** Order created, xuất hiện trong "Active Orders", status: Active

**TC-BS-020: Tạo Sell limit order**
- **Pre:** Có tokens
- **Steps:** Tab Sell → Limit Order → Target: 0.06 SOL → Amount: 100 tokens → Create
- **Expected:** Sell limit order created, execute khi price ≥0.06

**TC-BS-021: Validation target price**
- **Pre:** Current price = 0.05
- **Steps:** Tạo limit order với target: 0.05 (= current)
- **Expected:** Error "Target price must be different from current price"

**TC-BS-022: Hủy limit order**
- **Pre:** Có active limit order
- **Steps:** Active Orders → Click "Cancel" → Confirm
- **Expected:** Order cancelled, removed from list

**TC-BS-023: Auto-execute buy limit**
- **Pre:** Buy limit tại 0.04, current = 0.05
- **Steps:** Đợi price drop về 0.04
- **Expected:** Order auto execute, status "Completed", tokens received đúng, notification

**TC-BS-024: Auto-execute sell limit**
- **Pre:** Sell limit tại 0.06, current = 0.05
- **Steps:** Đợi price lên 0.06
- **Expected:** Order auto execute, SOL received đúng

**TC-BS-025: Xem Active Orders list**
- **Expected:** List active orders, mỗi order: Token, Type, Target, Amount, Status, nút Cancel

**TC-BS-026: Limit order hết hạn**
- **Pre:** Order có expiration time
- **Expected:** Status "Expired", notification gửi cho user

**TC-BS-027: Không đủ balance tạo order**
- **Pre:** Balance = 0.1 SOL
- **Steps:** Create limit order 10 SOL
- **Expected:** Error "Insufficient balance", order không tạo

**TC-BS-028: Thông báo khi order execute**
- **Expected:** In-app notification badge khi order được execute

**TC-BS-029: Order priority queue**
- **Pre:** Nhiều orders cùng price
- **Expected:** Execute theo thứ tự thời gian (FIFO)

**TC-BS-030: Order slippage protection**
- **Expected:** Order auto cancel nếu slippage vượt ngưỡng

---

## FR-004: My Profile (22 TCs)

**TC-MP-001: Tab Holding Tokens - hiển thị**
- **Pre:** Đã Connect Wallet, có holding tokens
- **Steps:** Mở My Profile → Tab "Holdings"
- **Expected:** Danh sách tokens đang hold, mỗi row: Token info, Amount, Value, P&L

**TC-MP-002: Tab Holding - tính P&L**
- **Expected:**
  - P&L = (Current Value - Buy Value) / Buy Value × 100%
  - Xanh nếu lãi, đỏ nếu lỗ
  - Số liệu chính xác

**TC-MP-003: Tab Holding - Sort by value**
- **Steps:** Click Sort → "Value (High to Low)"
- **Expected:** Tokens sort theo value giảm dần

**TC-MP-004: Tab Created Tokens**
- **Expected:** Danh sách tokens đã tạo (read-only), link đến Creator Dashboard

**TC-MP-005: Tab Created - link Creator Dashboard**
- **Steps:** Click vào token đã tạo
- **Expected:** Navigate đến Creator Dashboard của token đó

**TC-MP-006: Tab Edit Profile - lần đầu set username**
- **Steps:** Tab Edit → Nhập username lần đầu → Save
- **Expected:** Username được lưu thành công

**TC-MP-007: Tab Edit - username locked sau khi set**
- **Pre:** Đã set username
- **Expected:** Username field disabled, không cho sửa

**TC-MP-008: Tab Edit - validation username (3-20 chars)**
- **Steps:** Nhập username < 3 chars hoặc > 20 chars → Save
- **Expected:** Error "Username must be 3-20 characters"

**TC-MP-009: Tab Edit - validation username (ký tự hợp lệ)**
- **Steps:** Nhập username có ký tự đặc biệt (!@#)
- **Expected:** Error "Only alphanumeric and underscore allowed"

**TC-MP-010: Tab Edit - username đã tồn tại**
- **Steps:** Nhập username đã có người dùng → Save
- **Expected:** Error "Username already taken"

**TC-MP-011: Tab Edit - update avatar**
- **Steps:** Click avatar → Upload ảnh mới → Save
- **Expected:** Avatar cập nhật thành công

**TC-MP-012: Tab Edit - update bio**
- **Steps:** Nhập bio → Save
- **Expected:** Bio cập nhật thành công

**TC-MP-013: Tab Edit - update social links**
- **Steps:** Nhập Twitter/Telegram links → Save
- **Expected:** Social links cập nhật

**TC-MP-014: Tab Edit - display name locked**
- **Pre:** Đã set display name
- **Expected:** Display name field disabled

**TC-MP-015: Privacy settings - set private**
- **Steps:** Tab Edit → Toggle "Private Profile" ON → Save
- **Expected:** Toàn bộ profile ẩn khỏi công khai (holdings, transactions, created tokens đều ẩn)

**TC-MP-016: Privacy settings - set public**
- **Pre:** Profile đang private
- **Steps:** Toggle "Private Profile" OFF → Save
- **Expected:** Profile hiển thị công khai trở lại

**TC-MP-017: Tab Limit Orders**
- **Expected:** Hiển thị active orders, mỗi order có nút Cancel

**TC-MP-018: Xem total portfolio value**
- **Expected:** Tổng giá trị portfolio hiển thị chính xác (sum tất cả holdings)

**TC-MP-019: Xem token detail từ holdings**
- **Steps:** Click vào token trong holdings
- **Expected:** Navigate đến Token Detail

---

## FR-005: Public Profile (10 TCs)

**TC-PP-001: Xem public profile user khác**
- **Steps:** Click vào user name/avatar ở bất kỳ đâu
- **Expected:** Hiển thị Public Profile: avatar, name, rank, points, social links

**TC-PP-002: Profile public - hiển thị đầy đủ**
- **Pre:** User đặt profile public
- **Expected:** Hiển thị holdings, created tokens, transaction history

**TC-PP-003: Profile private - ẩn thông tin**
- **Pre:** User đặt profile private
- **Expected:** Hiển thị "This user's profile is private", chỉ thấy avatar, name, rank

**TC-PP-004: Xem created tokens**
- **Pre:** User có profile public
- **Expected:** Danh sách tokens user đã tạo

**TC-PP-005: Xem rank & points**
- **Expected:** Hiển thị rank badge và tổng points

**TC-PP-006: Xem social links**
- **Expected:** Hiển thị Twitter/Telegram links (nếu có)

**TC-PP-007: Copy wallet address**
- **Steps:** Click icon copy bên cạnh wallet address
- **Expected:** Wallet address copied, toast thông báo

---

## FR-006: Creator Dashboard (30 TCs)

### Dashboard & Revenue (15 TCs)

**TC-CD-001: Xem danh sách tokens đã tạo**
- **Pre:** Đã Connect Wallet, đã tạo ≥1 token
- **Steps:** Mở Creator Dashboard
- **Expected:** Danh sách tất cả tokens đã tạo với stats

**TC-CD-002: Xem tổng revenue**
- **Expected:** Tổng revenue từ tất cả tokens (sum creator fees 1%)

**TC-CD-003: Xem revenue breakdown**
- **Steps:** Click vào token cụ thể
- **Expected:** Revenue breakdown: tổng revenue, claim được, đã claim

**TC-CD-004: Claim revenue**
- **Pre:** Có revenue chưa claim
- **Steps:** Click "Claim" → Confirm trong wallet
- **Expected:** SOL chuyển vào wallet, revenue balance reset

**TC-CD-005: Revenue history**
- **Expected:** Lịch sử claim revenue: ngày, amount, transaction hash

**TC-CD-006: Token metrics**
- **Expected:** Mỗi token hiển thị: MC, Volume 24h, Holders, Trust Score

**TC-CD-007: Token performance chart**
- **Expected:** Chart hiển thị price/volume theo thời gian

**TC-CD-008: Best performing token**
- **Expected:** Highlight token có revenue/MC cao nhất

**TC-CD-009: Thống kê tokens created & graduated**
- **Expected:** Hiển thị đúng: tổng tokens đã tạo, số tokens đã graduated (MC ≥$69K)

**TC-CD-014: Claim all revenue**
- **Steps:** Click "Claim All" → Confirm
- **Expected:** Tất cả revenue được claim

**TC-CD-015: Revenue notification**
- **Expected:** Notification khi có revenue mới

### Token Management (15 TCs)

**TC-CD-016: Cập nhật LP lock**
- **Steps:** Token settings → Toggle "LP Lock" ON
- **Expected:** LP Lock enabled, Trust Score +20

**TC-CD-017: Cập nhật Audit**
- **Steps:** Toggle "Audit" ON
- **Expected:** Audit enabled, Trust Score +30

**TC-CD-018: Cập nhật Freeze authority**
- **Steps:** Toggle "Freeze Disabled" ON
- **Expected:** Freeze disabled, Trust Score +25

**TC-CD-019: Sửa token description**
- **Steps:** Edit → Sửa description → Save
- **Expected:** Description cập nhật trên Token Detail

**TC-CD-020: Sửa token avatar**
- **Steps:** Edit → Upload avatar mới → Save
- **Expected:** Avatar cập nhật

**TC-CD-021: Sửa social links của token**
- **Steps:** Edit → Thay đổi Twitter/Telegram/Website → Save
- **Expected:** Social links cập nhật trên Token Detail

**TC-CD-022: Tạo post mới**
- **Steps:** Click "New Post" → Nhập nội dung → Post
- **Expected:** Post xuất hiện trên Token Detail community

**TC-CD-023: Sửa post**
- **Steps:** Click Edit trên post → Sửa nội dung → Save
- **Expected:** Post cập nhật

**TC-CD-024: Xóa post**
- **Steps:** Click Delete → Confirm
- **Expected:** Post bị xóa

**TC-CD-025: Pin post**
- **Steps:** Click Pin trên post
- **Expected:** Post ghim lên đầu

**TC-CD-026: Unpin post**
- **Steps:** Click Unpin
- **Expected:** Post bỏ ghim

**TC-CD-027: Post validation và upload ảnh**
- **Steps:**
  1. Nhập post >500 ký tự → Post → Verify error
  2. Upload ảnh vào post → Verify ảnh đính kèm
- **Expected:** Counter hiển thị khi quá 500 ký tự; ảnh upload thành công kèm theo post

---

## FR-007: Tạo Token (40 TCs)

### Step 1: Thông tin cơ bản (10 TCs)

**TC-CT-001: Validation - tên bắt buộc**
- **Steps:** Bỏ trống tên → Next
- **Expected:** Error "Token name is required"

**TC-CT-002: Validation - tên tối đa 32 ký tự**
- **Steps:** Nhập tên >32 chars → Next
- **Expected:** Error "Token name max 32 characters"

**TC-CT-003: Validation - symbol bắt buộc**
- **Steps:** Bỏ trống symbol → Next
- **Expected:** Error "Token symbol is required"

**TC-CT-004: Validation - symbol viết hoa**
- **Steps:** Nhập symbol "pepe" (thường)
- **Expected:** Tự động chuyển thành "PEPE"

**TC-CT-005: Validation - symbol tối đa 10 ký tự**
- **Steps:** Nhập symbol >10 chars
- **Expected:** Error hiển thị

**TC-CT-006: Validation - statement tối đa 60 ký tự**
- **Steps:** Nhập statement >60 chars
- **Expected:** Counter hiển thị, cắt tại 60

**TC-CT-007: Validation - description tối đa 500 ký tự**
- **Steps:** Nhập description >500 chars
- **Expected:** Counter hiển thị, error

**TC-CT-008: AI assist - tạo statement**
- **Steps:** Click "AI Generate" cho statement
- **Expected:** AI tạo statement phù hợp với tên token

**TC-CT-009: AI assist - tạo description**
- **Steps:** Click "AI Generate" cho description
- **Expected:** AI tạo description phù hợp

**TC-CT-010: Next step khi valid**
- **Pre:** Đã điền đủ name + symbol
- **Steps:** Click Next
- **Expected:** Chuyển sang Step 2

### Step 2: Avatar (8 TCs)

**TC-CT-011: Upload avatar**
- **Steps:** Click Upload → Chọn file PNG/JPG
- **Expected:** Preview avatar hiển thị

**TC-CT-012: Validation file size**
- **Steps:** Upload file >5MB
- **Expected:** Error "Max file size is 5MB"

**TC-CT-013: Validation file type**
- **Steps:** Upload file .exe / .pdf
- **Expected:** Error "Only PNG, JPG, JPEG, GIF allowed"

**TC-CT-014: AI generate avatar**
- **Steps:** Click "AI Generate" → Nhập mô tả
- **Expected:** AI tạo avatar, preview hiển thị

**TC-CT-015: Preview avatar**
- **Expected:** Avatar hiển thị preview dạng tròn giống trên token card

**TC-CT-016: Xóa avatar**
- **Steps:** Click Remove
- **Expected:** Avatar bị xóa, quay lại placeholder

**TC-CT-017: Crop avatar**
- **Steps:** Upload ảnh → Drag crop area → Apply
- **Expected:** Avatar được crop theo vùng chọn

**TC-CT-018: Bỏ qua avatar**
- **Steps:** Click Next (không upload)
- **Expected:** Chuyển Step 3, dùng avatar mặc định

### Step 3: Security Settings (10 TCs)

**TC-CT-019: Bật LP Lock**
- **Steps:** Toggle "LP Lock" ON
- **Expected:** Trust Score +20

**TC-CT-020: Tắt LP Lock**
- **Steps:** Toggle OFF
- **Expected:** Trust Score -20

**TC-CT-021: Bật Audit**
- **Steps:** Toggle "Audited" ON
- **Expected:** Trust Score +30

**TC-CT-022: Tắt Audit**
- **Steps:** Toggle OFF
- **Expected:** Trust Score -30

**TC-CT-023: Bật Freeze Disabled**
- **Steps:** Toggle "Freeze Authority Disabled" ON
- **Expected:** Trust Score +25

**TC-CT-024: Tắt Freeze Disabled**
- **Steps:** Toggle OFF
- **Expected:** Trust Score -25

**TC-CT-025: Tính Trust Score tổng hợp**
- **Steps:** Bật cả 3 settings
- **Expected:** Trust Score = 20 + 30 + 25 = 75

**TC-CT-026: Trust Score tối đa**
- **Expected:** Max = 75 (khi bật hết)

**TC-CT-027: Trust Score tối thiểu**
- **Expected:** Min = 0 (khi tắt hết)

**TC-CT-028: Bỏ qua security settings**
- **Steps:** Click Next (không bật gì)
- **Expected:** Chuyển Step 4, Trust Score = 0

### Step 4: Initial Buy (6 TCs)

**TC-CT-029: Nhập initial buy amount**
- **Steps:** Nhập 0.5 SOL
- **Expected:** Hiển thị tokens sẽ nhận được

**TC-CT-030: Validation min amount**
- **Ghi chú:** *Cần chốt giá trị min buy*
- **Expected:** Error nếu dưới minimum

**TC-CT-031: Validation max = balance**
- **Pre:** Balance = 2 SOL
- **Steps:** Nhập 5 SOL
- **Expected:** Error "Insufficient balance"

**TC-CT-032: Tính tokens nhận được**
- **Steps:** Nhập 1 SOL
- **Expected:** Số tokens = tính theo bonding curve, verify chính xác

**TC-CT-033: Bỏ qua initial buy**
- **Steps:** Click Skip / Next (không nhập)
- **Expected:** Chuyển Step 5, không mua token

### Step 5: Review & Tạo Token (6 TCs)

**TC-CT-035: Review tất cả thông tin**
- **Steps:** Xem trang Review
- **Expected:** Hiển thị đầy đủ: Name, Symbol, Statement, Description, Avatar, Security, Initial Buy

**TC-CT-036: Quay lại sửa bước trước**
- **Steps:** Click "Edit" trên bất kỳ section nào
- **Expected:** Navigate về step tương ứng, data giữ nguyên

**TC-CT-037: Tạo token - transaction**
- **Steps:** Click "Create Token" → Confirm trong wallet
- **Expected:** Transaction submitted, loading state

**TC-CT-038: Tạo thành công → +20 points**
- **Expected:** Toast "Token created!", +20 points earned, token xuất hiện trên Token List

**TC-CT-039: Tạo thất bại**
- **Expected:** Error message, retry option, không mất SOL

**TC-CT-040: Redirect đến Token Detail**
- **Expected:** Sau tạo thành công, tự động chuyển đến Token Detail page

---

## FR-008: Leaderboard

**TC-LB-001: Top 3 featured cards**
- **Steps:** Mở trang Leaderboard
- **Expected:** Top 3 tokens hiển thị dạng card lớn

**TC-LB-002: Table từ rank 4+**
- **Expected:** Table hiển thị tokens từ rank 4 trở đi, sort mặc định theo MC giảm dần

**TC-LB-003: Click token → Token Detail**
- **Steps:** Click vào token
- **Expected:** Navigate đến Token Detail

**TC-LB-004: Quick Buy từ leaderboard**
- **Steps:** Click nút Buy
- **Expected:** Mở Trading Panel

---

## FR-009: Rewards - Slot Machine (10 TCs)

**TC-RW-001: Quay slot machine**
- **Pre:** Đã Connect Wallet, có ≥1 ticket
- **Steps:** Chọn bet amount → Click "Spin"
- **Expected:** Animation quay, hiển thị kết quả

**TC-RW-002: Trừ ticket khi quay**
- **Steps:** Spin 1 lần
- **Expected:** Ticket balance giảm đúng số bet

**TC-RW-003: Không đủ tickets**
- **Pre:** 0 tickets
- **Steps:** Click Spin
- **Expected:** Error "Not enough tickets", nút Spin disabled

**TC-RW-004: Thắng 3-of-a-kind**
- **Expected:** Payout = bet × multiplier, hiển thị animation thắng

**TC-RW-005: Thắng 4-of-a-kind**
- **Expected:** Payout cao hơn 3-of-a-kind

**TC-RW-006: Jackpot 5-of-a-kind**
- **Expected:** Jackpot 0.01 SOL, animation đặc biệt

**TC-RW-007: Symbol multipliers**
- **Expected:** 🌱=1×, 🌿=2×, 🌳=3×, 🍀=4×, 🌼=5×

**TC-RW-008: Nhận thưởng**
- **Steps:** Click "Claim"
- **Expected:** Rewards chuyển vào wallet

**TC-RW-009: Lịch sử quay**
- **Expected:** Hiển thị: thời gian, kết quả, bet, payout

**TC-RW-010: Hiển thị ticket balance**
- **Expected:** Ticket balance chính xác, cập nhật real-time

---

## FR-010: Referrals

**TC-RF-001: Tạo referral link**
- **Pre:** Đã Connect Wallet
- **Steps:** Mở Referral page → Click "Generate Link"
- **Expected:** Link tạo với format: domain.com/ref/[code]

**TC-RF-002: Copy referral link**
- **Steps:** Click "Copy"
- **Expected:** Link copied, toast thông báo

**TC-RF-003: Xem danh sách người được giới thiệu**
- **Expected:** List users đã dùng referral link: wallet (truncated), ngày join

**TC-RF-004: Tính earnings**
- **Data:** Referred user giao dịch 100 SOL → Fee 1% = 1 SOL → Referrer nhận 20% × 1 SOL = 0.2 SOL
- **Expected:** Earnings = 20% của 1% phí giao dịch từ referred users, tính chính xác

**TC-RF-005: Claim referral rewards**
- **Steps:** Click "Claim" → Confirm
- **Expected:** SOL chuyển vào wallet

**TC-RF-006: Referral stats**
- **Expected:** Total users, total earnings hiển thị chính xác

**TC-RF-007: Referral leaderboard**
- **Expected:** Top referrers xếp hạng theo earnings

**TC-RF-008: Referral notification**
- **Expected:** Notification khi có user mới signup qua link

**TC-RF-009: Referral link expiration**
- **Expected:** Link hết hạn sau thời gian quy định (nếu có)

**TC-RF-010: Referral code không hợp lệ**
- **Steps:** Truy cập link với code sai
- **Expected:** Error "Invalid referral code"

---

## FR-011: Points & Ranking (14 TCs)

**TC-PT-001: Xem points dashboard**
- **Pre:** Đã Connect Wallet
- **Steps:** Mở Points page
- **Expected:** Tổng points, rank hiện tại, thanh tiến trình rank tiếp theo

**TC-PT-002: Earn points - Trade (Volume × 5)**
- **Steps:** Mua token 1 SOL
- **Expected:** Points += Volume × 5

**TC-PT-003: Earn points - Sell không tính**
- **Steps:** Bán token
- **Expected:** Không nhận thêm points

**TC-PT-004: Earn points - Referral (NetVolume × 10)**
- **Pre:** Có referred user giao dịch
- **Expected:** Points += NetVolume × 10

**TC-PT-005: Earn points - Tạo token (+20)**
- **Steps:** Tạo token thành công
- **Expected:** Points +20

**TC-PT-006: Earn points - Upload image (+10)**
- **Steps:** Upload avatar cho token
- **Expected:** Points +10

**TC-PT-007: Earn points - Trust settings (+20)**
- **Steps:** Bật trust settings cho token
- **Expected:** Points +20

**TC-PT-008: Earn points - 10 buys milestone (+30)**
- **Pre:** Đã mua 9 lần
- **Steps:** Mua lần thứ 10
- **Expected:** Bonus +30 points, notification

**TC-PT-009: Rank Seed (0-499 points)**
- **Expected:** Badge 🌱 Seed hiển thị

**TC-PT-010: Rank Sprout (500-1,999 points)**
- **Expected:** Badge 🌿 Sprout hiển thị

**TC-PT-011: Rank Sapling (2,000-9,999 points)**
- **Expected:** Badge 🌳 Sapling hiển thị

**TC-PT-012: Rank Tree (10,000-49,999 points)**
- **Expected:** Badge 🌲 Tree hiển thị

**TC-PT-013: Rank Ancient Tree (50,000+ points)**
- **Expected:** Badge 🌴 Ancient Tree hiển thị

**TC-PT-014: Points history**
- **Steps:** Xem lịch sử points
- **Expected:** Danh sách: ngày, hành động, points earned

---

# 2. KIỂM THỬ BẢO MẬT

### Authentication & Authorization

**TC-SEC-001: Wallet signature hợp lệ**
- **Steps:** Connect Wallet (Phantom) → Ký message xác thực
- **Expected:** Signature verify thành công, session tạo, JWT token trả về

**TC-SEC-002: Wallet signature không hợp lệ**
- **Data:** Gửi signature giả mạo
- **Steps:** Gọi API `/auth/verify` với signature không hợp lệ
- **Expected:** 401 Unauthorized, session không tạo

**TC-SEC-003: Token expiration & Session timeout**
- **Pre:** Đã Connect Wallet, có JWT token
- **Steps:**
  1. Đợi token hết hạn → Thực hiện action bất kỳ trên UI → Verify redirect Connect Wallet
  2. Không thao tác trong xx thời gian → Thực hiện action → Verify session hết hạn
- **Expected:** Cả 2 trường hợp đều yêu cầu Connect Wallet lại

**TC-SEC-004: Concurrent sessions**
- **Steps:** Connect Wallet trên Browser A → Connect cùng wallet trên Browser B
- **Expected:** Session cũ bị invalidate hoặc cả 2 hoạt động độc lập (tùy policy)

**TC-SEC-005: Disconnect Wallet → clear session**
- **Pre:** Đã Connect Wallet
- **Steps:** Click Disconnect Wallet → Kiểm tra cookies/localStorage
- **Expected:** JWT token bị xóa, session cleared, redirect về trang chủ

**TC-SEC-006: Unauthorized access block**
- **Steps:** Truy cập `/my-profile`, `/creator-dashboard` khi chưa Connect Wallet
- **Expected:** Redirect về trang Connect Wallet hoặc hiển thị "Please connect wallet"

**TC-SEC-007: Role-based access**
- **Steps:** User không phải creator → Truy cập Creator Dashboard của token người khác
- **Expected:** 403 Forbidden, không hiển thị revenue/settings

**TC-SEC-008: Brute force & Account lockout**
- **Steps:**
  1. Gửi 10 request Connect Wallet thất bại liên tiếp trong 1 phút → Verify block
  2. 5 lần verify signature thất bại liên tiếp → Verify wallet bị lock tạm thời
- **Expected:** Block IP/wallet tạm thời (429), thông báo "Too many attempts"

---

### Input Validation & Injection

**XSS**

**TC-SEC-009: XSS trong các input fields**
- **Data:** Thử lần lượt các payloads:
  - description = `<img onerror="alert('XSS')" src="x">`
  - chat message = `<script>document.cookie</script>`
  - bio = `<svg onload="alert(1)">`
  - username = `<img src=x onerror=alert(1)>`
  - post content = `javascript:alert('XSS')`
  - social link = `javascript:alert(1)`
- **Steps:** Nhập từng payload vào field tương ứng → Submit → Kiểm tra DOM
- **Expected:** HTML bị sanitize hoặc validation reject, không execute script. Username chỉ accept alphanumeric + _. Social links chỉ accept https://

**SQL Injection**

**TC-SEC-010: SQL injection trong các input & API params**
- **Data:** Thử các payloads:
  - search = `'; DROP TABLE tokens; --`
  - filter min_mc = `1 OR 1=1`
  - sort = `; DELETE FROM users; --`
  - wallet_address = `' OR '1'='1`
  - token_id = `1 UNION SELECT * FROM users`
- **Steps:** Nhập payload vào search, filter, sort trên UI. Gửi API với params chứa SQL injection
- **Expected:** Validation reject hoặc trả kết quả rỗng/error an toàn. DB không bị ảnh hưởng. Wallet address chỉ accept base58 format

**Other Injection (đại diện)**

**TC-SEC-011: Injection tổng hợp (HTML, Template, NoSQL)**
- **Data:**
  - HTML: `<h1>Injected</h1><form action="evil.com">`
  - Template: `{{7*7}}` hoặc `${7*7}`
  - NoSQL: `{"$gt": ""}`
- **Steps:** Nhập từng payload vào token description, token name, API params
- **Expected:** HTML tags bị strip/encode. Template hiển thị literal text. NoSQL operator bị reject

---

### API Security

**TC-SEC-012: Rate limiting**
- **Steps:** Script gửi 101 requests trong 1 phút đến cùng endpoint
- **Expected:** Request thứ 101 bị reject, 429 Too Many Requests, header `Retry-After` present

**TC-SEC-013: CORS validation**
- **Data:** Origin = `https://evil-site.com`
- **Steps:** Gửi request từ domain không whitelisted → Kiểm tra response headers
- **Expected:** Không có `Access-Control-Allow-Origin` cho domain đó, CORS reject

**TC-SEC-014: API authentication & invalid token**
- **Steps:**
  1. Gọi API `/users/me`, `/trading/buy` không có Auth header → Verify 401
  2. Gọi API với `Authorization: Bearer invalid_token_here` → Verify 401 Invalid token
- **Expected:** Tất cả protected endpoints trả 401 khi không có hoặc sai token

**TC-SEC-015: Request validation**
- **Steps:**
  1. Gửi POST request với body > 10MB → Verify 413 Payload Too Large
  2. Gửi POST với malformed JSON `{invalid json` → Verify 400 Bad Request
- **Expected:** Server validate request size và format, trả error rõ ràng

**TC-SEC-016: API response sanitization & error handling**
- **Steps:**
  1. Gọi API endpoint → Kiểm tra response không leak stack trace, DB schema, server paths
  2. Gọi endpoint không tồn tại `/api/nonexistent` → Verify error message generic
  3. Gọi API với params sai type `/tokens?id=abc` → Verify error không leak internal details
- **Expected:** Response không chứa internal info, error messages generic và an toàn

**TC-SEC-017: API timeout**
- **Steps:** Gửi request gây slow query (search phức tạp)
- **Expected:** Timeout sau 30s, 504 Gateway Timeout

---

### Wallet & Blockchain Security

**TC-SEC-018: Transaction signature & replay prevention**
- **Steps:**
  1. Mở Token Detail → Buy 0.1 SOL → Wallet popup hiển thị → Approve → Verify transaction thành công trên Solana Explorer
  2. Dùng tool (ví dụ Solana CLI) sửa 1 byte trong signature của transaction trên → Submit lại → Verify bị reject
  3. Copy transaction hash đã thành công → Gửi lại cùng transaction data → Verify reject (nonce đã dùng)
- **Expected:** Signature hợp lệ thành công, signature sửa đổi và replay đều bị reject

**TC-SEC-019: Private key không bị lộ**
- **Steps:**
  1. Mở Chrome DevTools → Tab Network → Thực hiện Connect Wallet + Buy token
  2. Tìm kiếm trong tất cả requests/responses với keyword "private", "secret", "key"
  3. Mở tab Sources → Search toàn bộ frontend code với regex pattern private key
- **Expected:** Không có private key xuất hiện trong network traffic hoặc client code

**TC-SEC-020: Integer overflow/underflow prevention**
- **Steps:**
  1. Mở Buy form → Nhập amount = 999999999999999999 (rất lớn) → Click Buy → Verify reject
  2. Mở Buy form → Nhập amount = -1 → Click Buy → Verify reject
  3. Mở Buy form → Nhập amount = 0 → Click Buy → Verify reject
- **Expected:** Tất cả trường hợp bị validation reject với error message rõ ràng

**TC-SEC-021: MEV & front-running protection**
- **Pre:** Mở Token Detail → Advanced Settings → Bật Anti-MEV toggle ON
- **Steps:**
  1. Submit buy 1 SOL → Mở Solana Explorer → Kiểm tra transaction có đi qua private mempool (Jito/similar)
  2. So sánh: tắt Anti-MEV → Submit buy → Kiểm tra transaction đi qua public mempool
- **Expected:** Anti-MEV ON → transaction qua private mempool, không visible cho MEV bots

**TC-SEC-022: Concurrent transactions & nonce management**
- **Steps:**
  1. Mở 2 tab browser cùng Token Detail
  2. Tab 1: Nhập Buy 0.1 SOL → Click Buy
  3. Tab 2: Ngay lập tức nhập Buy 0.1 SOL → Click Buy
  4. Kiểm tra cả 2 transaction trên Solana Explorer
- **Expected:** Nonce quản lý đúng, không conflict. Cả 2 thành công tuần tự hoặc 1 reject rõ ràng

**TC-SEC-023: Wallet connection timeout**
- **Steps:** Click Connect Wallet → Wallet popup hiện → Không click Approve → Đợi 60s
- **Expected:** UI hiển thị "Connection timed out", popup tự đóng, có nút Retry

---

### Additional Security

**TC-SEC-024: CSRF protection**
- **Steps:** Tạo HTML page trên domain khác chứa form POST đến API `/trading/buy` → Mở page → Submit
- **Expected:** 403 Forbidden, CSRF token missing/invalid

**TC-SEC-025: Clickjacking & Secure headers**
- **Steps:**
  1. Tạo HTML page chứa `<iframe src="https://pumpfun.io">` → Mở trên browser → Verify site không load
  2. Dùng DevTools kiểm tra response headers của bất kỳ page nào
- **Expected:** Site không load trong iframe. Headers bảo mật có đủ: `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`, `Strict-Transport-Security` present

**TC-SEC-026: File upload validation (magic bytes)**
- **Steps:**
  1. Tạo file text → Rename thành `image.png` → My Profile → Upload avatar → Verify reject
  2. Tạo file `malware.exe` → Rename thành `photo.jpg` → Upload avatar → Verify reject (server check magic bytes)
  3. Upload file `.svg`, `.html`, `.php` → Verify reject (chỉ accept PNG/JPG/GIF)
  4. Upload ảnh hợp lệ > 5MB → Verify reject 413
- **Expected:** Server kiểm tra magic bytes, reject file không phải image thật. Chỉ accept PNG/JPG/GIF ≤ 5MB

**TC-SEC-027: DDoS & Bot protection**
- **Steps:**
  1. Dùng tool (ab/wrk) gửi 10,000 requests/second đến homepage → Kiểm tra site availability từ browser khác
  2. Script crawl toàn bộ Token List pages liên tục → Kiểm tra có bị rate limit/CAPTCHA
- **Expected:** CDN/WAF block traffic bất thường, site vẫn available cho users thường. Rate limit + CAPTCHA sau threshold

---

# 3. KIỂM THỬ HIỆU NĂNG

### Load Testing

**TC-PERF-001: Normal load 100 users**
- **Data:** 100 concurrent users, mix actions (browse 60%, trade 30%, create 10%)
- **Steps:** Dùng k6/JMeter → Ramp up 100 users trong 2 phút → Duy trì 10 phút
- **Expected:** Response time < 2s (P95), error rate < 1%, CPU < 70%

**TC-PERF-002: Peak load 500 users**
- **Data:** 500 concurrent users
- **Steps:** Ramp up 500 users trong 5 phút → Duy trì 15 phút
- **Expected:** Response time < 3s (P95), error rate < 2%, không downtime

**TC-PERF-003: Sustained load 200 users / 2h**
- **Data:** 200 users liên tục 2 giờ
- **Steps:** Ramp up 200 users → Duy trì 2h → Monitor memory/CPU
- **Expected:** Response time < 2.5s (P95), không memory leak, performance ổn định

**TC-PERF-004: Spike test 0→1000 users**
- **Steps:** 0 users → Đột ngột 1000 users trong 30s → Giảm về 100
- **Expected:** Response time < 5s trong spike, recovery < 1 phút, không crash

### Response Time Benchmarks

**TC-PERF-005: Response time tổng hợp (Page, API, DB, WebSocket)**
- **Steps:**
  1. **Page load:** Mở Token List, Token Detail, My Profile → Đo load time → Target < 3s
  2. **API P95:** Benchmark 10,000 requests đến các endpoints chính → Target P95 < 500ms, P99 < 1s
  3. **DB query:** Monitor slow query log khi load test → Target tất cả queries < 100ms
  4. **WebSocket:** Subscribe price updates → Tạo trade → Đo thời gian update → Target < 500ms
- **Expected:** Tất cả metrics đạt target, không có full table scan trong DB

### Stress Testing

**TC-PERF-006: Stress test tổng hợp (Users, DB, Memory, CPU, Network)**
- **Steps:**
  1. **Max users:** Tăng dần 500 → 1000 → 1500 → 2000 → Tìm breaking point → Ghi nhận graceful degradation
  2. **DB overload:** Script gửi 10,000 queries/second → Verify connection pool quản lý tốt
  3. **Memory/CPU:** Tăng load cho đến memory 90%, CPU 95% → Verify không OOM/crash, alert trigger
  4. **Network:** Simulate high latency 500ms + packet loss 5% → Verify retry logic + loading states
- **Expected:** Hệ thống graceful degradation, không crash. Alert triggers đúng thời điểm

### API Performance

**TC-PERF-007: API endpoints latency**
- **Steps:** Benchmark 1000 requests mỗi endpoint:
  - GET /tokens → Target P95 < 200ms
  - POST /trading/market → Target P95 < 300ms
  - GET /users/me → Target P95 < 150ms
  - GET /leaderboard → Target P95 < 250ms
  - POST /tokens/create → Target P95 < 500ms
- **Expected:** Tất cả endpoints đạt target latency

**TC-PERF-008: WebSocket broadcast latency**
- **Steps:** Measure WebSocket Server → Client delay
- **Expected:** Broadcast delay < 100ms

### Frontend Performance

**TC-PERF-009: Lighthouse audit**
- **Steps:** Chạy Lighthouse audit trên Chrome DevTools
- **Expected:** Performance > 90, Accessibility > 90, Best Practices > 90

**TC-PERF-010: Core Web Vitals**
- **Steps:** Đo FCP và TTI trên 3G/4G network
- **Expected:** FCP < 1.5s (4G), < 3s (3G). TTI < 3s, main thread blocking < 200ms

---

# 4. KIỂM THỬ TƯƠNG THÍCH VÍ

**TC-WALLET-001: Tương thích các loại ví Solana**
- **Steps:**
  1. **Phantom:** Install extension → Connect Wallet → Buy 0.1 SOL token → Sell → Disconnect → Verify full flow
  2. **Solflare:** Install extension → Connect → Buy → Sell → Disconnect → Verify full flow
  3. **Backpack:** Install extension → Connect → Buy → Sell → Disconnect → Verify full flow
  4. **Ledger (hardware):** Connect Ledger Nano S/X via USB → Approve connection trên device → Buy token → Confirm transaction trên Ledger screen → Verify transaction thành công
- **Expected:** Tất cả wallets: connect/disconnect smooth, transaction signing hoạt động, balance cập nhật đúng. Ledger hiển thị transaction details trên device screen trước khi confirm

---

# 5. KIỂM THỬ HỒI QUY (20 TCs)

### Critical Path (20 TCs)

**TC-REG-001: Connect Wallet flow**
- **Steps:** Disconnect → Connect Wallet → Verify session
- **Expected:** Flow hoàn chỉnh, session tạo đúng

**TC-REG-002: Tạo token end-to-end**
- **Steps:** Create → Step 1-5 → Submit → Verify on Token List
- **Expected:** Token xuất hiện, data đúng

**TC-REG-003: Mua token flow**
- **Steps:** Token Detail → Buy → Confirm → Verify balance
- **Expected:** Balance cập nhật đúng, transaction recorded

**TC-REG-004: Bán token flow**
- **Steps:** Holdings → Sell → Confirm → Verify SOL received
- **Expected:** SOL nhận đúng (trừ fee), token balance giảm

**TC-REG-005: Claim revenue flow**
- **Steps:** Creator Dashboard → Claim → Confirm → Verify wallet
- **Expected:** SOL vào wallet, revenue reset

**TC-REG-006: Referral system flow**
- **Steps:** Generate link → User B signup → User B trades → Verify earnings
- **Expected:** Referral tracked, earnings = 20% of 1% phí giao dịch từ referred users

**TC-REG-007: Points earning flow**
- **Steps:** Thực hiện trade → Verify points tăng
- **Expected:** Points = Volume × 5

**TC-REG-008: Rank progression flow**
- **Steps:** Earn points vượt threshold → Verify rank change
- **Expected:** Rank badge thay đổi, notification

**TC-REG-009: Slot machine flow**
- **Steps:** Có ticket → Spin → Verify kết quả + ticket giảm
- **Expected:** Animation, kết quả, payout đúng

**TC-REG-010: Edit profile flow**
- **Steps:** My Profile → Edit → Thay đổi bio/avatar → Save → Verify
- **Expected:** Changes lưu và hiển thị đúng

**TC-REG-011: Search & filter flow**
- **Steps:** Token List → Search → Filter → Sort → Verify kết quả
- **Expected:** Results đúng theo criteria

**TC-REG-012: Favorites management**
- **Steps:** Add favorite → Verify tab Favorites → Remove → Verify removed
- **Expected:** Add/remove hoạt động đúng

**TC-REG-013: Chat functionality**
- **Steps:** Token Detail → Gửi message → Verify hiển thị
- **Expected:** Message gửi và hiển thị real-time

**TC-REG-014: Limit orders flow**
- **Steps:** Tạo limit order → Verify Active Orders → Cancel → Verify cancelled
- **Expected:** CRUD orders hoạt động đúng

**TC-REG-015: Token graduation flow**
- **Pre:** Token MC gần $69K
- **Steps:** Mua đẩy MC ≥ $69K → Verify graduated badge + Raydium link
- **Expected:** Badge hiển thị, link Raydium available

**TC-REG-016: Trust settings update**
- **Steps:** Creator Dashboard → Toggle trust settings → Verify Trust Score
- **Expected:** Trust Score cập nhật đúng (+20/+30/+25)

**TC-REG-017: Wallet connection flow**
- **Steps:** Test connect/disconnect/reconnect nhiều lần
- **Expected:** Flow stable, không session leak

**TC-REG-018: Transaction signing flow**
- **Steps:** Initiate trade → Sign trong wallet → Verify completion
- **Expected:** Signing smooth, transaction confirmed

**TC-REG-019: Notification system**
- **Steps:** Trigger events (trade, order fill, referral) → Verify notifications
- **Expected:** Notifications hiển thị đúng, badge count đúng

**TC-REG-020: Real-time updates**
- **Steps:** Mở Token Detail → Tạo trade từ device khác → Verify update
- **Expected:** Price, MC, holders update real-time

