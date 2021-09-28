import os
from pathlib import Path

import numpy as np
from manim import Circle, Create, VGroup, FadeIn, Line

from general.data.graphics_stuff import OFF_WHITE, LABEL_COLORS
from general.data.lengths import dot_radius, line_width
from k_means.KMeans_Scene import KMeans_Scene


class _1_TwoClusters(KMeans_Scene):
    def construct(self):
        first_group_size = 8
        self.dots = [
            Circle(color=OFF_WHITE, radius=.85 * dot_radius, stroke_width=8, fill_opacity=.7).move_to(
                [3, 1.8, 0] + np.random.normal(size=3))
            for _ in range(first_group_size)]
        self.dots += [
            Circle(color=OFF_WHITE, radius=.85 * dot_radius, stroke_width=8, fill_opacity=.7).move_to(
                [-2.2, -2, 0] + np.random.normal(scale=[.7] * 3, size=3))
            for _ in range(9)]

        centroid1 = Circle(color=LABEL_COLORS[0], radius=2.2 * dot_radius, stroke_width=8, fill_opacity=.4) \
            .move_to(np.array([x.get_center() for x in self.dots[:first_group_size]]).mean(axis=0))

        centroid2 = Circle(color=LABEL_COLORS[1], radius=2.2 * dot_radius, stroke_width=8, fill_opacity=.4) \
            .move_to(np.array([x.get_center() for x in self.dots[first_group_size:]]).mean(axis=0))

        self.play(Create(VGroup(*self.dots)))
        self.wait()

        self.play(VGroup(*self.dots[:first_group_size]).animate.set_color(LABEL_COLORS[0]))
        self.wait()

        self.play(VGroup(*self.dots[first_group_size:]).animate.set_color(LABEL_COLORS[1]))
        self.wait()

        self.play(FadeIn(centroid1)),
        self.play(FadeIn(centroid2))
        self.wait()

        self.indicate_object(self.dots[0])
        self.play(Create(Line(start=centroid1.get_center(), end=self.dots[0], stroke_width=line_width,
                              color=LABEL_COLORS[0],
                              buff=dot_radius * 2.2)))
        self.wait()

        self.indicate_object(self.dots[1])
        self.play(Create(Line(start=centroid1.get_center(), end=self.dots[1], stroke_width=line_width,
                              color=LABEL_COLORS[0],
                              buff=dot_radius * 2.2)))
        self.wait()


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} -pqp")
