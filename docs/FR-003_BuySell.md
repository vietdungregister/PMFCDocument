# FR-003: CHỨC NĂNG BUY/SELL

## 1. Mô tả

Trading panel cho phép user mua (BUY) hoặc bán (SELL) token ngay lập tức với Market Order hoặc đặt lệnh với giá mục tiêu thông qua Limit Order. Panel hiển thị cố định bên phải trang Token Detail.

**User Story:**

```
Là một trader,
Tôi muốn có thể mua hoặc bán token nhanh chóng,
Để tham gia giao dịch mà không cần rời khỏi trang chi tiết token.
```

----------

## 2. Giao diện

![Trading Panel UI - To be added]

----------

## 3. ĐIỂM TRUY CẬP (ENTRY POINTS)

Trading Panel là **component cố định** trong Token Detail page (FR-002):

- **Position:** Fixed bên phải màn hình
- **Context:** Token address inherit từ Token Detail page
- **Always visible:** Không cần click để mở, luôn hiển thị

----------

## 4. YÊU CẦU CHỨC NĂNG

### 4.1. Trading Panel Layout

**FR-BS-003.1: Cấu trúc Panel**

**Mô tả:**  
Trading panel hiển thị ở góc phải với layout rõ ràng, hierarchical.

**Yêu cầu:**

```
Panel Structure:

1. Token Context
   - Token name + symbol
   - Current price (real-time)
   - Inherited từ Token Detail page

2. Mode Selector (Hierarchical - 2 layers)
   
   Layer 1 - PRIMARY (Large, Prominent):
   - [BUY] / [SELL] buttons
   - BUY: Green
   - SELL: Red
   - Click switch → Clear form
   
   Layer 2 - SECONDARY (Small, Subtle):
   - ⚡ Market / 🎯 Limit toggle
   - Market: Default
   - Limit: Phụ, ít dùng hơn
   - Radio buttons hoặc small toggle

3. Form Area
   - Amount input
   - Preview panel
   - Settings
   - Risk assessment
   - Execute button
   - (Chi tiết ở sections sau)

VÀ panel PHẢI:
- Sticky scroll: Scroll cùng page hoặc fixed
- Responsive
```

**Acceptance Criteria:**

- [ ] Panel fixed bên phải
- [ ] BUY/SELL prominent
- [ ] Market/Limit subtle
- [ ] Token context sync đúng

----------

### 4.2. Market Order - Giao dịch Ngay

**FR-BS-003.2: Market Order Form**

**Mô tả:**  
Form giao dịch đơn giản, thực hiện ngay theo giá hiện tại.

**Giao diện:**

[Image: Market Order form - to be added]

**Yêu cầu:**

```
Market Order Form bao gồm 5 phần:

═══════════════════════════════════════
PHẦN 1: AMOUNT INPUT
═══════════════════════════════════════

1. Currency Switch
   - Toggle: SOL ⇄ [TOKEN]
   - Default: SOL
   - Click để đổi currency
   - Position: Góc phải của label "Amount"

2. Input Field
   - Type: Number
   - Placeholder: "0.00"
   - Real-time validation
   - Error messages inline

3. Quick Amount Buttons
   - SOL mode: 0.1 / 0.5 / 1 / MAX
   - Token mode: 25% / 50% / 75% / MAX
   - MAX = Balance - estimated fees

4. Balance Display
   - "Balance: X.XX SOL"
   - Real-time update
   - Small text dưới input

5. Swap Icon
   - Icon: ⇅
   - Click để swap From ↔ To

6. You Receive Field (Estimated)
   - Read-only
   - Auto-calculate từ amount input
   - Format: ~XXX,XXX PSEED
   - Balance display

═══════════════════════════════════════
PHẦN 2: MIN RECEIVED (Always Visible)
═══════════════════════════════════════

Display:
- "Min Received (X% slippage)"
- Value: ~XXX,XXX PSEED
- Luôn hiển thị
- Update real-time khi input changes

═══════════════════════════════════════
PHẦN 3: FEES (Collapsible - Mặc định ẩn)
═══════════════════════════════════════

Header:
- Text: "Fees"
- Chevron: ▼ (click to expand)
- NO summary amount (không hiện ~0.00501 SOL)

Content (khi expand):
- Solana network fee: ~0.00001 SOL
- Anti-MEV fee: 0.005 SOL (nếu enabled)
- Priority fee: +0.0001 SOL (nếu Fast)
- Priority fee: +0.0005 SOL (nếu Instant)

Note: 
- Chỉ hiển thị fees mà user THỰC SỰ trả
- KHÔNG hiển thị Bonding curve fee, Platform fee

═══════════════════════════════════════
PHẦN 4: ADVANCED SETTINGS (Expandable)
═══════════════════════════════════════

Settings Icon (⚙️) - Click to expand/collapse:

A. Slippage Tolerance
   - Preset: 0.5% / 1% / 2% / 5% / Custom
   - Default: 2%
   - Range: 0.1% - 50%
   - Warnings:
     * < 0.5%: "May fail"
     * > 10%: "High slippage risk"

B. Anti-MEV Protection
   - Toggle: ON / OFF
   - Default: ON
   - Fee: +0.5%
   - Update fees section khi toggle

C. Priority Fee (Speed)
   - Options: Normal (Free) / Fast / Instant
   - Default: Normal
   - Fast: +0.0001 SOL
   - Instant: +0.0005 SOL
   - Update fees section khi change

D. Auto-retry
   - Toggle: ON / OFF
   - Default: OFF
   - Max retries: 3

═══════════════════════════════════════
PHẦN 5: RISK ASSESSMENT
═══════════════════════════════════════

Risk Badge:
- Level: 🟢 Low / 🟡 Medium / 🔴 High
- Based on:
  * Liquidity depth
  * Holder concentration
  * Price volatility
  * Audit status

Behavior:
- Green: Proceed normally
- Yellow: Show warning → "I understand" checkbox → Can proceed
- Red: Block BUY, only allow SELL

═══════════════════════════════════════
PHẦN 6: EXECUTE BUTTON
═══════════════════════════════════════

Button:
- Text: "Buy [Amount] [Symbol]" / "Sell [Amount] [Symbol]"
- Color: Green (BUY) / Red (SELL)
- States:
  * Disabled: Invalid input / insufficient balance / Red risk
  * Enabled: Ready to trade
  * Loading: Transaction processing

VÀ market order PHẢI:
- Real-time preview updates
- Clear error messages
- Login + wallet required
```

**Business Rules:**

```
Validation:
- Amount > 0
- Amount ≤ Balance (for SOL input)
- Min trade: 0.001 SOL hoặc $1 equivalent

Fees (User-paid only):
- Solana network: ~0.00001 SOL (always)
- Anti-MEV: 0.5% of amount (if enabled)
- Priority: Variable (based on speed selection)

Note: Bonding curve fee (1%) và Platform fee (0.5%) 
KHÔNG hiển thị vì đây là phí hệ thống thu, không phải user trả thêm

Risk Check:
- Red risk: Block BUY button
- Yellow risk: Show warning modal
- Green risk: No restrictions

Slippage:
- Applied to expected output
- If actual price > (expected - slippage) → transaction fails
```

**Acceptance Criteria:**

- [ ] Form inputs work correctly
- [ ] Currency switch SOL ↔ Token works
- [ ] Quick buttons set correct amounts
- [ ] Min Received updates real-time
- [ ] Fees section expands/collapses
- [ ] Only user-paid fees displayed
- [ ] Advanced Settings expand/collapse
- [ ] Risk assessment blocks/warns properly
- [ ] Execute button states correct
- [ ] Validation messages clear

----------

### 4.3. Limit Order - Đặt lệnh

**FR-BS-003.3: Limit Order Form**

**Mô tả:**  
Form đặt lệnh với giá mục tiêu, thực hiện khi đạt giá.

**Giao diện:**

[Image: Limit Order form với target price và 2 input modes]

**Yêu cầu:**

```
Limit Order Form = Market Order Form + Target Price

═══════════════════════════════════════
CÁC THÀNH PHẦN GIỐNG MARKET ORDER
═══════════════════════════════════════

1. Token Header
   - Token Name + Symbol
   - Current Price + 24h Change

2. BUY/SELL Toggle (Primary - Large)
   - [BUY] / [SELL]
   - Green/Red colors

3. Market/Limit Toggle (Secondary - Small)
   - ○ Market  ● Limit
   - Limit được chọn

4. Amount Input
   - Currency Switch: SOL ⇄ Token
   - Amount input field
   - MAX button
   - Balance display
   - Quick buttons (0.1 / 0.5 / 1.0 / MAX)

5. Advanced Settings (Expandable)
   - Note: "Advanced settings (slippage, Anti-MEV, 
     priority fee) not applicable for limit orders"
   - Không có các settings như Market Order

6. Risk Assessment
   - Badge: 🟢 Low / 🟡 Medium / 🔴 High
   - Same logic as Market Order

7. Execute Button
   - Text: "Place Buy Order" / "Place Sell Order"
   - Color: Green (BUY) / Red (SELL)

═══════════════════════════════════════
THÊM MỚI CHO LIMIT ORDER
═══════════════════════════════════════

1. TARGET PRICE FIELD (2 Input Modes)

   Toggle Button: [USD ⇄]
   - Position: Góc phải label "Target Price"
   - Click để switch giữa USD và % modes
   
   ────────────────────────────────────
   MODE A: Absolute Price (USD)
   ────────────────────────────────────
   Label: "Target Price [USD ⇄]"
   
   Input Display:
   ┌─────────────────────┐
   │ $ [0.00150_______]  │
   └─────────────────────┘
   
   Info Display (dưới input):
   - "+21.9% from current" (nếu target > current)
   - "-15.5% from current" (nếu target < current)
   - Color: Green (tăng) / Red (giảm)
   
   Reference:
   - "Current: $0.00123"
   
   User Action:
   - Nhập giá tuyệt đối mong muốn
   - System auto-calculate % difference
   
   ────────────────────────────────────
   MODE B: Percentage Change (%)
   ────────────────────────────────────
   Label: "Target Price [% ⇄]"
   
   Input Display:
   ┌─────────────────────┐
   │ [+21.9_______] %    │
   └─────────────────────┘
   
   Info Display (dưới input):
   - "= $0.00150" (calculated price)
   - Color: Always neutral
   
   Reference:
   - "Current: $0.00123"
   
   User Action:
   - Nhập % tăng/giảm
   - Dương (+20): Tăng 20%
   - Âm (-10): Giảm 10%
   - System auto-calculate price
   
   ────────────────────────────────────
   Toggle Behavior:
   ────────────────────────────────────
   - Click [USD ⇄] → Switch mode
   - USD → %: Label changes, input re-format
   - % → USD: Label changes, input re-format
   - Values sync between modes
   - Calculation updates real-time

2. FEES SECTION (Collapsible)
   
   Header:
   - Label: "Fees (when executed)"
   - Chevron: ▼ (click to expand)
   - Mặc định: Collapsed (ẩn)
   
   Content (khi expand):
   - Solana network fee: ~0.00001 SOL
   - Note: "No slippage (exact target price)"
   
   Giải thích:
   - Fees chỉ trả KHI order execute
   - Không trả khi place order
   - Không có Anti-MEV fee (limit = exact price)
   - Không có slippage (execute at exact target)

═══════════════════════════════════════
BỎ ĐI (So với Market Order)
═══════════════════════════════════════

❌ Swap Button (⇅)
   - Không cần swap vì không có "You Receive"

❌ "You Receive" Field
   - Không hiển thị estimated output
   - Vì price chưa chắc chắn (chờ target)

❌ Min Received
   - Không cần vì execute at exact target price
   - No slippage

❌ Slippage Setting
   - Limit order = exact price
   - Không có slippage tolerance

❌ Anti-MEV Protection Toggle
   - Không applicable cho limit orders

❌ Priority Fee / Speed Selection
   - Không applicable khi place order
   - Chỉ apply khi order executes

❌ Reserved Balance Display
   - Không hiển thị trong UI
   - Backend vẫn track, nhưng không show user

VÀ limit order form PHẢI:
- Target price validation reasonable
- 2 input modes sync correctly
- Clear "when executed" messaging
- Simple, focused UI
```

**Business Rules:**

```
Target Price Validation:

1. Must be > 0
2. Reasonable range: 0.1x - 10x current price
3. Warnings:
   - If > 2x current: "Price is 2x higher than current"
   - If < 0.5x current: "Price is 50% lower than current"
4. Errors:
   - If > 10x current: "Target price too high (max 10x)"
   - If < 0.1x current: "Target price too low (min 0.1x)"

USD ⇄ % Sync Logic:

When user changes USD input:
- Calculate: % = ((Target - Current) / Current) × 100
- Update % mode value

When user changes % input:
- Calculate: Target = Current × (1 + % / 100)
- Update USD mode value

Examples:
- Current: $0.00123
- USD $0.00150 → % = +21.95%
- % +20 → USD = $0.001476

Reserved Balance (Backend Logic):

Note: Không hiển thị UI, nhưng backend xử lý:
- Calculate: Amount + Network Fee (~0.00001 SOL)
- Lock balance khi place order
- Release khi:
  * User cancels order
  * Order executes
  * Order expires (future feature)
- User không thể trade với reserved amount

Order Placement Flow:

1. User fills Amount + Target Price
2. System validates:
   - Amount > 0 and ≤ Available Balance
   - Target Price in reasonable range
3. User clicks "Place Order"
4. Backend:
   - Calculate reserved balance
   - Check sufficient balance
   - Lock reserved amount
   - Save order to database (Status: ACTIVE)
5. Show confirmation modal
6. Navigate to My Profile > Limit Orders

Order Execution (Backend):

1. System monitors price every 10-30s
2. Execution conditions:
   - BUY order: Current Price ≤ Target Price
   - SELL order: Current Price ≥ Target Price
3. When condition met:
   - Execute trade at EXACT target price
   - Deduct network fee from balance
   - Release remaining reserved balance
   - Update order status: COMPLETED
4. Send notification to user

Order Lifecycle:

┌─────────────┐
│   CREATED   │ User places order
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   ACTIVE    │ Monitoring price
└──┬───────┬──┘
   │       │
   │       └─────────────┐
   │                     │
   ▼                     ▼
┌─────────────┐   ┌─────────────┐
│  COMPLETED  │   │  CANCELLED  │
└─────────────┘   └─────────────┘
(Price reached)   (User cancelled)
```

**Acceptance Criteria:**

- [ ] Target Price field hiển thị đúng
- [ ] USD ⇄ % toggle works smoothly
- [ ] Mode switching syncs values correctly
- [ ] % difference calculated accurately
- [ ] Price validation warnings/errors clear
- [ ] Fees section shows "when executed"
- [ ] Advanced Settings note clear
- [ ] No Reserved Balance in UI
- [ ] Execute button text: "Place [Buy/Sell] Order"
- [ ] Order placement flow completes
- [ ] Navigation to My Profile works
- [ ] Balance locked correctly (backend)

----------

### 4.4. Transaction Flow

**FR-BS-003.4: Quy trình Giao dịch**

**Mô tả:**  
Xử lý transaction từ submit đến kết quả.

**Flow:**

```
Market Order Flow:

1. User Input Amount
   - Validate amount > 0
   - Check balance sufficient
   
2. User Adjust Settings (optional)
   - Expand Advanced Settings
   - Set slippage
   - Toggle Anti-MEV
   - Select speed (Normal/Fast/Instant)
   
3. Review Preview
   - Min Received visible
   - Expand Fees to review (optional)
   
4. Risk Check:
   - Red → Block, show error
   - Yellow → Show warning modal → User confirms
   - Green → Proceed
   
5. User Click Execute
   
6. Wallet Confirmation
   - Phantom/Solflare popup
   - Show transaction details
   - User approves
   
7. Transaction Submitted
   
8. Show Loading State
   - "Processing transaction..."
   - Disable button
   
9. Transaction Processing (blockchain)
   - Wait for confirmation
   - Show progress indicator
   
10. Result:
    SUCCESS:
    - Show success modal:
      * Transaction hash (link to explorer)
      * Amounts (paid/received)
      * +1 reward ticket earned
    - Update user balance (real-time)
    - Clear form inputs
    - Update Token Detail page data
    
    FAIL:
    - Show error message
    - Offer retry (if auto-retry ON)
    - Keep form data

───────────────────────────────────────

Limit Order Flow:

1. User Input Amount
   - Validate amount
   
2. User Set Target Price
   - Choose mode: USD or %
   - Input target price/percentage
   - Validate reasonable range
   
3. Review Preview
   - Check Reserved Balance
   - Expand Fees (optional)
   
4. User Click "Place Order"
   
5. Order Validation
   - Check balance sufficient for reservation
   - Validate target price
   
6. Order Saved to Database
   - Status: ACTIVE
   - Reserved balance locked
   
7. Show Confirmation
   - "Order placed successfully"
   - Order details
   - Reserved balance amount
   
8. Navigate to My Profile > Limit Orders
   - Show active order in list
   - User can cancel anytime
```

**Error Handling:**

```
Common Errors:

1. Insufficient Balance
   - Message: "Insufficient SOL balance"
   - Action: Clear form or suggest lower amount

2. Slippage Exceeded
   - Message: "Price moved too much. Transaction failed."
   - Action: "Adjust slippage or retry"
   - Auto-retry if enabled

3. Network Error
   - Message: "Network error. Please retry."
   - Action: Retry button

4. Transaction Timeout
   - Message: "Transaction timeout. Check your wallet."
   - Action: Check wallet status

5. Unreasonable Target Price (Limit)
   - Message: "Target price too high/low. Max 10x current price."
   - Action: Adjust target price

Retry Logic (if auto-retry ON):
- Retry up to 3 times
- Wait 2s between retries
- Show retry attempt: "Retry 1/3..."
- If all retries fail → Show final error
```

**Success Flow:**

```
Market Order Success:

1. Success Modal Content:
   - ✅ "Transaction Successful!"
   - Transaction hash (clickable → Solana Explorer)
   - You Paid: X.XX SOL
   - You Received: XXX,XXX PSEED
   - 🎟️ +1 Reward Ticket earned
   - Close button

2. Auto Updates:
   - User balance updated
   - Token metrics refreshed
   - Transaction appears in history
   - Form cleared

3. User Actions:
   - Close modal → Continue trading
   - Click TX hash → View on explorer

───────────────────────────────────────

Limit Order Success:

1. Success Modal Content:
   - ✅ "Order Placed Successfully!"
   - Order ID
   - Target Price: $X.XXXX
   - Reserved Balance: X.XX SOL
   - "View in My Profile" button

2. Auto Updates:
   - Balance shows reserved amount
   - Order active in My Profile

3. Navigation:
   - Auto-navigate to My Profile > Limit Orders tab
   - OR user clicks "View in My Profile"
```

**Acceptance Criteria:**

- [ ] Market order flow completes successfully
- [ ] Limit order flow saves to database
- [ ] Risk check blocks/warns correctly
- [ ] Wallet confirmation prompt appears
- [ ] Loading states clear and visible
- [ ] Success modal shows correct info
- [ ] Error messages helpful and actionable
- [ ] Retry logic works (if enabled)
- [ ] Balance updates after trades
- [ ] Reserved balance locked for limit orders
- [ ] Navigation to My Profile works

----------

### 4.5. Real-time Updates

**FR-BS-003.5: Cập nhật Real-time**

**Mô tả:**  
Trading panel updates real-time để reflect current market.

**Yêu cầu:**

```
Real-time Updates:

1. Current Price (Token Header)
   - Update: Every 10s
   - WebSocket preferred, polling fallback
   - Pulse animation on change
   - Display: $X.XXXX ±X.X%

2. Min Received (Market Order)
   - Recalculate instantly when:
     * Amount input changes (debounced 300ms)
     * Slippage setting changes
     * Current price updates
   - Formula: Amount × Current Price × (1 - Slippage%)

3. Reserved Balance (Limit Order)
   - Calculate when:
     * Amount changes
     * Target price changes
   - Formula: Amount + Estimated Network Fee

4. You Receive (Market Order)
   - Update real-time as user types
   - Debounce: 300ms
   - Show estimated tokens received

5. Balance Display
   - Update after every transaction
   - Periodic check: Every 30s
   - Subtract reserved balance for limit orders

6. Fees Section Content
   - Update when:
     * Anti-MEV toggled ON/OFF
     * Speed changed (Normal/Fast/Instant)
   - Add/remove fee lines dynamically

7. Risk Level
   - Recalculate when:
     * Amount changes (affects liquidity impact)
     * Token metrics update (every 5 min)
     * Price volatility changes
   - Update badge color and text

VÀ updates PHẢI:
- Smooth animations (no jarring changes)
- No UI flickering
- Handle high-frequency updates gracefully
- Debounce user input (don't spam calculations)
```

**Update Frequencies:**

```
Element                 Frequency       Method
─────────────────────  ──────────────  ────────────
Current Price          10s             WebSocket/Poll
Min Received           On input change Debounced calc
You Receive            On input change Debounced calc
Reserved Balance       On input change Instant calc
User Balance           30s + on trade  Poll + Event
Risk Level             5 min + on amt  Poll + Calc
Token Metrics          30s             WebSocket/Poll
```

**Performance:**

```
Debouncing:
- User input: 300ms wait after last keystroke
- Prevents excessive calculations
- Smooth UX without lag

Caching:
- Cache current price for 10s
- Avoid redundant API calls
- Update only when price actually changes

Error Handling:
- If WebSocket fails → Fall back to polling
- If price fetch fails → Use cached value
- Show stale data indicator if > 1 min old
```

**Acceptance Criteria:**

- [ ] Price updates every 10s
- [ ] Min Received recalculates on input
- [ ] Reserved Balance accurate
- [ ] Balance updates after trades
- [ ] Risk level updates when needed
- [ ] No UI flickering
- [ ] Smooth animations
- [ ] Debouncing works correctly
- [ ] Fees section updates dynamically
- [ ] Fallback to polling if WebSocket fails

----------

## 5. ĐIỀU KIỆN CHẤP NHẬN (ACCEPTANCE CRITERIA)

**Overall Trading Panel:**

- [ ] Panel displays correctly bên phải Token Detail
- [ ] BUY/SELL toggle works
- [ ] Market/Limit toggle works
- [ ] All inputs validate properly
- [ ] Preview calculates accurately
- [ ] Settings expand/collapse
- [ ] Risk assessment functions correctly
- [ ] Execute button states correct
- [ ] Transactions process successfully
- [ ] Error handling works
- [ ] Real-time updates smooth

**Data Accuracy:**

- [ ] Prices accurate
- [ ] Fees calculated correctly
- [ ] Slippage applied properly
- [ ] Balance checks work
- [ ] Reserved balance tracked

**User Experience:**

- [ ] Form clear and intuitive
- [ ] Error messages helpful
- [ ] Loading states visible
- [ ] Success confirmations clear
- [ ] Mobile responsive (if applicable)

----------

**END OF FR-003**
