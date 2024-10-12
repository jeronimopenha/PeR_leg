import random as rnd
from src.old.python.util.per_graph import PeRGraph


class SaUtil(object):

    def __init__(self, proj_graph: PeRGraph):
        self.proj_graph = proj_graph

    @staticmethod
    def reset_random():
        rnd.seed(0)

    def get_initial_grid(self) -> tuple[list, list]:
        c_n = [None for i in range(self.proj_graph.n_cells)]
        n_c = [None for i in range(self.proj_graph.n_cells)]

        unsorted_nodes = [n for n in self.proj_graph.nodes]
        unsorted_cells = [i for i in range(self.proj_graph.n_cells)]

        while len(unsorted_nodes) > 0:
            r_n = rnd.randint(0, (len(unsorted_nodes) - 1))
            r_c = rnd.randint(0, (len(unsorted_cells) - 1))
            n = unsorted_nodes[r_n]
            c = unsorted_cells[r_c]

            c_n[c] = self.proj_graph.nodes_to_idx[n]
            n_c[c_n[c]] = c
            unsorted_cells.pop(r_c)
            unsorted_nodes.pop(r_n)

        return c_n, n_c
