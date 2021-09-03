import os
from pathlib import Path
from manim import *

from src.scenes.KNN_Scene import KNN_Scene


class Changing_NB_1(KNN_Scene):

    def construct(self):
        KNN_Scene.construct(self)

        self.x.add_updater(lambda it: it.move_to([self.tracker.get_value(), self.tracker.get_value(), 0]))

        self.play(self.tracker.animate.set_value(2), rate_func=linear, run_time=2)
        self.wait(3)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} Changing_NB_1 -pql")