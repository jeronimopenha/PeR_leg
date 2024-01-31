class Stage3YOTT:
    def __init__(self, len_pipe, n2c):
        """

        @param len_pipe:
        @type len_pipe:
        @param n2c:
        @type n2c:
        """
        self.n2c = n2c
        self.thread_adj_indexes: list[int] = [0 if i == 0 else 0 for i in range(len_pipe)]
        self.new_output: dict = {
            'thread_index': 0,
            'thread_valid': 0,
            'C_A': [0, 0],
            'B': 0,
            'C_C': [0, 0],
            'dist_CB': 1,
            'adj_index': 0,
            'edge_index': 0
        }

        self.old_output: dict = self.new_output

    def compute(self, stage2, stage6):
        """

        @param stage2:
        @type stage2:
        @param stage6:
        @type stage6:
        """
        self.old_output = self.new_output.copy()

        out_stage6 = stage6.old_output_stage3
        old_thread_index = out_stage6['thread_index']

        if out_stage6['should_write']:
            old_b = out_stage6['B']
            old_c_s = out_stage6['C_S']
            self.n2c[old_thread_index][old_b] = old_c_s  # type:ignore
            self.thread_adj_indexes[old_thread_index] = 0
        elif out_stage6['thread_valid'] == 1:
            self.thread_adj_indexes[old_thread_index] += 1

        out_previous_stage = stage2.old_output
        thread_valid = out_previous_stage['thread_valid']
        thread_index = out_previous_stage['thread_index']
        a = out_previous_stage['A']
        c = out_previous_stage['C']
        c_a = self.n2c[thread_index][a] if thread_valid == 1 else [0, 0]  # type:ignore
        c_c = self.n2c[thread_index][c] if c > -1 else [-1, -1]  # type:ignore

        adj_index = self.thread_adj_indexes[thread_index] if thread_valid else 0
        # print(self.N2C[thread_index])
        self.new_output = {
            'thread_index': thread_index,
            'thread_valid': thread_valid,
            'C_A': c_a,
            'B': out_previous_stage['B'],
            'C_C': c_c,
            'dist_CB': out_previous_stage['dist_CB'],
            'adj_index': adj_index,
            'edge_index': out_previous_stage['edge_index']

        }
