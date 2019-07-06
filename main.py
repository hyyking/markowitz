from markowitz.structs import DBCache, MetaDBCache
from markowitz.layout_parser import from_file
from markowitz import consumme_window, show

import argparse as ap


def build_arg_parser():
    parser = ap.ArgumentParser(
        description="Display assets and portfolio graphs from layout"
    )

    parser.add_argument('layout', help="Layout file path")
    parser.add_argument('database', help="Sqlite database path")
    parser.add_argument(
        '--debug', help="activate debug mode", action="store_true"
    )

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
