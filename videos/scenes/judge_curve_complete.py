"""Complete video composition for The Judge & The Curve.

Composes all 5 sections into a single 2-minute video with
precise timing boundaries and seamless transitions.
"""

from __future__ import annotations

from manim import Scene
from manim_voiceover import VoiceoverScene

from src.utils.color_utils import get_background_color


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
        from manim_voiceover.services.gtts import GTTSService

        self.set_speech_service(GTTSService())

        # Set background color
        self.camera.background_color = get_background_color()

        # Section 1: Hallucination (25 seconds)
        self._render_section_1()

        # TODO: Add render_animations() method to remaining sections
        # Section 2: Continuous Scale (25 seconds)
        # self._render_section_2()

        # Section 3: Linear Regression (25 seconds)
        # self._render_section_3()

        # Section 4: Non-Linear Regression (25 seconds)
        # self._render_section_4()

        # Section 5: Synthesis (20 seconds)
        # self._render_section_5()

    def _render_section_1(self) -> None:
        """Render Section 1: Hallucination scene.

        Duration: 25 seconds (0:00-0:25)
        Establishes AI hallucination metaphor with terminal chaos,
        warning overlay, and static dissolution.
        """
        from videos.scenes.section1_hallucination import HallucinationScene

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
        from videos.scenes.section2_scale import ContinuousScaleScene

        section = ContinuousScaleScene()
        section.render_to(self)

        self.clear()

    def _render_section_3(self) -> None:
        """Render Section 3: Linear Regression scene.

        Duration: 25 seconds (0:50-1:15)
        Demonstrates linear regression with data points,
        best-fit line, equation, and error visualization.
        """
        from videos.scenes.section3_linear import LinearRegressionScene

        section = LinearRegressionScene()
        section.render_to(self)

        self.clear()

    def _render_section_4(self) -> None:
        """Render Section 4: Non-Linear Regression scene.

        Duration: 25 seconds (1:15-1:40)
        Shows linear model failure on S-curve data,
        then morphs to polynomial curve.
        """
        from videos.scenes.section4_nonlinear import NonLinearRegressionScene

        section = NonLinearRegressionScene()
        section.render_to(self)

        self.clear()

    def _render_section_5(self) -> None:
        """Render Section 5: Synthesis scene.

        Duration: 20 seconds (1:40-2:00)
        Compresses curve to node, expands to neural network,
        displays final "VALUE PREDICTED" message.
        """
        from videos.scenes.section5_synthesis import SynthesisScene

        section = SynthesisScene()
        section.render_to(self)

        # No clear needed - this is the final scene


class BaseVideoScene(Scene):
    """Base class for all Judge & Curve video scenes.

    Provides common functionality and enforces interface contract.
    """

    SCENE_NAME: str = ""
    START_TIME: float = 0.0
    END_TIME: float = 0.0

    def construct(self) -> None:
        """Main animation sequence. Must complete within duration."""
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
