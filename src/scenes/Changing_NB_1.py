import os
from pathlib import Path

from manim import *
from numpy import sin

from src.config import line_width, dot_radius
from src.data import dots
from src.scenes.KNN_Scene import KNN_Scene


class Changing_NB_1(KNN_Scene):
    k = 1

    def construct(self):
        self.play(Create(VGroup(*dots)))
        self.tracker.set_value(-4)
        self.x.add_updater(lambda it: it.move_to([4.5 * sin(self.tracker.get_value()), self.tracker.get_value(), 0]))
        line1 = always_redraw(lambda:
                              Line(
                                  start=self.x.get_center(),
                                  end=self.get_nearest_dot().get_center(),
                                  stroke_width=line_width,
                                  color=self.get_nearest_dot().get_color(),
                                  buff=dot_radius * 1.5)
                              )
        self.add(line1, self.x)
        self.play(self.tracker.animate.set_value(4), rate_func=linear, run_time=8)
        self.wait(3)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} Changing_NB_1 -pql")
