# Claude Code Configuration

This directory contains the configuration for Claude Code in this project.

## Files

- **config.json** - Main configuration file with permissions and settings
- **commands/** (optional) - Custom slash commands for this project

## What's Configured

This template uses a **balanced configuration** optimized for Python GenAI development:

### ✅ Auto-Approved Bash Commands

**Package Management:**
- `uv` - All UV package manager operations

**Testing & Quality:**
- `pytest` - All test operations
- `ruff` - Linting and formatting
- `mypy` - Type checking

**Just Recipes (Specific only):**
- `just:test`, `just:lint`, `just:check`
- `just:fix`, `just:run`, `just:validate`
- `just:clean`

**Git (Read + Staging only):**
- `git:status`, `git:diff`, `git:log`
- `git:add` (staging only, NOT commit/push)

**Python (Scripts only):**
- `python:scripts/*` - Only files in scripts/ directory

**File Operations:**
- `ls`, `mkdir`, `chmod:+x`

### ✅ Auto-Approved Tools

- **Read** - Read any file (respects file permissions)
- **Glob** - Pattern-based file search
- **Grep** - Content search
- **Edit** - Edit existing files (changes are reviewable in git)

### 🔒 Protected Files

These files are **denied access** for safety:
- `.env` and `.env.*` - Environment variables with secrets
- `secrets/**/*` - Any secrets directory
- `*.key`, `*.pem` - Private keys and certificates
- `credentials.json` - Credentials files
- `.aws/**/*`, `.ssh/**/*` - Cloud and SSH credentials

### 📖 Read-Only Files

- `uv.lock` - Managed by UV, shouldn't be manually edited
- `.git/**/*` - Git internals

## Customizing This Configuration

### Adding New Commands

Edit `config.json` and add to `allowedBashCommands`:

```json
{
  "allowedBashCommands": [
    "your-command",
    "another-command:specific-arg"
  ]
}
```

### Protecting Additional Files

Add to `deniedPaths`:

```json
{
  "filePermissions": {
    "deniedPaths": [
      "my-secret-file.txt",
      "private/**/*"
    ]
  }
}
```

### Different Environment Configurations

You can create multiple configs:

```bash
.claude/
├── config.json              # Default (balanced)
├── config.dev.json          # Development (permissive)
└── config.production.json   # Production (restrictive)
```

Then switch between them as needed.

## Configuration Levels

This template uses **Balanced** configuration. Other options:

### Conservative (Safest)
- Only specific commands approved
- No Edit/Write auto-approval
- Good for: Learning, sensitive projects

### Balanced (Current) ⭐
- Common dev tools approved
- Edit tool auto-approved
- Good for: Active development, most projects

### Permissive
- Broad command approval
- All tools auto-approved
- Good for: Rapid prototyping, solo projects

See `CLAUDE_PERMISSIONS.md` in the root directory for detailed documentation on all available permissions and security best practices.

## Quick Reference

**View current config:**
```bash
cat .claude/config.json
```

**Validate JSON:**
```bash
python -m json.tool .claude/config.json
```

**Check what commands are allowed:**
```bash
grep -A 20 "allowedBashCommands" .claude/config.json
```

## Security Notes

⚠️ **Never commit:**
- Actual `.env` files (use `.env.example` instead)
- API keys or credentials
- Private keys

✅ **Safe to commit:**
- This `config.json` file
- `commands/` directory with custom slash commands
- Configuration is project-specific, not sensitive

## Custom Slash Commands

You can add custom slash commands in `.claude/commands/`:

```bash
.claude/commands/
├── test-all.md       # Custom test command
└── deploy.md         # Deployment workflow
```

Each `.md` file becomes a `/command-name` in Claude Code.

## Getting Help

- **Full permission guide:** See `CLAUDE_PERMISSIONS.md` in the root
- **Claude Code docs:** https://docs.claude.com/claude-code
- **Issues:** Report at https://github.com/anthropics/claude-code/issues

## Version

Configuration version: 1.0
Last updated: 2026-01-09
