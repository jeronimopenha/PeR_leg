import random

class Stage3YOTT:
  def __init__(self):
    self.output = {
        'thread_index': None,
        'thread_done': None,
        'SA': None,
        'C_S': None,
        'B': None
    } 
    self.ADJS_PEs = [(0,1),(0,-1),(1,0),(-1,0)]

  def compute(self,stage2 ):
    out_previous_stage = stage2.output.copy()
    thread_done = out_previous_stage['thread_done']
    if not thread_done:
        thread_index = out_previous_stage['thread_index']
        C_A = out_previous_stage['C_A']
        B = out_previous_stage['B']
        C_C = out_previous_stage['C_C']
        dist_CB = out_previous_stage['dist_CB']

        adj_PE = random.choice(self.ADJS_PEs)
        C_S = (adj_PE[0]+C_A[0],adj_PE[1]+C_A[1])
        
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
   stage3 =  Stage3YOTT()
   assert (stage3.dist_manhattan((0,0),(0,1)) == 1)
   assert(stage3.satisfies_annotation((0,1),(0,2),1) == True)
