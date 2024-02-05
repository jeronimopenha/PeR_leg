from src.util.per_enum import ArchType
from src.util.util import Util


class Stage4SA:
    """
    Fourth Pipe from SA_Verilog. This pipe is responsible to find the manhandle
    distances for each combination between cellA and cellB with their 
    respective neighbors cells before swap.
    """

    def __init__(self, arch_type: ArchType, n_lines: int, n_columns: int):
        """
        @param n_lines:
        @param n_columns:

        """
        self.arch_type: ArchType = arch_type
        self.n_lines: int = n_lines
        self.n_columns: int = n_columns
        self.new_output: dict = {
            'th_idx': 0,
            'th_valid': False,
            'cell_a': 0,
            'cell_b': 0,
            'cva': [None, None, None, None],
            'cvb': [None, None, None, None],
            'dvac': [0, 0, 0, 0],
            'dvbc': [0, 0, 0, 0]
        }
        self.old_output: dict = self.new_output.copy()

    def compute(self, st3_input: dict):
        """

        @param st3_input:
        """
        # moving forward the ready outputs
        self.old_output = self.new_output.copy()

        st3_th_idx: int = st3_input['th_idx']
        st3_th_valid: bool = st3_input['th_valid']
        st3_cell_a: int = st3_input['cell_a']
        st3_cell_b: int = st3_input['cell_b']
        st3_cva: list = st3_input['cva']
        st3_cvb: list = st3_input['cvb']

        # fixme only for debugging
        if st3_th_idx == 0:
            z = 1

        dvac = [0, 0, 0, 0]
        dvbc = [0, 0, 0, 0]

        ca = st3_input['cell_a']
        cb = st3_input['cell_b']
        cva = st3_input['cva']
        cvb = st3_input['cvb']

        for i in range(len(cva)):
            if cva[i] is not None:
                if self.arch_type == ArchType.ONE_HOP:
                    dvac[i] = Util.dist_one_hop(
                        Util.get_line_column_from_cell(ca, self.n_lines, self.n_columns),
                        Util.get_line_column_from_cell(cva[i], self.n_lines, self.n_columns)
                    )
                elif self.arch_type == ArchType.MESH:
                    dvac[i] = Util.dist_manhattan(
                        Util.get_line_column_from_cell(ca, self.n_lines, self.n_columns),
                        Util.get_line_column_from_cell(cva[i], self.n_lines, self.n_columns)
                    )

        for i in range(len(cvb)):
            if cvb[i] is not None:
                if self.arch_type == ArchType.ONE_HOP:
                    dvbc[i] = Util.dist_one_hop(
                        Util.get_line_column_from_cell(cb, self.n_lines, self.n_columns),
                        Util.get_line_column_from_cell(cvb[i], self.n_lines, self.n_columns)
                    )
                elif self.arch_type == ArchType.MESH:
                    dvbc[i] = Util.dist_manhattan(
                        Util.get_line_column_from_cell(cb, self.n_lines, self.n_columns),
                        Util.get_line_column_from_cell(cvb[i], self.n_lines, self.n_columns)
                    )

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
