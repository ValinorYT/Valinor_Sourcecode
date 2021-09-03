import os
from pathlib import Path

from manim import *

from config import line_width
from data import dots, positions
from KNN_Scene import KNN_Scene
import numpy as np


class Scene1(KNN_Scene):
    tracker = ValueTracker(0)

    def construct(self):
        super(Scene1, self).construct()

        def get_closest_dot():
            pos = np.array(positions)
            diff = pos - x.get_center()
            distances = np.linalg.norm(diff)
            return dots[np.argmin(distances)]

        x = always_redraw(
            lambda: Annulus(inner_radius=.1, outer_radius=.18).move_to(
                [self.tracker.get_value(), self.tracker.get_value(), 0]))

        line0 = always_redraw(lambda: Line(
            x.get_center(),
            get_closest_dot().get_center(),
            color=dots[0].color, buff=.2,
            stroke_width=line_width
        ))

        lines = [line0]
        self.add(x, *lines)

        self.play(self.tracker.animate.set_value(2), rate_func=linear, run_time=3)
        self.wait(3)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} Scene1 -pql")