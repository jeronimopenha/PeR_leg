class Stage9SA:
    """
    Ninth Pipe from SA_Verilog. This pipe is responsible to take the decision to do the swap or not.
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

    def compute(self, st8_input: dict):
        """

        @param st8_input:
        """
        # moving forward the ready outputs
        self.old_output = self.new_output.copy()

        st8_th_idx = st8_input['th_idx']
        st8_th_valid = st8_input['th_valid']

        st8_dc = st8_input['dc']
        st8_ds = st8_input['ds']

        sw = st8_ds < st8_dc
        if sw:
            a=1

        self.new_output: dict = {
            'th_idx': st8_th_idx,
            'th_valid': st8_th_valid,
            'sw': sw
        }
