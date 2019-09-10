""" *.ly file parser
    Using regex so most errors are ignored except when translating to concrete types
"""
import re

from .window import Window
from ..graphs.abstract import AbstractGraph


def clean_file(content):
    """ clean comments and whitespace """
    no_comments = re.sub(r"!.*?\n", "", content)
    no_escape = re.sub(r"[\n\t\s]", "", no_comments)
    return no_escape


def parse_config(cfg_str):
    """ Parse config from layout file
        default config are the AbstractGraph private fields
        will be modified affter during execution
    """
    cfg = {
        key: value
        for key, value in AbstractGraph.__dict__.items()
        if key[0] == "_" and key[1] != "_" and "abc" not in key
    }
    if cfg_str is None:
        return cfg

    settings = cfg_str.split(",")
    for setting in settings:
        val = setting.split("=")
        if not len(val) == 2:
            raise ValueError("Separate option name and value with =")
        name, value = f"_{val[0]}", val[1]
        if hasattr(AbstractGraph, name):
            cfg[name] = type(cfg[name])(value)

    return cfg


_LAYOUT_SPLIT_REGEX = re.compile(r"&(\w+?)(\((.*?)\))?{(.*?)}")
_ROWS_REGEX = re.compile(r"\[(.*?)\]")
_OBJ_REGEX = re.compile(r"(.+?)\((.+?)\)")

def parse_objs(objs):
    """ parse the multiple objects """
    for i, objm in enumerate(objs):
        graph_class = objm.group(1)
        assets = objm.group(2)
        objs[i] = (graph_class, assets)
    return objs

def parse_cols(cols):
    """ parse window columns """
    for j, element in enumerate(cols):
        objs = list(_OBJ_REGEX.finditer(element))
        cols[j] = parse_objs(objs)
    return cols

def parse_content(con_str):
    """ parse content of the window in layout file """
    max_cols = 0
    rows = list(_ROWS_REGEX.finditer(con_str))
    for i, row in enumerate(rows):
        cols = row.group(1).split("|")
        max_cols = len(cols) if len(cols) > max_cols else max_cols
        rows[i] = parse_cols(cols)
    return rows, max_cols

def parse(raw):
    """ Parse layout file """
    windows = list()
    for window in _LAYOUT_SPLIT_REGEX.finditer(raw):

        name = window.group(1)
        config = parse_config(window.group(3))
        content, max_cols = parse_content(window.group(4))

        windows.append(Window(name, max_cols, config, content))
    return windows
