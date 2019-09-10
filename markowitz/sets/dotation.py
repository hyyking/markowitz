""" Dotation Classes

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
from .linear import Linear


class Dotation2(AbstractSet):
    """ Defined by E = {(x, y) ∊ R^2, x + y = 1} """

    def __init__(self, until: int):
        self.x = Linear(0, 1, until)
        self.y = self.x.map(lambda x: 1 - x)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.x), next(self.y)


class Dotation3(AbstractSet):
    """ Defined by E = {(x, y, z) ∊ R^3, x + y + z = 1}
        Computed by rasterizing Barycentric coordinates
    """

    def __init__(self, until: int):
        self.max = until
        self.step = 1.0 / until

        # Iteration State
        self._stepn = 0
        self._inner = None

    def __iter__(self):
        self._stepn = 0
        self._inner = None
        return self

    def __next__(self):
        if self._stepn == self.max:
            raise StopIteration

        if self._inner is None:
            self._inner = Linear(0, self._stepn * self.step, self.max)

        z = 1 - self._stepn * self.step
        x = next(self._inner, None)
        y = (1 - x) if x is not None else 1

        if x is None:
            self._inner = None
            self._stepn += 1
            next(self)
        return x, y, z


class DotationDirichlet(AbstractSet):
    """ Defined by E = {(x, ..., x_i), i ∊ R, sum(x...x_i) = 1}
        Points are random but always satisfies the above Vector space
    """

    from numpy.random import dirichlet

    def __init__(self, dimension: int, until: int):
        self._content = iter(self.dirichlet((1,) * dimension, until))
        print(self._content)

    def __iter__(self):
        return self._content

    def __next__(self):
        return next(self._content)
