from src.util.per_enum import ArchType
from src.util.util import get_distance_table


class Stage4YOTO(object):
    """
    This class is responsible give one possible neighbor cell of 'a'.
    """

    def __init__(self, arch_type: ArchType, n_cells_sqrt: int, distance_table_bits: int, make_shuffle: bool):
        self.arch_type = arch_type
        self.n_cells_sqrt: int = n_cells_sqrt
        self.distance_table_bits: int = distance_table_bits
        self.n_distance_tables = pow(2, self.distance_table_bits)
        self.make_shuffle = make_shuffle
        self.distance_table: list[list[list]] = [
            get_distance_table(self.arch_type, self.n_cells_sqrt, self.make_shuffle) for _ in
            range(self.n_distance_tables)]

        self.new_output: dict = {
            'th_idx': 0,
            'th_valid': False,
            'ib': 0,
            'jb': 0,
            'dist_counter': 0,
            'b': 0,
        }

        self.old_output: dict = self.new_output.copy()

    def compute(self, st3_input: dict):
        # Move forward the output
        self.old_output = self.new_output.copy()

        # process the new output
        st3_th_idx: int = st3_input['th_idx']
        st3_th_valid: bool = st3_input['th_valid']
        st3_ia: int = st3_input['ia']
        st3_ja: int = st3_input['ja']
        st3_dist_table_num: int = st3_input['dist_table_num']
        st3_dist_counter: int = st3_input['dist_counter']
        st3_b: int = st3_input['b']

        # FIXME for debugging BEGIN
        if st3_th_idx == 0 and st3_th_valid:
            z = 1
        # FIXME END

        add_i, add_j = self.distance_table[st3_dist_table_num][st3_dist_counter]

        ib: int = st3_ia + add_i
        jb: int = st3_ja + add_j

        self.new_output = {
            'th_idx': st3_th_idx,
            'th_valid': st3_th_valid,
            'ib': ib,
            'jb': jb,
            'dist_counter': st3_dist_counter,
            'b': st3_b,
        }
