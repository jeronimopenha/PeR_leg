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

        self.st1_edge_selector: St1EdgesSel = St1EdgesSel(self.n_threads, self.per_graph.n_edges, self.latency)
        self.st2_edges: St2Edges = St2Edges(self.edges_int)
        self.st3_n2c: St3N2C = St3N2C(self.n2c, self.per_graph.n_cells_sqrt)
        self.st4_dist = St4Dist(self.per_graph.n_cells_sqrt, self.latency)
        self.st5_c2n = St5C2n(self.c2n, self.per_graph.n_cells_sqrt)

    def run(self):
        print(self.per_graph.nodes)
        print(self.per_graph.neighbors)
        print()

        while not self.st1_edge_selector.done:
            self.st1_edge_selector.execute(self.st1_edge_selector.output, self.st5_c2n.output)
            self.st2_edges.execute(self.st1_edge_selector.output)
            self.st3_n2c.execute(self.st2_edges.output, self.st5_c2n.output)
            self.st4_dist.execute(self.st3_n2c.output, self.st4_dist.output, self.st5_c2n.output)
            self.st5_c2n.execute(self.st4_dist.output, self.st5_c2n.output)
            print(self.st1_edge_selector.output)
            print(self.st2_edges.output)
            print(self.st3_n2c.output)
            print(self.st4_dist.output)
            print(self.st5_c2n.output)
            print()
