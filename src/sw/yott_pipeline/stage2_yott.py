class Stage2YOTT:
  def __init__(self,num_threads,first_vertex,num_vertexes):
    self.N2C = self.init_N2C(num_threads,first_vertex,num_vertexes)
    self.output = {
        'thread_index': None,
        'thread_done': None,
        'C_A':None,
        'B': None,
        'C_C':None,
        'dist_CB': None
    } 

  def compute(self,stage1,stage4):
    out_stage4 = stage4.output_stage2.copy()

    if out_stage4['writed']:
        old_B = out_stage4['B']
        old_C_S = out_stage4['C_S']
        old_thread_index = out_stage4['thread_index']
        # print(out_stage4)
        self.N2C[old_thread_index][old_B] = old_C_S #type:ignore

    out_previous_stage = stage1.output.copy()
    thread_done = out_previous_stage['thread_done']
    if not thread_done :
        thread_index = out_previous_stage['thread_index']
        A = out_previous_stage['A']
        B = out_previous_stage['B']
        C = out_previous_stage['C']
        dist_CB = out_previous_stage['dist_CB']

        C_A = self.N2C[thread_index][A] #type:ignore
        C_C = self.N2C[thread_index][C] if C > -1 else (-1,-1) #type:ignore

        self.output = {
            'thread_index': thread_index,
            'thread_done': thread_done,
            'C_A':C_A,
            'B': B,
            'C_C':C_C,
            'dist_CB': dist_CB
        } 
    else:
        self.output = {'thread_done': thread_done} 
    

  def init_N2C(self, num_threads,first_vertex,num_vertexes):
        N2C = []
        for i in range(num_threads):
          N2C.append([(-1,-1) for j in range(num_vertexes)])
          N2C[i][first_vertex] = self.initial_position()
        return N2C
        
  def initial_position(self):
    return (0,0)
  
if __name__ == "__main__":
   stage2 = Stage2YOTT(1,0,6)
   assert(stage2.N2C==[[(0,0),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1)]]) #type:ignore
   