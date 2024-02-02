class Stage4SA:
    """
    Fourth Pipe from SA_Verilog. This pipe is responsible to find the manhatan 
    distances for each combination between cellA and cellB with their 
    respective neighboors cells before swap.
    """

    def __init__(self):
        self.new_output = {
            'th_idx': 0,
            'th_valid': False,
            'cell_a': 0,
            'cell_b': 0,
            'cva': [None, None, None, None],
            'cvb': [None, None, None, None],
            'dvac': [0, 0, 0, 0],
            'dvbc': [0, 0, 0, 0]
        }
        self.old_output = self.new_output.copy()

    def compute(self, _in: dict):
        # moving forward the ready outputs
        self.old_output = self.new_output.copy()

        self.new_output['th_idx'] = _in['th_idx']
        self.new_output['th_valid'] = _in['th_valid']
        self.new_output['cell_a'] = _in['cell_a']
        self.new_output['cell_b'] = _in['cell_b']
        self.new_output['cva'] = _in['cva']
        self.new_output['cvb'] = _in['cvb']

        self.new_output['dvac'] = [0, 0, 0, 0]
        self.new_output['dvbc'] = [0, 0, 0, 0]

        ca = _in['cell_a']
        cb = _in['cell_b']
        cva = _in['cva']
        cvb = _in['cvb']

        for i in range(len(cva)):
            if cva[i] is not None:
                self.new_output['dvac'][i] = get_manhattan_distance(
                    ca, cva[i])
            else:
                break

        for i in range(len(cvb)):
            if cvb[i] is not None:
                self.new_output['dvbc'][i] = get_manhattan_distance(
                    cb, cvb[i])
            else:
                break
