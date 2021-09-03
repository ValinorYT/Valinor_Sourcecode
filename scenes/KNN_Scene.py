import os
from pathlib import Path

from manim import *

from config import background, line_width
from data import dots, positions


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
        self.x = always_redraw(
            lambda: Annulus(inner_radius=.1, outer_radius=.18).move_to(
                [self.tracker.get_value(), self.tracker.get_value(), 0]))

        self.line0 = always_redraw(lambda: Line(
            self.x.get_center(),
            positions[0],
            color=dots[0].color, buff=.2,
            stroke_width=line_width))

        self.lines = [self.line0]

        self.add(self.x)

    def construct(self):
        self.play(Create(VGroup(*dots)))

