import os
from pathlib import Path

import numpy as np
from manim import Scene, VGroup, Text


class BubbleSortScene(Scene):
    n = 5
    boxes = [Text(str(i)).scale(2) for i in range(n)]

    def shuffle(self):
        permutation = np.random.permutation(self.n)
        old_pos = [x.get_center() for x in self.boxes]
        for i in range(self.n):
            self.boxes[i].move_to(old_pos[permutation[i]])

    def swap(self, i, j):
        self.play(
            self.boxes[i].animate.move_to(self.boxes[j].get_center()),
            self.boxes[j].animate.move_to(self.boxes[i].get_center())
        )

    def construct(self):
        g = VGroup(*self.boxes)
        self.add(g)
        g.arrange(buff=.9)

        self.wait()
        self.shuffle()
        self.wait()
        self.swap(1, 2)
        self.wait()


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} -pqp")
