# Quickstart: The Judge & The Curve Video

**Feature**: 001-judge-curve-video
**Date**: 2026-01-10

## Prerequisites

1. **Nix environment**: Ensure direnv is enabled
   ```bash
   direnv allow
   ```

2. **Dependencies synced**: Verify uv has installed packages
   ```bash
   uv sync
   ```

3. **Manim working**: Test basic render
   ```bash
   manim -ql -p videos/scenes/section1_hallucination.py HallucinationScene
   ```

## Quick Commands

### Render Individual Scenes (Low Quality - Fast)

```bash
# Section 1: Hallucination
manim -ql videos/scenes/section1_hallucination.py HallucinationScene

# Section 2: Continuous Scale
manim -ql videos/scenes/section2_scale.py ContinuousScaleScene

# Section 3: Linear Regression
manim -ql videos/scenes/section3_linear.py LinearRegressionScene

# Section 4: Non-Linear Regression
manim -ql videos/scenes/section4_nonlinear.py NonLinearRegressionScene

# Section 5: Synthesis
manim -ql videos/scenes/section5_synthesis.py SynthesisScene
```

### Render Full Video (High Quality)

```bash
# Full video composition
manim -qh videos/scenes/judge_curve_complete.py JudgeCurveComplete

# Or use the entry point
python videos/judge_curve_main.py
```

### Quality Flags

| Flag | Resolution | FPS | Use Case |
|------|------------|-----|----------|
| `-ql` | 480p | 15 | Quick preview |
| `-qm` | 720p | 30 | Development testing |
| `-qh` | 1080p | 60 | Final render (required) |
| `-qk` | 4K | 60 | Future-proofing |

## Development Workflow

### 1. Generate Data Files

Before first render, generate the reproducible data:

```bash
python -c "
from src.utils.data_generator import generate_linear_data, generate_scurve_data, save_data_to_csv

linear = generate_linear_data()
save_data_to_csv(linear, 'videos/assets/data/linear_data.csv')

scurve = generate_scurve_data()
save_data_to_csv(scurve, 'videos/assets/data/nonlinear_data.csv')
"
```

### 2. Test Individual Scenes

Each scene can be developed and tested in isolation:

```bash
# Render with preview (opens video player)
manim -ql -p videos/scenes/section3_linear.py LinearRegressionScene
```

### 3. Run Type Checker

```bash
pyright
```

### 4. Run Linter

```bash
ruff check . --fix
ruff format .
```

### 5. Run Tests

```bash
pytest tests/ -v
```

### 6. Full Validation (Pre-commit)

```bash
pre-commit run --all-files
```

## File Locations

| Purpose | Path |
|---------|------|
| Configuration | `src/config.py` |
| Color utilities | `src/utils/color_utils.py` |
| Data generation | `src/utils/data_generator.py` |
| Scene implementations | `videos/scenes/*.py` |
| Reusable effects | `videos/templates/effects.py` |
| Custom animations | `videos/templates/animations.py` |
| Shape primitives | `videos/templates/custom_shapes.py` |
| Data files | `videos/assets/data/*.csv` |
| Output videos | `media/videos/` (git-ignored) |

## Troubleshooting

### "Font not found" Error

Manim uses system fonts. Ensure these are available:
- Monospace: Courier, RobotoMono, or any monospace font
- Serif: Times, Georgia, or any serif font
- Handwritten: Comic Sans or similar (Section 2 only)

### Render Takes Too Long

- Use `-ql` for development
- Reduce node count in SynthesisScene temporarily
- Check for infinite loops in custom animations

### Type Errors

All code must pass Pyright strict mode. Common fixes:
- Add return type annotations to all functions
- Use explicit type hints for variables with non-obvious types
- Avoid `Any` type where possible

### Colors Look Wrong

Verify you're using the centralized color palette from `src/config.py`. Do not hardcode hex values in scene files.

## Success Criteria Checklist

Before considering a scene complete:

- [ ] Renders without errors (`manim -qh`)
- [ ] Timing matches spec (use `self.wait()` precisely)
- [ ] Colors from palette only (no hardcoded hex)
- [ ] Pyright passes (no errors)
- [ ] Ruff passes (no violations)
- [ ] Docstrings present on all public methods
- [ ] Type hints on all functions
