import random
import random as rnd
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

        self.reconvergence: list[list[list]] = []
        self.edges_raw: list[list[list]] = []
        self.edges_str: list[list[list]] = []
        for _ in range(self.len_pipeline):
            edges_str, edges_raw, rec = self.per_graph.get_edges_zigzag(self.make_shuffle)
            self.reconvergence.append(rec)
            self.edges_raw.append(edges_raw)
            self.edges_str.append(edges_str)

        self.edges_int: list[list[list]] = [self.get_edges_int(self.edges_str[i]) for i in range(self.len_pipeline)]
        self.verify_edges_len()

        self.annotations: list[dict] = [Util.get_graph_annotations(self.edges_raw[i], self.reconvergence[i]) for i in
                                        range(self.len_pipeline)]

        self.visited_edges = len(self.edges_int[0])
        self.total_edges = len(self.edges_raw[0])

        self.n_lines = self.per_graph.n_cells_sqrt
        self.n_columns = self.n_lines
        self.line_bits = int(sqrt(self.per_graph.n_cells))
        self.column_bits = self.line_bits

    def verify_edges_len(self):
        max_len = max([len(edges) for edges in self.edges_int])
        for edge in self.edges_int:
            len_ = len(edge)
            if len_ < max_len:
                for _ in range(max_len - len_):
                    edge.append([-1, -1])

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
        for (a, b) in edges_str:
            edges_int.append(
                [
                    self.per_graph.nodes_to_idx[a],
                    self.per_graph.nodes_to_idx[b]
                ]
            )
        return edges_int

    def init_sa_placement_tables(self) -> tuple[list[list], list[list]]:
        """

        @return:
        """
        n2c: list[list] = []
        c2n: list[list] = []
        for i in range(self.n_threads):
            n2c_tmp: list = [-1 for _ in range(self.n_lines * self.n_columns)]
            c2n_tmp: list = [-1 for _ in range(self.n_lines * self.n_columns)]

            nodes = self.per_graph.nodes.copy()
            cells = [i for i in range(self.n_lines * self.n_columns)]
            random.shuffle(nodes)
            random.shuffle(cells)

            while nodes:
                random_node = nodes[0]
                random_cell = cells[0]
                nodes.pop(0)
                cells.pop(0)

                c2n_tmp[random_cell] = self.per_graph.nodes_to_idx[random_node]
                n2c_tmp[c2n_tmp[random_cell]] = random_cell

            n2c.append(n2c_tmp)
            c2n.append(c2n_tmp)
        return n2c, c2n

    def init_traversal_placement_tables(self, first_node: list) -> tuple[list[list], list[list]]:
        n2c: list[list[list]] = []
        c2n: list[list] = []
        for i in range(self.len_pipeline):
            n2c_tmp: list[list] = [[None, None] for _ in range(self.per_graph.n_cells)]
            c2n_tmp: list[list] = [
                [
                    None for _ in range(self.n_lines)
                ] for _ in range(self.n_lines)
            ]

            idx_i, idx_j = Util.get_line_column_cell_sqrt(rnd.randint(0, self.per_graph.n_cells - 1), self.n_lines)
            n2c_tmp[first_node[i]][0]: int = idx_i
            n2c_tmp[first_node[i]][1]: int = idx_j
            c2n_tmp[idx_i][idx_j]: int = first_node[i]
            n2c.append(n2c_tmp)
            c2n.append(c2n_tmp)

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
        n_cells_sqrt: int = self.n_lines
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
