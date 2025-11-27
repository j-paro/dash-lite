# dash-lite justfile - Task automation

# Set shell to PowerShell
set shell := ["powershell.exe", "-c"]

# Default recipe to display help
default:
    @just --list

# Install all dependencies including dev dependencies
install:
    poetry install --with dev

# Run black formatter (check only)
format-check:
    poetry run black --check src/ tests/

# Run black formatter (apply changes)
format:
    poetry run black src/ tests/

# Show formatting diff for a specific file
format-diff file:
    poetry run black --diff {{file}}

# Show formatting diff in VS Code diff viewer
format-diff-vscode file:
    $temp = New-TemporaryFile | Rename-Item -NewName { $_.Name -replace '\.tmp$','.py' } -PassThru; Copy-Item {{file}} $temp.FullName; poetry run black $temp.FullName --quiet; code --diff {{file}} $temp.FullName; Start-Sleep -Seconds 3; Remove-Item $temp.FullName

# Run ruff linter (check only)
lint:
    poetry run ruff check src/ tests/

# Run ruff linter (apply fixes)
lint-fix:
    poetry run ruff check --fix src/ tests/

# Run both black and ruff checks
check: format-check lint

# Run both black and ruff with auto-fix
fix: format lint-fix

# Install pre-commit hooks
pre-commit-install:
    poetry run pre-commit install

# Run pre-commit on all files
pre-commit-run:
    poetry run pre-commit run --all-files

# Update pre-commit hooks
pre-commit-update:
    poetry run pre-commit autoupdate

# Run tests with pytest
test:
    poetry run pytest

# Run tests with coverage report
test-cov:
    poetry run pytest --cov=src/dash_lite --cov-report=term-missing --cov-report=html

# Run the main dash-lite app
run:
    poetry run dashlite

# Run the DMC version
run-dmc:
    poetry run python -m using_dmc.app

# Run the Tailwind version
run-tailwind:
    poetry run python -m using_tailwind.app

# Clean generated files (cache, coverage, etc)
clean:
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue .pytest_cache, htmlcov, .coverage, .ruff_cache
    Get-ChildItem -Path . -Filter __pycache__ -Recurse -Directory | Remove-Item -Recurse -Force

# Run full CI pipeline (format, lint, test)
ci: check test

# Development setup (install + pre-commit hooks)
setup: install pre-commit-install
    Write-Host "Development environment ready! Run 'just run' to start the app."
