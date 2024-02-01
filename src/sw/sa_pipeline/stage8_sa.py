class Stage8SA:
    """
    Eighth Pipe from SA_Verilog. This pipe is responsible to execute the 2-2 
    additions for the distances found in the left pipe.
    """

    def __init__(self):
        self.new_output = {
            'th_idx': 0,
            'th_valid': False,
            'dc': 0,
            'ds': 0
        }
        self.old_output = self.new_output.copy()

    def compute(self, _in: dict):
        # moving forward the ready outputs
        self.old_output = self.new_output.copy()

        self.new_output['th_idx'] = _in['th_idx']
        self.new_output['th_valid'] = _in['th_valid']

        dc = _in['dc']
        dvas = _in['dvas']
        dvbs = _in['dvbs']

        self.new_output['dc'] = _in['dc']
        self.new_output['ds'] = dvas + dvbs
