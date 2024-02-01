class Stage10SA:
    """
    Tenth Pipe from SA_Verilog. This pipe is responsible to generate a sync delay
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
        self.new_output['sw'] = _in['sw']
