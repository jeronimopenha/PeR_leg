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

    def run(self, n_copies: int = 1) -> dict:

        reports = {}
        for exec_num in range(n_copies):
            exec_key = 'exec_%d' % exec_num

            n2c, c2n = self.init_sa_placement_tables()

            st0 = Stage0SA(self.n_lines, self.n_threads)
            st1 = Stage1SA(c2n, self.n_threads)
            st2 = Stage2SA(self.per_graph.neighbors)
            st3 = Stage3SA(n2c, self.n_threads)
            st4 = Stage4SA()
            st5 = Stage5SA()
            st6 = Stage6SA()
            st7 = Stage7SA()
            st8 = Stage8SA()
            st9 = Stage9SA()
            st10 = Stage10SA()

            counter = 0
            while not st0_edge_sel.done:
                st0.compute()
                st1.compute(st0.old_output, st9.old_output, st1.old_output['wd'])
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

            reports[exec_key] = Util.create_exec_report(self, exec_num, st0_edge_sel.total_pipeline_counter,
                                                        st0_edge_sel.exec_counter, st2_n2c.n2c)

        return Util.create_report(self, "YOTO", n_copies, reports)
