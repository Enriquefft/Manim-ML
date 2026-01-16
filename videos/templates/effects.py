"""Visual effects for Manim video production.

Provides reusable effect functions including chromatic aberration,
glow effects, pulse animations, and dolly zoom camera effects.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    Animation,
    FadeIn,
    FadeOut,
    Mobject,
    MovingCameraScene,
    ScaleInPlace,
    VGroup,
    rate_functions,
)

from src.config import COLORS, TIMING

if TYPE_CHECKING:
    from manim import Scene


def apply_chromatic_aberration(
    mobject: Mobject,
    offset: float = 0.02,
) -> VGroup:
    """Create RGB-split chromatic aberration effect on mobject.

    Creates the effect by overlaying RGB-shifted copies of the target
    mobject with offset positions, simulating lens distortion.

    Args:
        mobject: The Manim object to apply effect to
        offset: Pixel offset for RGB channels (default: 0.02)

    Returns:
        VGroup containing original and RGB-shifted copies

    """
    # Create RGB-shifted copies
    red_copy = mobject.copy()
    red_copy.set_color("#FF0000")
    red_copy.set_opacity(0.3)
    red_copy.shift(LEFT * offset + UP * offset * 0.5)

    blue_copy = mobject.copy()
    blue_copy.set_color("#0000FF")
    blue_copy.set_opacity(0.3)
    blue_copy.shift(RIGHT * offset + DOWN * offset * 0.5)

    # Combine with original on top
    result = VGroup(red_copy, blue_copy, mobject)
    return result


def apply_glow_effect(
    mobject: Mobject,
    glow_factor: float = 1.5,
    opacity: float = 0.3,
    color: str | None = None,
) -> VGroup:
    """Add outer glow to mobject.

    Creates glow by placing scaled, semi-transparent copies
    behind the original mobject.

    Args:
        mobject: The Manim object to add glow to
        glow_factor: Scale factor for glow layers (default: 1.5)
        opacity: Opacity of glow layers (default: 0.3)
        color: Optional glow color (defaults to mobject color)

    Returns:
        VGroup containing glow layers and original mobject

    """
    glow_layers = VGroup()

    # Create multiple glow layers for smooth falloff
    num_layers = 3
    for i in range(num_layers):
        layer_scale = 1.0 + (glow_factor - 1.0) * (i + 1) / num_layers
        layer_opacity = opacity * (num_layers - i) / num_layers

        glow = mobject.copy()
        glow.scale(layer_scale)
        glow.set_opacity(layer_opacity)
        if color:
            glow.set_color(color)
        glow_layers.add(glow)

    # Add original on top
    glow_layers.add(mobject)
    return glow_layers


def create_pulse_animation(
    mobject: Mobject,
    scale_factor: float = 1.1,
    duration: float = 0.5,
) -> Animation:
    """Create pulsing scale animation.

    Animates the mobject to scale up and back down, creating
    a breathing/pulse effect.

    Args:
        mobject: The Manim object to animate
        scale_factor: Maximum scale during pulse (default: 1.1)
        duration: Duration of one pulse cycle (default: 0.5s)

    Returns:
        Animation object for the pulse effect

    """
    return ScaleInPlace(
        mobject,
        scale_factor,
        rate_func=rate_functions.there_and_back,
        run_time=duration,
    )


def create_fade_pulse(
    mobject: Mobject,
    min_opacity: float = 0.5,
    max_opacity: float = 1.0,
    duration: float = 0.5,
) -> Animation:
    """Create opacity pulsing animation.

    Args:
        mobject: The Manim object to animate
        min_opacity: Minimum opacity during pulse
        max_opacity: Maximum opacity during pulse
        duration: Duration of one pulse cycle

    Returns:
        Animation object for the fade pulse

    """
    # Store original opacity
    original_opacity = mobject.get_fill_opacity()

    def update_opacity(mob: Mobject, alpha: float) -> None:
        # Use there_and_back for smooth pulse
        t = rate_functions.there_and_back(alpha)
        new_opacity = min_opacity + (max_opacity - min_opacity) * t
        mob.set_opacity(new_opacity)

    from manim import UpdateFromAlphaFunc

    return UpdateFromAlphaFunc(mobject, update_opacity, run_time=duration)


def create_dolly_zoom(
    scene: MovingCameraScene,
    target: Mobject,
    duration: float = 1.0,
    zoom_factor: float = 0.5,
) -> None:
    """Create Hitchcock dolly zoom effect.

    Animates camera focal length while simultaneously translating position,
    creating a vertigo-inducing effect where the subject stays the same
    size but the background appears to shift.

    Note: This function directly plays the animation on the scene.
    It should be called during the construct() method.

    Args:
        scene: The MovingCameraScene to apply effect to
        target: The mobject to keep centered during effect
        duration: Duration of the dolly zoom (default: 1.0s)
        zoom_factor: Amount to zoom (< 1 zooms in, > 1 zooms out)

    """
    camera = scene.camera.frame

    # Store initial state
    initial_width = camera.width
    target_width = initial_width * zoom_factor

    # Calculate positions
    target_center = target.get_center()

    # Animate camera zoom and position simultaneously
    scene.play(
        camera.animate.set_width(target_width).move_to(target_center),
        run_time=duration,
        rate_func=rate_functions.smooth,
    )


def create_screen_edge_pulse(
    color: str = COLORS.RED,
    pulse_count: int = 3,
    duration: float = 0.3,
) -> VGroup:
    """Create pulsing edges around the screen.

    Used to indicate errors or warnings with red screen edge flashes.

    Args:
        color: Color for the edge pulse (default: red)
        pulse_count: Number of pulses
        duration: Duration of each pulse

    Returns:
        VGroup containing edge rectangles for animation

    """
    from manim import ManimColor, Rectangle

    edges = VGroup()

    # Create thin rectangles along each edge
    edge_width = 0.1

    # Top edge
    top = Rectangle(
        width=16,
        height=edge_width,
        color=ManimColor(color),
        fill_opacity=0.8,
    )
    top.move_to([0, 4 - edge_width / 2, 0])
    edges.add(top)

    # Bottom edge
    bottom = Rectangle(
        width=16,
        height=edge_width,
        color=ManimColor(color),
        fill_opacity=0.8,
    )
    bottom.move_to([0, -4 + edge_width / 2, 0])
    edges.add(bottom)

    # Left edge
    left = Rectangle(
        width=edge_width,
        height=8,
        color=ManimColor(color),
        fill_opacity=0.8,
    )
    left.move_to([-7.5 + edge_width / 2, 0, 0])
    edges.add(left)

    # Right edge
    right = Rectangle(
        width=edge_width,
        height=8,
        color=ManimColor(color),
        fill_opacity=0.8,
    )
    right.move_to([7.5 - edge_width / 2, 0, 0])
    edges.add(right)

    edges.set_opacity(0)  # Start invisible
    return edges


def animate_screen_pulse(
    scene: Scene,
    edges: VGroup,
    pulse_count: int = 3,
    duration: float = 0.3,
) -> None:
    """Animate screen edge pulsing effect.

    Args:
        scene: The scene to play animation on
        edges: VGroup from create_screen_edge_pulse
        pulse_count: Number of pulses to play
        duration: Duration of each pulse

    """
    for _ in range(pulse_count):
        scene.play(
            FadeIn(edges, run_time=duration / 2),
        )
        scene.play(
            FadeOut(edges, run_time=duration / 2),
        )


def create_static_noise_overlay(
    width: float = 16.0,
    height: float = 9.0,
    density: int = 1000,
) -> VGroup:
    """Create static noise effect overlay.

    Generates random dots to simulate TV static/noise effect.

    Args:
        width: Width of the noise overlay
        height: Height of the noise overlay
        density: Number of noise dots

    Returns:
        VGroup containing noise dots

    """
    import numpy as np
    from manim import Dot, ManimColor

    rng = np.random.default_rng(42)
    noise = VGroup()

    for _ in range(density):
        x = rng.uniform(-width / 2, width / 2)
        y = rng.uniform(-height / 2, height / 2)
        brightness = rng.uniform(0.3, 1.0)

        dot = Dot(
            point=[x, y, 0],
            radius=0.02,
            color=ManimColor(COLORS.TEXT),
            fill_opacity=brightness,
        )
        noise.add(dot)

    return noise


def transition_fade(
    scene: Scene,
    out_mobjects: list[Mobject],
    in_mobjects: list[Mobject],
    overlap: float | None = None,
) -> None:
    """Perform smooth fade transition between mobject groups.

    Args:
        scene: The scene to play animation on
        out_mobjects: Mobjects to fade out
        in_mobjects: Mobjects to fade in
        overlap: Transition overlap duration (defaults to TIMING.SCENE_TRANSITION)

    """
    if overlap is None:
        overlap = TIMING.SCENE_TRANSITION

    # Fade out old content
    if out_mobjects:
        scene.play(
            *[FadeOut(m) for m in out_mobjects],
            run_time=overlap,
        )

    # Fade in new content
    if in_mobjects:
        scene.play(
            *[FadeIn(m) for m in in_mobjects],
            run_time=overlap,
        )
