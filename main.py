from markowitz.structures import Asset, DB_Connection, Portfolio

def markowitz_API_TEST():
    assets = list()
    with DB_Connection("cac40.db") as con:
        for asset in ["lvmh", "peugeot"]:
            assets.append(
                Asset.load_sql(con, asset)
            )

    p = Portfolio(assets)

    print(
        p.avg((0.1, 0.8))
    )


def graph_API_TEST():
    from markowitz.graph import D_Space, NormalGraph
    from markowitz.graph.module_header import ObjectCache
    import matplotlib.pyplot as plt

    g = NormalGraph(0, 1)

    fig, ax = plt.subplots()
    ax.plot(*g.ref().points(), 'k--')
    plt.show()


if __name__ == "__main__":
    # markowitz_API_TEST()
    graph_API_TEST()
