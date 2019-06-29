from .asset import m_Asset as _Asset
from .portfolio import m_Portfolio as _Portfolio
from .module_header import _Cache, Dict


import sqlite3 as sql

class _Singleton(type):
    _instances: Dict[str, object] = dict()
    def __call__(cls, *args, **kwargs):
        if args[0] not in cls._instances:
            cls._instances[args[0]] = super(_Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[args[0]]


class DBCache(object, metaclass=_Singleton):
    def __init__(self, db_path):
        self.db = sql.connect(db_path)

    def load(self, *assets):
        if len(assets) == 0:
            print("Nothing to load")
            return None

        if len(assets) == 1:
            asset = assets[0]
            if asset not in _Cache.cache:
                return _Asset.load_sql(self.db, asset)
            else:
                return _Cache.cache[asset]
        
        elif len(assets) > 1:
            pf = list()
            for a in assets:
                if a not in _Cache.cache:
                    _Asset.load_sql(self.db, a)
                pf.append(_Cache.cache[a])
            return _Portfolio(pf)
        
        return None

    def __del__(self):
        self.db.close()


