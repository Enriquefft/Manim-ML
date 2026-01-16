# Data Model: The Judge & The Curve Video

**Feature**: 001-judge-curve-video
**Date**: 2026-01-10

## Core Entities

### 1. ColorPalette

Central configuration for all colors used across scenes.

| Attribute | Type | Value | Purpose |
|-----------|------|-------|---------|
| BACKGROUND | str | "#0D0D0D" | Main dark void |
| TEXT | str | "#F2F2F2" | Primary text/foreground |
| CYAN | str | "#00F0FF" | Regression lines, highlights |
| RED | str | "#FF2A2A" | Errors, warnings, danger |
| GOLD | str | "#FFD700" | Final synthesis highlight |
| GRID | str | "#404040" | Faint grid lines |
| GREEN | str | "#00FF00" | Terminal cursor |
| BROWN | str | "#8B6F47" | Dull text highlight |

**Validation**: All values must be valid 6-digit hex color codes.

### 2. TimingConfig

Animation timing constants.

| Attribute | Type | Value | Purpose |
|-----------|------|-------|---------|
| FAST_MIN | float | 0.3 | Fast animation minimum (seconds) |
| FAST_MAX | float | 0.5 | Fast animation maximum (seconds) |
| MEDIUM_MIN | float | 0.6 | Medium animation minimum (seconds) |
| MEDIUM_MAX | float | 1.0 | Medium animation maximum (seconds) |
| SLOW_MIN | float | 1.5 | Slow animation minimum (seconds) |
| SLOW_MAX | float | 2.0 | Slow animation maximum (seconds) |
| TEXT_CASCADE_INTERVAL | float | 0.12 | Time between text line appearances |
| JITTER_INTERVAL | float | 0.05 | Letter jitter frequency |

### 3. SceneConfig

Per-scene timing boundaries.

| Attribute | Type | Purpose |
|-----------|------|---------|
| name | str | Scene identifier (e.g., "hallucination") |
| start_time | float | Start timestamp in seconds |
| end_time | float | End timestamp in seconds |
| duration | float | Computed: end_time - start_time |

**Instances**:
| Scene | Start | End | Duration |
|-------|-------|-----|----------|
| Section 1: Hallucination | 0.0 | 25.0 | 25.0 |
| Section 2: Continuous Scale | 25.0 | 50.0 | 25.0 |
| Section 3: Linear Regression | 50.0 | 75.0 | 25.0 |
| Section 4: Non-Linear Regression | 75.0 | 100.0 | 25.0 |
| Section 5: Synthesis | 100.0 | 120.0 | 20.0 |

### 4. DataPoint

Represents a single observation on the regression graph.

| Attribute | Type | Constraints | Purpose |
|-----------|------|-------------|---------|
| x | float | >= 0 | X-coordinate (input variable) |
| y | float | any | Y-coordinate (output variable) |
| color | str | valid hex | Visual color (default: WHITE) |

**Relationships**: Belongs to a DataSet.

### 5. DataSet

Collection of data points for a regression visualization.

| Attribute | Type | Constraints | Purpose |
|-----------|------|-------------|---------|
| name | str | non-empty | Identifier (e.g., "linear", "nonlinear") |
| points | list[DataPoint] | >= 1 | Collection of observations |
| seed | int | any | RNG seed for reproducibility |

**Validation**: Points must be generated using the specified seed.

### 6. RegressionLine

Mathematical model fitted to data.

| Attribute | Type | Constraints | Purpose |
|-----------|------|-------------|---------|
| line_type | str | "linear" \| "polynomial" | Model type |
| coefficients | list[float] | >= 1 | Model parameters |
| color | str | valid hex | Visual color (default: CYAN) |

**Computed Properties**:
- `equation_str`: LaTeX representation (e.g., "y = 1.05x + 1.0")
- `predict(x: float) -> float`: Calculate y for given x

### 7. ErrorBar

Residual visualization connecting data point to regression line.

| Attribute | Type | Constraints | Purpose |
|-----------|------|-------------|---------|
| data_point | DataPoint | required | Source observation |
| predicted_y | float | any | Y-value on regression line |
| residual | float | computed | data_point.y - predicted_y |
| color | str | valid hex | Visual color (default: RED) |

### 8. NetworkNode

Single neuron in the neural network visualization.

| Attribute | Type | Constraints | Purpose |
|-----------|------|-------------|---------|
| x | float | any | X position on screen |
| y | float | any | Y position on screen |
| layer | int | >= 0 | Network layer index |
| color | str | valid hex | Visual color (default: CYAN) |
| radius | float | > 0 | Node size (default: 0.02) |

### 9. NetworkConnection

Edge between two network nodes.

| Attribute | Type | Constraints | Purpose |
|-----------|------|-------------|---------|
| source | NetworkNode | required | Origin node |
| target | NetworkNode | required | Destination node |
| opacity | float | 0.0-1.0 | Visual transparency |
| color | str | valid hex | Line color (default: CYAN) |

### 10. NeuralNetwork

Complete network structure for Section 5.

| Attribute | Type | Constraints | Purpose |
|-----------|------|-------------|---------|
| nodes | list[NetworkNode] | >= 1 | All neurons |
| connections | list[NetworkConnection] | >= 0 | All edges |
| layer_sizes | list[int] | >= 1 | Nodes per layer |

**Validation**: Total nodes must be >= 1000 for final phase (FR-010).

## State Transitions

### Scene State Machine

```
[INIT] → [SETUP] → [ANIMATING] → [COMPLETE]
   │        │           │
   └────────┴───────────┴─── [ERROR] (on failure)
```

Each scene follows this lifecycle:
1. **INIT**: Scene class instantiated
2. **SETUP**: Mobjects created, positioned
3. **ANIMATING**: `construct()` executing animations
4. **COMPLETE**: All animations finished, ready for next scene

### Regression Line Optimization State

```
[INITIAL_FIT] → [ADJUSTING] → [OPTIMIZED]
                    │
                    └── (loop while error decreasing)
```

Used in Section 3 error minimization sequence.

## Data Files

### linear_data.csv

```csv
x,y
1.0,2.3
2.0,3.4
...
```

- 20 data points
- Seed: 42
- Noise: normal(0, 0.3)
- Pattern: y ≈ 1.05x + 1.0

### nonlinear_data.csv

```csv
x,y
1.0,1.2
2.0,2.6
...
```

- 25+ data points
- Seed: 42
- Pattern: S-curve (rise → plateau → crash)
