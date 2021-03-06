import os
from pathlib import Path

from manim import *

from general.data.dots.dots1 import positions, labels_2_classes
from general.data.dots.utils import get_dots, get_positions
from general.data.graphics_stuff import LABEL_COLORS
from knn.src.scenes.KNN_Scene import KNN_Scene


class _1_1_IntroductionScene(KNN_Scene):
    dots = get_dots(get_positions(positions), labels_2_classes)

    def construct(self):
        self.play(Create(VGroup(*self.dots)))

        self.x.move_to([.8, 1.13, 0])
        self.add(self.x, self.x_circle)
        self.indicate_object(self.x)

        self.wait(2)
        self.add(self.line_by_index(0, self.dots))
        self.wait(2)
        self.play(self.x.animate.set_color(LABEL_COLORS[0]), run_time=.6)
        self.wait(2)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} -pql")
