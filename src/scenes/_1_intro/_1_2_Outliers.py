import os
from pathlib import Path

from manim import *

from src.data.dots.dots1 import positions, labels_3_classes
from src.data.dots.utils import get_dots, get_positions
from src.data.graphics_stuff import LABEL_COLORS
from src.scenes.KNN_Scene import KNN_Scene


class Outliers(KNN_Scene):
    dots = get_dots(get_positions(positions), labels_3_classes)

    def construct(self):
        self.play(Create(VGroup(*self.dots)))

        self.x.move_to([-2.5, 2.6, 0])
        self.add(self.x, self.x_circle)
        self.indicate_x()
        self.wait(2)
        self.play(self.x.animate.set_color(LABEL_COLORS[1]), run_time=.6)
        self.wait(2)
        self.play(self.x.animate.set_color(LABEL_COLORS[0]), run_time=.6)
        self.wait(2)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} Outliers -pql")
