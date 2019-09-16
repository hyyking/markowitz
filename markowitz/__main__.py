""" PyMarkowitz command line utility """

import argparse as ap

from matplotlib.pyplot import show, style

from markowitz.structs import DBCache, MetaDBCache
from markowitz.parser import from_file
from markowitz import consumme_window


def build_arg_parser():
    """ Argument Parser """
    parser = ap.ArgumentParser(
        description="Display assets and portfolio graphs from layout"
    )

    parser.add_argument("layout", help="Layout file path")
    parser.add_argument("database", help="Sqlite database path")
    parser.add_argument("--debug", help="activate debug mode", action="store_true")
    parser.add_argument("--style", help="matplotlib graph style", default="bmh")

    return parser


if __name__ == "__main__":
    ARGS = build_arg_parser().parse_args()
    style.use(ARGS.style)

    if ARGS.debug:
        MetaDBCache.debug()

    DB = DBCache(ARGS.database)
    LAYOUT = from_file(ARGS.layout)

    for window in LAYOUT:
        consumme_window(window, DB)

    show()
