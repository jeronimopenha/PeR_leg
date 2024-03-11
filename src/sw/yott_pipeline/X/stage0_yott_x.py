from src.sw.yott_pipeline.IFIFO import IFIFO


class Stage0YOTTX:
    def __init__(self, fifo: IFIFO, len_pipeline:int,len_threads:int, len_vertexes:int, ):
        """

        @param fifo:
        @type fifo:
        @param len_pipeline:
        @type len_pipeline:
        """

        self.fifo = fifo
        self.total_pipeline_counter = 0
        self.exec_counter: list[int] = [0 for _ in range(len_pipeline)]
        self.new_output: dict = {'thread_index': 0,
                                 'should_write': 0,
                                 'thread_valid': 0}
        self.old_output: dict = self.new_output
        self.th_count_placed_vertexes = [1 if i < len_threads else len_vertexes for i in range(len_pipeline)]
        self.len_vertexes = len_vertexes

    def compute(self,mc_limiar):
        """

        """
        self.old_output = self.new_output.copy()

        thread_valid = 1 if not self.fifo.is_empty() else 0
        
        thread_index, should_write = (0, 0) if thread_valid == 0 else self.fifo.get()  # type:ignore
        
        self.th_count_placed_vertexes[thread_index] += should_write

        thread_valid = thread_valid and self.th_count_placed_vertexes[thread_index]/self.len_vertexes < mc_limiar


        self.new_output = {'thread_index': thread_index,
                           'should_write': should_write,
                           'thread_valid': thread_valid}

        self.exec_counter[thread_index] += thread_valid
        self.total_pipeline_counter += 1
