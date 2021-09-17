import numpy as np
from manim import Circle

from general.data.graphics_stuff import LABEL_COLORS
from general.data.lengths import dot_radius


def get_positions(_x_y_pos):
    return np.array([[float(line[0]), float(line[1]), 0] for line in _x_y_pos])


def get_dots(_positions, _labels):
    return [
        Circle(color=LABEL_COLORS[_labels[i]], radius=dot_radius, stroke_width=8, fill_opacity=.4).move_to(_positions[i])
        for i in range(len(_positions))]
