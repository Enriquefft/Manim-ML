# Manim-ML: Educational Video Creation Framework

A production-ready framework for creating stunning educational videos using Manim, focused on Machine Learning and mathematical demonstrations.

## Features

- 🎬 **Manim Integration**: Latest Manim version with full feature support
- 🔍 **Type Safety**: Python 3.13 with strict Pyright type checking
- 📏 **Code Quality**: Ruff linting with comprehensive rule coverage
- 🐚 **Reproducible Environment**: Nix flake for deterministic development setup
- 🎯 **Pre-commit Hooks**: Automated linting and type checking before commits
- 📚 **Educational Focus**: Templates and utilities for ML video creation

## Requirements

- **Nix** (for reproducible environment) or **Python 3.13+** with `uv` package manager
- **FFmpeg** (for video encoding)
- **TeX Live** (for LaTeX rendering in animations)
- **sox** (for audio processing)

## Quick Start

### Using Nix (Recommended)

```bash
# Clone the repository
git clone <your-repo-url>
cd Manim-ML

# Nix will automatically load the environment
direnv allow  # or manually load with: nix flake enter
```

The flake will automatically:
- Install Python 3.13
- Install `uv` package manager
- Install Manim (pre-packaged from nixpkgs - no compilation!)
- Set up the virtual environment

Then run:
```bash
uv sync
manim -ql videos/scenes/example_scene.py DynamicMathExample
```

### Manual Setup (Without Nix)

For non-Nix users, you'll need to install Manim and system dependencies first:

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install -y build-essential python3-dev ffmpeg texlive-full sox libpango-1.0-0 libpango-1.0-dev libcairo2
pip install manim
```

**macOS:**
```bash
brew install python ffmpeg texlive sox
pip install manim
```

**Windows:**
See [Manim Installation Guide](https://docs.manim.community/en/stable/installation.html)

Then set up the project:
```bash
# Ensure you have Python 3.13+ and uv installed
pip install uv

# Sync dependencies
uv sync

# Activate virtual environment
source .venv/bin/activate

# Test it works
manim -ql videos/scenes/example_scene.py DynamicMathExample
```

**Note:** Manim is an optional dependency (available as `manim` extra group). Nix users get it from the flake; non-Nix users must install it via their system package manager.

## Project Structure

```
Manim-ML/
├── videos/
│   ├── scenes/           # Manim scene files
│   │   └── example_scene.py
│   ├── templates/        # Reusable scene templates
│   └── assets/           # Media assets
│       ├── images/
│       └── data/
├── src/                  # Utility modules and helpers
├── tests/                # Test suite
├── docs/                 # Documentation
├── media/                # Generated video output (git-ignored)
├── manim.cfg            # Manim configuration
├── flake.nix            # Nix development environment
├── pyproject.toml       # Python project configuration
└── README.md
```

## Usage

### Running a Scene

```bash
# Render the example scene at low quality for preview
manim -ql videos/scenes/example_scene.py DynamicMathExample

# Render at high quality (full HD, 60fps)
manim -qh videos/scenes/example_scene.py DynamicMathExample

# Preview in real-time (requires display)
manim -p videos/scenes/example_scene.py DynamicMathExample
```

**Quality Options:**
- `-ql`: Low quality (480p, 15fps) - fastest
- `-qm`: Medium quality (720p, 30fps)
- `-qh`: High quality (1080p, 60fps)
- `-qk`: 4K quality (2160p, 60fps) - slowest

### Creating Your First Scene

Create a file in `videos/scenes/my_scene.py`:

```python
from __future__ import annotations

from manim import Scene, Circle

class MyScene(Scene):
    def construct(self) -> None:
        circle = Circle()
        self.play(FadeIn(circle))
        self.wait(1)
```

Run it:
```bash
manim -ql videos/scenes/my_scene.py MyScene
```

## Code Quality

### Type Checking

Run Pyright type checker in strict mode:

```bash
pyright
```

### Linting and Formatting

Check code with Ruff:

```bash
# Check for issues
ruff check .

# Automatically fix fixable issues
ruff check . --fix

# Format code
ruff format .
```

### Pre-commit Hooks

Install pre-commit hooks for automatic checks before commits:

```bash
# Install hooks
pre-commit install

# Run hooks on all files (useful for initial setup)
pre-commit run --all-files
```

After installation, hooks will run automatically on `git commit`.

## Configuration

### Manim Settings (`manim.cfg`)

Configure rendering defaults:

```ini
[CLI]
media_dir = ./media
quality = 1080p_60_fps
frame_rate = 60
```

### Ruff Settings (`pyproject.toml`)

- **Rule Selection**: All rules enabled (`select = ["ALL"]`)
- **Line Length**: 100 characters
- **Target Version**: Python 3.14

### Pyright Settings (`pyproject.toml`)

- **Type Checking Mode**: Strict
- **Python Version**: 3.14
- **Configuration**: Global type stub warnings (not inline suppressions)

## Example Scenes

### DynamicMathExample

Demonstrates:
- **ValueTracker**: Dynamic value tracking for animations
- **add_updater**: Real-time expression updates based on tracker values

Showcase a dynamic mathematical function `f(x) = x²` that updates as x changes from 1 to 3.

### ShapeMorphingExample

Demonstrates:
- **AnimationGroup**: Coordinated multiple animations
- **Shape Transformation**: Smooth transitions between shapes

Shows circles and squares moving and transforming with lag_ratio for staggered animations.

## Development Workflow

### 1. Create a New Scene

```bash
# Add a new file in videos/scenes/
touch videos/scenes/my_new_scene.py
```

### 2. Write Type-Safe Code

```python
from __future__ import annotations

from manim import Scene, Circle

class MyScene(Scene):
    def construct(self) -> None:
        """Construct the scene."""
        circle: Circle = Circle()
        self.add(circle)
```

### 3. Check Types and Format

```bash
pyright
ruff check . --fix
ruff format .
```

### 4. Render and Preview

```bash
manim -ql videos/scenes/my_new_scene.py MyScene
```

### 5. Commit with Pre-commit

```bash
git add videos/scenes/my_new_scene.py
git commit -m "Add new scene: MyScene"
# Pre-commit hooks run automatically
```

## Troubleshooting

### `ffmpeg` not found

**Linux:**
```bash
sudo apt-get install ffmpeg  # Debian/Ubuntu
sudo pacman -S ffmpeg         # Arch Linux
sudo yum install ffmpeg       # Red Hat/Fedora
```

**macOS:**
```bash
brew install ffmpeg
```

### LaTeX not found

**Linux:**
```bash
sudo apt-get install texlive-full  # Debian/Ubuntu
```

**macOS:**
```bash
brew install --cask mactex
```

### Out of Memory

For large scenes, use lower quality preview:
```bash
manim -ql videos/scenes/my_scene.py MyScene
```

### Type Checking Issues with Manim

If Pyright reports issues with Manim imports, they're configured as warnings globally (not suppressed). This is intentional as Manim's type stubs are incomplete.

## Dependencies

### Core
- **manim** >= 0.18.0 - Animation engine
- **numpy** >= 1.20 - Numerical computing
- **scipy** >= 1.7 - Scientific computing

### Optional (for ML examples)
- **pandas** >= 1.3 - Data manipulation
- **scikit-learn** >= 1.0 - Machine learning algorithms
- **matplotlib** >= 3.5 - Plotting utilities

### Development
- **pytest** >= 7.0 - Testing framework
- **pytest-cov** >= 4.0 - Coverage reporting
- **ruff** >= 0.1.0 - Fast Python linter and formatter
- **pyright** >= 1.1.300 - Static type checker

## Performance Tips

1. **Use `-ql` during development** - Renders 10x faster than high quality
2. **Enable previews** - Use `-p` flag to preview without saving
3. **Partial rendering** - Render specific scenes with `-s [start_frame]` to `-e [end_frame]`
4. **Cache LaTeX** - First render takes longer due to LaTeX compilation

## Contributing

1. Ensure all code passes type checking: `pyright`
2. Format with Ruff: `ruff format .`
3. Fix issues with Ruff: `ruff check . --fix`
4. Add tests for new features in `tests/`
5. Update documentation in `docs/`

## License

MIT License - See LICENSE file for details

## Resources

- [Manim Documentation](https://docs.manim.community/)
- [Manim Discord Community](https://discord.com/invite/mMRrZQW)
- [3Blue1Brown Manim Tutorials](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Pyright Documentation](https://github.com/microsoft/pyright)
