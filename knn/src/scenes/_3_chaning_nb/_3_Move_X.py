import os
from pathlib import Path

from manim import *
from numpy import sin

from general.data.dots.dots1 import positions, labels_3_classes
from general.data.dots.utils import get_dots, get_positions
from knn.src.scenes.KNN_Scene import KNN_Scene


class _3_Move_X(KNN_Scene):
    dots = get_dots(get_positions(positions), labels_3_classes)
    tracker = ValueTracker(0)

    def construct(self):
        self.play(Create(VGroup(*self.dots)))
        self.tracker.set_value(-2)
        self.k = 5
        self.x.add_updater(
            lambda it: it.move_to([2.5 * sin(2 * self.tracker.get_value()), self.tracker.get_value(), 0]))
        self.x.add_updater(lambda it: it.set_color(self.get_label_prediction(self.dots)))

        self.add(self.x, self.x_circle, self.get_k_group())
        self.add_nb_lines_with_updater(self.dots)

        self.play(self.tracker.animate.set_value(3), rate_func=linear, run_time=14)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} -pql")
