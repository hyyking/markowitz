from .graph_objs import build

from matplotlib.pyplot import figure
from matplotlib.gridspec import GridSpec


def consumme_window(window, db):
    """ Consumme windows to create plots """
    fig = figure(window.name, figsize=(15, 10))
    gs = GridSpec(window.rows, window.cols, figure=fig)

    for i, _ in enumerate(window.content):
        span = 0
        for o, col in enumerate(window.content[i]):
            sub = fig.add_subplot(
                gs.new_subplotspec(
                    (i, o + span),
                    colspan=int(window.span[i][o])
                )
            )
            span += int(window.span[i][o]) - 1
            for cls_name, asset_name in col:
                g = build(db, cls_name, asset_name)
                data = g.points(scale=window.cfg["scale"])
                sub.plot(*zip(*data), label=g.legend)
                sub.set_title(str(asset_name))
                sub.legend(loc='upper right')
