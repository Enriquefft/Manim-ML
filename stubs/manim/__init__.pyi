"""Manim - Animation engine for explanatory videos."""

from __future__ import annotations

from typing import Any, Callable, Sequence

__version__: str
__all__: list[str]

# ==== Core Mobject Classes ====
class Mobject:
    """Base class for all mobjects."""

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def get_color(self) -> tuple[float, float, float]: ...
    def set_color(self, color: str | tuple[float, float, float]) -> Mobject: ...
    def add(self, *mobjects: Mobject) -> Mobject: ...
    def remove(self, *mobjects: Mobject) -> Mobject: ...
    def add_updater(self, update_func: Callable[[Mobject], Mobject]) -> Mobject: ...
    def shift(self, vector: tuple[float, float, float] | Sequence[float]) -> Mobject: ...
    def move_to(self, point: tuple[float, float, float] | Sequence[float] | Mobject) -> Mobject: ...
    def rotate(self, angle: float, **kwargs: Any) -> Mobject: ...
    def scale(self, scale_factor: float) -> Mobject: ...
    def fade(self, darkness: float = ...) -> Mobject: ...
    @property
    def animate(self) -> Any: ...

class VMobject(Mobject):
    """Vector Mobject."""
    pass

class OpenGLMobject(Mobject):
    """OpenGL Mobject."""
    pass

class OpenGLVMobject(VMobject):
    """OpenGL Vector Mobject."""
    pass

# ==== Geometry Shapes ====
class Line(VMobject):
    """Line shape."""
    def __init__(self, start: tuple[float, float, float] | Sequence[float] = ..., end: tuple[float, float, float] | Sequence[float] = ..., **kwargs: Any) -> None: ...

class DashedLine(Line):
    """Dashed line shape."""
    pass

class Arc(VMobject):
    """Arc shape."""
    pass

class Circle(VMobject):
    """Circle shape."""
    def __init__(self, radius: float = ..., **kwargs: Any) -> None: ...

class Rectangle(VMobject):
    """Rectangle shape."""
    def __init__(self, width: float = ..., height: float = ..., **kwargs: Any) -> None: ...

class Square(VMobject):
    """Square shape."""
    def __init__(self, side_length: float = ..., **kwargs: Any) -> None: ...

class Polygon(VMobject):
    """Polygon shape."""
    def __init__(self, *vertices: Sequence[float], **kwargs: Any) -> None: ...

class Triangle(Polygon):
    """Triangle shape."""
    pass

class RegularPolygon(Polygon):
    """Regular polygon shape."""
    pass

# ==== Text and Math ====
class Text(VMobject):
    """Text mobject."""
    def __init__(self, text: str, **kwargs: Any) -> None: ...

class MathTex(VMobject):
    """LaTeX math text."""
    def __init__(self, *tex_strings: str, **kwargs: Any) -> None: ...

class Tex(VMobject):
    """LaTeX text."""
    def __init__(self, *tex_strings: str, **kwargs: Any) -> None: ...

class SingleStringMathTex(MathTex):
    """Single string LaTeX math."""
    pass

# ==== Animations - Base ====
class Animation:
    """Base animation class."""
    def __init__(self, *mobjects: Mobject, **kwargs: Any) -> None: ...

# ==== Animations - Creation ====
class Create(Animation):
    """Animation that creates a mobject."""
    pass

class DrawBorderThenFill(Animation):
    """Animation that draws border then fills."""
    pass

class Write(Animation):
    """Animation that writes text."""
    pass

class ShowPartial(Animation):
    """Animation that shows partial."""
    pass

class AddTextLetterByLetter(Animation):
    """Animation that adds text letter by letter."""
    pass

class ShowIncreasingSubsets(Animation):
    """Animation that shows increasing subsets."""
    pass

class ShowSubmobjectsOneByOne(Animation):
    """Animation that shows submobjects one by one."""
    pass

class Uncreate(Animation):
    """Animation that uncreates a mobject."""
    pass

# ==== Animations - Fading ====
class FadeIn(Animation):
    """Animation that fades in a mobject."""
    pass

class FadeOut(Animation):
    """Animation that fades out a mobject."""
    pass

class FadeInFrom(Animation):
    """Animation that fades in from direction."""
    pass

class FadeOutAndShiftDown(Animation):
    """Animation that fades out and shifts down."""
    pass

# ==== Animations - Composition ====
class AnimationGroup(Animation):
    """Group multiple animations."""
    def __init__(self, *animations: Animation, **kwargs: Any) -> None: ...

class Succession(AnimationGroup):
    """Play animations in succession."""
    pass

class Sequential(AnimationGroup):
    """Sequential animations."""
    pass

# ==== Animations - Transform ====
class Transform(Animation):
    """Transform one mobject to another."""
    pass

class ReplacementTransform(Transform):
    """Replacement transform."""
    pass

class TransformFromCopy(Transform):
    """Transform from copy."""
    pass

class ClockwiseTransform(Transform):
    """Clockwise transform."""
    pass

class CounterclockwiseTransform(Transform):
    """Counterclockwise transform."""
    pass

# ==== Animations - Movement ====
class ApplyMethod(Animation):
    """Apply a method as animation."""
    pass

class ApplyFunction(Animation):
    """Apply a function to mobject."""
    pass

class ApplyMatrix(Animation):
    """Apply matrix transform."""
    pass

class ApplyComplexFunction(Animation):
    """Apply complex function."""
    pass

class Homotopy(Animation):
    """Homotopy animation."""
    pass

class SmoothedVMobjectPointFromPointMethod(Animation):
    """Smoothed point from point animation."""
    pass

# ==== Animations - Rotation ====
class Rotate(Animation):
    """Rotation animation."""
    pass

# ==== Animations - Indication ====
class Indicate(Animation):
    """Indication animation."""
    pass

class Flash(Animation):
    """Flash animation."""
    pass

class ShowCreationThenDestruction(Animation):
    """Show creation then destruction."""
    pass

class Circumscribe(Animation):
    """Circumscribe animation."""
    pass

class ShowCreationThenFadeOut(Animation):
    """Show creation then fade out."""
    pass

class ApplyWave(Animation):
    """Apply wave animation."""
    pass

class WiggleOutThenIn(Animation):
    """Wiggle out then in."""
    pass

class TurnInsideOut(Animation):
    """Turn inside out."""
    pass

class FlashAround(Animation):
    """Flash around."""
    pass

class ShowPassingFlash(Animation):
    """Show passing flash."""
    pass

class ShowPassingFlashAround(Animation):
    """Show passing flash around."""
    pass

# ==== Scene ====
class Scene:
    """Base scene class."""

    def __init__(self, **kwargs: Any) -> None: ...
    def construct(self) -> None: ...
    def play(self, *animations: Any, **kwargs: Any) -> None: ...
    def add(self, *mobjects: Mobject) -> Scene: ...
    def remove(self, *mobjects: Mobject) -> Scene: ...
    def wait(self, duration: float = ...) -> None: ...

class MovingCameraScene(Scene):
    """Scene with moving camera."""
    pass

class ZoomedScene(Scene):
    """Scene with zoom."""
    pass

# ==== Utility Classes ====
class ValueTracker(Mobject):
    """Tracks and animates a value."""

    def __init__(self, initial_value: float = ..., **kwargs: Any) -> None: ...
    def get_value(self) -> float: ...
    def set_value(self, value: float) -> ValueTracker: ...

class Color:
    """Color class."""
    def __init__(self, color: str | tuple[float, float, float]) -> None: ...

# ==== Rate Functions ====
def linear(t: float) -> float: ...
def smooth(t: float) -> float: ...
def ease_in_quad(t: float) -> float: ...
def ease_out_quad(t: float) -> float: ...
def ease_in_out_quad(t: float) -> float: ...
def ease_in_cubic(t: float) -> float: ...
def ease_out_cubic(t: float) -> float: ...
def ease_in_out_cubic(t: float) -> float: ...
def ease_in_quart(t: float) -> float: ...
def ease_out_quart(t: float) -> float: ...
def ease_in_out_quart(t: float) -> float: ...
def ease_in_quint(t: float) -> float: ...
def ease_out_quint(t: float) -> float: ...
def ease_in_out_quint(t: float) -> float: ...
def ease_in_sine(t: float) -> float: ...
def ease_out_sine(t: float) -> float: ...
def ease_in_out_sine(t: float) -> float: ...
def ease_in_back(t: float) -> float: ...
def ease_out_back(t: float) -> float: ...
def ease_in_out_back(t: float) -> float: ...
def ease_in_elastic(t: float) -> float: ...
def ease_out_elastic(t: float) -> float: ...
def ease_in_out_elastic(t: float) -> float: ...
def ease_in_bounce(t: float) -> float: ...
def ease_out_bounce(t: float) -> float: ...
def ease_in_out_bounce(t: float) -> float: ...

# Rate functions module namespace
class rate_functions:
    """Rate functions module."""
    linear: Any
    smooth: Any
    ease_in_quad: Any
    ease_out_quad: Any
    ease_in_out_quad: Any
    ease_in_cubic: Any
    ease_out_cubic: Any
    ease_in_out_cubic: Any

# ==== Colors ====
WHITE: tuple[float, float, float]
BLACK: tuple[float, float, float]
RED: tuple[float, float, float]
GREEN: tuple[float, float, float]
BLUE: tuple[float, float, float]
YELLOW: tuple[float, float, float]
ORANGE: tuple[float, float, float]
PURPLE: tuple[float, float, float]
PINK: tuple[float, float, float]
CYAN: tuple[float, float, float]
GRAY: tuple[float, float, float]
DARK_GRAY: tuple[float, float, float]
LIGHT_GRAY: tuple[float, float, float]
TEAL: tuple[float, float, float]
LIGHT_BLUE: tuple[float, float, float]
DARK_BLUE: tuple[float, float, float]
LIGHT_GREEN: tuple[float, float, float]
DARK_GREEN: tuple[float, float, float]
MAROON: tuple[float, float, float]
GOLD: tuple[float, float, float]

# ==== Directions ====
UP: tuple[float, float, float]
DOWN: tuple[float, float, float]
LEFT: tuple[float, float, float]
RIGHT: tuple[float, float, float]
IN: tuple[float, float, float]
OUT: tuple[float, float, float]
ORIGIN: tuple[float, float, float]

# ==== Helper Functions ====
def config(*args: Any, **kwargs: Any) -> Any: ...
def rgb_to_hex(color: tuple[float, float, float]) -> str: ...
def hex_to_rgb(hex_color: str) -> tuple[float, float, float]: ...
