import os
from pathlib import Path

from manim import Table, Text, UP, LEFT, Underline, DOWN
from pygments.styles.paraiso_dark import RED, GREEN

from src.scenes.KNN_Scene import KNN_Scene


class ProContraTable(KNN_Scene):

    def construct(self):
        text = Text("Review of KNN").to_edge(UP)
        line = Underline(text, buff=0.2)

        table = Table(
            [["Very simple", "can take long to run\n-> O(num_datapoints)"],
             ["visually interpretable", "good value for k\nmust be chosen"],
             ["no need to train", "Good distance-function\noften impossible\n(e.g. on images)"]],
            col_labels=[Text("PRO", color=GREEN), Text("CONTRA", color=RED)],
            arrange_in_grid_config={"cell_alignment": LEFT}) \
            .scale(.6).next_to(line, DOWN, buff=1)

        self.add(text, line)
        self.play(table.create(run_time=3))
        self.wait(4)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} ProContraTable -pql")
