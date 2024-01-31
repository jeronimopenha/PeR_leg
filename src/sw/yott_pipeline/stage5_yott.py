from src.util.per_enum import ArchType
from src.util.util import calc_dist


class Stage5YOTT:
    def __init__(self, arch_type: ArchType):
        """

        @param arch_type:
        @type arch_type:
        """
        self.arch_type: ArchType = arch_type
        self.new_output: dict = {
            'thread_index': 0,
            'thread_valid': 0,
            'B': 0,
            'cost': 0,
            'C_S': [0, 1],
            'dist_CA_CS': 1
        }
        self.old_output: dict = self.new_output

    def compute(self, stage4):
        """

        @param stage4:
        @type stage4:
        """
        self.old_output = self.new_output.copy()

        out_previous_stage: dict = stage4.old_output

        thread_index = out_previous_stage['thread_index']
        b = out_previous_stage['B']
        c_c = out_previous_stage['C_C']
        dist_cb = out_previous_stage['dist_CB']
        c_s = out_previous_stage['C_S']

        cost = self.calc_cost(c_s, c_c, dist_cb, self.arch_type) if dist_cb != -1 else 0

        self.new_output = {
            'thread_index': thread_index,
            'thread_valid': out_previous_stage['thread_valid'],
            'cost': cost,
            'C_S': c_s,
            'B': b,
            'dist_CA_CS': out_previous_stage['dist_CA_CS']
        }

    @staticmethod
    def calc_cost(c_s: list, c_c: list, dist_c_b: int, arch_type: ArchType) -> int:
        """

        @param c_s: 
        @type c_s: 
        @param c_c: 
        @type c_c: 
        @param dist_c_b: 
        @type dist_c_b: 
        @param arch_type: 
        @type arch_type: 
        @return: 
        @rtype: 
        """
        return abs(calc_dist(c_s, c_c, arch_type) - dist_c_b)
