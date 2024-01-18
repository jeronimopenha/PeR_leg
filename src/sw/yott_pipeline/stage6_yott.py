class Stage6YOTT:
  def __init__(self,tam_grid, first_vertex, num_threads, len_pipe):
    self.tam_grid =tam_grid
    self.C2N = self.init_C2N(tam_grid, first_vertex, num_threads)
    self.try_count = [0 for i in range(len_pipe)]
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

        if not self.out_of_grid(C_S,self.tam_grid):
            N_C_S = self.C2N[thread_index][C_S]
            should_write = self.should_write(SA,N_C_S,self.try_count[thread_index])
        else: 
           should_write = False
        
        self.output_stage3 = {
        'should_write': should_write,
        'thread_index':thread_index,
        'B': B,
        'C_S': C_S
        }

        if should_write:
            self.C2N[thread_index][C_S] = B
            self.try_count[thread_index] = 0
        else:
           self.try_count[thread_index] += 1
           
        stage0.fifo.put(thread_index,should_write)


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

  def should_write(self,satisfies_annotation,N_C_S, try_count):
    if N_C_S != -1:
       return False
    return satisfies_annotation or try_count > 10
    
