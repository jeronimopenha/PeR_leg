import src.hw.sa_pipeline.util as _u


class Stage4SA:
    """
    Fourth Pipe from SA_Verilog. This pipe is responsible to find the manhatan 
    distances for each combination between cellA and cellB with their 
    respective neighboors cells before swap.
    """

    def __init__(self, sa_graph: _u.SaGraph):
        self.sa_graph = sa_graph
        self.new_output = {
            'idx': 0,
            'v': False,
            'ca': 0,
            'cb': 0,
            'cva': [None, None, None, None],
            'cvb': [None, None, None, None],
            'dvac': [0, 0, 0, 0],
            'dvbc': [0, 0, 0, 0]
        }
        self.old_output = self.new_output.copy()

    def compute(self, _in: dict):
        # moving forward the ready outputs
        self.old_output = self.new_output.copy()

        self.new_output['idx'] = _in['idx']
        self.new_output['v'] = _in['v']
        self.new_output['ca'] = _in['ca']
        self.new_output['cb'] = _in['cb']
        self.new_output['cva'] = _in['cva']
        self.new_output['cvb'] = _in['cvb']

        self.new_output['dvac'] = [0, 0, 0, 0]
        self.new_output['dvbc'] = [0, 0, 0, 0]

        ca = _in['ca']
        cb = _in['cb']
        cva = _in['cva']
        cvb = _in['cvb']

        for i in range(len(cva)):
            if cva[i] is not None:
                self.new_output['dvac'][i] = self.sa_graph.get_manhattan_distance(
                    ca, cva[i])
            else:
                break

        for i in range(len(cvb)):
            if cvb[i] is not None:
                self.new_output['dvbc'][i] = self.sa_graph.get_manhattan_distance(
                    cb, cvb[i])
            else:
                break
