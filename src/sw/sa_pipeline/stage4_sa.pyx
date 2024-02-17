from src.util.per_enum import ArchType
from src.util.util import Util
import cython


@cython.boundscheck(False)
@cython.wraparound(False)
class Stage4SA:
    """
    Fourth Pipe from SA_Verilog. This pipe is responsible for finding the manhandle
    distances for each combination between cellA and cellB with their respective
    neighbor cells before swap.
    """

    def __init__(self, arch_type: ArchType, n_lines: cython.int, n_columns: cython.int):
        """
        Initializes Stage4SA.

        Args:
            arch_type (ArchType): The architecture type.
            n_lines (cython.int): The number of lines.
            n_columns (cython.int): The number of columns.
        """
        self.arch_type: ArchType = arch_type
        self.n_lines: cython.int = n_lines
        self.n_columns: cython.int = n_columns
        self.new_output: dict = {
            'th_idx': 0,
            'th_valid': False,
            'cell_a': 0,
            'cell_b': 0,
            'cva': [-1, -1, -1, -1],
            'cvb': [-1, -1, -1, -1],
            'dvac': [0, 0, 0, 0],
            'dvbc': [0, 0, 0, 0]
        }
        self.old_output: dict = self.new_output.copy()

    def compute(self, st3_input: dict):
        """
        Computes distances between cellA and cellB and their respective neighbor cells.

        Args:
            st3_input (dict): The input dictionary containing 'th_idx', 'th_valid', 'cell_a', 'cell_b',
                              'cva', and 'cvb'.
        """
        # moving forward the ready outputs
        self.old_output = self.new_output.copy()

        st3_th_idx: cython.int = st3_input['th_idx']
        st3_th_valid: cython.bint = st3_input['th_valid']
        st3_cell_a: cython.int = st3_input['cell_a']
        st3_cell_b: cython.int = st3_input['cell_b']
        st3_cva: list[cython.int] = st3_input['cva']
        st3_cvb: list[cython.int] = st3_input['cvb']

        dvac: list[cython.int] = [0, 0, 0, 0]
        dvbc: list[cython.int] = [0, 0, 0, 0]

        # Compute distances for cellA
        self.compute_distances(st3_cell_a, st3_cva, dvac)

        # Compute distances for cellB
        self.compute_distances(st3_cell_b, st3_cvb, dvbc)

        self.new_output: dict = {
            'th_idx': st3_th_idx,
            'th_valid': st3_th_valid,
            'cell_a': st3_cell_a,
            'cell_b': st3_cell_b,
            'cva': st3_cva,
            'cvb': st3_cvb,
            'dvac': dvac,
            'dvbc': dvbc
        }

    def compute_distances(self, cell: cython.int, neighbors: list[cython.int], distances: list[cython.int]):
        """
        Computes distances between a cell and its neighbor cells.

        Args:
            cell (cython.int): The index of the cell.
            neighbors (list[cython.int]): The list of neighbor cell indices.
            distances (list[cython.int]): The list to store computed distances.
        """
        for i in range(len(neighbors)):
            if neighbors[i] != -1:
                if self.arch_type == ArchType.ONE_HOP:
                    distances[i] = Util.dist_one_hop(
                        Util.get_line_column_from_cell(cell, self.n_lines, self.n_columns),
                        Util.get_line_column_from_cell(neighbors[i], self.n_lines, self.n_columns)
                    )
                elif self.arch_type == ArchType.MESH:
                    distances[i] = Util.dist_manhattan(
                        Util.get_line_column_from_cell(cell, self.n_lines, self.n_columns),
                        Util.get_line_column_from_cell(neighbors[i], self.n_lines, self.n_columns)
                    )
