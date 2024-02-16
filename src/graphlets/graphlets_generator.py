import networkx as nx 
from itertools import combinations
class GraphletsGenerator:
    @staticmethod
    def generate_connected_graphlets(k):
        G = nx.complete_graph(k)
        def is_connected_subgraph(graph, nodes):
            subgraph = graph.subgraph(nodes)
            return nx.is_connected(subgraph)

        all_nodes = list(G.nodes())
        all_connected_subgraphs = []

        for k in range(1, len(all_nodes) + 1):
            for nodes_combo in combinations(all_nodes, k):
                if is_connected_subgraph(G, nodes_combo):
                    all_connected_subgraphs.append(G.subgraph(nodes_combo))

        return all_connected_subgraphs

