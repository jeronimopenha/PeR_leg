class StageYOTO(object):
    """
    This class is responsible give the 'a' node's cell and line and column.
    """

    def __init__(self, n2c: list[list[list]], n_cells_sqrt: int, len_pipeline: int):
        self.len_pipeline = len_pipeline
        self.n_cells_sqrt: int = n_cells_sqrt
        self.n2c: list[list[list]] = n2c
        self.th_dist_table_counter: list[int] = [0 for i in range(self.len_pipeline)]

        self.new_output: dict = {
            'th_idx': 0,
            'th_valid': False,
            'ia': 0,
            'ja': 0,
            'dist_counter': 0,
            'b': 0,
        }

        self.old_output: dict = self.new_output.copy()

    def compute(self, st2_input: dict, st5_input: dict):
        # Move forward the output
        self.old_output = self.new_output.copy()

        # return update
        st5_th_idx: int = st5_input['th_idx']
        st5_th_valid = st5_input['th_valid']
        st5_place: bool = st5_input['place']
        st5_dist_counter: int = st5_input['dist_counter']
        st5_ib: int = st5_input['ib']
        st5_jb: int = st5_input['jb']
        st5_b: int = st5_input['b']
        if st5_place:
            self.n2c[st5_th_idx][st5_b][0] = st5_ib
            self.n2c[st5_th_idx][st5_b][1] = st5_jb
            self.th_dist_table_counter[st5_th_idx] = 0
        elif st5_th_valid:
            self.th_dist_table_counter[st5_th_idx] = st5_dist_counter + 1

        # process the new output
        st2_th_idx: int = st2_input['th_idx']
        st2_th_valid: bool = st2_input['th_valid']
        st2_a: int = st2_input['a']
        st2_b: int = st2_input['b']

        # FIXME for debugging BEGIN
        if st2_th_idx == 0 and st2_th_valid:
            z = 1
        # FIXME END

        ia: int = self.n2c[st2_th_idx][st2_a][0] if self.n2c[st2_th_idx][st2_a][0] is not None else 0
        ja: int = self.n2c[st2_th_idx][st2_a][1] if self.n2c[st2_th_idx][st2_a][1] is not None else 0
        dist_counter = self.th_dist_table_counter[st2_th_idx]

        self.new_output = {
            'th_idx': st2_th_idx,
            'th_valid': st2_th_valid,
            'ia': ia,
            'ja': ja,
            'dist_counter': dist_counter,
            'b': st2_b,
        }
