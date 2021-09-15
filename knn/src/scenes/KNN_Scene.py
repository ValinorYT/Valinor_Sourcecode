from manim import *
from manim import Broadcast, Circle

from knn.src.data.graphics_stuff import BACKGROUND_COLOR, OFF_WHITE
from knn.src.data.lengths import line_width, dot_radius
from knn.src.utils.color_utils import most_common_color
from knn.src.utils.distances import stuff_sorted_by_distance


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

    k = 3

    def __init__(self):
        super().__init__()
        self.camera.background_color = BACKGROUND_COLOR
        self.x = Dot(radius=dot_radius * 1.3)
        self.x_circle = Circle(radius=self.x.radius * 1.2, color=OFF_WHITE, stroke_width=2)
        self.x_circle.add_updater(lambda it: it.move_to(self.x.get_center()))

    def get_label_prediction(self, dots):
        k_neighbours = stuff_sorted_by_distance(self.x, dots)[:self.k]
        return most_common_color([x.get_color() for x in k_neighbours])[0]

    def add_nb_lines_with_updater(self, dots):
        for j in range(self.k):
            self.add(self.line_by_index(j, dots))

    def line_by_index(self, idx, dots):
        return always_redraw(lambda:
                             Line(
                                 start=self.x.get_center() + [0, 0, -1],
                                 end=stuff_sorted_by_distance(self.x, dots)[idx].get_center() + [0, 0, -1],
                                 stroke_width=line_width,
                                 color=stuff_sorted_by_distance(self.x, dots)[idx].get_color(),
                                 buff=dot_radius * 2.2)
                             )

    def indicate_object(self, obj):
        self.play(
            Broadcast(Circle(color=OFF_WHITE, radius=dot_radius * 3.5),
                      n_mobs=1, focal_point=obj.get_center(), run_time=.6))

    def get_k_group(self):
        k_text = Text(f"k = {self.k}") \
            .scale(.8).to_edge(UL, buff=.3)
        k_rect = SurroundingRectangle(k_text, buff=0.13, stroke_color=OFF_WHITE, stroke_width=2)
        k_group = VGroup(k_text, k_rect)
        return k_group
