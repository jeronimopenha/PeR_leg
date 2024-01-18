from src.util.util import Util as U

class Stage4YOTT:
    def __init__(self, dimension_arch) -> None:        
        self.dimension_arch: int = dimension_arch
        self.distance_table: list[list] = U.get_distance_table(self.dimension_arch)

        self.output = {
        'thread_index': None,
        'thread_done': None,
        'B': None,
        'C_S': None,    
        'C_C':None,
        'dist_CB': None,
    } 

    def compute(self, stage3):
        out_previous_stage = stage3.output.copy()
        thread_done = out_previous_stage['thread_done']
        if not thread_done:
            adj_index = out_previous_stage['adj_index']
            C_A = out_previous_stage['C_A']

            i,j = self.distance_table[adj_index]
            C_S = (C_A[0]+i,C_A[1]+j) 

            self.output = {
            'thread_index': out_previous_stage['thread_index'],
            'thread_done': out_previous_stage['thread_done'],
            'B': out_previous_stage['B'],
            'C_S': C_S,    
            'C_C':out_previous_stage['C_C'],
            'dist_CB': out_previous_stage['dist_CB'],
        } 

        else:
            self.output = {'thread_done': thread_done} 

        