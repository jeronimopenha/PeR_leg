class Stage6YOTT:
  def __init__(self,tam_grid, len_pipe,C2N):
    self.tam_grid =tam_grid
    self.C2N = C2N
    self.try_count = [0 for i in range(len_pipe)]
    self.threads_free_cel = [None for i in range(len_pipe)]
    self.output_stage3= {
        'should_write': 0,
        'thread_index':0 ,
        'B': None,
        'C_S': None
    } 

  def compute(self,stage5,stage0):
      out_previous_stage = stage5.output.copy()
      thread_done = out_previous_stage['thread_done']
      if not thread_done:
        thread_index = out_previous_stage['thread_index']
        SA = out_previous_stage['SA']
        C_S = out_previous_stage['C_S']
        B = out_previous_stage['B']

        follow_annotation = self.try_count[thread_index] < 10
        
        if not self.out_of_grid(C_S,self.tam_grid):
            N_C_S = self.C2N[thread_index][C_S[0]][C_S[1]]
            should_write = self.should_write(SA,N_C_S)
        else: 
           N_C_S = -1
           should_write = False
        
        if not follow_annotation and self.threads_free_cel[thread_index] != None: #type:ignore
           C_S = self.threads_free_cel[thread_index] #type:ignore
           should_write =  True
        elif follow_annotation and self.threads_free_cel[thread_index] == None and N_C_S == None: #type:ignore
           self.threads_free_cel[thread_index] =  C_S #type:ignore

        self.output_stage3 = {
        'should_write': should_write,
        'thread_index':thread_index,
        'B': B,
        'C_S': C_S
        }

        if should_write:
            self.C2N[thread_index][C_S[0]][C_S[1]] = B
            self.try_count[thread_index] = 0
            self.threads_free_cel[thread_index] = None #type:ignore
        else:
           self.try_count[thread_index] += 1
           
        stage0.fifo.put(thread_index,should_write)  
  
  def out_of_grid(self,C_S,tam_grid):
    return ((C_S[0] < 0 or C_S[0]>=tam_grid ) or (C_S[1] < 0 or C_S[1]>=tam_grid ))

  def should_write(self,satisfies_annotation,N_C_S):
    if N_C_S != None:
       return False
    return satisfies_annotation 
    
