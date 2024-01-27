class Stage3YOTT:
  def __init__(self,len_pipe,N2C):
    self.N2C = N2C
    self.thread_adj_indexes: list[int] = [0 if i == 0 else 0 for i in range(len_pipe)]
    self.new_output = {
        'thread_index': 0,
        'thread_valid': 0,
        'C_A':[0,0],
        'B': 0,
        'C_C':[0,0],
        'dist_CB': 1,
        'adj_index': 0,
        'edge_index': 0

    } 

    self.old_output = self.new_output

  def compute(self,stage2,stage6, len_adjacentes):
    self.old_output = self.new_output.copy()

    out_stage6 = stage6.old_output_stage3
    old_thread_index = out_stage6['thread_index']
    
    if out_stage6['should_write']:
        old_B = out_stage6['B']
        old_C_S = out_stage6['C_S']
        self.N2C[old_thread_index][old_B] = old_C_S #type:ignore
        self.thread_adj_indexes[old_thread_index] = 0
    elif out_stage6['thread_valid'] == 1:
        self.thread_adj_indexes[old_thread_index] += 1

    out_previous_stage = stage2.old_output
    thread_valid = out_previous_stage['thread_valid'] 
    thread_index = out_previous_stage['thread_index']
    A = out_previous_stage['A']
    C = out_previous_stage['C']
    C_A = self.N2C[thread_index][A] if thread_valid == 1 else [0,0]#type:ignore
    C_C = self.N2C[thread_index][C] if C > -1 else [-1,-1] #type:ignore

    adj_index = self.thread_adj_indexes[thread_index]

    self.new_output = {
        'thread_index': thread_index,
        'thread_valid': thread_valid,
        'C_A':C_A,
        'B': out_previous_stage['B'],
        'C_C': C_C,
        'dist_CB': out_previous_stage['dist_CB'],
        'adj_index': adj_index,
        'edge_index': out_previous_stage['edge_index']

    } 

 
   