from .cleaner import clean_file
from .parser import layout_parse


def from_file(file_name):
    layouts = None
    with open(file_name, "r") as ly:
        cleaned = clean_file(ly.read())
        layouts = layout_parse(cleaned)

    return layouts
