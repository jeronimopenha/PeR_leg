from src.util.proj_graph import ProjGraph
from src.simul.yott_pipeline.st1_edges_sel import St1EdgesSel


class YottPipeline(object):
    def __init__(self, proj_graph: ProjGraph):
        self.n_threads: int = 1
        self.proj_graph: ProjGraph = proj_graph
        self.st1_edge_selector: St1EdgesSel = St1EdgesSel(self.n_threads, self.proj_graph.n_edges)

        pass

    def run(self):
        print(self.proj_graph.nodes)
        print(self.proj_graph.neighbors)

        while not self.st1_edge_selector.done:
            self.st1_edge_selector.execute()
            print(self.st1_edge_selector.output)
            a = 1
