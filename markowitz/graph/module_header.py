from typing import Dict, Tuple


class CacheRef(object):
    def __init__(self, cache_id: int, signature: Tuple[int, int]) -> None:
        self.cache_id = cache_id
        self._signature = signature

    def __repr__(self):
        return "<CacheRef[{}] -> {}>".format(self.cache_id, self._signature)

    def signature(self):
        return self._signature

    def ref(self):
        return ObjectCache.get(self._signature)


class ObjectCache(type):
    _cached: Dict[Tuple[int, int], object] = dict()

    @staticmethod
    def whole_cache():
        return ObjectCache._cached

    @staticmethod
    def get_type(key: int) -> Dict[int, object]:
        result: Dict[int, object] = dict()
        for gen, spe in ObjectCache._cached:
            if gen == key:
                alt_key = spe
                obj = ObjectCache._cached[(gen, spe)]
                result[alt_key] = obj
        return result

    @staticmethod
    def get(key: Tuple[int, int]) -> object:
        return ObjectCache._cached[key]

    def __call__(cls, *ls, **kw) -> CacheRef:
        signature = (
                hash(cls),                                  # Class    ID
                (hash(ls) + hash(kw.values())) % hash(cls)   # Specific ID
        )

        if signature not in ObjectCache.whole_cache():
            ObjectCache._cached[signature] = super(
                ObjectCache, cls
            ).__call__(*ls, **kw)

        return CacheRef(len(ObjectCache._cached), signature)
