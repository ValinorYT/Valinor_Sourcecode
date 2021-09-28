import matplotlib.pyplot
import numpy as np
from manim import Circle

from general.data.graphics_stuff import OFF_WHITE
from general.data.lengths import dot_radius
from k_means.KMeans_Scene import KMeans_Scene


class OneDimExample(KMeans_Scene):
    def construct(self):
        self.dots = []

        for i in range(4):
            self.dots += [Circle(color=OFF_WHITE, radius=.85 * dot_radius, stroke_width=8, fill_opacity=.7).move_to(
                np.array([-1.5, 0, 0]) + np.array([np.random.normal(scale=.35), 0, 0]))]

        for i in range(5):
            self.dots += [Circle(color=OFF_WHITE, radius=.85 * dot_radius, stroke_width=8, fill_opacity=.7).move_to(
                np.array([1.5, 0, 0]) + np.array([np.random.normal(scale=.5), 0, 0]))]

        super(OneDimExample, self).construct()


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} -pqp")
