#!/usr/bin/env python
"""Entry point script for rendering The Judge & The Curve video.

Usage:
    # Low quality preview (480p, fast)
    python videos/judge_curve_main.py -ql

    # Medium quality (720p)
    python videos/judge_curve_main.py -qm

    # High quality final render (1080p60, required for delivery)
    python videos/judge_curve_main.py -qh

    # 4K render (future-proofing)
    python videos/judge_curve_main.py -qk
"""

from __future__ import annotations

import sys
from pathlib import Path

# Add project root to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from manim import config

from src.config import VIDEO_FPS, VIDEO_HEIGHT, VIDEO_WIDTH


def main() -> None:
    """Render the complete Judge & Curve video."""
    # Configure Manim settings
    config.pixel_width = VIDEO_WIDTH
    config.pixel_height = VIDEO_HEIGHT
    config.frame_rate = VIDEO_FPS

    # Import and render
    from videos.scenes.judge_curve_complete import JudgeCurveComplete

    scene = JudgeCurveComplete()
    scene.render()


if __name__ == "__main__":
    main()
