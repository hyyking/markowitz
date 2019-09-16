""" Efficient Frontier Graph Class """

from .abstract import AbstractGraph
from ..sets import Dotation2, Dotation3, DotationDirichlet


class EfficientFrontier(AbstractGraph):
    """The efficient frontier is a function on plane
       which represents all the efficient asset combinations.
       Plane has risk as abscis and gains as origin.
    """

    def __init__(self, portfolio, **config) -> None:
        super(EfficientFrontier, self).__init__()
        self._setup(config)

        self.pf_size = len(portfolio)
        self.mu = portfolio.avg  # pylint: disable=invalid-name
        self.sigma = portfolio.stdv

    def _setup(self, config):
        self.__dict__.update(config)
        self.legend = "Efficient Frontier"

    @staticmethod
    def determine_set(size):
        """ Determine the set to use for point generation """
        if size == 2:
            return Dotation2
        if size == 3:
            return Dotation3
        return DotationDirichlet

    def points(self):
        """ Override abstract method to generate efficient frontier points """
        mset = EfficientFrontier.determine_set(self.pf_size)
        args = (
            (self.precision // 10,)
            if not hasattr(mset, "dirichlet")
            else (self.pf_size, self.precision // 10)
        )
        dots = mset(*args)
        return zip(
            dots.map(lambda x: self.scale * self.mu(x)),
            dots.map(lambda x: self.scale * self.sigma(x)),
        )


# Code for third dimension plotting
# if self.pf_size == 3:
#   for x, y, z in zip(lin_sigma, lin_mu, np.linspace(0, 1, dots.counter)):
#       yield (x*scale, y*scale, z)
