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
    from markowitz.graph import D_Space, NormalGraph, EfficientFrontier
    from markowitz.graph.module_header import ObjectCache
    import matplotlib.pyplot as plt

    assets = list()
    with DB_Connection("cac40.db") as con:
        for asset in ["lvmh", "peugeot", "axa"]:
            assets.append(
                Asset.load_sql(con, asset)
            )

    p = Portfolio(assets)

    nm = NormalGraph(p["lvmh"].avg, p["lvmh"].stdv).ref().points(scale=100)
    ef = EfficientFrontier(len(p), p.avg, p.stdv).ref().points(scale=100)

    fig, ax = plt.subplots()
    ax.plot(*ef[:2])
    
    fig, ax = plt.subplots()
    ax.plot(*nm)

    plt.show()


if __name__ == "__main__":
    # markowitz_API_TEST()
    graph_API_TEST()
