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

    def execute(self, st_input: dict):
        # Move forward the output
        self.output = self.output_new.copy()

        # process the new output
        th_idx: int = st_input['th_idx']
        th_valid: bool = st_input['th_valid']
        ia: int = st_input['ia']
        ja: int = st_input['ja']
        b: int = st_input['b']
        add_i, add_j = self.distance_table[self.th_dist_table_counter[th_idx]]

        ib: int = ia + add_i
        jb: int = ja + add_j

        # TODO
        # return increment

        self.output_new = {
            'th_idx': th_idx,
            'th_valid': th_valid,
            'ib': ib,
            'jb': jb,
            'b': b,
        }
