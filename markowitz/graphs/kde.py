""" Kernel Density Estimation Class Graph """

import numpy as np

from .abstract import AbstractGraph
from ..sets import Linear


class Kde(AbstractGraph):
    """ Kernel Density Estimation graph """

    def __init__(self, asset, **config):
        super(Kde, self).__init__()
        self._setup(config)

        self.stdv = asset.stdv
        self.df = asset.df

    def _setup(self, config):
        self.legend = "KDE"
        self.__dict__.update(config)

    @staticmethod
    def _kernel(k):
        """ Kernel of the KDE (currently gaussian) """
        return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * k * k)

    @staticmethod
    def estimate(point, df, stdv):
        """ Estimation function """
        hyperparamter = 1.06 * (stdv) / np.power(len(df - 1), 0.2)
        results = np.array(
            [Kde._kernel((point - xi) / hyperparamter) for xi in df if not np.isnan(xi)]
        )
        return 1.0 / (len(df - 1) * hyperparamter) * np.sum(results)

    def points(self):
        """ Override abstract method to generate kernel density estimation points """
        x = Linear(-10, 10, self.precision)
        y = x.map(self.estimate, self.df * self.scale, self.stdv * self.scale)
        return zip(x, y)
