# Manim-ML

Educational video creation framework using Manim for machine learning demonstrations with integrated voiceover support.

## Features

- High-quality mathematical animations using Manim
- Integrated voiceover narration with manim-voiceover
- Type-safe Python code with strict Pyright checking
- Reproducible development environment with Nix flake
- Production-ready code quality standards

## Prerequisites

- Nix with flakes enabled (recommended)
- Or Python 3.13+ with uv package manager

## Installation

### Using Nix (Recommended)

```bash
# Clone the repository
git clone <repository-url>
cd Manim-ML

# Allow direnv to load the environment
direnv allow

# Dependencies will be automatically installed
```

### Without Nix

```bash
# Clone the repository
git clone <repository-url>
cd Manim-ML

# Install dependencies
uv sync

# Activate the virtual environment
source .venv/bin/activate
```

## Voiceover Support

This project integrates [manim-voiceover](https://voiceover.manim.community/) for synchronized narration in animations.

### Supported TTS Services

- **gTTS** (Google Text-to-Speech) - Free, no API key required
- **Azure Cognitive Services** - High-quality, requires API key
- **OpenAI TTS** - Natural voices, requires API key
- **ElevenLabs** - Premium quality, requires API key
- **pyttsx3** - Offline TTS, no API key required
- **RecorderService** - Record your own voice

### Configuration

1. Copy the environment file:
   ```bash
   cp .env.example .env
   ```

2. Add your API keys to `.env` (optional, only for premium services):
   ```bash
   # For Azure
   AZURE_SUBSCRIPTION_KEY=your_key_here
   AZURE_SERVICE_REGION=your_region_here

   # For OpenAI
   OPENAI_API_KEY=your_key_here
   ```

3. Configure settings in `manim.cfg` (already set up with defaults)

### Usage Example

```python
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class MyScene(VoiceoverScene):
    def construct(self):
        # Initialize TTS service
        self.set_speech_service(GTTSService())

        # Create animation with synchronized voiceover
        circle = Circle()
        with self.voiceover(text="Watch this circle appear!") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
```

### Rendering with Voiceover

**IMPORTANT**: Always use the `--disable_caching` flag when rendering scenes with voiceovers:

```bash
# Low quality for testing
manim -ql videos/scenes/voiceover_example.py VoiceoverDemo --disable_caching

# Production quality
manim -qh videos/scenes/voiceover_example.py VoiceoverDemo --disable_caching
```

## Project Structure

```
Manim-ML/
├── videos/
│   ├── scenes/              # Manim scene definitions
│   │   ├── voiceover_example.py  # Voiceover examples
│   │   └── ...
│   ├── templates/           # Reusable scene templates
│   └── assets/              # Images and data files
├── src/                     # Utility modules
├── tests/                   # Test suite
├── media/                   # Generated videos (git-ignored)
├── flake.nix               # Nix environment
├── manim.cfg               # Manim configuration
├── pyproject.toml          # Project metadata
└── README.md               # This file
```

## Development

### Code Quality

The project enforces strict code quality standards:

- **Type Checking**: Pyright in strict mode
- **Linting**: Ruff with ALL rules enabled
- **Formatting**: Ruff formatter (double quotes, 100 char line length)
- **Pre-commit Hooks**: Automated checks before commits

### Running Checks

```bash
# Type checking
pyright

# Linting and formatting
ruff check . --fix
ruff format .

# Run tests
pytest
```

### Creating New Scenes

1. Create a new file in `videos/scenes/`
2. Import from `manim` and optionally `manim_voiceover`
3. Use type hints and docstrings
4. Test with low quality first: `manim -ql <file> <SceneName> --disable_caching`

Example:
```python
"""My awesome scene."""

from __future__ import annotations

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


class MyAwesomeScene(VoiceoverScene):
    """Demonstrates something amazing."""

    def construct(self) -> None:
        """Create the scene."""
        self.set_speech_service(GTTSService())
        # Your animation code here
```

## Available Examples

Run these examples to see manim-voiceover in action:

```bash
# Basic voiceover demonstration
manim -ql videos/scenes/voiceover_example.py VoiceoverDemo --disable_caching

# ML concept with voiceover
manim -ql videos/scenes/voiceover_example.py MLConceptWithVoiceover --disable_caching
```

## Documentation

- [Manim Documentation](https://docs.manim.community/)
- [Manim Voiceover Documentation](https://voiceover.manim.community/)
- [Project Guidelines](.claude/CLAUDE.md)

## Troubleshooting

### Voiceover Issues

1. **Missing audio in output**: Ensure `--disable_caching` flag is used
2. **TTS service errors**: Check API keys in `.env` file
3. **Audio quality issues**: Try a different TTS service or adjust settings

### Build Issues

1. **PyAV build errors**: Ensure you're using Python 3.13 (not 3.14)
2. **Missing dependencies**: Run `uv sync` or `direnv reload`
3. **Type errors**: Check with `pyright` and fix type annotations

## License

MIT

## Contributing

1. Follow the code quality standards (see `.claude/CLAUDE.md`)
2. Add type hints to all functions
3. Include docstrings for public APIs
4. Test with `ruff check` and `pyright` before committing
5. Use `--disable_caching` when testing voiceover scenes
