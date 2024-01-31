from math import ceil, sqrt
from src.util.per_graph import PeRGraph


class Stage1SA:
    """
    First Pipe from SA_Verilog. This pipe is responsible to search the content of the two cells selected by threads
    """

    def __init__(self, per_graph: PeRGraph, n_threads: int = 10):
        self.per_graph = per_graph
        # self.per_graph.reset_random()
        self.n_threads = n_threads
        # fixme
        self.c2n = [per_graph.get_initial_grid()[0]
                    for i in range(self.n_threads)]
        self.fifo_a = [{'th_idx': 0, 'cell': 0, 'node': None}
                       for i in range(self.n_threads - 2)]
        self.fifo_b = [{'th_idx': 0, 'cell': 0, 'node': None}
                       for i in range(self.n_threads - 2)]
        self.flag = True

        self.output_new = {
            'th_idx': 0,
            'th_valid': False,
            'cell_a': 0,
            'cell_b': 0,
            'node_a': None,
            'node_b': None,
            'sw': {'idx': 0, 'v': False, 'sw': False},
            'wa': {'idx': 0, 'c': 0, 'n': None},
            'wb': {'idx': 0, 'c': 0, 'n': None},
        }
        self.old_output = self.output_new.copy()
        # self.print_matrix(0)

    # TODO update logic
    def compute(self, _in: dict, _sw: dict, _wb: dict):
        # moving forward the ready outputs
        self.old_output = self.output_new.copy()

        # reading pipe inputs
        idx = _in['idx']
        v = _in['v']
        ca = _in['ca']
        cb = _in['cb']

        # enqueuing data
        if v:
            self.fifo_a.append(
                {'idx': self.output_new['idx'], 'c': self.output_new['ca'], 'n': self.output_new['nb']})
            self.fifo_b.append(
                {'idx': self.output_new['idx'], 'c': self.output_new['cb'], 'n': self.output_new['na']})

        # Pop Queues
        wa = self.output_new['wa']
        wb = self.output_new['wb']
        if v:
            wa = self.fifo_a.pop(0)
            wb = self.fifo_b.pop(0)

        # update memory
        usw = self.output_new['sw']['sw']
        uwa = self.output_new['wa']
        uwb = _wb
        if usw:
            if self.flag:
                self.c2n[uwa['idx']][uwa['c']] = wa['n']
                self.flag = not self.flag
            else:
                self.c2n[uwb['idx']][uwb['c']] = uwb['n']
                self.flag = not self.flag
                if (uwb['idx'] == 0):
                    self.print_matrix(uwb['idx'])

        # fifos outptuts ready to be moved forward
        self.output_new['wa'] = wa
        self.output_new['wb'] = wb
        self.output_new['sw'] = _sw

        # data ready to be moved forward
        self.output_new['idx'] = idx
        self.output_new['v'] = v
        self.output_new['ca'] = ca
        self.output_new['cb'] = cb

        # cell content ready to be moved forward
        self.output_new['na'] = self.c2n[idx][ca]
        self.output_new['nb'] = self.c2n[idx][cb]

    def print_matrix(self, idx: int):
        sqrt_ = ceil(sqrt(len(self.c2n[idx])))
        cidx = 0
        str_ = 'c2n_th:%d\n' % idx
        for i in range(sqrt_):
            for j in range(sqrt_):
                if self.c2n[idx][cidx] is None:
                    str_ += '   '
                else:
                    str_ += '%2d ' % self.c2n[idx][cidx]
                cidx += 1
            str_ += '\n'
        print(str_)
