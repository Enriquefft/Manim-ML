"""Custom shape primitives for Manim video production.

Provides reusable shape components including warning icons, sliders,
and neural network nodes. All shapes are generated programmatically
using Manim primitives per FR-012 requirement.
"""

from __future__ import annotations

from manim import (
    UP,
    Circle,
    Line,
    ManimColor,
    Polygon,
    Rectangle,
    Text,
    VGroup,
)

from src.config import COLORS


def create_warning_icon(
    size: float = 1.0,
    color: str = COLORS.RED,
) -> VGroup:
    """Create a warning triangle with exclamation mark.

    Generates the icon programmatically using Manim primitives,
    satisfying FR-012 requirement for vector/code-based generation.

    Args:
        size: Scale factor for the icon (default: 1.0)
        color: Hex color for the icon (default: red)

    Returns:
        VGroup containing the warning triangle and exclamation mark

    """
    # Create equilateral triangle pointing up
    triangle_height = size * 0.866  # height of equilateral triangle
    triangle = Polygon(
        [-size / 2, -triangle_height / 3, 0],
        [size / 2, -triangle_height / 3, 0],
        [0, 2 * triangle_height / 3, 0],
        color=ManimColor(color),
        stroke_width=3 * size,
    )
    triangle.set_fill(ManimColor(COLORS.BACKGROUND), opacity=0.8)

    # Create exclamation mark
    exclaim_line = Line(
        start=[0, triangle_height / 4, 0],
        end=[0, -triangle_height / 8, 0],
        color=ManimColor(color),
        stroke_width=4 * size,
    )

    exclaim_dot = Circle(
        radius=0.05 * size,
        color=ManimColor(color),
        fill_opacity=1.0,
    )
    exclaim_dot.move_to([0, -triangle_height / 4, 0])

    # Combine into group
    warning_icon = VGroup(triangle, exclaim_line, exclaim_dot)
    return warning_icon


def create_slider_component(
    height: float = 4.0,
    width: float = 0.3,
    top_color: str = COLORS.CYAN,
    bottom_color: str = COLORS.RED,
) -> VGroup:
    """Create a vertical gradient slider with handle.

    The slider displays a gradient from top_color to bottom_color,
    with a draggable handle for value indication.

    Args:
        height: Slider track height
        width: Slider track width
        top_color: Color at top of gradient (typically cyan)
        bottom_color: Color at bottom of gradient (typically red)

    Returns:
        VGroup containing track, gradient overlay, handle, and labels.
        The handle can be accessed via result[2] for animation.

    """
    # Create track background
    track = Rectangle(
        height=height,
        width=width,
        color=ManimColor(COLORS.GRID),
        fill_opacity=0.3,
        stroke_width=2,
    )

    # Create gradient segments (approximation of gradient)
    num_segments = 20
    segment_height = height / num_segments
    gradient_segments = VGroup()

    for i in range(num_segments):
        # Interpolate color from top to bottom
        t = i / (num_segments - 1)
        # Simple linear interpolation in hex
        top_rgb = _hex_to_rgb(top_color)
        bottom_rgb = _hex_to_rgb(bottom_color)
        r = int(top_rgb[0] + (bottom_rgb[0] - top_rgb[0]) * t)
        g = int(top_rgb[1] + (bottom_rgb[1] - top_rgb[1]) * t)
        b = int(top_rgb[2] + (bottom_rgb[2] - top_rgb[2]) * t)
        segment_color = f"#{r:02X}{g:02X}{b:02X}"

        segment = Rectangle(
            height=segment_height,
            width=width * 0.8,
            color=ManimColor(segment_color),
            fill_opacity=0.8,
            stroke_width=0,
        )
        segment.move_to([0, height / 2 - segment_height / 2 - i * segment_height, 0])
        gradient_segments.add(segment)

    # Create handle
    handle = Circle(
        radius=width * 0.8,
        color=ManimColor(COLORS.TEXT),
        fill_opacity=1.0,
        stroke_width=2,
    )
    handle.move_to([0, height / 4, 0])  # Start at 75% position

    # Combine into group
    slider = VGroup(track, gradient_segments, handle)
    return slider


def create_slider_with_labels(
    height: float = 4.0,
    width: float = 0.3,
    top_label: str = "1.0",
    bottom_label: str = "0.0",
    top_color: str = COLORS.CYAN,
    bottom_color: str = COLORS.RED,
) -> VGroup:
    """Create a slider with top and bottom labels.

    Args:
        height: Slider track height
        width: Slider track width
        top_label: Text label at top of slider
        bottom_label: Text label at bottom of slider
        top_color: Color at top of gradient
        bottom_color: Color at bottom of gradient

    Returns:
        VGroup containing slider and labels.
        Slider is at index 0, labels at indices 1 and 2.

    """
    slider = create_slider_component(height, width, top_color, bottom_color)

    # Create labels
    top_text = Text(top_label, font_size=24, color=ManimColor(COLORS.TEXT))
    top_text.next_to(slider, UP, buff=0.2)

    bottom_text = Text(bottom_label, font_size=24, color=ManimColor(COLORS.TEXT))
    bottom_text.next_to(slider, direction=-UP, buff=0.2)

    return VGroup(slider, top_text, bottom_text)


def create_network_node(
    radius: float = 0.02,
    color: str = COLORS.CYAN,
    symbol: str | None = None,
) -> VGroup:
    """Create a neural network node with optional internal symbol.

    Args:
        radius: Node circle radius
        color: Node color as hex string
        symbol: Optional symbol to display inside node (e.g., "σ")

    Returns:
        VGroup containing the node circle and optional symbol

    """
    # Create outer circle
    node = Circle(
        radius=radius,
        color=ManimColor(color),
        fill_opacity=0.8,
        stroke_width=1,
    )

    # Add glow effect by creating a larger, faded circle behind
    glow = Circle(
        radius=radius * 1.5,
        color=ManimColor(color),
        fill_opacity=0.2,
        stroke_width=0,
    )

    result = VGroup(glow, node)

    # Add symbol if provided
    if symbol:
        text = Text(symbol, font_size=int(radius * 600), color=ManimColor(COLORS.TEXT))
        text.move_to(node.get_center())
        result.add(text)

    return result


def create_sigma_node(
    radius: float = 0.3,
    color: str = COLORS.CYAN,
) -> VGroup:
    """Create a neural network node with sigma (σ) activation symbol.

    Used in synthesis scene when compressing curve to single neuron.

    Args:
        radius: Node circle radius
        color: Node color as hex string

    Returns:
        VGroup containing node with sigma symbol

    """
    return create_network_node(radius=radius, color=color, symbol="σ")


def create_data_point_dot(
    radius: float = 0.08,
    color: str = COLORS.TEXT,
) -> Circle:
    """Create a data point visualization dot.

    Args:
        radius: Dot radius
        color: Dot color as hex string

    Returns:
        Circle representing a data point

    """
    return Circle(
        radius=radius,
        color=ManimColor(color),
        fill_opacity=1.0,
        stroke_width=0,
    )


def create_grid_background(
    x_range: tuple[float, float] = (-7, 7),
    y_range: tuple[float, float] = (-4, 4),
    x_step: float = 1.0,
    y_step: float = 1.0,
) -> VGroup:
    """Create a faint grid background for charts.

    Args:
        x_range: Tuple of (min_x, max_x) for grid extent
        y_range: Tuple of (min_y, max_y) for grid extent
        x_step: Spacing between vertical grid lines
        y_step: Spacing between horizontal grid lines

    Returns:
        VGroup containing all grid lines

    """
    grid = VGroup()

    # Vertical lines
    x = x_range[0]
    while x <= x_range[1]:
        line = Line(
            start=[x, y_range[0], 0],
            end=[x, y_range[1], 0],
            color=ManimColor(COLORS.GRID),
            stroke_width=0.5,
            stroke_opacity=0.3,
        )
        grid.add(line)
        x += x_step

    # Horizontal lines
    y = y_range[0]
    while y <= y_range[1]:
        line = Line(
            start=[x_range[0], y, 0],
            end=[x_range[1], y, 0],
            color=ManimColor(COLORS.GRID),
            stroke_width=0.5,
            stroke_opacity=0.3,
        )
        grid.add(line)
        y += y_step

    return grid


def _hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """Convert hex color to RGB tuple (internal helper).

    Args:
        hex_color: Color in format "#RRGGBB"

    Returns:
        Tuple of (r, g, b) values in range 0-255

    """
    hex_color = hex_color.lstrip("#")
    return (
        int(hex_color[0:2], 16),
        int(hex_color[2:4], 16),
        int(hex_color[4:6], 16),
    )
