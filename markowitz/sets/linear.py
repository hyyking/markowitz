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


class Linear(AbstractSet):
    """ Linear set of points """

    def __init__(self, start, end, nb):
        self.start = start
        self.end = end
        self.step = (end - start) / nb

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        if self.start > self.end:
            raise StopIteration
        return self.start
