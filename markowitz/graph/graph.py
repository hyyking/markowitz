# from ..structures import Portfolio
from .module_header import ObjectCache, CacheRef

from .space import Dot_Space, Range_Space

from numpy import pi, sqrt, exp, fromiter
# from typing import Tuple


class _Graph(object, metaclass=ObjectCache):
    def __init__(self, vs_cache_ref: CacheRef) -> None:
        self.vspace = vs_cache_ref


class NormalGraph(_Graph):
    def __init__(self, mu: float, sigma: float) -> None:
        self.mu = mu
        self.sigma = sigma
        super(NormalGraph, self).__init__(Range_Space(-5, 5, 1000))

    @staticmethod
    def f(point, *args):
        v = args[1] * args[1]
        curve = 1/sqrt(2*pi*v)
        x = (point - args[0]) * (point - args[0])
        dens = exp(-(x/(2*v)))
        return dens

    def y(self):
        return fromiter(
                self.vspace.ref().map(self.f, self.mu, self.sigma), 
                float,
                self.vspace.ref().nb
        )

    def points(self):
        return (fromiter(self.vspace.ref().map(), float), self.y())
