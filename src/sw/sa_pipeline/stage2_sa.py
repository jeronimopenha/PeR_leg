class Stage2SA:
    """
    Second Pipe from SA_Verilog. This pipe is responsible to bring the neighbor from each node selected in the left
    pipe in the graph.
    """

    def __init__(self, neighbors: dict):
        """

        @param neighbors:
        """
        self.neighbors: dict = neighbors
        self.new_output: dict = {
            'th_idx': 0,
            'th_valid': False,
            'cell_a': 0,
            'cell_b': 0,
            'node_a': 0,
            'node_b': 0,
            'va': [None, None, None, None],
            'vb': [None, None, None, None],
            'sw': {'th_idx': 0, 'th_valid': False, 'sw': False},
            'wa': {'th_idx': 0, 'cell': 0, 'node': None},
            'wb': {'th_idx': 0, 'cell': 0, 'node': None},
        }
        self.old_output: dict = self.new_output.copy()

    def compute(self, st1_input: dict):
        """

        @param st1_input:
        """
        # moving forward the ready outputs
        self.old_output = self.new_output.copy()

        st1_th_idx: int = st1_input['th_idx']
        st1_th_valid: bool = st1_input['th_valid']
        st1_cell_a: int = st1_input['cell_a']
        st1_cell_b: int = st1_input['cell_b']
        st1_node_a: int = st1_input['node_a']
        st1_node_b: int = st1_input['node_b']
        st1_sw: list = st1_input['sw']
        st1_wa: list = st1_input['wa']
        st1_wb: list = st1_input['wb']

        # fixme only for debugging
        if st1_th_idx == 0:
            z = 1

        va: list = [None, None, None, None]
        vb: list = [None, None, None, None]

        if st1_node_a is not None:
            for i in range(len(self.neighbors[st1_node_a])):
                va[i] = self.neighbors[st1_node_a][i]
        if st1_node_b is not None:
            for i in range(len(self.neighbors[st1_node_b])):
                vb[i] = self.neighbors[st1_node_b][i]

        # reading pipe inputs
        self.new_output = {
            'th_idx': st1_th_idx,
            'th_valid': st1_th_valid,
            'cell_a': st1_cell_a,
            'cell_b': st1_cell_b,
            'node_a': st1_node_a,
            'node_b': st1_node_b,
            'va': va,
            'vb': vb,
            'sw': st1_sw,
            'wa': st1_wa,
            'wb': st1_wb
        }
