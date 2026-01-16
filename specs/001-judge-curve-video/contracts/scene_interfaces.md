# Scene Interface Contracts

**Feature**: 001-judge-curve-video
**Date**: 2026-01-10

## Base Scene Contract

All scenes must implement this interface:

```python
class BaseVideoScene(Scene):
    """Base class for all Judge & Curve video scenes."""

    # Class attributes
    SCENE_NAME: str  # Unique identifier
    START_TIME: float  # In seconds from video start
    END_TIME: float  # In seconds from video start

    def construct(self) -> None:
        """Main animation sequence. Must complete within duration."""
        ...

    def get_duration(self) -> float:
        """Return END_TIME - START_TIME."""
        ...
```

## Scene-Specific Contracts

### HallucinationScene (Section 1)

**Duration**: 25 seconds (0:00 - 0:25)

```python
class HallucinationScene(BaseVideoScene):
    """
    Section 1: Establish AI hallucination metaphor.

    Demonstrates unguided AI producing noise, setting narrative context
    for why regression/judgment matters.
    """

    SCENE_NAME: str = "hallucination"
    START_TIME: float = 0.0
    END_TIME: float = 25.0

    def create_terminal_cursor(self) -> Mobject:
        """Create blinking green cursor with chromatic aberration."""
        ...

    def create_text_cascade(self, lines: list[str]) -> VGroup:
        """Create cascading nonsense text with jitter effect."""
        ...

    def create_warning_overlay(self) -> VGroup:
        """Create red warning box with 'NO METRIC FOUND' text."""
        ...

    def create_warning_icon(self) -> VGroup:
        """Create programmatic warning triangle icon."""
        ...

    def apply_static_dissolution(self, target: Mobject) -> Animation:
        """Transition target to static noise with dolly zoom."""
        ...
```

### ContinuousScaleScene (Section 2)

**Duration**: 25 seconds (0:25 - 0:50)

```python
class ContinuousScaleScene(BaseVideoScene):
    """
    Section 2: Introduce continuous scoring concept.

    Shows split-screen with slider to demonstrate that outputs
    exist on a continuous scale, not just true/false.
    """

    SCENE_NAME: str = "continuous_scale"
    START_TIME: float = 25.0
    END_TIME: float = 50.0

    def create_split_screen(
        self,
        left_text: str,
        right_text: str
    ) -> tuple[VGroup, VGroup, Line]:
        """Create split screen with divider and text panes."""
        ...

    def create_slider(
        self,
        height: float,
        top_label: str,
        bottom_label: str
    ) -> VGroup:
        """Create vertical gradient slider with labels."""
        ...

    def animate_slider_movement(
        self,
        slider: VGroup,
        target_value: float,
        duration: float
    ) -> Animation:
        """Animate slider handle to target position."""
        ...

    def create_cycling_numbers(self) -> DecimalNumber:
        """Create rapidly cycling number display."""
        ...
```

### LinearRegressionScene (Section 3)

**Duration**: 25 seconds (0:50 - 1:15)

```python
class LinearRegressionScene(BaseVideoScene):
    """
    Section 3: Demonstrate linear regression.

    Shows data points, fits a line, explains error/residuals,
    and demonstrates error minimization.
    """

    SCENE_NAME: str = "linear_regression"
    START_TIME: float = 50.0
    END_TIME: float = 75.0

    def create_cartesian_grid(
        self,
        x_label: str,
        y_label: str
    ) -> VGroup:
        """Create 2D grid with axis labels."""
        ...

    def load_data_points(self, csv_path: str) -> list[DataPoint]:
        """Load pre-generated data from CSV."""
        ...

    def create_data_point_mobjects(
        self,
        points: list[DataPoint]
    ) -> VGroup:
        """Create dot mobjects for each data point."""
        ...

    def fit_linear_regression(
        self,
        points: list[DataPoint]
    ) -> RegressionLine:
        """Calculate best-fit line parameters."""
        ...

    def create_regression_line_mobject(
        self,
        regression: RegressionLine,
        x_range: tuple[float, float]
    ) -> Line:
        """Create visual line from regression model."""
        ...

    def create_equation_display(
        self,
        regression: RegressionLine
    ) -> VGroup:
        """Create LaTeX equation with animated coefficients."""
        ...

    def create_error_bars(
        self,
        points: list[DataPoint],
        regression: RegressionLine
    ) -> VGroup:
        """Create residual visualization lines."""
        ...

    def animate_error_minimization(
        self,
        line: Line,
        error_bars: VGroup,
        points: list[DataPoint]
    ) -> AnimationGroup:
        """Animate line rotation while updating error bars."""
        ...
```

### NonLinearRegressionScene (Section 4)

**Duration**: 25 seconds (1:15 - 1:40)

```python
class NonLinearRegressionScene(BaseVideoScene):
    """
    Section 4: Demonstrate non-linear regression.

    Shows linear model failure on S-curve data, then morphs
    to polynomial curve that fits better.
    """

    SCENE_NAME: str = "nonlinear_regression"
    START_TIME: float = 75.0
    END_TIME: float = 100.0

    def create_scurve_data(self) -> list[DataPoint]:
        """Load S-curve pattern data from CSV."""
        ...

    def show_linear_failure(
        self,
        linear_line: Line,
        data_points: VGroup
    ) -> AnimationGroup:
        """Show linear line failing with large error bars."""
        ...

    def create_screen_pulse_effect(
        self,
        color: str,
        count: int
    ) -> Animation:
        """Create red screen edge pulse animation."""
        ...

    def animate_line_to_curve(
        self,
        linear_line: Line,
        polynomial_coefficients: list[float]
    ) -> Animation:
        """Morph straight line into polynomial curve."""
        ...

    def create_polynomial_equation_morph(
        self,
        from_equation: MathTex,
        to_equation: MathTex
    ) -> Animation:
        """Animate equation transformation."""
        ...
```

### SynthesisScene (Section 5)

**Duration**: 20 seconds (1:40 - 2:00)

```python
class SynthesisScene(BaseVideoScene):
    """
    Section 5: Connect regression to neural networks.

    Compresses curve to node, expands to massive network,
    delivers final 'VALUE PREDICTED' message.
    """

    SCENE_NAME: str = "synthesis"
    START_TIME: float = 100.0
    END_TIME: float = 120.0

    def isolate_curve(self, curve: ParametricFunction) -> VGroup:
        """Remove context, keep only glowing curve."""
        ...

    def animate_curve_to_node(
        self,
        curve: ParametricFunction
    ) -> tuple[Animation, Circle]:
        """Compress curve into single node with sigma symbol."""
        ...

    def create_neural_network(
        self,
        node_count: int,
        layer_sizes: list[int]
    ) -> NeuralNetwork:
        """Generate network structure with connections."""
        ...

    def animate_network_expansion(
        self,
        start_node: Circle,
        network: NeuralNetwork
    ) -> AnimationGroup:
        """Rapid zoom-out expansion animation."""
        ...

    def create_data_flow_pulses(
        self,
        network: NeuralNetwork,
        pulse_count: int
    ) -> AnimationGroup:
        """Animate light pulses traveling through connections."""
        ...

    def create_final_stamp(
        self,
        text: str,
        color: str
    ) -> Animation:
        """Create stamp animation for final text."""
        ...
```

## Utility Contracts

### effects.py

```python
def apply_chromatic_aberration(
    mobject: Mobject,
    offset: float = 0.02
) -> VGroup:
    """Create RGB-split effect on mobject."""
    ...

def apply_glow_effect(
    mobject: Mobject,
    glow_factor: float = 1.5,
    opacity: float = 0.3
) -> VGroup:
    """Add outer glow to mobject."""
    ...

def create_pulse_animation(
    mobject: Mobject,
    scale_factor: float = 1.1,
    duration: float = 0.5
) -> Animation:
    """Create pulsing scale/opacity animation."""
    ...

def create_dolly_zoom(
    camera: Camera,
    duration: float = 1.0
) -> Animation:
    """Create Hitchcock dolly zoom effect."""
    ...
```

### animations.py

```python
class TextJitter(Animation):
    """Animate random character corruption."""

    def __init__(
        self,
        text_mobject: Text,
        corruption_rate: float = 0.3,
        **kwargs: Any
    ) -> None:
        ...

class LineMorph(Animation):
    """Smoothly morph line to curve."""

    def __init__(
        self,
        line: Line,
        target_func: Callable[[float], float],
        **kwargs: Any
    ) -> None:
        ...

class StampIn(Animation):
    """Stamp text with shear/skew effect."""

    def __init__(
        self,
        text: Text,
        shear_angle: float = 0.1,
        **kwargs: Any
    ) -> None:
        ...
```

### custom_shapes.py

```python
def create_warning_icon(
    size: float = 1.0,
    color: str = "#FF2A2A"
) -> VGroup:
    """Create warning triangle with exclamation mark."""
    ...

def create_slider_component(
    height: float,
    width: float,
    top_color: str,
    bottom_color: str
) -> VGroup:
    """Create gradient slider with handle."""
    ...

def create_network_node(
    radius: float = 0.02,
    color: str = "#00F0FF",
    symbol: str | None = None
) -> VGroup:
    """Create neural network node with optional internal symbol."""
    ...
```

### data_generator.py

```python
def generate_linear_data(
    n_points: int = 20,
    slope: float = 1.05,
    intercept: float = 1.0,
    noise_std: float = 0.3,
    seed: int = 42
) -> list[DataPoint]:
    """Generate linear trend data with noise."""
    ...

def generate_scurve_data(
    n_points: int = 25,
    seed: int = 42
) -> list[DataPoint]:
    """Generate S-curve pattern (rise, plateau, crash)."""
    ...

def save_data_to_csv(
    points: list[DataPoint],
    filepath: str
) -> None:
    """Save data points to CSV file."""
    ...

def load_data_from_csv(
    filepath: str
) -> list[DataPoint]:
    """Load data points from CSV file."""
    ...
```
