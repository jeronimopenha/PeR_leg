import math


class Stage6YOTT:
    def __init__(self, tam_grid: int, len_pipe: int, c2n: list[list[list]]):
        """

        @param tam_grid:
        @type tam_grid:
        @param len_pipe:
        @type len_pipe:
        @param c2n:
        @type c2n:
        """
        self.tam_grid: int = tam_grid
        self.c2n: list[list[list]] = c2n
        self.threads_current_adj_dists: list = [1 for _ in range(len_pipe)]
        self.threads_free_cel: list[list] = [[None, math.inf] for _ in range(len_pipe)]
        self.new_output_stage3: dict = {
            'should_write': 0,
            'thread_index': 0,
            'thread_valid': 0,
            'B': 0,
            'C_S': [0, 0]
        }
        self.old_output_stage3: dict = self.new_output_stage3

    def compute(self, stage5, stage0):
        """

        @param stage5:
        @type stage5:
        @param stage0:
        @type stage0:
        """
        self.old_output_stage3: dict = self.new_output_stage3.copy()
        out_previous_stage: dict = stage5.old_output
        thread_index = out_previous_stage['thread_index']
        cost = out_previous_stage['cost']
        c_s = out_previous_stage['C_S']
        b = out_previous_stage['B']
        thread_valid = out_previous_stage['thread_valid']
        dist_ca_cs = out_previous_stage['dist_CA_CS']

        # fixme  dividir em mais estágios. 1 ou 2
        was_there_change = dist_ca_cs != self.threads_current_adj_dists[thread_index]
        if not self.out_of_grid(c_s, self.tam_grid):
            n_c_s = self.c2n[thread_index][c_s[0]][c_s[1]]
            if n_c_s is None:
                if dist_ca_cs < 3:
                    if cost == 0:
                        should_write = 1
                    else:
                        if cost < self.threads_free_cel[thread_index][1]:
                            self.threads_free_cel[thread_index] = [c_s, cost]
                        should_write = 0
                else:
                    should_write = 1
            else:
                should_write = 0
        else:
            should_write = 0

        if was_there_change:
            self.threads_current_adj_dists[thread_index] = dist_ca_cs
            if self.threads_free_cel[thread_index][0] is not None:
                c_s = self.threads_free_cel[thread_index][0]
                should_write = 1

        should_write = should_write and thread_valid

        self.new_output_stage3 = {
            'should_write': should_write,
            'thread_index': thread_index,
            'thread_valid': thread_valid,
            'B': b,
            'C_S': c_s
        }

        if should_write == 1:
            self.c2n[thread_index][c_s[0]][c_s[1]] = b
            self.threads_current_adj_dists[thread_index] = 1
            self.threads_free_cel[thread_index] = [None, math.inf]  # type:ignore

        if thread_valid == 1:
            stage0.fifo.put(thread_index, should_write)

    @staticmethod
    def out_of_grid(c_s: list, tam_grid: int) -> bool:
        """

        @param c_s:
        @type c_s:
        @param tam_grid:
        @type tam_grid:
        @return:
        @rtype:
        """
        return (c_s[0] < 0 or c_s[0] >= tam_grid) or (c_s[1] < 0 or c_s[1] >= tam_grid)
