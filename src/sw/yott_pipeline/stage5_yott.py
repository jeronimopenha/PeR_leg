class Stage5YOTT:
  def __init__(self):
      self.new_output = {
        'thread_index': 0,
        'thread_valid': 0,
        'B': 0,
        'SA': 0,
        'C_S': [0,1],    
    } 
      self.old_output = self.new_output

  def compute(self,stage4):
    self.old_output = self.new_output.copy()

    out_previous_stage = stage4.old_output
    

    thread_index = out_previous_stage['thread_index']
    B = out_previous_stage['B']
    C_C = out_previous_stage['C_C']
    dist_CB = out_previous_stage['dist_CB']
    C_S = out_previous_stage['C_S']

    
    SA = self.satisfies_annotation(C_S,C_C,dist_CB) if dist_CB != -1 else True

    self.new_output = {
        'thread_index': thread_index,
        'thread_valid': out_previous_stage['thread_valid'],
        'SA': SA,
        'C_S': C_S,
        'B': B
    }

  def dist_manhattan(self,pe1:tuple, pe2:tuple):
    return abs(pe1[0] - pe2[0]) + abs(pe1[1] - pe2[1])

  def satisfies_annotation(self,C_S,C_C,distC_B)-> bool:
    return distC_B == self.dist_manhattan(C_S,C_C)
