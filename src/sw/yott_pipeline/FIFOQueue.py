from src.sw.yott_pipeline.IFIFO import IFIFO
from queue import Queue

class FIFOQueue(IFIFO):
    def __init__(self, num_threads):
        self.fifo = self.init_fifo(num_threads)

    def init_fifo(self, num_threads):
        fifo = Queue()
        for i in range(num_threads):
            fifo.put((i,0))
        return fifo

    def put(self, thread_index,should_write):
        self.fifo.put((thread_index, should_write)) #type:ignore

    def get(self):
        return self.fifo.get() #type:ignore
    
    def is_empty(self) -> bool:
        return self.fifo.empty()