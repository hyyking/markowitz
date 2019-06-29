from .module_header import _Graph, np
from .spaces import DotationSpace

class EfficientFrontier(_Graph):
    def __init__(self, portfolio) -> None:
        self.pf_size = len(portfolio)
        self.mu = portfolio.avg
        self.sigma = portfolio.stdv

        super(EfficientFrontier, self).__init__()

    def points(self, scale=1):
        dots = DotationSpace(self.pf_size, int(self.precision/10))
        lin_mu = dots.map(self.mu)
        lin_sigma = dots.map(self.sigma)

        if self.pf_size == 3:
            for x, y, z in zip(lin_sigma, lin_mu, np.linspace(0, 1, dots.counter)):
                yield (x*scale, y*scale, z)
        else:
            for x, y in zip(lin_sigma, lin_mu):
                yield (x*scale, y*scale)

