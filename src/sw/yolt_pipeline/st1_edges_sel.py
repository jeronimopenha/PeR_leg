class St1EdgesSel(object):
    """
    This class is responsible to generate the edges sections for each thread.
    """

    def __init__(self, n_threads: int, n_edges: int, latency: int):
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
            'place': False
        }

        self.output: dict = self.output_new.copy()

    def execute(self, st1_input: dict, st5_input: dict):
        # Move forward the output
        self.output = self.output_new.copy()

        # return update
        st5_place: bool = st5_input['place']

        st1_edg_n: int = st1_input['edg_n']
        st1_th_idx: int = st1_input['th_idx']
        st1_place: int = st1_input['place']
        if st1_place:
            if st1_edg_n == self.n_edges - 1:
                self.edge_counter[st1_th_idx] = 0
            else:
                self.edge_counter[st1_th_idx] = st1_edg_n

            # process the new output
        th_idx: int = self.th_idx

        # increment the thread index
        self.th_idx = th_idx + 1 if th_idx + 1 < self.latency else 0

        # done condition
        if self.thread_valid[th_idx] and self.edge_counter[th_idx] == self.n_edges:
            self.thread_valid[th_idx] = False
            self.thread_done[th_idx] = True

        # process done condition
        self.done = True
        for th_done in self.thread_done:
            if not th_done:
                self.done = False
                break

        edge_n: int = self.edge_counter[th_idx] if not st5_place else self.edge_counter[th_idx] + 1
        th_valid: int = self.thread_valid[th_idx]

        self.output_new = {
            'th_idx': th_idx,
            'th_valid': th_valid,
            'edg_n': edge_n,
            'place': st5_place,
        }
