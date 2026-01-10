"""Example Manim scene demonstrating two advanced features.

This module shows:
1. ValueTracker with add_updater for dynamic mathematical expressions
2. AnimationGroup with smooth shape transformations
"""

from __future__ import annotations

from manim import (
    AnimationGroup,
    Circle,
    FadeIn,
    FadeOut,
    MathTex,
    Scene,
    Square,
    ValueTracker,
    rate_functions,
)


class DynamicMathExample(Scene):
    """Demonstrates ValueTracker with add_updater for dynamic expressions."""

    def construct(self) -> None:
        """Construct the scene with dynamic mathematical expression."""
        # Create a value tracker that will change from 1 to 3
        x_tracker: ValueTracker = ValueTracker(1.0)

        # Create a MathTex that depends on the tracker value
        math_expr: MathTex = MathTex(r"f(x) = x^2")
        math_expr.shift([-2, 2, 0])

        result_expr: MathTex = MathTex("= 1")
        result_expr.shift([2, 2, 0])

        # Update the result whenever the tracker changes
        def update_result(mob: MathTex) -> MathTex:
            """Update result expression based on tracker value."""
            x_val: float = x_tracker.get_value()
            result: float = x_val**2
            new_expr: MathTex = MathTex(f"= {result:.1f}")
            new_expr.move_to(result_expr)
            return new_expr

        result_expr.add_updater(update_result)  # type: ignore[arg-type]

        self.add(math_expr, result_expr)
        self.wait(0.5)

        # Animate the tracker from 1 to 3
        self.play(
            x_tracker.animate.set_value(3.0),
            rate_func=rate_functions.ease_in_out_quad,
            run_time=3,
        )

        self.wait(1)


class ShapeMorphingExample(Scene):
    """Demonstrates smooth shape morphing and animation."""

    def construct(self) -> None:
        """Construct the scene with shape morphing animation."""
        # Create initial shape
        circle: Circle = Circle(radius=1.0, color="BLUE")
        circle.shift([-3, 0, 0])

        # Create target shape
        square: Square = Square(side_length=2.0, color="RED")
        square.shift([3, 0, 0])

        # Add title
        title: MathTex = MathTex(r"\text{Shape Morphing}")
        title.shift([0, 3, 0])

        self.add(title, circle, square)
        self.wait(1)

        # Morph circle to square using intermediate shape
        intermediate: Circle = Circle(radius=1.0, color="GREEN")
        intermediate.shift([0, 0, 0])

        animation_group: AnimationGroup = AnimationGroup(
            FadeIn(intermediate),
            circle.animate.shift([3, 0, 0]),
            square.animate.shift([-3, 0, 0]),
            lag_ratio=0.2,
        )

        self.play(animation_group, run_time=2)
        self.wait(1)

        # Fade out all objects
        self.play(FadeOut(circle, square, intermediate, title))
        self.wait(0.5)
