import math
import os
from pathlib import Path

import numpy as np
from manim import Circle, FadeOut, VGroup

from general.data.graphics_stuff import OFF_WHITE, LABEL_COLORS
from general.data.lengths import dot_radius
from k_means.KMeans_Scene import KMeans_Scene


class _2_Animation2(KMeans_Scene):
    def construct(self):
        self.dots = []
        center_size = 8
        for i in range(50):
            angle = np.random.uniform() * 2 * math.pi
            self.dots += [Circle(color=OFF_WHITE, radius=.85 * dot_radius, stroke_width=8, fill_opacity=.7).move_to(
                np.array([1, -.5, 0]) +
                (np.array([math.sin(angle), math.cos(angle), 0]) * (2.5 + np.random.normal(scale=.2)))
                if i > center_size
                else np.array([1, -.5, 0]) + np.random.normal(scale=[.3] * 3, size=3))]
        super(_2_Animation2, self).construct()

        self.play(FadeOut(VGroup(*self.centroids)))
        for i in range(len(self.dots)):
            self.dots[i].set_color(LABEL_COLORS[0] if i > center_size else LABEL_COLORS[1])

        self.wait(4)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} -pqp")
