from src.util.util import Util as U


class St3N2C(object):
    """
    This class is responsible give the 'a' node's cell and line and column.
    """

    def __init__(self, n2c: list[list], n_cells_sqrt: int):
        # FIXME Guardar linha e coluna, não o número da célula
        self.n2c: list[list] = n2c
        self.n_cells_sqrt: int = n_cells_sqrt

        self.output_new: dict = {
            'th_idx': 0,
            'th_valid': False,
            'ia': 0,
            'ja': 0,
            'b': 0,
        }

        self.output: dict = self.output_new.copy()

    def execute(self, st2_input: dict, st5_input: dict):
        # Move forward the output
        self.output = self.output_new.copy()

        # return update
        st5_th_idx: int = st5_input['th_idx']
        st5_place: bool = st5_input['place']
        st5_cb: int = st5_input['cb']
        st5_b: int = st5_input['b']
        if st5_place:
            self.n2c[st5_th_idx][st5_b] = st5_cb

        # process the new output
        st2_th_idx: int = st2_input['th_idx']
        st2_th_valid: bool = st2_input['th_valid']
        st2_a: int = st2_input['a']
        st2_b: int = st2_input['b']

        ca: int = self.n2c[st2_th_idx][st2_a] if self.n2c[st2_th_idx][st2_a] is not None else 0

        # fixme sumir com essa linha
        ia, ja = U.get_line_column_cell_sqrt(ca, self.n_cells_sqrt)

        self.output_new = {
            'th_idx': st2_th_idx,
            'th_valid': st2_th_valid,
            'ia': ia,
            'ja': ja,
            'b': st2_b,
        }
