# Dependencies
# ----------------------------------------------------------------------------------------------------------
from typing import Tuple, Union, Callable, Collection, Dict, Any
import pandas as pd
import numpy as np

# Public Interface
# ----------------------------------------------------------------------------------------------------------
__all__ = ['m_types', 'm_utils', 'm_structs', 'm_maths']


# Types namespace
# ----------------------------------------------------------------------------------------------------------

class _data_types:
    class PD_DATAFRAME(pd.DataFrame):
        pass

    class NP_ARRAY(np.ndarray):
        pass

    class M_FLOAT(float):
        def __float__(self):
            return self

    FLOAT_COLLECTION = Tuple[float, ...]


class _LOCAL_A_TYPE(object):
    """Public API to Create Portfolio Compatible Assets"""
    # ----- Attributes
    # ___ Private
    _table_data_origin: Union[str, int, Tuple[Any], Dict[Any, Any]]
    # ___ Public
    name:       str
    df:         _data_types.PD_DATAFRAME    # Data Series
    avg:        _data_types.M_FLOAT         # Average of self->df
    stdv:       _data_types.M_FLOAT         # Standart Deviation of self->df

    # ----- Magic Methods
    __init__:           Callable[[Any], None]


class _A_types(object):
    class A_TYPE(_LOCAL_A_TYPE):
        pass
    A_TYPE_COLLECTION = Collection[A_TYPE]
    A_TYPE_MAP = Dict[str, A_TYPE]


class _LOCAL_PF_TYPE(object):
    """Public API for creating a Portfolio"""
    # ----- Attributes
    assets:         _A_types.A_TYPE_MAP
    covar_matrix:   _data_types.PD_DATAFRAME
    corr_matrix:    _data_types.PD_DATAFRAME

    # ----- Magic Methods
    __init__:       Callable[[_A_types.A_TYPE_COLLECTION], None]
    __getitem__:    Callable[[str], _A_types.A_TYPE]
    __setitem__:    Callable[[str, _A_types.A_TYPE], None]

    # ----- Methods
    # ___ Public
    covar:      Callable[[str, str], _data_types.M_FLOAT]
    corr:       Callable[[str, str], _data_types.M_FLOAT]
    avg:        Callable[[_data_types.FLOAT_COLLECTION], _data_types.M_FLOAT]
    stdv:       Callable[[_data_types.FLOAT_COLLECTION], _data_types.M_FLOAT]


class _PF_types:
    class PF_TYPE(_LOCAL_PF_TYPE):
        pass
    PF_TYPE_COLLECTION = Collection[PF_TYPE]
    PF_TYPE_MAP = Dict[str, PF_TYPE]


class m_types(_data_types, _A_types, _PF_types):
    pass

# Other Namespaces
# ----------------------------------------------------------------------------------------------------------


class m_structs:
    A_TYPE = _LOCAL_A_TYPE
    PF_TYPE = _LOCAL_PF_TYPE

    DataFrame = pd.DataFrame
    array = np.array


class m_utils:
    read_sql_query = pd.read_sql_query
    concat = pd.concat


class m_maths:
    sqrt = np.sqrt
    trace = np.trace
    dot = np.dot
    zeros = np.zeros

    @staticmethod
    def symmetric_matrix(point: m_types.FLOAT_COLLECTION) -> m_types.NP_ARRAY:
        matrix = list()
        for i in range(len(point)):
            mid = list()
            for o in range(len(point)):
                if i == o:
                    mid.append(point[i] * point[o])
                else:
                    mid.append((point[i]*point[o])/2)
            matrix.append(m_structs.array(mid))
        return m_structs.array(matrix)
