from src.util.per_graph import PeRGraph
from src.sw.yott_pipeline.FIFOQueue import FIFOQueue
from src.sw.yott_pipeline.stage0_yott import Stage0YOTT
from src.sw.yott_pipeline.stage1_yott import Stage1YOTT
from src.sw.yott_pipeline.stage2_yott import Stage2YOTT
from src.sw.yott_pipeline.stage3_yott import Stage3YOTT
from src.sw.yott_pipeline.stage4_yott import Stage4YOTT
from src.sw.yott_pipeline.stage5_yott import Stage5YOTT
from src.sw.yott_pipeline.stage6_yott import Stage6YOTT
from src.sw.yott_pipeline.stage7_yott import Stage7YOTT
from src.sw.yott_pipeline.stage8_yott import Stage8YOTT
from src.sw.yott_pipeline.stage9_yott import Stage9YOTT
from src.util.piplinebase import PiplineBase
from src.util.util import Util


class YOTTPipeline(PiplineBase):
    len_pipeline = 10

    def __init__(self, per_graph: PeRGraph, arch_type, distance_table_bits, make_shuffle, num_threads: int = None):
        num_threads = self.len_pipeline if num_threads == None else num_threads
        super().__init__(per_graph, arch_type, distance_table_bits, make_shuffle, self.len_pipeline, num_threads)
        self.len_edges = len(self.edges_int[0])

    def run(self, n_copies: int = 1) -> dict:

        reports = {}
        for exec_num in range(n_copies):
            exec_key = 'exec_%d' % exec_num

            first_nodes: list = [self.edges_int[i][0][0] for i in range(self.len_pipeline)]
            n2c, c2n = self.init_traversal_placement_tables(first_nodes)

            stage0 = Stage0YOTT(FIFOQueue(self.n_threads), self.len_pipeline)
            stage1 = Stage1YOTT(self.len_pipeline, self.n_threads, self.len_edges)
            stage2 = Stage2YOTT(self.edges_int, self.per_graph, self.annotations, self.n_threads,
                                self.distance_table_bits)
            stage3 = Stage3YOTT(self.len_pipeline, n2c)
            stage4 = Stage4YOTT(self.arch_type, self.n_lines, self.distance_table_bits, self.make_shuffle)
            stage5 = Stage5YOTT(self.arch_type)
            stage6 = Stage6YOTT(self.arch_type)
            stage7 = Stage7YOTT(self.n_lines, self.len_pipeline, c2n)
            stage8 = Stage8YOTT()
            stage9 = Stage9YOTT(self.len_pipeline)

            counter = 0
            while not stage1.done:
                # print(stage6.old_output_stage3)
                stage0.compute()
                # print(stage0.new_output)
                # print()
                # print(stage0.old_output)
                stage1.compute(stage0)
                # print(stage1.new_output)
                # print()
                # print(stage1.old_output)
                stage2.compute(stage1)
                # print(stage2.new_output)
                # print()
                # print(stage2.old_output)
                stage3.compute(stage2, stage9)
                # print(stage3.new_output)
                # print()
                # print(stage3.old_output)
                # print(stage6.C2N)
                stage4.compute(stage3)
                # print(stage4.new_output)
                # print()
                # print(stage4.old_output)
                stage5.compute(stage4)
                # print(stage5.new_output)
                # print()
                # print(stage5.old_output)
                stage6.compute(stage5)
                # print(stage6.new_output_stage3)
                # print()
                # print(stage5.old_output)
                stage7.compute(stage6, stage9)
                # print(stage6.new_output_stage3)
                # print()
                stage8.compute(stage7)
                # print(stage6.new_output_stage3)
                # print()
                stage9.compute(stage8, stage0)
                # print(stage6.new_output_stage3)
                # print()

                # input()
                counter += 1
            # self.print_grid(stage7.c2n)

            reports[exec_key] = Util.create_exec_report(self, exec_num, stage0.total_pipeline_counter,
                                                        stage0.exec_counter, stage3.n2c)

        return Util.create_report(self, "YOTT", n_copies, reports)

    def print_grid(self, C2N):
        for idx_thread, thread in enumerate(C2N):
            print(f'thread{idx_thread}')
            for row in thread:
                print(row)
            print()
