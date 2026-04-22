---
description: Generate test cases from requirements using unit-testing-test-generate skill
---

# Test Case Generator Workflow

Tự động generate test cases từ requirements và code analysis.

## Prerequisites

1. Đọc skill: `.agent/skills/skills/unit-testing-test-generate/SKILL.md`
2. Có access đến requirements hoặc user stories
3. Có access đến source code (nếu generate từ code)

## Steps

### 1. Identify Source
Xác định nguồn để generate test cases:
- **From Requirements**: User stories, functional specs
- **From Code**: Existing functions, classes, APIs
- **From User Flows**: E2E scenarios, user journeys

### 2. Analyze Requirements/Code
Phân tích để xác định:
- Testable units (functions, methods, components)
- Input parameters và types
- Expected outputs
- Edge cases và error conditions
- Dependencies cần mock

### 3. Generate Test Cases by Type

#### A. Unit Test Cases
Sử dụng unit-testing-test-generate skill:

```python
# Analyze code structure
- Identify functions and classes
- Extract parameters and return types
- Calculate complexity
- Identify dependencies

# Generate test cases
- Happy path tests
- Edge case tests
- Error handling tests
- Boundary value tests
```

#### B. Integration Test Cases
```markdown
**Test Case**: API Integration Test
- Setup: Mock external services
- Execute: Call API endpoint
- Verify: Response format, status codes
- Cleanup: Reset test data
```

#### C. E2E Test Cases
```markdown
**Test Case**: User Registration Flow
- Navigate to registration page
- Fill in valid user data
- Submit form
- Verify success message
- Verify email sent
- Verify user in database
```

### 4. Apply Testing Patterns
Sử dụng testing-patterns skill:

- **Factory Pattern**: Generate mock data
- **Arrange-Act-Assert**: Structure test cases
- **Given-When-Then**: BDD style test cases

### 5. Generate Test Code
Tạo actual test code:

#### Python/pytest
```python
import pytest
from unittest.mock import Mock, patch

class TestUserRegistration:
    @pytest.fixture
    def mock_user_data(self):
        return {
            'email': 'test@example.com',
            'password': 'SecurePass123',
            'username': 'testuser'
        }
    
    def test_register_user_success(self, mock_user_data):
        result = register_user(mock_user_data)
        assert result.success is True
        assert result.user_id is not None
    
    def test_register_user_duplicate_email(self, mock_user_data):
        with pytest.raises(DuplicateEmailError):
            register_user(mock_user_data)
```

#### JavaScript/Jest
```javascript
describe('User Registration', () => {
  const mockUserData = {
    email: 'test@example.com',
    password: 'SecurePass123',
    username: 'testuser'
  };

  it('should register user successfully', async () => {
    const result = await registerUser(mockUserData);
    expect(result.success).toBe(true);
    expect(result.userId).toBeDefined();
  });

  it('should reject duplicate email', async () => {
    await expect(registerUser(mockUserData))
      .rejects.toThrow(DuplicateEmailError);
  });
});
```

### 6. Generate Test Data
Tạo test data fixtures:

```python
# test_fixtures.py
def get_mock_user(overrides=None):
    default = {
        'id': '123',
        'email': 'test@example.com',
        'username': 'testuser',
        'role': 'user'
    }
    return {**default, **(overrides or {})}

def get_mock_token_data(overrides=None):
    default = {
        'name': 'Test Token',
        'symbol': 'TEST',
        'supply': 1000000,
        'decimals': 9
    }
    return {**default, **(overrides or {})}
```

### 7. Coverage Analysis
Phân tích coverage và identify gaps:

```bash
# Run coverage analysis
pytest --cov=src --cov-report=html

# Identify uncovered lines
# Generate additional test cases for gaps
```

### 8. Organize Test Cases
Tổ chức test cases theo structure:

```
tests/
├── unit/
│   ├── test_user_service.py
│   ├── test_token_service.py
│   └── test_validators.py
├── integration/
│   ├── test_api_endpoints.py
│   └── test_database.py
├── e2e/
│   ├── test_user_flows.py
│   └── test_token_creation.py
└── fixtures/
    ├── user_fixtures.py
    └── token_fixtures.py
```

### 9. Document Test Cases
Tạo test case documentation:

```markdown
# Test Cases: User Management

## TC-001: Register New User
**Priority**: High
**Type**: Functional
**Preconditions**: Database is empty
**Steps**:
1. Call registerUser() with valid data
2. Verify user created in database
3. Verify welcome email sent
**Expected**: User registered successfully
**Actual**: [To be filled during execution]
**Status**: [Pass/Fail]

## TC-002: Register Duplicate Email
**Priority**: High
**Type**: Negative
**Preconditions**: User with email exists
**Steps**:
1. Call registerUser() with existing email
2. Verify error thrown
**Expected**: DuplicateEmailError
**Actual**: [To be filled]
**Status**: [Pass/Fail]
```

### 10. Present Generated Test Cases
Trình bày test cases với user:
- Summary of coverage
- Test case count by type
- Identified gaps
- Recommendations

## Output Deliverables

1. **Test Code Files** (Python, JavaScript, etc.)
2. **Test Fixtures** (Mock data generators)
3. **Test Documentation** (Test case descriptions)
4. **Coverage Report** (Current coverage analysis)
5. **Gap Analysis** (Uncovered scenarios)

## Best Practices

- ✅ Follow AAA pattern (Arrange-Act-Assert)
- ✅ Use factory functions for test data
- ✅ One assertion per test (when possible)
- ✅ Clear, descriptive test names
- ✅ Test behavior, not implementation
- ✅ Mock external dependencies
- ✅ Clean up after tests

## Example Usage

```
User: Generate test cases cho token creation feature
AI: [Follows workflow]
1. Analyzes token creation code
2. Identifies parameters: name, symbol, supply, decimals
3. Generates test cases:
   - Valid token creation
   - Invalid name (empty, too long)
   - Invalid symbol (special chars)
   - Invalid supply (negative, zero)
   - Duplicate token name
4. Creates test code với pytest
5. Generates mock data factories
6. Presents coverage report
```
