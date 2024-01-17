class Stage4YOTT:
  def __init__(self,tam_grid, first_vertex, num_threads):
    self.C2N = self.init_C2N(tam_grid, first_vertex, num_threads)
    self.output_stage2 = {
        'writed': 0,
        'thread_index':None,
        'B': None,
        'C_S': None
    } 

  def compute(self,stage3,tam_grid,FIFO):
      out_previous_stage = stage3.output.copy()
      thread_done = out_previous_stage['thread_done']

      if not thread_done:
        thread_index = out_previous_stage['thread_index']
        SA = out_previous_stage['SA']
        C_S = out_previous_stage['C_S']
        B = out_previous_stage['B']

        if not self.out_of_grid(C_S,tam_grid):
            N_C_S = self.C2N[thread_index][C_S]
            should_write = self.should_write(SA,N_C_S)
        else: 
           should_write = False
        
        self.output_stage2 = {
        'writed': should_write,
        'thread_index':thread_index,
        'B': B,
        'C_S': C_S
        }

        if should_write:
            self.C2N[thread_index][C_S] = B
        FIFO.put((thread_index,should_write))


  def init_C2N(self, tam_grid, first_vertex, num_threads):
        C2N = [None for i in range(num_threads)]
        for k in range(num_threads):
          C2N[k]={} #type:ignore
          for i in range(tam_grid):
            for j in range(tam_grid):
              C2N[k][(i,j)] = -1 #type:ignore
          C2N[k][self.initial_position()] = first_vertex #type:ignore
        return C2N

  def initial_position(self):
    return (0,0)
  
  def out_of_grid(self,C_S,tam_grid):
    return ((C_S[0] < 0 or C_S[0]>=tam_grid ) or (C_S[1] < 0 or C_S[1]>=tam_grid ))

  def should_write(self,satisfies_annotation,N_C_S):
    if N_C_S != -1:
       return False
    # value = random.random()
    # if value <=0.1:
    #    return True
    return satisfies_annotation
    
  
if __name__ == '__main__':
   stage4 = Stage4YOTT(3,0,1)
   assert(stage4.C2N[0] == {(0, 0): 0, (0, 1): -1, (0, 2): -1, (1, 0): -1, (1, 1): -1, (1, 2): -1, (2, 0): -1, (2, 1): -1, (2, 2): -1})
   assert(stage4.initial_position() == (0,0))
   assert(stage4.should_write(1,-1) == True)
   assert(stage4.should_write(0,0) == False)
   assert(stage4.should_write(0,-1) == False)
   assert(stage4.should_write(1,1) == False)

