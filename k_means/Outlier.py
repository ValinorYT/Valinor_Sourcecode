import os
from pathlib import Path

from k_means.KMeans_Scene import KMeans_Scene


class Outlier(KMeans_Scene):
    pass


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} -pqp")
