# Source Code Directory

Place your Python package source code here.

## Recommended Structure

See `STRUCTURE_OPTIONS.md` in the root directory for different project structure patterns.

### Example: Basic Package

```
src/
└── your_package_name/
    ├── __init__.py
    ├── main.py
    ├── config.py
    └── ...
```

### Example: Feature-Based

```
src/
└── your_package_name/
    ├── __init__.py
    ├── core/
    ├── features/
    └── utils/
```

## Getting Started

1. Create your package directory: `mkdir -p src/your_package_name`
2. Add `__init__.py`: `touch src/your_package_name/__init__.py`
3. Start building your application!

The package name in `pyproject.toml` should match your directory name.
