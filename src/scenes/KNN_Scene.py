from manim import *

from src.config import background
from src.data import dots, positions
from src.utils.distances import nearest_pos


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

        self.x = Annulus(inner_radius=.1, outer_radius=.18)

        self.add(self.x)

    def construct(self):
        self.play(Create(VGroup(*dots)))

    def get_nearest_dot(self):
        return nearest_pos(self.x.get_center(), positions)
