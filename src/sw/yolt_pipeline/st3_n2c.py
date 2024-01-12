from src.util.util import Util as U


class St3N2C(object):
    """
    This class is responsible give the 'a' node's cell and line and column.
    """

    def __init__(self, n2c: list[list], n_cells_sqrt: int):
        self.n2c: list[list] = n2c
        self.n_cells_sqrt: int = n_cells_sqrt

        self.output_new: dict = {
            'th_idx': 0,
            'th_valid': False,
            'ca': 0,
            'ia': 0,
            'ja': 0,
            'b': 0,
        }

        self.output: dict = self.output_new.copy()

    def execute(self, st_input: dict):
        # Move forward the output
        self.output = self.output_new.copy()

        # process the new output
        th_idx: int = st_input['th_idx']
        th_valid: bool = st_input['th_valid']
        a: int = st_input['a']
        b: int = st_input['b']
        ca: int = self.n2c[th_idx][a] if self.n2c[th_idx][a] is not None else 0

        ia, ja = U.get_line_column_cell_sqrt(ca, self.n_cells_sqrt)

        # TODO
        # return increment

        self.output_new = {
            'th_idx': th_idx,
            'th_valid': th_valid,
            'ca': ca,
            'ia': ia,
            'ja': ja,
            'b': b,
        }
