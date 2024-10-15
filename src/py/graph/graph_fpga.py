from src.py.graph.graph import Graph
from math import ceil, sqrt
import networkx as nx


class GraphFGA(Graph):
    def __init__(self, dot_path: str, dot_name: str):
        super().__init__(dot_path, dot_name)
        self.longest_path = []
        self.longest_path_nodes = []
        self.longest_path_and_length()

    def get_nodes_vars(self):
        n_list = list(self.g.nodes)
        nodes_counter = 0
        for i, node in enumerate(n_list):
            nl = node.lower()
            if "level" in nl or "title" in nl:
                self.g.remove_node(node)
                continue
            self.nodes_str.append(node)
            self.nodes_to_idx[node] = nodes_counter
            # Because of the charcteristics of ABC dot graph,
            # I needed to invert the edges
            if len(list(self.g.succ[node])) == 0:
                self.input_nodes.append(node)
            elif len(list(self.g.pred[node])) == 0:
                self.output_nodes.append(node)
            nodes_counter += 1

    def get_edges_vars(self):
        for e in list(self.g.edges):
            # Because of the characteristics of ABC dot graph,
            # I needed to invert the edges
            idx_0 = self.nodes_to_idx[e[1]]
            idx_1 = self.nodes_to_idx[e[0]]
            # Because of the characteristics of ABC dot graph,
            # I needed to invert the edges
            self.edges_str.append((e[1], e[0]))
            self.n_edges += 1

            self.neighbors_idx[idx_0].append(idx_1)
            self.neighbors_idx[idx_1].append(idx_0)
            self.neighbors_str[e[0]].append(e[1])
            self.neighbors_str[e[1]].append(e[0])

            self.dag_neighbors_idx[idx_0].append(idx_1)
            self.dag_neighbors_str[e[0]].append(e[1])

    def longest_path_and_length(self):
        nodes = []
        length = 0
        for o in self.output_nodes:
            for i in self.input_nodes:
                path_tmp = nx.dijkstra_path(self.g, o, i)
                length_tmp = nx.dijkstra_path_length(self.g, o, i)
                if length_tmp > length:
                    length = length_tmp
                    nodes = path_tmp
        self.longest_path_nodes = nodes
        path = []
        for i in range(0, len(nodes) - 1):
            path.append([nodes[i], nodes[i + 1]])
        self.longest_path = path
