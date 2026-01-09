# Scripts Directory

Place utility scripts and automation tools here.

## Purpose

This directory is for:
- Setup and initialization scripts
- Data processing scripts
- Deployment automation
- Maintenance tasks
- One-off utilities

## Common Scripts

```
scripts/
├── setup_env.py           # Environment validation
├── ingest_data.py         # Data ingestion for RAG
├── setup_vector_db.py     # Initialize vector database
├── migrate_data.py        # Data migration
├── benchmark.py           # Performance testing
└── deploy.py              # Deployment automation
```

## Script Template

```python
#!/usr/bin/env python3
"""
Brief description of what this script does.
"""

import argparse
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Script description")
    parser.add_argument("--input", type=Path, help="Input file")
    parser.add_argument("--output", type=Path, help="Output file")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    logger.info("Starting script...")
    # Your logic here
    logger.info("Script completed!")


if __name__ == "__main__":
    main()
```

## Best Practices

1. **Make scripts executable:**
   ```bash
   chmod +x scripts/your_script.py
   ```

2. **Add shebang:**
   ```python
   #!/usr/bin/env python3
   ```

3. **Use argparse** for command-line arguments

4. **Add docstrings** and comments

5. **Handle errors gracefully:**
   ```python
   try:
       # risky operation
   except Exception as e:
       logger.error(f"Error: {e}")
       sys.exit(1)
   ```

6. **Log progress:**
   ```python
   logger.info("Processing file...")
   logger.debug("Detailed debug info")
   logger.warning("Something unexpected")
   logger.error("Error occurred")
   ```

## Running Scripts

```bash
# Direct execution (if executable)
./scripts/your_script.py --help

# Via Python
python scripts/your_script.py --input data.txt

# Via Just (if configured)
just run-script your_script.py

# From anywhere (if package installed)
python -m your_package.scripts.your_script
```

## Claude Code Permissions

Scripts in this directory can be executed by Claude Code with:
- `python:scripts/*` permission (already configured)

This allows Claude to run your utility scripts safely.

## Testing Scripts

Consider adding tests for complex scripts:

```
tests/
└── scripts/
    └── test_your_script.py
```

## Getting Started

1. Create your first script: `touch scripts/my_script.py`
2. Make it executable: `chmod +x scripts/my_script.py`
3. Add your logic
4. Run it: `python scripts/my_script.py`
