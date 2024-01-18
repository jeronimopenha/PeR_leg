class Stage2YOTT:
  def __init__(self, ITL: list, annotations : list, num_threads:int ):
    super().__init__()
    self.edges = ITL
    self.len_edges = len(ITL)
    self.num_threads = num_threads 
    self.annotations = annotations
    self.stage_finished = False
    self.output = {
        'thread_index': None,
        'A':None,
        'B': None,
        'C':None,
        'dist_CB': None,

    }
  
  def compute(self,stage1):
    out_previous_stage = stage1.output.copy()
    thread_done = out_previous_stage['thread_done']
    if not thread_done:
        edge_index = out_previous_stage['edge_index']
        thread_index = out_previous_stage['thread_index']
        B,A = self.edges[edge_index]
        C,dist_CB = self.annotations[edge_index]

        self.output = {
        'thread_index':thread_index,
        'thread_done': thread_done,
        'A': A,
        'B': B,
        'C': C,
        'dist_CB': dist_CB
    }
    else:
      self.output = {'thread_done': thread_done}


if __name__ == "__main__":
    ITL = [(1,0),(2,1),(3,2),(4,3),(5,4)]
    annotations = [[-1,-1],[-1,-1],[-1,-1],[0,2],[0,1]]
    stage2 = Stage2YOTT(ITL,annotations,1)

    assert(stage2.output == {
        'thread_index':0,
        'thread_done':False,
        'A':0,
        'B': 1,
        'C':-1,
        'dist_CB': -1
    } )

    assert(stage2.stage_finished == False)

    assert(stage2.output == {
        'thread_done':True,
    } )
    assert(stage2.stage_finished == True)