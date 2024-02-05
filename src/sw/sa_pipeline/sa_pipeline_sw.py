from src.util.per_graph import PeRGraph
from src.util.per_enum import ArchType
from src.util.piplinebase import PiplineBase
from src.sw.sa_pipeline.stage0_sa import Stage0SA
from src.sw.sa_pipeline.stage1_sa import Stage1SA
from src.sw.sa_pipeline.stage2_sa import Stage2SA
from src.sw.sa_pipeline.stage3_sa import Stage3SA
from src.sw.sa_pipeline.stage4_sa import Stage4SA
from src.sw.sa_pipeline.stage5_sa import Stage5SA
from src.sw.sa_pipeline.stage6_sa import Stage6SA
from src.sw.sa_pipeline.stage7_sa import Stage7SA
from src.sw.sa_pipeline.stage8_sa import Stage8SA
from src.sw.sa_pipeline.stage9_sa import Stage9SA
from src.sw.sa_pipeline.stage10_sa import Stage10SA
from src.util.util import Util


class SAPipeline(PiplineBase):
    len_pipeline = 6

    def __init__(self, per_graph: PeRGraph, arch_type: ArchType, distance_table_bits: int, make_shuffle: bool,
                 n_threads: int = 1):
        self.len_pipeline: int = 10
        super().__init__(per_graph, arch_type, distance_table_bits, make_shuffle, self.len_pipeline, n_threads, )

    def run(self, exec_id: str, return_dict: dict, n_copies: int = 1):
        exec_times = 1
        reports = {}
        for exec_num in range(n_copies):
            exec_key = 'exec_%d' % exec_num

            n2c, c2n = self.init_sa_placement_tables()

            st0 = Stage0SA(self.per_graph.n_cells, self.n_threads)
            st1 = Stage1SA(c2n, self.n_threads)
            st2 = Stage2SA(self.per_graph.neighbors)
            st3 = Stage3SA(n2c, self.n_threads)
            st4 = Stage4SA(self.arch_type, self.n_lines, self.n_columns)
            st5 = Stage5SA(self.arch_type, self.n_lines, self.n_columns)
            st6 = Stage6SA()
            st7 = Stage7SA()
            st8 = Stage8SA()
            st9 = Stage9SA()
            st10 = Stage10SA()

            counter = 0
            max_counter = pow(self.per_graph.n_cells, 2) * exec_times
            while counter < max_counter:
                st0.compute()
                st1.compute(st0.old_output, st9.old_output, st1.old_output['wb'])
                st2.compute(st1.old_output)
                st3.compute(st2.old_output, st3.old_output['wb'])
                st4.compute(st3.old_output)
                st5.compute(st4.old_output)
                st6.compute(st5.old_output)
                st7.compute(st6.old_output)
                st8.compute(st7.old_output)
                st9.compute(st8.old_output)
                st10.compute(st9.old_output)

                counter += 1
            for th_idx in range(self.n_threads):
                for n_idx in range(len(n2c[th_idx])):
                    if n2c[th_idx][n_idx] is not None:
                        n2c[th_idx][n_idx] = Util.get_line_column_from_cell(n2c[th_idx][n_idx], self.n_lines,
                                                                            self.n_columns)
                    else:
                        n2c[th_idx][n_idx] = [None, None]
            reports[exec_key] = Util.create_exec_report(self, exec_num, counter,
                                                        [st0.exec_counter for _ in range(self.n_threads)], n2c)
        if exec_id not in return_dict.keys():
            return_dict[exec_id] = []
        return_dict[exec_id].append(Util.create_report(self, "SA_PIPELINE", n_copies, reports))
