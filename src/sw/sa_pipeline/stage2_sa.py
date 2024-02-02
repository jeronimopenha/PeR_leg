import src.hw.sa_pipeline.util as _u


class Stage2SA:
    """
    Second Pipe from SA_Verilog. This pipe is responsible to bring the neighboor from each node selected in the left pipe in the graph.
    """

    def __init__(self, neighbors: dict):
        self.neighbors = neighbors
        self.new_output = {
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
        self.old_output = self.new_output.copy()

    def compute(self, _in: dict):
        # moving forward the ready outputs
        self.old_output = self.new_output.copy()

        th_idx
        th_valid
        cell_a
        cell_b
        node_a
        node_b

        # reading pipe inputs
        self.new_output = {
            'th_idx': _in['th_idx'],
            'th_valid': _in['th_valid'],
            'cell_a': _in['cell_a'],
            'cell_b': _in['cell_b'],
            'node_a': _in['node_a'],
            'node_b': _in['node_b'],
            'va': [None, None, None, None],
            'vb': [None, None, None, None],
            'sw': _in['sw'],
            'wa': _in['wa'],
            'wb': _in['wb']
        }

        na = _in['na']
        nb = _in['nb']
        if na is not None:
            for i in range(len(self.neighbors[na])):
                self.new_output['va'][i] = self.neighbors[na][i]
        if nb is not None:
            for i in range(len(self.neighbors[nb])):
                self.new_output['vb'][i] = self.neighbors[nb][i]
