import os
from pathlib import Path

import numpy as np
from manim import Scene, VGroup, Text, Underline, FadeIn, FadeOut, Transform, Rectangle, UP, DR, UL, \
    SurroundingRectangle, Write, Create, SMALL_BUFF
from pygments.styles.paraiso_dark import RED
from pygments.styles.rainbow_dash import GREY, GREEN, WHITE

from general.data.graphics_stuff import BACKGROUND_COLOR

t_short = .5


class SortingScene(Scene):

    def __init__(self):
        super().__init__()

        self.n = 6
        y = [6, 2, 5, 3, 1, 4]  # formerly np.random.permutation(self.n)

        self.items = VGroup(*[VGroup(  # was für ein Brecher LUL
            Text(str(y[i] + 1), height=1),
            Rectangle(height=(y[i] + 1) / 3, width=.7),
            Rectangle(height=(self.n - y[i]) / 3, width=.7, stroke_opacity=0)  # make all items same height
        ).arrange(UP) for i in range(self.n)]).arrange(buff=.9).to_edge(DR, buff=1.2)

        pseudo_lines = ["Randomly place k centroids",
                        "repeat until centroids stand still:",
                        "          Assign each datapoint to closest centroid",
                        "          Move centroid to mean of its data points"]

        self.pseudo_string = "\n".join(pseudo_lines)
        self.pseudo_text = Text(self.pseudo_string, font="Source Han Sans", line_spacing=1.3) \
            .scale(0.5).to_edge(UL, buff=.4)
        self.pseudo_lengths = np.cumsum([0] + [len(line.replace(" ", "")) for line in pseudo_lines])
        self.pseudo_rect = SurroundingRectangle(self.pseudo_text, buff=0.15, stroke_color=GREY, stroke_width=1)

    def swap_items(self, i, j):
        self.play(  # swap on visualization
            self.items[i].animate.move_to(self.items[j].get_center()),
            self.items[j].animate.move_to(self.items[i].get_center())
        )
        self.items[i], self.items[j] = self.items[j], self.items[i]  # also swap in list

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.play(FadeIn(self.items))
        self.play(Write(self.pseudo_text), Create(self.pseudo_rect))

        range_line = Underline(VGroup(*self.items), stroke_width=6).shift(np.array([0, -.2, 0]))
        self.play(FadeIn(range_line), run_time=t_short)

        for i in range(self.n - 1, 0, -1):
            self.play(Transform(range_line,
                                Underline(VGroup(*self.items[0:i + 1]), stroke_width=6).shift(np.array([0, -.2, 0]))))

            for j in range(i):
                swap_line = Underline(VGroup(*self.items[j:j + 2]), stroke_width=6, buff=SMALL_BUFF * 1.35)
                self.play(FadeIn(swap_line), run_time=t_short)
                if int(self.items[j][0].text) > int(self.items[j + 1][0].text):
                    self.play(swap_line.animate.set_color(GREEN),
                              VGroup(self.items[j], self.items[j + 1]).animate.set_color(GREY),
                              run_time=t_short)
                    self.swap_items(j, j + 1)
                else:
                    self.play(swap_line.animate.set_color(RED), run_time=t_short)
                    self.wait()

                self.play(FadeOut(swap_line),
                          VGroup(self.items[j], self.items[j + 1]).animate.set_color(WHITE),
                          run_time=t_short)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} -pqp")
