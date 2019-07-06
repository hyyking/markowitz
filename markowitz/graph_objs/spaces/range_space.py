
class RangeSpace(object):
    def __init__(self, start, end, nb):
        self.start = start
        self.end = end
        self.nb = nb

    def _iter(self, map_func, *map_args):
        width = self.end - self.start
        step = width/(self.nb)

        if map_func is not None:
            for i in range(self.nb + 1):
                point = self.start + i*step
                yield point, map_func(point, *map_args)
        else:
            for i in range(self.nb):
                yield self.start + i*step
    
    def gen(self):
        return self._iter(None)

    def map(self, map_func, *map_args):
        return self._iter(map_func, *map_args)

