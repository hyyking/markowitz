import re
from math import gcd
import copy


settings_types = {
    "precision": int,
    "scale": int,
}

default_conf = {
    "scale": 1,
    "precision": 1000,
}

class Window(object):
    def __init__(self, name, config, content):
        self.name = name
        self.cfg = config
        self.content = content[0]
        
        self.rows = len(self.content)
        self.cols = content[1]

        self.span = self.span_matrix()

    def span_matrix(self):
        matrix = [
            [None for _ in range(self.cols)]
            for _ in range(len(self.content))
        ]

        for i, row in enumerate(self.content):
            rl = len(row)
            # cp = self.colnb % 2 == 0
            rp = rl % 2 == 0

            if self.cols % rl == 0:
                matrix[i] = [self.cols/rl for _ in range(rl)]

            elif rl == 1:
                matrix[i] = [self.cols]
 
            elif rp:  # PAIR
                mod = self.cols % rl
                gc = (self.cols - mod)/rl
                matrix[i] = [gc for _ in range(rl)]
                matrix[i][0] += mod

            elif not rp:  # IMPAIRE
                mod = self.cols % rl
                gc = (self.cols - mod)/rl
                matrix[i] = [gc for _ in range(rl)]
                index = int(rl/2 - 0.5)
                matrix[i][index] += mod
            else:
                print("Don't know how to determin the layout")

        return matrix



def parse_config(cfg_str):
    cfg = copy.deepcopy(default_conf)
    if cfg_str is None:
        return cfg

    settings = cfg_str.split(",")
    for setting in settings:
        val = setting.split("=")
        assert(len(val) == 2)
        name = val[0]
        value = val[1]
        cfg[name] = settings_types[name](value) 
    
    return cfg



def parse_content(con_str):
    max_cols = 0
    rows = list(re.finditer(r"\[(.*?)\]", con_str))
    for i, row in enumerate(rows):
        row_content = row.group(1)
        cols = row_content.split("|")
        if len(cols) > max_cols:
            max_cols = len(cols)
        for o, element in enumerate(cols):
            objs = list(re.finditer(r"(.+?)\((.+?)\)", element))
            for n, m in enumerate(objs):
                graph_class = m.group(1)
                assets = m.group(2)
                objs[n] = (graph_class, assets) 
            cols[o] = objs
        rows[i] = cols
    return rows, max_cols


def layout_parse(raw):
    windows = list()
    for window in re.finditer(r"&(\w+?)(\((.*?)\))?{(.*?)}", raw):
        
        name = window.group(1)
        config = parse_config(window.group(3))
        content = parse_content(window.group(4))
        
        windows.append(Window(name, config, content)) 
    return windows
