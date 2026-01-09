# Tests Directory

Place your test files here.

## Structure

Tests should mirror your source code structure:

```
tests/
├── __init__.py
├── test_module1.py
├── test_module2.py
└── feature_name/
    ├── __init__.py
    └── test_feature.py
```

## Naming Conventions

- Test files: `test_*.py` or `*_test.py`
- Test classes: `Test*`
- Test functions: `test_*`

## Running Tests

```bash
# Run all tests
just test
# or
pytest

# Run with coverage
just test-cov
# or
pytest --cov

# Run specific test file
pytest tests/test_module.py

# Run specific test function
pytest tests/test_module.py::test_function_name
```

## Writing Tests

```python
import pytest

def test_example():
    """Example test function."""
    assert 1 + 1 == 2

def test_with_fixture(tmp_path):
    """Example using pytest fixture."""
    test_file = tmp_path / "test.txt"
    test_file.write_text("content")
    assert test_file.read_text() == "content"

@pytest.mark.slow
def test_slow_operation():
    """Mark slow tests to skip them when needed."""
    pass
```

## Test Markers

Configure in `pyproject.toml`:

- `@pytest.mark.unit` - Unit tests
- `@pytest.mark.integration` - Integration tests
- `@pytest.mark.slow` - Slow tests (skip with `-m "not slow"`)

## Getting Started

1. Create `__init__.py`: `touch tests/__init__.py`
2. Create your first test: `touch tests/test_example.py`
3. Run tests: `just test`
