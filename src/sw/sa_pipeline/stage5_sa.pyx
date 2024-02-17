from src.util.util import Util
from src.util.per_enum import ArchType
import cython


@cython.boundscheck(False)
@cython.wraparound(False)
class Stage5SA:
    """
    Fifth Pipe from SA_Verilog. This pipe is responsible for finding the manhandle
    distances for each combination between cellA and cellB with their respective
    neighbor cells after a swap and executing the first 2-2 additions for the
    distances found in the left pipe.
    """

    def __init__(self, arch_type: ArchType, n_lines: cython.int, n_columns: cython.int):
        """
        Initialize Stage5SA.

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
            'dvac': [0, 0],
            'dvbc': [0, 0],
            'dvas': [0, 0, 0, 0],
            'dvbs': [0, 0, 0, 0]
        }
        self.old_output: dict = self.new_output.copy()

    def compute(self, st4_input: dict):
        """
        Compute method for Stage5SA.

        Args:
            st4_input (dict): The input dictionary.
        """
        self.old_output = self.new_output.copy()

        st4_th_idx: cython.int = st4_input['th_idx']
        st4_th_valid: cython.bint = st4_input['th_valid']
        st4_cbs: cython.int = st4_input['cell_a']
        st4_cas: cython.int = st4_input['cell_b']
        st4_cva: list[cython.int] = st4_input['cva']
        st4_cvb: list[cython.int] = st4_input['cvb']
        st4_dvac: list[cython.int] = st4_input['dvac']
        st4_dvbc: list[cython.int] = st4_input['dvbc']

        dvac: list[cython.int] = self.compute_distances(st4_cas, st4_cbs, st4_cva, st4_dvac)
        dvbc: list[cython.int] = self.compute_distances(st4_cbs, st4_cas, st4_cvb, st4_dvbc)
        dvas: list[cython.int] = self.compute_dvas(st4_cas, st4_cbs, st4_cva)
        dvbs: list[cython.int] = self.compute_dvas(st4_cbs, st4_cas, st4_cvb)

        self.new_output: dict = {
            'th_idx': st4_th_idx,
            'th_valid': st4_th_valid,
            'dvac': dvac,
            'dvbc': dvbc,
            'dvas': dvas,
            'dvbs': dvbs
        }

    def compute_distances(self, src_cell: cython.int, dest_cell: cython.int, neighbors: list[cython.int],
                          deltas: list[cython.int]) -> list[cython.int]:
        """
        Compute distances between source and destination cells.

        Args:
            src_cell (cython.int): Source cell index.
            dest_cell (cython.int): Destination cell index.
            neighbors (list[cython.int]): List of neighbor cell indices.
            deltas (list[cython.int]): List of deltas.

        Returns:
            list[cython.int]: List of computed distances.
        """
        distances: list[cython.int] = []
        for i in range(len(neighbors)):
            if neighbors[i] != -1:
                if self.arch_type == ArchType.ONE_HOP:
                    distances.append(Util.dist_one_hop(
                        Util.get_line_column_from_cell(src_cell, self.n_lines, self.n_columns),
                        Util.get_line_column_from_cell(dest_cell, self.n_lines, self.n_columns)
                    ) if src_cell == neighbors[i] else Util.dist_one_hop(
                        Util.get_line_column_from_cell(src_cell, self.n_lines, self.n_columns),
                        Util.get_line_column_from_cell(neighbors[i], self.n_lines, self.n_columns)
                    ))
                elif self.arch_type == ArchType.MESH:
                    distances.append(Util.dist_manhattan(
                        Util.get_line_column_from_cell(src_cell, self.n_lines, self.n_columns),
                        Util.get_line_column_from_cell(dest_cell, self.n_lines, self.n_columns)
                    ) if src_cell == neighbors[i] else Util.dist_manhattan(
                        Util.get_line_column_from_cell(src_cell, self.n_lines, self.n_columns),
                        Util.get_line_column_from_cell(neighbors[i], self.n_lines, self.n_columns)
                    ))
        return distances

    def compute_dvas(self, src_cell: cython.int, dest_cell: cython.int, neighbors: list[cython.int]) -> list[cython.int]:
        """
        Compute dvas.

        Args:
            src_cell (cython.int): Source cell index.
            dest_cell (cython.int): Destination cell index.
            neighbors (list[cython.int]): List of neighbor cell indices.

        Returns:
            list[cython.int]: List of computed dvas.
        """
        dvas: list[cython.int] = []
        for neighbor in neighbors:
            if neighbor != -1:
                if self.arch_type == ArchType.ONE_HOP:
                    dvas.append(Util.dist_one_hop(
                        Util.get_line_column_from_cell(src_cell, self.n_lines, self.n_columns),
                        Util.get_line_column_from_cell(dest_cell, self.n_lines, self.n_columns)
                    ) if src_cell == neighbor else Util.dist_one_hop(
                        Util.get_line_column_from_cell(src_cell, self.n_lines, self.n_columns),
                        Util.get_line_column_from_cell(neighbor, self.n_lines, self.n_columns)
                    ))
                elif self.arch_type == ArchType.MESH:
                    dvas.append(Util.dist_manhattan(
                        Util.get_line_column_from_cell(src_cell, self.n_lines, self.n_columns),
                        Util.get_line_column_from_cell(dest_cell, self.n_lines, self.n_columns)
                    ) if src_cell == neighbor else Util.dist_manhattan(
                        Util.get_line_column_from_cell(src_cell, self.n_lines, self.n_columns),
                        Util.get_line_column_from_cell(neighbor, self.n_lines, self.n_columns)
                    ))
        return dvas
