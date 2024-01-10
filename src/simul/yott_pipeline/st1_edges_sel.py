class St1EdgesSel(object):
    """
    This class is responsible to generate the edges sections for each thread.
    """

    def __init__(self, n_threads: int = 1, n_edges: int = 0):
        self.latency = 5
        self.n_threads: int = n_threads
        self.n_edges: int = n_edges
        self.edge_counter: list[int] = [0 for i in range(self.latency)]

        self.thread_valid: list[bool] = [True if i < self.n_threads else False for i in range(self.latency)]
        self.thread_done: list[bool] = [False if i < self.n_threads else True for i in range(self.latency)]
        self.idx = 0
        self.done = False

        self.output_new = {
            'th_idx': 0,
            'edge': 0,
            'valid': False,
        }

        self.output = self.output_new.copy()

    def execute(self):
        # Move forward the output
        self.output = self.output_new.copy()

        # process the new output
        idx = self.idx
        if self.thread_valid[idx] and self.edge_counter[idx] == self.n_edges:
            self.thread_valid[idx] = False
            self.thread_done[idx] = True

        # TODO
        # return increment

        # increment thee thread index
        self.idx = self.idx + 1 if self.idx + 1 < self.latency else 0

        if len(set(self.thread_valid)) == 1:
            self.done = True

        self.output_new = {
            'th_idx': idx,
            'edge': self.edge_counter[idx],
            'valid': self.thread_valid[idx],
        }
