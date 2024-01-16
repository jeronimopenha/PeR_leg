class St1EdgesSel(object):
    """
    This class is responsible to generate the edges sections for each thread.
    """

    def __init__(self, n_threads: int, n_edges: int, latency: int):
        self.latency: int = latency
        self.n_threads: int = n_threads
        self.n_edges: int = n_edges
        self.edge_counter: list[int] = [0 for i in range(self.latency)]
        self.exec_counter: list[int] = [0 for i in range(self.latency)]
        self.total_pipeline_counter: int = 0

        self.thread_valid: list[bool] = [True if i < self.n_threads else False for i in range(self.latency)]
        self.thread_done: list[bool] = [False if i < self.n_threads else True for i in range(self.latency)]
        self.th_idx: int = 0
        self.done: bool = False

        self.output_new: dict = {
            'th_idx': 0,
            'th_valid': False,
            'edg_n': 0,
            'incr_edge_n': False
        }

        self.output: dict = self.output_new.copy()

    def execute(self, st1_input: dict, st5_input: dict):
        # Move forward the output
        self.output = self.output_new.copy()

        # return update
        st5_place: bool = st5_input['place']
        st5_b_placed: bool = st5_input['b_placed']

        st1_edg_n: int = st1_input['edg_n']
        st1_th_idx: int = st1_input['th_idx']
        st1_th_valid: int = st1_input['th_valid']
        st1_incr_edge_n: int = st1_input['incr_edge_n']

        if st1_incr_edge_n:
            self.edge_counter[st1_th_idx] = st1_edg_n
        if st1_th_valid:
            self.exec_counter[st1_th_idx] += 1

        self.total_pipeline_counter += 1

        # process the new output
        th_idx: int = self.th_idx
        if th_idx == 0:
            z = 1

        # increment the thread index
        self.th_idx = th_idx + 1 if th_idx + 1 < self.latency else 0

        # done condition
        if st1_th_valid and st1_edg_n == self.n_edges and st1_incr_edge_n:
            self.thread_valid[st1_th_idx] = False
            self.thread_done[st1_th_idx] = True

        # process done condition
        self.done = True
        for th_done in self.thread_done:
            if not th_done:
                self.done = False
                break

        incr_edge_n = st5_place or st5_b_placed
        edge_n: int = self.edge_counter[th_idx] if not incr_edge_n else self.edge_counter[th_idx] + 1
        th_valid: int = self.thread_valid[th_idx]

        self.output_new = {
            'th_idx': th_idx,
            'th_valid': th_valid,
            'edg_n': edge_n,
            'incr_edge_n': incr_edge_n,
        }
