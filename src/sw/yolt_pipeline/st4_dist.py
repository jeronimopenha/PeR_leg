from src.util.util import Util as U


class St4Dist(object):
    """
    This class is responsible give one possible neighbor cell of 'a'.
    """

    def __init__(self, n_cells_sqrt: int, latency: int):
        self.latency = latency
        self.n_cells_sqrt: int = n_cells_sqrt
        self.distance_table: list[list] = U.get_distance_table(self.n_cells_sqrt)
        self.th_dist_table_counter: list[int] = [0 for i in range(self.latency)]

        self.output_new: dict = {
            'th_idx': 0,
            'th_valid': False,
            'ib': 0,
            'jb': 0,
            'b': 0,
        }

        self.output: dict = self.output_new.copy()

    def execute(self, st3_input: dict, st4_input: dict, st5_input: dict):
        # Move forward the output
        self.output = self.output_new.copy()

        # return update
        st4_th_idx = st4_input['th_idx']
        st4_th_valid = st4_input['th_valid']
        st5_th_idx: int = st5_input['th_idx']
        st5_place: bool = st5_input['place']
        if st5_place:
            self.th_dist_table_counter[st5_th_idx] = 0
        elif st4_th_valid:
            self.th_dist_table_counter[st4_th_idx] += 1

        # process the new output
        st3_th_idx: int = st3_input['th_idx']
        st3_th_valid: bool = st3_input['th_valid']
        st3_ia: int = st3_input['ia']
        st3_ja: int = st3_input['ja']
        st3_b: int = st3_input['b']

        add_i, add_j = self.distance_table[self.th_dist_table_counter[st3_th_idx]]

        ib: int = st3_ia + add_i
        jb: int = st3_ja + add_j

        self.output_new = {
            'th_idx': st3_th_idx,
            'th_valid': st3_th_valid,
            'ib': ib,
            'jb': jb,
            'b': st3_b,
        }
