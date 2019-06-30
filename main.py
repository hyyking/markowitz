from markowitz.structs import DBCache, MetaDBCache
from markowitz.graph_objs import build
from markowitz.layout_parser import from_file

from matplotlib.pyplot import show, figure
from matplotlib.gridspec import GridSpec

import argparse as ap

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



def build_arg_parser():
    parser = ap.ArgumentParser(description="Display Assets and Portfolio graphs from layout")
    parser.add_argument('layout', help="Layout file path")
    parser.add_argument('database', help="Sqlite database path")
    parser.add_argument('--debug', help="Activate debug mode", action="store_true")
    return parser


if __name__ == "__main__":
    args = build_arg_parser().parse_args()

    if args.debug:
        MetaDBCache.debug()

    db = DBCache(args.database)
    layout = from_file(args.layout)

    for window in layout:
        consumme_window(window, db)

    show()
