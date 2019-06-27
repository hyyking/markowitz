from vecs_generator import rasterize_barycentric

from collections import namedtuple

import numpy as np
from scipy.stats import norm

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as plt3d

NormalInfo = namedtuple("NormalInfo", "nom x y mu sigma")

fig_size = (6, 6)


class EfficientFrontier(object):
    def __init__(self, *elements, covar_matrix, precision, threeD):
        self.elements = elements

        self.covar_matrix = covar_matrix

        self.dist_plane = self._generate_plane(precision)
        self.precision = precision

        self.threeD = threeD

        self.fig, self.ax = plt.subplots(
            figsize=fig_size
        )

    def _generate_plane(self, precision):
        assert(len(self.elements) < 4)

        if len(self.elements) == 2:
            x = np.linspace(0, 1, precision)
            return np.array(list(zip(x, 1-x)))

        if len(self.elements) == 3:
            return rasterize_barycentric(precision)

    def set_config(self):
        self.ax.set_xlabel("Risk (sigma)")
        self.ax.set_ylabel("Gains (mu)")
        self.ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    def ef_plot(self):
        if not self.threeD:
            self.ax.plot(
                self.sigma()*100,
                self.mu()*100,
                'k--',
                label="Courbe d'efficience"
            )
            self.set_config()

        else:
            self.ax = plt3d.Axes3D(self.fig)


            self.ax.set_zlabel("Part de {}".format(self.elements[0].name.title()))

            self.ax.plot(
                self.sigma()*100,
                self.mu()*100,
                np.linspace(0, 1, self.precision**2 + 100),
                'k-',
                label="Courbe d'efficience"
            )
            self.set_config()


class Frontiers(object):
    def __init__(self, args):
        super(Frontiers, self).__init__(*args)
        self.ef_plots = list()

    def add_ef(self, *args, precision=100, threeD=False):
        unwraped = [self.assets[arg] for arg in args]
        self.ef_plots.append(
            EfficientFrontier(*unwraped, covar_matrix=self.sub_covar(*args), precision=precision, threeD=threeD)
        )

    def plot_all_ef(self):
        for ef in self.ef_plots:
            ef.ef_plot()


class NormalCurve(object):
    def __init__(self, args):
        super(NormalCurve, self).__init__(args)
        self.infos = list()

    def _norm_cfg(self, ax):
        ax.set_title('Normal Distribution of Portfolio Assets Variation ~> N(mu, sigma)')
        ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


    def add_norm(self, t):
        mu = self.avg(t)*100
        sigma = self.stdv(t)*100

        x = np.linspace(mu-10, mu+10, 500)
        y = norm.pdf(x, mu, sigma)

        self.infos.append(NormalInfo(t, x, y, mu, sigma))

    def norm_plot(self):
        if len(self.infos) > 0:
            norm_fig, norm_ax = plt.subplots(figsize=fig_size)
            for builder in self.infos:
                norm_ax.plot(
                        builder.x,
                        builder.y,
                        label= "{} ~> N({}, {})".format(builder.nom.title(), str(round(builder.mu, 4)), str(round(builder.sigma, 4)))
                )
            self._norm_cfg(norm_ax)

class Graphics(NormalCurve, Frontiers, Portfolio):
    def __init__(self, *args):
        super(Graphics, self).__init__(args)

    def show(self):
        self.norm_plot()
        self.plot_all_ef()

        self.infos = list()
        self.ef_plots = list()

        return plt.show()

if __name__ == "__main__":
    import sys, os
    sys.path.append(os.getcwd() + "/markowitz")
    from structures import Asset, Portfolio

    t1 = Asset("airliquide")
    t2 = Asset("pernodricard")
    t3 = Asset("loreal")

    g = Graphics(t1, t2, t3)

    g.add_norm("loreal")
    g.add_norm("airliquide")

    g.add_ef("loreal", "pernodricard", "airliquide", threeD=True)
    g.add_ef("loreal", "pernodricard", "airliquide")

    g.show()
