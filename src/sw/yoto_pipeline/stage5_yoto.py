from src.util.util import Util as U


class Stage5YOTO(object):
    """
    This class is responsible decide if the 'b' can b placed in the proposed cell
    and send to other stages the update signal
    """

    def __init__(self, c2n: list[list[list]], n_cells_sqrt: int):
        self.n_cells_sqrt: int = n_cells_sqrt
        self.c2n: list[list[list]] = c2n

        self.new_output: dict = {
            'th_idx': 0,
            'th_valid': False,
            'place': False,
            'dist_counter': 0,
            'b': 0,
            'ib': 0,
            'jb': 0,
        }

        self.old_output: dict = self.new_output.copy()

    def compute(self, st4_input: dict, st5_input: dict):
        # Move forward the output
        self.old_output = self.new_output.copy()

        # return update
        st5_th_idx: int = st5_input['th_idx']
        st5_place: bool = st5_input['place']
        st5_ib: int = st5_input['ib']
        st5_jb: int = st5_input['jb']
        st5_b: int = st5_input['b']
        if st5_place:
            self.c2n[st5_th_idx][st5_ib][st5_jb] = st5_b
            # for l in self.c2n[st5_th_idx]:
            # print(l)pass
            # print()

        # process the new output
        st4_th_idx: int = st4_input['th_idx']
        st4_th_valid: bool = st4_input['th_valid']
        st4_ib: int = st4_input['ib']
        st4_jb: int = st4_input['jb']
        st4_dist_counter: int = st4_input['dist_counter']
        st4_b: int = st4_input['b']

        # FIXME for debugging BEGIN
        if st4_th_idx == 0 and st4_th_valid:
            z = 1
        # FIXME END

        place: bool = False

        out_of_border: U.is_out_of_border_sqr(st4_ib, st4_jb, self.n_cells_sqrt)

        cb_content = 0 if out_of_border else self.c2n[st4_th_idx][st4_ib][st4_jb]

        if st4_th_valid and cb_content is None and not out_of_border:
            place = True

        self.new_output = {
            'th_idx': st4_th_idx,
            'th_valid': st4_th_valid,
            'place': place,
            'dist_counter': st4_dist_counter,
            'b': st4_b,
            'ib': st4_ib,
            'jb': st4_jb,
        }
