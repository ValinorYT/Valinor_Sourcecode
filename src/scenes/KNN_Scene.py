from manim import *

from src.data.dots.dots1 import dots
from src.data.graphics_stuff import BACKGROUND_COLOR, opacity_medium, opacity_weak
from src.data.lengths import x_radius_outer, x_radius_inner, line_width, dot_radius
from src.utils.color_utils import most_common_color
from src.utils.distances import dots_sorted_by_distance


def change_opacity_by_condition(condition):
    for dot in dots:
        dot.add_updater(
            lambda it: it.set_fill(
                opacity=opacity_medium if it in condition(dots) else opacity_weak))


class KNN_Scene(Scene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -5,
        "y_max": 5,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        "axes_color": WHITE
    }

    tracker = ValueTracker(0)
    k = 5

    def __init__(self):
        super().__init__()
        self.camera.background_color = BACKGROUND_COLOR
        self.x = Annulus(inner_radius=x_radius_inner, outer_radius=x_radius_outer)

    def get_label_prediction(self):
        k_neighbours = dots_sorted_by_distance(self.x, dots)[:self.k]
        return most_common_color([x.get_color() for x in k_neighbours])[0]

    def add_nb_lines(self):
        for j in range(self.k):
            self.add(self.line_by_index(j))

    def line_by_index(self, idx):
        return always_redraw(lambda:
                             Line(
                                 start=self.x.get_center(),
                                 end=dots_sorted_by_distance(self.x, dots)[idx].get_center(),
                                 stroke_width=line_width,
                                 color=dots_sorted_by_distance(self.x, dots)[idx].get_color(),
                                 buff=dot_radius * 1.5)
                             )
