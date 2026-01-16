"""Effect function unit tests.

Tests for visual effects including chromatic aberration,
glow effects, pulse animations, and screen edge pulses.

These tests require manim to be available. Skip if not installed.
"""

from __future__ import annotations

import pytest

try:
    from manim import Circle, VGroup

    MANIM_AVAILABLE = True
except ImportError:
    MANIM_AVAILABLE = False
    Circle = None  # type: ignore[assignment, misc]
    VGroup = None  # type: ignore[assignment, misc]


pytestmark = pytest.mark.skipif(not MANIM_AVAILABLE, reason="Manim not available")


if MANIM_AVAILABLE:
    from src.config import COLORS
    from videos.templates.effects import (
        apply_chromatic_aberration,
        apply_glow_effect,
        create_screen_edge_pulse,
        create_static_noise_overlay,
    )


class TestChromaticAberration:
    """Test chromatic aberration effect."""

    def test_creates_vgroup(self) -> None:
        """Verify effect returns a VGroup."""
        circle = Circle(radius=1.0)
        result = apply_chromatic_aberration(circle)
        assert isinstance(result, VGroup)

    def test_contains_multiple_copies(self) -> None:
        """Verify effect creates RGB-shifted copies."""
        circle = Circle(radius=1.0)
        result = apply_chromatic_aberration(circle)
        # Should have red copy, blue copy, and original
        assert len(result) == 3

    def test_custom_offset(self) -> None:
        """Verify custom offset parameter works."""
        circle = Circle(radius=1.0)
        result = apply_chromatic_aberration(circle, offset=0.1)
        assert isinstance(result, VGroup)


class TestGlowEffect:
    """Test glow effect application."""

    def test_creates_vgroup(self) -> None:
        """Verify effect returns a VGroup."""
        circle = Circle(radius=1.0)
        result = apply_glow_effect(circle)
        assert isinstance(result, VGroup)

    def test_contains_glow_layers(self) -> None:
        """Verify effect creates glow layers plus original."""
        circle = Circle(radius=1.0)
        result = apply_glow_effect(circle)
        # Should have 3 glow layers + original = 4 elements
        assert len(result) == 4

    def test_custom_glow_factor(self) -> None:
        """Verify custom glow factor works."""
        circle = Circle(radius=1.0)
        result = apply_glow_effect(circle, glow_factor=2.0)
        assert isinstance(result, VGroup)

    def test_custom_opacity(self) -> None:
        """Verify custom opacity works."""
        circle = Circle(radius=1.0)
        result = apply_glow_effect(circle, opacity=0.5)
        assert isinstance(result, VGroup)


class TestScreenEdgePulse:
    """Test screen edge pulse effect."""

    def test_creates_vgroup(self) -> None:
        """Verify effect returns a VGroup."""
        result = create_screen_edge_pulse()
        assert isinstance(result, VGroup)

    def test_contains_four_edges(self) -> None:
        """Verify effect creates four edge rectangles."""
        result = create_screen_edge_pulse()
        assert len(result) == 4

    def test_custom_color(self) -> None:
        """Verify custom color works."""
        result = create_screen_edge_pulse(color=COLORS.CYAN)
        assert isinstance(result, VGroup)

    def test_starts_invisible(self) -> None:
        """Verify edges start with zero opacity."""
        result = create_screen_edge_pulse()
        for edge in result:
            assert edge.get_fill_opacity() == 0


class TestStaticNoiseOverlay:
    """Test static noise overlay generation."""

    def test_creates_vgroup(self) -> None:
        """Verify overlay returns a VGroup."""
        result = create_static_noise_overlay()
        assert isinstance(result, VGroup)

    def test_default_density(self) -> None:
        """Verify default density creates expected number of dots."""
        result = create_static_noise_overlay(density=100)
        assert len(result) == 100

    def test_custom_dimensions(self) -> None:
        """Verify custom dimensions work."""
        result = create_static_noise_overlay(width=10.0, height=5.0, density=50)
        assert len(result) == 50
