""" Portfolio class """

import numpy as np
import pandas as pd


def symmetric_matrix(points: tuple) -> np.array:
    """ return the symmetric matrix of a quadratic equation"""
    matrix = []
    for i, _ in enumerate(points):
        mid = []
        for j in enumerate(points):
            if i == j:
                mid.append(points[i] * points[j])
                continue
            mid.append((points[i] * points[j]) / 2)
        matrix.append(np.array(mid))
    return np.array(matrix)


class Portfolio:
    """ Representation of a portfolio of assets """

    def __init__(self, titres: list):
        self.assets = dict((titre.name, titre) for titre in titres)

        self.covar_matrix = self._covar_m()
        self.corr_matrix = self._corr_m()

    def __getitem__(self, key: str):
        return self.assets[key]

    def __setitem__(self, key: str, item):
        self.assets[key] = item

    def __len__(self):
        return len(self.assets)

    def _covar_m(self) -> pd.DataFrame:
        names = tuple(self.assets.keys())
        avgs = tuple(titre.avg for titre in self.assets.values())

        matrix = np.zeros((len(names), len(names)))
        for i, _ in enumerate(names):
            for j, _ in enumerate(names):
                if i == j:
                    matrix[i][j] = (
                        self.assets[names[i]].stdv * self.assets[names[j]].stdv
                    )
                    continue
                mul = self.assets[names[i]].values * self.assets[names[j]].values
                matrix[i][j] = mul.mean() - (avgs[i] * avgs[j])

        return pd.DataFrame(data=matrix, columns=names, index=names)

    def _corr_m(self) -> pd.DataFrame:
        names = tuple(self.assets.keys())
        stdvs = tuple(titre.stdv for titre in self.assets.values())

        matrix = np.zeros((len(names), len(names)))
        for i, _ in enumerate(names):
            for j, _ in enumerate(names):
                matrix[i][j] = self.covar_matrix[names[i]][names[j]] / (
                    stdvs[i] * stdvs[j]
                )

        return pd.DataFrame(data=matrix, columns=names, index=names)

    def covar(self, asset_one: str, asset_two: str) -> np.float64:
        """ return the covariance between two assets """
        return self.covar_matrix[asset_one][asset_two]

    def corr(self, asset_one: str, asset_two: str) -> np.float64:
        """ return the correlation between two assets """
        return self.corr_matrix[asset_one][asset_two]

    def avg(self, dot: tuple) -> np.float64:
        """ return the returns of the portfolio for this asset distribution """
        mus = [el.avg for el in self.assets.values()]
        return np.sum([dot[i] * mus[i] for i, _ in enumerate(dot)])

    def stdv(self, dot: tuple) -> np.float64:
        """ return the risk of the portfolio for this asset distribution """
        product = np.dot(symmetric_matrix(dot), self.covar_matrix)
        return np.sqrt(np.trace(product))

    def recap(self) -> str:
        """ recap dataframe of the portfolio """
        assets_df = pd.DataFrame(
            {f"{t.name}": [len(t.df), t.avg, t.stdv, ""] for t in self.assets.values()},
            index=["len", "avg", "stdv", "COVAR"],
        )
        empty_df = pd.DataFrame({f"{t}": [""] for t in self.assets}, index=["CORR"])
        return pd.concat([assets_df, self.covar_matrix, empty_df, self.corr_matrix])
