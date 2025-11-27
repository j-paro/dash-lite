# Tests

This directory contains the test suite for dash-lite.

## Structure

- `conftest.py` - Pytest configuration and shared fixtures
- `test_app.py` - Tests for the main application module
- `test_layout.py` - Tests for the layout components
- `test_callbacks.py` - Tests for callback functions

## Running Tests

Run all tests:
```powershell
poetry run pytest
```

Run with coverage report:
```powershell
poetry run pytest --cov=src/dash_lite --cov-report=html
```

Run specific test file:
```powershell
poetry run pytest tests/test_callbacks.py
```

Run specific test:
```powershell
poetry run pytest tests/test_callbacks.py::test_friendly_greeting
```

Run tests by marker:
```powershell
poetry run pytest -m unit
```

## Test Markers

- `@pytest.mark.integration` - Integration tests (with Dash server)
- `@pytest.mark.slow` - Tests that take longer to run

By default, all tests without markers are unit tests (isolated, fast).

## Coverage

Coverage reports are generated in `htmlcov/` directory. Open `htmlcov/index.html` in a browser to view detailed coverage.

Target coverage: 80%+ for critical paths (app initialization, callbacks, layout generation)
