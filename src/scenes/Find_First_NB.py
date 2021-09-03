import os
from pathlib import Path

from manim import *

from src.data import positions
from src.scenes.KNN_Scene import KNN_Scene
from src.utils.distances import nearest_pos


class Find_First_NB(KNN_Scene):

    def construct(self):
        KNN_Scene.construct(self)

        self.wait(6)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} Find_First_NB -pql")
