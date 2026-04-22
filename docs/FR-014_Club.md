# FR-014: CLUB

## 1. Mô tả

Hệ thống Club cho phép cộng đồng tập hợp xung quanh một token. Mỗi token chỉ có 1 club duy nhất. Mỗi user chỉ tham gia 1 club tại mọi thời điểm. Club tạo identity, gắn kết cộng đồng, và là nền tảng cho Club War.

**User Story:**

```
Là một user,
Tôi muốn tạo hoặc tham gia club của token mình yêu thích,
Để cùng cộng đồng tham gia Arena, Club War, và kiếm rewards.
```

----------

## 2. Giao diện

[To be added]

----------

## 3. ĐIỂM TRUY CẬP (ENTRY POINTS)

Users có thể truy cập Club từ:

1. **Main Navigation** — Sidebar menu "Clubs"
2. **Token Detail** — "Join Club" button (nếu token có club)
3. **My Profile** — Club badge / Club info section
4. **Club War** — Link đến club profile
5. **Direct URL** — /clubs, /club/:id

**Default:** Hiển thị Club Leaderboard (danh sách clubs xếp hạng)

----------

## 4. YÊU CẦU CHỨC NĂNG

### 4.1. Club List Page

**FR-CLB-014.1: Danh sách Club**

**Mô tả:**
Trang chính hiển thị top clubs và danh sách đầy đủ.

**Yêu cầu:**

```
Page Structure:

1. Header
   - Title: "Clubs"
   - Stats: "X clubs · X members"
   - Button: "+ Create Club" (top-right)

2. Top 3 Podium
   - 3 cards nổi bật (giống Leaderboard FR-008)
   - Hiển thị: Avatar, Club Name, Token Symbol, Rank
   - Stats: Members, Win Rate, Pts/Week

3. Filter Tabs
   - [All] [Token Club] [Meme] [DeFi] [Football] [Anime] [Other]
   - Sort: [Rank] [Members] [Win Rate] [Pts/Week]

4. Search Bar
   - Placeholder: "Search clubs..."
   - Search by: Club name, Token name, Token symbol

5. Club Cards Grid
   - 3 columns desktop, 2 tablet, 1 mobile
   - Each card:
     * Club avatar (từ token avatar)
     * Club name + [TOKEN_SYMBOL]
     * Rank badge (#N)
     * Description (truncated 2 lines)
     * Tags (Meme, OG, Diamond Hands...)
     * Stats row: Members | Win Rate | Pts/Week | Level

VÀ club list PHẢI:
- Real-time stats updates
- Pagination (load more)
- Responsive grid
- Click card → Club Detail
```

**Acceptance Criteria:**

- [ ] Top 3 podium displays correctly
- [ ] Filter tabs work
- [ ] Search functional
- [ ] Sort options work
- [ ] Cards show accurate stats
- [ ] Pagination works
- [ ] Responsive layout

----------

### 4.2. Create Club

**FR-CLB-014.2: Tạo Club**

**Mô tả:**
Flow tạo club mới, gắn với 1 token trên platform.

**Yêu cầu:**

```
Điều kiện tạo:
- Wallet connected
- Có ít nhất 1 trade trên platform
- Token chưa có club (1 token = 1 club)
- Stake 0.5 SOL khi tạo (hoàn khi club đạt 10 members)

Form Fields:

1. Token * (required)
   - Dropdown/Search: chọn token trên platform
   - Chỉ hiện tokens chưa có club
   - Hiển thị: Avatar + Name + Symbol
   - Validation: Token must exist, no existing club

2. Club Name * (required)
   - Auto-fill: "[Token Name] Club"
   - Editable, max 40 characters
   - Validation: Not empty

3. Description * (required)
   - Textarea, 3 rows
   - Max 200 characters
   - Placeholder: "Mô tả club của bạn..."

4. Tags (optional)
   - Multi-select từ predefined list:
     [Meme] [OG] [Diamond Hands] [DeFi] [Moon]
     [Degen] [Community] [Anime] [Football] [Art]
   - Max 3 tags

5. Stake Confirmation
   - Display: "Stake 0.5 SOL để tạo club"
   - Note: "Hoàn lại khi club đạt 10 members"
   - Checkbox: "Tôi đồng ý stake 0.5 SOL"

6. Create Button
   - "Create Club"
   - Sign transaction → deploy

VÀ create club PHẢI:
- Validate token chưa có club
- Deduct 0.5 SOL stake
- Auto-set club avatar = token avatar
- Creator becomes Club Owner
- Club immediately visible in list
```

**Post-Creation:**

```
Success Screen:
- "Club Created Successfully!"
- Club card preview
- "Share on Twitter" button
- "Invite Members" link
- Auto-redirect to Club Detail (5s)

Club Owner auto-joined as first member.
```

**Acceptance Criteria:**

- [ ] Token search/select works
- [ ] Validation prevents duplicate clubs per token
- [ ] Stake deducted correctly
- [ ] Club created successfully
- [ ] Owner auto-joined
- [ ] Success screen displays
- [ ] Club visible in list immediately

----------

### 4.3. Club Detail Page

**FR-CLB-014.3: Chi tiết Club**

**Mô tả:**
Trang chi tiết club với thông tin, members, và hoạt động.

**Yêu cầu:**

```
Page Structure:

1. Club Header
   - Club avatar (80px, from token)
   - Club name + [TOKEN_SYMBOL] + Level badge
   - Description
   - Tags
   - Stats row: Members | Win Rate | Pts/Week | Level
   - Action buttons:
     * "Join Club" (nếu chưa join bất kỳ club)
     * "Leave Club" (nếu đang là member)
     * Disabled + tooltip nếu user đã ở club khác
     * "Manage" (chỉ Club Owner)

2. Tabs
   - [Members] [Activity] [Wars] [Token Info]

3. Tab: Members
   - Table: Rank | User | Contribution (pts/week) | Joined
   - Owner badge cho club owner
   - Sorted by contribution desc
   - Pagination

4. Tab: Activity
   - Feed các hoạt động gần đây:
     * "UserX joined the club"
     * "UserY traded 2 SOL of [TOKEN]"
     * "Club won war vs [CLUB_B]"
     * "Club reached Level 5"
   - Sorted newest first, load more

5. Tab: Wars
   - Danh sách Club Wars (active + history)
   - Each war: Opponent | Status | Result | Prize
   - Link to Club War detail

6. Tab: Token Info
   - Token metadata (from FR-002)
   - Current price, MC, volume
   - "Trade [TOKEN]" button → Token Detail

VÀ club detail PHẢI:
- Real-time member count
- Real-time activity feed
- Responsive tabs
```

**Acceptance Criteria:**

- [ ] Header displays correctly
- [ ] All 4 tabs functional
- [ ] Members table accurate
- [ ] Activity feed real-time
- [ ] Wars history shows
- [ ] Token info links to FR-002
- [ ] Join/Leave buttons work
- [ ] Responsive layout

----------

### 4.4. Join / Leave Club

**FR-CLB-014.4: Membership Flow**

**Mô tả:**
Quy trình join và leave club.

**Yêu cầu:**

```
JOIN Flow:

1. Điều kiện join:
   - Wallet connected
   - User chưa ở bất kỳ club nào (1 user = 1 club)
   - User chưa bị kick từ club này trong 7 ngày gần đây

2. Request:
   - Click "Join Club"
   - Confirm dialog: "Bạn muốn join [CLUB_NAME]?"
   - Submit → status: PENDING

3. Approval:
   - Club Owner nhận notification
   - Owner approve → user becomes MEMBER
   - Owner reject → user nhận notification "Request bị từ chối"

4. Post-Join:
   - User thấy club badge trên profile
   - User bắt đầu earn Club Points
   - Club member count +1

LEAVE Flow:

1. Điều kiện leave:
   - KHÔNG đang trong Club War active → block leave
   - Hiển thị: "Không thể rời club khi đang trong Club War"

2. Leave:
   - Click "Leave Club"
   - Confirm dialog:
     "Bạn chắc chắn muốn rời [CLUB_NAME]?
      Toàn bộ contribution history sẽ bị mất."
   - Confirm → removed immediately

3. Post-Leave:
   - Mất toàn bộ contribution history tại club
   - Club member count -1
   - User có thể join club khác ngay lập tức
   - NGOẠI TRỪ: không join lại club vừa rời trong 24h (cooldown)

KICK Flow:

1. Club Owner vào Members tab
2. Click "Kick" trên member row
3. Confirm: "Kick [USER] khỏi club?"
4. Member bị remove, nhận notification
5. Member không join lại được trong 7 ngày

VÀ membership PHẢI:
- Enforce 1 user = 1 club
- Block leave during active Club War
- Track join/leave history
- Notifications cho tất cả state changes
```

**Acceptance Criteria:**

- [ ] Join request works
- [ ] Owner approval flow works
- [ ] Owner reject flow works
- [ ] Leave with confirmation works
- [ ] Leave blocked during Club War
- [ ] Contribution history cleared on leave
- [ ] Kick flow works
- [ ] Cooldown enforced (24h rejoin, 7d after kick)
- [ ] Notifications sent

----------

### 4.5. Club Points & Level

**FR-CLB-014.5: Hệ thống Club Points**

**Mô tả:**
Club Points = tổng contribution của members. Club Level tích lũy từ Club Points.

**Yêu cầu:**

```
Club Points — nguồn:

┌────────────────────────────────────┬────────┐
│ Hành động member                   │ Club Pts│
├────────────────────────────────────┼────────┤
│ Trade token CỦA CLUB              │ +20    │
│ Trade token bất kỳ                 │ +5     │
│ Bet Arena bất kỳ                   │ +10    │
│ Bet Arena đúng                     │ +30    │
│ Complete Club Quest                │ +25    │
│ Club War thắng                     │ +500   │
│ Member mới join (per người)        │ +50    │
└────────────────────────────────────┴────────┘

Quy tắc:
- Club Points = tổng cộng dồn all-time
- Weekly Points = tổng điểm tuần hiện tại (reset Monday 00:00 UTC)
- Weekly Points dùng cho Club Leaderboard
- All-time Points dùng cho Club Level

Club Level:

┌────────┬──────────────┬──────────────────────┐
│ Level  │ Points cần   │ Unlock               │
├────────┼──────────────┼──────────────────────┤
│ Lv.1   │ 0            │ Tạo club             │
│ Lv.2   │ 500          │ —                    │
│ Lv.3   │ 1,500        │ —                    │
│ Lv.5   │ 5,000        │ Club badge on Arena  │
│ Lv.10  │ 25,000       │ Tạo Club War         │
│ Lv.15  │ 100,000      │ Custom club flair    │
│ Lv.20  │ 500,000      │ Max level badge      │
└────────┴──────────────┴──────────────────────┘

Hiển thị:
- Club card: Level badge (Lv.X)
- Progress bar: current / next level
- Weekly Pts chart (bar chart 7 ngày)

VÀ club points PHẢI:
- Cập nhật real-time khi member thực hiện hành động
- Weekly reset đúng lịch
- All-time KHÔNG reset
- Anti-farm: chỉ tính trade ≥ 0.01 SOL
```

**Acceptance Criteria:**

- [ ] Points earned correctly per action
- [ ] Weekly reset works (Monday 00:00 UTC)
- [ ] All-time accumulation correct
- [ ] Level up triggers correctly
- [ ] Level unlocks functional
- [ ] Progress bar accurate
- [ ] Anti-farm rules enforced

----------

### 4.6. Club Leaderboard

**FR-CLB-014.6: Bảng xếp hạng Club**

**Mô tả:**
Xếp hạng clubs theo Weekly Points. Top 3 nhận SOL rewards từ Reward Vault.

**Yêu cầu:**

```
Leaderboard:
- Ranked by: Weekly Club Points (default)
- Tabs: [Weekly] [Monthly] [All-time]
- Display: Top 3 podium + table list

Weekly Rewards (từ Reward Vault):
┌────────┬──────────────────────────────────┐
│ Rank   │ Reward                           │
├────────┼──────────────────────────────────┤
│ #1     │ 40% weekly reward pool           │
│ #2     │ 30% weekly reward pool           │
│ #3     │ 20% weekly reward pool           │
│ #4-10  │ Chia nhau 10% còn lại            │
└────────┴──────────────────────────────────┘

Weekly reward pool = accumulated Reward Vault weekly allocation.
Nếu Vault < 5 SOL → chỉ thưởng Points bonus, không SOL.

Reward Distribution:
- SOL chia đều cho TẤT CẢ members trong club
- Hoặc chia theo contribution % (top contributor nhận nhiều hơn)
- Club Owner quyết định kiểu chia (setting)

VÀ leaderboard PHẢI:
- Reset weekly (Monday 00:00 UTC)
- Snapshot trước khi reset để tính reward
- Auto-distribute rewards
- Hiển thị lịch sử tuần trước
```

**Acceptance Criteria:**

- [ ] Rankings accurate
- [ ] Weekly/Monthly/All-time tabs work
- [ ] Weekly reset + snapshot correct
- [ ] Rewards distributed from Vault
- [ ] Vault safety rule enforced (< 5 SOL)
- [ ] Distribution method configurable by owner
- [ ] History viewable

----------

### 4.7. Club Owner Management

**FR-CLB-014.7: Quản lý Club**

**Mô tả:**
Club Owner dashboard để quản lý club.

**Yêu cầu:**

```
Owner Panel (accessible via "Manage" button):

1. Club Settings
   - Edit Description
   - Edit Tags
   - Reward Distribution setting:
     [Equal] — chia đều
     [Contribution] — theo % đóng góp

2. Member Management
   - Pending Requests: [Approve] [Reject]
   - Member List: [Kick] button per member
   - Search members

3. Club Stats Dashboard
   - Total Members (trend chart)
   - Weekly Points (trend chart)
   - Win Rate (Club Wars)
   - Token trading volume from members

4. Club War Management
   - "Challenge Club" button
   - Active Wars status
   - War History

VÀ owner panel PHẢI:
- Only accessible by Club Owner
- Real-time pending request count badge
- Notification khi có new request
```

**Acceptance Criteria:**

- [ ] Only owner can access
- [ ] Edit settings works
- [ ] Approve/Reject requests works
- [ ] Kick member works
- [ ] Stats dashboard accurate
- [ ] War management functional

----------

## 5. BUSINESS RULES

```
Core Rules:
- 1 token = 1 club (unique, first come first served)
- 1 user = 1 club (at any time)
- Club Owner = người tạo club (không chuyển quyền V1)
- Stake 0.5 SOL khi tạo, hoàn khi đạt 10 members
- Leave blocked during active Club War
- Mất contribution history khi leave
- Cooldown: 24h rejoin club vừa rời, 7 ngày sau khi bị kick
- Club không thể xóa sau khi tạo (V1)
- Anti-farm: chỉ tính actions với trade ≥ 0.01 SOL
```

----------

## 6. ĐIỀU KIỆN CHẤP NHẬN (ACCEPTANCE CRITERIA)

**Overall:**

- [ ] Club creation works end-to-end
- [ ] 1 token = 1 club enforced
- [ ] 1 user = 1 club enforced
- [ ] Club Points tracked accurately
- [ ] Club Level progression correct
- [ ] Leaderboard rankings accurate
- [ ] Rewards distributed correctly
- [ ] Responsive on all devices

**Membership:**

- [ ] Join request → approval flow works
- [ ] Leave with confirmation works
- [ ] Leave blocked during Club War
- [ ] Kick with cooldown works

**Owner:**

- [ ] Management panel accessible
- [ ] Settings editable
- [ ] Member management functional

----------

**END OF FR-014**
