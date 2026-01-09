# Python GenAI Project Commands
# Install just: https://github.com/casey/just
# Usage: just <command>
# List all commands: just --list

# Default recipe to display help
default:
    @just --list

# ============================================
# Installation & Setup
# ============================================

# Create virtual environment and install core dependencies
install:
    @echo "Creating virtual environment and installing dependencies..."
    uv venv
    uv pip install -e .
    @echo "✓ Installation complete! Activate with: source .venv/bin/activate"

# Install development dependencies
install-dev:
    @echo "Installing development dependencies..."
    uv venv
    uv pip install -e ".[dev]"
    @echo "✓ Dev dependencies installed!"

# Install all dependencies (dev + all optional groups)
install-all:
    @echo "Installing all dependencies..."
    uv venv
    uv pip install -e ".[dev,genai,vector,database,web]"
    @echo "✓ All dependencies installed!"

# First-time setup (venv + dev install + pre-commit hooks)
setup:
    @echo "Running first-time setup..."
    just install-dev
    just pre-commit
    @echo ""
    @echo "✓ Setup complete!"
    @echo "Next steps:"
    @echo "  1. Activate venv: source .venv/bin/activate"
    @echo "  2. Copy .env file: cp .env.example .env"
    @echo "  3. Edit .env with your API keys"
    @echo "  4. Run validation: python scripts/setup_env.py"

# ============================================
# Development
# ============================================

# Run all tests
test:
    @echo "Running tests..."
    pytest

# Run tests with coverage report
test-cov:
    @echo "Running tests with coverage..."
    pytest --cov --cov-report=term-missing --cov-report=html
    @echo ""
    @echo "✓ Coverage report generated in htmlcov/index.html"

# Run tests in verbose mode
test-verbose:
    @echo "Running tests in verbose mode..."
    pytest -v

# Run only unit tests
test-unit:
    @echo "Running unit tests..."
    pytest -m unit

# Run only integration tests
test-integration:
    @echo "Running integration tests..."
    pytest -m integration

# Run tests excluding slow tests
test-fast:
    @echo "Running fast tests..."
    pytest -m "not slow"

# ============================================
# Code Quality
# ============================================

# Run ruff linter (check only)
lint:
    @echo "Running ruff linter..."
    ruff check .

# Run ruff linter with auto-fix
lint-fix:
    @echo "Running ruff linter with auto-fix..."
    ruff check --fix .

# Run ruff formatter (check only)
format-check:
    @echo "Checking code formatting..."
    ruff format --check .

# Run ruff formatter (apply changes)
format:
    @echo "Formatting code..."
    ruff format .

# Run mypy type checker
type-check:
    @echo "Running mypy type checker..."
    mypy src/

# Run all quality checks (lint + format + type)
check:
    @echo "Running all quality checks..."
    @echo "\n[1/3] Linting..."
    just lint
    @echo "\n[2/3] Format checking..."
    just format-check
    @echo "\n[3/3] Type checking..."
    just type-check
    @echo "\n✓ All checks passed!"

# Fix all auto-fixable issues (lint + format)
fix:
    @echo "Auto-fixing code issues..."
    just lint-fix
    just format
    @echo "✓ Auto-fix complete!"

# ============================================
# Pre-commit Hooks
# ============================================

# Install pre-commit hooks
pre-commit:
    @echo "Installing pre-commit hooks..."
    pre-commit install
    @echo "✓ Pre-commit hooks installed!"

# Run pre-commit on all files
pre-commit-all:
    @echo "Running pre-commit on all files..."
    pre-commit run --all-files

# Update pre-commit hook versions
pre-commit-update:
    @echo "Updating pre-commit hooks..."
    pre-commit autoupdate

# ============================================
# Cleanup
# ============================================

# Clean up cache files and build artifacts
clean:
    @echo "Cleaning up cache files and build artifacts..."
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
    find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
    find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
    find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
    find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name ".coverage" -delete 2>/dev/null || true
    find . -type f -name "*.pyc" -delete 2>/dev/null || true
    rm -rf build/ dist/ 2>/dev/null || true
    @echo "✓ Cleanup complete!"

# Clean everything including virtual environment
clean-all: clean
    @echo "Removing virtual environment..."
    rm -rf .venv
    @echo "✓ Full cleanup complete!"

# ============================================
# Running the Application
# ============================================

# Run the main application
run:
    @echo "Running application..."
    python -m my_package.main

# Run the application with INFO logging
run-verbose:
    @echo "Running application with verbose logging..."
    LOG_LEVEL=DEBUG python -m my_package.main

# Validate environment setup
validate:
    @echo "Validating environment setup..."
    python scripts/setup_env.py

# ============================================
# Dependencies
# ============================================

# Show installed packages
list:
    @echo "Installed packages:"
    uv pip list

# Show outdated packages
outdated:
    @echo "Checking for outdated packages..."
    uv pip list --outdated

# Update a specific package
update package:
    @echo "Updating {{package}}..."
    uv pip install --upgrade {{package}}

# Generate requirements.txt from current environment
freeze:
    @echo "Generating requirements.txt..."
    uv pip freeze > requirements.txt
    @echo "✓ requirements.txt generated!"

# ============================================
# Documentation
# ============================================

# Show project info
info:
    @echo "Project: my-genai-project"
    @echo "Python version: $(python --version)"
    @echo "UV version: $(uv --version)"
    @echo ""
    @echo "Key commands:"
    @echo "  just setup          - First-time project setup"
    @echo "  just install-dev    - Install dev dependencies"
    @echo "  just test           - Run tests"
    @echo "  just check          - Run all quality checks"
    @echo "  just run            - Run the application"
    @echo ""
    @echo "For all commands: just --list"

# ============================================
# CI/CD Simulation
# ============================================

# Run the same checks as CI would run
ci: check test
    @echo ""
    @echo "✓ CI checks passed!"
    @echo "This is what will run in CI/CD pipeline."
