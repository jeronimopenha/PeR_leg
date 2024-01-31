import src.hw.sa_pipeline.util as _u


class Stage2SA:
    """
    Second Pipe from SA_Verilog. This pipe is responsible to bring the neighboor from each node selected in the left pipe in the graph.
    """

    def __init__(self, sa_graph: _u.SaGraph):
        self.sa_graph = sa_graph
        self.neighbors = self.sa_graph.neighbors

        self.new_output = {
            'idx': 0,
            'v': False,
            'ca': 0,
            'cb': 0,
            'na': None,
            'nb': None,
            'va': [None, None, None, None],
            'vb': [None, None, None, None],
            'sw': {'idx': 0, 'v': False, 'sw': False},
            'wa': {'idx': 0, 'c': 0, 'n': None},
            'wb': {'idx': 0, 'c': 0, 'n': None},
        }
        self.old_output = self.new_output.copy()

    def compute(self, _in: dict):
        # moving forward the ready outputs
        self.old_output = self.new_output.copy()

        # reading pipe inputs
        self.new_output['idx'] = _in['idx']
        self.new_output['v'] = _in['v']
        self.new_output['ca'] = _in['ca']
        self.new_output['cb'] = _in['cb']
        self.new_output['na'] = _in['na']
        self.new_output['nb'] = _in['nb']
        self.new_output['sw'] = _in['sw']
        self.new_output['wa'] = _in['wa']
        self.new_output['wb'] = _in['wb']

        self.new_output['va'] = [None, None, None, None]
        self.new_output['vb'] = [None, None, None, None]

        na = _in['na']
        nb = _in['nb']
        if na is not None:
            for i in range(len(self.neighbors[na])):
                self.new_output['va'][i] = self.neighbors[na][i]
        if nb is not None:
            for i in range(len(self.neighbors[nb])):
                self.new_output['vb'][i] = self.neighbors[nb][i]
