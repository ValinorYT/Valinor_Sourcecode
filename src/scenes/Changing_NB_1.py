import os
from pathlib import Path

from manim import *
from numpy import sin

from src.config import line_width, dot_radius
from src.data import dots
from src.scenes.KNN_Scene import KNN_Scene
from src.utils.distances import dots_sorted_by_distance


class Changing_NB_1(KNN_Scene):

    def construct(self):
        self.play(Create(VGroup(*dots)))
        self.tracker.set_value(-4)
        self.x.add_updater(lambda it: it.move_to([4.5 * sin(self.tracker.get_value()), self.tracker.get_value(), 0]))
        self.add(self.x)
        self.add_lines()

        self.play(self.tracker.animate.set_value(4), rate_func=linear, run_time=8)

    def add_lines(self): # Hardcoded k = 3
        self.add(always_redraw(lambda:
                               Line(
                                   start=self.x.get_center(),
                                   end=dots_sorted_by_distance(self.x, dots)[0].get_center(),
                                   stroke_width=line_width,
                                   color=dots_sorted_by_distance(self.x, dots)[0].get_color(),
                                   buff=dot_radius * 1.5)
                               ))
        self.add(always_redraw(lambda:
                               Line(
                                   start=self.x.get_center(),
                                   end=dots_sorted_by_distance(self.x, dots)[1].get_center(),
                                   stroke_width=line_width,
                                   color=dots_sorted_by_distance(self.x, dots)[1].get_color(),
                                   buff=dot_radius * 1.5)
                               ))
        self.add(always_redraw(lambda:
                               Line(
                                   start=self.x.get_center(),
                                   end=dots_sorted_by_distance(self.x, dots)[2].get_center(),
                                   stroke_width=line_width,
                                   color=dots_sorted_by_distance(self.x, dots)[2].get_color(),
                                   buff=dot_radius * 1.5)
                               ))


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} Changing_NB_1 -pql")
