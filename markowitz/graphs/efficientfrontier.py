from .abstract import AbstractGraph
from .spaces import DotationSpace


# pylint: disable=too-few-public-methods
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
        self.legend = "Efficient Frontier"
        self.__dict__.update(config)

    def points(self):
        """ Override abstract method to generate efficient frontier points """
        dots = DotationSpace(self.pf_size, int(self.precision / 10))
        lin_mu = dots.map(self.mu)
        lin_sigma = dots.map(self.sigma)
        for i, j in zip(lin_sigma, lin_mu):
            yield (i * self.scale, j * self.scale)


# Code for third dimension plotting
# if self.pf_size == 3:
#   for x, y, z in zip(lin_sigma, lin_mu, np.linspace(0, 1, dots.counter)):
#       yield (x*scale, y*scale, z)
