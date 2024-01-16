from src.util.per_graph import PeRGraph
from src.util.yolt.yolt import Yolt
from src.sw.yolt_pipeline.st1_edges_sel import St1EdgesSel
from src.sw.yolt_pipeline.st2_edges import St2Edges
from src.sw.yolt_pipeline.st3_n2c import St3N2C
from src.sw.yolt_pipeline.st4_dist import St4Dist
from src.sw.yolt_pipeline.st5_c2n import St5C2n


class YoltPipeline(Yolt):
    def __init__(self, per_graph: PeRGraph, n_threads: int = 1):
        super().__init__(per_graph, n_threads)

    def run(self, times: int = 1):
        results: dict = {}
        print(self.per_graph.nodes)
        print(self.per_graph.neighbors)
        print()
        for t in range(times):
            results_key = 'exec_%d' % t
            results[results_key] = []

            n2c, c2n = self.get_initial_position_ij(self.edges_int[0][0], self.latency)

            st1_edge_sel: St1EdgesSel = St1EdgesSel(self.n_threads, self.per_graph.n_edges, self.latency)
            st2_edges: St2Edges = St2Edges(self.edges_int, self.latency, self.per_graph.n_edges)
            st3_n2c: St3N2C = St3N2C(n2c, self.per_graph.n_cells_sqrt, self.latency)
            st4_dist = St4Dist(self.per_graph.n_cells_sqrt)
            st5_c2n = St5C2n(c2n, self.per_graph.n_cells_sqrt)

            counter = 0
            while not st1_edge_sel.done:
                st1_edge_sel.execute(st1_edge_sel.output, st5_c2n.output)
                st2_edges.execute(st1_edge_sel.output)
                st3_n2c.execute(st2_edges.output, st5_c2n.output)
                st4_dist.execute(st3_n2c.output, st4_dist.output)
                st5_c2n.execute(st4_dist.output, st5_c2n.output)
                counter += 1
            results[results_key].append('Total execution clocks: %d\n' % st1_edge_sel.total_pipeline_counter)
            th_dict: dict = {}
            for th in range(self.latency):
                th_key = 'Time_%d_TH_%d' % (th, t)
                th_dict[th_key] = []
                th_dict[th_key].append('thread - %d, loop counter: %d' % (th, st1_edge_sel.exec_counter[th]))
                th_dict[th_key].append(st5_c2n.c2n[th])
            results[results_key].append(th_dict)
        z = 1
