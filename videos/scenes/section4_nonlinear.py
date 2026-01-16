"""Section 4: Non-Linear Regression (The Biological Reality).

Time: 1:15 - 1:40

[Visual Scene]
- 1:15: New Graph. X-axis: "Drug Dosage", Y-axis: "Patient Health"
- 1:20: Points rise steeply, plateau (saturation), then crash (toxicity)
- 1:25: Straight Linear line appears. It FAILS. It suggests infinite dosage
        equals infinite health. The "Residual" red lines are MASSIVE.
- 1:30: The line bends. It curves into a hill shape. Red error lines disappear.
- 1:35: Text: "NON-LINEAR REGRESSION"

[Audio / Voiceover]
"But biology isn't linear. If you keep doubling the dose, you don't cure the
patient—you kill them. Reality saturates. Reality curves. To minimize error
here, we must bend the line. This is Non-Linear Regression. We fit the math
to the messiness of the real world."

Duration: 25 seconds (1:15-1:40)
"""

from __future__ import annotations

import math

from manim import (
    DOWN,
    LEFT,
    Axes,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    ManimColor,
    ParametricFunction,
    Text,
    Transform,
    VGroup,
    Write,
)
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

from src.config import COLORS, SCENE_NONLINEAR_REGRESSION
from src.utils.color_utils import get_background_color
from src.utils.data_generator import DataPoint, fit_linear_regression


class NonLinearRegressionScene(VoiceoverScene):
    """Section 4: Non-Linear Regression (The Biological Reality).

    Demonstrates why linear models fail on biological/pharmacological data,
    and how non-linear regression can capture complex dose-response curves
    (rise → saturation → toxicity).

    Visual Timeline:
    - 1:15-1:20: Graph with "Drug Dosage"/"Patient Health" axes
    - 1:20-1:25: Data points showing dose-response (rise, plateau, crash)
    - 1:25-1:30: Linear line FAILS with MASSIVE red residuals
    - 1:30-1:35: Line bends into hill shape, errors disappear
    - 1:35-1:40: "NON-LINEAR REGRESSION" text appears

    Timing: 1:15-1:40 (25 seconds)
    """

    SCENE_NAME: str = "nonlinear_regression"
    START_TIME: float = SCENE_NONLINEAR_REGRESSION.start_time
    END_TIME: float = SCENE_NONLINEAR_REGRESSION.end_time

    # Voiceover script for this section
    VOICEOVER_TEXT: str = (
        "But biology isn't linear. "
        "If you keep doubling the dose, you don't cure the patient—you kill them. "
        "Reality saturates. Reality curves. "
        "To minimize error here, we must bend the line. "
        "This is Non-Linear Regression. "
        "We fit the math to the messiness of the real world."
    )

    def construct(self) -> None:
        """Build the non-linear regression scene animation sequence."""
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
        # Phases: grid (15%), points (15%), linear fail (25%), bend (25%), text+fade (20%)
        grid_duration = total_duration * 0.15
        points_duration = total_duration * 0.15
        linear_fail_duration = total_duration * 0.25
        bend_duration = total_duration * 0.25
        conclusion_duration = total_duration * 0.20

        # Phase 1: Create graph with axes (1:15-1:20)
        axes = self._create_dose_response_axes()
        self.play(Create(axes), run_time=grid_duration)

        # Phase 2: Data points appear - dose response pattern (1:20-1:25)
        # Rise steeply, plateau (saturation), then crash (toxicity)
        points = self._generate_dose_response_data()
        point_mobjects = self._create_data_point_mobjects(points, axes)

        time_per_point = points_duration / len(point_mobjects)
        for dot in point_mobjects:
            self.play(FadeIn(dot), run_time=time_per_point * 0.8)

        # Phase 3: Linear line FAILS - MASSIVE error bars (1:25-1:30)
        linear_regression = fit_linear_regression(points)

        # Extend line beyond data to show absurd "infinite dose = infinite health"
        linear_line = Line(
            start=axes.c2p(-0.5, linear_regression.predict(-0.5)),
            end=axes.c2p(12, linear_regression.predict(12)),
            color=ManimColor(COLORS.CYAN),
            stroke_width=3,
        )

        self.play(Create(linear_line), run_time=linear_fail_duration * 0.3)

        # Show MASSIVE red residual lines
        error_bars = self._create_massive_error_bars(points, linear_regression, axes)
        self.play(Create(error_bars), run_time=linear_fail_duration * 0.4)
        self.wait(linear_fail_duration * 0.3)

        # Phase 4: Line BENDS into hill shape, errors disappear (1:30-1:35)
        # Create the hill-shaped curve that fits the dose-response data
        hill_curve = self._create_hill_curve(axes)

        # Fade out error bars as line transforms
        self.play(
            FadeOut(error_bars),
            Transform(linear_line, hill_curve),
            run_time=bend_duration * 0.7,
        )
        self.wait(bend_duration * 0.3)

        # Phase 5: Show "NON-LINEAR REGRESSION" text and fade out (1:35-1:40)
        conclusion_text = Text(
            "NON-LINEAR REGRESSION",
            font_size=36,
            color=ManimColor(COLORS.CYAN),
            weight="BOLD",
        )
        conclusion_text.to_edge(DOWN, buff=0.5)

        self.play(Write(conclusion_text), run_time=conclusion_duration * 0.5)
        self.wait(conclusion_duration * 0.2)

        # Fade out everything
        all_content = VGroup(axes, point_mobjects, linear_line, conclusion_text)
        self.play(FadeOut(all_content), run_time=conclusion_duration * 0.3)

    def _create_dose_response_axes(self) -> Axes:
        """Create axes labeled for drug dosage vs patient health.

        Returns:
            Axes mobject with "Drug Dosage" and "Patient Health" labels.

        """
        axes = Axes(
            x_range=[0, 11, 1],
            y_range=[0, 10, 2],
            x_length=10,
            y_length=6,
            axis_config={
                "color": ManimColor(COLORS.GRID),
                "include_tip": True,
                "tip_length": 0.2,
            },
            x_axis_config={"numbers_to_include": [2, 4, 6, 8, 10]},
            y_axis_config={"numbers_to_include": [2, 4, 6, 8]},
        )

        # Add axis labels
        x_label = Text("Drug Dosage", font_size=24, color=ManimColor(COLORS.TEXT))
        x_label.next_to(axes.x_axis, DOWN, buff=0.3)

        y_label = Text("Patient Health", font_size=24, color=ManimColor(COLORS.TEXT))
        y_label.next_to(axes.y_axis, LEFT, buff=0.3)
        y_label.rotate(90 * math.pi / 180)

        axes.add(x_label, y_label)
        axes.center()

        return axes

    def _generate_dose_response_data(self) -> list[DataPoint]:
        """Generate pharmacological dose-response data pattern.

        Creates data that rises steeply, plateaus (saturation),
        then crashes (toxicity) - the biological reality.

        Returns:
            List of DataPoint objects following dose-response curve.

        """
        points: list[DataPoint] = []

        # Generate hill-shaped dose-response curve with some noise
        x_values = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

        for x in x_values:
            # Dose-response: rises, saturates, then crashes (toxicity)
            # Therapeutic effect (rises and saturates)
            therapeutic = 8.0 * (1.0 - math.exp(-0.6 * x))
            # Toxicity kicks in at higher doses (quadratic crash)
            toxicity = 0.15 * max(0.0, x - 4.0) ** 2
            y = max(0.5, therapeutic - toxicity)

            # Add small noise for realism
            noise = 0.3 * math.sin(x * 2.5)
            y = max(0.5, y + noise)

            points.append(DataPoint(x=x, y=y))

        return points

    def _create_data_point_mobjects(
        self,
        points: list[DataPoint],
        axes: Axes,
    ) -> VGroup:
        """Create dot mobjects for each data point.

        Args:
            points: List of data points.
            axes: Axes to position dots on.

        Returns:
            VGroup containing all dot mobjects.

        """
        dots = VGroup()

        for point in points:
            pos = axes.c2p(point.x, point.y)
            dot = Dot(
                point=pos,
                radius=0.08,
                color=ManimColor(COLORS.TEXT),
                fill_opacity=1.0,
            )
            dots.add(dot)

        return dots

    def _create_massive_error_bars(
        self,
        points: list[DataPoint],
        regression: object,
        axes: Axes,
    ) -> VGroup:
        """Create MASSIVE red error bars showing linear failure.

        The linear model predicts completely wrong values for the
        dose-response curve, especially at high doses where it
        suggests "infinite dose = infinite health".

        Args:
            points: List of data points.
            regression: Linear regression model with predict() method.
            axes: Axes for coordinate conversion.

        Returns:
            VGroup of thick red error bar lines.

        """
        bars = VGroup()

        for point in points:
            predicted_y = regression.predict(point.x)  # type: ignore[union-attr]

            start = axes.c2p(point.x, point.y)
            end = axes.c2p(point.x, predicted_y)

            # MASSIVE thick red bars to emphasize failure
            bar = Line(
                start=start,
                end=end,
                color=ManimColor(COLORS.RED),
                stroke_width=5,
                stroke_opacity=0.9,
            )
            bars.add(bar)

        return bars

    def _create_hill_curve(self, axes: Axes) -> ParametricFunction:
        """Create the hill-shaped curve that fits dose-response data.

        The curve rises, plateaus (saturation), then crashes (toxicity).

        Args:
            axes: Axes for coordinate conversion.

        Returns:
            ParametricFunction representing the hill curve.

        """

        def hill_function(x: float) -> float:
            """Dose-response hill function."""
            # Therapeutic effect (rises and saturates)
            therapeutic = 8.0 * (1.0 - math.exp(-0.6 * x))
            # Toxicity kicks in at higher doses
            toxicity = 0.15 * max(0.0, x - 4.0) ** 2
            return max(0.5, therapeutic - toxicity)

        return ParametricFunction(
            lambda t: axes.c2p(t, hill_function(t)),
            t_range=[0.3, 10.5],
            color=ManimColor(COLORS.CYAN),
            stroke_width=3,
        )

    def get_duration(self) -> float:
        """Return scene duration."""
        return self.END_TIME - self.START_TIME
