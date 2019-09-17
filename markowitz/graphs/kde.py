""" Kernel Density Estimation Class Graph """

import numpy as np

from .abstract import AbstractGraph
from ..sets import Linear

__all__ = "Kde"


class Kde(AbstractGraph):
    """ Kernel Density Estimation graph """

    def __init__(self, asset, **config):
        super(Kde, self).__init__()
        self._setup(config)

        self.stdv = asset.stdv
        self.values = asset.values

    def _setup(self, config):
        self.__dict__.update(config)
        self.legend = "KDE"

    @staticmethod
    def _kernel(k):
        """ Kernel of the KDE (currently gaussian) """
        return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * k * k)

    @staticmethod
    def estimate(point, values, stdv):
        """ Estimation function """
        hyperparamter = 1.06 * (stdv) / np.power(len(values), 0.2)
        results = np.fromiter(
            map(lambda xi: Kde._kernel((point - xi) / hyperparamter), values),
            dtype=np.float64,
        )
        return 1.0 / (len(values) * hyperparamter) * np.sum(results)

    def points(self):
        """ Override abstract method to generate kernel density estimation points """
        x = Linear(-10, 10, self.precision)
        y = x.map(self.estimate, self.values * self.scale, self.stdv * self.scale)
        return zip(x, y)
