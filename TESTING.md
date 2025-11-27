# Testing Setup Guide

## Quick Start

Once you have network connectivity, install the dev dependencies:

```powershell
# Using Poetry (recommended)
poetry add --group dev pytest pytest-cov

# Or update pyproject.toml and run
poetry install
```

Then run the tests:

```powershell
poetry run pytest
```

## What Was Created

### Configuration Files

1. **`pyproject.toml`** (updated)
   - Added `[project.optional-dependencies]` section with pytest and pytest-cov
   - Added `[tool.pytest.ini_options]` for test configuration
   - Added `[tool.coverage.run]` and `[tool.coverage.report]` for coverage settings

2. **`pytest.ini`**
   - Basic pytest configuration (alternative to pyproject.toml settings)

3. **`.coveragerc`**
   - Coverage.py configuration file

### Test Files

1. **`tests/__init__.py`**
   - Package marker for tests directory

2. **`tests/conftest.py`**
   - Shared pytest fixtures
   - `dash_app` fixture - provides configured Dash app instance
   - `dash_duo` fixture - for browser-based integration tests (future use)

3. **`tests/test_app.py`**
   - Tests for main application module
   - Verifies app creation, layout, and callback registration

4. **`tests/test_layout.py`**
   - Tests for layout generation
   - Validates component structure and default values
   - Checks for required interactive elements

5. **`tests/test_callbacks.py`**
   - Tests for callback functions
   - Unit tests for `_build_greeting` helper function
   - Tests for the main greeting callback with various inputs

6. **`tests/README.md`**
   - Documentation for test suite usage

## Test Coverage

Current test suite covers:

- ✅ App initialization and configuration
- ✅ Layout structure and component IDs
- ✅ Default values for inputs
- ✅ Callback registration
- ✅ Greeting logic with all three styles
- ✅ Edge cases (empty names, whitespace, None values)

All tests are unit tests by default (no marker needed).

## Running Tests

```powershell
# Run all tests
poetry run pytest

# Run with verbose output
poetry run pytest -v

# Run with coverage
poetry run pytest --cov=src/dash_lite

# Run with HTML coverage report
poetry run pytest --cov=src/dash_lite --cov-report=html

# Run specific test file
poetry run pytest tests/test_callbacks.py

# Run specific test
poetry run pytest tests/test_callbacks.py::TestBuildGreeting::test_friendly_greeting

# Run by marker
poetry run pytest -m unit
```

## Test Markers

Tests are organized with markers:

- No marker - Unit tests (fast, isolated - this is the default)
- `@pytest.mark.integration` - Integration tests (requires running app)
- `@pytest.mark.slow` - Long-running tests

Run specific marker:
```powershell
pytest run pytest -m integration  # Only integration tests
pytest run pytest -m "not slow"   # Exclude slow tests
```

## Coverage Reports

After running with `--cov-report=html`, open `htmlcov/index.html` in your browser to see:

- Line-by-line coverage
- Branch coverage
- Missing lines highlighted
- Per-file coverage percentages

## Next Steps

1. Install dependencies when network is available
2. Run `poetry run pytest` to verify all tests pass
3. Add more integration tests using `dash.testing` as needed
4. Maintain 80%+ coverage for critical paths

## Common Commands

```powershell
# Install and test in one go
poetry install; poetry run pytest

# Quick test during development (no coverage)
poetry run pytest -v

# Generate and view coverage report
poetry run pytest --cov=src/dash_lite --cov-report=html; Start-Process htmlcov/index.html
```
