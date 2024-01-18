class Stage1YOTT:
    def __init__(self,len_pipe:int, num_threads,len_edges) -> None:
            self.edges_indexes = [0 for i in range(len_pipe)]
            self.len_edges = len_edges
            self.num_threads = num_threads
            self.output = {'thread_index':None,
                'edge_index': None,
                'thread_done':None}
    
    def compute(self,stage0):
        out_previous_stage = stage0.output.copy()
        
        thread_index = out_previous_stage['thread_index']
        should_write = out_previous_stage['should_write']

        self.edges_indexes[thread_index] += should_write
        
        edge_index = self.edges_indexes[thread_index]

        thread_done = edge_index ==  self.len_edges

        self.output = {'thread_index':thread_index,
            'edge_index': edge_index,
            'thread_done':thread_done}  

          

