import src.hw.sa_pipeline.util as _u


class Stage5SA:
    """
    Fifth Pipe from SA_Verilog. This pipe is responsible to find the manhatan 
    distances for each combination between cellA and cellB with their 
    respective neighboors cells after swap and execute the first 2-2 additions 
    for the distances found in the left pipe.
    """

    def __init__(self):
        self.new_output = {
            'th_idx': 0,
            'th_valid': False,
            'dvac': [0, 0],
            'dvbc': [0, 0],
            'dvas': [0, 0, 0, 0],
            'dvbs': [0, 0, 0, 0]
        }
        self.old_output = self.new_output.copy()

    def compute(self, _in: dict):
        # moving forward the ready outputs
        self.old_output = self.new_output.copy()

        self.new_output['th_idx'] = _in['th_idx']
        self.new_output['th_valid'] = _in['th_valid']

        cbs = _in['cell_a']
        cas = _in['cell_b']
        cva = _in['cva']
        cvb = _in['cvb']
        dvac = _in['dvac']
        dvbc = _in['dvbc']

        self.new_output['dvac'] = [dvac[0] + dvac[1], dvac[2] + dvac[3]]
        self.new_output['dvbc'] = [dvbc[0] + dvbc[1], dvbc[2] + dvbc[3]]

        self.new_output['dvas'] = [0, 0, 0, 0]
        self.new_output['dvbs'] = [0, 0, 0, 0]

        for i in range(len(cva)):
            if cva[i] is not None:
                if cas == cva[i]:
                    self.new_output['dvas'][i] = get_manhattan_distance(
                        cas, cbs)
                else:
                    self.new_output['dvas'][i] = get_manhattan_distance(
                        cas, cva[i])
            else:
                break

        for i in range(len(cvb)):
            if cvb[i] is not None:
                if cbs == cvb[i]:
                    self.new_output['dvbs'][i] = get_manhattan_distance(
                        cas, cbs)
                else:
                    self.new_output['dvbs'][i] = get_manhattan_distance(
                        cbs, cvb[i])
            else:
                break
