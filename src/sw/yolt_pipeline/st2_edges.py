class St2Edges(object):
    """
    This class is responsible give the edges for each thread.
    """

    def __init__(self, edges: list):
        #FIXME Uma lista de arestas para cada thread
        self.edges: list = edges

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

        a, b = self.edges[st1_edge_n]

        self.output_new = {
            'th_idx': st1_th_idx,
            'th_valid': st1_th_valid,
            'a': a,
            'b': b,
        }
