""" Dotation Classes

Example usage:
```
    # A tuple of two
    x = Dotation2(100)
    for i in x:
        print(i)
```
"""

from .abstract import AbstractSet
from .linear import Linear

__all__ = ["Dotation2", "Dotation3", "DotationDirichlet"]


class Dotation2(AbstractSet):
    """ Defined by E = {(x, y) ∊ R^2, x + y = 1}
        Uses spaces.Linear under the hood
    """

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
        self._innerx = None
        self._innery = None

    def _reset_xy(self):
        self._innerx = Linear(0.0, self._stepn * self.step, self.max)
        self._innery = self._innerx.map(lambda x: 1 - x)

    def __iter__(self):
        self._stepn = 1
        self._reset_xy()
        return self

    def __next__(self):
        if self._stepn > self.max:
            raise StopIteration

        x = next(self._innerx, None)
        y = next(self._innery, None)
        z = 1 - self._stepn * self.step

        if x is None or y is None:
            self._stepn += 1
            self._reset_xy()
            return next(self)
        return x, y, z


class DotationDirichlet(AbstractSet):
    """ Defined by E = {(x, ..., x_i), i ∊ R, sum(x...x_i) = 1}
        Points are random but always satisfies the above Vector space
    """

    from numpy.random import dirichlet

    def __init__(self, dimension: int, until: int):
        self._content = iter(
            self.dirichlet((1,) * dimension, until)
        )  # pylint: disable=too-many-function-args

    def __iter__(self):
        return self._content

    def __next__(self):
        return next(self._content)
