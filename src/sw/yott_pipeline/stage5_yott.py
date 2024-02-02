from src.util.per_enum import ArchType
from src.util.util import Util


class Stage5YOTT:
    def __init__(self, arch_type: ArchType,) -> None:
        self.new_output : dict = {
            'thread_index': 0,
            'thread_valid': 0,
            'B': 0,
            'C_S': [0, 1],
            'C_C': [0, 0],
            'dist_CB': 1,
            'dist_CA_CS': 1

        }
        self.arch_type = arch_type

        self.old_output : dict = self.new_output


    def compute(self,stage4):
        self.old_output = self.new_output.copy()

        out_previous_stage = stage4.old_output
        c_a = out_previous_stage['C_A']
        c_s = out_previous_stage['C_S'] 

        try:
            dist_ca_cs = Util.calc_dist(c_a, c_s, self.arch_type)
        except Exception as e:
            a=1

        self.new_output = {
            'thread_index': out_previous_stage['thread_index'],
            'thread_valid': out_previous_stage['thread_valid'],
            'B': out_previous_stage['B'],
            'C_S': out_previous_stage['C_S'],
            'C_C': out_previous_stage['C_C'],
            'dist_CB': out_previous_stage['dist_CB'],
            'dist_CA_CS': dist_ca_cs,
        }
