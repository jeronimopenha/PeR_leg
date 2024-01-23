from src.sw.yott_pipeline.IFIFO import IFIFO

class Stage0YOTT:
    def __init__(self, fifo: IFIFO,len_pipeline):
        self.fifo = fifo
        self.output = {'thread_index':None, # Trocar depois 0,0,False
                       'should_write': None,
                       'thread_valid':None}
        
        self.total_pipeline_counter = 0
        self.exec_counter: list[int] = [0 for i in range(len_pipeline)]

    def compute(self):

        thread_index, should_write = (0,0) if self.fifo.is_empty() else self.fifo.get() #type:ignore
        thread_valid = not self.fifo.is_empty()
        self.output = {'thread_index':thread_index,
                    'should_write': should_write,
                    'thread_valid': thread_valid}
        
        self.exec_counter[thread_index] += 1
        self.total_pipeline_counter += 1


        
    