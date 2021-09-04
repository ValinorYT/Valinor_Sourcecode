from manim import *

from src.config import background
from src.data import dots
from src.utils.colors import most_common_color
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
        self.x = Annulus(inner_radius=.08, outer_radius=.16)

    def get_label_prediction(self):
        k_neighbours = dots_sorted_by_distance(self.x, dots)[:3]
        return str(most_common_color([x.get_color() for x in k_neighbours])[0][0])
