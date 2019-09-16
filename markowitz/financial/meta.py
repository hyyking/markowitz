""" MetaAsset Metaclass """


class MetaAsset(type):
    """ keep only one instance of all assets and portfolio """
    cache = dict()

    def __call__(cls, *ls, **kw):
        names = ls[0]

        if isinstance(names, str):
            name = names
            if name not in cls.cache:
                cls.cache[name] = super(MetaAsset, cls).__call__(*ls, **kw)

        elif isinstance(names, list):
            name = "/".join([n.name for n in names])
            if name not in cls.cache:
                cls.cache[name] = super(MetaAsset, cls).__call__(*ls, **kw)

        return cls.cache[name]

    @staticmethod
    def get(key):
        """ get a cached asset """
        return MetaAsset.cache[key]
