class RangeSpace(object):
    def __init__(self, start, end, nb):
        self.start = start
        self.end = end
        self.iterations = nb

    def _iter_hook(self):
        return self.end - self.start, (self.end - self.start) / (self.iterations)

    def gen(self):
        width, step = self._iter_hook()
        for i in range(self.iterations):
            yield i * step + self.start

    def map(self, map_func, *map_args):
        width, step = self._iter_hook()
        for i in range(self.iterations + 1):
            point = i * step + self.start
            yield point, map_func(point, *map_args)
