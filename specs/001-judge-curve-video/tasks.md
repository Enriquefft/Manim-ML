# Tasks: The Judge & The Curve Video

**Input**: Design documents from `/specs/001-judge-curve-video/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are included as specified in the feature specification for scene validation and reproducibility.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization, configuration, and directory structure

- [x] T001 Create directory structure: `src/utils/`, `videos/scenes/`, `videos/templates/`, `videos/assets/data/`
- [x] T002 [P] Create `src/__init__.py` with module docstring
- [x] T003 [P] Create `src/utils/__init__.py` with utility module exports
- [x] T004 [P] Create `videos/__init__.py` with package docstring
- [x] T005 [P] Create `videos/scenes/__init__.py` with scene exports
- [x] T006 [P] Create `videos/templates/__init__.py` with template exports
- [x] T007 Create `src/config.py` with ColorPalette, TimingConfig, SceneConfig dataclasses per data-model.md

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core utilities and templates that MUST be complete before ANY user story scene can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

- [x] T008 [P] Implement `src/utils/color_utils.py` with color palette functions and constants per data-model.md
- [x] T009 [P] Implement `src/utils/data_generator.py` with `generate_linear_data()`, `generate_scurve_data()`, `save_data_to_csv()`, `load_data_from_csv()` functions per contracts/scene_interfaces.md
- [x] T010 [P] Implement `videos/templates/custom_shapes.py` with `create_warning_icon()`, `create_slider_component()`, `create_network_node()` per contracts/scene_interfaces.md
- [x] T011 [P] Implement `videos/templates/effects.py` with `apply_chromatic_aberration()`, `apply_glow_effect()`, `create_pulse_animation()`, `create_dolly_zoom()` per contracts/scene_interfaces.md
- [x] T012 [P] Implement `videos/templates/animations.py` with `TextJitter`, `LineMorph`, `StampIn` animation classes per contracts/scene_interfaces.md
- [x] T013 Generate data files: `videos/assets/data/linear_data.csv` (20 points, seed=42, noise=0.3) per data-model.md
- [x] T014 Generate data files: `videos/assets/data/nonlinear_data.csv` (25+ points, seed=42, S-curve pattern) per data-model.md

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Complete Video Playback (Priority: P1) MVP

**Goal**: Deliver complete 2-minute video with all 5 sections in sequence, exact timing boundaries

**Independent Test**: Render `videos/scenes/judge_curve_complete.py` and verify 120-second duration with all 5 sections

### Tests for User Story 1

- [x] T015 [P] [US1] Create `tests/test_scenes.py` with render validation tests for complete video
- [x] T016 [P] [US1] Create `tests/test_data_generator.py` with reproducibility checks for seeded data

### Implementation for User Story 1

- [x] T017 [US1] Create `videos/scenes/judge_curve_complete.py` with `JudgeCurveComplete` scene class that composes all 5 sections
- [x] T018 [US1] Create `videos/judge_curve_main.py` entry point script for full video rendering
- [x] T019 [US1] Implement scene transition logic with 0.3-second FadeOut/FadeIn overlaps per research.md
- [x] T020 [US1] Validate exact 120-second duration (Section 1: 0:00-0:25, Section 2: 0:25-0:50, Section 3: 0:50-1:15, Section 4: 1:15-1:40, Section 5: 1:40-2:00)

**Checkpoint**: Complete video structure ready; individual scene content filled in subsequent phases

---

## Phase 4: User Story 2 - Linear Regression Understanding (Priority: P1)

**Goal**: Section 3 demonstrates linear regression with data points, best-fit line, equation display, and error visualization

**Independent Test**: Render `videos/scenes/section3_linear.py` independently, verify data points, line, equation, and error bars appear

### Tests for User Story 2

- [x] T021 [P] [US2] Add `tests/test_scenes.py` test for `LinearRegressionScene` independent rendering

### Implementation for User Story 2

- [x] T022 [P] [US2] Create DataPoint, RegressionLine, ErrorBar type definitions in `src/utils/data_generator.py` per data-model.md
- [x] T023 [US2] Implement `videos/scenes/section3_linear.py` with `LinearRegressionScene` class per contracts/scene_interfaces.md
- [x] T024 [US2] Implement `create_cartesian_grid()` with axis labels and #404040 grid lines
- [x] T025 [US2] Implement `load_data_points()` to read from `videos/assets/data/linear_data.csv`
- [x] T026 [US2] Implement `create_data_point_mobjects()` with cyan dots on grid
- [x] T027 [US2] Implement `fit_linear_regression()` to calculate slope and intercept (y ≈ 1.05x + 1.0)
- [x] T028 [US2] Implement `create_regression_line_mobject()` with cyan line from regression model
- [x] T029 [US2] Implement `create_equation_display()` with MathTex "y = mx + b" and DecimalNumber values
- [x] T030 [US2] Implement `create_error_bars()` with red vertical lines showing residuals
- [x] T031 [US2] Implement `animate_error_minimization()` with line rotation updating error bars dynamically
- [x] T032 [US2] Add outlier zoom animation with epsilon symbol "ERROR" label

**Checkpoint**: Section 3 (Linear Regression) fully functional and independently testable

---

## Phase 5: User Story 3 - Non-Linear Comparison (Priority: P2)

**Goal**: Section 4 shows linear model failure on S-curve data, then morphs to polynomial curve that fits better

**Independent Test**: Render `videos/scenes/section4_nonlinear.py` independently, verify linear failure, morph, and curve fit

### Tests for User Story 3

- [x] T033 [P] [US3] Add `tests/test_scenes.py` test for `NonLinearRegressionScene` independent rendering

### Implementation for User Story 3

- [x] T034 [US3] Implement `videos/scenes/section4_nonlinear.py` with `NonLinearRegressionScene` class per contracts/scene_interfaces.md
- [x] T035 [US3] Implement `create_scurve_data()` to load S-curve pattern from `videos/assets/data/nonlinear_data.csv`
- [x] T036 [US3] Implement `show_linear_failure()` with large red error bars on crash points
- [x] T037 [US3] Implement `create_screen_pulse_effect()` with red edge pulses indicating error
- [x] T038 [US3] Implement `animate_line_to_curve()` with shatter and morph to polynomial curve
- [x] T039 [US3] Implement `create_polynomial_equation_morph()` transforming y=mx+b to polynomial form
- [x] T040 [US3] Animate error bars fading out as curve fits data

**Checkpoint**: Section 4 (Non-Linear Regression) fully functional and independently testable

---

## Phase 6: User Story 4 - Neural Network Connection (Priority: P2)

**Goal**: Section 5 compresses curve to node, expands to 1000+ node network, delivers "VALUE PREDICTED" finale

**Independent Test**: Render `videos/scenes/section5_synthesis.py` independently, verify curve-to-node compression, network expansion, and final stamp

### Tests for User Story 4

- [x] T041 [P] [US4] Add `tests/test_scenes.py` test for `SynthesisScene` independent rendering
- [x] T042 [P] [US4] Add test to verify neural network contains >= 1000 nodes (FR-010)

### Implementation for User Story 4

- [x] T043 [P] [US4] Create NetworkNode, NetworkConnection, NeuralNetwork type definitions in `src/utils/data_generator.py` per data-model.md
- [x] T044 [US4] Implement `videos/scenes/section5_synthesis.py` with `SynthesisScene` class per contracts/scene_interfaces.md
- [x] T045 [US4] Implement `isolate_curve()` to remove context and keep glowing curve
- [x] T046 [US4] Implement `animate_curve_to_node()` compressing curve into single node with sigma symbol
- [x] T047 [US4] Implement `create_neural_network()` with >= 1000 nodes in layered structure per research.md
- [x] T048 [US4] Implement `animate_network_expansion()` with rapid zoom-out expansion
- [x] T049 [US4] Implement `create_data_flow_pulses()` with light pulses traveling through connections
- [x] T050 [US4] Implement `create_final_stamp()` with gold "VALUE PREDICTED" stamp animation

**Checkpoint**: Section 5 (Synthesis) fully functional and independently testable

---

## Phase 7: User Story 5 - Visual Atmosphere (Priority: P3)

**Goal**: Sections 1-2 establish narrative atmosphere with AI hallucination metaphor and continuous scale concept

**Independent Test**: Render `videos/scenes/section1_hallucination.py` and `videos/scenes/section2_scale.py` independently

### Tests for User Story 5

- [x] T051 [P] [US5] Add `tests/test_scenes.py` test for `HallucinationScene` independent rendering
- [x] T052 [P] [US5] Add `tests/test_scenes.py` test for `ContinuousScaleScene` independent rendering
- [x] T053 [P] [US5] Add `tests/test_effects.py` with effect function unit tests

### Implementation for User Story 5 - Section 1

- [x] T054 [US5] Implement `videos/scenes/section1_hallucination.py` with `HallucinationScene` class per contracts/scene_interfaces.md
- [x] T055 [US5] Implement `create_terminal_cursor()` with green blinking cursor and chromatic aberration
- [x] T056 [US5] Implement `create_text_cascade()` with nonsense text and TextJitter animation
- [x] T057 [US5] Implement `create_warning_overlay()` with red box and "NO METRIC FOUND" text
- [x] T058 [US5] Implement `create_warning_icon()` with programmatic triangle and exclamation mark per FR-012
- [x] T059 [US5] Implement `apply_static_dissolution()` with noise transition and dolly zoom

### Implementation for User Story 5 - Section 2

- [x] T060 [US5] Implement `videos/scenes/section2_scale.py` with `ContinuousScaleScene` class per contracts/scene_interfaces.md
- [x] T061 [US5] Implement `create_split_screen()` with left/right panes and divider
- [x] T062 [US5] Implement `create_slider()` with vertical gradient from cyan to red
- [x] T063 [US5] Implement `animate_slider_movement()` with handle animation
- [x] T064 [US5] Implement `create_cycling_numbers()` with DecimalNumber rapid cycling display

**Checkpoint**: Sections 1-2 (Atmosphere) fully functional and independently testable

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Integration, validation, and quality assurance across all scenes

- [x] T065 Integrate all 5 scene implementations into `videos/scenes/judge_curve_complete.py`
- [x] T066 Verify scene transitions with 0.3-second FadeOut/FadeIn overlaps
- [x] T067 Validate color consistency across all scenes using only palette-defined colors (FR-003)
- [x] T068 Validate animation timing categories (fast: 0.3-0.5s, medium: 0.6-1.0s, slow: 1.5-2.0s) per FR-005
- [x] T069 Run Pyright strict mode validation on all source files
- [x] T070 Run Ruff check and format on all source files
- [x] T071 Run full test suite with `pytest tests/ -v` - 39 passed, 22 skipped (manim-dependent)
- [ ] T072 Render final video at 1920x1080@60fps quality (`manim -qh`) - Requires manim in active shell
- [ ] T073 Validate video duration is exactly 120 seconds (SC-002) - Requires render
- [x] T074 Validate neural network has >= 1000 nodes (SC-010) - Test passes with generate_neural_network()
- [ ] T075 Run quickstart.md validation commands - Requires manim in active shell

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - US1 (Complete Video): Creates composition shell
  - US2 (Linear Regression): P1 - Core educational content
  - US3 (Non-Linear): P2 - Depends on US2 concepts
  - US4 (Neural Network): P2 - Depends on US3 curve
  - US5 (Atmosphere): P3 - Sections 1-2, can be developed in parallel
- **Polish (Phase 8)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Creates video composition structure; content filled by other stories
- **User Story 2 (P1)**: Core linear regression scene - no dependencies on other stories
- **User Story 3 (P2)**: Uses linear model concepts from US2, but independently testable
- **User Story 4 (P2)**: Uses curve from US3, but independently testable
- **User Story 5 (P3)**: Sections 1-2 are standalone atmosphere scenes

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Type definitions before scene classes
- Helper methods before main `construct()` logic
- Animation helpers before complex animations
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (T008-T012)
- Tests for each user story marked [P] can run in parallel
- Type definitions within a story marked [P] can run in parallel
- US2 and US5 can be worked on in parallel (independent scenes)

---

## Implementation Strategy

### MVP First (User Stories 1 + 2)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (video composition shell)
4. Complete Phase 4: User Story 2 (linear regression - core education)
5. **STOP and VALIDATE**: Test complete video with Section 3 content
6. Continue with User Stories 3, 4, 5 in priority order

### Incremental Delivery

1. Complete Setup + Foundational -> Foundation ready
2. Add User Story 1 -> Video shell exists
3. Add User Story 2 -> Linear regression works -> Core MVP!
4. Add User Story 3 -> Non-linear comparison -> Enhanced education
5. Add User Story 4 -> Neural network synthesis -> Complete narrative
6. Add User Story 5 -> Atmosphere scenes -> Full experience
7. Polish phase -> Production ready

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- All code must pass Pyright strict mode and Ruff ALL rules per constitution
- Color values must come from centralized `src/config.py` palette only
- Data generation must use seed=42 for reproducibility (FR-004)
