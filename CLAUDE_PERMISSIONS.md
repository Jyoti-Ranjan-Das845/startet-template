# Claude Code Permissions Guide

This document explains all permissions and configurations available for Claude Code in the `.claude` directory, specifically tailored for Python GenAI projects.

## Table of Contents

1. [Overview](#overview)
2. [Bash Command Permissions](#bash-command-permissions)
3. [File Access Permissions](#file-access-permissions)
4. [Tool Auto-Approval Settings](#tool-auto-approval-settings)
5. [Custom Settings](#custom-settings)
6. [Recommended Configuration](#recommended-configuration)
7. [Security Best Practices](#security-best-practices)
8. [Example Configuration](#example-configuration)

---

## Overview

### What is `.claude`?

The `.claude` directory contains configuration files that control how Claude Code interacts with your project:

```
.claude/
├── config.json          # Main configuration with permissions
└── commands/            # Custom slash commands (optional)
```

### Why Configure Permissions?

**Benefits:**
- **Speed up workflow** - No approval needed for common commands
- **Consistency** - Same behavior across sessions
- **Team alignment** - Share configurations via git

**Safety:**
- Only approve commands you trust
- Protect sensitive operations
- Review periodically

---

## Bash Command Permissions

Bash permissions allow Claude to run specific terminal commands without asking for approval each time.

### Format

```json
{
  "allowedBashCommands": [
    "command_name",           // Allow all uses of this command
    "command_name:arg",       // Allow specific argument
    "command_name:*"          // Wildcard - allow all arguments
  ]
}
```

### Recommended for Python GenAI Projects

#### Package Management (UV)

| Permission | What It Allows | Risk Level | Recommended |
|------------|----------------|------------|-------------|
| `uv` | All UV commands | Low | ✅ Yes |
| `uv:venv` | Create virtual environments | Very Low | ✅ Yes |
| `uv:pip` | Pip operations via UV | Low | ✅ Yes |
| `uv:pip:install` | Install packages only | Very Low | ✅ Yes |
| `uv:pip:list` | List packages | None | ✅ Yes |
| `uv:pip:freeze` | Show package versions | None | ✅ Yes |

**Why allow:** UV is essential for dependency management and is generally safe.

#### Testing (pytest)

| Permission | What It Allows | Risk Level | Recommended |
|------------|----------------|------------|-------------|
| `pytest` | All pytest commands | Very Low | ✅ Yes |
| `pytest:*` | Pytest with any arguments | Very Low | ✅ Yes |

**Why allow:** Running tests is a read-only operation and very safe.

#### Code Quality (Ruff)

| Permission | What It Allows | Risk Level | Recommended |
|------------|----------------|------------|-------------|
| `ruff` | All ruff commands | Low | ✅ Yes |
| `ruff:check` | Linting only | None | ✅ Yes |
| `ruff:format` | Auto-formatting | Low | ✅ Yes |

**Why allow:** Ruff is a linter/formatter with minimal risk.

#### Type Checking (mypy)

| Permission | What It Allows | Risk Level | Recommended |
|------------|----------------|------------|-------------|
| `mypy` | All mypy commands | None | ✅ Yes |
| `mypy:src/` | Type check src/ directory | None | ✅ Yes |

**Why allow:** Type checking is read-only and completely safe.

#### Command Runner (Just)

| Permission | What It Allows | Risk Level | Recommended |
|------------|----------------|------------|-------------|
| `just` | All just commands | Low-Medium | ⚠️ Consider |
| `just:test` | Run just test only | Very Low | ✅ Yes |
| `just:lint` | Run just lint only | None | ✅ Yes |
| `just:check` | Run quality checks | None | ✅ Yes |

**Why cautious:** Just executes recipes that could contain any command. Consider allowing specific recipes only.

#### Python Execution

| Permission | What It Allows | Risk Level | Recommended |
|------------|----------------|------------|-------------|
| `python` | All Python commands | Medium | ⚠️ Consider |
| `python:-m` | Module execution | Medium | ⚠️ Consider |
| `python:scripts/*` | Run scripts in scripts/ | Low | ✅ Yes |

**Why cautious:** Python can execute arbitrary code. Consider restricting to specific scripts.

#### File Operations

| Permission | What It Allows | Risk Level | Recommended |
|------------|----------------|------------|-------------|
| `chmod` | Change file permissions | Medium | ⚠️ Specific only |
| `chmod:+x` | Make files executable | Low | ✅ Yes |
| `mkdir` | Create directories | Low | ✅ Yes |
| `ls` | List directory contents | None | ✅ Yes |

**Note:** Claude Code prefers using dedicated tools (Read, Write, Glob) over bash for file ops.

#### Version Control (Git)

| Permission | What It Allows | Risk Level | Recommended |
|------------|----------------|------------|-------------|
| `git` | All git commands | High | ❌ No |
| `git:status` | Show git status | None | ✅ Yes |
| `git:diff` | Show diffs | None | ✅ Yes |
| `git:log` | Show commit history | None | ✅ Yes |
| `git:add` | Stage files | Low | ⚠️ Consider |
| `git:commit` | Create commits | Medium | ⚠️ Consider |
| `git:push` | Push to remote | High | ❌ No |
| `git:pull` | Pull from remote | Medium | ❌ No |

**Why cautious:** Git operations can modify history or push code. Only allow read operations by default.

#### Documentation

| Permission | What It Allows | Risk Level | Recommended |
|------------|----------------|------------|-------------|
| `cat` | Read files | None | ⚠️ Use Read tool |
| `head` | Read file start | None | ⚠️ Use Read tool |
| `tail` | Read file end | None | ⚠️ Use Read tool |

**Note:** Claude Code has dedicated Read tool - prefer that over bash commands.

#### Process Management

| Permission | What It Allows | Risk Level | Recommended |
|------------|----------------|------------|-------------|
| `ps` | List processes | None | ✅ Yes |
| `kill` | Terminate processes | High | ❌ No |

#### Environment

| Permission | What It Allows | Risk Level | Recommended |
|------------|----------------|------------|-------------|
| `env` | Show environment variables | Medium | ⚠️ Consider |
| `export` | Set environment variables | Medium | ❌ No |
| `source` | Execute shell scripts | High | ❌ No |

**Why cautious:** Can expose sensitive environment variables like API keys.

### Additional Tools for GenAI Projects

| Permission | What It Allows | Risk Level | Recommended |
|------------|----------------|------------|-------------|
| `curl` | HTTP requests | Medium | ⚠️ Specific URLs |
| `wget` | Download files | Medium | ⚠️ Specific URLs |
| `docker` | Container operations | High | ❌ No (ask per use) |
| `docker-compose` | Multi-container ops | High | ❌ No (ask per use) |

---

## File Access Permissions

Control which files and directories Claude can access.

### Configuration Options

```json
{
  "filePermissions": {
    "allowedPaths": [
      "/path/to/allowed/directory",
      "src/**/*",
      "tests/**/*"
    ],
    "deniedPaths": [
      ".env",
      "secrets/**/*",
      "*.key",
      "*.pem"
    ],
    "readOnlyPaths": [
      "docs/**/*"
    ]
  }
}
```

### Recommended Settings for This Template

**Allow (Read/Write):**
- `src/**/*` - Source code
- `tests/**/*` - Test files
- `scripts/**/*` - Utility scripts
- `docs/**/*` - Documentation
- `*.md` - Markdown files
- `*.py` - Python files
- `*.toml` - Configuration files
- `*.yaml` / `*.yml` - Config files

**Deny (No Access):**
- `.env` - Environment variables (contains secrets)
- `.env.local` - Local environment
- `secrets/**/*` - Any secrets directory
- `*.key` - Private keys
- `*.pem` - Certificates
- `credentials.json` - Credentials
- `.aws/**/*` - AWS credentials
- `.ssh/**/*` - SSH keys

**Read-Only:**
- `uv.lock` - Lock file (should be managed by UV)
- `.git/**/*` - Git internals

---

## Tool Auto-Approval Settings

Configure which Claude Code tools can be used without approval.

### Available Tools

```json
{
  "autoApproveTools": [
    "Read",        // Read files
    "Write",       // Write new files
    "Edit",        // Edit existing files
    "Bash",        // Execute bash commands (respects allowedBashCommands)
    "Glob",        // Pattern-based file search
    "Grep",        // Content search
    "WebFetch",    // Fetch web content
    "WebSearch"    // Web search
  ]
}
```

### Recommendations

| Tool | What It Does | Recommended | Notes |
|------|--------------|-------------|-------|
| `Read` | Read any file | ✅ Yes | Safe, read-only |
| `Glob` | Find files by pattern | ✅ Yes | Safe, read-only |
| `Grep` | Search file contents | ✅ Yes | Safe, read-only |
| `Edit` | Modify existing files | ⚠️ Consider | Review changes in git |
| `Write` | Create new files | ⚠️ Consider | Could overwrite files |
| `Bash` | Run bash commands | ⚠️ Depends | Only with allowedBashCommands |
| `WebFetch` | Fetch URLs | ⚠️ Consider | Could expose data |
| `WebSearch` | Search the web | ⚠️ Consider | Sends queries externally |

**Safe approach:**
- Always allow: `Read`, `Glob`, `Grep`
- Consider allowing: `Edit`, `Write` (you'll review in git)
- Control with allowedBashCommands: `Bash`
- Be cautious: `WebFetch`, `WebSearch`

---

## Custom Settings

### Status Line Configuration

Show useful information in the Claude Code status line:

```json
{
  "statusLine": {
    "enabled": true,
    "format": "{{project}} | {{branch}} | {{python_version}}"
  }
}
```

### Output Preferences

```json
{
  "output": {
    "style": "concise",        // "concise" or "verbose"
    "showLineNumbers": true,
    "maxOutputLines": 50
  }
}
```

### Working Directory

```json
{
  "workingDirectory": ".",
  "autoChangeDirectory": false
}
```

---

## Recommended Configuration

Here's our recommended `.claude/config.json` for this Python GenAI template:

### Option 1: Conservative (Safest)

```json
{
  "allowedBashCommands": [
    "uv:venv",
    "uv:pip:list",
    "uv:pip:freeze",
    "pytest",
    "ruff:check",
    "ruff:format",
    "mypy",
    "just:test",
    "just:lint",
    "just:check",
    "git:status",
    "git:diff",
    "git:log",
    "ls",
    "chmod:+x"
  ],
  "autoApproveTools": [
    "Read",
    "Glob",
    "Grep"
  ]
}
```

**Good for:** First-time users, sensitive projects, learning phase

### Option 2: Balanced (Recommended)

```json
{
  "allowedBashCommands": [
    "uv",
    "pytest",
    "ruff",
    "mypy",
    "just:test",
    "just:lint",
    "just:check",
    "just:run",
    "python:scripts/*",
    "git:status",
    "git:diff",
    "git:log",
    "git:add",
    "ls",
    "mkdir",
    "chmod:+x"
  ],
  "autoApproveTools": [
    "Read",
    "Glob",
    "Grep",
    "Edit"
  ],
  "filePermissions": {
    "deniedPaths": [
      ".env",
      ".env.*",
      "secrets/**/*",
      "*.key",
      "*.pem",
      "credentials.json"
    ]
  }
}
```

**Good for:** Active development, trusted environments, productivity

### Option 3: Permissive (For Experimentation)

```json
{
  "allowedBashCommands": [
    "uv",
    "pytest",
    "ruff",
    "mypy",
    "just",
    "python",
    "git:status",
    "git:diff",
    "git:log",
    "git:add",
    "git:commit",
    "ls",
    "mkdir",
    "chmod"
  ],
  "autoApproveTools": [
    "Read",
    "Glob",
    "Grep",
    "Edit",
    "Write",
    "Bash"
  ],
  "filePermissions": {
    "deniedPaths": [
      ".env",
      "*.key",
      "*.pem"
    ]
  }
}
```

**Good for:** Personal projects, rapid prototyping, solo development

---

## Security Best Practices

### ❌ Never Auto-Approve

1. **Destructive operations:**
   - `rm -rf`
   - `git push --force`
   - `git reset --hard`
   - `docker system prune`

2. **Network operations:**
   - Unrestricted `curl`/`wget`
   - Database connections to production
   - API calls with production keys

3. **Permission changes:**
   - `chmod 777`
   - `chown`
   - `sudo` anything

4. **Secret exposure:**
   - `env` (shows all env vars including API keys)
   - Reading `.env` files
   - Logging sensitive data

### ✅ Good Practices

1. **Use version control:**
   - Review all changes before committing
   - Keep `.claude/config.json` in git
   - Share config with your team

2. **Principle of least privilege:**
   - Start conservative
   - Add permissions as needed
   - Remove unused permissions

3. **Protect secrets:**
   - Never allow reading `.env`
   - Use `deniedPaths` for secret files
   - Don't log API keys

4. **Review regularly:**
   - Audit permissions quarterly
   - Remove obsolete commands
   - Update for new tools

5. **Test in isolation:**
   - Try new permissions in test projects first
   - Understand what each command does
   - Monitor Claude's actions

### Environment-Specific Configs

Consider different configs for different environments:

```bash
.claude/
├── config.json              # Base config (conservative)
├── config.dev.json          # Development (permissive)
└── config.production.json   # Production (restrictive)
```

---

## Example Configuration

### Complete `.claude/config.json` (Recommended)

```json
{
  "$schema": "https://claude.com/schemas/claude-config.json",
  "version": "1.0",

  "allowedBashCommands": [
    "uv",
    "pytest",
    "ruff",
    "mypy",
    "just:test",
    "just:lint",
    "just:check",
    "just:fix",
    "just:run",
    "just:validate",
    "just:clean",
    "python:scripts/setup_env.py",
    "git:status",
    "git:diff",
    "git:log",
    "git:add",
    "ls",
    "mkdir",
    "chmod:+x"
  ],

  "autoApproveTools": [
    "Read",
    "Glob",
    "Grep",
    "Edit"
  ],

  "filePermissions": {
    "allowedPaths": [
      "src/**/*",
      "tests/**/*",
      "scripts/**/*",
      "docs/**/*",
      "*.md",
      "*.py",
      "*.toml",
      "*.yaml",
      "*.yml",
      "justfile"
    ],
    "deniedPaths": [
      ".env",
      ".env.*",
      "secrets/**/*",
      "*.key",
      "*.pem",
      "credentials.json",
      ".aws/**/*",
      ".ssh/**/*"
    ],
    "readOnlyPaths": [
      "uv.lock",
      ".git/**/*"
    ]
  },

  "statusLine": {
    "enabled": true,
    "format": "GenAI Project | Python {{python_version}}"
  },

  "output": {
    "style": "concise",
    "showLineNumbers": true
  },

  "workingDirectory": ".",

  "notes": [
    "This configuration is optimized for Python GenAI projects",
    "It allows common development tools while protecting secrets",
    "Review and adjust based on your team's needs"
  ]
}
```

---

## Discussion Points

Before finalizing the configuration, consider:

### 1. Git Commit Permissions
**Question:** Should Claude be allowed to create git commits?
- ✅ **Pros:** Faster workflow, automatic commit messages
- ❌ **Cons:** Less control, might commit unwanted changes
- **Recommendation:** Allow `git:add`, require manual `git commit`

### 2. Just vs Direct Commands
**Question:** Allow full `just` access or only specific recipes?
- **Option A:** `"just"` - Allow all recipes (simpler)
- **Option B:** `"just:test", "just:lint", ...` - Explicit recipes (safer)
- **Recommendation:** Start with specific recipes, expand as needed

### 3. Python Execution
**Question:** How permissive should Python execution be?
- **Option A:** `"python"` - Allow any Python command
- **Option B:** `"python:scripts/*"` - Only scripts directory
- **Option C:** Ask each time
- **Recommendation:** Restrict to scripts directory

### 4. File Write Operations
**Question:** Should Edit/Write be auto-approved?
- ✅ **Pros:** Faster development, seamless experience
- ❌ **Cons:** Could overwrite files accidentally
- **Recommendation:** Auto-approve (you have git to review)

### 5. Web Access
**Question:** Should WebFetch/WebSearch be allowed?
- **Use case:** Fetching documentation, searching for solutions
- **Risk:** Sends data externally
- **Recommendation:** Allow for learning/docs, deny for sensitive projects

---

## Next Steps

1. **Review this document** - Understand each permission
2. **Choose a config level** - Conservative, Balanced, or Permissive
3. **Customize** - Add/remove based on your needs
4. **Create** - We'll create `.claude/config.json` with your choices
5. **Test** - Try it out and adjust as needed
6. **Iterate** - Permissions can always be updated

---

## Questions to Answer

Before we create the config file, please decide:

1. Which configuration level do you want? (Conservative/Balanced/Permissive)
2. Should Claude be able to create git commits? (Yes/No/Only git add)
3. Allow full `just` access or specific recipes only?
4. Allow Python execution? (All/Scripts only/Ask each time)
5. Auto-approve Edit and Write tools? (Yes/No)
6. Allow WebFetch for documentation? (Yes/No)
7. Any additional commands specific to your workflow?
8. Any additional files/directories to protect?

Once you answer these, we'll create the perfect `.claude/config.json` for your template!
