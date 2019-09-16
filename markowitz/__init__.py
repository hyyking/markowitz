""" PyMarkowitz lib entry """

from matplotlib.pyplot import figure
from matplotlib.gridspec import GridSpec

from .graphs import build


def consumme_window(window, loader):
    """ Consumme windows to create plots """
    fig = figure(window.name, figsize=(15, 10))
    grid = GridSpec(window.rows, window.cols, figure=fig)

    for i, _ in enumerate(window.content):
        span = 0
        for j, col in enumerate(window.content[i]):
            sub = fig.add_subplot(
                grid.new_subplotspec((i, j + span), colspan=int(window.span[i][j]))
            )
            span += int(window.span[i][j]) - 1
            for cls_name, asset_name in col:
                graph = build(loader, cls_name, asset_name, **window.cfg)
                sub.plot(*zip(*graph.points()), label=graph.legend)
                sub.set_title(str(asset_name))
                sub.legend(loc="upper right")
