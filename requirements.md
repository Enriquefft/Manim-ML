# Manim Video Implementation Requirements

## Project: "The Judge & The Curve"
**Duration:** 2:00 minutes
**Total Scenes:** 5 major sections
**Visual Style:** Dark mode (Background: `#0D0D0D`, Text: `#F2F2F2`), Cyan accents (`#00F0FF`), Danger red (`#FF2A2A`)
**Target:** Educational video explaining Regression (Linear vs. Non-Linear) via Error Minimization and Reward Models

---

## Implementation Checklist

### ✅ Section 1: The Hallucination (0:00 – 0:25)
**Scene Class:** `HallucinationScene`
**Difficulty:** Medium

#### 1.1: Terminal Cursor & Void (0:00 – 0:04)
- [ ] Create black void background (`#0D0D0D`)
- [ ] Render blinking block cursor (green `#00FF00`, 1.5x scale)
- [ ] Apply chromatic aberration effect (RGB split) to cursor edges
- [ ] Cursor blink frequency: 0.5 seconds

#### 1.2: Text Cascade with Jitter (0:05 – 0:09)
- [ ] Generate monospace text (Courier/RobotoMono) line by line
- [ ] Text content: "The moon is made of blue algorithm potato... / syntax_error: truth_value_null... / happiness = 42 / 0..."
- [ ] Cascade timing: 120ms intervals between lines
- [ ] Implement letter jitter animation: random glyph flickering ('A' → '@' → 'A') at ~50ms intervals
- [ ] Text color: `#F2F2F2` (light grey)

#### 1.3: Warning Overlay (0:10 – 0:14)
- [ ] Draw hollow red box (`#FF2A2A`) around cascaded text
- [ ] Box animation: slam/bounce-in effect (0.3 second duration)
- [ ] Add pulsing glow effect to red box edges
- [ ] TODO: Generate an image with this prompt: "A minimalist warning icon (triangle with exclamation mark) in bright red (#FF2A2A) with glowing edges, 256x256px, transparent background, vector style, suitable for dark UI overlay" and place it at `/videos/assets/images/warning_icon.png`
- [ ] Add text "NO METRIC FOUND" (white, bold, monospace)
- [ ] Cast red ambient light onto surrounding text (subtle glow)

#### 1.4: Static Dissolution (0:15 – 0:25)
- [ ] Transition text to white noise/static effect
- [ ] Static should form vague shapes that fail to coalesce (use fractal Perlin noise)
- [ ] Implement Hitchcock dolly zoom: camera dolly in while zooming out (optical illusion)
- [ ] Final frame: screen entirely filled with grey noise (`#808080` ± variance)
- [ ] Duration: 1.0 second zoom

---

### ✅ Section 2: The Continuous Scale (0:25 – 0:50)
**Scene Class:** `ContinuousScaleScene`
**Difficulty:** Medium-Hard

#### 2.1: Split Screen Setup (0:25 – 0:29)
- [ ] Create vertical split via thin white line (1px width, centered)
- [ ] Left pane: render "Paris is France" (serif font, elegant, `#F2F2F2`)
- [ ] Right pane: render "Paris is a cheese" (Comic Sans or handwritten style, messy, `#F2F2F2`)
- [ ] Both texts centered in their respective panes
- [ ] Background: `#0D0D0D`

#### 2.2: Gradient Slider UI (0:30 – 0:34)
- [ ] Create vertical slider on center line (height: 40% of screen, width: 0.3 units)
- [ ] Slider color: gradient from cyan (`#00F0FF`) at top to red (`#FF2A2A`) at bottom
- [ ] Add vertical gradient bar beneath slider (visual mixing console style)
- [ ] Top label: "+1.0 (True/High Value)" (`#F2F2F2`, small font)
- [ ] Bottom label: "-1.0 (False/Harmful)" (`#F2F2F2`, small font)
- [ ] Slider handle: glowing disc (5x5 units)

#### 2.3: Slider Movement Animation (0:35 – 0:44)
- [ ] Phase 1 (0:35–0:39): Indicator arrow snaps upward to **0.99**, points at Left text
  - Duration: 0.5 seconds
  - Left text glows cyan (`#00F0FF`)
- [ ] Phase 2 (0:39–0:44): Indicator arrow drops to **-0.50**, points at Right text
  - Duration: 0.8 seconds
  - Add bounce/overshoot effect (ease-out with oscillation)
  - Right text transitions to dull brown (`#8B6F47`)
- [ ] Cycling numbers display: next to slider, numbers cycle rapidly (e.g., 0.45... 0.67... 0.99)
  - Update frequency: 5 times per second
  - Font: monospace, small, `#00F0FF`

#### 2.4: Text Reveal (0:45 – 0:50)
- [ ] Fade out slider
- [ ] Keep floating numbers **0.99** and **-0.50** on screen
- [ ] Animate text "REGRESSION: PREDICTING A QUANTITY" with mask reveal (left-to-right wipe)
- [ ] Text color: `#00F0FF`, bold, large font
- [ ] Animation duration: 0.8 seconds

---

### ✅ Section 3: Linear Regression (0:50 – 1:15)
**Scene Class:** `LinearRegressionScene`
**Difficulty:** Hard

#### 3.1: Cartesian Grid & Data Points (0:50 – 0:59)
- [ ] Create 2D Cartesian grid (glowing effect)
- [ ] Grid lines: faint grey (`#404040`), opacity 0.5
- [ ] X-axis label: "Input (Study Hours)" (`#F2F2F2`, right-aligned)
- [ ] Y-axis label: "Output (Test Score)" (`#F2F2F2`, top-aligned)
- [ ] Generate 20 white dots (`#FFFFFF`) positioned to form loose upward trend
- [ ] Dot spawn animation: pop in sequentially, 0.4 second duration total
- [ ] Dots positioned roughly: (1, 2), (2, 3.5), (3, 4), (4, 5.5), (5, 6), etc. (add +/-0.5 noise)

#### 3.2: Linear Fit Line (1:00 – 1:04)
- [ ] Draw cyan laser line (`#00F0FF`) across graph (y = mx + b form)
- [ ] Line animation: draw smoothly from origin across data (1.0 second)
- [ ] Display equation near line: y = mx + b with animated numbers
- [ ] Variables m (slope) and b (intercept) cycle through values rapidly (0.1s updates)
- [ ] Final equation: approximately y = 1.05x + 1.0

#### 3.3: Residual Detail (1:05 – 1:09)
- [ ] Extreme zoom: focus on single outlier dot (e.g., at (2.5, 5.5) when line at y=3.6)
- [ ] Camera zoom factor: 3x, centered on outlier
- [ ] Drop vertical red line (`#FF2A2A`) from dot to regression line
- [ ] Bracket annotation next to red line with label "ε (epsilon)" and text "ERROR"
- [ ] Font: monospace, white, medium size
- [ ] Zoom duration: 0.6 seconds

#### 3.4: Error Minimization (1:10 – 1:15)
- [ ] Zoom out to full graph view
- [ ] Show red residual lines on all dots (calculate distances)
- [ ] Animate cyan line slight rotation/adjustment (optimize slope by ±0.1)
- [ ] As line moves: red lines expand/contract in real-time
- [ ] When optimized: all red lines turn green and fade out (0.5 second fade)
- [ ] Line locks in place

---

### ✅ Section 4: Non-Linear Regression (1:15 – 1:40)
**Scene Class:** `NonLinearRegressionScene`
**Difficulty:** Very Hard

#### 4.1: Non-Linear Data Pattern (1:15 – 1:24)
- [ ] Create new graph with darkened background (slightly darker `#0A0A0A`)
- [ ] X-axis label: "Drug Dosage" (`#F2F2F2`)
- [ ] Y-axis label: "Patient Health" (`#F2F2F2`)
- [ ] Generate 25+ data points with S-curve (sigmoid) pattern:
  - Rising steeply: (1, 1), (2, 2.5), (3, 4)
  - Plateau: (4, 4.8), (5, 4.9), (6, 4.95)
  - Plummet: (7, 3), (8, 1.5), (9, 0.2)
- [ ] Points color: white (`#FFFFFF`)
- [ ] Spawn sequentially, 0.5 second total duration

#### 4.2: Linear Line Failure (1:25 – 1:29)
- [ ] Reuse cyan line from Section 3 (y = 1.05x + 1.0)
- [ ] Overlay on new data: line cuts through rising phase, misses crash entirely
- [ ] Draw massive, thick red residual bars (`#FF2A2A`, 3px width) on crash points
- [ ] Screen pulse effect: red glow on edges every 0.3 seconds (4 pulses)
- [ ] Add warning text: "LINEAR MODEL FAILS" (red, small, center-bottom)

#### 4.3: Curve Bending Animation (1:30 – 1:35)
- [ ] Straight line snaps/shatters visual effect
- [ ] Morphs into polynomial curve (inverted U shape, quadratic)
- [ ] Curve equation: y = -0.4(x-5)^2 + 5
- [ ] Animation duration: 0.8 seconds (smooth morph)
- [ ] Curve color: cyan (`#00F0FF`)
- [ ] Red error bars fade instantly when curve fits (< 0.1 second)

#### 4.4: Non-Linear Label & Equation (1:36 – 1:40)
- [ ] Fade out grid
- [ ] Display "NON-LINEAR REGRESSION" text (bold, `#00F0FF`, large)
- [ ] Show equation morphing: y = mx + b → y = ax^2 + bx + c
- [ ] Equation animation: old terms fade, new terms appear (0.6 seconds)
- [ ] Keep curved line visible

---

### ✅ Section 5: The Synthesis (1:40 – 2:00)
**Scene Class:** `SynthesisScene`
**Difficulty:** Very Hard

#### 5.1: Isolate Curve (1:40 – 1:44)
- [ ] Remove axes, grid, labels from previous scene
- [ ] Keep only the glowing cyan curve from Section 4
- [ ] Curve positioned center-screen, floating in void (`#0D0D0D`)
- [ ] Apply glow effect to curve (larger, fainter copy behind)

#### 5.2: Curve to Node Compression (1:45 – 1:49)
- [ ] Animate curve shrinking/compressing into circle (0.8 seconds)
- [ ] Final size: 0.8 units diameter
- [ ] Draw sigmoid symbol (σ) inside circle
- [ ] Node color: cyan (`#00F0FF`) with white core
- [ ] Style: looks like biological cell or digital neuron

#### 5.3: Network Expansion (1:50 – 1:55)
- [ ] Rapid zoom out sequence (1.0 seconds)
- [ ] Phase 1 (0.2s): 1 node → 5 connected nodes (lines between them)
- [ ] Phase 2 (0.3s): 5 nodes → 50 nodes (fractal-like expansion)
- [ ] Phase 3 (0.5s): 50 nodes → 1,000+ nodes (massive neural network)
- [ ] Every connection: thin cyan line (`#00F0FF`, 0.5px opacity)
- [ ] Every node: small glowing disc, random positions
- [ ] Add light pulses traveling left-to-right through connections (data flow animation)
- [ ] Pulse frequency: 10 pulses per second, staggered

#### 5.4: Climax & Final Text (1:56 – 2:00)
- [ ] Network fades slightly (reduce opacity to 0.6)
- [ ] "Judge" text from Section 1 reappears (center-screen, glowing gold `#FFD700`)
- [ ] Stamp animation: "VALUE PREDICTED" text appears with bold stroke effect
- [ ] Text color: gold (`#FFD700`), very large, bold
- [ ] Text animation: stamp with slight shear/skew (0.2 seconds)
- [ ] Hold final frame for 0.5 seconds

---

## Audio Requirements (For Reference)

### Section 1: SFX & VO
- **SFX:** Modem handshake screech (low volume) → 40Hz hum when red box appears
- **VO:** "Intelligence without a target is just noise..." (provided in script)

### Section 2: SFX & VO
- **SFX:** Mechanical clicking (aperture ring), heavy "thud" on negative values
- **VO:** "This 'Judge' doesn't just say 'Wrong'..." (provided in script)

### Section 3: SFX & VO
- **SFX:** Digital "ping" for each dot, servo motor sound as line rotates
- **VO:** "In a perfect world, relationships are simple..." (provided in script)

### Section 4: SFX & VO
- **SFX:** Alarm buzzer (subtle) on failure, fluid "whoosh" when line bends
- **VO:** "But biology isn't linear..." (provided in script)

### Section 5: SFX & VO
- **SFX:** Crescendo of digital synapses firing, building to unified hum
- **VO:** "And that AI Judge from the beginning?..." (provided in script)

---

## Technical Specifications

### Manim Configuration
- **Frame Rate:** 60 FPS
- **Resolution:** 1920x1080 (16:9 aspect ratio)
- **Quality:** High quality render (adjust via `-qh` flag)
- **Scene Resolution:** 1080p

### Color Palette (Consistent)
| Element | Hex Color | Purpose |
|---------|-----------|---------|
| Background | `#0D0D0D` | Main dark void |
| Text/Foreground | `#F2F2F2` | Primary text |
| Accent Primary | `#00F0FF` | Cyan (regression lines, highlights) |
| Accent Danger | `#FF2A2A` | Red (errors, warnings) |
| Green Terminal | `#00FF00` | Terminal cursor, legacy |
| Gold | `#FFD700` | Final synthesis highlight |
| Grid/Subtle | `#404040` | Faint grid lines |
| Brown/Dull | `#8B6F47` | Dull text highlight |

### Animation Timings (Reference)
- **Fast transition:** 0.3 – 0.5 seconds
- **Medium animation:** 0.6 – 1.0 seconds
- **Slow reveal:** 1.5 – 2.0 seconds
- **Text cascade:** 120ms per line
- **Letter jitter:** ~50ms per flicker

### Data Point Generation
- Use `np.random.seed(42)` for reproducibility
- Apply noise with `np.random.normal(0, 0.3)` for realistic scatter
- Ensure all datasets are deterministic (same seed each render)

---

## File Structure & Organization

```
Manim-ML/
├── videos/
│   ├── scenes/
│   │   ├── __init__.py
│   │   ├── section1_hallucination.py      # HallucinationScene
│   │   ├── section2_scale.py              # ContinuousScaleScene
│   │   ├── section3_linear.py             # LinearRegressionScene
│   │   ├── section4_nonlinear.py          # NonLinearRegressionScene
│   │   ├── section5_synthesis.py          # SynthesisScene
│   │   └── judge_curve_complete.py        # Full video composition
│   ├── templates/
│   │   ├── effects.py                     # Chromatic aberration, glows, etc.
│   │   ├── animations.py                  # Custom animation classes
│   │   └── custom_shapes.py               # Slider, warning icon, nodes
│   ├── assets/
│   │   ├── images/
│   │   │   └── warning_icon.png           # TODO: See Section 1.3
│   │   └── data/
│   │       ├── linear_data.csv            # Pre-computed regression data
│   │       └── nonlinear_data.csv         # S-curve drug dosage data
│   └── judge_curve_main.py                # Entry point script
├── src/
│   ├── utils/
│   │   ├── data_generator.py              # Generate consistent datasets
│   │   └── color_utils.py                 # Color palette constants
│   └── config.py                          # Shared configuration
└── requirements.md                         # This file
```

---

## Implementation Order (For AI Agents)

### Phase 1: Setup & Utilities (Foundation)
1. **config.py** - Define all color constants, timings, frame rates
2. **src/utils/color_utils.py** - Reusable color palette and functions
3. **src/utils/data_generator.py** - Functions to generate linear & non-linear datasets
4. **videos/templates/custom_shapes.py** - Slider, warning icon, node shapes

### Phase 2: Effects & Animations (Base Layer)
5. **videos/templates/effects.py** - Chromatic aberration, glows, pulses
6. **videos/templates/animations.py** - Custom animation classes (jitter, morph, etc.)

### Phase 3: Individual Scenes (Implementation)
7. **section1_hallucination.py** - Build HallucinationScene
8. **section2_scale.py** - Build ContinuousScaleScene
9. **section3_linear.py** - Build LinearRegressionScene
10. **section4_nonlinear.py** - Build NonLinearRegressionScene
11. **section5_synthesis.py** - Build SynthesisScene

### Phase 4: Composition & Final (Integration)
12. **judge_curve_complete.py** - Combine all scenes with timing
13. **judge_curve_main.py** - Entry point, render full video

---

## Success Criteria

- [ ] All 5 scenes render without errors
- [ ] Timings match script (total duration: 2:00)
- [ ] Color palette is consistent across all scenes
- [ ] Animations are smooth (60 FPS, no jank)
- [ ] Type hints pass Pyright strict mode
- [ ] Code passes Ruff linting (all rules)
- [ ] Final video quality is 1920x1080 @ 60FPS
- [ ] All scenes have comprehensive docstrings
- [ ] Data points are reproducible (seeded RNG)
- [ ] All TODOs for asset generation are completed before final render

---

## Notes for AI Agents

1. **Use `from __future__ import annotations`** at the top of every module
2. **Type hint everything:** All function returns, parameters, variables
3. **Create helper functions** in templates for reusable effects (glow, pulse, etc.)
4. **Test sections independently** before composing into full video
5. **Use Manim Groups** to organize complex animations
6. **Pre-generate datasets** to `videos/assets/data/` for consistency
7. **Document timings carefully** - sync animations to scene durations
8. **Leverage animate()** for smooth transitions between states
9. **Use ConfigDict** (from Manim) for scene resolution/FPS settings
10. **Run `ruff format .` and `ruff check . --fix`** before each commit
11. **Verify with Pyright** before considering code complete
12. **For TODOs marked with "Generate an image with this prompt:"**
    - Use an AI image generation service (DALL-E, Midjourney, Stable Diffusion, etc.)
    - Save generated images to the specified path
    - Ensure transparency and proper dimensions as specified
    - Document which service was used for reproducibility

---

## Asset TODO List (Images to Generate)

### Section 1: Hallucination Scene
- **TODO:** Generate an image with this prompt: "A minimalist warning icon (triangle with exclamation mark) in bright red (#FF2A2A) with glowing edges, 256x256px, transparent background, vector style, suitable for dark UI overlay" and place it at `/videos/assets/images/warning_icon.png`

---

## Key References

- **Script Source:** `script.md` (complete visual & audio directives)
- **Manim Docs:** https://docs.manim.community/
- **Color Palette:** See Technical Specifications section
- **Templates:** See File Structure & Organization section
