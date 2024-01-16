from src.util.util import Util as U


class St4Dist(object):
    """
    This class is responsible give one possible neighbor cell of 'a'.
    """

    def __init__(self, n_cells_sqrt: int):
        self.n_cells_sqrt: int = n_cells_sqrt
        self.distance_table: list[list] = U.get_distance_table(self.n_cells_sqrt)

        self.output_new: dict = {
            'th_idx': 0,
            'th_valid': False,
            'ib': 0,
            'jb': 0,
            'd_count': 0,
            'b': 0,
            'b_placed': False,
        }

        self.output: dict = self.output_new.copy()

    def execute(self, st3_input: dict, st4_input: dict):
        # Move forward the output
        self.output = self.output_new.copy()

        # process the new output
        st3_th_idx: int = st3_input['th_idx']
        st3_th_valid: bool = st3_input['th_valid']
        st3_ia: int = st3_input['ia']
        st3_ja: int = st3_input['ja']
        st3_d_count: int = st3_input['d_count']
        st3_b: int = st3_input['b']
        st3_b_placed: bool = st3_input['b_placed']

        # FIXME apenas para depuração
        if st3_th_idx == 0 and st3_th_valid:
            z = 1

        add_i, add_j = self.distance_table[st3_d_count]

        ib: int = st3_ia + add_i
        jb: int = st3_ja + add_j

        self.output_new = {
            'th_idx': st3_th_idx,
            'th_valid': st3_th_valid,
            'ib': ib,
            'jb': jb,
            'd_count': st3_d_count,
            'b': st3_b,
            'b_placed': st3_b_placed,
        }
