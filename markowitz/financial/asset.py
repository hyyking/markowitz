""" Asset Class """

from dataclasses import dataclass, field

import numpy as np

from .meta import MetaAsset

__all__ = ["Asset"]


@dataclass
class Asset(metaclass=MetaAsset):
    """ representation of an asset """

    name: str
    values: list = field(repr=False)
    avg: np.float64 = field(init=False)
    stdv: np.float64 = field(init=False)

    def __post_init__(self):
        self.avg = np.mean(self.values)
        self.stdv = np.sqrt(np.var(self.values))
