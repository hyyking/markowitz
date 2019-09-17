""" Loader Class """

import sqlite3 as sqll
import pandas as pd

from .financial import MetaAsset, Asset, Portfolio

__all__ = "Loader"


class Loader:
    """ Holds the state of the data that could be loaded
    Works like a switch statement:
    - _loader becomes the method that will load the assets:
        - sqlite for sqlite databases
        - csv for a list of csv files
        - _default if it's not found
    - input is a list of input files (first file is used for sqlite)
    """

    def __init__(self, filetype: str, inputfile: str, column: str):
        self._loader = getattr(self, filetype, "_default")
        self._filetype = filetype
        self.input = inputfile
        self.column = column

    def _default(self, assets):
        raise NotImplementedError(
            f"This loader {self._filetype} is not implemented and will not load {assets}"
        )

    def load(self, asset: str):
        """ load an asset """
        assets = asset.split("/") if "/" in asset else asset
        return self._loader(assets)

    @staticmethod
    def _load_as(assets):
        if isinstance(assets, str):
            return MetaAsset.get(assets)
        if isinstance(assets, list):
            return Portfolio([MetaAsset.get(asset) for asset in assets])
        raise NotImplementedError

    def sqlite(self, assets):
        """ sqlite loader """
        not_loaded = list(MetaAsset.reduce(assets))

        if not_loaded:
            conn = sqll.connect(self.input[0])
            for name in not_loaded:
                series = pd.read_sql_query(
                    f"SELECT {self.column} FROM {name.upper()}", conn
                )
                Asset(name, series[self.column].pct_change().values[1:])
            conn.close()
        return self._load_as(assets)

    def csv(self, assets):
        """ csv loader """
        not_loaded = list(MetaAsset.reduce(assets))
        if not_loaded:
            for name in not_loaded:
                if name + ".csv" in self.input:
                    series = pd.read_csv(name + ".csv", sep=";")
                    Asset(name, series[self.column].pct_change().values[1:])
        return self._load_as(assets)
