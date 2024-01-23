import random as rnd
import numpy as np

from math import sqrt
from src.util.util import Util as U
from src.util.per_graph import PeRGraph


class Yoto(object):

    def __init__(self, per_graph: PeRGraph, n_threads: int = 1, random_seed: int = 0):
        self.len_pipeline: int = 6
        self.per_graph: PeRGraph = per_graph
        self.n_threads: int = n_threads
        self.reset_random(random_seed)

        self.edges_str: list[list] = self.per_graph.get_edges_zigzag()
        self.edges_int: list[list] = []
        for a, b in self.edges_str:
            self.edges_int.append(
                [
                    self.per_graph.nodes_to_idx[a],
                    self.per_graph.nodes_to_idx[b]
                ]
            )

        self.n_lines = self.per_graph.n_cells_sqrt
        self.n_columns = self.per_graph.n_cells_sqrt
        self.line_bits = int(sqrt(self.per_graph.n_cells))
        self.column_bits = self.line_bits

    @staticmethod
    def reset_random(random_seed: int = 0):
        rnd.seed(random_seed)

    def get_initial_position(self, first_node: int, len_pipeline: int = 5) -> tuple[list[list], list[list]]:
        n2c: list[list] = []
        c2n: list[list] = []
        for i in range(len_pipeline):
            n2c_tmp: list = [None for j in range(self.per_graph.n_cells)]
            c2n_tmp: list = [None for j in range(self.per_graph.n_cells)]
            idx: int = rnd.randint(0, self.per_graph.n_cells - 1)
            n2c_tmp[first_node] = idx
            c2n_tmp[idx] = first_node
            n2c.append(n2c_tmp)
            c2n.append(c2n_tmp)
        return n2c, c2n

    def get_initial_position_ij(self, first_node: int, len_pipeline: int = 5) -> tuple[list[list], list[list]]:
        n2c: list[list[list]] = []
        c2n: list[list] = []
        for i in range(len_pipeline):
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

    def routing_mesh(self, edges: list[list], positions: list[list]):
        '''
        Input:
            list_edge: lista de arestas [[0,1],[1,2],...] 0 -> 1 e 1->2, ...
            GRID_SIZE: tamanho do grid (considerei tamanho quadratico)
            positions: dicionario da posicao do nodo que retorna uma tupla de valores x e y do PE.
                Exemplo, se é o PE 0 então os valores de linha (i) e coluna (j) seriam 0 e 0, respectivamente
        Output:
            True: roteamento deu certo
            False: roteamento deu ruim

    '''

        n_cells = self.per_graph.n_cells
        n_cells_sqrt = self.per_graph.n_cells_sqrt
        # uma matriz que sera preenchida com os nodos
        grid = np.full((n_cells, 4, 1), -1, dtype=int)
        dic_path = {}

        for j in range(0, len(edges)):
            a = int(edges[j][0])
            b = int(edges[j][1])
            key = '%d_%d' % (edges[j][0], edges[j][1])
            pos_a_i = positions[a][0]
            pos_a_j = positions[a][1]
            pos_b_i = positions[b][0]
            pos_b_j = positions[b][1]

            dic_path[key] = []
            dist_walk = -1

            # diff_i, diff_j = pos_b_i - pos_a_i, pos_b_j - pos_a_j
            dist_i, dist_j = abs(pos_b_i - pos_a_i), abs(pos_b_j - pos_a_j)

            pos_node_i, pos_node_j = pos_a_i, pos_a_j
            change = False

            count_per_curr = []
            while dist_i != 0 or dist_j != 0:
                diff_i = pos_b_i - pos_node_i
                diff_j = pos_b_j - pos_node_j

                # get the current position node
                pe_curr = pos_node_i * n_cells_sqrt + pos_node_j
                dic_path[key].append(pe_curr)
                count_per_curr.append(pe_curr)

                # go to right neighbor
                # [pe], [0 = top, 1 = right, 2 = down, 3 = left], [0 = IN, OUT = 1]
                # go right
                if (diff_j > 0 and pe_curr + 1 < (pos_node_i + 1) * n_cells_sqrt and
                        (grid[pe_curr][1][0] == -1 or grid[pe_curr][1][0] == a) and
                        grid[pe_curr + 1][3][0] != a and (pe_curr + 1) not in count_per_curr):
                    grid[pe_curr][1][0] = a
                    pos_node_j += 1
                    change = True
                    # print("VIZ right 1")
                # go left
                elif (diff_j < 0 and pe_curr - 1 >= pos_node_i * n_cells_sqrt and
                      (grid[pe_curr][3][0] == -1 or grid[pe_curr][3][0] == a) and
                      grid[pe_curr - 1][1][0] != a and (pe_curr - 1) not in count_per_curr):
                    grid[pe_curr][3][0] = a
                    pos_node_j -= 1
                    change = True
                    # print("VIZ left 1")
                # go down
                elif (diff_i > 0 and pe_curr + n_cells_sqrt < n_cells and
                      (grid[pe_curr][2][0] == -1 or grid[pe_curr][2][0] == a) and
                      grid[pe_curr + n_cells_sqrt][0][0] != a and (pe_curr + n_cells_sqrt) not in count_per_curr):
                    grid[pe_curr][2][0] = a
                    pos_node_i += 1
                    change = True
                    # print("VIZ down 1")
                # go up
                elif (diff_i < 0 <= pe_curr - n_cells_sqrt and
                      (grid[pe_curr][0][0] == -1 or grid[pe_curr][0][0] == a) and
                      grid[pe_curr - n_cells_sqrt][2][0] != a and (pe_curr - n_cells_sqrt) not in count_per_curr):
                    grid[pe_curr][0][0] = a
                    pos_node_i -= 1
                    change = True
                    # print("VIZ top 1")

                if not change:  # change, try a long path

                    # go right
                    if (pe_curr + 1 < (pos_node_i + 1) * n_cells_sqrt and
                            (grid[pe_curr][1][0] == -1 or grid[pe_curr][1][0] == a) and
                            grid[pe_curr + 1][3][0] != a and (pe_curr + 1) not in count_per_curr):
                        grid[pe_curr][1][0] = a
                        pos_node_j += 1
                        change = True
                        # print("right 1")
                    # go left
                    elif (pe_curr - 1 >= pos_node_i * n_cells_sqrt and
                          (grid[pe_curr][3][0] == -1 or grid[pe_curr][3][0] == a) and
                          grid[pe_curr - 1][1][0] != a and (pe_curr - 1) not in count_per_curr):
                        grid[pe_curr][3][0] = a
                        pos_node_j -= 1
                        change = True
                        # print("left 1")
                    # go down
                    elif (pe_curr + n_cells_sqrt < n_cells and
                          (grid[pe_curr][2][0] == -1 or grid[pe_curr][2][0] == a) and
                          grid[pe_curr + n_cells_sqrt][0][0] != a and (pe_curr + n_cells_sqrt) not in count_per_curr):
                        grid[pe_curr][2][0] = a
                        pos_node_i += 1
                        change = True
                        # print("down 1")
                    elif (pe_curr - n_cells_sqrt >= 0 and
                          (grid[pe_curr][0][0] == -1 or grid[pe_curr][0][0] == a) and
                          grid[pe_curr - n_cells_sqrt][2][0] != a and
                          (pe_curr - n_cells_sqrt) not in count_per_curr):  # go up
                        grid[pe_curr][0][0] = a
                        pos_node_i -= 1
                        change = True
                        # print("top 1")

                    if not change:  # not routing
                        return False, grid, dic_path

                if not change:  # not routing
                    return False, grid, dic_path

                dist_i, dist_j = abs(pos_b_i - pos_node_i), abs(pos_b_j - pos_node_j)
                dist_walk += 1
                change = False

            if change:  # stop, give errors
                return False, grid, dic_path

            # pe_final = pos_node_i * n_cells_sqrt + pos_node_j
        return True, grid, dic_path
