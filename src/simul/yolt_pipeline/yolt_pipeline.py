from src.util.proj_graph import ProjGraph
from src.simul.yolt_pipeline.st1_edges_sel import St1EdgesSel
from src.simul.yolt_pipeline.st2_edges import St2Edges


class YoltPipeline(object):
    def __init__(self, proj_graph: ProjGraph, n_threads: int = 1):
        self.n_threads: int = n_threads
        self.latency: int = 5
        self.proj_graph: ProjGraph = proj_graph
        self.edges: list = []
        self.edges_str = self.proj_graph.get_edges_zigzag()
        for a, b, dir in self.edges_str:
            self.edges.append(
                [
                    self.proj_graph.nodes_to_idx[a],
                    self.proj_graph.nodes_to_idx[b]
                ]
            )
        self.st1_edge_selector: St1EdgesSel = St1EdgesSel(self.n_threads, self.proj_graph.n_edges, self.latency)
        self.st2_edges: St2Edges = St2Edges(self.edges, self.latency)

    def run(self):
        print(self.proj_graph.nodes)
        print(self.proj_graph.neighbors)
        print()

        while not self.st1_edge_selector.done:
            self.st1_edge_selector.execute()
            self.st2_edges.execute(self.st1_edge_selector.output)
            print(self.st2_edges.output)
            a = 1
