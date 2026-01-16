"""Section 2: The Scale (Continuous Scoring).

Time: 0:25 - 0:50

[Visual Scene]
- 0:25: Split screen.
        Left: "Paris is France."
        Right: "Paris is a cheese."
- 0:30: A sliding gauge appears between them. It is NOT a switch (Yes/No).
        It is a smooth slider labeled "REWARD SCORE."
- 0:35: The slider moves to 0.99 for the Left text.
        It slides down to -0.50 for the Right text.
- 0:45: Text appears: REGRESSION: PREDICTING A QUANTITY.

[Audio / Voiceover]
"This 'Judge' (a Reward Model) doesn't just say 'Wrong.' It asks 'How much?'
Is this answer 10% useful? 90%? Predicting a precise number on a continuous
scale is the definition of Regression. It turns qualitative chaos into
quantitative data."

Duration: 25 seconds (0:25-0:50)
"""

from __future__ import annotations

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    Create,
    DecimalNumber,
    FadeIn,
    FadeOut,
    Line,
    ManimColor,
    Rectangle,
    RoundedRectangle,
    Text,
    VGroup,
    Write,
)
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

from src.config import COLORS, SCENE_CONTINUOUS_SCALE
from src.utils.color_utils import get_background_color


class ContinuousScaleScene(VoiceoverScene):
    """Section 2: The Scale (Continuous Scoring).

    Introduces the concept that reward models predict continuous scores,
    not just binary true/false values - this is regression.

    Visual Timeline:
    - 0:25-0:30: Split screen with two Paris statements
    - 0:30-0:35: Sliding gauge "REWARD SCORE" appears
    - 0:35-0:45: Slider animates to 0.99 (left), then -0.50 (right)
    - 0:45-0:50: "REGRESSION: PREDICTING A QUANTITY" text appears

    Timing: 0:25-0:50 (25 seconds)
    """

    SCENE_NAME: str = "continuous_scale"
    START_TIME: float = SCENE_CONTINUOUS_SCALE.start_time
    END_TIME: float = SCENE_CONTINUOUS_SCALE.end_time

    # Example statements for comparison
    LEFT_STATEMENT: str = "Paris is France."
    RIGHT_STATEMENT: str = "Paris is a cheese."

    # Reward scores for each statement
    LEFT_SCORE: float = 0.99
    RIGHT_SCORE: float = -0.50

    # Voiceover script for this section
    VOICEOVER_TEXT: str = (
        "This 'Judge' (a Reward Model) doesn't just say 'Wrong.' "
        "It asks 'How much?' Is this answer 10% useful? 90%? "
        "Predicting a precise number on a continuous scale "
        "is the definition of Regression. "
        "It turns qualitative chaos into quantitative data."
    )

    def construct(self) -> None:
        """Build the continuous scale scene animation sequence."""
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
        with parent_scene.voiceover(text=self.VOICEOVER_TEXT) as tracker:
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
        split_duration = total_duration * 0.20
        slider_duration = total_duration * 0.20
        scoring_duration = total_duration * 0.40
        conclusion_duration = total_duration * 0.20

        # Phase 1: Split screen
        left_pane, right_pane, divider = self._create_split_screen()
        scene.play(
            FadeIn(left_pane),
            FadeIn(right_pane),
            FadeIn(divider),
            run_time=split_duration * 0.4,
        )
        scene.wait(split_duration * 0.6)

        # Phase 2: Reward score slider
        slider_group = self._create_reward_slider()
        scene.play(Create(slider_group), run_time=slider_duration)

        # Phase 3: Animate scores
        self._animate_score_in_scene(
            scene,
            slider_group,
            self.LEFT_SCORE,
            left_pane,
            duration=scoring_duration * 0.45,
        )
        scene.wait(scoring_duration * 0.05)

        self._animate_score_in_scene(
            scene,
            slider_group,
            self.RIGHT_SCORE,
            right_pane,
            duration=scoring_duration * 0.45,
        )
        scene.wait(scoring_duration * 0.05)

        # Phase 4: Conclusion text
        conclusion = self._create_conclusion_text()
        scene.play(Write(conclusion), run_time=conclusion_duration * 0.6)
        scene.wait(conclusion_duration * 0.4)

        # Fade out
        all_content = VGroup(left_pane, right_pane, divider, slider_group, conclusion)
        scene.play(FadeOut(all_content), run_time=0.5)

    def _run_visual_sequence(self, total_duration: float) -> None:
        """Run the visual animation sequence synchronized to voiceover.

        Args:
            total_duration: Total duration from voiceover tracker.

        """
        # Calculate phase durations based on total voiceover length
        # Phases: split screen (20%), slider appear (20%), scoring (40%), conclusion (20%)
        split_duration = total_duration * 0.20
        slider_duration = total_duration * 0.20
        scoring_duration = total_duration * 0.40
        conclusion_duration = total_duration * 0.20

        # Phase 1: Split screen with two statements (0:25-0:30)
        left_pane, right_pane, divider = self._create_split_screen()
        self.play(
            FadeIn(left_pane),
            FadeIn(right_pane),
            FadeIn(divider),
            run_time=split_duration * 0.4,
        )
        self.wait(split_duration * 0.6)

        # Phase 2: Reward score slider appears (0:30-0:35)
        slider_group = self._create_reward_slider()
        self.play(Create(slider_group), run_time=slider_duration)

        # Phase 3: Animate scores (0:35-0:45)
        # First show score for left statement (0.99)
        self._animate_score(
            slider_group,
            self.LEFT_SCORE,
            left_pane,
            duration=scoring_duration * 0.45,
        )
        self.wait(scoring_duration * 0.05)

        # Then show score for right statement (-0.50)
        self._animate_score(
            slider_group,
            self.RIGHT_SCORE,
            right_pane,
            duration=scoring_duration * 0.45,
        )
        self.wait(scoring_duration * 0.05)

        # Phase 4: Show conclusion text (0:45-0:50)
        conclusion = self._create_conclusion_text()
        self.play(Write(conclusion), run_time=conclusion_duration * 0.6)
        self.wait(conclusion_duration * 0.4)

        # Fade out everything
        all_content = VGroup(left_pane, right_pane, divider, slider_group, conclusion)
        self.play(FadeOut(all_content), run_time=0.5)

    def _create_split_screen(self) -> tuple[VGroup, VGroup, Line]:
        """Create split screen with two statement cards.

        Returns:
            Tuple of (left_pane, right_pane, divider).

        """
        # Create divider line
        divider = Line(
            start=UP * 2.5,
            end=DOWN * 1.5,
            color=ManimColor(COLORS.GRID),
            stroke_width=3,
        )

        # Create left pane - good answer
        left_card = self._create_statement_card(
            self.LEFT_STATEMENT,
            position=LEFT * 3.5,
            border_color=COLORS.GREEN,
        )

        # Create right pane - bad answer
        right_card = self._create_statement_card(
            self.RIGHT_STATEMENT,
            position=RIGHT * 3.5,
            border_color=COLORS.RED,
        )

        return left_card, right_card, divider

    def _create_statement_card(
        self,
        statement: str,
        position: tuple[float, float, float],
        border_color: str,
    ) -> VGroup:
        """Create a card containing a statement.

        Args:
            statement: The text statement to display.
            position: Position vector for the card.
            border_color: Color for the card border.

        Returns:
            VGroup containing the card and text.

        """
        # Create card background
        card = RoundedRectangle(
            width=5.5,
            height=2.0,
            corner_radius=0.2,
            color=ManimColor(border_color),
            fill_opacity=0.1,
            stroke_width=2,
        )
        card.move_to(position)

        # Create statement text
        text = Text(
            statement,
            font_size=28,
            color=ManimColor(COLORS.TEXT),
        )
        text.move_to(position)

        return VGroup(card, text)

    def _create_reward_slider(self) -> VGroup:
        """Create horizontal reward score slider gauge.

        NOT a binary switch - a smooth continuous slider.

        Returns:
            VGroup containing the complete slider component.

        """
        # Slider positioned at center-bottom
        slider_y = DOWN * 2.5

        # Create slider track (horizontal bar)
        track = Rectangle(
            width=10.0,
            height=0.3,
            color=ManimColor(COLORS.GRID),
            fill_opacity=0.3,
            stroke_width=2,
        )
        track.move_to(slider_y)

        # Create gradient overlay (red on left, green on right)
        # Left side (negative) - red
        left_gradient = Rectangle(
            width=5.0,
            height=0.25,
            color=ManimColor(COLORS.RED),
            fill_opacity=0.4,
            stroke_width=0,
        )
        left_gradient.move_to(slider_y + LEFT * 2.5)

        # Right side (positive) - green
        right_gradient = Rectangle(
            width=5.0,
            height=0.25,
            color=ManimColor(COLORS.GREEN),
            fill_opacity=0.4,
            stroke_width=0,
        )
        right_gradient.move_to(slider_y + RIGHT * 2.5)

        # Create slider handle (knob)
        handle = Rectangle(
            width=0.15,
            height=0.6,
            color=ManimColor(COLORS.CYAN),
            fill_opacity=1.0,
            stroke_width=2,
        )
        handle.move_to(slider_y)  # Start at center (0)

        # Create labels
        title_label = Text(
            "REWARD SCORE",
            font_size=24,
            color=ManimColor(COLORS.TEXT),
            weight="BOLD",
        )
        title_label.next_to(track, UP, buff=0.4)

        # Min/max labels
        min_label = Text("-1.0", font_size=20, color=ManimColor(COLORS.RED))
        min_label.next_to(track, LEFT, buff=0.3)

        max_label = Text("+1.0", font_size=20, color=ManimColor(COLORS.GREEN))
        max_label.next_to(track, RIGHT, buff=0.3)

        # Center label
        zero_label = Text("0", font_size=18, color=ManimColor(COLORS.GRID))
        zero_label.next_to(track, DOWN, buff=0.2)

        # Score display (will be updated during animation)
        score_display = DecimalNumber(
            0.0,
            num_decimal_places=2,
            font_size=36,
            color=ManimColor(COLORS.CYAN),
            include_sign=True,
        )
        score_display.next_to(handle, UP, buff=0.3)

        return VGroup(
            track,
            left_gradient,
            right_gradient,
            handle,
            title_label,
            min_label,
            max_label,
            zero_label,
            score_display,
        )

    def _animate_score(
        self,
        slider_group: VGroup,
        target_score: float,
        highlight_pane: VGroup,
        duration: float,
    ) -> None:
        """Animate the slider to show a score for a statement.

        Args:
            slider_group: The slider VGroup.
            target_score: Target score (-1.0 to 1.0).
            highlight_pane: The pane to highlight during scoring.
            duration: Animation duration.

        """
        track = slider_group[0]
        handle = slider_group[3]
        score_display = slider_group[8]

        # Calculate target x position (-1.0 = left edge, +1.0 = right edge)
        track_left = track.get_left()[0]
        track_right = track.get_right()[0]
        track_center_y = track.get_center()[1]

        # Map score (-1 to 1) to position
        normalized = (target_score + 1.0) / 2.0  # 0 to 1
        target_x = track_left + (track_right - track_left) * normalized

        # Determine color based on score
        score_color = ManimColor(COLORS.GREEN) if target_score >= 0 else ManimColor(COLORS.RED)

        # Animate handle movement and score update
        self.play(
            handle.animate.move_to([target_x, track_center_y, 0]),
            score_display.animate.set_value(target_score).move_to(
                [target_x, track_center_y + 0.5, 0],
            ),
            score_display.animate.set_color(score_color),
            highlight_pane[0].animate.set_stroke(width=4),
            run_time=duration,
        )

        # Reset highlight
        self.play(
            highlight_pane[0].animate.set_stroke(width=2),
            run_time=0.2,
        )

    def _animate_score_in_scene(
        self,
        scene: VoiceoverScene,
        slider_group: VGroup,
        target_score: float,
        highlight_pane: VGroup,
        duration: float,
    ) -> None:
        """Animate the slider to show a score in a specific scene (for composition).

        Args:
            scene: The scene to add animations to.
            slider_group: The slider VGroup.
            target_score: Target score (-1.0 to 1.0).
            highlight_pane: The pane to highlight during scoring.
            duration: Animation duration.

        """
        track = slider_group[0]
        handle = slider_group[3]
        score_display = slider_group[8]

        # Calculate target x position (-1.0 = left edge, +1.0 = right edge)
        track_left = track.get_left()[0]
        track_right = track.get_right()[0]
        track_center_y = track.get_center()[1]

        # Map score (-1 to 1) to position
        normalized = (target_score + 1.0) / 2.0  # 0 to 1
        target_x = track_left + (track_right - track_left) * normalized

        # Determine color based on score
        score_color = ManimColor(COLORS.GREEN) if target_score >= 0 else ManimColor(COLORS.RED)

        # Animate handle movement and score update
        scene.play(
            handle.animate.move_to([target_x, track_center_y, 0]),
            score_display.animate.set_value(target_score).move_to(
                [target_x, track_center_y + 0.5, 0],
            ),
            score_display.animate.set_color(score_color),
            highlight_pane[0].animate.set_stroke(width=4),
            run_time=duration,
        )

        # Reset highlight
        scene.play(
            highlight_pane[0].animate.set_stroke(width=2),
            run_time=0.2,
        )

    def _create_conclusion_text(self) -> Text:
        """Create the conclusion text about regression.

        Returns:
            Text mobject with the conclusion.

        """
        conclusion = Text(
            "REGRESSION: PREDICTING A QUANTITY",
            font_size=36,
            color=ManimColor(COLORS.CYAN),
            weight="BOLD",
        )
        conclusion.to_edge(DOWN, buff=0.5)
        return conclusion

    def get_duration(self) -> float:
        """Return scene duration."""
        return self.END_TIME - self.START_TIME
