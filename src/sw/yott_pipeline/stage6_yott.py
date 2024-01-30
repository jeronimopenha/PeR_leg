import math


class Stage6YOTT:
  def __init__(self,tam_grid, len_pipe,C2N):
    self.tam_grid =tam_grid
    self.C2N = C2N
    self.threads_current_adj_dists = [1 for i in range(len_pipe)]
    self.threads_free_cel = [[None,math.inf] for i in range(len_pipe)]
    self.new_output_stage3= {
        'should_write': 0,
        'thread_index':0 ,
        'thread_valid': 0,
        'B': 0,
        'C_S': [0,0]
    } 
    self.old_output_stage3 = self.new_output_stage3

  def compute(self,stage5,stage0):
      self.old_output_stage3 =  self.new_output_stage3.copy()
      out_previous_stage = stage5.old_output
      thread_index = out_previous_stage['thread_index']
      cost = out_previous_stage['cost']
      C_S = out_previous_stage['C_S']
      B = out_previous_stage['B']
      thread_valid = out_previous_stage['thread_valid']
      dist_CA_CS = out_previous_stage['dist_CA_CS']

      was_there_change = dist_CA_CS != self.threads_current_adj_dists[thread_index]
      if not self.out_of_grid(C_S,self.tam_grid):
         N_C_S = self.C2N[thread_index][C_S[0]][C_S[1]]
         if N_C_S == None:
            if dist_CA_CS < 3:
               if cost == 0:
                  should_write = 1
               else:
                  if cost < self.threads_free_cel[thread_index][1]:
                     self.threads_free_cel[thread_index] = [C_S,cost]
                  should_write = 0
            else: 
               should_write = 1
         else:
            should_write = 0
      else: 
         should_write = 0
      

      if was_there_change:
         self.threads_current_adj_dists[thread_index] = dist_CA_CS
         if self.threads_free_cel[thread_index][0] != None:
            C_S = self.threads_free_cel[thread_index][0]
            should_write = 1

             
      should_write = should_write and thread_valid

      self.new_output_stage3 = {
      'should_write': should_write,
      'thread_index':thread_index,
      'thread_valid': thread_valid,
      'B': B,
      'C_S': C_S
      }

      if should_write == 1:
         self.C2N[thread_index][C_S[0]][C_S[1]] = B
         self.threads_current_adj_dists[thread_index] = 1
         self.threads_free_cel[thread_index] = [None,math.inf] #type:ignore

      
      if thread_valid == 1:   
         stage0.fifo.put(thread_index,should_write)  

  def out_of_grid(self,C_S,tam_grid):
    return ((C_S[0] < 0 or C_S[0]>=tam_grid ) or (C_S[1] < 0 or C_S[1]>=tam_grid ))
