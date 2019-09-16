""" Loader Class """

import sqlite3 as sqll
import pandas as pd

from .financial import MetaAsset, Asset, Portfolio


class Loader:
    """ Loader instance to load assets """

    def __init__(self, filetype: str, inputfile: str, column: str):
        self._loader = getattr(self, filetype)
        self.input = inputfile
        self.column = column

    def load(self, asset: str):
        """ load an asset """
        assets = asset.split("/") if "/" in asset else asset
        return self._loader(assets)

    def sqlite(self, assets):
        """ sqlite loader """
        not_loaded = list(MetaAsset.reduce(assets))

        if not_loaded:
            conn = sqll.connect(self.input)
            for name in not_loaded:
                series = pd.read_sql_query(
                    f"SELECT {self.column} FROM {name.upper()}", conn
                )
                Asset(name, series[self.column].pct_change().values[1:])
            conn.close()

        if isinstance(assets, str):
            return MetaAsset.get(assets)
        if isinstance(assets, list):
            return Portfolio([MetaAsset.get(asset) for asset in assets])

        raise NotImplementedError

    def csv(self, assets):
        """ csv loader """
