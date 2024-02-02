import math


class Stage0SA:
    """
    This class is responsible to generate the values for each thread.
    """

    def __init__(self, n_cells: int, n_threads: int):
        """


        @param n_threads:
        """
        self.n_threads: int = n_threads
        self.n_cells: int = n_cells
        self.th_bits: int = math.ceil(math.log2(self.n_threads))
        self.cell_bits: int = math.ceil(math.log2(self.n_cells))
        self.counter_mask = int(pow(math.ceil(math.sqrt(self.n_cells)), 2)) - 1
        self.counter: list = [0 for _ in range(self.n_threads)]

        self.cell_a = [0 for _ in range(self.n_threads)]
        self.cell_b = [0 for _ in range(self.n_threads)]
        self.th_valid = [True for _ in range(self.n_threads)]
        self.th_idx = 0

        self.new_output: dict = {
            'th_idx': 0,
            'th_valid': True,
            'cell_a': 0,
            'cell_b': 0,
        }

        self.old_output: dict = self.new_output.copy()

    def compute(self):
        """

        """
        th_idx: int = self.th_idx
        cell_bits: int = self.cell_bits
        mask: int = self.counter_mask

        # Move forward the output
        self.old_output = self.new_output.copy()

        # process the new output
        if not self.th_valid[th_idx]:
            self.counter[th_idx] += 1
            if self.counter[th_idx] >= pow(self.n_cells, 2):
                self.counter[th_idx] = 0
            self.cell_a[th_idx] = self.counter[th_idx] & mask
            self.cell_b[th_idx] = (self.counter[th_idx] >> cell_bits) & mask

            self.th_idx += 1
            if self.th_idx == self.n_threads:
                self.th_idx = 0
        self.th_valid[th_idx] = not self.th_valid[th_idx]

        # th_idx = self.th_idx
        self.new_output = {
            'th_idx': self.th_idx,
            'th_valid': self.th_valid[th_idx],
            'cell_a': self.cell_a[th_idx],
            'cell_b': self.cell_b[th_idx]
        }
