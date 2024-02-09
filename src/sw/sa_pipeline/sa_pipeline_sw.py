import time
from typing import Tuple, List

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
import multiprocessing as mp


class SAPipeline(PiplineBase):
    len_pipeline = 6

    def __init__(self, per_graph: PeRGraph, arch_type: ArchType, distance_table_bits: int, make_shuffle: bool,
                 n_threads: int = 1):
        self.len_pipeline: int = 10
        super().__init__(per_graph, arch_type, distance_table_bits, make_shuffle, self.len_pipeline, n_threads, )

    def run(self, n_copies: int = 1) -> dict:
        max_jobs = 8
        exec_times = 1000
        max_counter = pow(self.per_graph.n_cells, 2) * exec_times
        queue = mp.Queue()
        reports = {}
        jobs_alive = []
        for exec_num in range(n_copies):
            p = mp.Process(target=self.exec_pipeline, args=(exec_num, max_counter, queue))
            p.start()
            jobs_alive.append(p)
            if exec_num == 0:
                print('Tasks:')
            if exec_num % 10 == 0 and exec_num != 0:
                print()
            print(exec_num, end=" ")
            while len(jobs_alive) >= max_jobs:
                new_jobs_alive = []
                for job in jobs_alive:
                    if job.is_alive():
                        new_jobs_alive.append(job)
                    else:
                        while not queue.empty():
                            exec_num, exec_counter, n2c = queue.get()
                            exec_key = 'exec_%d' % exec_num
                            reports[exec_key] = Util.create_exec_report(self, exec_num, max_counter,
                                                                        [exec_counter for _ in range(self.n_threads)],
                                                                        n2c
                                                                        )
                jobs_alive = new_jobs_alive
                time.sleep(1)
        while len(jobs_alive) > 0:
            jobs_alive = [job for job in jobs_alive if job.is_alive()]
            time.sleep(1)
        while not queue.empty():
            exec_num, exec_counter, n2c = queue.get()
            exec_key = 'exec_%d' % exec_num
            reports[exec_key] = Util.create_exec_report(self, exec_num, max_counter,
                                                        [exec_counter for _ in range(self.n_threads)],
                                                        n2c
                                                        )

        report = Util.create_report(self, "SA_PIPELINE", n_copies, reports)
        print()
        return report

    def exec_pipeline(self, exec_key, max_counter, queue: mp.Queue):
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
        queue.put([exec_key, st0.exec_counter, n2c])
