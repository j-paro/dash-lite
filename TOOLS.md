# Code Quality Tools

This project uses `just` for task automation with `black`, `ruff`, and `pre-commit`.

## Quick Start

```powershell
# Install just (if not already installed)
# Via scoop: scoop install just
# Via cargo: cargo install just

# Setup development environment
just setup

# Check code quality
just check

# Auto-fix issues
just fix
```

## Available Commands

### Setup & Installation
- `just install` - Install all dependencies
- `just setup` - Full dev setup (install + pre-commit hooks)

### Code Formatting (Black)
- `just format-check` - Check formatting without changes
- `just format` - Apply black formatting

### Linting (Ruff)
- `just lint` - Check code with ruff
- `just lint-fix` - Auto-fix linting issues

### Combined Operations
- `just check` - Run format-check + lint
- `just fix` - Run format + lint-fix
- `just ci` - Full CI pipeline (check + test)

### Pre-commit Hooks
- `just pre-commit-install` - Install git hooks
- `just pre-commit-run` - Run hooks on all files
- `just pre-commit-update` - Update hook versions

### Testing
- `just test` - Run pytest
- `just test-cov` - Run tests with coverage

### Running Apps
- `just run` - Start main app (port 8050)
- `just run-dmc` - Start DMC version (port 8052)
- `just run-tailwind` - Start Tailwind version (port 8051)

### Cleanup
- `just clean` - Remove cache and coverage files

## Tool Configuration

### Black
- Line length: 79 characters
- Target: Python 3.13
- Config: `[tool.black]` in `pyproject.toml`

### Ruff
- Line length: 79 characters
- Target: Python 3.13
- Linting rules: E, W, F, I, B, C4, UP, ARG, SIM
- Config: `[tool.ruff]` in `pyproject.toml`

### Pre-commit
- Runs on every git commit
- Includes: black, ruff, trailing whitespace, YAML/TOML checks
- Config: `.pre-commit-config.yaml`

## Workflow

### Daily Development
```powershell
just fix      # Format and fix linting issues
just test     # Run tests
```

### Before Committing
Pre-commit hooks run automatically, but you can also:
```powershell
just check    # Verify code quality
just ci       # Full pipeline (check + test)
```

### First Time Setup
```powershell
just setup    # Install deps + pre-commit hooks
```
