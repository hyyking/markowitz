""" PyMarkowitz command line utility """

import argparse as ap

from matplotlib.pyplot import show, style

from markowitz.parser import from_file
from markowitz.loader import Loader
from markowitz import consumme_window


def build_arg_parser():
    """ Argument Parser """
    parser = ap.ArgumentParser(
        prog="PyMarkowitz",
        description="Display Assets and Portfolio Graphs from Layout Files",
        usage="%(prog)s [options] LAYOUT INPUT [INPUT...]"
    )

    parser.add_argument("layout", help="layout file path")
    parser.add_argument("input", help="data input file(s)", nargs="+")

    parser.add_argument("-l", "--loader", help="loader (default: %(default)s)", default="sqlite")
    parser.add_argument(
        "-c", "--column", help="name of the header (default: %(default)s)", default="clot"
    )

    parser.add_argument("--debug", help="activate debug mode", action="store_true")
    parser.add_argument("--style", help="matplotlib graph style", default="bmh")

    return parser


if __name__ == "__main__":
    ARGS = build_arg_parser().parse_args()

    style.use(ARGS.style)

    # NOTE: ADD DEBUG MODE

    LOADER = Loader(ARGS.loader, ARGS.input, ARGS.column)
    LAYOUT = from_file(ARGS.layout)

    for WINDOW in LAYOUT:
        consumme_window(WINDOW, LOADER)

    show()
