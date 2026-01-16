<!--
SYNC IMPACT REPORT
==================
Version Change: 0.0.0 → 1.0.0 (MAJOR - initial constitution establishment)
Principles Added: 5 core principles established for Manim-ML project
New Sections: Technology Stack Requirements, Development Quality Standards, Governance
Templates Updated: All templates reviewed for alignment ✅
Files Flagged for Review: None - first constitution establishment

Constitution ratified on 2026-01-09 for Manim-ML production video framework.
-->

# Manim-ML Constitution

## Core Principles

### I. Reproducibility First
Every environment must be reproducible. Nix flakes define all dependencies with exact versions,
ensuring consistent builds across all developers and CI/CD systems. No "works on my machine"
failures are acceptable. direnv automatically loads the environment; manual setup is optional.
Environment changes require `direnv reload` to take effect.

### II. Type Safety (Strict)
All Python code must pass Pyright in strict mode. Every function requires return type annotations
and parameter type hints. No `# pyright: ignore` inline suppressions are permitted; problematic
third-party libraries must be configured globally in `[tool.pyright]`. Type inference is never
a substitute for explicit annotations. Code that cannot be typed is not acceptable.

### III. Code Clarity (Ruff ALL Rules)
Ruff linting with ALL rules enabled enforces consistent, readable code. Code must pass
`ruff check . --fix` before commit. Line length is capped at 100 characters. Double quotes are
mandatory. All imports must be sorted. Docstrings are required for all public classes and functions.
Unused code is removed immediately—no dead code, dead imports, or commented-out sections.

### IV. Educational Value Through Clarity
Manim scenes exist to demonstrate concepts. Each scene must have a clear purpose, descriptive
variable names (e.g., `circle_shape` not `c`), and docstrings explaining what the scene demonstrates.
Complex animations must be grouped into `AnimationGroup`s with clear intent. Every public API must be
thoroughly documented for future maintainers and learners.

### V. Single Source of Truth
One authoritative definition for every piece of information. Configuration changes in `pyproject.toml`
take effect immediately; changes to `manim.cfg` affect all future renders; changes to `flake.nix`
require `direnv reload`. No duplicated configuration. No contradictory definitions across files.
Documentation in `.claude/CLAUDE.md`, `README.md`, and this constitution must stay synchronized.

## Technology Stack Requirements

- **Language**: Python 3.14 (strict type checking mode)
- **Animation Framework**: Manim (latest stable version)
- **Package Manager**: uv (for Python dependency management)
- **Environment**: Nix flake with direnv (impure mode for system dependencies)
- **Type Checker**: Pyright (strict mode, no inline suppressions)
- **Linter/Formatter**: Ruff with ALL rules enabled
- **Testing**: pytest (with type-safe test code)
- **Pre-commit Hooks**: Mandatory before commits (ruff, pyright, trailing whitespace, large files)

All dependencies must be pinned or tracked in flake.lock and uv.lock. No floating versions.
No optional typing via gradual adoption—strict mode is non-negotiable.

## Development Quality Standards

### File Organization
```
Manim-ML/
├── .claude/          # Project guidelines and runtime documentation
├── videos/           # Scene definitions and reusable templates
│   ├── scenes/       # Manim scene implementations
│   ├── templates/    # Reusable scene patterns and base classes
│   └── assets/       # Images, data files, external resources
├── src/              # Utility modules and helper functions
├── tests/            # Pytest test suite (type-safe)
├── docs/             # Project documentation
├── media/            # Generated videos (git-ignored)
├── flake.nix         # Nix environment definition
├── manim.cfg         # Manim rendering configuration
└── pyproject.toml    # Python project metadata and tool configuration
```

### Code Review Checklist (Pre-commit Validation)
1. **Type Safety**: `pyright` passes in strict mode (no errors, no inline ignores)
2. **Linting/Formatting**: `ruff check . --fix` produces no violations
3. **Imports**: All imports sorted, no unused imports
4. **Docstrings**: All public functions, classes, and methods documented
5. **Testing**: New code includes tests in `tests/`; tests are type-safe
6. **Manim Scenes**: Extend `Scene` class, use `construct() -> None`, include docstrings
7. **No Dead Code**: Remove unused variables, functions, and commented-out blocks

### Manim-Specific Requirements
- All scenes inherit from `Scene` class
- Scene entry point: `construct(self) -> None` method
- Type hints required on all mobject creation and manipulation
- Complex animations grouped into `AnimationGroup` for clarity
- Docstring format: Google-style or Sphinx-style, explaining what the scene teaches
- Testing approach: Pytest in `tests/` directory; use type-safe assertions
- Asset references: Relative paths from project root, documented in scene docstring

## Governance

**Constitutional Authority**: This constitution supersedes all other project documentation,
tool configurations, and informal conventions. When conflicts arise, constitution principles
take precedence.

**Amendment Process**: Amendments require explicit documentation of rationale, impact on
existing code/processes, and migration plan for any breaking changes. Version bumping follows
semantic versioning:
- **MAJOR**: Backward-incompatible changes (principle removal, redefinition, or new mandatory requirement)
- **MINOR**: New principle added, guidance materially expanded, or non-breaking new requirements introduced
- **PATCH**: Clarifications, wording refinements, typo fixes, or examples added

**Compliance Review**: All PRs and reviews must verify constitution compliance. Deviations require
explicit justification documented in the commit message or PR description. Ongoing audits via
pre-commit hooks enforce type safety, code formatting, and test coverage.

**Runtime Guidance**: Development decisions should consult `.claude/CLAUDE.md` for patterns,
best practices, and tool configurations. This constitution defines the rules; CLAUDE.md provides
context and how-to guidance.

**Single Source of Truth Maintenance**: Changes to this constitution MUST trigger review of
`.claude/CLAUDE.md`, `README.md`, and all `.specify/templates/*` files to ensure consistency.
Outdated guidance must be updated or removed immediately.

---

**Version**: 1.0.0 | **Ratified**: 2026-01-09 | **Last Amended**: 2026-01-09
