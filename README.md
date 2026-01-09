# Python GenAI Project Template

A production-ready template for building GenAI applications with modern Python tooling.

## Features

- **UV** - Fast, reliable Python package manager
- **Ruff** - Lightning-fast linting and formatting
- **pytest** - Comprehensive testing with coverage
- **mypy** - Static type checking
- **Pre-commit hooks** - Automated code quality checks
- **Just** - Command runner for common development tasks
- **Claude Code ready** - Pre-configured permissions for AI-assisted development
- **Flexible structure** - Adapt to any project layout
- **Environment management** - Secure configuration handling

## Using This Template

This repository is a ready-to-use template for starting new Python GenAI projects.

### Option 1: Quick Start (Automated)

```bash
# Clone the template
git clone https://github.com/Jyoti-Ranjan-Das845/startet-template.git my-new-project
cd my-new-project

# Run the initialization script (will ask for your project name)
python init_template.py

# Start building!
```

### Option 2: Manual Setup

```bash
# 1. Clone the template
git clone https://github.com/Jyoti-Ranjan-Das845/startet-template.git my-new-project
cd my-new-project

# 2. Rename the package directory
mv src/template_package src/my_project_name

# 3. Update pyproject.toml
# Change: name = "template-package"
# To: name = "my-project-name"

# 4. Remove old git history (optional, to start fresh)
rm -rf .git
git init

# 5. Run setup
just setup

# 6. Create your first commit
git add .
git commit -m "Initial commit"
```

### Option 3: Use GitHub's "Use this template" Button

1. Click the green "Use this template" button on GitHub
2. Create your new repository
3. Clone your new repository
4. Run `python init_template.py` to customize
5. Start coding!

## Quick Start

### Prerequisites

- Python 3.10 or higher
- UV package manager
- Just command runner (optional but recommended)

### Install Required Tools

#### Install UV

If you haven't installed UV yet:

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or with pip
pip install uv
```

#### Install Just (Optional but Recommended)

Just is a command runner that makes development tasks easier:

```bash
# macOS
brew install just

# Linux
cargo install just
# or
wget -qO - 'https://proget.makedeb.org/debian-feeds/prebuilt-mpr.pub' | gpg --dearmor | sudo tee /usr/share/keyrings/prebuilt-mpr-archive-keyring.gpg 1> /dev/null
echo "deb [arch=all,$(dpkg --print-architecture) signed-by=/usr/share/keyrings/prebuilt-mpr-archive-keyring.gpg] https://proget.makedeb.org prebuilt-mpr $(lsb_release -cs)" | sudo tee /etc/apt/sources.list.d/prebuilt-mpr.list
sudo apt update
sudo apt install just

# Windows (with Scoop)
scoop install just

# Or download from: https://github.com/casey/just/releases
```

See all available commands: `just --list`

### Project Setup

#### Option A: Using Just (Recommended)

```bash
# First-time setup (creates venv, installs dev deps, sets up pre-commit)
just setup

# Activate virtual environment
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# Copy and edit environment file
cp .env.example .env
# Edit .env with your API keys

# Validate setup
just validate
```

#### Option B: Manual Setup

1. **Clone/use this template** and navigate to the directory

2. **Create a virtual environment and install dependencies:**

   ```bash
   # Create virtual environment with UV
   uv venv

   # Activate virtual environment
   # macOS/Linux:
   source .venv/bin/activate
   # Windows:
   .venv\Scripts\activate

   # Install core dependencies
   uv pip install -e .

   # Install development dependencies
   uv pip install -e ".[dev]"
   ```

3. **Set up environment variables:**

   ```bash
   # Copy the example environment file
   cp .env.example .env

   # Edit .env and add your API keys
   # Never commit .env to version control!
   ```

4. **Install optional dependencies as needed:**

   ```bash
   # GenAI frameworks
   uv pip install -e ".[genai]"

   # Vector databases
   uv pip install -e ".[vector]"

   # Traditional databases
   uv pip install -e ".[database]"

   # Web/API frameworks
   uv pip install -e ".[web]"

   # Or install everything at once
   uv pip install -e ".[dev,genai,vector,database,web]"
   ```

5. **Set up pre-commit hooks (optional but recommended):**

   ```bash
   pre-commit install

   # Run manually on all files
   pre-commit run --all-files
   ```

## Development Workflow

### Using Just Commands (Recommended)

Just provides convenient shortcuts for all common tasks:

```bash
# Show all available commands
just --list

# Code quality
just lint              # Run linter
just lint-fix          # Run linter with auto-fix
just format            # Format code
just type-check        # Run type checking
just check             # Run ALL checks (lint + format + type)
just fix               # Auto-fix all issues

# Testing
just test              # Run all tests
just test-cov          # Run tests with coverage report
just test-unit         # Run only unit tests
just test-fast         # Skip slow tests

# Development
just run               # Run the application
just validate          # Validate environment setup
just clean             # Clean cache files

# Setup & maintenance
just install-dev       # Install dev dependencies
just pre-commit        # Install pre-commit hooks
just ci                # Run all CI checks locally
```

### Manual Commands (Without Just)

If you prefer not to use Just, you can run commands directly:

#### Code Quality

```bash
# Run linting
ruff check .

# Run linting with auto-fix
ruff check --fix .

# Run formatting
ruff format .

# Run type checking
mypy src/
```

#### Testing

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov

# Run specific test file
pytest tests/test_example.py

# Run tests matching a pattern
pytest -k "test_function_name"

# Run with verbose output
pytest -v

# Run only unit tests (if marked)
pytest -m unit

# Skip slow tests
pytest -m "not slow"
```

### Development Tips

- Use `uv pip list` to see installed packages
- Use `uv pip freeze` to see exact versions
- Update dependencies: `uv pip install --upgrade package-name`
- UV automatically handles virtual environments

## Project Structure

This template provides a minimal structure. See [STRUCTURE_OPTIONS.md](STRUCTURE_OPTIONS.md) for different layout patterns you can adapt:

```
.
├── .claude/                # Claude Code configuration
│   ├── config.json         # Permissions and settings
│   └── README.md           # Configuration guide
├── src/                    # Your source code (flexible)
├── tests/                  # Test files
├── scripts/                # Utility scripts
├── justfile                # Command runner tasks
├── pyproject.toml          # Project configuration
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## Adding Dependencies

### Option 1: Edit pyproject.toml

Add your dependency to the appropriate section in `pyproject.toml`, then:

```bash
uv pip install -e .
```

### Option 2: Direct installation

```bash
# Install and it will be tracked
uv pip install package-name

# To make it permanent, add to pyproject.toml
```

### Common GenAI Dependencies

Uncomment or add these to `pyproject.toml` as needed:

```toml
dependencies = [
    "langchain>=0.3.0",
    "openai>=1.0.0",
    "anthropic>=0.39.0",
    "chromadb>=0.5.0",
    "fastapi>=0.115.0",
    # ... add more
]
```

## Configuration

All tool configurations are in `pyproject.toml`:

- **Ruff**: Linting and formatting rules
- **MyPy**: Type checking settings
- **Pytest**: Test discovery and coverage
- **Coverage**: Coverage reporting options

Customize these to match your project needs!

## Environment Variables

Copy `.env.example` to `.env` and configure:

- LLM API keys (OpenAI, Anthropic, etc.)
- Vector database credentials
- Database connection strings
- Application settings

## Pre-commit Hooks

Automatically run checks before each commit:

- Ruff linting and formatting
- MyPy type checking
- File validation (no large files, no private keys, etc.)
- Security checks with Bandit

Bypass hooks if needed (not recommended):
```bash
git commit --no-verify
```

## Claude Code Configuration

This template comes pre-configured for Claude Code with optimized permissions:

### What's Pre-Configured

**Auto-approved commands:**
- `uv`, `pytest`, `ruff`, `mypy` - Development tools
- `just:test`, `just:lint`, `just:check`, etc. - Just recipes
- `git:status`, `git:diff`, `git:add` - Git operations (read + staging)
- `python:scripts/*` - Python execution in scripts/ only

**Auto-approved tools:**
- Read, Glob, Grep, Edit - File operations

**Protected files:**
- `.env` files, secrets, keys - Never accessible

### Customizing Permissions

See `.claude/README.md` and `CLAUDE_PERMISSIONS.md` for:
- Full list of available permissions
- Security best practices
- How to customize for your workflow

The configuration is balanced for productivity while protecting sensitive data.

## Common Commands Reference

### Quick Reference with Just

```bash
# First time setup
just setup                           # Complete project setup

# Daily development
just test                            # Run tests
just check                           # Run all quality checks
just fix                             # Auto-fix issues
just run                             # Run application

# Full command list
just --list                          # Show all available commands
```

### Detailed Commands (Manual)

```bash
# Setup
uv venv                              # Create virtual environment
uv pip install -e ".[dev]"          # Install dev dependencies

# Development
ruff check --fix .                   # Lint and fix
ruff format .                        # Format code
mypy src/                            # Type check
pytest                               # Run tests

# Package management
uv pip install package-name          # Add package
uv pip uninstall package-name        # Remove package
uv pip list                          # List packages
uv pip freeze                        # Show exact versions

# Pre-commit
pre-commit install                   # Setup hooks
pre-commit run --all-files          # Run manually
```

## Next Steps

1. Rename the project in `pyproject.toml`
2. Update author information
3. Choose and implement your project structure (see STRUCTURE_OPTIONS.md)
4. Add your GenAI framework dependencies
5. Start coding!

## Resources

- [UV Documentation](https://docs.astral.sh/uv/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Just Documentation](https://just.systems/)
- [pytest Documentation](https://docs.pytest.org/)
- [mypy Documentation](https://mypy.readthedocs.io/)
- [Pre-commit Documentation](https://pre-commit.com/)

## License

MIT License - Customize as needed
