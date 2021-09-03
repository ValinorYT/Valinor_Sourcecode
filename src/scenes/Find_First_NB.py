import os
from pathlib import Path

from manim import *

from src.scenes.KNN_Scene import KNN_Scene


class Find_First_NB(KNN_Scene):

    def construct(self):
        KNN_Scene.construct(self)

        self.play(Broadcast(Circle(radius=4, color=TEAL_A), n_mobs=3, run_time=2))
        self.wait(3)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} Find_First_NB -pql")
