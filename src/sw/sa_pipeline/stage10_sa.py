class Stage10SA:
    """
    Tenth Pipe from SA_Verilog. This pipe is responsible to generate a sync delay
    """

    def __init__(self):
        """

        """
        self.new_output: dict = {
            'th_idx': 0,
            'th_valid': False,
            'sw': False
        }
        self.old_output: dict = self.new_output.copy()

    def compute(self, st9_input: dict):
        """

        @param st9_input:
        """
        # moving forward the ready outputs
        self.old_output = self.new_output.copy()

        st9_th_idx = st9_input['th_idx']
        st9_th_valid = st9_input['th_valid']
        st9_sw = st9_input['sw']

        self.new_output: dict = {
            'th_idx': st9_th_idx,
            'th_valid': st9_th_valid,
            'sw': st9_sw
        }
