from markowitz.structs import DBCache, _Cache
from markowitz.graph_objs import build


if __name__ == '__main__':
    db = DBCache("cac40.db")

    a = build(db, "NormalGraph", "axa")
    for i in a.points():
        print(i)

