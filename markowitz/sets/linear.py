""" Linear Class

Example usage:
```
    # 100 points between 0 and 1
    x = Linear(0, 1, 100)
    for i in x:
        print(i)

    # Generate y = ln(x) points between 0 and 1
    x = Linear(0, 1, 100)
    y = x.map(math.log, 2)
```
"""

from .abstract import AbstractSet

__all__ = "Linear"


class Linear(AbstractSet):
    """ Linear set of points """

    def __init__(self, start, end, nb):
        self.start = start
        self.end = end
        self.step = (end - start) / nb

        self.current = self.start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        self.current += self.step
        if self.current > self.end:
            raise StopIteration
        return self.current
