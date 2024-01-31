class Stage6SA:
    """
    Sixth Pipe from SA_Verilog. This pipe is responsible to execute the 2-2 
    additions for the distances found in the left pipe.
    """

    def __init__(self):
        self.new_output = {
            'idx': 0,
            'v': False,
            'dvac': 0,
            'dvbc': 0,
            'dvas': [0, 0],
            'dvbs': [0, 0]
        }
        self.old_output = self.new_output.copy()

    def compute(self, _in: dict):
        # moving forward the ready outputs
        self.old_output = self.new_output.copy()

        self.new_output['idx'] = _in['idx']
        self.new_output['v'] = _in['v']

        dvac = _in['dvac']
        dvbc = _in['dvbc']
        dvas = _in['dvas']
        dvbs = _in['dvbs']

        self.new_output['dvac'] = dvac[0] + dvac[1]
        self.new_output['dvbc'] = dvbc[0] + dvbc[1]
        self.new_output['dvas'] = [dvas[0] + dvas[1], dvas[2] + dvas[3]]
        self.new_output['dvbs'] = [dvbs[0] + dvbs[1], dvbs[2] + dvbs[3]]
