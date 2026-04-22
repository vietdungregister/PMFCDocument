# Hướng Dẫn Sử Dụng Slash Commands và Skills

## Vấn đề bạn gặp phải

Bạn không thể sử dụng lệnh slash để gọi Skills vì **thiếu thư mục workflows**.

## Giải pháp đã thực hiện

Đã tạo thư mục `.agent/workflows/` và các workflow files mẫu:

### 1. `/deep-research` - Nghiên cứu sâu với Google Gemini
**File**: `.agent/workflows/deep-research.md`
- Thực hiện nghiên cứu tự động đa bước
- Thời gian: 2-10 phút
- Chi phí: $2-5 mỗi lần
- Sử dụng: Phân tích thị trường, nghiên cứu kỹ thuật, so sánh công nghệ

### 2. `/api-documenter` - Tạo tài liệu API
**File**: `.agent/workflows/api-documenter.md`
- Tự động tạo tài liệu API từ code
- Hỗ trợ OpenAPI/Swagger
- Bao gồm examples và error codes

### 3. `/ui-ux-pro-max` - Phân tích UI/UX chuyên nghiệp
**File**: `.agent/workflows/ui-ux-pro-max.md`
- Đánh giá thiết kế UI/UX
- Kiểm tra accessibility (WCAG)
- Đề xuất cải tiến có ưu tiên

## Cách sử dụng Slash Commands

### Cú pháp cơ bản:
```
/tên-workflow
```

### Ví dụ:
```
/deep-research
```

Sau khi gõ lệnh slash, AI sẽ:
1. Đọc file workflow tương ứng
2. Thực hiện các bước được định nghĩa
3. Tương tác với bạn theo workflow

## Cách tạo Workflow mới cho Skills khác

Bạn có **84 skills** trong `.agent/skills/skills/`. Để tạo workflow cho bất kỳ skill nào:

### Bước 1: Xem danh sách skills
```bash
ls .agent/skills/skills/
```

### Bước 2: Đọc SKILL.md của skill bạn muốn
```bash
cat .agent/skills/skills/[tên-skill]/SKILL.md
```

### Bước 3: Tạo file workflow
Tạo file `.agent/workflows/[tên-skill].md` với cấu trúc:

```markdown
---
description: Mô tả ngắn gọn về workflow
---

# Tên Workflow

Mô tả chi tiết

## Steps

1. Bước đầu tiên
2. Bước thứ hai
// turbo (nếu muốn auto-run lệnh)
3. Bước thứ ba với lệnh
```

### Ví dụ Skills bạn có thể tạo workflow:

- `/aws-serverless` - Phát triển AWS Serverless
- `/angular` - Phát triển Angular
- `/api-design-principles` - Thiết kế API
- `/beautiful-prose` - Viết văn bản đẹp
- `/agent-evaluation` - Đánh giá AI agents
- `/billing-automation` - Tự động hóa billing

## Annotation đặc biệt

### `// turbo`
Đặt trước một bước để auto-run lệnh `run_command` mà không cần xác nhận:
```markdown
// turbo
3. Run command: `npm install`
```

### `// turbo-all`
Đặt ở đầu file để auto-run TẤT CẢ lệnh:
```markdown
---
description: Auto-run all commands
---
// turbo-all

# Workflow Name
...
```

## Kiểm tra Workflows hiện có

Xem tất cả workflows đã tạo:
```bash
ls .agent/workflows/
```

## Lưu ý quan trọng

1. **Tên file = Tên slash command**: File `deep-research.md` → lệnh `/deep-research`
2. **YAML frontmatter bắt buộc**: Phải có `description` trong `---`
3. **Workflows ≠ Skills**: 
   - Skills = Hướng dẫn và tài nguyên
   - Workflows = Quy trình thực thi cụ thể
4. **Auto-run cẩn thận**: Chỉ dùng `// turbo` cho lệnh an toàn

## Troubleshooting

### Lệnh slash không hoạt động?
- Kiểm tra file có đúng trong `.agent/workflows/`
- Kiểm tra YAML frontmatter hợp lệ
- Kiểm tra tên file (không có khoảng trắng, dùng dấu gạch ngang)

### Muốn xem workflow đang chạy gì?
AI sẽ tự động đọc và hiển thị các bước từ file workflow

## Tài nguyên

- Skills directory: `.agent/skills/skills/`
- Workflows directory: `.agent/workflows/`
- Mỗi skill có file `SKILL.md` với hướng dẫn chi tiết
