# TEST CASES BY CATEGORY

**Tổng:** ~450 test cases

---

## TỔNG QUAN CATEGORIES

| # | Category | Số TCs | Mục đích | Độ ưu tiên |
|---|----------|--------|----------|------------|
| 1 | **Kiểm thử chức năng** | ~230 | Verify tất cả FR-001 đến FR-011 | Critical/High |
| 2 | **Kiểm thử bảo mật** | 139 | XSS, SQL Injection, Auth, Blockchain | Critical |
| 3 | **Kiểm thử hiệu năng** | 25 | Load, Stress, API response time | High |
| 4 | **Kiểm thử khả dụng** | 15 | UX, Navigation, Accessibility | Medium |
| 5 | **Kiểm thử tương thích** | 12 | Browser, Mobile, Wallet | High |
| 6 | **Kiểm thử hồi quy** | 50 | Ngăn regression sau update | High |

**Phân bổ theo module (Chức năng):**
- FR-001 Token List: 20 TCs
- FR-002 Token Detail: 26 TCs
- FR-003 Mua/Bán: 41 TCs (22 Market + 19 Limit)
- FR-004 My Profile: 22 TCs
- FR-005 Public Profile: 10 TCs
- FR-006 Creator Dashboard: 30 TCs
- FR-007 Tạo Token: 40 TCs
- FR-008 Leaderboard: 8 TCs
- FR-009 Rewards: 10 TCs
- FR-010 Referrals: 13 TCs
- FR-011 Points: 14 TCs

---

## 1. KIỂM THỬ CHỨC NĂNG (~230 TCs)

### FR-001: Token List (20 TCs)
- TC-TL-001: Hiển thị danh sách mặc định (phân trang)
- TC-TL-002: Chuyển tab (Discover/Trending/New/Graduated/Favorites)
- TC-TL-003: Tìm kiếm theo tên
- TC-TL-004: Tìm kiếm theo symbol
- TC-TL-005: Lọc theo MC range (min/max)
- TC-TL-006: Sắp xếp theo MC
- TC-TL-007: Lọc NSFW
- TC-TL-008: Click card → Token Detail
- TC-TL-009: Quick Buy từ card
- TC-TL-010: Kết quả tìm kiếm rỗng
- TC-TL-011: Lọc theo Trust Score
- TC-TL-012: Lọc theo Holders
- TC-TL-013: Sắp xếp theo Volume 24h
- TC-TL-014: Sắp xếp theo Price
- TC-TL-015: Pagination (next/prev)
- TC-TL-016: Load more tokens
- TC-TL-017: Refresh danh sách
- TC-TL-018: Filter kết hợp (MC + Trust Score)
- TC-TL-019: Clear all filters
- TC-TL-020: Bookmark token

### FR-002: Token Detail (26 TCs)
- TC-TD-001: Hiển thị đầy đủ thông tin token
- TC-TD-002: Xem Trust Score breakdown
- TC-TD-003: Add to Favorites
- TC-TD-004: Remove from Favorites
- TC-TD-005: Xem danh sách Holders (top 100)
- TC-TD-006: Xem Transaction History (50 giao dịch)
- TC-TD-007: Gửi chat message
- TC-TD-008: Chat validation - empty message
- TC-TD-009: Chat validation - quá dài (>200 chars)
- TC-TD-010: Click creator → Public Profile
- TC-TD-011: Xem bonding curve chart
- TC-TD-012: Copy token address
- TC-TD-013: Share token (Twitter/Telegram)
- TC-TD-014: Report token (spam/scam)
- TC-TD-015: Xem LP lock status
- TC-TD-016: Xem audit status
- TC-TD-017: Xem freeze authority status
- TC-TD-018: Real-time price update
- TC-TD-019: Real-time holder count update
- TC-TD-020: Real-time MC update
- TC-TD-021: Chat scroll to bottom
- TC-TD-022: Chat load more (pagination)
- TC-TD-023: Holder click → Public Profile
- TC-TD-024: Transaction click → Explorer
- TC-TD-025: Graduated badge hiển thị
- TC-TD-026: Raydium pool link (nếu graduated)

### FR-003: Mua/Bán Token (41 TCs)

**Market Orders (22 TCs)**
- TC-BS-001: Mở Trading Panel
- TC-BS-002: Mua token hợp lệ (verify số lượng token nhận được)
- TC-BS-003: Bán token hợp lệ (verify SOL nhận trừ 1% fee)
- TC-BS-004: Mua - Không đủ SOL
- TC-BS-005: Bán - Không đủ token
- TC-BS-006: Chọn slippage preset (0.5%/1%/3%)
- TC-BS-007: Chọn slippage custom
- TC-BS-008: Priority fee Normal
- TC-BS-009: Priority fee Fast
- TC-BS-010: Priority fee Turbo
- TC-BS-011: Bật Anti-MEV
- TC-BS-012: Bật Auto-retry
- TC-BS-013: Validation min trade *(TBD - chưa chốt)*
- TC-BS-014: Tính toán tokens nhận được (Mua)
- TC-BS-015: Tính toán SOL nhận được (Bán)
- TC-BS-016: Creator fee 1% khi bán
- TC-BS-017: Price impact warning (>5%)
- TC-BS-018: Xác nhận giao dịch
- TC-BS-019: Mua thành công → +1 ticket
- TC-BS-020: Giao dịch thất bại → retry
- TC-BS-021: Hủy giao dịch
- TC-BS-022: Xem giao dịch trên explorer

**Limit Orders (19 TCs)**
- TC-BS-023: Tạo Buy limit order
- TC-BS-024: Tạo Sell limit order
- TC-BS-025: Validation target price ≠ current price
- TC-BS-026: Hủy limit order
- TC-BS-027: Auto-execute buy limit
- TC-BS-028: Auto-execute sell limit
- TC-BS-029: Xem Active Orders list
- TC-BS-030: Sửa limit order
- TC-BS-031: Limit order hết hạn
- TC-BS-032: Nhiều limit orders cùng token
- TC-BS-033: Không đủ balance tạo order
- TC-BS-034: Lịch sử orders
- TC-BS-035: Thông báo khi order execute
- TC-BS-036: Order partial fill
- TC-BS-037: Order fully filled
- TC-BS-038: Order hủy bởi user
- TC-BS-039: Order hủy bởi system
- TC-BS-040: Order priority queue
- TC-BS-041: Order slippage protection

### FR-004: My Profile (22 TCs)
- TC-MP-001: Tab Holdings - hiển thị danh sách
- TC-MP-002: Tab Holdings - tính P&L
- TC-MP-003: Tab Holdings - Sort by value
- TC-MP-004: Tab Created Tokens
- TC-MP-005: Tab Created - link Creator Dashboard
- TC-MP-006: Tab Edit - lần đầu set username
- TC-MP-007: Tab Edit - username locked sau khi set
- TC-MP-008: Tab Edit - validation username (3-20 chars)
- TC-MP-009: Tab Edit - validation username (alphanumeric + _)
- TC-MP-010: Tab Edit - username đã tồn tại
- TC-MP-011: Tab Edit - update avatar
- TC-MP-012: Tab Edit - update bio
- TC-MP-013: Tab Edit - update social links
- TC-MP-014: Tab Edit - display name locked
- TC-MP-015: Tab Edit - Privacy settings
- TC-MP-016: Privacy - toggle show holdings
- TC-MP-017: Privacy - toggle show transactions
- TC-MP-018: Tab Limit Orders
- TC-MP-019: Xem total portfolio value
- TC-MP-020: Export holdings CSV
- TC-MP-021: Quick sell từ holdings
- TC-MP-022: Xem token detail từ holdings

### FR-005: Public Profile (10 TCs)
- TC-PP-001: Xem public profile user khác
- TC-PP-002: Hiển thị holdings (nếu public)
- TC-PP-003: Ẩn holdings (nếu private)
- TC-PP-004: Hiển thị transactions (nếu public)
- TC-PP-005: Ẩn transactions (nếu private)
- TC-PP-006: Xem created tokens
- TC-PP-007: Xem rank & points
- TC-PP-008: Xem social links
- TC-PP-009: Copy wallet address
- TC-PP-010: Report user

### FR-006: Creator Dashboard (30 TCs)

**Dashboard & Revenue (15 TCs)**
- TC-CD-001: Xem danh sách tokens đã tạo
- TC-CD-002: Xem tổng revenue
- TC-CD-003: Xem revenue breakdown theo token
- TC-CD-004: Claim revenue
- TC-CD-005: Revenue history
- TC-CD-006: Token metrics (MC, Volume, Holders)
- TC-CD-007: Token performance chart
- TC-CD-008: Best performing token
- TC-CD-009: Total tokens created count
- TC-CD-010: Total graduated tokens
- TC-CD-011: Filter tokens by status
- TC-CD-012: Sort tokens by revenue
- TC-CD-013: Export revenue report
- TC-CD-014: Claim all revenue
- TC-CD-015: Revenue notification

**Token Management & Edit (15 TCs)**
- TC-CD-016: Cập nhật LP lock
- TC-CD-017: Cập nhật Audit
- TC-CD-018: Cập nhật Freeze authority
- TC-CD-019: Sửa token description
- TC-CD-020: Sửa token avatar
- TC-CD-021: Sửa social links token
- TC-CD-022: Tạo post mới
- TC-CD-023: Sửa post
- TC-CD-024: Xóa post
- TC-CD-025: Pin post
- TC-CD-026: Unpin post
- TC-CD-027: Post validation (max 500 chars)
- TC-CD-028: Upload ảnh vào post
- TC-CD-029: Xem post engagement
- TC-CD-030: Quản lý token visibility

### FR-007: Create Token (40 TCs)

**Step 1: Basic Info (10 TCs)**
- TC-CT-001: Validation name required
- TC-CT-002: Validation name max 32 chars
- TC-CT-003: Validation symbol required
- TC-CT-004: Validation symbol uppercase
- TC-CT-005: Validation symbol max 10 chars
- TC-CT-006: Validation statement max 60 chars
- TC-CT-007: Validation description max 500 chars
- TC-CT-008: AI assist statement
- TC-CT-009: AI assist description
- TC-CT-010: Next step enabled khi valid

**Step 2: Avatar (8 TCs)**
- TC-CT-011: Upload avatar (PNG/JPG)
- TC-CT-012: Validation file size max 5MB
- TC-CT-013: Validation file type
- TC-CT-014: AI generate avatar
- TC-CT-015: Preview avatar
- TC-CT-016: Remove avatar
- TC-CT-017: Crop avatar
- TC-CT-018: Skip avatar (optional)

**Step 3: Security (10 TCs)**
- TC-CT-019: Enable LP lock (+20 trust)
- TC-CT-020: Disable LP lock
- TC-CT-021: Enable Audit (+30 trust)
- TC-CT-022: Disable Audit
- TC-CT-023: Enable Freeze disabled (+25 trust)
- TC-CT-024: Disable Freeze disabled
- TC-CT-025: Trust score calculation
- TC-CT-026: Max trust score 75
- TC-CT-027: Min trust score 0
- TC-CT-028: Skip security (optional)

**Step 4: Initial Buy (6 TCs)**
- TC-CT-029: Enter initial buy amount
- TC-CT-030: Validation min 0.01 SOL
- TC-CT-031: Validation max = balance
- TC-CT-032: Calculate tokens received
- TC-CT-033: Skip initial buy
- TC-CT-034: Insufficient balance warning

**Step 5: Review & Create (6 TCs)**
- TC-CT-035: Review all information
- TC-CT-036: Edit any step
- TC-CT-037: Create token transaction
- TC-CT-038: Transaction success → +20 points
- TC-CT-039: Transaction failed
- TC-CT-040: Redirect to token detail

### FR-008: Leaderboard (8 TCs)
- TC-LB-001: Hiển thị top 3 featured cards
- TC-LB-002: Hiển thị table từ rank 4+
- TC-LB-003: Sort by MC (default)
- TC-LB-004: Sort by Volume 24h
- TC-LB-005: Sort by Holders
- TC-LB-006: Click token → Token Detail
- TC-LB-007: Quick Buy từ leaderboard
- TC-LB-008: Real-time ranking update

### FR-009: Rewards (10 TCs)
- TC-RW-001: Spin slot machine
- TC-RW-002: Deduct bet từ tickets
- TC-RW-003: Insufficient tickets error
- TC-RW-004: Calculate payout 3-of-a-kind
- TC-RW-005: Calculate payout 4-of-a-kind
- TC-RW-006: Jackpot 5-of-a-kind (0.01 SOL)
- TC-RW-007: Symbol multipliers (🌱=1, 🌿=2, 🌳=3, 🍀=4, 🌼=5)
- TC-RW-008: Claim rewards
- TC-RW-009: Spin history
- TC-RW-010: Ticket balance display

### FR-010: Referrals (13 TCs)
- TC-RF-001: Generate referral link
- TC-RF-002: Copy referral link
- TC-RF-003: Share Twitter
- TC-RF-004: Share Telegram
- TC-RF-005: View referred users list
- TC-RF-006: Calculate earnings (5% fees)
- TC-RF-007: Claim referral rewards
- TC-RF-008: Referral stats (total users, total earnings)
- TC-RF-009: Referral leaderboard
- TC-RF-010: Track referral activity
- TC-RF-011: Referral notification
- TC-RF-012: Referral link expiration
- TC-RF-013: Invalid referral code

### FR-011: Points & Ranking (14 TCs)
- TC-PT-001: Xem points dashboard
- TC-PT-002: Earn points - Trade (Volume × 5)
- TC-PT-003: Earn points - Sell không tính
- TC-PT-004: Earn points - Referral (NetVolume × 10)
- TC-PT-005: Earn points - Tạo token (+20)
- TC-PT-006: Earn points - Upload image (+10)
- TC-PT-007: Earn points - Trust settings (+20)
- TC-PT-008: Earn points - 10 buys milestone (+30)
- TC-PT-009: Rank Seed (0-499)
- TC-PT-010: Rank Sprout (500-1999)
- TC-PT-011: Rank Sapling (2000-9999)
- TC-PT-012: Rank Tree (10000-49999)
- TC-PT-013: Rank Ancient Tree (50000+)
- TC-PT-014: Points history (xem lịch sử, không có filter)

---

## 2. KIỂM THỬ BẢO MẬT (139 TCs)

### Authentication & Authorization (14 TCs)
- TC-SEC-001: Wallet signature hợp lệ
- TC-SEC-002: Wallet signature không hợp lệ
- TC-SEC-003: Token expiration
- TC-SEC-004: Session timeout
- TC-SEC-005: Concurrent sessions
- TC-SEC-006: Logout clear session
- TC-SEC-007: Unauthorized access block
- TC-SEC-008: Role-based access
- TC-SEC-009: API key validation
- TC-SEC-010: Refresh token
- TC-SEC-011: Brute force protection
- TC-SEC-012: Account lockout
- TC-SEC-013: Password reset (nếu có)
- TC-SEC-014: 2FA (nếu có)

### Input Validation & Injection (27 TCs)

**XSS (8 TCs)**
- TC-SEC-015: XSS trong token name
- TC-SEC-016: XSS trong token description
- TC-SEC-017: XSS trong chat message
- TC-SEC-018: XSS trong bio
- TC-SEC-019: XSS trong username
- TC-SEC-020: XSS trong post content
- TC-SEC-021: XSS trong social links
- TC-SEC-022: Stored XSS prevention

**SQL Injection (6 TCs)**
- TC-SEC-023: SQL injection trong search
- TC-SEC-024: SQL injection trong filter
- TC-SEC-025: SQL injection trong sort
- TC-SEC-026: SQL injection trong login
- TC-SEC-027: SQL injection trong API params
- TC-SEC-028: Prepared statements

**Other Injection (13 TCs)**
- TC-SEC-029: Command injection file upload
- TC-SEC-030: Path traversal
- TC-SEC-031: LDAP injection
- TC-SEC-032: XML injection
- TC-SEC-033: HTML injection
- TC-SEC-034: NoSQL injection
- TC-SEC-035: CRLF injection
- TC-SEC-036: Template injection
- TC-SEC-037: Code injection
- TC-SEC-038: OS command injection
- TC-SEC-039: XPATH injection
- TC-SEC-040: LDAP injection
- TC-SEC-041: Server-side injection

### API Security (19 TCs)
- TC-SEC-042: Rate limiting 100 req/min
- TC-SEC-043: Rate limit 429 error
- TC-SEC-044: CORS headers validation
- TC-SEC-045: CORS origin whitelist
- TC-SEC-046: API authentication required
- TC-SEC-047: Invalid API key reject
- TC-SEC-048: Request size limit
- TC-SEC-049: Invalid JSON reject
- TC-SEC-050: API versioning
- TC-SEC-051: Deprecated API warning
- TC-SEC-052: API response sanitization
- TC-SEC-053: API error handling
- TC-SEC-054: API logging
- TC-SEC-055: API monitoring
- TC-SEC-056: API timeout
- TC-SEC-057: API retry logic
- TC-SEC-058: API circuit breaker
- TC-SEC-059: API throttling
- TC-SEC-060: API quota management

### Wallet & Blockchain Security (15 TCs)
- TC-SEC-061: Transaction signature validation
- TC-SEC-062: Private key never exposed
- TC-SEC-063: Reentrancy attack prevention
- TC-SEC-064: Integer overflow prevention
- TC-SEC-065: Integer underflow prevention
- TC-SEC-066: MEV protection enabled
- TC-SEC-067: Front-running prevention
- TC-SEC-068: Sandwich attack prevention
- TC-SEC-069: Smart contract audit
- TC-SEC-070: Gas limit validation
- TC-SEC-071: Nonce management
- TC-SEC-072: Transaction replay prevention
- TC-SEC-073: Wallet connection timeout
- TC-SEC-074: Multi-sig support
- TC-SEC-075: Hardware wallet support

### Data Protection (13 TCs)
- TC-SEC-076: Encryption at rest
- TC-SEC-077: Encryption in transit (HTTPS)
- TC-SEC-078: TLS 1.3
- TC-SEC-079: Privacy settings enforced
- TC-SEC-080: Wallet address masking
- TC-SEC-081: PII protection
- TC-SEC-082: Data anonymization
- TC-SEC-083: GDPR compliance
- TC-SEC-084: Data retention policy
- TC-SEC-085: Data deletion
- TC-SEC-086: Backup encryption
- TC-SEC-087: Secure key storage
- TC-SEC-088: Password hashing (nếu có)

### Business Logic Security (18 TCs)
- TC-SEC-089: Price manipulation prevention
- TC-SEC-090: Wash trading detection
- TC-SEC-091: Pump & dump detection
- TC-SEC-092: Privilege escalation prevention
- TC-SEC-093: Race condition handling
- TC-SEC-094: Double spending prevention
- TC-SEC-095: Concurrent transaction handling
- TC-SEC-096: Order book manipulation
- TC-SEC-097: Flash loan attack prevention
- TC-SEC-098: Oracle manipulation
- TC-SEC-099: Slippage attack prevention
- TC-SEC-100: Liquidity attack prevention
- TC-SEC-101: Token supply manipulation
- TC-SEC-102: Fee manipulation
- TC-SEC-103: Reward manipulation
- TC-SEC-104: Points farming prevention
- TC-SEC-105: Referral abuse prevention
- TC-SEC-106: Bot detection

### Compliance & Geolocation (7 TCs)
- TC-SEC-107: Block Vietnam IP
- TC-SEC-108: VPN detection
- TC-SEC-109: Proxy detection
- TC-SEC-110: Tor detection
- TC-SEC-111: Geolocation accuracy
- TC-SEC-112: KYC compliance (nếu có)
- TC-SEC-113: AML compliance (nếu có)

### Additional Security (26 TCs)
- TC-SEC-114: CSRF protection
- TC-SEC-115: Clickjacking prevention
- TC-SEC-116: Content Security Policy
- TC-SEC-117: Secure headers
- TC-SEC-118: Cookie security
- TC-SEC-119: Session fixation prevention
- TC-SEC-120: Open redirect prevention
- TC-SEC-121: File upload validation
- TC-SEC-122: File type whitelist
- TC-SEC-123: File size limit
- TC-SEC-124: Malware scanning
- TC-SEC-125: DDoS protection
- TC-SEC-126: Bot mitigation
- TC-SEC-127: Captcha integration
- TC-SEC-128: Email verification
- TC-SEC-129: Phone verification (nếu có)
- TC-SEC-130: Audit logging
- TC-SEC-131: Security monitoring
- TC-SEC-132: Intrusion detection
- TC-SEC-133: Vulnerability scanning
- TC-SEC-134: Penetration testing
- TC-SEC-135: Security headers
- TC-SEC-136: Subresource integrity
- TC-SEC-137: Dependency scanning
- TC-SEC-138: License compliance
- TC-SEC-139: Security patch management

---

## 3. KIỂM THỬ HIỆU NĂNG (25 TCs)

### Load Testing (8 TCs)
- TC-PERF-001: Normal load 100 users (< 2s)
- TC-PERF-002: Peak load 500 users (< 3s)
- TC-PERF-003: Sustained load 200 users 2h (< 2.5s)
- TC-PERF-004: Spike test 0→1000 users (< 5s)
- TC-PERF-005: Page load time < 3s
- TC-PERF-006: API response < 500ms (P95)
- TC-PERF-007: Database query < 100ms
- TC-PERF-008: WebSocket latency < 500ms

### Stress Testing (5 TCs)
- TC-PERF-009: Max users 2000+
- TC-PERF-010: Database overload 10K queries/s
- TC-PERF-011: Memory stress 90%
- TC-PERF-012: CPU stress 95%
- TC-PERF-013: Network stress

### Endurance Testing (3 TCs)
- TC-PERF-014: 24h run - memory leaks
- TC-PERF-015: 7 days run - performance degradation
- TC-PERF-016: Connection pool 12h - leaks

### API Performance (6 TCs)
- TC-PERF-017: GET /tokens < 200ms
- TC-PERF-018: POST /trading/market < 300ms
- TC-PERF-019: GET /users/me < 150ms
- TC-PERF-020: WebSocket updates < 100ms
- TC-PERF-021: GET /leaderboard < 250ms
- TC-PERF-022: POST /tokens/create < 500ms

### Frontend Performance (3 TCs)
- TC-PERF-023: Lighthouse score > 90
- TC-PERF-024: First Contentful Paint < 1.5s
- TC-PERF-025: Time to Interactive < 3s

---

## 4. KIỂM THỬ KHẢ DỤNG (15 TCs)

### Navigation & Workflows (6 TCs)
- TC-UX-001: Onboarding flow mới user
- TC-UX-002: Token discovery → purchase
- TC-UX-003: Token creation wizard flow
- TC-UX-004: Profile setup flow
- TC-UX-005: Earning features access
- TC-UX-006: Help & support access

### UI/UX Design (5 TCs)
- TC-UX-007: Visual hierarchy & layout
- TC-UX-008: Color contrast & readability
- TC-UX-009: Button sizes & touch targets
- TC-UX-010: Form validation feedback
- TC-UX-011: Loading states & spinners

### Accessibility (4 TCs)
- TC-UX-012: Keyboard navigation
- TC-UX-013: Screen reader compatibility
- TC-UX-014: WCAG 2.1 AA compliance
- TC-UX-015: Color blindness support

---

## 5. KIỂM THỬ TƯƠNG THÍCH (12 TCs)

### Browser Compatibility (5 TCs)
- TC-COMPAT-001: Chrome latest 2 versions
- TC-COMPAT-002: Firefox latest 2 versions
- TC-COMPAT-003: Safari latest 2 versions
- TC-COMPAT-004: Edge latest
- TC-COMPAT-005: Brave latest

### Mobile Devices (3 TCs)
- TC-COMPAT-006: iOS 15+
- TC-COMPAT-007: Android 11+
- TC-COMPAT-008: Tablet responsive

### Wallet Compatibility (4 TCs)
- TC-COMPAT-009: Phantom wallet
- TC-COMPAT-010: Solflare wallet
- TC-COMPAT-011: Backpack wallet
- TC-COMPAT-012: Ledger hardware wallet

---

## 6. KIỂM THỬ HỒI QUY (50 TCs)

### Critical Path Testing (20 TCs)
- TC-REG-001: User authentication flow
- TC-REG-002: Token creation end-to-end
- TC-REG-003: Buy transaction flow
- TC-REG-004: Sell transaction flow
- TC-REG-005: Revenue claiming flow
- TC-REG-006: Referral system flow
- TC-REG-007: Points earning flow
- TC-REG-008: Rank progression flow
- TC-REG-009: Slot machine flow
- TC-REG-010: Profile editing flow
- TC-REG-011: Search & filter flow
- TC-REG-012: Favorites management
- TC-REG-013: Chat functionality
- TC-REG-014: Limit orders flow
- TC-REG-015: Token graduation flow
- TC-REG-016: Trust settings update
- TC-REG-017: Wallet connection flow
- TC-REG-018: Transaction signing flow
- TC-REG-019: Notification system
- TC-REG-020: Real-time updates

### Bug Fix Verification (15 TCs)
- TC-REG-021 đến TC-REG-035: Verify bug fixes

### Automated Regression (15 TCs)
- TC-REG-036 đến TC-REG-050: Automated API & UI tests

---

**TỔNG: ~450 TEST CASES**
