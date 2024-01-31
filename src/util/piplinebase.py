import random as rnd
from typing import Tuple

import numpy as np
from math import sqrt

from numpy import ndarray

from src.util.per_enum import ArchType
from src.util.per_graph import PeRGraph
from src.util.util import Util


class PiplineBase(object):

    def __init__(self, per_graph: PeRGraph, arch_type: ArchType, distance_table_bits: int, make_shuffle: bool,
                 len_pipeline: int, n_threads: int):
        """

        @param per_graph: 
        @type per_graph: 
        @param arch_type: 
        @type arch_type: 
        @param distance_table_bits: 
        @type distance_table_bits: 
        @param make_shuffle: 
        @type make_shuffle: 
        @param len_pipeline: 
        @type len_pipeline: 
        @param n_threads: 
        @type n_threads: 
        @param random_seed: 
        @type random_seed: 
        """
        self.len_pipeline: int = len_pipeline
        self.per_graph: PeRGraph = per_graph
        self.arch_type: ArchType = arch_type
        self.distance_table_bits: int = distance_table_bits
        self.make_shuffle: bool = make_shuffle
        self.n_threads: int = n_threads
        # self.reset_random(random_seed)

        self.cycle: list[list[list]] = []
        self.edges_raw: list[list[list]] = []
        self.edges_str: list[list[list]] = []
        for _ in range(self.len_pipeline):
            edges_str, edges_raw, cycle = self.per_graph.get_edges_zigzag(self.make_shuffle)
            self.cycle.append(cycle)
            self.edges_raw.append(edges_raw)
            self.edges_str.append(edges_str)

        self.edges_int: list[list[list]] = [self.get_edges_int(self.edges_str[i]) for i in range(self.len_pipeline)]
        self.annotations: list[dict] = [Util.get_graph_annotations(self.edges_raw[i], self.cycle[i]) for i in
                                        range(self.len_pipeline)]

        self.visited_edges = len(self.edges_int[0])
        self.total_edges = len(self.edges_raw[0])

        self.n_lines = self.per_graph.n_cells_sqrt
        self.n_columns = self.per_graph.n_cells_sqrt
        self.line_bits = int(sqrt(self.per_graph.n_cells))
        self.column_bits = self.line_bits

    @staticmethod
    def reset_random(random_seed: int = 0):
        """

        @param random_seed:
        @type random_seed:
        """
        rnd.seed(random_seed)

    def get_edges_int(self, edges_str: list[list]) -> list[list]:
        """

        @param edges_str:
        @type edges_str:
        @return:
        @rtype:
        """
        edges_int: list[list] = []
        for a, b in edges_str:
            edges_int.append(
                [
                    self.per_graph.nodes_to_idx[a],
                    self.per_graph.nodes_to_idx[b]
                ]
            )
        return edges_int

    def get_initial_position_traversal(self, first_node: int, len_pipeline: int = 5) -> list[list[list]]:
        """

        @param first_node:
        @type first_node:
        @param len_pipeline:
        @type len_pipeline:
        @return:
        @rtype:
        """
        n2c: list[list] = []
        c2n: list[list] = []
        for i in range(len_pipeline):
            n2c_tmp: list = [None for _ in range(self.per_graph.n_cells)]
            c2n_tmp: list = [None for _ in range(self.per_graph.n_cells)]
            idx: int = rnd.randint(0, self.per_graph.n_cells - 1)
            n2c_tmp[first_node] = idx
            c2n_tmp[idx] = first_node
            n2c.append(n2c_tmp)
            c2n.append(c2n_tmp)
        return [n2c, c2n]

    def init_placement_tables(self, first_node: list, len_pipeline: int = 5) -> tuple[list[list], list[list]]:
        n2c: list[list[list]] = []
        c2n: list[list] = []
        for i in range(len_pipeline):
            try:
                n2c_tmp: list[list] = [[None, None] for _ in range(self.per_graph.n_cells)]
                c2n_tmp: list[list] = [
                    [
                        None for _ in range(self.per_graph.n_cells_sqrt)
                    ] for _ in range(self.per_graph.n_cells_sqrt)
                ]

                idx_i, idx_j = Util.get_line_column_cell_sqrt(rnd.randint(0, self.per_graph.n_cells - 1),
                                                              self.per_graph.n_cells_sqrt)
                n2c_tmp[first_node[i]][0]: int = idx_i
                n2c_tmp[first_node[i]][1]: int = idx_j
                c2n_tmp[idx_i][idx_j]: int = first_node[i]
                n2c.append(n2c_tmp)
                c2n.append(c2n_tmp)
            except Exception as e:
                print(e)

        return n2c, c2n

    # FIXME
    '''
            Input:
                list_edge: edges list [[0,1],[1,2],...] 0 -> 1 e 1->2, ...
                GRID_SIZE: size of grid
                positions: dict with (i,j) indexes of a positioned node
                    Ex, if the node is in cell 0, so the position will be (0,0)
            Output:
                True: routed
                False: router error
    '''

    def routing_mesh(self, edges: list[list], positions: list[list]) -> tuple[bool, ndarray, dict]:
        """

        @param edges:
        @type edges:
        @param positions:
        @type positions:
        @return:
        @rtype:
        """
        n_cells: int = self.per_graph.n_cells
        n_cells_sqrt: int = self.per_graph.n_cells_sqrt
        grid = np.full((n_cells, 4, 1), -1, dtype=int)
        dic_path: dict = {}

        for j in range(0, len(edges)):
            a = int(edges[j][0])
            b = int(edges[j][1])
            key: str = '%d_%d' % (edges[j][0], edges[j][1])
            pos_a_i: int = positions[a][0]
            pos_a_j: int = positions[a][1]
            pos_b_i: int = positions[b][0]
            pos_b_j: int = positions[b][1]

            dic_path[key]: list = []
            dist_walk: int = -1

            dist_i, dist_j = abs(pos_b_i - pos_a_i), abs(pos_b_j - pos_a_j)

            pos_node_i, pos_node_j = pos_a_i, pos_a_j
            change: bool = False

            count_per_curr = []
            while dist_i != 0 or dist_j != 0:
                diff_i: int = pos_b_i - pos_node_i
                diff_j: int = pos_b_j - pos_node_j

                # get the current position node
                pe_curr: int = pos_node_i * n_cells_sqrt + pos_node_j
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
