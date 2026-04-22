# FR-007: TẠO TOKEN (CREATE TOKEN)

## 1. Mô tả

Flow tạo token mới với 5 bước: Basic Info, Avatar, Security Settings, Initial Buy, và Review & Create.

**User Story:**

```
Là một user,
Tôi muốn tạo token meme của riêng mình,
Để launch project và kiếm revenue từ trading fees.
```

----------

## 2. Giao diện

[To be added]

----------

## 3. ĐIỂM TRUY CẬP (ENTRY POINTS)

Users có thể truy cập Create Token từ:

1. **Main Navigation** - Sidebar menu "Create Token"
2. **Token List** - "Create Token" button
3. **My Profile** - Created Tokens empty state
4. **Direct URL** - /create

**Default:** Mở Step 1 (Basic Info)

----------

## 4. YÊU CẦU CHỨC NĂNG

### 4.1. Overall Flow

**FR-CT-007.1: 5-Step Wizard**

**Mô tả:**  
Wizard flow với progress indicator và navigation.

**Yêu cầu:**

```
Flow Structure:

1. Progress Steps (Top)
   - 5 steps indicator
   - Progress line animation
   - States:
     * Active (current step - green)
     * Completed (checkmark - green)
     * Pending (gray)

2. Navigation
   - Previous button (disabled on step 1)
   - Next button (validates before proceeding)
   - Step labels:
     1. Basic Info
     2. Avatar
     3. Security
     4. Initial Buy
     5. Review

3. Validation
   - Validate each step before Next
   - Show error messages inline
   - Required fields marked with *

VÀ wizard PHẢI:
- Save progress (draft)
- Allow Previous navigation
- Clear validation errors
- Smooth transitions
```

**Acceptance Criteria:**

- [ ] Progress indicator works
- [ ] Navigation buttons functional
- [ ] Validation before Next
- [ ] Draft saving works

----------

### 4.2. Step 1 - Basic Information

**FR-CT-007.2: Token Metadata**

**Mô tả:**  
Form nhập thông tin cơ bản của token.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Form Fields:

1. Token Name * (required)
   - Input text
   - Max 32 characters
   - Character counter
   - Placeholder: "e.g., Pepe Seed"
   - Validation: Not empty, unique

2. Symbol * (required)
   - Input text
   - Max 10 characters
   - Auto uppercase
   - Placeholder: "e.g., PSEED"
   - Validation: 2-10 chars, letters only, unique
   - Hint: "2-10 characters, letters only"

3. Statement * (required)
   - Input text
   - Max 60 characters
   - Character counter
   - Placeholder: "Short catchy phrase about your token"
   - Validation: Not empty

4. Description * (required)
   - Textarea, 4 rows
   - Max 200 characters
   - Character counter
   - AI Assist button (top right)
   - Placeholder: "Tell people what makes your token special..."
   - Validation: Not empty

VÀ basic info PHẢI:
- Real-time character count
- Inline validation
- AI Assist for description
```

**AI Assist:**

```
Click "✨ AI Assist" button:
1. Open AI modal
2. User enters prompt/keywords
3. AI generates description
4. User can edit/accept
5. Fill into description field
```

**Acceptance Criteria:**

- [ ] All fields validate correctly
- [ ] Character counters accurate
- [ ] Symbol uniqueness check works
- [ ] AI Assist generates content
- [ ] Next button validates

----------

### 4.3. Step 2 - Avatar Upload

**FR-CT-007.3: Token Avatar**

**Mô tả:**  
Upload hoặc generate avatar cho token.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Avatar Options:

1. Preview
   - Large circle (120px)
   - Default: Emoji placeholder 🚀
   - Updates when image uploaded/generated

2. Upload Image
   - Upload box (dashed border)
   - Click to select file
   - Supported: PNG, JPG, GIF
   - Max size: 5MB
   - Auto crop to square
   - Preview after upload

3. AI Generator
   - Button: "✨ Generate with AI"
   - Click → AI generation modal
   - User enters prompt
   - AI generates image
   - Preview options (4 variants)
   - Select and apply

VÀ avatar PHẢI:
- Validate file type and size
- Crop to square automatically
- Optimize for web
```

**Acceptance Criteria:**

- [ ] Upload works
- [ ] File validation correct
- [ ] AI generation works
- [ ] Preview updates
- [ ] Image optimized

----------

### 4.4. Step 3 - Security Settings

**FR-CT-007.4: Trusted Level Initial Setup**

**Mô tả:**  
Cài đặt security features ban đầu.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Security Features:

1. LP Lock (Toggle)
   - Default: ON (enabled)
   - Label: "LP Lock"
   - Description: "Lock liquidity pool to prevent rug pulls"
   - Impact: +20 trust score

2. Request Audit (Toggle)
   - Default: OFF
   - Label: "Request Audit"
   - Description: "Get your token audited by verified auditors"
   - Impact: +30 trust score when completed

3. Disable Freeze Authority (Toggle)
   - Default: OFF
   - Label: "Disable Freeze Authority"
   - Description: "Increase trust by disabling freeze (permanent)"
   - Impact: +25 trust score
   - Warning: Permanent action

VÀ security settings PHẢI:
- Toggles save state
- Show trust score impact
- Warn about permanent actions
```

**Acceptance Criteria:**

- [ ] Toggles work
- [ ] Default states correct
- [ ] Trust score displayed
- [ ] Warnings shown

----------

### 4.5. Step 4 - Initial Buy (Optional)

**FR-CT-007.5: Initial Purchase**

**Mô tả:**  
Option để mua tokens ngay khi tạo.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Initial Buy Form:

1. Amount Input
   - Label: "Amount (SOL)"
   - Input: Number, min 0, step 0.1
   - Unit: SOL
   - Validation: ≥ 0, ≤ wallet balance

2. Quick Amounts
   - Buttons: [0.1 SOL] [0.5 SOL] [1 SOL] [Skip]
   - Click fills amount input
   - Skip → Proceed without buying

3. Preview
   - "You will receive"
   - "~XXX,XXX tokens" (calculated)
   - Based on bonding curve formula

VÀ initial buy PHẢI:
- Calculate tokens accurately
- Check wallet balance
- Allow skip
- Update preview real-time
```

**Token Calculation:**

```
Tokens = BondingCurve.calculateTokensOut(SOL_amount)
Display with ~XXX,XXX format
```

**Acceptance Criteria:**

- [ ] Amount input validates
- [ ] Quick buttons work
- [ ] Token calculation accurate
- [ ] Skip button works
- [ ] Balance check works

----------

### 4.6. Step 5 - Review & Create

**FR-CT-007.6: Final Review**

**Mô tả:**  
Review tất cả thông tin trước khi create.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Review Content:

1. Summary Card
   - Avatar preview (80px, centered)
   - Token info list:
     * Token Name
     * Symbol
     * Statement
     * Description (truncated)
     * LP Lock: ✓ Enabled / ✗ Disabled
     * Audit: ✓ Requested / ✗ Not Requested
     * Freeze: ✓ Disabled / ✗ Enabled
     * Initial Buy: X SOL or "Skipped"

2. Create Button
   - "Create Token 🚀"
   - Large, primary button
   - Requires wallet connection
   - Shows loading state

3. Transaction Flow
   - Click Create
   - Connect wallet (if not connected)
   - Sign transaction
   - Show loading: "Creating token..."
   - Deploy contract
   - Initialize bonding curve
   - Execute initial buy (if any)
   - Show success screen

VÀ review PHẢI:
- Show complete summary
- Require wallet connection
- Handle transaction errors
```

**Acceptance Criteria:**

- [ ] Summary displays all info
- [ ] Create button works
- [ ] Wallet connection required
- [ ] Transaction processes
- [ ] Loading states shown
- [ ] Error handling works

----------

### 4.7. Success Screen

**FR-CT-007.7: Token Created**

**Mô tả:**  
Celebration screen sau khi token được tạo thành công.

**Giao diện:**

[To be added]

**Yêu cầu:**

```
Success Content:

1. Celebration
   - Icon: 🎉 (large)
   - Title: "Token Created Successfully!"
   - Message: "Your token is now live on Solana"

2. Token Info Card
   - Token Name + Symbol
   - Contract Address (monospace, clickable)
   - Initial Market Cap (USD)

3. Action Buttons
   - "View Token Detail" (primary)
     → Navigate to Token Detail (FR-002)
   - "Share on Twitter" (secondary)
     → Open Twitter with pre-filled tweet

VÀ success screen PHẢI:
- Auto-redirect option (5s countdown)
- Copy contract address button
- Twitter share with token details
```

**Twitter Share Text:**

```
🚀 I just launched [TOKEN_NAME] ($[SYMBOL]) on @PumpFunSOL!

Contract: [ADDRESS]
Market Cap: $[MC]

Trade now: [URL]

#Solana #MemeCoin
```

**Acceptance Criteria:**

- [ ] Success message shows
- [ ] Token info accurate
- [ ] View Token works
- [ ] Share Twitter works
- [ ] Copy address works

----------

## 5. ĐIỀU KIỆN CHẤP NHẬN (ACCEPTANCE CRITERIA)

**Overall Flow:**

- [ ] 5 steps complete successfully
- [ ] Navigation works smoothly
- [ ] Validation prevents errors
- [ ] Draft saving works

**Steps:**

- [ ] Basic Info validates all fields
- [ ] Avatar upload/generate works
- [ ] Security settings apply
- [ ] Initial buy calculates correctly
- [ ] Review shows complete summary

**Creation:**

- [ ] Token deploys successfully
- [ ] Contract address generated
- [ ] Initial buy executes (if any)
- [ ] Success screen displays

**Post-Creation:**

- [ ] Token visible in lists
- [ ] Creator dashboard updated
- [ ] Trading enabled immediately

----------

**END OF FR-007**
