"""Section 1: The Hallucination (Cognitive Dissonance).

Time: 0:00 - 0:25

[Visual Scene]
- 0:00: Black screen. A terminal cursor blinks green.
- 0:05: Text floods the screen rapidly. It is incoherent:
        "The moon is made of blue algorithm potato..."
- 0:10: A red box overlays the text: NO METRIC FOUND.
- 0:15: The text blurs into static noise.

[Audio / Voiceover]
"Intelligence without a target is just noise. When Large Language Models
were born, they could speak, but they couldn't judge. They had no idea if
an answer was brilliant or garbage. To fix this, engineers didn't write
rules. They built a mathematical Judge."

Duration: 25 seconds (0:00-0:25)
"""

from __future__ import annotations

import random

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    AddTextLetterByLetter,
    FadeIn,
    FadeOut,
    ManimColor,
    Rectangle,
    Text,
    VGroup,
)
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

from src.config import COLORS, SCENE_HALLUCINATION
from src.utils.color_utils import get_background_color
from videos.templates.animations import create_bounce_animation
from videos.templates.custom_shapes import create_warning_icon
from videos.templates.effects import (
    apply_chromatic_aberration,
    apply_glow_effect,
    create_static_noise_overlay,
)

# Incoherent text fragments representing AI hallucination
# Style: nonsensical word salad mixing concepts inappropriately
HALLUCINATION_FRAGMENTS: list[str] = [
    "The moon is made of blue algorithm potato...",
    "Seventeen clouds whispered to the database...",
    "The answer is definitely purple entropy...",
    "Water flows upward through recursive dreams...",
    "Confidence: the smell of triangular logic...",
    "Birds are secretly compressed wavelengths...",
    "Tomorrow happened yesterday in parallel...",
    "The gradient tastes like forgotten syntax...",
    "Multiply the feeling by abstract tuesday...",
    "Neural pathways dissolve into soup metaphor...",
    "The the the prediction is is is...",
    "ERROR: meaning has left the building...",
    "Truth equals false equals maybe equals...",
    "Elephants compute faster than yellow...",
    "The output smells like burning certainty...",
]


class HallucinationScene(VoiceoverScene):
    """Section 1: The Hallucination (Cognitive Dissonance).

    Demonstrates unguided AI producing noise and incoherent output,
    setting narrative context for why regression/judgment matters.

    Visual Timeline:
    - 0:00-0:05: Black screen with blinking green terminal cursor
    - 0:05-0:10: Rapid flood of incoherent text ("The moon is made of...")
    - 0:10-0:15: Red warning box overlay "NO METRIC FOUND"
    - 0:15-0:25: Text blurs into static noise dissolution

    Timing: 0:00-0:25 (25 seconds)
    """

    SCENE_NAME: str = "hallucination"
    START_TIME: float = SCENE_HALLUCINATION.start_time
    END_TIME: float = SCENE_HALLUCINATION.end_time

    # Voiceover script for this section
    VOICEOVER_TEXT: str = (
        "Intelligence without a target is just noise. "
        "When Large Language Models were born, they could speak, "
        "but they couldn't judge. They had no idea if an answer was "
        "brilliant or garbage. To fix this, engineers didn't write rules. "
        "They built a mathematical Judge."
    )

    def construct(self) -> None:
        """Build the hallucination scene animation sequence."""
        self.set_speech_service(GTTSService())
        self.camera.background_color = get_background_color()

        # Start voiceover that plays throughout the scene
        with self.voiceover(text=self.VOICEOVER_TEXT) as tracker:
            self._run_visual_sequence(tracker.duration)

    def render_animations(self, parent_scene: VoiceoverScene) -> None:
        """Render this section's animations into a parent scene.

        Args:
            parent_scene: The parent VoiceoverScene to add animations to.

        """
        # Transfer the scene reference temporarily
        original_scene = self

        # Use parent scene's voiceover functionality
        with parent_scene.voiceover(text=self.VOICEOVER_TEXT) as tracker:
            # Run visual sequence using parent scene's play/wait methods
            self._run_visual_sequence_in_scene(parent_scene, tracker.duration)

    def _run_visual_sequence_in_scene(
        self,
        scene: VoiceoverScene,
        total_duration: float,
    ) -> None:
        """Run visual sequence in a specific scene (for composition).

        Args:
            scene: The scene to add animations to.
            total_duration: Total duration from voiceover tracker.

        """
        # Calculate phase durations
        cursor_duration = total_duration * 0.2
        flood_duration = total_duration * 0.2
        warning_duration = total_duration * 0.2
        static_duration = total_duration * 0.4

        # Phase 1: Black screen with blinking terminal cursor
        cursor = self.create_terminal_cursor()
        scene.play(FadeIn(cursor), run_time=0.5)

        # Animate cursor blinking
        blink_time = (cursor_duration - 0.5) / 8
        for _ in range(4):
            scene.play(cursor.animate.set_opacity(0.3), run_time=blink_time)
            scene.play(cursor.animate.set_opacity(1.0), run_time=blink_time)

        # Phase 2: Rapid incoherent text flood
        text_group = self._flood_incoherent_text_in_scene(scene, flood_duration)

        # Phase 3: Warning overlay
        warning = self.create_warning_overlay()
        scene.play(create_bounce_animation(warning, duration=0.5))
        scene.wait(warning_duration - 0.5)

        # Phase 4: Static dissolution
        all_content = VGroup(cursor, text_group, warning)
        self._apply_static_dissolution_in_scene(scene, all_content, static_duration)

    def _run_visual_sequence(self, total_duration: float) -> None:
        """Run the visual animation sequence synchronized to voiceover.

        Args:
            total_duration: Total duration from voiceover tracker.

        """
        # Calculate phase durations based on total voiceover length
        # Phases: cursor (20%), text flood (20%), warning (20%), static (40%)
        cursor_duration = total_duration * 0.2
        flood_duration = total_duration * 0.2
        warning_duration = total_duration * 0.2
        static_duration = total_duration * 0.4

        # Phase 1: Black screen with blinking terminal cursor
        cursor = self.create_terminal_cursor()
        self.play(FadeIn(cursor), run_time=0.5)

        # Animate cursor blinking
        blink_time = (cursor_duration - 0.5) / 8  # 4 cycles, 2 animations each
        for _ in range(4):
            self.play(cursor.animate.set_opacity(0.3), run_time=blink_time)
            self.play(cursor.animate.set_opacity(1.0), run_time=blink_time)

        # Phase 2: Rapid incoherent text flood
        text_group = self._flood_incoherent_text_timed(flood_duration)

        # Phase 3: Warning overlay "NO METRIC FOUND"
        warning = self.create_warning_overlay()
        self.play(create_bounce_animation(warning, duration=0.5))
        self.wait(warning_duration - 0.5)

        # Phase 4: Text blurs into static noise
        all_content = VGroup(cursor, text_group, warning)
        self._apply_static_dissolution_timed(all_content, static_duration)

    # Color variation thresholds for text
    _GREEN_COLOR_THRESHOLD: float = 0.7
    _WARNING_COLOR_THRESHOLD: float = 0.5

    def _flood_incoherent_text_timed(self, duration: float) -> VGroup:
        """Flood the screen with rapid incoherent text.

        Creates the visual effect of AI hallucination - text appearing
        rapidly across the screen in an overwhelming, chaotic manner.

        Args:
            duration: Total duration for the text flood phase.

        Returns:
            VGroup containing all the text mobjects for later reference.

        """
        text_group = VGroup()
        # Deterministic randomness for reproducibility (not for crypto)
        rng = random.Random(42)  # noqa: S311

        # Create text lines at various positions
        for i, fragment in enumerate(HALLUCINATION_FRAGMENTS):
            # Vary position across the screen
            x_offset = rng.uniform(-5.5, 3.5)
            y_offset = 3.0 - (i * 0.45)

            text = Text(
                fragment,
                font="Courier",
                font_size=20,
                color=ManimColor(COLORS.TEXT),
            )
            text.move_to(LEFT * (-x_offset) + UP * y_offset)

            # Add slight color variation for some lines
            if rng.random() > self._GREEN_COLOR_THRESHOLD:
                text.set_color(ManimColor(COLORS.GREEN))
            elif rng.random() > self._WARNING_COLOR_THRESHOLD:
                text.set_color(ManimColor(COLORS.WARNING))

            text_group.add(text)

        # Calculate timing based on duration
        num_lines = len(text_group)
        time_per_line = duration / num_lines

        # Rapid-fire text appearance (flooding effect)
        for i, text in enumerate(text_group):
            # Use AddTextLetterByLetter for rapid typing effect
            self.play(
                AddTextLetterByLetter(text, time_per_char=0.015),
                run_time=time_per_line * 0.8,
            )
            # Brief pause between lines
            if i < num_lines - 1:
                self.wait(time_per_line * 0.2)

        return text_group

    def create_terminal_cursor(self) -> VGroup:
        """Create blinking green cursor with chromatic aberration.

        Returns:
            VGroup containing the cursor with effects applied.

        """
        # Create base cursor rectangle
        cursor = Rectangle(
            width=0.15,
            height=0.4,
            color=ManimColor(COLORS.GREEN),
            fill_opacity=1.0,
            stroke_width=0,
        )
        cursor.move_to(LEFT * 5 + UP * 3)

        # Apply chromatic aberration effect
        cursor_with_effect = apply_chromatic_aberration(cursor, offset=0.03)

        # Add glow and return
        return apply_glow_effect(cursor_with_effect, glow_factor=1.3, opacity=0.4)

    def create_warning_overlay(self) -> VGroup:
        """Create red warning box with 'NO METRIC FOUND' text.

        Returns:
            VGroup containing the warning box, icon, and text.

        """
        # Create warning box
        box = Rectangle(
            width=8,
            height=2,
            color=ManimColor(COLORS.RED),
            fill_opacity=0.2,
            stroke_width=3,
        )

        # Create warning icon
        icon = self.create_warning_icon()
        icon.scale(0.8)
        icon.next_to(box, LEFT, buff=0.3)
        icon.shift(RIGHT * 1.5)

        # Create warning text
        text = Text(
            "NO METRIC FOUND",
            font_size=48,
            color=ManimColor(COLORS.RED),
            weight="BOLD",
        )
        text.move_to(box.get_center())
        text.shift(RIGHT * 0.5)

        warning = VGroup(box, icon, text)
        warning.move_to(DOWN * 0.5)

        return warning

    def create_warning_icon(self) -> VGroup:
        """Create programmatic warning triangle icon.

        Returns:
            VGroup containing the warning icon (FR-012).

        """
        return create_warning_icon(size=0.8, color=COLORS.RED)

    def _apply_static_dissolution_timed(
        self,
        target: VGroup,
        duration: float,
    ) -> None:
        """Transition target to static noise - text blurs into static.

        Args:
            target: The mobject group to dissolve into static.
            duration: Total duration for the dissolution phase.

        """
        # Create static noise overlay
        noise = create_static_noise_overlay(density=500)
        noise.set_opacity(0)

        self.add(noise)

        # Allocate time: 40% blur, 30% hold, 30% fade out
        blur_time = duration * 0.4
        hold_time = duration * 0.3
        fade_time = duration * 0.3

        # Text blurs into static - gradual transition
        self.play(
            FadeOut(target),
            noise.animate.set_opacity(0.8),
            run_time=blur_time,
        )

        # Hold on static noise
        self.wait(hold_time)

        # Fade out static to black
        self.play(FadeOut(noise), run_time=fade_time)

    def get_duration(self) -> float:
        """Return scene duration."""
        return self.END_TIME - self.START_TIME

    def _flood_incoherent_text_in_scene(
        self,
        scene: VoiceoverScene,
        duration: float,
    ) -> VGroup:
        """Flood screen with text in a specific scene (for composition).

        Args:
            scene: The scene to add animations to.
            duration: Total duration for the text flood phase.

        Returns:
            VGroup containing all the text mobjects.

        """
        text_group = VGroup()
        rng = random.Random(42)  # noqa: S311

        # Create text lines
        for i, fragment in enumerate(HALLUCINATION_FRAGMENTS):
            x_offset = rng.uniform(-5.5, 3.5)
            y_offset = 3.0 - (i * 0.45)

            text = Text(
                fragment,
                font="Courier",
                font_size=20,
                color=ManimColor(COLORS.TEXT),
            )
            text.move_to(LEFT * (-x_offset) + UP * y_offset)

            # Add color variation
            if rng.random() > self._GREEN_COLOR_THRESHOLD:
                text.set_color(ManimColor(COLORS.GREEN))
            elif rng.random() > self._WARNING_COLOR_THRESHOLD:
                text.set_color(ManimColor(COLORS.BROWN))

            text_group.add(text)

        # Calculate timing
        num_lines = len(text_group)
        time_per_line = duration / num_lines

        # Rapid-fire text appearance
        for i, text in enumerate(text_group):
            scene.play(
                AddTextLetterByLetter(text, time_per_char=0.015),
                run_time=time_per_line * 0.8,
            )
            if i < num_lines - 1:
                scene.wait(time_per_line * 0.2)

        return text_group

    def _apply_static_dissolution_in_scene(
        self,
        scene: VoiceoverScene,
        target: VGroup,
        duration: float,
    ) -> None:
        """Apply static dissolution in a specific scene (for composition).

        Args:
            scene: The scene to add animations to.
            target: The mobject group to dissolve.
            duration: Total duration for the dissolution phase.

        """
        noise = create_static_noise_overlay(density=500)
        noise.set_opacity(0)
        scene.add(noise)

        blur_time = duration * 0.4
        hold_time = duration * 0.3
        fade_time = duration * 0.3

        scene.play(
            FadeOut(target),
            noise.animate.set_opacity(0.8),
            run_time=blur_time,
        )
        scene.wait(hold_time)
        scene.play(FadeOut(noise), run_time=fade_time)
