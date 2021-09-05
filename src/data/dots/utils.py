import numpy as np
from manim import Dot

from src.data.graphics_stuff import LABEL_COLORS
from src.data.lengths import dot_radius


def get_positions(_x_y_pos):
    return np.array([[float(line[0]), float(line[1]), 0] for line in _x_y_pos])


def get_dots(_positions, _labels):
    return [
        Dot(color=LABEL_COLORS[_labels[i]], radius=dot_radius).move_to(_positions[i])
        for i in range(len(_positions))]
