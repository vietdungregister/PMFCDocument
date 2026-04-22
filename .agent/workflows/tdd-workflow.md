---
description: Guided Test-Driven Development workflow with Red-Green-Refactor cycle
---

# TDD Workflow (Test-Driven Development)

Guided workflow theo TDD methodology với Red-Green-Refactor cycle.

## Prerequisites

1. Đọc skill: `.agent/skills/skills/test-driven-development/SKILL.md`
2. Hiểu rõ feature requirements
3. Testing framework đã setup (pytest, jest, etc.)

## Core Principle

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

## Steps

### 1. Understand Requirement
Clarify với user:
- What should the feature do?
- What are the inputs and outputs?
- What are edge cases?
- What errors should be handled?

### 2. RED - Write Failing Test

#### A. Design Test First
```python
# test_feature.py
def test_user_can_create_token():
    """User should be able to create a token with valid data"""
    # Arrange
    token_data = {
        'name': 'My Token',
        'symbol': 'MTK',
        'supply': 1000000
    }
    
    # Act
    result = create_token(token_data)
    
    # Assert
    assert result.success is True
    assert result.token.name == 'My Token'
    assert result.token.symbol == 'MTK'
```

#### B. Run Test - Verify It Fails
// turbo
```bash
pytest tests/test_feature.py -v
```

**Expected**: Test FAILS (not errors) vì `create_token()` chưa tồn tại

**Critical**: Phải xem test FAIL trước. Nếu test PASS ngay → đang test existing code, không phải TDD!

### 3. Verify RED Correctly

Kiểm tra:
- ✅ Test fails (not errors)
- ✅ Failure message là expected
- ✅ Fails vì feature missing (không phải typo)

**If test errors**: Fix error, re-run until it fails correctly
**If test passes**: You're testing existing behavior, fix test

### 4. GREEN - Write Minimal Code

Viết code tối thiểu để pass test:

```python
# feature.py
def create_token(token_data):
    """Create a new token"""
    # Minimal implementation
    return TokenResult(
        success=True,
        token=Token(
            name=token_data['name'],
            symbol=token_data['symbol'],
            supply=token_data['supply']
        )
    )
```

**Don't**:
- ❌ Add extra features not in test
- ❌ Refactor other code
- ❌ Over-engineer solution

**Do**:
- ✅ Simplest code that passes
- ✅ Hard-code if needed
- ✅ Focus only on making test green

### 5. Verify GREEN

// turbo
```bash
pytest tests/test_feature.py -v
```

**Expected**: Test PASSES

Kiểm tra:
- ✅ New test passes
- ✅ All other tests still pass
- ✅ No errors or warnings

**If test fails**: Fix code, not test
**If other tests fail**: Fix now before continuing

### 6. REFACTOR - Clean Up

Sau khi test GREEN, refactor:

```python
# Refactor: Extract validation
def create_token(token_data):
    _validate_token_data(token_data)  # Extracted
    
    return TokenResult(
        success=True,
        token=Token(
            name=token_data['name'],
            symbol=token_data['symbol'],
            supply=token_data['supply']
        )
    )

def _validate_token_data(data):
    if not data.get('name'):
        raise ValueError('Token name required')
    if not data.get('symbol'):
        raise ValueError('Token symbol required')
```

**Rules**:
- Keep tests green
- Don't add new behavior
- Improve code quality only

// turbo
```bash
pytest tests/test_feature.py -v
```

**Verify**: Tests still GREEN after refactor

### 7. Next Test - Add Edge Case

```python
def test_create_token_rejects_empty_name():
    """Should reject token with empty name"""
    token_data = {
        'name': '',
        'symbol': 'MTK',
        'supply': 1000000
    }
    
    with pytest.raises(ValueError, match='Token name required'):
        create_token(token_data)
```

### 8. Repeat Cycle

Quay lại Step 2 (RED) cho test mới:
1. RED - Write failing test
2. Verify RED
3. GREEN - Minimal code
4. Verify GREEN
5. REFACTOR
6. Next test

## TDD Checklist

Trước khi commit:

- [ ] Every function có test
- [ ] Watched each test FAIL before implementing
- [ ] Each test failed for right reason (feature missing)
- [ ] Wrote minimal code to pass
- [ ] All tests pass
- [ ] No errors/warnings
- [ ] Tests use real code (minimal mocking)
- [ ] Edge cases covered

**Can't check all boxes?** → Bạn đã skip TDD, start over!

## Common Mistakes to Avoid

| ❌ Wrong | ✅ Right |
|---------|---------|
| Write code first, test after | Write test first, watch fail |
| Test passes immediately | Test must fail first |
| "I'll test later" | Test NOW |
| "Too simple to test" | Everything gets tested |
| "Keep code as reference" | DELETE and start fresh |
| Over-engineer solution | Minimal code to pass |

## When Stuck

| Problem | Solution |
|---------|----------|
| Don't know how to test | Write wished-for API first |
| Test too complicated | Design too complex, simplify |
| Must mock everything | Code too coupled, use DI |
| Test setup huge | Extract helpers or simplify design |

## Example: Complete TDD Cycle

### Iteration 1: Happy Path

**RED**:
```python
def test_calculate_total_price():
    items = [
        {'price': 10, 'quantity': 2},
        {'price': 5, 'quantity': 3}
    ]
    assert calculate_total(items) == 35
```

**Verify RED**: ❌ `NameError: calculate_total not defined`

**GREEN**:
```python
def calculate_total(items):
    return sum(item['price'] * item['quantity'] for item in items)
```

**Verify GREEN**: ✅ Test passes

**REFACTOR**: Code is clean, no refactor needed

### Iteration 2: Edge Case

**RED**:
```python
def test_calculate_total_empty_list():
    assert calculate_total([]) == 0
```

**Verify RED**: ✅ Test passes (code already handles this!)

**Analysis**: Test passed immediately → not adding new behavior, good!

### Iteration 3: Error Handling

**RED**:
```python
def test_calculate_total_invalid_item():
    items = [{'price': 10}]  # Missing quantity
    with pytest.raises(KeyError):
        calculate_total(items)
```

**Verify RED**: ✅ Test fails correctly

**GREEN**:
```python
def calculate_total(items):
    total = 0
    for item in items:
        if 'price' not in item or 'quantity' not in item:
            raise KeyError('Item must have price and quantity')
        total += item['price'] * item['quantity']
    return total
```

**Verify GREEN**: ✅ All tests pass

**REFACTOR**: Extract validation
```python
def calculate_total(items):
    return sum(_calculate_item_total(item) for item in items)

def _calculate_item_total(item):
    _validate_item(item)
    return item['price'] * item['quantity']

def _validate_item(item):
    if 'price' not in item or 'quantity' not in item:
        raise KeyError('Item must have price and quantity')
```

**Verify GREEN**: ✅ All tests still pass

## Integration with Other Skills

- Use **testing-patterns** cho factory functions
- Use **unit-testing-test-generate** để suggest test cases
- Use **test-automator** cho CI/CD integration

## Final Reminder

```
If you didn't watch the test FAIL,
you don't know if it tests the right thing.
```

**NO EXCEPTIONS** without user permission!
