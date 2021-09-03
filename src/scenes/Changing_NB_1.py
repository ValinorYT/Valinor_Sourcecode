import os
from pathlib import Path

from manim import *
from numpy import sin

from src.config import line_width
from src.scenes.KNN_Scene import KNN_Scene


class Changing_NB_1(KNN_Scene):

    def construct(self):
        KNN_Scene.construct(self)
        self.tracker.set_value(-5)
        self.x.add_updater(lambda it: it.move_to([2.5 * sin(self.tracker.get_value()), self.tracker.get_value(), 0]))
        line1 = always_redraw(lambda:
                              Line(
                                  start=self.x.get_center(),
                                  end=self.get_nearest_dot(),
                                  stroke_width=line_width,
                                  color=RED)
                              )
        self.add(line1)
        self.play(self.tracker.animate.set_value(4), rate_func=linear, run_time=6)
        self.wait(3)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} Changing_NB_1 -pqm")
