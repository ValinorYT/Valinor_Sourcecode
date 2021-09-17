from collections import Counter

from general.utils.HashWrapper import HashWrapper


def most_common_color(colors):
    wrapped_colors = [HashWrapper(c) for c in colors]
    return [elem.val for elem, freq in Counter(wrapped_colors).most_common()]
