# Manim-ML Project Guidelines for Claude

## Project Overview
Manim-ML is a production-ready framework for creating educational videos using Manim, focused on Machine Learning demonstrations. The project prioritizes code quality, type safety, and reproducibility.

## Technology Stack
- **Language**: Python 3.14
- **Animation**: Manim (latest version)
- **Package Manager**: uv
- **Environment**: Nix flake (impure mode) with direnv
- **Linting**: Ruff with ALL rules enabled
- **Type Checking**: Pyright in strict mode
- **Pre-commit**: Automated checks before commits

## Code Quality Standards

### Type Safety (Pyright)
- **Mode**: Strict (`typeCheckingMode = "strict"`)
- **Python Version**: 3.14
- **Requirements**:
  - All functions must have return type annotations (`-> Type`)
  - All function parameters should have type hints
  - Use `from __future__ import annotations` at the top of modules
  - Variables should have explicit types where not obvious
  - Never use inline `# pyright: ignore` comments
  - Configure problematic third-party libraries globally in `[tool.pyright]`

### Linting & Formatting (Ruff)
- **Rule Selection**: `select = ["ALL"]` with minimal ignores
- **Ignores**:
  - `D100`, `D104`: Module/package docstrings (not always needed)
  - `ANN101`, `ANN102`: Type annotations for `self` and `cls` (implicit)
- **Line Length**: 100 characters
- **Quote Style**: Double quotes
- **Target Version**: Python 3.14

### Code Style
- Format all code with `ruff format .` before committing
- Run `ruff check . --fix` to auto-fix issues
- All imports must be sorted by Ruff
- Use comprehensive docstrings for all public classes/functions
- Follow PEP 8 with Ruff's stricter defaults

## File Organization

```
Manim-ML/
├── .claude/
│   └── CLAUDE.md              # This file - project guidelines
├── videos/
│   ├── scenes/                # Manim scene definitions
│   ├── templates/             # Reusable scene templates
│   └── assets/
│       ├── images/            # Image assets
│       └── data/              # Data files
├── src/                       # Utility modules and helpers
├── tests/                     # Test suite
├── docs/                      # Documentation
├── media/                     # Generated videos (git-ignored)
├── flake.nix                  # Nix environment definition
├── manim.cfg                  # Manim rendering configuration
├── pyproject.toml             # Python project metadata and tool config
└── README.md                  # Project documentation
```

## Workflow Guidelines

### Before Making Changes
1. Read existing code to understand patterns and conventions
2. Check `pyproject.toml` for current configurations
3. Verify type hints are in place for similar code
4. Understand Manim scene structure before extending

### Creating New Code
1. Use `from __future__ import annotations` at the top
2. Add comprehensive type hints to all functions
3. Include docstrings for all public APIs
4. Ensure Ruff compliance (use `ruff check --fix`)
5. Verify with Pyright before committing

### Manim-Specific Guidelines
- All scenes should extend `Scene` class
- Use `construct() -> None` method for scene definition
- Add type hints to all mobject creation and manipulation
- Use descriptive variable names (e.g., `circle_shape` not `c`)
- Group related animations in `AnimationGroup` when appropriate
- Always include docstrings explaining what the scene demonstrates

### Testing
- Place test files in `tests/` directory
- Use pytest for testing (configured in `pyproject.toml`)
- Aim for type-safe test code as well
- Run tests with: `pytest` or `pytest -v`

## Environment Management

### Using Nix (Recommended)
```bash
direnv allow  # Auto-loads environment
# Or manually: nix flake enter
```

When updating `flake.nix`:
```bash
direnv reload
```

### Without Nix
```bash
uv sync           # Install dependencies
source .venv/bin/activate
```

## Common Commands

```bash
# Type checking
pyright

# Linting and formatting
ruff check . --fix
ruff format .

# Running Manim scenes
manim -ql videos/scenes/example_scene.py DynamicMathExample

# Testing
pytest

# Pre-commit hooks
pre-commit install
pre-commit run --all-files
```

## Important Conventions

1. **Single Source of Truth**: Always maintain a single authoritative definition
2. **No Inline Suppressions**: Use global configurations instead of comment-based ignores
3. **Explicit Types**: Prefer explicit type annotations over inference
4. **Comprehensive Docstrings**: Document public APIs thoroughly
5. **Clean Code**: Remove unused imports, variables, and code
6. **DRY Principle**: Extract common patterns into templates or utilities

## When Working on Specific Areas

### Modifying flake.nix
- Run `direnv reload` after changes
- Test in a fresh shell session
- Ensure all dependencies are pinned or tracked in flake.lock

### Adding Dependencies
- Add to `pyproject.toml` dependencies array
- Run `uv sync` to update lock file
- Update `flake.nix` if the dependency needs system-level packages

### Creating New Scenes
- Create file in `videos/scenes/`
- Follow DynamicMathExample or ShapeMorphingExample as templates
- Use latest Manim API features
- Include type hints and docstrings
- Test with low quality first: `manim -ql ...`

### Updating Configuration
- Changes to tool configs in `pyproject.toml` take effect immediately
- Changes to `manim.cfg` affect all future renders
- Pre-commit config requires `pre-commit install` again if modified

## CI/CD and Pre-commit

The project uses pre-commit hooks to enforce:
- Ruff formatting and linting
- Pyright type checking
- File cleanup (trailing whitespace, EOF formatting)
- Large file detection (>5MB)

Install with: `pre-commit install`

## Documentation

- Keep `README.md` synchronized with actual project structure
- Add docstrings following Google-style or Sphinx-style conventions
- Document complex scenes with comments in the code
- Include examples for public utilities

## General Principles

1. **Reproducibility First**: Use Nix flake to ensure everyone has identical environment
2. **Type Safety**: Leverage strict Pyright to catch errors early
3. **Code Clarity**: Ruff rules enforce readable, consistent code
4. **Educational Value**: Scenes should demonstrate Manim features effectively
5. **Maintainability**: Clear code structure makes the project scalable

## Questions or Updates?

Refer to:
- `.claude/CLAUDE.md` - This file
- `README.md` - User documentation
- `pyproject.toml` - Tool configurations
- Scene examples in `videos/scenes/` - Implementation patterns
