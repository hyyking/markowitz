from .module_header import CacheRef
from .graph import NormalGraph, EfficientFrontier


from typing import Dict, Tuple, List

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


class Window(object):
    def __init__(
            self,
            graphs: Tuple[CacheRef, ...],
            layout_type: str
            ) -> None:

        self.normals: List[CacheRef] = list()
        self.frontiers: List[CacheRef] = list()
        self.others: List[CacheRef] = list()
        self._sort_graphs(graphs)

        self.fig = plt.figure()
        self.ltype = layout_type

    def _sort_graphs(self, graphs) -> None:
        for graph_ref in graphs:
            if graph_ref.has(hash(NormalGraph)):
                self.normals.append(graph_ref)
            elif graph_ref.has(hash(EfficientFrontier)):
                self.frontiers.append(graph_ref)
            else:
                print("Graph Type Not Recognised, plotted to other window")
                self.others.append(graph_ref)

    def make_layout(self):
        if self.ltype == "default":
            nn = len(self.normals)
            nf = len(self.frontiers)
            gs = GridSpec(nf+1, nn, figure=self.fig)
            
            ns = list()
            for i in range(nn):
                share_y = None
                if len(ns) > 0:
                    share_y = ns[i-1]

                n = self.fig.add_subplot(gs.new_subplotspec((0, i)), sharey=share_y)
                n.plot(*self.normals[i].ref().points(scale=100))
                ns.append(n)
            
            fs = list()
            for i in range(nf):
                share_ax = None
                if len(fs) > 0:
                    share_ax = fs[i-1]
                f = self.fig.add_subplot(gs.new_subplotspec((i+1, 0), colspan=nn), sharex=share_ax, sharey=share_ax)
                f.plot(*self.frontiers[i].ref().points(scale=100)[:2])
                fs.append(f)

