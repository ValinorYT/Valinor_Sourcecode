from manim import *
from src.data.graphics_stuff import background
from src.data.dots.dots1 import dots
from src.data.lengths import x_radius_big, x_radius_small

from src.utils.color_utils import most_common_color
from src.utils.distances import dots_sorted_by_distance


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

    def __init__(self):
        super().__init__()
        self.camera.background_color = background
        self.x = Annulus(inner_radius=x_radius_small, outer_radius=x_radius_big)

    def get_label_prediction(self):
        k_neighbours = dots_sorted_by_distance(self.x, dots)[:3]
        return most_common_color([x.get_color() for x in k_neighbours])[0]
