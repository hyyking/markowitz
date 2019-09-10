""" *.ly file parser
    Using regex so most errors are ignored except when translating to concrete types
"""

from .parser import parse, clean_file


def from_string(string):
    """ generate windows from string """
    return parse(clean_file(string))


def from_file(file_name):
    """ generate windows from a file """
    with open(file_name, "r") as lyfile:
        return from_string(lyfile.read())
