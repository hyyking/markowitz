from .graph_objs import build

from matplotlib.pyplot import show, figure
from matplotlib.gridspec import GridSpec


def consumme_window(window, db):
    fig = figure(window.name)
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


