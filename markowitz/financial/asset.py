""" Asset Class """

import numpy as np
import pandas as pd


class Asset:
    """ representation of an asset """

    DEFAULT_COLUMN = "clot"

    # pylint: disable=invalid-name
    @classmethod
    def read_sql(cls, con, name: str, on=Asset.DEFAULT_COLUMN) -> "Asset":
        """ load an sqlite table """
        main_df = pd.read_sql_query(f"SELECT * FROM {name.upper()}", con)
        return cls(name, main_df[on].pct_change().values)

    def __init__(self, name: str, values: list) -> None:
        self.name = name
        self.avg = np.mean(values)
        self.stdv = np.sqrt(np.var(values))
        self.values = values

    def __repr__(self) -> str:
        return "<Titre: {name} | {lenght} | {avg} | {stdv}>".format(
            name=self.name, lenght=len(self.values), avg=self.avg, stdv=self.stdv
        )
