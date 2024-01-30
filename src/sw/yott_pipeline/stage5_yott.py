from src.util.per_enum import ArchType
from src.util.util import Util


class Stage5YOTT:
  def __init__(self, arch_type :ArchType):
      self.arch_type = arch_type 
      self.new_output = {
        'thread_index': 0,
        'thread_valid': 0,
        'B': 0,
        'cost': 0,
        'C_S': [0,1],
        'dist_CA_CS': 1    
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

    cost = self.calc_cost(C_S,C_C,dist_CB,self.arch_type) if dist_CB != -1 else 0

    self.new_output = {
        'thread_index': thread_index,
        'thread_valid': out_previous_stage['thread_valid'],
        'cost': cost,
        'C_S': C_S,
        'B': B,
        'dist_CA_CS': out_previous_stage['dist_CA_CS']
    }

  def calc_cost(self,C_S,C_C,distC_B,arch_type : ArchType)-> bool:
    return abs(Util.calc_dist(C_S,C_C,arch_type) - distC_B)
