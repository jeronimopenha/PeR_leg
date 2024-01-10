import pygraphviz as pgv
import networkx as nx
from math import ceil, sqrt


class ProjGraph:
    # _instance = None

    # def __new__(cls, dot: str):
    #    if cls._instance is None:
    #        cls._instance = super().__new__(cls)
    #    return cls._instance

    def __init__(self, dot: str):
        self.dot = dot
        self.nodes = []
        self.n_nodes = 0
        self.edges = []
        self.nodes_to_idx = {}
        self.neighbors = {}
        self.n_cells = 0
        self.n_cells_sqrt = 0
        self.get_dot_vars()

    def get_dot_vars(self):
        dot = self.dot

        gv = pgv.AGraph(dot, strict=False, directed=True)
        g = nx.DiGraph(gv)
        self.nodes = list(g.nodes)
        self.n_nodes = len(self.nodes)
        self.edges = list(g.edges)
        self.nodes_to_idx = {}
        self.neighbors = {}
        for i in range(self.n_nodes):
            self.nodes_to_idx[self.nodes[i]] = i

        for e in self.edges:
            if self.nodes_to_idx[e[0]] not in self.neighbors.keys():
                self.neighbors[self.nodes_to_idx[e[0]]] = []
            if self.nodes_to_idx[e[1]] not in self.neighbors.keys():
                self.neighbors[self.nodes_to_idx[e[1]]] = []
            self.neighbors[self.nodes_to_idx[e[0]]].append(
                self.nodes_to_idx[e[1]])
            self.neighbors[self.nodes_to_idx[e[1]]].append(
                self.nodes_to_idx[e[0]])

        self.n_cells_sqrt = ceil(sqrt(self.n_nodes))
        self.n_cells = pow(self.n_cells_sqrt, 2)
