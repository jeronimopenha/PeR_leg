from src.util.proj_graph import ProjGraph
from src.simul.yolt_pipeline.st1_edges_sel import St1EdgesSel
from src.simul.yolt_pipeline.st2_edges import St2Edges


class YoltPipeline(object):
    def __init__(self, proj_graph: ProjGraph, n_threads: int = 1):
        self.n_threads: int = n_threads
        self.latency: int = 5
        self.proj_graph: ProjGraph = proj_graph
        self.st2_edges: list = self.proj_graph.get_edges_zigzag()

        self.st1_edge_selector: St1EdgesSel = St1EdgesSel(self.n_threads, self.proj_graph.n_edges, self.latency)
        self.st2_edges: St2Edges = St2Edges(self.n_threads, self.latency)

        pass

    def run(self):
        print(self.proj_graph.nodes)
        print(self.proj_graph.neighbors)

        while not self.st1_edge_selector.done:
            self.st1_edge_selector.execute()
            print(self.st1_edge_selector.output)
            a = 1
