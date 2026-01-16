"""Example scene demonstrating manim-voiceover integration."""

from __future__ import annotations

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


class VoiceoverDemo(VoiceoverScene):
    """Demonstrates basic voiceover functionality with Manim animations."""

    def construct(self) -> None:
        """Create an animated scene with synchronized voiceover narration."""
        # Initialize Google Text-to-Speech service
        self.set_speech_service(GTTSService())

        # Create title
        title = Text("Manim Voiceover Demo", font_size=48)

        with self.voiceover(text="Welcome to Manim Voiceover!") as tracker:
            self.play(Write(title), run_time=tracker.duration)

        self.wait(0.5)

        # Create and animate a circle
        with self.voiceover(
            text="Let's create a beautiful circle that grows as I speak.",
            subcaption="Watch the circle appear!"
        ) as tracker:
            self.play(FadeOut(title))
            circle = Circle(radius=2, color=BLUE, fill_opacity=0.5)
            self.play(Create(circle), run_time=tracker.duration)

        # Transform to square
        with self.voiceover(
            text="Now we'll transform this circle into a square."
        ) as tracker:
            square = Square(side_length=4, color=GREEN, fill_opacity=0.5)
            self.play(Transform(circle, square), run_time=tracker.duration)

        # Final message
        with self.voiceover(
            text="This is just the beginning of what you can do with Manim Voiceover!"
        ) as tracker:
            final_text = Text("The possibilities are endless!", font_size=36)
            self.play(
                FadeOut(circle),
                Write(final_text),
                run_time=tracker.duration
            )

        self.wait(1)


class MLConceptWithVoiceover(VoiceoverScene):
    """Demonstrates ML concept explanation with voiceover."""

    def construct(self) -> None:
        """Explain a simple ML concept with synchronized animations and voice."""
        self.set_speech_service(GTTSService())

        # Introduction
        title = Text("Linear Regression", font_size=48, color=YELLOW)

        with self.voiceover(
            text="Let's explore linear regression, a fundamental machine learning algorithm."
        ) as tracker:
            self.play(Write(title), run_time=tracker.duration)

        self.wait(0.3)
        self.play(FadeOut(title))

        # Create axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=7,
            y_length=5,
            axis_config={"color": BLUE}
        )

        # Add labels
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y", edge=LEFT, direction=LEFT)

        with self.voiceover(
            text="We start by plotting our data points on a coordinate system."
        ) as tracker:
            self.play(
                Create(axes),
                Write(x_label),
                Write(y_label),
                run_time=tracker.duration
            )

        # Add data points
        points_data = [(2, 3), (3, 4), (5, 6), (7, 7), (8, 9)]
        dots = VGroup(*[
            Dot(axes.coords_to_point(x, y), color=RED)
            for x, y in points_data
        ])

        with self.voiceover(
            text="Here are our sample data points scattered across the graph."
        ) as tracker:
            self.play(Create(dots), run_time=tracker.duration)

        # Add regression line
        line = axes.plot(
            lambda x: 1.2 * x + 0.5,
            color=GREEN,
            x_range=[1, 9]
        )

        with self.voiceover(
            text="Linear regression finds the best fitting line through these points."
        ) as tracker:
            self.play(Create(line), run_time=tracker.duration)

        # Highlight the relationship
        equation = MathTex(
            r"y = mx + b",
            font_size=40,
            color=GREEN
        ).to_edge(UP)

        with self.voiceover(
            text="The line follows the equation y equals m x plus b, "
            "where m is the slope and b is the intercept."
        ) as tracker:
            self.play(Write(equation), run_time=tracker.duration)

        self.wait(2)
