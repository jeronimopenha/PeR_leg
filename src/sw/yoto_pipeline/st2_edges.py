class St2Edges(object):
    """
    This class is responsible give the edges for each thread.
    """

    def __init__(self, edges: list, latency: int, n_edges):
        self.edges: list[list] = [edges for i in range(latency)]
        self.n_edges: int = n_edges

        self.output_new: dict = {
            'th_idx': 0,
            'th_valid': False,
            'a': 0,
            'b': 0,
        }

        self.output: dict = self.output_new.copy()

    def execute(self, st1_input: dict):
        # Move forward the output
        self.output = self.output_new.copy()

        # process the new output
        st1_th_idx: int = st1_input['th_idx']
        st1_th_valid: bool = st1_input['th_valid']
        st1_edge_n: int = st1_input['edg_n']

        # FIXME apenas para depuração
        if st1_th_idx == 0 and st1_th_valid:
            z = 1

        edge_n_valid = st1_edge_n < self.n_edges

        a, b = self.edges[st1_th_idx][st1_edge_n] if edge_n_valid else (0, 0)

        self.output_new = {
            'th_idx': st1_th_idx,
            'th_valid': st1_th_valid and edge_n_valid,
            'a': a,
            'b': b,
        }
