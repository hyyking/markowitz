from markowitz.structs import DBCache, MetaDBCache
from markowitz.graph_objs import build
from markowitz.layout_parser import from_file

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

import numpy as np

def PLOT_EX():
    db = DBCache("cac40.db")
    
    MetaDBCache.debug()

    a = build(db, "EfficientFrontier", "axa/lvmh/peugeot")

    data = a.points(scale=100)

    fig, ax = plt.subplots()
    ax.plot(*zip(*data), "r-")
    
    plt.show()


def consumme_window(window, db):
    fig = plt.figure(window.name)
    gs = GridSpec(window.rows, window.cols, figure=fig)

    for i, row in enumerate(window.content):
        for o, col in enumerate(row):
            sub = fig.add_subplot(
                gs.new_subplotspec(
                    (i, o),
                    colspan=int(window.span[i][o])
                )
            )
            for graph in col:
                g = build(db, graph[0], graph[1])
                data = g.points(scale=window.cfg["scale"])
                sub.plot(*zip(*data), window.cfg["line"])


if __name__ == "__main__":
    MetaDBCache.debug()
    db = DBCache("cac40.db")
    layout = from_file("test.ly")

    for window in layout:
        consumme_window(window, db)

    plt.show()
