import numpy as np
from manim import Circle

from src.data.dots.dots1 import labels1
from src.data.graphics_stuff import LABEL_COLORS
from src.data.lengths import dot_radius


def get_positions(_x_y_pos):
    return np.array([[float(line[0]), float(line[1]), 0] for line in _x_y_pos])


def get_dots(_positions):
    return [
        Circle(color=LABEL_COLORS[labels1[i]], radius=dot_radius, stroke_width=5, fill_opacity=.1).move_to(_positions[i])
        for i in range(len(_positions))]
