import random as rnd

from math import sqrt
from src.util.per_graph import PeRGraph


class Yolt(object):

    def __init__(self, per_graph: PeRGraph, n_threads: int = 1, random_seed: int = 0):
        self.latency: int = 5
        self.per_graph: PeRGraph = per_graph
        self.n_threads: int = n_threads
        self.reset_random(random_seed)

        self.edges_str: list[list] = self.per_graph.get_edges_zigzag()
        self.edges_int: list[list] = []
        for a, b, direction in self.edges_str:
            self.edges_int.append(
                [
                    self.per_graph.nodes_to_idx[a],
                    self.per_graph.nodes_to_idx[b]
                ]
            )

        self.n2c, self.c2n = self.get_initial_position(self.edges_int[0][0], self.latency)

        self.n_lines = self.per_graph.n_cells_sqrt
        self.n_columns = self.per_graph.n_cells_sqrt
        self.line_bits = int(sqrt(self.per_graph.n_cells))
        self.column_bits = self.line_bits

    @staticmethod
    def reset_random(random_seed: int = 0):
        rnd.seed(random_seed)

    def get_initial_position(self, first_node: int, latency: int = 5) -> tuple[list[list], list[list]]:
        n2c: list[list] = []
        c2n: list[list] = []
        for i in range(latency):
            n2c_tmp: list = [None for j in range(self.per_graph.n_cells)]
            c2n_tmp: list = [None for j in range(self.per_graph.n_cells)]
            idx: int = rnd.randint(0, self.per_graph.n_cells - 1)
            n2c_tmp[first_node] = idx
            c2n_tmp[idx] = first_node
            n2c.append(n2c_tmp)
            c2n.append(c2n_tmp)
        return n2c, c2n
