""" PyMarkowitz lib entry """

from matplotlib.pyplot import figure
from matplotlib.gridspec import GridSpec

from .graphs import build


def load_sub_plots(sub, loader, col, config):
    """ load all sub plots of a graph """
    for cls_name, asset_name in col:
        graph = build(loader, cls_name, asset_name, **config)
        sub.plot(*zip(*graph.points()), label=graph.legend)
        sub.set_title(str(asset_name))
        sub.legend(loc="upper right")


def consumme_window(window, loader):
    """ Consumme a Window object to create a matplotlib figure adjusted by the GridSpec """
    fig = figure(window.name, figsize=(15, 10))
    grid = GridSpec(window.rows, window.cols, figure=fig)

    for i, _ in enumerate(window.content):
        span = 0
        for j, col in enumerate(window.content[i]):
            sub = fig.add_subplot(
                grid.new_subplotspec((i, j + span), colspan=int(window.span[i][j]))
            )
            span += int(window.span[i][j]) - 1
            load_sub_plots(sub, loader, col, window.cfg)
