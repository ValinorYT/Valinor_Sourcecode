import os
from pathlib import Path

from manim import *
from numpy import sin

from src.data.dots.dots1 import positions
from src.data.dots.utils import get_dots, get_positions
from src.data.graphics_stuff import OFF_WHITE
from src.data.lengths import dot_radius, x_radius_circle
from src.scenes.KNN_Scene import KNN_Scene, change_opacity_by_condition
from src.utils.distances import dots_sorted_by_distance


class Changing_NB_1(KNN_Scene):
    dots = get_dots(get_positions(positions))

    def construct(self):
        self.play(Create(VGroup(*self.dots)))
        self.tracker.set_value(-4)

        change_opacity_by_condition(lambda a: dots_sorted_by_distance(self.x, a)[:self.k], self.dots)

        c1 = Circle(radius=dot_radius * x_radius_circle, color=OFF_WHITE, stroke_width=2)
        c1.add_updater(lambda it: it.move_to(self.x.get_center()))

        self.x.add_updater(
            lambda it: it.move_to([3.5 * sin(2 * self.tracker.get_value()), self.tracker.get_value(), 0]))
        self.x.add_updater(lambda it: it.set_color(self.get_label_prediction(self.dots)))
        self.add(self.x, c1)
        self.add_nb_lines(self.dots)

        self.play(self.tracker.animate.set_value(4), rate_func=linear, run_time=14)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} Changing_NB_1 -pql")
