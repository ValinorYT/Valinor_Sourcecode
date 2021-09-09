import os
from pathlib import Path

from manim import *
from pygments.styles.paraiso_dark import RED, GREEN

from knn.src.scenes.KNN_Scene import KNN_Scene


class ProContraTable(KNN_Scene):

    def construct(self):
        text = Text("Review of KNN").to_edge(UP)
        line = Underline(text, buff=0.2)

        table = Table(
            [["no need to train", "can take long to run\n-> O(num_datapoints)"],
             ["visually interpretable", "good value for k\nmust be chosen"],
             ["very simple", "good distance-function\noften impossible\n(e.g. on images)"]],
            col_labels=[Text("PRO", color=GREEN), Text("CONTRA", color=RED)],
            arrange_in_grid_config={"cell_alignment": LEFT}) \
            .scale(.6).next_to(line, DOWN, buff=1)

        self.add(text, line)
        self.play(table.create(run_time=1.5))
        for x in table.elements:
            self.play(Indicate(x))
        self.wait(4)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} ProContraTable -pqp")
