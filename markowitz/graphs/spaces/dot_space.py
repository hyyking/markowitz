import numpy as np


class DotationSpace(object):
    def __init__(self, v_size: int, max_num: int) -> None:
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
            h = 1 / self.nb
            for i in range(self.nb + 1):
                z = 1 - i * h
                xs = np.linspace(0, i * h, self.nb)
                for x, y in zip(xs, i * h - xs):
                    yield (x, y, z)
        else:
            for els in np.random.dirichlet((1,) * s, self.nb * 10):
                yield tuple(els)

    def _iter(self, mapper, *map_args):
        gen_alg = self._alg()

        if mapper is not None:
            for point in gen_alg:
                self.counter += 1
                yield mapper(point, *map_args)
        else:
            for point in gen_alg:
                self.counter += 1
                yield point

    def gen(self):
        return self._iter(None)

    def map(self, map_func, *map_args):
        return self._iter(map_func, *map_args)
