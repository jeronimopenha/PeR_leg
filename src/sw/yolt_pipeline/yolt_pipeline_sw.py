from src.util.per_graph import PeRGraph
from src.util.yolt.yolt import Yolt
from src.sw.yolt_pipeline.st1_edges_sel import St1EdgesSel
from src.sw.yolt_pipeline.st2_edges import St2Edges
from src.sw.yolt_pipeline.st3_n2c import St3N2C


class YoltPipeline(Yolt):
    def __init__(self, per_graph: PeRGraph, n_threads: int = 1):
        super().__init__(per_graph, n_threads)

        self.st1_edge_selector: St1EdgesSel = St1EdgesSel(self.n_threads, self.per_graph.n_edges, self.latency)
        self.st2_edges: St2Edges = St2Edges(self.edges_int)
        self.st3_n2c: St3N2C = St3N2C(self.n2c, self.per_graph.n_cells_sqrt)

    def run(self):
        print(self.per_graph.nodes)
        print(self.per_graph.neighbors)
        print()

        while not self.st1_edge_selector.done:
            self.st1_edge_selector.execute()
            self.st2_edges.execute(self.st1_edge_selector.output)
            self.st3_n2c.execute(self.st2_edges.output)
            print(self.st1_edge_selector.output)
            print(self.st2_edges.output)
            print(self.st3_n2c.output)
            print()
            a = 1
