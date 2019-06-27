from .module_header import ObjectCache
import numpy as np

from typing import Callable, Tuple, Iterator


Dot_Mapping = Callable[[Tuple[float, ...]], float]


class Space(metaclass=ObjectCache):
    pass


class Dot_Space(Space):
    def __init__(
            self,
            v_size: int,
            max_num: int,
            ) -> None:
        self.counter = 0
        self.size = v_size
        self.nb = max_num

    def _alg(self):
        s = self.size
        if s == 0:
            yield 0

        elif s == 1:
            for x in np.linspace(0, 1, self.nb):
                yield x

        elif s == 2:
            x_s = np.linspace(0, 1, self.nb)
            for x, y in zip(x_s, 1 - x_s):
                yield (x, y)

        elif s == 3:
            h = 1/self.nb
            for i in range(self.nb + 1):
                z = 1 - i*h
                xs = np.linspace(0, i*h, self.nb)
                for x, y in zip(xs, i*h - xs):
                    yield (x, y, z)


    def _iter(self, mapper, *map_args) -> Iterator[float]:
        gen_alg = self._alg()

        if mapper is not None:
            for point in gen_alg:
                yield mapper(point, *map_args)
        else:
            for point in gen_alg:
                yield point

    def map(self, map_func: Dot_Mapping = None, *map_args) -> Iterator[float]:
        return self._iter(map_func, *map_args)


class Range_Space(Space):
    def __init__(self, start, end, nb):
        self.start = start
        self.end = end
        self.nb = nb

    def _iter(self, map_func, *map_args):
        width = self.end - self.start
        step = width/(self.nb-1)

        if map_func is not None:
            for i in range(self.nb):
                yield map_func(self.start + i*step, *map_args)
        else:
            for i in range(self.nb):
                yield self.start + i*step

    def map(self, map_func=None, *map_args):
        return self._iter(map_func, *map_args)
