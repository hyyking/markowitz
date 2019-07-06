import numpy as np


class _Graph(object):
    precision = 1000

    def set_config(self, cfg):
        pass

    def points(self):
        raise Exception("points method not implemented")
