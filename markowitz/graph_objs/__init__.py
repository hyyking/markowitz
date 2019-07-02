from importlib import import_module


def build(db, class_ref, asset_str, **config):
    asset = asset_str.split("/")

    imp_ref = ".{}".format(class_ref.lower())

    graph_module = import_module(imp_ref, "markowitz.graph_objs")
    graph_class = getattr(graph_module, class_ref)

    if len(asset) == 1:  # Only One Asset to load
        a = db.load(asset[0])
        return graph_class(a)

    elif len(asset) > 1:  # Load Portfolio
        p = db.load(*asset)
        return graph_class(p)
