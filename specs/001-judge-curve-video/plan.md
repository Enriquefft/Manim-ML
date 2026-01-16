# Implementation Plan: The Judge & The Curve Video

**Branch**: `001-judge-curve-video` | **Date**: 2026-01-10 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-judge-curve-video/spec.md`

## Summary

Create a 2-minute educational video titled "The Judge & The Curve" using Manim that explains regression concepts (linear vs. non-linear) through visual storytelling. The video consists of 5 sections: AI hallucination metaphor, continuous scale introduction, linear regression demonstration, non-linear regression evolution, and neural network synthesis. All code must comply with the project's strict type safety, linting, and reproducibility requirements.

## Technical Context

**Language/Version**: Python 3.14 (strict type checking mode per constitution)
**Primary Dependencies**: Manim (latest stable), NumPy (data generation)
**Storage**: N/A (video file output only)
**Testing**: pytest (scene rendering validation, reproducibility checks)
**Target Platform**: Linux (Nix flake environment), output: MP4 1920x1080@60fps
**Project Type**: Single project (Manim video generation)
**Performance Goals**: 60 FPS playback, 1000+ nodes in neural network scene
**Constraints**: Exact 120-second duration, reproducible data points (seeded RNG)
**Scale/Scope**: 5 scenes, ~13 source files, 1 complete video output

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Requirement | Status | Notes |
|-----------|-------------|--------|-------|
| I. Reproducibility First | Nix flake, seeded RNG, pinned deps | ✅ PASS | FR-004 requires reproducible data points; Nix environment already configured |
| II. Type Safety (Strict) | Pyright strict, no inline ignores | ✅ PASS | All scene classes, utilities, and animations must have full type annotations |
| III. Code Clarity (Ruff ALL) | Ruff check, 100-char lines, docstrings | ✅ PASS | All public classes/functions require docstrings explaining educational purpose |
| IV. Educational Value | Clear purpose, descriptive names, AnimationGroup | ✅ PASS | Scenes explicitly designed for education; FR-011 requires legible text |
| V. Single Source of Truth | No duplicate config, centralized constants | ✅ PASS | Color palette in single config file; timing constants centralized |

**Gate Result**: ✅ ALL PRINCIPLES SATISFIED - Proceed to Phase 0

## Project Structure

### Documentation (this feature)

```text
specs/001-judge-curve-video/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output (scene interfaces)
└── tasks.md             # Phase 2 output (/speckit.tasks command)
```

### Source Code (repository root)

```text
src/
├── config.py                    # Color palette, timing constants, frame rate
└── utils/
    ├── __init__.py
    ├── color_utils.py           # Color palette functions and constants
    └── data_generator.py        # Seeded data generation for regression scenes

videos/
├── scenes/
│   ├── __init__.py
│   ├── section1_hallucination.py    # HallucinationScene
│   ├── section2_scale.py            # ContinuousScaleScene
│   ├── section3_linear.py           # LinearRegressionScene
│   ├── section4_nonlinear.py        # NonLinearRegressionScene
│   ├── section5_synthesis.py        # SynthesisScene
│   └── judge_curve_complete.py      # Full video composition
├── templates/
│   ├── __init__.py
│   ├── effects.py               # Chromatic aberration, glows, pulses
│   ├── animations.py            # Custom animation classes (jitter, morph)
│   └── custom_shapes.py         # Slider, warning icon, node shapes
├── assets/
│   ├── images/                  # Placeholder images (if any)
│   └── data/
│       ├── linear_data.csv      # Pre-computed linear regression data
│       └── nonlinear_data.csv   # Pre-computed S-curve data
└── judge_curve_main.py          # Entry point script

tests/
├── __init__.py
├── test_scenes.py               # Scene rendering validation
├── test_data_generator.py       # Reproducibility checks
└── test_effects.py              # Effect function tests
```

**Structure Decision**: Single project structure following Manim-ML constitution file organization. Source utilities in `src/`, scene implementations in `videos/scenes/`, reusable components in `videos/templates/`, tests in `tests/`.

## Complexity Tracking

> No violations detected. All requirements align with constitution principles.

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| (none) | - | - |
