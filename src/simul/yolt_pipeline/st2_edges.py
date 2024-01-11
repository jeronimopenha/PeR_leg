class St2Edges(object):
    """
    This class is responsible give the edges for each thread.
    """

    def __init__(self, edges: list, latency: int = 5):
        self.latency: int = latency
        self.edges: list = edges

        self.output_new = {
            'th_idx': 0,
            'th_valid': False,
            'a': 0,
            'b': 0,
        }

        self.output = self.output_new.copy()

    def execute(self, st_input: dict):
        # Move forward the output
        self.output = self.output_new.copy()

        # process the new output
        th_idx: int = st_input['th_idx']
        th_valid: bool = st_input['th_valid']
        edge_n: int = st_input['edge_n']
        a, b = self.edges[edge_n]

        self.output_new = {
            'th_idx': th_idx,
            'th_valid': th_valid,
            'a': a,
            'b': b,
        }
