class Stage9SA:
    """
    Ninth Pipe from SA_Verilog. This pipe is responsible to take the decision to do the swap or not.
    """

    def __init__(self):
        self.new_output = {
            'idx': 0,
            'v': False,
            'sw': False
        }
        self.old_output = self.new_output.copy()

    def compute(self, _in: dict):
        # moving forward the ready outputs
        self.old_output = self.new_output.copy()

        self.new_output['idx'] = _in['idx']
        self.new_output['v'] = _in['v']

        dc = _in['dc']
        ds = _in['ds']

        self.new_output['sw'] = ds < dc
