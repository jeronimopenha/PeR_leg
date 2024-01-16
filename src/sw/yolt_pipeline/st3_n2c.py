from src.util.util import Util as U


class St3N2C(object):
    """
    This class is responsible give the 'a' node's cell and line and column.
    """

    def __init__(self, n2c: list[list[list]], n_cells_sqrt: int, latency: int):
        self.latency = latency
        # FIXME Guardar linha e coluna, não o número da célula
        self.n_cells_sqrt: int = n_cells_sqrt
        self.n2c: list[list[list]] = n2c
        self.th_dist_table_counter: list[int] = [0 for i in range(self.latency)]

        self.output_new: dict = {
            'th_idx': 0,
            'th_valid': False,
            'ia': 0,
            'ja': 0,
            'd_count': 0,
            'b': 0,
            'b_placed': False,
        }

        self.output: dict = self.output_new.copy()

    def execute(self, st2_input: dict, st5_input: dict):
        # Move forward the output
        self.output = self.output_new.copy()

        # return update
        st5_th_idx: int = st5_input['th_idx']
        st5_th_valid = st5_input['th_valid']
        st5_place: bool = st5_input['place']
        st5_d_count: int = st5_input['d_count']
        st5_ib: int = st5_input['ib']
        st5_jb: int = st5_input['jb']
        st5_b: int = st5_input['b']
        st5_b_placed: bool = st5_input['b_placed']
        if st5_place:
            self.n2c[st5_th_idx][st5_b][0] = st5_ib
            self.n2c[st5_th_idx][st5_b][1] = st5_jb
            self.th_dist_table_counter[st5_th_idx] = 0
        elif st5_th_valid and not st5_b_placed:
            self.th_dist_table_counter[st5_th_idx] = st5_d_count + 1

        # process the new output
        st2_th_idx: int = st2_input['th_idx']
        st2_th_valid: bool = st2_input['th_valid']
        st2_a: int = st2_input['a']
        st2_b: int = st2_input['b']

        # FIXME apenas para depuração
        if st2_th_idx == 0 and st2_th_valid:
            z = 1

        ia: int = self.n2c[st2_th_idx][st2_a][0] if self.n2c[st2_th_idx][st2_a][0] is not None else 0
        ja: int = self.n2c[st2_th_idx][st2_a][1] if self.n2c[st2_th_idx][st2_a][1] is not None else 0
        b_placed: bool = False if self.n2c[st2_th_idx][st2_b][1] is None else True
        d_count = self.th_dist_table_counter[st2_th_idx]

        self.output_new = {
            'th_idx': st2_th_idx,
            'th_valid': st2_th_valid,
            'ia': ia,
            'ja': ja,
            'd_count': d_count,
            'b': st2_b,
            'b_placed': b_placed,
        }
