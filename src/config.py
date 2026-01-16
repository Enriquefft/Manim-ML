"""Central configuration for The Judge & The Curve video.

This module provides the single source of truth for all configuration values
used across scenes, including colors, timing constants, and scene boundaries.
All color values and timing parameters MUST be imported from this module.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final


@dataclass(frozen=True)
class ColorPalette:
    """Central color palette for all video scenes.

    All color values are 6-digit hex codes. Do not hardcode hex values
    in scene files - always reference this palette.
    """

    BACKGROUND: str = "#0D0D0D"
    """Main dark void background."""

    TEXT: str = "#F2F2F2"
    """Primary text/foreground color."""

    CYAN: str = "#00F0FF"
    """Regression lines, highlights, key elements."""

    RED: str = "#FF2A2A"
    """Errors, warnings, danger indicators."""

    GOLD: str = "#FFD700"
    """Final synthesis highlight, VALUE PREDICTED text."""

    GRID: str = "#404040"
    """Faint grid lines on cartesian plane."""

    GREEN: str = "#00FF00"
    """Terminal cursor color."""

    BROWN: str = "#8B6F47"
    """Dull text highlight for secondary emphasis."""


@dataclass(frozen=True)
class TimingConfig:
    """Animation timing constants in seconds.

    Use these categories to maintain consistent animation feel across scenes:
    - FAST: Quick transitions, small movements (0.3-0.5s)
    - MEDIUM: Standard animations, reveals (0.6-1.0s)
    - SLOW: Dramatic moments, emphasis (1.5-2.0s)
    """

    FAST_MIN: float = 0.3
    """Fast animation minimum duration."""

    FAST_MAX: float = 0.5
    """Fast animation maximum duration."""

    MEDIUM_MIN: float = 0.6
    """Medium animation minimum duration."""

    MEDIUM_MAX: float = 1.0
    """Medium animation maximum duration."""

    SLOW_MIN: float = 1.5
    """Slow animation minimum duration."""

    SLOW_MAX: float = 2.0
    """Slow animation maximum duration."""

    TEXT_CASCADE_INTERVAL: float = 0.12
    """Time between text line appearances in cascade."""

    JITTER_INTERVAL: float = 0.05
    """Letter jitter frequency for text corruption effect."""

    SCENE_TRANSITION: float = 0.3
    """Overlap duration for scene transitions (FadeOut/FadeIn)."""


@dataclass(frozen=True)
class SceneConfig:
    """Timing boundaries for a single scene.

    Each scene has precise start and end times to ensure
    the complete video totals exactly 120 seconds.
    """

    name: str
    """Scene identifier (e.g., 'hallucination', 'linear_regression')."""

    start_time: float
    """Start timestamp in seconds from video start."""

    end_time: float
    """End timestamp in seconds from video start."""

    @property
    def duration(self) -> float:
        """Calculate scene duration from end_time - start_time."""
        return self.end_time - self.start_time


# Scene configuration instances - Single source of truth for timing
SCENE_HALLUCINATION: Final[SceneConfig] = SceneConfig(
    name="hallucination",
    start_time=0.0,
    end_time=25.0,
)

SCENE_CONTINUOUS_SCALE: Final[SceneConfig] = SceneConfig(
    name="continuous_scale",
    start_time=25.0,
    end_time=50.0,
)

SCENE_LINEAR_REGRESSION: Final[SceneConfig] = SceneConfig(
    name="linear_regression",
    start_time=50.0,
    end_time=75.0,
)

SCENE_NONLINEAR_REGRESSION: Final[SceneConfig] = SceneConfig(
    name="nonlinear_regression",
    start_time=75.0,
    end_time=100.0,
)

SCENE_SYNTHESIS: Final[SceneConfig] = SceneConfig(
    name="synthesis",
    start_time=100.0,
    end_time=120.0,
)

# All scenes in order for iteration
ALL_SCENES: Final[tuple[SceneConfig, ...]] = (
    SCENE_HALLUCINATION,
    SCENE_CONTINUOUS_SCALE,
    SCENE_LINEAR_REGRESSION,
    SCENE_NONLINEAR_REGRESSION,
    SCENE_SYNTHESIS,
)

# Video configuration constants
VIDEO_TOTAL_DURATION: Final[float] = 120.0
"""Total video duration in seconds (2 minutes)."""

VIDEO_WIDTH: Final[int] = 1920
"""Video width in pixels (1080p)."""

VIDEO_HEIGHT: Final[int] = 1080
"""Video height in pixels (1080p)."""

VIDEO_FPS: Final[int] = 60
"""Target frame rate."""

# Data generation constants
DATA_SEED: Final[int] = 42
"""Random seed for reproducible data generation (FR-004)."""

LINEAR_DATA_POINTS: Final[int] = 20
"""Number of data points for linear regression scene."""

LINEAR_SLOPE: Final[float] = 1.05
"""Target slope for linear regression data."""

LINEAR_INTERCEPT: Final[float] = 1.0
"""Target intercept for linear regression data."""

LINEAR_NOISE_STD: Final[float] = 0.3
"""Standard deviation of noise for linear data."""

NONLINEAR_DATA_POINTS: Final[int] = 25
"""Number of data points for non-linear regression scene."""

NEURAL_NETWORK_MIN_NODES: Final[int] = 1000
"""Minimum node count for neural network visualization (FR-010)."""

# Default singleton instances for convenience
COLORS: Final[ColorPalette] = ColorPalette()
"""Default color palette instance."""

TIMING: Final[TimingConfig] = TimingConfig()
"""Default timing configuration instance."""
