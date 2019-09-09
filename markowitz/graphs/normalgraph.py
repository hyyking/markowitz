import numpy as np

from .abstract import AbstractGraph
from .spaces import RangeSpace


class NormalGraph(AbstractGraph):
    """Gaussian Curve of an asset average and standart deviation.
       It represents the distribution of the data.
    """

    def __init__(self, asset, **config):
        super(NormalGraph, self).__init__()
        self._setup(config)

        self.mu = asset.avg  # pylint: disable=invalid-name
        self.sigma = asset.stdv
        self.legend = f"N({round(self.mu, 2)}, {round(self.sigma, 2)})"

    def _setup(self, config):
        self.__dict__.update(config)

    @staticmethod
    def density(point, mu, sigma):  # pylint: disable=invalid-name
        """ density function of a gaussian curve """
        term = (point - mu) / sigma
        return 1.0 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * term * term)

    def points(self):
        """ Override abstract method to generate gaussian curve points """
        return RangeSpace(-10, 10, self.precision).map(
            self.density, self.mu * self.scale, self.sigma * self.scale
        )
