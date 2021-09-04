import os
from pathlib import Path

from manim import *

from src.data.dots.dots1 import positions, labels2
from src.data.dots.utils import get_dots, get_positions
from src.data.graphics_stuff import OFF_WHITE
from src.scenes.KNN_Scene import KNN_Scene
from src.utils.distances import dots_sorted_by_distance


class Find_K_NB(KNN_Scene):
    dots = get_dots(get_positions(positions), labels2)

    def construct(self):
        self.play(Create(VGroup(*self.dots)))

        self.x.move_to([.75, .15, 0])

        self.x_circle = always_redraw(
            lambda: Circle(radius=self.tracker.get_value(), color=OFF_WHITE,
                           stroke_width=2).move_to(self.x.get_center())
        )

        self.add(self.x, self.x_circle)

        for j in range(self.k):
            new_radius = self.distance_to_nth_dot(j)
            self.play(self.tracker.animate.set_value(new_radius), run_time=2)
            self.add(self.line_by_index(j, self.dots))
            dot_pos = dots_sorted_by_distance(self.x, self.dots)[j].get_center()
            ctr_text = Text(str(j+1)).scale(.5).next_to(dot_pos, DOWN)
            self.add(ctr_text)
        self.wait(3)

    def distance_to_nth_dot(self, n):
        other_pos = np.array(dots_sorted_by_distance(self.x, self.dots)[n].get_center())
        return np.linalg.norm(np.array(self.x.get_center()) - other_pos)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} Find_K_NB -pqp")
