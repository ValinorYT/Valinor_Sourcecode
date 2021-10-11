import os
import random
from pathlib import Path

from manim import *

from general.data.graphics_stuff import BACKGROUND_COLOR, V_GREEN, V_RED, OFF_WHITE, V_YELLOW

t_short = .5
buff_scaling = .9
screen_width = 12  # sadly hardcoded, idk how to get it automatically
max_bar_height = 4

run_idx = "run_index"
stop_idx = "stop_index"


class SortingScene(Scene):

    def __init__(self):
        super().__init__()

        self.y = [6, 5, 2, 4, 3, 1]
        random.shuffle(self.y)
        self.n = len(self.y)

        self.text_width = 1.0 * screen_width / (len(self.y) * (1 + buff_scaling))
        self.items = [VGroup(
            Rectangle(height=self.get_bar_height(i), width=self.text_width),
            Rectangle(height=max_bar_height - self.get_bar_height(i), width=self.text_width, stroke_opacity=0))
                          .arrange(UP) for i in range(self.n)]
        self.items = VGroup(*self.items)  # make VGroup
        self.items.arrange(buff=buff_scaling * self.text_width).to_edge(DOWN, buff=1.5)

    def get_bar_height(self, bar_idx):
        return max_bar_height * (self.y[bar_idx] / self.n)

    def swap_items_animation(self, i, j):
        self.play(  # swap on visualization
            self.items[i].animate.move_to(self.items[j].get_center()),
            self.items[j].animate.move_to(self.items[i].get_center())
        )
        self.items[i], self.items[j] = self.items[j], self.items[i]  # also swap in list

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.play(FadeIn(self.items))

        range_line = Underline(VGroup(*self.items), stroke_width=6).shift(np.array([0, -.2, 0]))
        self.play(FadeIn(range_line), run_time=t_short)

        for i in range(self.n - 1, 0, -1):
            self.play(Transform(range_line,
                                Underline(VGroup(*self.items[0:i + 1]), stroke_width=6).shift(np.array([0, -.2, 0]))),
                      run_time=2)

            for j in range(i):
                self.wait()
                swap_line = Underline(VGroup(*self.items[j:j + 2]), stroke_width=6, buff=SMALL_BUFF * 1.35)
                self.play(FadeIn(swap_line), run_time=1)
                if self.y[j] > self.y[j + 1]:
                    self.play(swap_line.animate.set_color(V_GREEN),
                              VGroup(self.items[j], self.items[j + 1]).animate.set_color(GREY),
                              run_time=1)

                    self.swap_items_animation(j, j + 1)
                    self.y[j], self.y[j + 1] = self.y[j + 1], self.y[j]
                else:
                    self.play(swap_line.animate.set_color(V_RED), run_time=1)
                    self.wait()

                self.play(FadeOut(swap_line),
                          VGroup(self.items[j], self.items[j + 1]).animate.set_color(OFF_WHITE),
                          run_time=t_short)
            self.play(self.items[i].animate.set_color(V_YELLOW))

        self.wait()
        self.play(self.items[0].animate.set_color(V_YELLOW), FadeOut(range_line))
        self.wait(3)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} -pqp")
