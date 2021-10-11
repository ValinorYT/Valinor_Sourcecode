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

    def color_pseudo(self, line_idx, highlight_color=GREY, default_color=OFF_WHITE):
        self.pseudo_text.set_color(default_color)
        self.pseudo_text[self.pseudo_lengths[line_idx]: self.pseudo_lengths[line_idx + 1]].set_color(highlight_color)

    def __init__(self):
        super().__init__()

        self.y = [5, 2, 4, 3, 1]
        random.shuffle(self.y)
        self.n = len(self.y)

        self.text_width = 1.0 * screen_width / (len(self.y) * (1 + buff_scaling))
        self.items = [VGroup(
            Rectangle(height=self.get_bar_height(i), width=self.text_width),
            Rectangle(height=max_bar_height - self.get_bar_height(i), width=self.text_width, stroke_opacity=0))
                          .arrange(UP) for i in range(self.n)]
        self.items = VGroup(*self.items)  # make VGroup
        self.items.arrange(buff=buff_scaling * self.text_width).to_edge(DOWN, buff=1.5)

        pseudo_lines = [f"for {stop_idx} from n-2 down to 0:",
                        f"       for {run_idx} from 0 to {stop_idx}:",
                        f"               swap at {run_idx} & {run_idx}+1 if needed"]

        self.pseudo_string = "\n".join(pseudo_lines)
        self.pseudo_text = Text(self.pseudo_string, font="Source Han Sans", line_spacing=1.3) \
            .scale(0.5).to_edge(UL, buff=.4)
        self.pseudo_lengths = np.cumsum([0] + [len(line.replace(" ", "")) for line in pseudo_lines])
        self.pseudo_rect = SurroundingRectangle(self.pseudo_text, buff=0.15, stroke_color=GREY, stroke_width=1.5)

        self.last_idx = Text(stop_idx).scale(.35).to_edge(DOWN, buff=.2)
        self.run_idx = Text(run_idx).scale(.35).to_edge(DOWN, buff=.77)

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
        self.play(Write(self.pseudo_text), Create(self.pseudo_rect), Write(self.last_idx), Write(self.run_idx))

        range_line = Underline(VGroup(*self.items), stroke_width=6).shift(np.array([0, -.2, 0]))
        self.play(FadeIn(range_line), run_time=t_short)

        for i in range(self.n - 1, 0, -1):
            self.color_pseudo(0)
            self.play(Transform(range_line,
                                Underline(VGroup(*self.items[0:i + 1]), stroke_width=6).shift(np.array([0, -.2, 0]))),
                      self.last_idx.animate.move_to(
                          [self.items[i - 1].get_center()[0], self.last_idx.get_center()[1], 0]),
                      run_time=2)

            for j in range(i):
                self.color_pseudo(1)
                self.wait()
                swap_line = Underline(VGroup(*self.items[j:j + 2]), stroke_width=6, buff=SMALL_BUFF * 1.35)
                self.play(FadeIn(swap_line),
                          self.run_idx.animate.move_to(
                              [self.items[j].get_center()[0], self.run_idx.get_center()[1], 0]),
                          run_time=1)
                self.color_pseudo(2)
                if self.y[j] > self.y[j + 1]:
                    self.play(swap_line.animate.set_color(V_GREEN),
                              VGroup(self.items[j], self.items[j + 1]).animate.set_color(GREY),
                              run_time=1)
                    self.color_pseudo(2, highlight_color=V_GREEN)

                    self.swap_items_animation(j, j + 1)
                    self.y[j], self.y[j + 1] = self.y[j + 1], self.y[j]
                else:
                    self.play(swap_line.animate.set_color(V_RED), run_time=1)
                    self.color_pseudo(2, highlight_color=V_RED)
                    self.wait()

                self.play(FadeOut(swap_line),
                          VGroup(self.items[j], self.items[j + 1]).animate.set_color(OFF_WHITE),
                          run_time=t_short)
            self.play(self.items[i].animate.set_color(V_YELLOW))

        self.wait()
        self.play(self.items[0].animate.set_color(V_YELLOW),
                  FadeOut(self.last_idx, self.run_idx, self.pseudo_text, self.pseudo_rect, range_line))
        self.wait(3)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} -pqp")
