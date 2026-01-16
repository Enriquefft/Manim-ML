"""Color utility functions for Manim video production.

Provides helper functions for converting between color formats and
applying color transformations. All base color values come from
src.config.COLORS to maintain single source of truth.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from src.config import COLORS

if TYPE_CHECKING:
    from manim import ManimColor, Mobject


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """Convert hex color string to RGB tuple.

    Args:
        hex_color: Color in format "#RRGGBB" (e.g., "#00F0FF")

    Returns:
        Tuple of (red, green, blue) values in range 0-255

    Raises:
        ValueError: If hex_color is not in valid format

    """
    hex_color = hex_color.lstrip("#")
    if len(hex_color) != 6:
        msg = f"Invalid hex color format: {hex_color}"
        raise ValueError(msg)
    return (
        int(hex_color[0:2], 16),
        int(hex_color[2:4], 16),
        int(hex_color[4:6], 16),
    )


def hex_to_rgb_normalized(hex_color: str) -> tuple[float, float, float]:
    """Convert hex color string to normalized RGB tuple.

    Args:
        hex_color: Color in format "#RRGGBB" (e.g., "#00F0FF")

    Returns:
        Tuple of (red, green, blue) values in range 0.0-1.0

    """
    r, g, b = hex_to_rgb(hex_color)
    return (r / 255.0, g / 255.0, b / 255.0)


def rgb_to_hex(r: int, g: int, b: int) -> str:
    """Convert RGB values to hex color string.

    Args:
        r: Red component (0-255)
        g: Green component (0-255)
        b: Blue component (0-255)

    Returns:
        Hex color string in format "#RRGGBB"

    """
    return f"#{r:02X}{g:02X}{b:02X}"


def get_manim_color(hex_color: str) -> Any:
    """Convert hex color to Manim-compatible color.

    Args:
        hex_color: Color in format "#RRGGBB"

    Returns:
        ManimColor instance for use in Manim animations

    """
    from manim import ManimColor

    return ManimColor(hex_color)


def get_background_color() -> Any:
    """Get the standard background color for scenes.

    Returns:
        ManimColor for the dark void background (#0D0D0D)

    """
    return get_manim_color(COLORS.BACKGROUND)


def get_text_color() -> Any:
    """Get the standard text/foreground color.

    Returns:
        ManimColor for primary text (#F2F2F2)

    """
    return get_manim_color(COLORS.TEXT)


def get_cyan_color() -> Any:
    """Get the cyan accent color for regression lines and highlights.

    Returns:
        ManimColor for cyan (#00F0FF)

    """
    return get_manim_color(COLORS.CYAN)


def get_red_color() -> Any:
    """Get the red color for errors and warnings.

    Returns:
        ManimColor for red (#FF2A2A)

    """
    return get_manim_color(COLORS.RED)


def get_gold_color() -> Any:
    """Get the gold color for final synthesis highlight.

    Returns:
        ManimColor for gold (#FFD700)

    """
    return get_manim_color(COLORS.GOLD)


def get_grid_color() -> Any:
    """Get the color for grid lines.

    Returns:
        ManimColor for grid (#404040)

    """
    return get_manim_color(COLORS.GRID)


def get_green_color() -> Any:
    """Get the green color for terminal cursor.

    Returns:
        ManimColor for green (#00FF00)

    """
    return get_manim_color(COLORS.GREEN)


def interpolate_color(
    color1: str,
    color2: str,
    t: float,
) -> str:
    """Linearly interpolate between two colors.

    Args:
        color1: Starting hex color
        color2: Ending hex color
        t: Interpolation factor (0.0 = color1, 1.0 = color2)

    Returns:
        Interpolated hex color string

    """
    r1, g1, b1 = hex_to_rgb(color1)
    r2, g2, b2 = hex_to_rgb(color2)

    t = max(0.0, min(1.0, t))  # Clamp to [0, 1]

    r = int(r1 + (r2 - r1) * t)
    g = int(g1 + (g2 - g1) * t)
    b = int(b1 + (b2 - b1) * t)

    return rgb_to_hex(r, g, b)


def apply_color_to_mobject(mobject: Any, hex_color: str) -> Any:
    """Apply a hex color to a Manim mobject.

    Args:
        mobject: The Manim object to colorize
        hex_color: Color in format "#RRGGBB"

    Returns:
        The mobject with color applied (for chaining)

    """
    return mobject.set_color(get_manim_color(hex_color))
