import os
from itertools import combinations
from pathlib import Path

import numpy as np
from manim import Scene, BarChart, ValueTracker, always_redraw, smooth, DL, DR


def gini(x):
    """Compute Gini coefficient of array of values"""
    diffsum = 0
    for i, xi in enumerate(x[:-1], 1):
        diffsum += np.sum(np.abs(xi - x[i:]))
    return diffsum / (len(x)**2 * np.mean(x))


class BarCharExam(Scene):

    def construct(self):
        n_trackers = 4
        trackers = [ValueTracker(1) for _ in range(n_trackers)]

        def tracker_values():
            return [t.get_value() for t in trackers]

        bar_chart = always_redraw(lambda: BarChart(tracker_values()).to_edge(DL))
        gini_bar = always_redraw(lambda: BarChart([gini(np.array(tracker_values()))]).to_edge(DR))

        self.add(bar_chart, gini_bar)

        self.play(trackers[0].animate.set_value(0),
                  trackers[1].animate.set_value(1.3),
                  trackers[2].animate.set_value(0),
                  trackers[3].animate.set_value(.7),
                  run_time=4, rate_func=smooth)
        print("test")
        self.play(trackers[3].animate.set_value(0),
                  run_time=3, rate_func=smooth)


# if __name__ == "__main__":
#     script_name = f"{Path(__file__).resolve()}"
#     os.system(f"manim {script_name} -pql")

print(gini(np.array([0, 0, 0, 1])))