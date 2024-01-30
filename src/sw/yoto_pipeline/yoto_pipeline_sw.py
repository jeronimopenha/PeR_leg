from src.sw.sa_pipeline import st1
from src.util.per_graph import PeRGraph
from src.util.util import Util
from src.util.per_enum import ArchType
from src.util.traversal import Traversal
from src.sw.yoto_pipeline.stage1_yoto import Stage1YOTO
from src.sw.yoto_pipeline.stage2_yoto import Stage2YOTO
from src.sw.yoto_pipeline.stage3_yoto import Stage3YOTO
from src.sw.yoto_pipeline.stage4_yoto import Stage4YOTO
from src.sw.yoto_pipeline.stage5_yoto import Stage5YOTO


class YotoPipeline(Traversal):
    def __init__(self, per_graph: PeRGraph, arch_type: ArchType, distance_table_bits: int, make_shuffle: bool,
                 n_threads: int = 1, random_seed: int = 0):
        self.len_pipeline: int = 6
        super().__init__(per_graph, arch_type, distance_table_bits, make_shuffle, self.len_pipeline, n_threads,
                         random_seed)

    def run(self, n_copies: int = 1) -> dict:

        # print(self.per_graph.nodes)
        # print(self.per_graph.neighbors)
        # print()

        reports = {}
        self.reset_random(0)
        for exec_num in range(n_copies):
            exec_key = 'exec_%d' % exec_num
            first_nodes: list = [self.edges_int[i][0][0] for i in range(self.len_pipeline)]
            n2c, c2n = self.get_initial_position_ij(first_nodes, self.len_pipeline)

            st1_edge_sel: Stage1YOTO = Stage1YOTO(self.n_threads, self.visited_edges, self.len_pipeline)
            st2_edges: Stage2YOTO = Stage2YOTO(self.edges_int, self.distance_table_bits, self.visited_edges)
            st3_n2c: Stage3YOTO = Stage3YOTO(n2c, self.per_graph.n_cells_sqrt, self.len_pipeline)
            st4_dist = Stage4YOTO(self.arch_type, self.per_graph.n_cells_sqrt, self.distance_table_bits,
                                  self.make_shuffle)
            st5_c2n = Stage5YOTO(c2n, self.per_graph.n_cells_sqrt)

            counter = 0
            while not st1_edge_sel.done:
                st1_edge_sel.compute(st1_edge_sel.old_output, st5_c2n.old_output)
                st2_edges.compute(st1_edge_sel.old_output)
                st3_n2c.compute(st2_edges.old_output, st5_c2n.old_output)
                st4_dist.compute(st3_n2c.old_output)
                st5_c2n.compute(st4_dist.old_output, st5_c2n.old_output)
                counter += 1

            reports[exec_key] = Util.create_exec_report(self, exec_num, st1_edge_sel.total_pipeline_counter,
                                                        st1_edge_sel.exec_counter, st3_n2c.n2c)

        return Util.create_report(self, "YOTO", n_copies, reports)


