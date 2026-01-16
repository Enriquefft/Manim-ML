"""Section 5: The Synthesis (The Network).

Time: 1:40 - 2:00

[Visual Scene]
- 1:40: Isolate the curved biological line (from Section 4)
- 1:45: Zoom out rapidly. That curve becomes a single wire (neuron)
- 1:50: Reveal a massive network of millions of these curved wires connected
- 1:55: The "Judge" text returns, GLOWING over the network

[Audio / Voiceover]
"And that AI Judge from the beginning? It's not magic. It is just millions of
Non-Linear Regressions stacked on top of each other. It processes the complexity
of human language to predict one simple thing: Value."

Duration: 20 seconds (1:40-2:00)
"""

from __future__ import annotations

import math

from manim import (
    DOWN,
    ORIGIN,
    Create,
    FadeIn,
    FadeOut,
    ManimColor,
    ParametricFunction,
    Text,
    VGroup,
    Write,
)
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

from src.config import COLORS, SCENE_SYNTHESIS
from src.utils.color_utils import get_background_color
from videos.templates.effects import apply_glow_effect


class SynthesisScene(VoiceoverScene):
    """Section 5: The Synthesis (The Network).

    Connects non-linear regression to neural networks by showing that a
    neural network is just "millions of non-linear regressions stacked."
    The "Judge" text returns glowing over the network, tying back to
    Section 1's narrative about the "mathematical Judge."

    Visual Timeline:
    - 1:40-1:45: Isolate the curved biological line from Section 4
    - 1:45-1:50: Zoom out rapidly - curve becomes single wire (neuron)
    - 1:50-1:55: Reveal massive network of curved wires connected
    - 1:55-2:00: "Judge" text returns, GLOWING over the network

    Timing: 1:40-2:00 (20 seconds)
    """

    SCENE_NAME: str = "synthesis"
    START_TIME: float = SCENE_SYNTHESIS.start_time
    END_TIME: float = SCENE_SYNTHESIS.end_time

    # Voiceover script for this section
    VOICEOVER_TEXT: str = (
        "And that AI Judge from the beginning? It's not magic. "
        "It is just millions of Non-Linear Regressions stacked on top of each other. "
        "It processes the complexity of human language "
        "to predict one simple thing: Value."
    )

    def construct(self) -> None:
        """Build the synthesis scene animation sequence."""
        self.set_speech_service(GTTSService())
        self.camera.background_color = get_background_color()

        # Start voiceover that plays throughout the scene
        with self.voiceover(text=self.VOICEOVER_TEXT) as tracker:
            self._run_visual_sequence(tracker.duration)

    def _run_visual_sequence(self, total_duration: float) -> None:
        """Run the visual animation sequence synchronized to voiceover.

        Args:
            total_duration: Total duration from voiceover tracker.

        """
        # Calculate phase durations based on total voiceover length
        # Phases: isolate (20%), zoom/wire (25%), network (30%), judge text (25%)
        isolate_duration = total_duration * 0.20
        wire_duration = total_duration * 0.25
        network_duration = total_duration * 0.30
        judge_duration = total_duration * 0.25

        # Phase 1: Isolate the curved biological line (1:40-1:45)
        curve = self._create_biological_curve()
        curve_with_glow = self._isolate_curve(curve)
        self.play(Create(curve_with_glow), run_time=isolate_duration * 0.7)
        self.wait(isolate_duration * 0.3)

        # Phase 2: Zoom out - curve becomes single wire/neuron (1:45-1:50)
        wire = self._transform_curve_to_wire(curve_with_glow, wire_duration)

        # Phase 3: Reveal massive network of curved wires (1:50-1:55)
        network = self._reveal_curved_wire_network(wire, network_duration)

        # Phase 4: "Judge" text returns, GLOWING (1:55-2:00)
        self._create_glowing_judge_text(network, judge_duration)

    def _create_biological_curve(self) -> ParametricFunction:
        """Create the hill-shaped dose-response curve from Section 4.

        Returns:
            ParametricFunction representing the non-linear curve.

        """

        def hill_function(t: float) -> float:
            """Dose-response hill function matching Section 4."""
            # Map t from [0, 10] to x values for the hill curve
            x = t
            # Therapeutic effect (rises and saturates)
            therapeutic = 8.0 * (1.0 - math.exp(-0.6 * x))
            # Toxicity kicks in at higher doses
            toxicity = 0.15 * max(0.0, x - 4.0) ** 2
            return max(0.5, therapeutic - toxicity)

        return ParametricFunction(
            lambda t: [t - 5, hill_function(t) - 4, 0],
            t_range=[0.3, 10.5],
            color=ManimColor(COLORS.CYAN),
            stroke_width=4,
        )

    def _isolate_curve(self, curve: ParametricFunction) -> VGroup:
        """Remove context, keep only glowing curve.

        Args:
            curve: The curve to isolate.

        Returns:
            VGroup containing curve with glow effect.

        """
        return apply_glow_effect(curve, glow_factor=1.5, opacity=0.4)

    def _transform_curve_to_wire(
        self,
        curve: VGroup,
        duration: float,
    ) -> ParametricFunction:
        """Zoom out - the curve becomes a single wire (neuron).

        The wire remains curved to show it's a non-linear function.
        This represents one neuron = one non-linear regression.

        Args:
            curve: The isolated curve VGroup.
            duration: Duration for the transformation.

        Returns:
            The resulting small curved wire.

        """
        # Scale down the curve to become a small "wire" (neuron)
        # The curve shrinks but stays curved - showing it's non-linear
        self.play(
            curve.animate.scale(0.15).move_to(ORIGIN),
            run_time=duration * 0.6,
        )

        # Brief pause to show single wire
        self.wait(duration * 0.4)

        # Return reference to the transformed curve (now a wire)
        return curve

    # Network generation constants
    _WIRE_ROWS: int = 12
    _WIRE_COLS: int = 18
    _WIRE_SPACING_X: float = 0.8
    _WIRE_SPACING_Y: float = 0.6
    _WIRE_SCALE: float = 0.08

    def _reveal_curved_wire_network(
        self,
        start_wire: VGroup | ParametricFunction,
        duration: float,
    ) -> VGroup:
        """Zoom out rapidly to reveal network of millions of curved wires.

        The network shows many curved wires (not straight lines) to emphasize
        that neural networks are "millions of non-linear regressions stacked."

        Args:
            start_wire: The starting wire to expand from.
            duration: Duration for the network reveal.

        Returns:
            VGroup containing all network wire elements.

        """
        # Create a grid of curved wires (neurons)
        network_wires = VGroup()

        # Generate many small curved wires
        for row in range(self._WIRE_ROWS):
            for col in range(self._WIRE_COLS):
                # Create small curved wire (each represents a non-linear function)
                wire = self._create_small_curved_wire()

                # Position in grid pattern
                x = (col - self._WIRE_COLS / 2) * self._WIRE_SPACING_X
                y = (row - self._WIRE_ROWS / 2) * self._WIRE_SPACING_Y

                wire.move_to([x, y, 0])
                wire.scale(self._WIRE_SCALE)

                # Vary opacity slightly for depth effect
                base_opacity = 0.6
                opacity_variation = 0.3 * ((row + col) % 3) / 2
                wire.set_opacity(base_opacity + opacity_variation)

                network_wires.add(wire)

        # Create connection lines between wires (also curved for consistency)
        connections = self._create_network_connections()

        # Combine into full network
        full_network = VGroup(connections, network_wires)

        # Start small and expand rapidly (zoom out effect)
        full_network.scale(0.01)
        full_network.move_to(ORIGIN)
        full_network.set_opacity(0)

        # Fade out the single wire
        self.play(FadeOut(start_wire), run_time=duration * 0.15)

        # Add network and expand rapidly
        self.add(full_network)
        self.play(
            full_network.animate.scale(100).set_opacity(1),
            run_time=duration * 0.65,
        )

        self.wait(duration * 0.20)

        return full_network

    def _create_small_curved_wire(self) -> ParametricFunction:
        """Create a small curved wire representing one neuron.

        Each wire is curved to show it's a non-linear function.

        Returns:
            ParametricFunction for a small curved wire.

        """
        # Small sigmoid-like curve - represents non-linear activation
        return ParametricFunction(
            lambda t: [t, 0.3 * math.tanh(t * 2), 0],
            t_range=[-1, 1],
            color=ManimColor(COLORS.CYAN),
            stroke_width=2,
        )

    # Connection generation constants
    _CONNECTION_COUNT: int = 150
    _CONNECTION_OPACITY: float = 0.25

    def _create_network_connections(self) -> VGroup:
        """Create curved connections between network nodes.

        Returns:
            VGroup containing curved connection lines.

        """
        import random

        connections = VGroup()

        # Deterministic randomness for reproducibility
        rng = random.Random(42)  # noqa: S311

        # Create curved connection paths
        for _ in range(self._CONNECTION_COUNT):
            # Random start and end points within the network bounds
            x1 = rng.uniform(-6, 6)
            y1 = rng.uniform(-3, 3)
            x2 = rng.uniform(-6, 6)
            y2 = rng.uniform(-3, 3)

            # Create curved connection (Bezier-like)
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2 + rng.uniform(-0.5, 0.5)

            connection = ParametricFunction(
                lambda t, x1=x1, y1=y1, mid_x=mid_x, mid_y=mid_y, x2=x2, y2=y2: [
                    (1 - t) ** 2 * x1 + 2 * (1 - t) * t * mid_x + t**2 * x2,
                    (1 - t) ** 2 * y1 + 2 * (1 - t) * t * mid_y + t**2 * y2,
                    0,
                ],
                t_range=[0, 1],
                color=ManimColor(COLORS.GRID),
                stroke_width=0.5,
                stroke_opacity=self._CONNECTION_OPACITY,
            )
            connections.add(connection)

        return connections

    def _create_glowing_judge_text(
        self,
        network: VGroup,
        duration: float,
    ) -> None:
        """Create glowing "Judge" text over the network.

        This connects back to Section 1's narrative about the
        "mathematical Judge" that engineers built.

        Args:
            network: The network VGroup to display text over.
            duration: Duration for the judge text animation.

        """
        # Create "Judge" text - connects back to Section 1
        judge_text = Text(
            "Judge",
            font_size=96,
            color=ManimColor(COLORS.GOLD),
            weight="BOLD",
        )
        judge_text.move_to(ORIGIN)

        # Create glowing version
        glow_text = apply_glow_effect(
            judge_text,
            glow_factor=1.8,
            opacity=0.5,
            color=COLORS.GOLD,
        )

        # Animate text appearing with glow
        self.play(Write(judge_text), run_time=duration * 0.4)

        # Replace with glowing version
        self.remove(judge_text)
        glow_text.move_to(ORIGIN)
        self.add(glow_text)

        # Pulse the glow for emphasis
        self.play(
            glow_text.animate.scale(1.1),
            run_time=duration * 0.2,
        )
        self.play(
            glow_text.animate.scale(1 / 1.1),
            run_time=duration * 0.2,
        )

        self.wait(duration * 0.2)

        # Fade everything out
        all_content = VGroup(network, glow_text)
        self.play(FadeOut(all_content), run_time=duration * 0.0)

    def get_duration(self) -> float:
        """Return scene duration."""
        return self.END_TIME - self.START_TIME
