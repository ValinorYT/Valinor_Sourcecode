from manim import *
from manim import Circle

from general.data.dots.utils import get_positions
from general.data.graphics_stuff import OFF_WHITE, LABEL_COLORS
from general.data.lengths import dot_radius
from general.utils.distances import stuff_sorted_by_distance
from k_means.data.dots.dots1 import k_means_positions
from knn.src.scenes.KNN_Scene import KNN_Scene


class KMeans_Scene(KNN_Scene):
    centroid_starting_positions = [-5, -.5, 0], [3, .4, 0]
    k = len(centroid_starting_positions)
    n_runs = 3
    dots = [
        Circle(color=OFF_WHITE, radius=.85 * dot_radius, stroke_width=8, fill_opacity=.7).move_to(
            get_positions(k_means_positions)[i])
        for i in range(len(get_positions(k_means_positions)))]

    centroids = [
        Circle(color=LABEL_COLORS[i], radius=2.2 * dot_radius, stroke_width=8, fill_opacity=.4).move_to(pos)
        for i, pos in enumerate(centroid_starting_positions)
    ]

    pseudo_lines = [f"Randomly place k (={k}) centroids",
                    "repeat until centroids stand still:",
                    "          Assign each datapoint to closest centroid",
                    "          Move centroid to mean of its data points"]

    pseudo_string = "\n".join(pseudo_lines)
    pseudo_text = Text(pseudo_string, font="Source Han Sans", line_spacing=1.2) \
        .scale(0.4).to_edge(UL, buff=.3)
    pseudo_lengths = np.cumsum([0] + [len(line.replace(" ", "")) for line in pseudo_lines])
    pseudo_rect = SurroundingRectangle(pseudo_text, buff=0.15, stroke_color=GREY, stroke_width=1)

    def color_pseudo(self, line_idx):
        self.pseudo_text.set_color(WHITE)
        self.pseudo_text[self.pseudo_lengths[line_idx]: self.pseudo_lengths[line_idx + 1]].set_color(GREY)

    def distance_to_closest_centroid(self, dot):
        closest_centroid = np.array(stuff_sorted_by_distance(dot, self.centroids)[0].get_center())
        return np.linalg.norm(np.array(dot.get_center()) - closest_centroid)

    def construct(self):
        self.play(Create(VGroup(*self.dots)))
        self.play(Write(self.pseudo_text), Create(self.pseudo_rect))

        self.color_pseudo(0)
        self.play(Create(VGroup(*self.centroids)), run_time=2)
        self.wait(2)

        for run_idx in range(self.n_runs):

            self.color_pseudo(1)
            self.wait(1.6)
            self.color_pseudo(2)

            # === Get closest centroid for each datapoint ===
            for idx, dot in enumerate(self.dots):
                closest_centroid = stuff_sorted_by_distance(dot, self.centroids)[0]
                my_color = closest_centroid.get_color()

                radius_tracker = ValueTracker(0)
                growing_circle = always_redraw(
                    lambda: Circle(radius=radius_tracker.get_value(), color=OFF_WHITE, stroke_width=2).move_to(
                        dot.get_center()))
                self.add(growing_circle)

                self.play(
                    radius_tracker.animate.set_value(self.distance_to_closest_centroid(dot)),
                    FadeIn(Line(closest_centroid.get_center(), dot.get_center(), color=my_color, buff=.2),
                           rate_func=there_and_back),
                    dot.animate.set_color(my_color),
                    run_time=2.5 * (.85 ** idx)
                )
                self.remove(growing_circle)

            self.color_pseudo(3)
            # === Move each centroid to mean ===
            for centroid in self.centroids:
                relevant_dots = list(filter(lambda d: d.get_color() == centroid.get_color(), self.dots))
                new_pos = np.array([d.get_center() for d in relevant_dots]).mean(axis=0)
                self.play(centroid.animate.move_to(new_pos), run_time=1.3)

            for dot in self.dots:  # reset colors of datapoints
                dot.set_color(OFF_WHITE)
        self.wait(2)
