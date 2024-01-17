class Stage1YOTT:
  def __init__(self, ITL: list, annotations : list, num_threads:int, tam_pipe: int):
    super().__init__()
    self.edges = ITL
    self.len_edges = len(ITL)
    self.edges_indexes = [0 for i in range(tam_pipe)]
    self.threads_done: list[bool] = [False if i < num_threads else True for i in range(num_threads)]
    self.num_threads = num_threads 
    self.annotations = annotations
    self.stage_finished = False
    self.output = {
        'thread_index': None,
        'A':None,
        'B': None,
        'C':None,
        'dist_CB': None
    }
  
  def compute(self,thread_index,writed):
    self.edges_indexes[thread_index] += writed
    
    edge_index = self.edges_indexes[thread_index]

    thread_done = edge_index ==  self.len_edges

    if not thread_done:
        B,A = self.edges[edge_index]
        C,dist_CB = self.annotations[edge_index]

        self.output = {
        'thread_index':thread_index,
        'thread_done': thread_done,
        'A':A,
        'B': B,
        'C':C,
        'dist_CB': dist_CB
    }
    else:
      self.output = {'thread_done': thread_done}
      
    self.threads_done[thread_index] = edge_index ==  self.len_edges

    self.stage_finished = sum(self.threads_done) == self.num_threads

if __name__ == "__main__":
    ITL = [(1,0),(2,1),(3,2),(4,3),(5,4)]
    annotations = [[-1,-1],[-1,-1],[-1,-1],[0,2],[0,1]]
    stage1 = Stage1YOTT(ITL,annotations,1,6)

    stage1.compute(0,0)
    assert(stage1.edges_indexes[0]==0)
    assert(stage1.output == {
        'thread_index':0,
        'thread_done':False,
        'A':0,
        'B': 1,
        'C':-1,
        'dist_CB': -1
    } )

    stage1.compute(0,1)
    stage1.compute(0,1)
    stage1.compute(0,1)
    stage1.compute(0,1)
    assert(stage1.stage_finished == False)

    stage1.compute(0,1)
    assert(stage1.edges_indexes[0]==5)
    assert(stage1.output == {
        'thread_done':True,
    } )
    assert(stage1.stage_finished == True)