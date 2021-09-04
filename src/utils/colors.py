from collections import Counter

from manim import Dot

from src.data import dots
from src.utils.HashWrapper import HashWrapper
from src.utils.distances import dots_sorted_by_distance


def most_common_color(colors):
    wrapped_colors = [HashWrapper(c) for c in colors]
    return Counter(wrapped_colors).most_common()


my_dots = dots_sorted_by_distance(Dot([0, 0, 0]), dots)
my_colors = [d.get_color() for d in my_dots]
print(type(most_common_color(my_colors)[0][0]))
