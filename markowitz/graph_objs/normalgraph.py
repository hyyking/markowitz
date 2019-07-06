from .module_header import _Graph, np
from .spaces import RangeSpace


class NormalGraph(_Graph):
    const1 = np.sqrt(2*np.pi)

    def __init__(self, asset) -> None:
        self.mu = asset.avg
        self.sigma = asset.stdv
        self.legend = "N({}, {})".format(
                round(self.mu, 2), round(self.sigma, 2))
        super(NormalGraph, self).__init__()

    @staticmethod
    def f(point, *args):
        t1 = 1/(args[1]*NormalGraph.const1)
        x = (point-args[0])/args[1]
        t2 = np.exp(-0.5*x*x)
        return t1*t2

    def points(self, scale=1):
        self.legend = "N({}, {})".format(
                round(self.mu*scale, 2), round(self.sigma*scale, 2))

        fg = RangeSpace(-10, 10, self.precision).map(
                self.f, self.mu * scale, self.sigma * scale)
        return fg
