from src.sw.yott_pipeline.IFIFO import IFIFO

class Stage0YOTT:
    def __init__(self, fifo: IFIFO):
        self.fifo = fifo
        self.output = {'thread_index':None,
                       'should_write': None}
    
    def compute(self):
        thread_index, should_write = self.fifo.get() #type:ignore
        self.output = {'thread_index':thread_index,
                    'should_write': should_write}

        
    