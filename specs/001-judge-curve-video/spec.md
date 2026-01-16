# Feature Specification: The Judge & The Curve Video

**Feature Branch**: `001-judge-curve-video`
**Created**: 2026-01-09
**Status**: Draft
**Input**: User description: "Implement the video detailed at ./requirements.md using Manim"

## Clarifications

### Session 2026-01-10

- Q: How should the warning icon asset be generated? → A: Icon is generated programmatically as part of build (vector/code-based)
- Q: What hardware baseline defines the render time target? → A: Remove time constraint; render time is informational only
- Q: How should image assets be handled? → A: Use simple placeholders for all images (except code-generated icons); externally generated images added post-render

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Complete Video Playback (Priority: P1)

A viewer watches "The Judge & The Curve" educational video from start to finish. The video explains regression concepts (linear vs. non-linear) through visual storytelling, starting with AI hallucination chaos, progressing through the concept of continuous scoring, demonstrating linear regression with error minimization, showing non-linear regression as an evolution, and culminating in neural network synthesis.

**Why this priority**: The core deliverable is a watchable, educational video. Without a complete video, no educational value is delivered.

**Independent Test**: Can be verified by playing the rendered video file and confirming all 5 sections appear in sequence, totaling exactly 2 minutes of content.

**Acceptance Scenarios**:

1. **Given** the video is rendered, **When** a viewer plays it, **Then** the video runs for exactly 2:00 minutes without interruption
2. **Given** the video is playing, **When** Section 1 ends at 0:25, **Then** Section 2 begins immediately with the split-screen setup
3. **Given** the video is playing, **When** the final frame appears, **Then** the "VALUE PREDICTED" text is visible with the neural network background

---

### User Story 2 - Linear Regression Concept Understanding (Priority: P1)

A viewer with no prior statistics knowledge watches Section 3 (Linear Regression) and understands how a straight line can represent a relationship between two variables, and how "error" represents the distance between actual data and the prediction line.

**Why this priority**: Linear regression is the foundational concept. If viewers don't grasp this, the non-linear section loses context.

**Independent Test**: Section 3 can be rendered and viewed independently, showing data points appearing, a line being drawn, and error bars visualizing the gap between prediction and reality.

**Acceptance Scenarios**:

1. **Given** Section 3 begins at 0:50, **When** data points appear on the grid, **Then** they form a visible upward trend pattern
2. **Given** the cyan line is drawn, **When** the equation appears, **Then** the mathematical notation y = mx + b is displayed near the line
3. **Given** an outlier is zoomed, **When** the red error line drops, **Then** the "ERROR" label with epsilon symbol clearly annotates the residual

---

### User Story 3 - Non-Linear Regression Comparison (Priority: P2)

A viewer sees the limitation of linear models when applied to complex data patterns, then witnesses the transition to a curved model that better fits the data. This teaches that not all relationships are straight lines.

**Why this priority**: Builds on linear regression understanding to show why more complex models exist. Critical for the educational narrative.

**Independent Test**: Section 4 can be rendered independently, showing the linear model failing with large error bars, then transforming into a curve that fits better.

**Acceptance Scenarios**:

1. **Given** the S-curve data is displayed, **When** the linear line from Section 3 is overlaid, **Then** large red error bars appear on the crash points
2. **Given** the linear model fails, **When** the line shatters and morphs, **Then** it transforms into a smooth polynomial curve
3. **Given** the curve fits the data, **When** the error bars are recalculated, **Then** they fade out indicating minimal error

---

### User Story 4 - Neural Network Connection (Priority: P2)

A viewer sees the regression curve compress into a single node (neuron), then expand into a massive neural network, illustrating that complex AI models are built from simple regression-like building blocks.

**Why this priority**: Provides the "aha moment" connecting regression to modern AI. Completes the educational arc.

**Independent Test**: Section 5 can be rendered independently, showing curve-to-node compression and network expansion animation.

**Acceptance Scenarios**:

1. **Given** the curve is isolated, **When** it compresses, **Then** it forms a glowing node with sigma symbol
2. **Given** a single node exists, **When** the network expands, **Then** 1000+ interconnected nodes appear with flowing data pulses
3. **Given** the network is visible, **When** the final text appears, **Then** "VALUE PREDICTED" stamps onto screen in gold

---

### User Story 5 - Visual Atmosphere Establishment (Priority: P3)

A viewer experiences the "AI hallucination" metaphor in Section 1, establishing the narrative premise that unguided AI produces noise. This creates emotional context for why regression/judgment matters.

**Why this priority**: Sets the mood and hook but is not strictly required for educational content about regression itself.

**Independent Test**: Section 1 can be rendered independently, showing terminal chaos, warning overlay, and static dissolution.

**Acceptance Scenarios**:

1. **Given** the video starts, **When** the cursor blinks, **Then** it pulses with chromatic aberration effect
2. **Given** nonsense text cascades, **When** the warning box appears, **Then** it slams in with bounce animation and "NO METRIC FOUND" text
3. **Given** the warning is displayed, **When** static dissolution begins, **Then** the screen fills with noise using a dolly zoom effect

---

### Edge Cases

- What happens if the video is paused mid-animation? Animations are pre-rendered; pausing shows a static frame.
- What happens if data points overlap during generation? A fixed random seed ensures consistent, non-overlapping point placement.
- What happens if the neural network expansion exceeds display boundaries? The animation is designed to zoom out, keeping all nodes within frame.
- What happens if fonts are missing? The system should fall back to available monospace/serif fonts or fail gracefully with clear error messaging.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Video MUST be exactly 2 minutes (120 seconds) in total duration
- **FR-002**: Video MUST contain 5 distinct sections with precise timing boundaries (Section 1: 0:00-0:25, Section 2: 0:25-0:50, Section 3: 0:50-1:15, Section 4: 1:15-1:40, Section 5: 1:40-2:00)
- **FR-003**: All visual elements MUST use the defined color palette (Background: #0D0D0D, Text: #F2F2F2, Cyan: #00F0FF, Red: #FF2A2A, Gold: #FFD700, Grid: #404040)
- **FR-004**: Data points in regression sections MUST be reproducible across renders (same positions each time)
- **FR-005**: Animations MUST follow specified timing (fast: 0.3-0.5s, medium: 0.6-1.0s, slow: 1.5-2.0s)
- **FR-006**: Each scene class MUST be independently renderable for testing purposes
- **FR-007**: The linear regression line MUST display the equation y = mx + b with calculated values
- **FR-008**: The non-linear curve MUST be a polynomial (quadratic) that visually fits the S-curve data pattern
- **FR-009**: Error visualization MUST show vertical lines from data points to regression line
- **FR-010**: Neural network expansion MUST show at least 1,000 nodes in final phase
- **FR-011**: All text MUST be legible at 1080p resolution
- **FR-012**: The warning icon asset MUST be generated programmatically (vector/code-based) as part of the build process
- **FR-013**: All non-icon image assets MUST use simple placeholders during video generation; final images will be externally generated and composited post-render

### Key Entities

- **Scene**: A distinct section of the video with its own timing, animations, and visual elements. Five scenes exist: Hallucination, Continuous Scale, Linear Regression, Non-Linear Regression, Synthesis.
- **Data Point**: A visual dot on the Cartesian grid representing an observation. Has x/y coordinates and consistent color.
- **Regression Line**: A mathematical line or curve fitted to data points, colored cyan, with associated equation display.
- **Error Bar**: A vertical red line from a data point to the regression line, representing the residual/error.
- **Node**: A circular element representing a neuron in the neural network visualization, with glow effect and internal symbol.
- **Color Palette**: The fixed set of 8 hex colors used consistently throughout all scenes.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Video renders completely without errors (render time is informational, not a constraint)
- **SC-002**: Video duration is exactly 120 seconds (plus or minus 0.1 second tolerance)
- **SC-003**: All 5 sections transition seamlessly without visible jumps or gaps
- **SC-004**: Animation frame rate maintains 60 FPS throughout playback (no dropped frames)
- **SC-005**: Video resolution is exactly 1920x1080 pixels (16:9 aspect ratio)
- **SC-006**: Each of the 5 scenes can be rendered independently for testing
- **SC-007**: Data points appear in identical positions across multiple renders (reproducibility)
- **SC-008**: All text elements are readable when viewed at 100% scale on a 1080p display
- **SC-009**: Color consistency: spot-checking 10 random frames shows only palette-defined colors for key elements
- **SC-010**: Neural network final phase contains at least 1,000 visible nodes

## Assumptions

- The viewer has access to a video player capable of 1080p60 playback
- The production environment has fonts available (Courier/RobotoMono, serif, Comic Sans/handwritten style) or suitable fallbacks
- Audio/voiceover integration is handled separately and is not part of this visual implementation scope
- The warning icon will be generated programmatically using vector graphics within the codebase (no external dependencies)
- Non-icon image assets use placeholders during development; final images are externally generated and composited after initial video render
- The target audience has no prior knowledge of regression or machine learning concepts
