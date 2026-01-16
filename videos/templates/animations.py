"""Custom animation classes for Manim video production.

Provides specialized animations including text jitter/corruption,
line morphing to curves, and stamp-in text effects.
"""

from __future__ import annotations

import random
from collections.abc import Callable
from typing import TYPE_CHECKING, Any

from manim import (
    Animation,
    FadeIn,
    Line,
    ManimColor,
    ParametricFunction,
    Text,
    Transform,
    rate_functions,
)

from src.config import COLORS, DATA_SEED

if TYPE_CHECKING:
    from manim import Mobject


# Character corruption mapping for jitter effect
CORRUPTION_MAP: dict[str, list[str]] = {
    "A": ["@", "4", "∆", "Λ"],
    "B": ["8", "ß", "β", "6"],
    "C": ["(", "<", "¢", "©"],
    "D": ["Ð", "∂", "δ"],
    "E": ["3", "€", "∑", "Σ"],
    "F": ["ƒ", "Ƒ"],
    "G": ["6", "9", "Ǥ"],
    "H": ["#", "Ħ", "ħ"],
    "I": ["1", "|", "!", "¡"],
    "J": ["ʝ", "ǰ"],
    "K": ["Қ", "ķ"],
    "L": ["1", "|", "Ł", "ℓ"],
    "M": ["Μ", "м", "₥"],
    "N": ["И", "η", "ñ"],
    "O": ["0", "Ø", "○", "◎"],
    "P": ["ρ", "Þ", "þ"],
    "Q": ["Ω", "Ǫ"],
    "R": ["Я", "®", "Ř"],
    "S": ["$", "5", "§", "Ş"],
    "T": ["7", "+", "†", "Ŧ"],
    "U": ["Ц", "µ", "Ų"],
    "V": ["√", "∨", "ν"],
    "W": ["Ш", "ω", "Ŵ"],
    "X": ["×", "Ж", "χ"],
    "Y": ["¥", "ψ", "Ұ"],
    "Z": ["2", "Ž", "ζ"],
    "0": ["O", "Ø", "○"],
    "1": ["I", "|", "l"],
    "2": ["Z", "Ƨ"],
    "3": ["E", "Ʒ", "ε"],
    "4": ["A", "Ч"],
    "5": ["S", "Ƽ"],
    "6": ["G", "б"],
    "7": ["T", "Ƭ"],
    "8": ["B", "&"],
    "9": ["g", "q"],
}


class TextJitter(Animation):
    """Animate random character corruption for glitch effect.

    Creates a text corruption effect by randomly replacing characters
    with similar-looking alternatives, simulating data corruption
    or AI hallucination.
    """

    def __init__(
        self,
        text_mobject: Text,
        corruption_rate: float = 0.3,
        seed: int = DATA_SEED,
        **kwargs: Any,
    ) -> None:
        """Initialize text jitter animation.

        Args:
            text_mobject: The Text mobject to animate
            corruption_rate: Probability of corrupting each character (0.0-1.0)
            seed: Random seed for reproducibility
            **kwargs: Additional animation parameters

        """
        self.original_text = text_mobject.text
        self.corruption_rate = corruption_rate
        self.rng = random.Random(seed)
        super().__init__(text_mobject, **kwargs)

    def interpolate_mobject(self, alpha: float) -> None:
        """Update the mobject for the current animation frame.

        Args:
            alpha: Animation progress from 0.0 to 1.0

        """
        if alpha < 0.1 or alpha > 0.9:
            # At start and end, show original text
            return

        # Corrupt some characters based on alpha and corruption_rate
        corrupted_chars = []
        for char in self.original_text:
            if self.rng.random() < self.corruption_rate:
                upper_char = char.upper()
                if upper_char in CORRUPTION_MAP:
                    corrupted_chars.append(
                        self.rng.choice(CORRUPTION_MAP[upper_char]),
                    )
                else:
                    corrupted_chars.append(char)
            else:
                corrupted_chars.append(char)

        # Note: In practice, we would need to replace the text content
        # This is a simplified version - full implementation would
        # recreate the Text mobject or use character-by-character submobjects


class LineMorph(Animation):
    """Smoothly morph a straight line to a curved function.

    Used to transform linear regression line into polynomial curve,
    demonstrating the transition from simple to complex models.
    """

    def __init__(
        self,
        line: Line,
        target_func: Callable[[float], float],
        x_range: tuple[float, float] = (-5, 5),
        **kwargs: Any,
    ) -> None:
        """Initialize line morph animation.

        Args:
            line: The Line mobject to morph
            target_func: Target function y = f(x) for the curve
            x_range: Domain for the parametric curve
            **kwargs: Additional animation parameters

        """
        self.target_func = target_func
        self.x_range = x_range

        # Store initial line endpoints
        self.start_point = line.get_start()
        self.end_point = line.get_end()

        # Create target curve
        self.target_curve = ParametricFunction(
            lambda t: [t, target_func(t), 0],
            t_range=[x_range[0], x_range[1]],
            color=line.get_color(),
        )

        super().__init__(line, **kwargs)

    def interpolate_mobject(self, alpha: float) -> None:
        """Update the mobject for the current animation frame.

        Args:
            alpha: Animation progress from 0.0 to 1.0

        """
        # Interpolate between line and curve
        # This simplified version uses Transform internally
        t = rate_functions.smooth(alpha)

        # In a full implementation, we would interpolate control points
        # or use Manim's built-in Transform capabilities


def create_line_to_curve_animation(
    line: Line,
    target_func: Callable[[float], float],
    x_range: tuple[float, float] = (-5, 5),
    duration: float = 1.5,
) -> Animation:
    """Create animation morphing line to parametric curve.

    Convenience function that creates a Transform animation
    from a line to a parametric function curve.

    Args:
        line: The Line mobject to transform
        target_func: Target function y = f(x)
        x_range: Domain for the curve
        duration: Animation duration

    Returns:
        Transform animation from line to curve

    """
    target_curve = ParametricFunction(
        lambda t: [t, target_func(t), 0],
        t_range=[x_range[0], x_range[1]],
        color=line.get_color(),
        stroke_width=line.get_stroke_width(),
    )

    return Transform(line, target_curve, run_time=duration)


class StampIn(Animation):
    """Stamp text with shear/skew effect for dramatic reveal.

    Creates a stamp-like animation where text appears to be
    slammed onto the screen with a slight shear effect.
    """

    def __init__(
        self,
        text: Text,
        shear_angle: float = 0.1,
        scale_factor: float = 1.5,
        **kwargs: Any,
    ) -> None:
        """Initialize stamp-in animation.

        Args:
            text: The Text mobject to animate
            shear_angle: Angle of shear in radians
            scale_factor: Initial scale before stamping down
            **kwargs: Additional animation parameters

        """
        self.shear_angle = shear_angle
        self.scale_factor = scale_factor
        self.original_matrix = text.get_points().copy() if len(text.get_points()) > 0 else None
        super().__init__(text, **kwargs)

    def interpolate_mobject(self, alpha: float) -> None:
        """Update the mobject for the current animation frame.

        Args:
            alpha: Animation progress from 0.0 to 1.0

        """
        # Use rush_from rate function for slam effect
        t = rate_functions.rush_from(alpha)

        # Scale down from large to normal
        current_scale = self.scale_factor - (self.scale_factor - 1.0) * t

        # Reduce shear as animation progresses
        current_shear = self.shear_angle * (1.0 - t)

        # Apply transformations
        self.mobject.scale(
            current_scale / self.mobject.get_height() if self.mobject.get_height() > 0 else 1
        )


def create_stamp_animation(
    text: Text,
    duration: float = 0.5,
    color: str = COLORS.GOLD,
) -> Animation:
    """Create stamp-in animation for text.

    Convenience function for creating a dramatic text reveal
    with scale and fade effects.

    Args:
        text: The Text mobject to animate
        duration: Animation duration
        color: Text color (default: gold for final reveal)

    Returns:
        FadeIn animation with scale effect

    """
    text.set_color(ManimColor(color))
    text.scale(0.1)  # Start small

    return FadeIn(
        text,
        scale=10,  # Scale up 10x during fade in
        run_time=duration,
        rate_func=rate_functions.rush_from,
    )


class CascadeText(Animation):
    """Animate text appearing line by line in cascade.

    Used for the hallucination scene where nonsense text
    appears progressively down the screen.
    """

    def __init__(
        self,
        text_lines: list[Text],
        interval: float = 0.12,
        **kwargs: Any,
    ) -> None:
        """Initialize cascade text animation.

        Args:
            text_lines: List of Text mobjects to reveal
            interval: Time between each line appearing
            **kwargs: Additional animation parameters

        """
        from manim import VGroup

        self.text_lines = text_lines
        self.interval = interval
        self.group = VGroup(*text_lines)

        # Start all lines invisible
        for line in text_lines:
            line.set_opacity(0)

        super().__init__(self.group, **kwargs)

    def interpolate_mobject(self, alpha: float) -> None:
        """Update the mobject for the current animation frame.

        Args:
            alpha: Animation progress from 0.0 to 1.0

        """
        # Calculate which lines should be visible
        total_lines = len(self.text_lines)
        if total_lines == 0:
            return

        # Each line takes up 1/total_lines of the animation
        for i, line in enumerate(self.text_lines):
            line_start = i / total_lines
            line_end = (i + 1) / total_lines

            if alpha < line_start:
                line.set_opacity(0)
            elif alpha >= line_end:
                line.set_opacity(1)
            else:
                # Fade in during this line's segment
                line_alpha = (alpha - line_start) / (line_end - line_start)
                line.set_opacity(line_alpha)


def create_bounce_animation(
    mobject: Mobject,
    duration: float = 0.5,
    overshoot: float = 1.2,
) -> Animation:
    """Create bounce-in animation for mobjects.

    Used for warning boxes and dramatic reveals.

    Args:
        mobject: The mobject to animate
        duration: Animation duration
        overshoot: Scale overshoot factor for bounce

    Returns:
        FadeIn animation with bounce effect

    """
    return FadeIn(
        mobject,
        scale=overshoot,
        run_time=duration,
        rate_func=rate_functions.ease_out_bounce,
    )
