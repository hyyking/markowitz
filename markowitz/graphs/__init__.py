""" Graph Abstraction and Dynamic import of  """

from importlib import import_module


def build(loader, class_name, asset_str, **config):
    """
    Build a graph from class name and asset(s).
    Graphs are loaded dynamically as lowercase class_name
    in the graphs module.
    """
    to_load = f".{class_name.lower()}"

    graph_module = import_module(to_load, "markowitz.graphs")
    graph = getattr(graph_module, class_name)
    return graph(loader.load(asset_str), **config)
