# Headers
# ----------------------------------------------------------------------------------------------------------
from .module_header import m_types, m_maths, m_utils, m_structs


# Utils Functions
# ----------------------------------------------------------------------------------------------------------
def _portfolio_descriptor(portfolio: m_types.PF_TYPE) -> m_structs.DataFrame:
    assets_df = m_structs.DataFrame(
        {
            '{}'.format(t.name): [len(t.df), t.avg, t.stdv, ""]
            for t in portfolio.assets.values()
        },
        index=["len", "avg", "stdv", "COVAR"]
    )

    empty_df = m_structs.DataFrame(
        {"{}".format(t): [""] for t in portfolio.assets},
        index=["CORR"]
    )

    result: m_structs.DataFrame = m_utils.concat([
        assets_df,
        portfolio.covar_matrix,
        empty_df,
        portfolio.corr_matrix
    ])
    return result


# Public API
# ----------------------------------------------------------------------------------------------------------
class m_Portfolio(m_structs.PF_TYPE):

    def __init__(self, titres: m_types.A_TYPE_COLLECTION) -> None:
        self.assets: m_types.A_TYPE_MAP = dict(
            (titre.name, titre) for titre in titres
        )

        self.covar_matrix = self._covar_m()
        self.corr_matrix = self._corr_m()

    def __repr__(self) -> str:
        return str(_portfolio_descriptor(self))

    def __getitem__(self, key: str) -> m_types.A_TYPE:
        return self.assets[key]

    def __setitem__(self, key: str, item: m_types.A_TYPE) -> None:
        self.assets[key] = item

    def __len__(self):
        return len(self.assets)

    def _covar_m(self) -> m_structs.DataFrame:
        names = tuple(self.assets.keys())
        avgs = tuple(titre.avg for titre in self.assets.values())

        n_nb = len(names)
        matrix = m_maths.zeros((n_nb, n_nb))
        for i in range(n_nb):
            for o in range(n_nb):
                n1, n2 = (names[i], names[o])
                if i == o:
                    matrix[i][o] = self.assets[n1].stdv * self.assets[n2].stdv
                else:
                    mul = self.assets[n1].df * self.assets[n2].df
                    matrix[i][o] = mul.mean() - (avgs[i] * avgs[o])

        return m_structs.DataFrame(data=matrix, columns=names, index=names)

    def _corr_m(self) -> m_structs.DataFrame:
        names = tuple(self.assets.keys())
        stdvs = tuple(titre.stdv for titre in self.assets.values())

        n_nb = len(names)
        matrix = m_maths.zeros((n_nb, n_nb))
        for i in range(n_nb):
            for o in range(n_nb):
                n1, n2 = (names[i], names[o])
                matrix[i][o] = self.covar_matrix[n1][n2]/(stdvs[i] * stdvs[o])

        return m_structs.DataFrame(data=matrix, columns=names, index=names)

    def covar(self, t1: str, t2: str) -> m_types.M_FLOAT:
        return m_types.M_FLOAT(self.covar_matrix[t1][t2])

    def corr(self, t1: str, t2: str) -> m_types.M_FLOAT:
        return m_types.M_FLOAT(self.corr_matrix[t1][t2])

    def avg(self, dot: m_types.FLOAT_COLLECTION) -> m_types.M_FLOAT:
        mus = [el.avg for el in self.assets.values()]
        assert(len(dot) == len(mus))
        result: float = 0
        for i in range(len(dot)):
            result += dot[i] * mus[i]
        return m_types.M_FLOAT(result)

    def stdv(self, dot: m_types.FLOAT_COLLECTION) -> m_types.M_FLOAT:
        assert(len(dot) == len(self.assets))
        product = m_maths.dot(m_maths.symmetric_matrix(dot), self.covar_matrix)
        trace = m_maths.trace(product)
        return m_types.M_FLOAT(trace)
