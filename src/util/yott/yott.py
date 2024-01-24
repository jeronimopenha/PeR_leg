import random as rnd

from math import sqrt
from src.util.util import Util as U
from src.util.per_graph import PeRGraph


class YOTT(object):

    def __init__(self, per_graph: PeRGraph, n_threads: int = 1, random_seed: int = 0):
        self.latency: int = 7
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
        self.edges_int = self. remove_nodes_already_placed(self.edges_int)
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

    def get_initial_position_ij(self, first_node: int, latency: int = 5) -> tuple[list[list], list[list]]:
        n2c: list[list[list]] = []
        c2n: list[list] = []
        for i in range(latency):
            n2c_tmp: list[list] = [[None, None] for j in range(self.per_graph.n_cells)]
            c2n_tmp: list[list] = [
                [
                    None for _ in range(self.per_graph.n_cells_sqrt)
                ] for _ in range(self.per_graph.n_cells_sqrt)
            ]

            idxl, idxc = U.get_line_column_cell_sqrt(rnd.randint(0, self.per_graph.n_cells - 1),
                                                     self.per_graph.n_cells_sqrt)
            n2c_tmp[first_node][0] = idxl
            n2c_tmp[first_node][1] = idxc
            c2n_tmp[idxl][idxc] = first_node
            n2c.append(n2c_tmp)
            c2n.append(c2n_tmp)

        return n2c, c2n
    
    def remove_nodes_already_placed(self,ITL):
        dic = {ITL[0][0]:True,
            ITL[0][1]:True}
        new_ITL = [ITL[0]]
        print(ITL)
        for dst,src in (ITL[1:]):
            if dic.get(src) is None:
                dic[src] = True
                new_ITL.append([dst,src])
        return new_ITL

