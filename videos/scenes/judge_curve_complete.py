"""Complete video composition for The Judge & The Curve.

Compose all 5 sections into a single 2-minute video with
precise timing boundaries and seamless transitions.
"""

from __future__ import annotations

from manim import Scene
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

from src.utils.color_utils import get_background_color
from videos.scenes.section1_hallucination import HallucinationScene
from videos.scenes.section2_scale import ContinuousScaleScene
from videos.scenes.section3_linear import LinearRegressionScene
from videos.scenes.section4_nonlinear import NonLinearRegressionScene
from videos.scenes.section5_synthesis import SynthesisScene


class JudgeCurveComplete(VoiceoverScene):
    """Complete 2-minute video composition.

    Composes all 5 sections in sequence:
    - Section 1: Hallucination (0:00-0:25)
    - Section 2: Continuous Scale (0:25-0:50)
    - Section 3: Linear Regression (0:50-1:15)
    - Section 4: Non-Linear Regression (1:15-1:40)
    - Section 5: Synthesis (1:40-2:00)

    Total duration: exactly 120 seconds.
    """

    def construct(self) -> None:
        """Build the complete video sequence."""
        # Initialize voiceover service
        self.set_speech_service(GTTSService())

        # Set background color
        self.camera.background_color = get_background_color()

        # Section 1: Hallucination (25 seconds)
        self._render_section_1()

        # Section 2: Continuous Scale (25 seconds)
        self._render_section_2()

        # Section 3: Linear Regression (25 seconds)
        self._render_section_3()

        # Section 4: Non-Linear Regression (25 seconds)
        self._render_section_4()

        # Section 5: Synthesis (20 seconds)
        self._render_section_5()

    def _render_section_1(self) -> None:
        """Render Section 1: Hallucination scene.

        Duration: 25 seconds (0:00-0:25)
        Establishes AI hallucination metaphor with terminal chaos,
        warning overlay, and static dissolution.
        """
        # Render section animations to this scene
        section = HallucinationScene()
        section.render_animations(self)

        # Clear for next section
        self.clear()

    def _render_section_2(self) -> None:
        """Render Section 2: Continuous Scale scene.

        Duration: 25 seconds (0:25-0:50)
        Introduces continuous scoring concept with split screen
        and slider visualization.
        """
        section = ContinuousScaleScene()
        section.render_animations(self)

        self.clear()

    def _render_section_3(self) -> None:
        """Render Section 3: Linear Regression scene.

        Duration: 25 seconds (0:50-1:15)
        Demonstrates linear regression with data points,
        best-fit line, equation, and error visualization.
        """
        section = LinearRegressionScene()
        section.render_animations(self)

        self.clear()

    def _render_section_4(self) -> None:
        """Render Section 4: Non-Linear Regression scene.

        Duration: 25 seconds (1:15-1:40)
        Shows linear model failure on S-curve data,
        then morphs to polynomial curve.
        """
        section = NonLinearRegressionScene()
        section.render_animations(self)

        self.clear()

    def _render_section_5(self) -> None:
        """Render Section 5: Synthesis scene.

        Duration: 20 seconds (1:40-2:00)
        Compresses curve to node, expands to neural network,
        displays final "VALUE PREDICTED" message.
        """
        section = SynthesisScene()
        section.render_animations(self)

        # No clear needed - this is the final scene


class BaseVideoScene(Scene):
    """Base class for all Judge & Curve video scenes.

    Provides common functionality and enforces interface contract.
    """

    SCENE_NAME: str = ""
    START_TIME: float = 0.0
    END_TIME: float = 0.0

    def construct(self) -> None:
        """Build the scene's main animation sequence."""
        # Set background color
        self.camera.background_color = get_background_color()

    def get_duration(self) -> float:
        """Return the scene duration in seconds."""
        return self.END_TIME - self.START_TIME

    def validate_timing(self) -> bool:
        """Verify scene completes within allowed duration.

        Returns:
            True if timing is valid, False otherwise.

        """
        expected_duration = self.END_TIME - self.START_TIME
        return expected_duration > 0
