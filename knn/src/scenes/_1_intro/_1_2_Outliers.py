import os
from pathlib import Path

from manim import *

from knn.src.data.dots.dots1 import positions, labels_3_classes
from knn.src.data.dots.utils import get_dots, get_positions
from knn.src.data.graphics_stuff import LABEL_COLORS
from knn.src.scenes.KNN_Scene import KNN_Scene
from knn.src.utils.distances import stuff_sorted_by_distance


class _1_2_Outliers(KNN_Scene):
    dots = get_dots(get_positions(positions), labels_3_classes)

    def construct(self):
        self.play(Create(VGroup(*self.dots)))

        self.x.move_to([-2.5, 2.6, 0])
        self.add(self.x, self.x_circle)
        self.indicate_object(self.x)
        self.wait(2)

        self.indicate_object(stuff_sorted_by_distance(self.x, self.dots)[0])
        self.play(self.x.animate.set_color(LABEL_COLORS[1]), run_time=.6)
        self.wait(2)

        self.indicate_object(stuff_sorted_by_distance(self.x, self.dots)[1])
        self.indicate_object(stuff_sorted_by_distance(self.x, self.dots)[2])
        self.play(self.x.animate.set_color(LABEL_COLORS[0]), run_time=.6)
        self.wait(2)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} -pqp")
