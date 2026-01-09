#!/usr/bin/env python3
"""
Template Initialization Script

This script helps you customize the template for your new project.
It will:
1. Ask for your project name
2. Rename the package directory
3. Update pyproject.toml
4. Optionally reinitialize git
5. Remove itself (this script)
"""

import re
import shutil
import sys
from pathlib import Path


def to_snake_case(name: str) -> str:
    """Convert a name to snake_case for Python package names."""
    # Replace hyphens and spaces with underscores
    name = re.sub(r'[-\s]+', '_', name)
    # Remove any non-alphanumeric characters except underscores
    name = re.sub(r'[^\w]', '', name)
    # Convert to lowercase
    return name.lower()


def to_kebab_case(name: str) -> str:
    """Convert a name to kebab-case for project names."""
    # Replace underscores and spaces with hyphens
    name = re.sub(r'[_\s]+', '-', name)
    # Remove any non-alphanumeric characters except hyphens
    name = re.sub(r'[^\w-]', '', name)
    # Convert to lowercase
    return name.lower()


def get_user_input() -> tuple[str, str, str, str]:
    """Get project information from the user."""
    print("=" * 60)
    print("Python GenAI Template Initialization")
    print("=" * 60)
    print()

    # Project name
    while True:
        project_name = input("Enter your project name (e.g., 'My GenAI App'): ").strip()
        if project_name:
            break
        print("Project name cannot be empty!")

    # Generate defaults
    package_name = to_snake_case(project_name)
    pyproject_name = to_kebab_case(project_name)

    print()
    print(f"Suggested package name (Python): {package_name}")
    package_name_input = input(f"Press Enter to use '{package_name}' or enter a different name: ").strip()
    if package_name_input:
        package_name = to_snake_case(package_name_input)

    print()
    print(f"Suggested project name (pyproject.toml): {pyproject_name}")
    pyproject_name_input = input(f"Press Enter to use '{pyproject_name}' or enter a different name: ").strip()
    if pyproject_name_input:
        pyproject_name = to_kebab_case(pyproject_name_input)

    # Author info
    print()
    author_name = input("Enter your name (for pyproject.toml): ").strip() or "Your Name"
    author_email = input("Enter your email (for pyproject.toml): ").strip() or "your.email@example.com"

    return package_name, pyproject_name, author_name, author_email


def rename_package(old_name: str, new_name: str) -> bool:
    """Rename the package directory."""
    old_path = Path("src") / old_name
    new_path = Path("src") / new_name

    if not old_path.exists():
        print(f"❌ Package directory not found: {old_path}")
        return False

    if new_path.exists():
        print(f"❌ Target directory already exists: {new_path}")
        return False

    try:
        shutil.move(str(old_path), str(new_path))
        print(f"✓ Renamed package: {old_name} → {new_name}")
        return True
    except Exception as e:
        print(f"❌ Failed to rename package: {e}")
        return False


def update_pyproject_toml(
    package_name: str,
    project_name: str,
    author_name: str,
    author_email: str
) -> bool:
    """Update pyproject.toml with new project information."""
    pyproject_path = Path("pyproject.toml")

    if not pyproject_path.exists():
        print("❌ pyproject.toml not found!")
        return False

    try:
        content = pyproject_path.read_text()

        # Update project name
        content = re.sub(
            r'name = "template-package"',
            f'name = "{project_name}"',
            content
        )

        # Update description
        content = re.sub(
            r'description = ".*template.*"',
            f'description = "{project_name} - A GenAI application"',
            content,
            flags=re.IGNORECASE
        )

        # Update author
        content = re.sub(
            r'name = "Your Name"',
            f'name = "{author_name}"',
            content
        )
        content = re.sub(
            r'email = "your\.email@example\.com"',
            f'email = "{author_email}"',
            content
        )

        pyproject_path.write_text(content)
        print("✓ Updated pyproject.toml")
        return True
    except Exception as e:
        print(f"❌ Failed to update pyproject.toml: {e}")
        return False


def update_package_init(package_name: str) -> bool:
    """Update the package __init__.py file."""
    init_path = Path("src") / package_name / "__init__.py"

    if not init_path.exists():
        print(f"⚠️  Warning: {init_path} not found")
        return True  # Not critical

    try:
        content = f'''"""
{package_name.replace('_', ' ').title()}

Your GenAI application package.
"""

__version__ = "0.1.0"

__all__ = ["__version__"]
'''
        init_path.write_text(content)
        print(f"✓ Updated {package_name}/__init__.py")
        return True
    except Exception as e:
        print(f"⚠️  Warning: Failed to update __init__.py: {e}")
        return True  # Not critical


def reinit_git() -> bool:
    """Ask if user wants to reinitialize git."""
    print()
    response = input("Reinitialize git repository? (removes old history) [y/N]: ").strip().lower()

    if response in ['y', 'yes']:
        try:
            git_dir = Path(".git")
            if git_dir.exists():
                shutil.rmtree(git_dir)
                print("✓ Removed old .git directory")

            import subprocess
            subprocess.run(["git", "init"], check=True, capture_output=True)
            print("✓ Initialized new git repository")
            return True
        except Exception as e:
            print(f"⚠️  Warning: Git reinitialization failed: {e}")
            return False

    return True


def remove_self() -> None:
    """Remove this initialization script."""
    script_path = Path(__file__)
    try:
        script_path.unlink()
        print(f"✓ Removed initialization script: {script_path.name}")
    except Exception as e:
        print(f"⚠️  Warning: Could not remove script: {e}")


def main() -> int:
    """Main function."""
    # Check we're in the right directory
    if not Path("pyproject.toml").exists():
        print("❌ Error: pyproject.toml not found!")
        print("Please run this script from the template root directory.")
        return 1

    # Get user input
    package_name, project_name, author_name, author_email = get_user_input()

    print()
    print("=" * 60)
    print("Configuration Summary:")
    print("=" * 60)
    print(f"Package name: {package_name}")
    print(f"Project name: {project_name}")
    print(f"Author: {author_name} <{author_email}>")
    print("=" * 60)
    print()

    response = input("Proceed with these settings? [Y/n]: ").strip().lower()
    if response in ['n', 'no']:
        print("Aborted.")
        return 0

    print()
    print("Initializing template...")
    print()

    # Perform updates
    success = True
    success &= rename_package("template_package", package_name)
    success &= update_pyproject_toml(package_name, project_name, author_name, author_email)
    success &= update_package_init(package_name)
    success &= reinit_git()

    if success:
        print()
        print("=" * 60)
        print("✓ Template initialized successfully!")
        print("=" * 60)
        print()
        print("Next steps:")
        print("  1. Run: uv venv && uv pip install -e '.[dev]'")
        print("  2. Run: uv run pre-commit-install")
        print("  3. Copy .env.example to .env and add your API keys")
        print("  4. Start building your GenAI application!")
        print()

        # Remove this script
        response = input("Remove this initialization script? [Y/n]: ").strip().lower()
        if response not in ['n', 'no']:
            remove_self()

        return 0
    else:
        print()
        print("=" * 60)
        print("❌ Initialization completed with errors")
        print("=" * 60)
        print("Please review the errors above and fix manually if needed.")
        return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\nAborted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
