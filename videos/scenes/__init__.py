"""Scene implementations for The Judge & The Curve video.

Contains 5 scene classes corresponding to video sections:
- HallucinationScene: Section 1 (0:00-0:25) - AI hallucination metaphor
- ContinuousScaleScene: Section 2 (0:25-0:50) - Continuous scoring concept
- LinearRegressionScene: Section 3 (0:50-1:15) - Linear regression demonstration
- NonLinearRegressionScene: Section 4 (1:15-1:40) - Non-linear evolution
- SynthesisScene: Section 5 (1:40-2:00) - Neural network synthesis

Plus the composition class:
- JudgeCurveComplete: Full 120-second video composition

Also includes existing example scenes for reference.
"""

from __future__ import annotations

from videos.scenes.example_scene import DynamicMathExample, ShapeMorphingExample
from videos.scenes.judge_curve_complete import JudgeCurveComplete
from videos.scenes.section1_hallucination import HallucinationScene
from videos.scenes.section2_scale import ContinuousScaleScene
from videos.scenes.section3_linear import LinearRegressionScene
from videos.scenes.section4_nonlinear import NonLinearRegressionScene
from videos.scenes.section5_synthesis import SynthesisScene

__all__ = [
    "ContinuousScaleScene",
    "DynamicMathExample",
    "HallucinationScene",
    "JudgeCurveComplete",
    "LinearRegressionScene",
    "NonLinearRegressionScene",
    "ShapeMorphingExample",
    "SynthesisScene",
]
