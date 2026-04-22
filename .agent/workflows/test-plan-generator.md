---
description: Generate comprehensive test plan using test-automator skill
---

# Test Plan Generator Workflow

Tự động tạo test plan toàn diện cho dự án sử dụng test-automator skill.

## Prerequisites

1. Đọc skill instructions: `.agent/skills/skills/test-automator/SKILL.md`
2. Hiểu rõ requirements và scope của dự án

## Steps

### 1. Gather Requirements
Thu thập thông tin từ user:
- Loại ứng dụng (web app, mobile app, API, microservices, etc.)
- Công nghệ stack
- Critical user workflows
- Performance requirements
- Security requirements
- Compliance requirements (nếu có)

### 2. Analyze Codebase
Phân tích codebase để xác định:
- Existing test coverage
- Testing frameworks đã sử dụng
- CI/CD pipeline hiện tại
- Test data management approach

### 3. Design Test Strategy
Tạo comprehensive test strategy bao gồm:

#### Test Pyramid
- **Unit Tests**: Coverage target, frameworks, patterns
- **Integration Tests**: API testing, contract testing
- **E2E Tests**: Critical user journeys, browser coverage
- **Performance Tests**: Load testing, stress testing
- **Security Tests**: SAST, DAST, penetration testing

#### Quality Metrics
- Code coverage targets
- Test execution time limits
- Defect detection rate
- Test stability metrics

### 4. Create Test Plan Document
Generate test plan với các sections:

```markdown
# Test Plan: [Project Name]

## 1. Introduction
- Purpose
- Scope
- Audience

## 2. Test Strategy
- Test Levels (Unit, Integration, E2E)
- Test Types (Functional, Performance, Security)
- Entry/Exit Criteria

## 3. Test Environment
- Hardware requirements
- Software requirements
- Test data requirements

## 4. Test Schedule
- Milestones
- Deliverables
- Resource allocation

## 5. Test Cases
- Test case categories
- Priority levels
- Traceability matrix

## 6. Defect Management
- Bug tracking process
- Severity levels
- Resolution workflow

## 7. Risk Management
- Identified risks
- Mitigation strategies

## 8. Automation Strategy
- Tools and frameworks
- Automation scope
- Maintenance plan

## 9. Reporting
- Metrics to track
- Report frequency
- Stakeholders
```

### 5. Define Test Cases Structure
Tạo template cho test cases:

```markdown
## Test Case Template

**ID**: TC-XXX
**Title**: [Descriptive title]
**Priority**: High/Medium/Low
**Type**: Functional/Performance/Security
**Preconditions**: 
**Steps**:
1. Step 1
2. Step 2
**Expected Result**:
**Actual Result**:
**Status**: Pass/Fail/Blocked
```

### 6. Setup CI/CD Integration
Đề xuất CI/CD pipeline configuration:
- Test execution triggers
- Parallel execution strategy
- Test result reporting
- Automated deployment gates

### 7. Present Test Plan
Trình bày test plan với user và thu thập feedback

### 8. Iterate Based on Feedback
Cập nhật test plan dựa trên user feedback

## Output Deliverables

1. **Test Plan Document** (Markdown format)
2. **Test Case Templates**
3. **CI/CD Configuration Examples**
4. **Test Data Strategy Document**
5. **Automation Roadmap**

## Best Practices

- Align với industry standards (ISO 29119, IEEE 829)
- Risk-based testing approach
- Shift-left testing mindset
- Continuous improvement metrics
- Clear traceability từ requirements đến test cases

## Example Usage

```
User: Tôi cần test plan cho PumpFun Clone project
AI: [Follows workflow steps]
1. Gathers info về Web3 features, Solana integration
2. Analyzes existing TEST_PLAN.md, TEST_E2E_SCENARIOS.md
3. Designs strategy covering smart contract testing, UI testing, API testing
4. Generates comprehensive test plan document
5. Presents for review
```
