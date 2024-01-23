from src.sw.yott_pipeline.IFIFO import IFIFO

class Stage0YOTT:
    def __init__(self, fifo: IFIFO,len_pipeline):
        self.fifo = fifo
        self.output = {'thread_index':None,
                       'should_write': None}
        self.total_pipeline_counter = 0
        self.exec_counter: list[int] = [0 for i in range(len_pipeline)]

    def compute(self):
        thread_index, should_write = self.fifo.get() #type:ignore
        self.output = {'thread_index':thread_index,
                    'should_write': should_write}
        
        self.exec_counter[thread_index] += 1
        self.total_pipeline_counter += 1


        
    