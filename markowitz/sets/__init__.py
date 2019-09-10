"""Set Module

Collection of point generators currently featuring:
    - Linear(start, end, number of values):
        Linear set of points
        equivalent to numpy linspace

    - Dotation2(...):
        Defined by E = {(x, y) ∊ R^2, x + y = 1}

    - Dotation3(...):
        Defined by E = {(x, y, z) ∊ R^3, x + y + z = 1}

Implement your own sets by subclassing AbstractSpace
"""

from .linear import Linear
from .dotspace import Dotation2, Dotation3
