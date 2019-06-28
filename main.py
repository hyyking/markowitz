from markowitz.structures import Asset, DB_Connection, Portfolio


def markowitz_API_TEST():
    assets = list()
    with DB_Connection("cac40.db") as con:
        for asset in ["lvmh", "peugeot", "axa"]:
            assets.append(
                Asset.load_sql(con, asset)
            )

    p = Portfolio(assets)
    print(
        p.avg((0.1, 0.8))
    )


def graph_API_TEST():
    from markowitz.graph import D_Space, NormalGraph, EfficientFrontier, Window
    from markowitz.graph.module_header import ObjectCache
    import matplotlib.pyplot as plt

    assets = list()
    with DB_Connection("cac40.db") as con:
        for asset in ["lvmh", "peugeot", "axa"]:
            assets.append(
                Asset.load_sql(con, asset)
            )

    p = Portfolio(assets[:2])
    p2 = Portfolio(assets[1:])

    n1 = NormalGraph(p["lvmh"].avg, p["lvmh"].stdv)
    n2 = NormalGraph(p["peugeot"].avg, p["peugeot"].stdv)
    n3 = NormalGraph(p2["axa"].avg, p2["axa"].stdv)
    
    ef = EfficientFrontier(len(p), p.avg, p.stdv)
    ef2 = EfficientFrontier(len(p2), p2.avg, p2.stdv)

    w = Window((n1, n2, n3, ef, ef2), 'default').make_layout()
    
    plt.show()


if __name__ == "__main__":
    # markowitz_API_TEST()
    graph_API_TEST()
