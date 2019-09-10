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
        return self.start if self.start <= self.end else StopIteration

    def gen(self):
        """ Override abstract method to create a linear space generator """
        return iter(self)

    def map(self, func, *margs, **mkwargs):
        """ Override abstract method to map a function to a linear space """
        return map(lambda x: func(x, *margs, **mkwargs), iter(self))
