from manim import *

from config import line_width
from data import dots
from KNN_Scene import KNN_Scene


class Scene1(KNN_Scene):
    tracker = ValueTracker(0)

    def construct(self):
        super(Scene1, self).construct()

        x = always_redraw(
            lambda: Annulus(inner_radius=.1, outer_radius=.18).move_to(
                [self.tracker.get_value(), self.tracker.get_value(), 0]))

        line0 = always_redraw(lambda: Line(
            x.get_center(),
            dots[0].get_center(),
            color=dots[0].color, buff=.2,
            stroke_width=line_width
        ))

        lines = [line0]
        self.add(x, *lines)

        self.play(self.tracker.animate.set_value(2), rate_func=linear, run_time=3)
        self.wait(3)
