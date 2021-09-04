import os
from pathlib import Path

from manim import *

from src.data.dots.dots1 import positions, labels_2_classes
from src.data.dots.utils import get_dots, get_positions
from src.data.graphics_stuff import OFF_WHITE
from src.data.lengths import dot_radius
from src.scenes.KNN_Scene import KNN_Scene
from src.utils.distances import dots_sorted_by_distance


class Find_K_NB(KNN_Scene):
    dots = get_dots(get_positions(positions), labels_2_classes)

    def construct(self):
        self.play(Create(VGroup(*self.dots)))

        self.x.move_to([-.75, .3, 0])

        animation_circle = always_redraw(
            lambda: Circle(radius=self.tracker.get_value(), color=OFF_WHITE,
                           stroke_width=2).move_to(self.x.get_center())
        )

        self.add(self.x, self.x_circle, animation_circle)

        for j in range(self.k):
            pos = dots_sorted_by_distance(self.x, self.dots)[j].get_center()
            self.play(
                LaggedStart(
                    self.tracker.animate.set_value(self.distance_to_nth_dot(j)),
                    Create(Circle(radius=dot_radius * 1.25, color=OFF_WHITE, stroke_width=1.2).move_to(pos)),
                    Create(self.line_by_index(j, self.dots)),
                    Broadcast(Circle(color=OFF_WHITE, radius=dot_radius * 1.5), n_mobs=1, focal_point=pos),
                    Write(Text(str(j + 1)).scale(.35).next_to(pos, DOWN, buff=.3)),
                    run_time=4, lag_ratio=.3
                )
            )

    def distance_to_nth_dot(self, n):
        other_pos = np.array(dots_sorted_by_distance(self.x, self.dots)[n].get_center())
        return np.linalg.norm(np.array(self.x.get_center()) - other_pos)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} Find_K_NB -pqp")
