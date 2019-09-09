from markowitz.structs import DBCache
from markowitz.graph_objs.normalgraph import NormalGraph
from markowitz.graph_objs.spaces import RangeSpace
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def hist(series, lower, upper, step):
    df = pd.DataFrame(data=series.values, columns=["vars"])
    ranje = (upper - lower) / step
    bins = [(lower + i * ranje) for i in range(step + 1)]
    return df.apply(lambda x: pd.cut(x, bins=bins).value_counts() / len(df))


if __name__ == "__main__":
    db = DBCache("cac40.db")
    a = db.load("axa")
    test = hist(a.df, -0.2, 0.2, 10)
    print(test)

    s = RangeSpace(-10, 10, 1000).map(estimation, a.df * 100, a.stdv * 100)
    plt.plot(*zip(*s))

    g = NormalGraph(a).points(scale=100)
    plt.plot(*zip(*g))

    plt.show()
