""" MetaAsset Metaclass """

__all__ = ["MetaAsset"]


class MetaAsset(type):
    """ keep only one instance of all assets and portfolio """

    cache = dict()

    def __call__(cls, *ls, **kw):
        names = ls[0]

        if isinstance(names, str):
            if names not in cls.cache:
                cls.cache[names] = super(MetaAsset, cls).__call__(*ls, **kw)

        elif isinstance(names, list):
            names = "/".join([n.name for n in names])
            if names not in cls.cache:
                cls.cache[names] = super(MetaAsset, cls).__call__(*ls, **kw)
        else:
            raise NotImplementedError

        return cls.cache[names]

    @staticmethod
    def get(key):
        """ get a cached asset """
        return MetaAsset.cache[key]

    @staticmethod
    def reduce(keys):
        """ reduce the list of assets to load """
        if isinstance(keys, str) and keys not in MetaAsset.cache:
            return [keys]
        if isinstance(keys, list):
            return filter(lambda x: x not in MetaAsset.cache, keys)
        return []
