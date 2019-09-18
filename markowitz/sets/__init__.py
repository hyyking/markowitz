"""Set Module

Collection of point generators currently featuring:

    - Linear(start, end, number of values):
        Linear set of points
        equivalent to numpy linspace

    - Dotation2(number of values):
        Defined by E = {(x, y) ∊ R^2, x + y = 1}

    - Dotation3(number of values):
        Defined by E = {(x, y, z) ∊ R^3, x + y + z = 1}

    - DotationDirichlet(dimension, number of values):
        Defined by E = {(x, ..., xi) ∊ R^i, i ∊ N, sum(x, ..., xi) = 1}

Implement your own sets by subclassing AbstractSet
"""

from .linear import Linear
from .dotation import Dotation2, Dotation3, DotationDirichlet
