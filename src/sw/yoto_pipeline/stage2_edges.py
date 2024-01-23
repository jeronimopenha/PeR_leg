class Stage2YOTO(object):
    """
    This class is responsible give the edges for each thread.
    """

    def __init__(self, edges: list, len_pipeline: int, n_edges):
        self.edges: list[list] = [edges for i in range(len_pipeline)]
        self.n_edges: int = n_edges

        self.new_output: dict = {
            'th_idx': 0,
            'th_valid': False,
            'a': 0,
            'b': 0,
        }

        self.old_output: dict = self.new_output.copy()

    def compute(self, st1_input: dict):
        # Move forward the output
        self.old_output = self.new_output.copy()

        # process the new output
        st1_th_idx: int = st1_input['th_idx']
        st1_th_valid: bool = st1_input['th_valid']
        st1_edge_n: int = st1_input['edg_n']

        # FIXME for debugging BEGIN
        if st1_th_idx == 0 and st1_th_valid:
            z = 1
        # FIXME END

        edge_n_valid = st1_edge_n < self.n_edges

        a, b = self.edges[st1_th_idx][st1_edge_n] if edge_n_valid else (0, 0)

        self.new_output = {
            'th_idx': st1_th_idx,
            'th_valid': st1_th_valid and edge_n_valid,
            'a': a,
            'b': b,
        }
