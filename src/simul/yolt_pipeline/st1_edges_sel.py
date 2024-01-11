class St1EdgesSel(object):
    """
    This class is responsible to generate the edges sections for each thread.
    """

    def __init__(self, n_threads: int = 1, n_edges: int = 0, latency: int = 5):
        self.latency: int = latency
        self.n_threads: int = n_threads
        self.n_edges: int = n_edges
        self.edge_counter: list[int] = [0 for i in range(self.latency)]

        self.thread_valid: list[bool] = [True if i < self.n_threads else False for i in range(self.latency)]
        self.thread_done: list[bool] = [False if i < self.n_threads else True for i in range(self.latency)]
        self.th_idx: int = 0
        self.done: bool = False

        self.output_new: dict = {
            'th_idx': 0,
            'th_valid': False,
            'edg_n': 0,
        }

        self.output: dict = self.output_new.copy()

    def execute(self):
        # Move forward the output
        self.output = self.output_new.copy()

        # process the new output
        th_idx: int = self.th_idx
        if self.thread_valid[th_idx] and self.edge_counter[th_idx] == self.n_edges:
            self.thread_valid[th_idx] = False
            self.thread_done[th_idx] = True

        # TODO
        # return increment

        # increment thee thread index
        self.th_idx = self.th_idx + 1 if self.th_idx + 1 < self.latency else 0

        if len(set(self.thread_valid)) == 1:
            self.done = True

        self.output_new = {
            'th_idx': th_idx,
            'th_valid': self.thread_valid[th_idx],
            'edg_n': self.edge_counter[th_idx],
        }
