# from ..structures import Portfolio
from .module_header import ObjectCache, CacheRef

from .space import Dot_Space, Range_Space

import numpy as np

from typing import Tuple, Callable


class _Graph(object, metaclass=ObjectCache):
    precision = 1000

    def __init__(self, vs_cache_ref: CacheRef) -> None:
        self.vspace = vs_cache_ref

    def points(self):
        return None


class NormalGraph(_Graph):
    const1 = np.sqrt(2*np.pi)

    def __init__(self, mu: float, sigma: float) -> None:
        self.mu = mu
        self.sigma = sigma
        super(NormalGraph, self).__init__(Range_Space(-10, 10, self.precision))

    @staticmethod
    def f(point, *args):
        t1 = np.float64(1/(args[1]*NormalGraph.const1))
        x = ((point-args[0])/args[1])
        t2 = np.exp(-0.5*x*x)
        return t1*t2

    def y(self, scale):
        return np.fromiter(
                self.vspace.ref().map(self.f, self.mu*scale, self.sigma*scale),
                float,
                self.vspace.ref().nb
        )

    def points(self, scale=1):
        x = np.linspace(0, 1, self.precision)
        y = self.y(scale)
        return (x, y)


class EfficientFrontier(_Graph):
    def __init__(
            self,
            pf_size: int,
            mu:     Callable[[Tuple[float, ...]], float],
            sigma:  Callable[[Tuple[float, ...]], float]
            ) -> None:
        self.pf_size = pf_size
        self.mu = mu
        self.sigma = sigma
        super(EfficientFrontier, self).__init__(Dot_Space(pf_size, int(self.precision/10)))

    def points(self, scale=1):
        lin_mu = np.fromiter(self.vspace.ref().map(self.mu), float)*scale
        lin_sigma = np.fromiter(self.vspace.ref().map(self.sigma), float)*scale

        if self.pf_size == 3:
            return (lin_sigma, lin_mu, np.linspace(0, 1, self.precision))
        else:
            return (lin_sigma, lin_mu)
