from math import ceil, sqrt


class Stage1SA:
    """
    First Pipe from SA_Verilog. This pipe is responsible to search the content of the two cells selected by threads
    """

    def __init__(self, c2n: list[list], n_threads: int):
        self.c2n: list[list] = c2n
        self.n_threads = n_threads
        self.fifo_a = [{'th_idx': 0, 'cell': 0, 'node': None}
                       for i in range(self.n_threads - 2)]
        self.fifo_b = [{'th_idx': 0, 'cell': 0, 'node': None}
                       for i in range(self.n_threads - 2)]
        self.flag = True

        self.new_output = {
            'th_idx': 0,
            'th_valid': False,
            'cell_a': 0,
            'cell_b': 0,
            'node_a': 0,
            'node_b': 0,
            'sw': {'th_idx': 0, 'th_valid': False, 'sw': False},
            'wa': {'th_idx': 0, 'cell': 0, 'node': 0},
            'wb': {'th_idx': 0, 'cell': 0, 'node': 0},
        }
        self.old_output = self.new_output.copy()
        # self.print_matrix(0)

    # TODO update logic
    def compute(self, _in: dict, _sw: dict, _wb: dict):
        # moving forward the ready outputs
        self.old_output = self.new_output.copy()

        # reading pipe inputs
        th_idx = _in['th_idx']
        th_valid = _in['th_valid']
        cell_a = _in['cell_a']
        cell_b = _in['cell_b']

        # enqueuing data
        if th_valid:
            self.fifo_a.append(
                {'th_idx': self.new_output['th_idx'], 'cell': self.new_output['cell_a'],
                 'node': self.new_output['node_b']})
            self.fifo_b.append(
                {'th_idx': self.new_output['th_idx'], 'cell': self.new_output['cell_b'],
                 'node': self.new_output['node_a']})

        # Pop Queues
        wa = self.new_output['wa']
        wb = self.new_output['wb']
        if th_valid:
            wa = self.fifo_a.pop(0)
            wb = self.fifo_b.pop(0)

        # update memory
        usw = self.new_output['sw']['sw']
        uwa = self.new_output['wa']
        uwb = _wb
        if usw:
            if self.flag:
                self.c2n[uwa['th_idx']][uwa['cell']] = wa['node']
                self.flag = not self.flag
            else:
                self.c2n[uwb['th_idx']][uwb['cell']] = uwb['node']
                self.flag = not self.flag
                if uwb['th_idx'] == 0:
                    self.print_matrix(uwb['th_idx'])

        self.new_output = {
            # fifos outptuts ready to be moved forward
            'wa': wa,
            'wb': wb,
            'sw': _sw,

            # data ready to be moved forward
            'th_idx': th_idx,
            'th_valid': th_valid,
            'cell_a': cell_a,
            'cell_b': cell_b,

            # cell content ready to be moved forward
            'node_a': self.c2n[th_idx][cell_a],
            'node_b': self.c2n[th_idx][cell_b],
        }

    def print_matrix(self, idx: int):
        sqrt_ = ceil(sqrt(len(self.c2n[idx])))
        cell_idx = 0
        str_to_print = 'c2n_th:%d\n' % idx
        for i in range(sqrt_):
            for j in range(sqrt_):
                if self.c2n[idx][cell_idx] is None:
                    str_to_print += '   '
                else:
                    str_to_print += '%2d ' % self.c2n[idx][cell_idx]
                cell_idx += 1
            str_to_print += '\n'
        print(str_to_print)
