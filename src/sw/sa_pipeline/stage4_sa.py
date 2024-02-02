class Stage4SA:
    """
    Fourth Pipe from SA_Verilog. This pipe is responsible to find the manhandle
    distances for each combination between cellA and cellB with their 
    respective neighbors cells before swap.
    """

    def __init__(self):
        """

        """
        self.new_output: dict = {
            'th_idx': 0,
            'th_valid': False,
            'cell_a': 0,
            'cell_b': 0,
            'cva': [None, None, None, None],
            'cvb': [None, None, None, None],
            'dvac': [0, 0, 0, 0],
            'dvbc': [0, 0, 0, 0]
        }
        self.old_output: dict = self.new_output.copy()

    def compute(self, st3_input: dict):
        """

        @param st3_input:
        """
        # moving forward the ready outputs
        self.old_output = self.new_output.copy()

        st3_th_idx: int = st3_input['th_idx']
        st3_th_valid: bool = st3_input['th_valid']
        st3_cell_a: int = st3_input['cell_a']
        st3_cell_b: int = st3_input['cell_b']
        st3_cva: list = st3_input['cva']
        st3_cvb: list = st3_input['cvb']

        dvac = [0, 0, 0, 0]
        dvbc = [0, 0, 0, 0]

        ca = st3_input['cell_a']
        cb = st3_input['cell_b']
        cva = st3_input['cva']
        cvb = st3_input['cvb']

        for i in range(len(cva)):
            if cva[i] is not None:
                dvac[i] = get_manhattan_distance(ca, cva[i])

        for i in range(len(cvb)):
            if cvb[i] is not None:
                dvbc[i] = get_manhattan_distance(cb, cvb[i])

        self.new_output: dict = {
            'th_idx': st3_th_idx,
            'th_valid': st3_th_valid,
            'cell_a': st3_cell_a,
            'cell_b': st3_cell_b,
            'cva': st3_cva,
            'cvb': st3_cvb,
            'dvac': dvac,
            'dvbc': dvbc
        }
