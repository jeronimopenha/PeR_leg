import random
from src.py.graph.graph import Graph
from src.py.per.base.per import PeR, EdgesAlgEnum
from typing import List, Tuple


class FPGAPeR(PeR):
    def __init__(self, graph: Graph):
        super().__init__()
        random.seed(0)
        self.graph = graph

    def per_sa(self):
        pass

    def per_yoto(self, n_exec: int = 1, edges_alg: EdgesAlgEnum = EdgesAlgEnum.ZIG_ZAG):
        # Final placements
        placements = []

        # I will initialize the vector with the possible positions for inputs and outputs
        possible_pos_in, possible_pos_out = self.get_in_out_pos()

        # starting executions

        for exec in range(n_exec):
            # First I will start the placement of matrix
            placement = [None for _ in range(self.graph.n_cells)]

            # possible distances to find free cells
            distances_cells = self.graph.get_mesh_distances()

            # Creating the n2c matrix
            n2c = [None for _ in range(self.graph.n_cells)]

            # And then I need to draw the input and output positions
            # They will be randomly placed and the inputs can be on top and left
            # while outputs can be on bottom and right.
            i = 0
            while i < max(len(self.graph.input_nodes), len(self.graph.output_nodes)):
                if i < len(self.graph.input_nodes):
                    n = self.graph.nodes_to_idx[self.graph.input_nodes[i]]
                    ch = self.choose_position(placement, n, possible_pos_in)
                    n2c[n] = ch
                    placement[ch] = n
                if i < len(self.graph.output_nodes):
                    n = self.graph.nodes_to_idx[self.graph.output_nodes[i]]
                    ch = self.choose_position(placement, n, possible_pos_out)
                    n2c[n] = ch
                    placement[ch] = n
                i += 1
            # now, I will start the yoto algorithm.

            # Getting the adges to be placed
            ed_str = []
            if edges_alg == EdgesAlgEnum.ZIG_ZAG:
                ed_str = self.graph.get_edges_zigzag()[0]
            else:
                ed_str = self.graph.get_edges_depth_first()
            ed = self.graph.get_edges_idx(ed_str)

            # if the node that it wants to place is placed, then it will go to next edge

            for e in ed:
                a = e[0]
                b = e[1]
                if n2c[b] is not None:
                    continue
                ai = n2c[a] // self.graph.n_cells_sqrt
                aj = n2c[a] % self.graph.n_cells_sqrt
                # while not find a clear cell, I will try to find one
                distance = 1
                for line in distances_cells:
                    placed = False
                    for ij in line:
                        bi = ai + ij[0]
                        bj = aj + ij[1]
                        if (bi < 0 or bi > self.graph.n_cells_sqrt - 1 or
                                bj < 0 or bj > self.graph.n_cells_sqrt - 1):
                            continue
                        ch = bi * self.graph.n_cells_sqrt + bj
                        if placement[ch] is None:
                            placement[ch] = b
                            n2c[b] = ch
                            placed = True
                            break
                    if placed:
                        break

                a = 1
        # TODO Fazer o relatório e os cálculos de distancias, gerar dot.
        pass

    def choose_position(self, placement, node, choices):
        while True:
            ch = random.choice(choices)
            if placement[ch] is not None:
                continue
            return ch

    def get_in_out_pos(self):
        in_ = []
        out_ = []
        for i in range(self.graph.n_cells_sqrt):
            in_.append(i)
            out_.append(i + self.graph.n_cells - self.graph.n_cells_sqrt)
        for i in range(self.graph.n_cells_sqrt, self.graph.n_cells, self.graph.n_cells_sqrt):
            in_.append(i)
        for i in range(self.graph.n_cells_sqrt - 1, self.graph.n_cells - 1, self.graph.n_cells_sqrt):
            out_.append(i)
        return in_, out_

    def per_yott(self):
        pass
