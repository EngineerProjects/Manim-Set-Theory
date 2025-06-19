from manim import *
import numpy as np

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        self.play(Create(circle))

class SquareToCircle(Scene):
    def construct(self):

        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.rotate(PI / 4)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.set_fill(BLUE, opacity=0.5)

        square.next_to(circle, RIGHT, buff=0.5)
        self.play(Create(circle), Create(square))


class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(LEFT * 2)
        right_square = Square(color=RED, fill_opacity=0.7).shift(RIGHT * 2)

        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI/2, about_point=ORIGIN), run_time=2
        )

        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )

        self.play(
            left_square.animate.shift(UP * 2),
            right_square.animate.shift(DOWN * 2),
            run_time=2
        )

        self.wait()


class TwoTransforms(Scene):
    def transform(self):
        a = Circle()
        b = Square()
        c = Triangle()

        self.play(Transform(a, b))
        self.play(Transform(a, c))
        self.play(FadeOut(a))

    def replacement_transform(self):
        a = Circle()
        b = Square()
        c = Triangle()

        self.play(ReplacementTransform(a, b))
        self.play(ReplacementTransform(b, c))
        self.play(FadeOut(c))

    def construct(self):
        self.transform()
        self.wait(0.5) # Wait to see the first transform
        self.replacement_transform()

# ========================= custom animations =========================

class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        super().__init__(number, **kwargs)
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set the value of the number based on alpha
        value = self.start + (self.end - self.start) * alpha
        self.mobject.set_value(value)


class CountingScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        number = DecimalNumber().set_color(GREEN).scale(5)
        number.add_updater(lambda number: number.move_to(ORIGIN))

        self.add(number)

        self.wait()

        self.play(Count(number, 0, 100), run_time=4, rate_func = linear)
        self.wait()
      

# =========================Config end =========================

class VMobjectDemo(Scene):
    def construct(self):
        plane = NumberPlane()
        my_vmobject = VMobject(color=GREEN)
        my_vmobject.points = [
            np.array([-2, -1, 0]),  # start of first curve
            np.array([-3, 1, 0]),
            np.array([0, 3, 0]),
            np.array([1, 3, 0]),  # end of first curve
            np.array([1, 3, 0]),  # start of second curve
            np.array([0, 1, 0]),
            np.array([4, 3, 0]),
            np.array([4, -2, 0]),  # end of second curve
        ]
        handles = [
            Dot(point, color=RED) for point in
            [[-3, 1, 0], [0, 3, 0], [0, 1, 0], [4, 3, 0]]
        ]
        handle_lines = [
            Line(
                my_vmobject.points[ind],
                my_vmobject.points[ind+1],
                color=RED,
                stroke_width=2
            ) for ind in range(0, len(my_vmobject.points), 2)
        ]
        self.add(plane, *handles, *handle_lines, my_vmobject)