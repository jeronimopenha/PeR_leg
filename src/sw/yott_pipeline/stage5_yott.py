class Stage5YOTT:
  def __init__(self):
      self.output = {
        'thread_index': None,
        'thread_done': None,
        'B': None,
        'C_S': None,    
        'C_C':None,
        'dist_CB': None,
    } 

  def compute(self,stage4):
    out_previous_stage = stage4.output.copy()
    thread_done = out_previous_stage['thread_done']
    if not thread_done:
        thread_index = out_previous_stage['thread_index']
        B = out_previous_stage['B']
        C_C = out_previous_stage['C_C']
        dist_CB = out_previous_stage['dist_CB']
        C_S = out_previous_stage['C_S']

        
        SA = self.satisfies_annotation(C_S,C_C,dist_CB) if dist_CB != -1 else 1

        self.output = {
            'thread_index': thread_index,
            'thread_done':thread_done,
            'SA': SA,
            'C_S': C_S,
            'B': B
        }
    else:
        self.output = {'thread_done': thread_done} 

  def dist_manhattan(self,pe1:tuple, pe2:tuple):
    return abs(pe1[0] - pe2[0]) + abs(pe1[1] - pe2[1])

  def satisfies_annotation(self,C_S,C_C,distC_B)-> bool:
    return distC_B == self.dist_manhattan(C_S,C_C)

if __name__ == "__main__":
   stage3 =  Stage5YOTT()
   assert (stage3.dist_manhattan((0,0),(0,1)) == 1)
   assert(stage3.satisfies_annotation((0,1),(0,2),1) == True)
