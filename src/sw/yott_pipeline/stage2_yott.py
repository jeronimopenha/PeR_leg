class Stage2YOTT:
  def __init__(self, ITL: list[list], annotations : list, num_threads:int ):
    super().__init__()
    self.threads_edges = ITL
    self.len_edges = len(ITL)
    self.num_threads = num_threads 
    self.annotations = annotations

    self.new_output = {
        'thread_index': 0,
        'thread_valid': 0,
        'A':0,
        'B': 0,
        'C':-1,
        'dist_CB': 0,
    }

    self.old_output = self.new_output
  
  def compute(self,stage1):
    self.old_output = self.new_output.copy()
    out_previous_stage = stage1.old_output

    thread_index = out_previous_stage['thread_index']
    edge_index = out_previous_stage['edge_index']

    A,B = self.threads_edges[thread_index][edge_index]
    C,dist_CB = self.annotations[edge_index]
    
    self.new_output = {
    'thread_index':thread_index,
    'thread_valid': out_previous_stage['thread_valid'],
    'A': A,
    'B': B,
    'C': C,
    'dist_CB': dist_CB
}

