import math
import os
from pathlib import Path

from colour import Color
from manim import *
from numpy import sin

from knn.src.data.dots.dots1 import positions, labels_3_classes
from knn.src.data.dots.utils import get_positions
from knn.src.data.graphics_stuff import OFF_WHITE
from knn.src.data.lengths import stroke_width
from knn.src.scenes.KNN_Scene import KNN_Scene

radius_factor = .3


def radius_formula(val):
    return .22 * math.sqrt(val + .7)


y_vals = [
    1.4,
    0.2,
    1.7,
    2.54,
    2.52,
    0.2,
    0.88,
    1.4,
    .98,
    2.25,
    0.24,
    0.0,
    2.4,
    1.45,
    0.55,
    1.42,
    0.0
]


def color_by_interpolation(val):
    return interpolate_color(Color("#504945"), Color("#fbf0c9"), val / max(*y_vals))


class _5_RegressionScene(KNN_Scene):
    dots = [Dot(radius=radius_formula(y_vals[i]),
                color=color_by_interpolation(y_vals[i]),
                stroke_color=BLACK,
                stroke_opacity=.5,
                stroke_width=stroke_width).move_to(get_positions(positions)[i])
            for i in range(len(get_positions(positions)))]

    tracker = ValueTracker(0)

    def construct(self):
        self.play(Create(VGroup(*self.dots)))

        for idx in range(len(self.dots)):
            self.add(Text(str(y_vals[idx])).scale(.44)
                     .next_to(self.dots[idx].get_center(), UP, buff=self.dots[idx].radius +.05))

        self.tracker.set_value(-4)
        self.k = 5

        self.x = always_redraw(lambda:
                               Dot(radius=radius_formula(self.get_y_mean()),
                                   color=color_by_interpolation(self.get_y_mean()),
                                   point=[3 * sin(2 * self.tracker.get_value()), self.tracker.get_value(), 0],
                                   stroke_color=BLACK,
                                   stroke_opacity=.5,
                                   stroke_width=stroke_width
                                   )
                               )
        x_value_prediction = always_redraw(lambda:
                                           Text(str(round(self.get_y_mean(), ndigits=2)))
                                           .scale(.4)
                                           .next_to(self.x.get_center(),
                                                    UP,
                                                    buff=.47)
                                           )

        self.add(self.x, self.get_k_group(), x_value_prediction)
        self.add_nb_lines_with_updater(self.dots)

        self.play(self.tracker.animate.set_value(4), rate_func=linear, run_time=20)

    def get_y_mean(self):
        x_np = np.array(self.x.get_center())
        k_neighbours = sorted(self.dots, key=lambda j: np.linalg.norm(x_np - np.array(j.get_center())))[:self.k]

        return float(np.mean([y_vals[self.dots.index(d)] for d in k_neighbours]))


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} -pqp")
