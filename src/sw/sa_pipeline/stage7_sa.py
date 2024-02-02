class Stage7SA:
    """
    Seventh Pipe from SA_Verilog. This pipe is responsible to execute the 2-2 
    additions for the distances found in the left pipe.
    """

    def __init__(self):
        self.new_output = {
            'th_idx': 0,
            'th_valid': False,
            'dc': 0,
            'dvas': 0,
            'dvbs': 0
        }
        self.old_output = self.new_output.copy()

    def compute(self, _in: dict):
        # moving forward the ready outputs
        self.old_output = self.new_output.copy()

        self.new_output['th_idx'] = _in['th_idx']
        self.new_output['th_valid'] = _in['th_valid']

        dvac = _in['dvac']
        dvbc = _in['dvbc']
        dvas = _in['dvas']
        dvbs = _in['dvbs']

        self.new_output['dc'] = dvac + dvbc
        self.new_output['dvas'] = dvas[0] + dvas[1]
        self.new_output['dvbs'] = dvbs[0] + dvbs[1]
