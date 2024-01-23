class Stage1YOTT:
    def __init__(self,len_pipe:int,len_edges) -> None:
            self.edges_indexes = [0 for i in range(len_pipe)]
            self.len_edges = len_edges
            #lista de threads_done
            #saída da computação realizada
            self.new_output = {'thread_index':None,
                'edge_index': None,
                'thread_done':1}
            
            #saída anterior
            self.old_output = self.new_output.copy()

    
    def compute(self,stage0):
        self.output = self.new_output.copy()
        out_previous_stage = stage0.output
        
        thread_index = out_previous_stage['thread_index']
        should_write = out_previous_stage['should_write']

        self.edges_indexes[thread_index] += should_write
        
        edge_index = self.edges_indexes[thread_index]

        thread_done = edge_index ==  self.len_edges
        # if thread_done -> thread_valid = False
        self.output = {'thread_index':thread_index,
            'edge_index': edge_index,
            'thread_done':thread_done,
            'thread_valid':None} #FIXME  

          

