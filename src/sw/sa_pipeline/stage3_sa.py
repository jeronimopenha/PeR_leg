from math import ceil, sqrt


class Stage3SA:
    """
    Third Pipe from SA_Verilog. This pipe is responsible to bring the neighbor's cell from each neighbor node.
    """

    def __init__(self, n2c: list[list], n_threads: int):
        """

        @param n2c:
        @param n_threads:
        """
        self.n_threads: int = n_threads
        self.n2c: list[list] = n2c
        self.flag: bool = True
        self.new_output: dict = {
            'th_idx': 0,
            'th_valid': False,
            'cell_a': 0,
            'cell_b': 0,
            'cva': [None, None, None, None],
            'cvb': [None, None, None, None],
            'sw': {'th_idx': 0, 'th_valid': False, 'sw': False},
            'wa': {'th_idx': 0, 'cell': 0, 'node': None},
            'wb': {'th_idx': 0, 'cell': 0, 'node': None},
        }
        self.old_output: dict = self.new_output.copy()
        # self.print_matrix(0)

    def compute(self, st2_input: dict, st3_wb: dict):
        """

        @param st2_input:
        @param st3_wb:
        """
        # moving forward the ready outputs
        self.old_output = self.new_output.copy()

        st2_th_idx: int = st2_input['th_idx']
        st2_th_valid: bool = st2_input['th_valid']
        st2_cell_a: int = st2_input['cell_a']
        st2_cell_b: int = st2_input['cell_b']
        st2_sw: list = st2_input['sw']
        st2_wa: list = st2_input['wa']
        st2_wb: list = st2_input['wb']
        st2_va: list = st2_input['va']
        st2_vb: list = st2_input['vb']

        # fixme only for debugging
        if st2_th_idx == 0:
            z = 1

        # update memory
        usw = self.old_output['sw']['sw']
        uwa = self.old_output['wa']
        uwb = st3_wb
        if usw:
            if self.flag:
                if uwa['node'] is not None:
                    self.n2c[uwa['th_idx']][uwa['node']] = uwa['cell']
                self.flag = not self.flag
            else:
                if uwb['node'] is not None:
                    self.n2c[uwb['th_idx']][uwb['node']] = uwb['cell']
                self.flag = not self.flag

        cva: list = [None, None, None, None]
        cvb: list = [None, None, None, None]

        for i in range(len(st2_va)):
            if st2_va[i] is not None:
                cva[i] = self.n2c[st2_th_idx][st2_va[i]]
        for i in range(len(st2_vb)):
            if st2_vb[i] is not None:
                cvb[i] = self.n2c[st2_th_idx][st2_vb[i]]

        self.new_output = {
            'th_idx': st2_th_idx,
            'th_valid': st2_th_valid,
            'cell_a': st2_cell_a,
            'cell_b': st2_cell_b,
            'cva': cva,
            'cvb': cvb,
            'sw': st2_sw,
            'wa': st2_wa,
            'wb': st2_wb,
        }

    def print_matrix(self, idx: int):
        sqrt_ = ceil(sqrt(len(self.n2c[idx])))
        nidx = 0
        str_ = 'n2c_th:%d\n' % idx
        for i in range(sqrt_):
            for j in range(sqrt_):
                str_ += '%d ' % self.n2c[idx][nidx]
                nidx += 1
            str_ += '\n'
        print(str_)
