import os
from pathlib import Path

from manim import *
from manim import Circle

from k_means.data.dots.dots1 import k_means_positions
from knn.src.data.dots.utils import get_positions
from knn.src.data.graphics_stuff import OFF_WHITE, LABEL_COLORS
from knn.src.data.lengths import dot_radius
from knn.src.scenes.KNN_Scene import KNN_Scene
from knn.src.utils.distances import stuff_sorted_by_distance


class KMeans_Scene(KNN_Scene):

    centroid_starting_positions = [-2, -2, 0], [0, 3, 0], [3, 0, 0]

    dots = [
        Circle(color=OFF_WHITE, radius=.85 * dot_radius, stroke_width=8, fill_opacity=.7).move_to(
            get_positions(k_means_positions)[i])
        for i in range(len(get_positions(k_means_positions)))]

    centroids = [
        Circle(color=LABEL_COLORS[i], radius=2.2 * dot_radius, stroke_width=8, fill_opacity=.4).move_to(pos)
        for i, pos in enumerate(centroid_starting_positions)
    ]

    pseudo_lines = ["Randomly place k centroids",
                    "repeat until centroids stand still:",
                    "          Assign each datapoint to closest centroid",
                    "          Move centroid to mean of its data points"]

    pseudo_string = "\n".join(pseudo_lines)
    pseudo_text = Text(pseudo_string, line_spacing=2).scale(0.37).to_edge(UL, buff=.4)
    pseudo_lengths = np.cumsum([0] + [len(line.replace(" ", "")) for line in pseudo_lines])
    pseudo_rect = SurroundingRectangle(pseudo_text, buff=0.2, stroke_color=GREY, stroke_width=1)

    def color_pseudo(self, line_idx):
        self.pseudo_text.set_color(WHITE)
        self.pseudo_text[self.pseudo_lengths[line_idx]: self.pseudo_lengths[line_idx + 1]].set_color(YELLOW)

    def construct(self):
        n_runs = 1

        self.play(Create(VGroup(*self.dots)))
        self.play(Write(self.pseudo_text), Create(self.pseudo_rect))

        self.color_pseudo(0)
        self.play(Create(VGroup(*self.centroids)), run_time=2)
        self.wait(2)

        for run_idx in range(n_runs):

            self.color_pseudo(1)

            self.color_pseudo(2)

            for dot in self.dots:
                closest_centroid = stuff_sorted_by_distance(dot, self.centroids)[0]
                my_color = closest_centroid.get_color()

                self.indicate_object(dot)
                self.play(
                    LaggedStart(
                        FadeIn(
                            Line(closest_centroid.get_center(), dot.get_center(), color=my_color, buff=.2).shift(
                                np.array([0, 0, -10])),
                            rate_func=there_and_back),
                        dot.animate.set_color(my_color),
                        lag_ratio=.3, run_time=1.5
                    ))

            self.color_pseudo(3)
            for centroid in self.centroids:
                relevant_dots = list(filter(lambda d: d.get_color() == centroid.get_color(), self.dots))
                new_pos = np.array([d.get_center() for d in relevant_dots]).mean(axis=0)
                self.play(centroid.animate.move_to(new_pos), run_time=1.3)

            for dot in self.dots:
                dot.set_color(OFF_WHITE)
        self.wait(2)
