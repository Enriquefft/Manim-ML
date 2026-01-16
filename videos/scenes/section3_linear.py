"""Section 3: Linear Regression (The Ideal World).

Time: 0:50 - 1:15

[Visual Scene]
- 0:50: Graph appears. X-axis: "Study Hours", Y-axis: "Test Score"
- 0:55: Data points (dots) appear scattered in upward trend
- 1:00: Straight line shoots through them
- 1:05: CRITICAL: Zoom on single dot NOT touching line, red vertical bar
        labeled "RESIDUAL (ERROR)"
- 1:10: Line wiggles until red bars are minimized

[Audio / Voiceover]
"In a perfect world, relationships are simple. Double the study time, double
the grade. This is Linear Regression. The math draws a straight line (y=mx+b)
to minimize the distance between the prediction and reality. We call that
distance the 'Error.' The line exists to make the Error small."

Duration: 25 seconds (0:50-1:15)
"""

from __future__ import annotations

from pathlib import Path

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    Axes,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    ManimColor,
    Text,
    VGroup,
    Write,
)
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

from src.config import COLORS, SCENE_LINEAR_REGRESSION
from src.utils.color_utils import get_background_color
from src.utils.data_generator import (
    DataPoint,
    RegressionLine,
    create_error_bars,
    fit_linear_regression,
    generate_linear_data,
    load_data_from_csv,
)


class LinearRegressionScene(VoiceoverScene):
    """Section 3: Linear Regression (The Ideal World).

    Demonstrates linear regression visually - the concept that relationships
    can be captured with a straight line, and the importance of minimizing
    error (residuals) between predictions and reality.

    Visual Timeline:
    - 0:50-0:55: Cartesian grid with "Study Hours"/"Test Score" axes
    - 0:55-1:00: Data points appear scattered in upward trend
    - 1:00-1:05: Straight line shoots through them
    - 1:05-1:10: CRITICAL - Zoom on dot NOT touching line, red bar "RESIDUAL (ERROR)"
    - 1:10-1:15: Line wiggles until red bars are minimized

    Timing: 0:50-1:15 (25 seconds)
    """

    SCENE_NAME: str = "linear_regression"
    START_TIME: float = SCENE_LINEAR_REGRESSION.start_time
    END_TIME: float = SCENE_LINEAR_REGRESSION.end_time

    # Voiceover script for this section
    VOICEOVER_TEXT: str = (
        "In a perfect world, relationships are simple. "
        "Double the study time, double the grade. "
        "This is Linear Regression. "
        "The math draws a straight line (y=mx+b) to minimize the distance "
        "between the prediction and reality. "
        "We call that distance the 'Error.' "
        "The line exists to make the Error small."
    )

    def construct(self) -> None:
        """Build the linear regression scene animation sequence."""
        self.set_speech_service(GTTSService())
        self.camera.background_color = get_background_color()

        # Start voiceover that plays throughout the scene
        with self.voiceover(text=self.VOICEOVER_TEXT) as tracker:
            self._run_visual_sequence(tracker.duration)

    def _run_visual_sequence(self, total_duration: float) -> None:
        """Run the visual animation sequence synchronized to voiceover.

        Args:
            total_duration: Total duration from voiceover tracker.

        """
        # Calculate phase durations based on total voiceover length
        # Phases: grid (15%), points (15%), line (15%), residual (25%), wiggle (20%), fadeout (10%)
        grid_duration = total_duration * 0.15
        points_duration = total_duration * 0.15
        line_duration = total_duration * 0.15
        residual_duration = total_duration * 0.25
        wiggle_duration = total_duration * 0.20
        fadeout_duration = total_duration * 0.10

        # Phase 1: Create grid with axes (0:50-0:55)
        axes = self._create_cartesian_grid("Study Hours", "Test Score")
        self.play(Create(axes), run_time=grid_duration)

        # Phase 2: Load and display data points (0:55-1:00)
        data_path = Path("videos/assets/data/linear_data.csv")
        if data_path.exists():
            points = self._load_data_points(str(data_path))
        else:
            # Generate data if file doesn't exist
            points = generate_linear_data()

        point_mobjects = self._create_data_point_mobjects(points, axes)

        # Animate points appearing in upward trend
        time_per_point = points_duration / len(point_mobjects)
        for dot in point_mobjects:
            self.play(FadeIn(dot), run_time=time_per_point * 0.8)

        # Phase 3: Straight line shoots through (1:00-1:05)
        regression = self._fit_linear_regression(points)
        line = self._create_regression_line_mobject(regression, axes, (-0.5, 10.5))
        self.play(Create(line), run_time=line_duration)

        # Phase 4: CRITICAL - Zoom on single dot, show "RESIDUAL (ERROR)" (1:05-1:10)
        error_bars = self._create_error_bars(points, regression, axes)

        # Find the point with largest error for zoom
        errors = create_error_bars(points, regression)
        max_error_idx = max(range(len(errors)), key=lambda i: abs(errors[i].residual))

        outlier_dot = point_mobjects[max_error_idx]
        outlier_bar = error_bars[max_error_idx]

        # Show just the single error bar first
        self.play(Create(outlier_bar), run_time=residual_duration * 0.2)

        # Zoom effect on the outlier dot and its error bar
        self.play(
            outlier_dot.animate.scale(1.5),
            outlier_bar.animate.set_stroke(width=4),
            run_time=residual_duration * 0.2,
        )

        # Add "RESIDUAL (ERROR)" label
        residual_label = Text(
            "RESIDUAL (ERROR)",
            font_size=24,
            color=ManimColor(COLORS.RED),
            weight="BOLD",
        )
        residual_label.next_to(outlier_bar, RIGHT, buff=0.2)

        self.play(Write(residual_label), run_time=residual_duration * 0.3)
        self.wait(residual_duration * 0.3)

        # Phase 5: Line wiggles until red bars are minimized (1:10-1:15)
        # Show all error bars first
        other_bars = VGroup(*[bar for i, bar in enumerate(error_bars) if i != max_error_idx])
        self.play(Create(other_bars), run_time=wiggle_duration * 0.3)

        # Animate line wiggle to show error minimization
        self._animate_error_minimization(
            line,
            regression,
            axes,
            duration=wiggle_duration * 0.7,
        )

        # Phase 6: Fade out everything
        all_content = VGroup(
            axes,
            point_mobjects,
            line,
            error_bars,
            residual_label,
        )
        self.play(FadeOut(all_content), run_time=fadeout_duration)

    def _create_cartesian_grid(
        self,
        x_label: str,
        y_label: str,
    ) -> Axes:
        """Create 2D grid with axis labels.

        Args:
            x_label: Label for x-axis
            y_label: Label for y-axis

        Returns:
            Axes mobject with labels

        """
        axes = Axes(
            x_range=[0, 11, 1],
            y_range=[0, 14, 2],
            x_length=10,
            y_length=6,
            axis_config={
                "color": ManimColor(COLORS.GRID),
                "include_tip": True,
                "tip_length": 0.2,
            },
            x_axis_config={"numbers_to_include": [2, 4, 6, 8, 10]},
            y_axis_config={"numbers_to_include": [2, 4, 6, 8, 10, 12]},
        )

        # Add axis labels
        x_label_text = Text(x_label, font_size=24, color=ManimColor(COLORS.TEXT))
        x_label_text.next_to(axes.x_axis, DOWN, buff=0.3)

        y_label_text = Text(y_label, font_size=24, color=ManimColor(COLORS.TEXT))
        y_label_text.next_to(axes.y_axis, LEFT, buff=0.3)
        y_label_text.rotate(90 * 3.14159 / 180)

        axes.add(x_label_text, y_label_text)
        axes.center()

        return axes

    def _load_data_points(self, csv_path: str) -> list[DataPoint]:
        """Load pre-generated data from CSV.

        Args:
            csv_path: Path to CSV file

        Returns:
            List of DataPoint objects

        """
        return load_data_from_csv(csv_path)

    def _create_data_point_mobjects(
        self,
        points: list[DataPoint],
        axes: Axes,
    ) -> VGroup:
        """Create dot mobjects for each data point.

        Args:
            points: List of data points
            axes: Axes to position dots on

        Returns:
            VGroup containing all dot mobjects

        """
        dots = VGroup()

        for point in points:
            # Convert data coordinates to scene coordinates
            pos = axes.c2p(point.x, point.y)
            dot = Dot(
                point=pos,
                radius=0.08,
                color=ManimColor(COLORS.TEXT),
                fill_opacity=1.0,
            )
            dots.add(dot)

        return dots

    def _fit_linear_regression(
        self,
        points: list[DataPoint],
    ) -> RegressionLine:
        """Calculate best-fit line parameters.

        Args:
            points: List of data points

        Returns:
            RegressionLine with fitted parameters

        """
        return fit_linear_regression(points)

    def _create_regression_line_mobject(
        self,
        regression: RegressionLine,
        axes: Axes,
        x_range: tuple[float, float],
    ) -> Line:
        """Create visual line from regression model.

        Args:
            regression: Fitted regression model
            axes: Axes for coordinate conversion
            x_range: (min_x, max_x) for line endpoints

        Returns:
            Line mobject representing the regression

        """
        x1, x2 = x_range
        y1 = regression.predict(x1)
        y2 = regression.predict(x2)

        start = axes.c2p(x1, y1)
        end = axes.c2p(x2, y2)

        return Line(
            start=start,
            end=end,
            color=ManimColor(COLORS.CYAN),
            stroke_width=3,
        )

    def _create_error_bars(
        self,
        points: list[DataPoint],
        regression: RegressionLine,
        axes: Axes,
    ) -> VGroup:
        """Create residual visualization lines.

        Args:
            points: List of data points
            regression: Fitted regression model
            axes: Axes for coordinate conversion

        Returns:
            VGroup containing all error bar lines

        """
        bars = VGroup()

        for point in points:
            predicted_y = regression.predict(point.x)

            start = axes.c2p(point.x, point.y)
            end = axes.c2p(point.x, predicted_y)

            bar = Line(
                start=start,
                end=end,
                color=ManimColor(COLORS.RED),
                stroke_width=2,
                stroke_opacity=0.7,
            )
            bars.add(bar)

        return bars

    # Number of coefficients in a standard linear regression (slope + intercept)
    _LINEAR_COEFFICIENT_COUNT: int = 2

    def _animate_error_minimization(
        self,
        line: Line,
        regression: RegressionLine,
        axes: Axes,
        duration: float,
    ) -> None:
        """Animate line wiggling to show error minimization.

        Demonstrates the line adjusting to minimize residuals - starts with
        a slightly wrong slope, then settles to the optimal position.

        Args:
            line: Regression line to wiggle.
            regression: Fitted regression model (optimal position).
            axes: Axes for coordinate conversion.
            duration: Total duration for the wiggle animation.

        """
        # Get optimal coefficients
        is_standard_linear = (
            regression.line_type == "linear"
            and len(regression.coefficients) == self._LINEAR_COEFFICIENT_COUNT
        )
        if is_standard_linear:
            optimal_slope, optimal_intercept = regression.coefficients
        else:
            # Default if not standard linear
            optimal_slope, optimal_intercept = 1.0, 1.0

        # Define wiggle sequence: start slightly off, then converge
        # Wiggle offsets from optimal slope (shrinking oscillation)
        wiggle_offsets = [0.3, -0.2, 0.1, -0.05, 0.0]

        time_per_wiggle = duration / len(wiggle_offsets)

        for offset in wiggle_offsets:
            new_slope = optimal_slope + offset

            # Calculate new line endpoints with perturbed slope
            x1, x2 = -0.5, 10.5
            y1 = new_slope * x1 + optimal_intercept
            y2 = new_slope * x2 + optimal_intercept

            new_start = axes.c2p(x1, y1)
            new_end = axes.c2p(x2, y2)

            # Animate line moving to new position
            self.play(
                line.animate.put_start_and_end_on(new_start, new_end),
                run_time=time_per_wiggle,
            )

    def get_duration(self) -> float:
        """Return scene duration."""
        return self.END_TIME - self.START_TIME
