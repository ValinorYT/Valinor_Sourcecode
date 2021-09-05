from manim import *
from manim import Broadcast, Circle

from src.data.graphics_stuff import BACKGROUND_COLOR, OFF_WHITE
from src.data.lengths import line_width, dot_radius
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
    k = 3

    def __init__(self):
        super().__init__()
        self.camera.background_color = BACKGROUND_COLOR
        self.x = Dot(radius=dot_radius * 1.3)
        self.x_circle = Circle(radius=self.x.radius * 1.2, color=OFF_WHITE, stroke_width=2)
        self.x_circle.add_updater(lambda it: it.move_to(self.x.get_center()))

        self.k_text = Text(f"k = Number of used dots\n= {self.k}") \
            .scale(.5).to_edge(UL, buff=.3)
        self.k_rect = SurroundingRectangle(self.k_text, buff=0.13, stroke_color=OFF_WHITE, stroke_width=2)
        self.k_group = VGroup(self.k_text, self.k_rect)

    def get_label_prediction(self, dots):
        k_neighbours = dots_sorted_by_distance(self.x, dots)[:self.k]
        return most_common_color([x.get_color() for x in k_neighbours])[0]

    def add_nb_lines(self, dots):
        for j in range(self.k):
            self.add(self.line_by_index(j, dots))

    def line_by_index(self, idx, dots):
        return always_redraw(lambda:
                             Line(
                                 start=self.x.get_center(),
                                 end=dots_sorted_by_distance(self.x, dots)[idx].get_center(),
                                 stroke_width=line_width,
                                 color=dots_sorted_by_distance(self.x, dots)[idx].get_color(),
                                 buff=dot_radius * 1.66)
                             )

    def indicate_x(self):
        self.play(
            Broadcast(Circle(color=OFF_WHITE, radius=dot_radius * 4.5),
                      n_mobs=3, focal_point=self.x.get_center(), run_time=2))
