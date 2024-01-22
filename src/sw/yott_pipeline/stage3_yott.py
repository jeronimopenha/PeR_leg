class Stage3YOTT:
  def __init__(self,len_pipe,N2C):
    self.N2C = N2C
    self.thread_adj_indexes: list[int] = [-1 if i == 0 else 0 for i in range(len_pipe)]
    self.output = {
        'thread_index': None,
        'thread_done': None,
        'C_A':None,
        'B': None,
        'C_C':None,
        'dist_CB': None,
        'adj_index':None
    } 

  def compute(self,stage2,stage6, len_adjacentes):
    out_stage6 = stage6.output_stage3.copy()
    old_thread_index = out_stage6['thread_index']
    
    if out_stage6['should_write']:
        old_B = out_stage6['B']
        old_C_S = out_stage6['C_S']
        self.N2C[old_thread_index][old_B] = old_C_S #type:ignore

        self.thread_adj_indexes[old_thread_index] = 0
    else:
       if old_thread_index != None:
        self.thread_adj_indexes[old_thread_index] += 1 if self.thread_adj_indexes[old_thread_index] < len_adjacentes else 0 

    out_previous_stage = stage2.output.copy()
    print(out_previous_stage)
    thread_done = out_previous_stage['thread_done']
    if not thread_done :
        thread_index = out_previous_stage['thread_index']
        A = out_previous_stage['A']
        C = out_previous_stage['C']
        
        C_A = self.N2C[thread_index][A] #type:ignore
        C_C = self.N2C[thread_index][C] if C > -1 else (-1,-1) #type:ignore

        adj_index = self.thread_adj_indexes[thread_index]

        self.output = {
            'thread_index': thread_index,
            'thread_done': thread_done,
            'C_A':C_A,
            'B': out_previous_stage['B'],
            'C_C':C_C,
            'dist_CB': out_previous_stage['dist_CB'],
            'adj_index':adj_index
        } 
    else:
        self.output = {'thread_done': thread_done} 
 
   