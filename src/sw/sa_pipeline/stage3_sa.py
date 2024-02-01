from math import ceil, sqrt


class Stage3SA:
    """
    Third Pipe from SA_Verilog. This pipe is responsible to bring the neighboor's cell from each neighbor node.
    """

    def __init__(self, n2c: list[list], n_threads: int = 10):
        self.n_threads = n_threads
        self.n2c = n2c
        self.flag = True
        self.new_output = {
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
        self.old_output = self.new_output.copy()
        # self.print_matrix(0)

    def compute(self, _in: dict, _wb: dict):
        # moving forward the ready outputs
        self.old_output = self.new_output.copy()

        # update memory
        usw = self.new_output['sw']['sw']
        uwa = self.new_output['wa']
        uwb = _wb
        if usw:
            if self.flag:
                if uwa['n'] is not None:
                    self.n2c[uwa['th_idx']][uwa['node']] = uwa['cell']
                self.flag = not self.flag
            else:
                if uwb['node'] is not None:
                    self.n2c[uwb['th_idx']][uwb['node']] = uwb['cell']
                self.flag = not self.flag
                # if(uwb['idx'] == 0):
                #    self.print_matrix(uwb['idx'])

        # reading pipe inputs
        self.new_output['th_idx'] = _in['th_idx']
        self.new_output['th_valid'] = _in['th_valid']
        self.new_output['cell_a'] = _in['cell_a']
        self.new_output['cell_b'] = _in['cell_b']

        self.new_output['sw'] = _in['sw']
        self.new_output['wa'] = _in['wa']
        self.new_output['wb'] = _in['wb']

        self.new_output['cva'] = [None, None, None, None]
        self.new_output['cvb'] = [None, None, None, None]

        idx = _in['th_idx']
        va = _in['va']
        vb = _in['vb']

        for i in range(len(va)):
            if va[i] is not None:
                self.new_output['cva'][i] = self.n2c[idx][va[i]]
            else:
                break
        for i in range(len(vb)):
            if vb[i] is not None:
                self.new_output['cvb'][i] = self.n2c[idx][vb[i]]
            else:
                break

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
