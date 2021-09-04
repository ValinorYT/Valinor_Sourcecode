import os
from pathlib import Path

from manim import *
from numpy import sin

from src.data.graphics_stuff import opacity_weak, opacity_medium
from src.data.dots.dots1 import dots
from src.data.lengths import dot_radius, line_width
from src.scenes.KNN_Scene import KNN_Scene
from src.utils.distances import dots_sorted_by_distance


class Changing_NB_1(KNN_Scene):

    def construct(self):
        self.play(Create(VGroup(*dots)))
        self.tracker.set_value(-4)

        self.add_dot_opacity_toggle()

        c1 = Circle(radius=dot_radius * 1.35, color="#EEEEEE", stroke_width=2)
        c1.add_updater(lambda it: it.move_to(self.x.get_center()))

        self.x.add_updater(lambda it: it.move_to([3.5 * sin(2*self.tracker.get_value()), self.tracker.get_value(), 0]))
        self.x.add_updater(lambda it: it.set_color(self.get_label_prediction()))
        self.add(self.x, c1)
        self.add_lines()

        self.play(self.tracker.animate.set_value(4), rate_func=linear, run_time=14)

    def add_dot_opacity_toggle(self):
        for dot in dots:
            dot.add_updater(
                lambda it: it.set_fill(
                    opacity=opacity_medium if it in dots_sorted_by_distance(self.x, dots)[:3] else opacity_weak))

    def add_lines(self):  # Hardcoded k = 3, as always_redraw can't be in a loop for some reason!?
        self.add(self.line_by_index(0))
        self.add(self.line_by_index(1))
        self.add(self.line_by_index(2))

    def line_by_index(self, idx):
        return always_redraw(lambda:
                             Line(
                                 start=self.x.get_center(),
                                 end=dots_sorted_by_distance(self.x, dots)[idx].get_center(),
                                 stroke_width=line_width,
                                 color=dots_sorted_by_distance(self.x, dots)[idx].get_color(),
                                 buff=dot_radius * 1.5)
                             )


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} Changing_NB_1 -pqp")
