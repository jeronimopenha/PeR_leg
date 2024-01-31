from src.util.per_enum import ArchType
from src.util.util import Util


class Stage4YOTT:
    def __init__(self, arch_type: ArchType, dimension_arch, len_pipeline, distance_table_bits, make_shuffle) -> None:
        """

        @param dimension_arch:
        @type dimension_arch:
        @param len_pipeline:
        @type len_pipeline:
        @param distance_table_bits:
        @type distance_table_bits:
        @param make_shuffle:
        @type make_shuffle:
        """
        self.arch_type = arch_type
        self.dimension_arch: int = dimension_arch
        self.distance_table: list[list] = [Util.get_distance_table(arch_type, self.dimension_arch, make_shuffle) for
                                           _ in range(pow(2, distance_table_bits))]
        self.dist_table_mask: int = pow(2, distance_table_bits) - 1
        self.new_output: dict = {
            'thread_index': 0,
            'thread_valid': 0,
            'B': 0,
            'C_S': [0, 1],
            'C_C': [0, 0],
            'dist_CB': 1,
            'dist_CA_CS': 1

        }
        self.old_output: dict = self.new_output

    def compute(self, stage3):
        """

        @param stage3:
        @type stage3:
        """
        self.old_output = self.new_output

        out_previous_stage = stage3.old_output
        thread_index = out_previous_stage['thread_index']
        edge_index = out_previous_stage['edge_index']

        adj_index = out_previous_stage['adj_index']
        c_a = out_previous_stage['C_A']

        # fixme passar o calculo a linha da tabela de distacias para alum estagio anterior
        i, j = self.distance_table[(thread_index ^ edge_index) & self.dist_table_mask][adj_index]

        c_s = [c_a[0] + i, c_a[1] + j]

        # fixme criam um estágio a frente para calcular as distancias
        dist_ca_cs = Util.calc_dist(c_a, c_s, self.arch_type)  # type:ignore

        self.new_output = {
            'thread_index': thread_index,
            'thread_valid': out_previous_stage['thread_valid'],
            'B': out_previous_stage['B'],
            'C_S': c_s,
            'C_C': out_previous_stage['C_C'],
            'dist_CB': out_previous_stage['dist_CB'],
            'dist_CA_CS': dist_ca_cs,
        }
