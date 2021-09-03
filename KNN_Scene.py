from manim import *

from config import background
from data import dots


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

    def construct(self):
        self.camera.background_color = background
        self.play(Create(VGroup(*dots)))
