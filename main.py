from markowitz.structs import DBCache, _Cache
from markowitz.graph_objs import build


import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    db = DBCache("cac40.db")

    a = build(db, "EfficientFrontier", "axa/lvmh")

    data = list(a.points(scale=100))
    
    fig, ax = plt.subplots()
    ax.plot(*zip(*data), "r-")
    plt.show()
