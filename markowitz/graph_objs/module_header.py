import numpy as np


class _Graph(object):
    precision = 1000
    legend = "missing legend attribute"

    def points(self):
        raise Exception("points method not implemented")
