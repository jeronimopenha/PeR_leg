import cython


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

        st9_th_idx: cython.int = st9_input['th_idx']
        st9_th_valid: cython.bint = st9_input['th_valid']
        st9_sw: cython.bint = st9_input['sw']

        # fixme only for debugging
        '''if st9_th_idx == 0 and st9_th_valid:
            # print(st9_input)
            z = 1'''

        self.new_output: dict = {
            'th_idx': st9_th_idx,
            'th_valid': st9_th_valid,
            'sw': st9_sw
        }
