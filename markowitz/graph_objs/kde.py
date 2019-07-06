from .module_header import _Graph, np
from .spaces import RangeSpace


class Kde(_Graph):
    """ Kernel Density Estimation graph """

    legend = "KDE"
    const1 = np.sqrt(2*np.pi)

    def __init__(self, asset) -> None:
        self.stdv = asset.stdv
        self.df = asset.df
        super(Kde, self).__init__()

    @staticmethod
    def _kernel(k):
        """ Kernel of the KDE (currently gaussian) """
        return (1/Kde.const1)*np.exp(-0.5*k*k)

    @staticmethod
    def f(point, df, stdv):
        """ estimation function """
        n = len(df-1)  # index 0 is NaN
        h = 1.06 * (stdv)/np.power(n, 0.2)
        pre = 1.0/(n*h)
        results = [
            Kde._kernel((point-xi)/h)
            for xi in df
            if not np.isnan(xi)
        ]
        return np.sum(results) * pre

    def points(self, scale=1):
        fg = RangeSpace(-10, 10, self.precision).map(
                self.f, self.df * scale, self.stdv * scale)
        return fg
