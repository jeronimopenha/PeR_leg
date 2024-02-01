class Stage9SA:
    """
    Ninth Pipe from SA_Verilog. This pipe is responsible to take the decision to do the swap or not.
    """

    def __init__(self):
        self.new_output = {
            'th_idx': 0,
            'th_valid': False,
            'sw': False
        }
        self.old_output = self.new_output.copy()

    def compute(self, _in: dict):
        # moving forward the ready outputs
        self.old_output = self.new_output.copy()

        self.new_output['th_idx'] = _in['th_idx']
        self.new_output['th_valid'] = _in['th_valid']

        dc = _in['dc']
        ds = _in['ds']

        self.new_output['sw'] = ds < dc
