from src.util.per_enum import ArchType
from src.util.util import Util as U

class Stage4YOTT:
    def __init__(self, dimension_arch,len_pipeline) -> None:        
        self.dimension_arch: int = dimension_arch
        self.distance_table: list[list] = [U.get_distance_table(ArchType.MESH,self.dimension_arch) for i in range(len_pipeline)]

        self.new_output = {
        'thread_index': 0,
        'thread_valid': 0,
        'B': 0,
        'C_S': [0,1],    
        'C_C':[0,0],
        'dist_CB': 1,
        'dist_CA_CS': 1

    } 
        self.old_output = self.new_output  

    def compute(self, stage3):
        self.old_output = self.new_output 

        out_previous_stage = stage3.old_output
        thread_index = out_previous_stage['thread_index']

        adj_index = out_previous_stage['adj_index']
        C_A = out_previous_stage['C_A']

        i,j = self.distance_table[thread_index][adj_index]
        
        C_S = [C_A[0]+i,C_A[1]+j] 

        dist_CA_CS = U.dist_manhattan(C_A,C_S) #type:ignore

        self.new_output = {
        'thread_index': thread_index,
        'thread_valid': out_previous_stage['thread_valid'],
        'B': out_previous_stage['B'],
        'C_S': C_S,    
        'C_C':out_previous_stage['C_C'],
        'dist_CB': out_previous_stage['dist_CB'],
        'dist_CA_CS': dist_CA_CS
    } 


        