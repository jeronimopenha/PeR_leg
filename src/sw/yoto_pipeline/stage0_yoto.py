class Stage0YOTO(object):
    """
    This class is responsible to generate the edges sections for each thread.
    """

    def __init__(self, n_threads: int, n_edges: int, len_pipeline: int):
        """

        @param n_threads:
        @type n_threads:
        @param n_edges:
        @type n_edges:
        @param len_pipeline:
        @type len_pipeline:
        """
        self.len_pipeline: int = len_pipeline
        self.n_threads: int = n_threads
        self.n_edges: int = n_edges
        self.edge_counter: list[int] = [0 for _ in range(self.len_pipeline)]
        self.exec_counter: list[int] = [0 for _ in range(self.len_pipeline)]
        self.total_pipeline_counter: int = 0

        self.thread_valid: list[bool] = [True if i < self.n_threads else False for i in range(self.len_pipeline)]
        self.thread_done: list[bool] = [False if i < self.n_threads else True for i in range(self.len_pipeline)]
        self.th_idx: int = 0
        self.done: bool = False

        self.new_output: dict = {
            'th_idx': 0,
            'th_valid': False,
            'edg_n': 0,
            'incr_edge': False
        }

        self.old_output: dict = self.new_output.copy()

    def compute(self, st1_input: dict, st5_input: dict):
        """

        @param st1_input:
        @type st1_input:
        @param st5_input:
        @type st5_input:
        """
        # Move forward the output
        self.old_output = self.new_output.copy()

        # return update
        st5_place: bool = st5_input['place']

        st1_edg_n: int = st1_input['edg_n']
        st1_th_idx: int = st1_input['th_idx']
        st1_th_valid: int = st1_input['th_valid']
        st1_incr_edge: int = st1_input['incr_edge']

        if st1_incr_edge:
            self.edge_counter[st1_th_idx] = st1_edg_n
        if st1_th_valid:
            self.exec_counter[st1_th_idx] += 1

        self.total_pipeline_counter += 1

        # process the new output
        th_idx: int = self.th_idx

        # increment the thread index
        self.th_idx = th_idx + 1 if th_idx + 1 < self.len_pipeline else 0

        # done condition
        if st1_th_valid and st1_edg_n == self.n_edges and st1_incr_edge:
            self.thread_valid[st1_th_idx] = False
            self.thread_done[st1_th_idx] = True

        # process done condition
        self.done = True
        for th_done in self.thread_done:
            if not th_done:
                self.done = False
                break

        incr_edge = st5_place
        edge_n: int = self.edge_counter[th_idx] if not st5_place else self.edge_counter[th_idx] + 1
        th_valid: int = self.thread_valid[th_idx]

        self.new_output = {
            'th_idx': th_idx,
            'th_valid': th_valid,
            'edg_n': edge_n,
            'incr_edge': incr_edge,
        }
