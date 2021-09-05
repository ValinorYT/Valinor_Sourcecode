import os
from pathlib import Path

from manim import *
from numpy import sin

from src.data.dots.dots1 import positions, labels_3_classes
from src.data.dots.utils import get_dots, get_positions
from src.scenes.KNN_Scene import KNN_Scene


class Changing_NB_1(KNN_Scene):
    dots = get_dots(get_positions(positions), labels_3_classes)

    def construct(self):
        self.play(Create(VGroup(*self.dots)))
        self.tracker.set_value(-4)

        self.x.add_updater(
            lambda it: it.move_to([3.5 * sin(2 * self.tracker.get_value()), self.tracker.get_value(), 0]))
        self.x.add_updater(lambda it: it.set_color(self.get_label_prediction(self.dots)))

        self.add(self.x, self.x_circle)
        self.add_nb_lines(self.dots)

        self.play(self.tracker.animate.set_value(4), rate_func=linear, run_time=14)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} Changing_NB_1 -pqp")
