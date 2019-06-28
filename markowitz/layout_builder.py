import re

from .structures import DB_Connection, Asset, Portfolio

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


class Layout(object):
    def __init__(self, name, content, cols):
        self.name = name
        self.content = content

        self.cols = cols
        self.rows = len(content)


def _parse_content(content):
    max_col = 0
    rows = re.split(r"\[(.*?)\]", content)

    valid = list()
    for row in rows:
        if row != "":
            columns = row.split("|")

            if len(columns) > max_col:
                max_col = len(columns)

            for i, token in enumerate(columns):
                m = re.match(r"(\w+?)\((.+?)\)", token)
                columns[i] = (m.group(1), m.group(2))

            valid.append(columns)

    return valid, max_col


def _capture_windows(content):
    layouts = list()
    for m in re.finditer(r"\[window=(\w*)\]{(.*?)}", content):
        if m.group(0) != "":
            if m.group(1) != "":
                if m.group(2) != "":
                    layouts.append(
                        Layout(
                            m.group(1),
                            *_parse_content(m.group(2))
                        )
                    )
                else:
                    print("Empty Window Content")
            else:
                print("Invalid Window Name")
    return layouts



def from_file(file_name):
    cleaned = None
    with open(file_name, "r") as ly:
        cleaned = ly.read().replace(" ", "").replace("\n", "").replace("\t", "")
    return _capture_windows(cleaned)


def load_asset(asset):
    ret = None
    return ret

def deploy(layoutsn, db):
    for l in layouts:
        fig = plt.figure(l.name)
        gs = GridSpec(l.rows, l.cols, figure=fig)  # (rows, cols)
        
        with DB_Connection(db) as con: 
            for o, row in enumerate(l.content):
                span = 1
                if len(row) < l.rows:
                    
                for i, col in enumerate(row):
                    g_type, asset = col
                    
                    if g_type == "Norm":
                        asset = Asset.load_sql(con, asset)
                    
                    elif g_type == "Eff":
                        assets = list(
                            map(lambda x: Asset.load_sql(con, x), asset.split("/"))
                        )
                        p = Portfolio(*assets)


        print(l.content)

    return True
