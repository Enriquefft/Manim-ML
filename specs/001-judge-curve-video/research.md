# Research: The Judge & The Curve Video

**Feature**: 001-judge-curve-video
**Date**: 2026-01-10
**Status**: Complete

## Research Areas

### 1. Manim Scene Composition & Timing

**Decision**: Use Manim's `Scene` class with `self.wait()` for precise timing control; compose full video by sequencing individual scene renders.

**Rationale**: Manim's built-in timing mechanisms (`self.play()` with `run_time` parameter, `self.wait()`) provide frame-accurate control. Each section can be developed and tested independently, then combined using Manim's scene sequencing or post-render concatenation.

**Alternatives Considered**:
- Single monolithic scene: Rejected due to complexity and difficulty testing individual sections
- External video editor composition: Rejected to maintain reproducibility within codebase

### 2. Custom Animation Effects

**Decision**: Implement custom effect functions in `videos/templates/effects.py` using Manim's `Mobject.set_color()`, `Mobject.set_opacity()`, and shader-based approaches where available.

**Rationale**:
- **Chromatic aberration**: Overlay RGB-shifted copies of the target mobject with offset positions
- **Glow effects**: Use `SurroundingRectangle` or duplicate mobjects with increased scale and reduced opacity
- **Pulsing**: Animate opacity/scale with sinusoidal rate functions
- **Dolly zoom**: Animate camera focal length while simultaneously translating position

**Alternatives Considered**:
- Post-processing in video editor: Rejected for reproducibility
- External shader libraries: Rejected to maintain dependency simplicity

### 3. Data Point Generation & Reproducibility

**Decision**: Use `numpy.random.default_rng(seed=42)` for all random data generation; pre-generate and cache data in CSV files.

**Rationale**: NumPy's modern RNG API with explicit seeding guarantees reproducibility. Pre-generating to CSV ensures identical data across renders without runtime computation, satisfying FR-004.

**Alternatives Considered**:
- Runtime generation only: Rejected due to potential seed handling complexity
- Hardcoded coordinates: Rejected for flexibility in adjusting noise parameters

### 4. Neural Network Visualization (1000+ nodes)

**Decision**: Use Manim's `VGroup` with procedurally generated `Dot` and `Line` mobjects; implement spatial partitioning for connection culling to manage complexity.

**Rationale**:
- Generate nodes in layered structure (input → hidden → output pattern)
- Connect nodes within adjacent layers only (reduces O(n²) to O(n))
- Use low opacity for connections to prevent visual clutter
- Animate data pulses as `MoveAlongPath` with staggered start times

**Alternatives Considered**:
- Pre-rendered image overlay: Rejected to maintain animation capability
- Reduced node count: Rejected as FR-010 requires 1000+ nodes

### 5. Warning Icon Generation (Vector/Code-based)

**Decision**: Create warning icon using Manim primitives (`Polygon` for triangle, `Line` for exclamation mark) in `videos/templates/custom_shapes.py`.

**Rationale**: Per clarification session, icons must be generated programmatically. Manim's `Polygon` and `Line` classes provide sufficient primitives. Apply glow effect using the standard approach from Research #2.

**Alternatives Considered**:
- SVG import: Rejected to avoid external file dependencies
- External image generation: Explicitly rejected in clarification

### 6. Text Jitter Animation

**Decision**: Implement as custom `Animation` subclass that randomly replaces characters with similar glyphs on each frame.

**Rationale**: Create a mapping of characters to "corrupted" alternatives (e.g., 'A' → '@', 'O' → '0'). The animation interpolates between showing original and corrupted characters based on rate function.

**Alternatives Considered**:
- Pre-rendered text frames: Rejected for flexibility
- Shader-based distortion: Rejected for complexity

### 7. Slider UI Component

**Decision**: Implement as composite `VGroup` containing `Rectangle` (track), `Circle` (handle), `Text` (labels), and gradient fill via `LinearGradient`.

**Rationale**: Manim's gradient support allows smooth color transitions from cyan to red. The handle can be animated along the track using `MoveToTarget()` or `animate.move_to()`.

**Alternatives Considered**:
- Image-based slider: Rejected for animation flexibility

### 8. Error Bar Visualization

**Decision**: Implement as `DashedLine` or `Line` objects connecting each data point to the corresponding point on the regression line, colored red.

**Rationale**: Calculate residual for each point as `y_actual - y_predicted`, draw vertical line of that length. Update in real-time during line rotation animation using `become()` or `UpdateFromFunc()`.

**Alternatives Considered**:
- Static lines only: Rejected as FR-009 requires dynamic visualization during optimization

### 9. Equation Display with Animated Values

**Decision**: Use Manim's `MathTex` with `DecimalNumber` for variable values that can be animated.

**Rationale**: `DecimalNumber` provides smooth interpolation between values. Embed within `VGroup` alongside static `MathTex` for the equation structure (y = mx + b).

**Alternatives Considered**:
- Regenerating `MathTex` each frame: Rejected for performance
- Text-only (non-LaTeX): Rejected for visual quality

### 10. Scene Transition Strategy

**Decision**: Use `FadeOut`/`FadeIn` transitions between sections with 0.3-second overlap.

**Rationale**: Simple, clean transitions that maintain professional appearance without distracting from educational content. Each section handles its own setup and teardown.

**Alternatives Considered**:
- Hard cuts: Rejected as too jarring
- Complex transitions (wipes, morphs): Rejected as potentially distracting

## Technology Decisions Summary

| Component | Technology | Reason |
|-----------|------------|--------|
| Animation Framework | Manim Community Edition | Project standard, Python native |
| Data Generation | NumPy with seeded RNG | Reproducibility requirement |
| Type Checking | Pyright strict mode | Constitution requirement |
| Linting | Ruff (ALL rules) | Constitution requirement |
| Testing | pytest | Scene validation, reproducibility checks |
| Vector Graphics | Manim primitives | Programmatic icon generation requirement |

## Open Questions Resolved

All technical questions resolved. No NEEDS CLARIFICATION items remain.
