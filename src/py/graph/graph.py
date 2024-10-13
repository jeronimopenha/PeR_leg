import pygraphviz as pgv
import networkx as nx
import random
from math import ceil, sqrt
from collections import defaultdict
from typing import List, Tuple, Dict, Any


class Graph:

    def __init__(self, dot_path: str, dot_name: str):
        self.dot_path: str = dot_path
        self.dot_name: str = dot_name
        self.gv: pgv.AGraph = pgv.AGraph(self.dot_path, strict=False, directed=True)
        self.g: nx.DiGraph = nx.DiGraph(self.gv)
        self.nodes: List[str] = []  # list(self.g.nodes)
        self.edges: List[Tuple[str, str]] = []  # list(self.g.edges)
        self.n_edges: int = 0  # len(self.edges_str)
        self.nodes_to_idx: Dict[str, int] = {}
        self.neighbors: Dict[int, List[int]] = defaultdict(list)
        self.input_nodes: list = []
        self.output_nodes: list = []
        self.n_cells: int = 0
        self.n_cells_sqrt: int = 0
        self.get_dot_vars()

    def get_edges_idx(self, edges):
        edges_idx = [(self.nodes_to_idx[a], self.nodes_to_idx[b])
                     for (a, b) in edges]
        return edges_idx

    def get_nodes_idx(self, nodes):
        return [self.nodes_to_idx[n] for n in nodes]

    def get_mesh_distances(self, make_shuffle: bool = True) -> list[list[int]]:
        distance_table_raw: list[list] = [[] for _ in range((self.n_cells_sqrt - 1) * 2)]
        for i in range(self.n_cells_sqrt):
            for j in range(self.n_cells_sqrt):
                if j == i == 0:
                    continue
                dist: int = i + j
                if [i, j] not in distance_table_raw[dist - 1]:
                    distance_table_raw[dist - 1].append([i, j])
                if [i, -j] not in distance_table_raw[dist - 1]:
                    distance_table_raw[dist - 1].append([i, -j])
                if [-i, -j] not in distance_table_raw[dist - 1]:
                    distance_table_raw[dist - 1].append([-i, -j])
                if [-i, j] not in distance_table_raw[dist - 1]:
                    distance_table_raw[dist - 1].append([-i, j])
        if make_shuffle:
            for dist in distance_table_raw:
                if make_shuffle:
                    random.shuffle(dist)
        return distance_table_raw  # mesh_distances

    def format_distance_table(distance_table_raw: List[List], make_shuffle: bool) -> List[List[int]]:
        distance_table: List[List[int]] = []
        for dist in distance_table_raw:
            if make_shuffle:
                random.shuffle(dist)
            distance_table.extend(dist)
        return distance_table

    def get_dot_vars(self):
        n_list = list(self.g.nodes)
        nodes_counter = 0
        for i, node in enumerate(n_list):
            nl = node.lower()
            if "level" in nl or "title" in nl:
                self.g.remove_node(node)
                continue
            self.nodes.append(node)
            self.nodes_to_idx[node] = nodes_counter
            if len(list(self.g.succ[node])) == 0:
                self.output_nodes.append(node)
            elif len(list(self.g.pred[node])) == 0:
                self.input_nodes.append(node)
            nodes_counter += 1
        for e in list(self.g.edges):
            idx_1 = self.nodes_to_idx[e[1]]
            idx_0 = self.nodes_to_idx[e[0]]
            self.edges.append((e[0], e[1]))
            self.n_edges += 1

            self.neighbors[idx_0].append(idx_1)
            self.neighbors[idx_1].append(idx_0)

        self.n_cells_sqrt = ceil(sqrt(len(self.nodes)))
        self.n_cells = pow(self.n_cells_sqrt, 2)
        m = max(len(self.output_nodes), len(self.input_nodes))
        if m > self.n_cells_sqrt:
            self.n_cells_sqrt = m
            self.n_cells = pow(m, 2)

    # FIXME
    def get_edges_depth_first(self) -> list[list]:
        temp_edges: list = list(self.g.edges)
        r_edges: list = []

        # finding the bottom node (with no successors)
        lower_node: str = ""
        for p in self.g._succ:
            if len(self.g._succ[p]) == 0:
                lower_node = p
                break

        # creating the edges list
        r: str = lower_node
        q: list = [r]
        working: bool = True
        while working:
            working = False
            for e in temp_edges:
                if e[1] == r:
                    r_edges.append([e[1], e[0]])
                    temp_edges.remove(e)
                    q.append(e[0])
                    r = e[0]
                    working = True
                    break
            if q and temp_edges and not working:
                q = q[:-1]
                if q:
                    r = q[-1]
                    working = True
                '''elif edges:
                        q.append(edges[0][0])
                        r = edges[0][0]
                        working = True'''
        return r_edges

    def get_edges_zigzag(self, make_shuffle: bool = True) -> tuple[list[list[str]], list[list[str]], list[list[Any]]]:

        output_list = [[node, 'IN'] for node in self.output_nodes]

        if make_shuffle:
            random.shuffle(output_list)

        stack = output_list.copy()
        edges = []
        visited = set()
        convergence = []

        fan_in = {node: list(self.g.predecessors(node)) for node in self.g.nodes()}
        fan_out = {node: list(self.g.successors(node)) for node in self.g.nodes()}

        if make_shuffle:
            for node in self.g.nodes():
                random.shuffle(fan_in[node])
                random.shuffle(fan_out[node])

        while stack:
            a, direction = stack.pop(0)  # get the top1
            visited.add(a)

            if direction == 'IN':  # direction == 'IN'

                if fan_out[a]:  # Case 3
                    b = fan_out[a][-1]
                    stack.insert(0, [a, 'IN'])
                    stack[:0] = [[a, 'IN']] * len(fan_in[a])
                    stack.insert(0, [b, 'OUT'])
                    fan_out[a].remove(b)
                    fan_in[b].remove(a)
                    if b in visited:
                        convergence.append([a, b])
                    edges.append([a, b, 'OUT'])

                elif fan_in[a]:  # Case 2
                    b = fan_in[a][-1]
                    stack.insert(0, [a, 'IN'])
                    stack[:0] = [[b, 'IN']] * len(fan_in[a])
                    fan_in[a].remove(b)
                    fan_out[b].remove(a)
                    if b in visited:
                        convergence.append([a, b])
                    edges.append([a, b, 'IN'])

            else:  # direction == 'OUT'

                if fan_in[a]:  # Case 3
                    b = fan_in[a][0]
                    stack.insert(0, [a, 'OUT'])
                    stack[:0] = [[a, 'OUT']] * len(fan_out[a])
                    stack.insert(0, [b, 'IN'])
                    fan_in[a].remove(b)
                    fan_out[b].remove(a)
                    if b in visited:
                        convergence.append([a, b])
                    edges.append([a, b, 'IN'])

                elif fan_out[a]:  # Case 2
                    b = fan_out[a][0]
                    stack.insert(0, [a, 'OUT'])
                    stack[:0] = [[b, 'OUT']] * len(fan_out[a])
                    fan_out[a].remove(b)
                    fan_in[b].remove(a)
                    if b in visited:
                        convergence.append([a, b])
                    edges.append([a, b, 'OUT'])

        return self.clear_edges(edges), self.clear_edges(edges, False), convergence

    @staticmethod
    def clear_edges(edges: List[List[str]], remove_placed_edges: bool = True) -> List[List[str]]:
        dic = set()
        dic.add(edges[0][0])
        new_edges = []
        for edge in edges:
            n1, n2 = edge[:2]
            if n2 not in dic or not remove_placed_edges:
                dic.add(n2)
                new_edges.append([n1, n2])
        return new_edges

    def get_cost(self, n_c, node1, node2, cell1, cell2):
        cost1_b = 0
        cost1_a = 0
        cost2_b = 0
        cost2_a = 0
        if node1 is not None:
            for n in self.neighbors[node1]:
                cost1_b += self.get_manhattan_distance(cell1, n_c[n])
                if cell2 == n_c[n]:
                    cost1_a += self.get_manhattan_distance(cell1, cell2)
                else:
                    cost1_a += self.get_manhattan_distance(cell2, n_c[n])
        if node2 is not None:
            for n in self.neighbors[node2]:
                cost2_b += self.get_manhattan_distance(cell2, n_c[n])
                if cell1 == n_c[n]:
                    cost2_a += self.get_manhattan_distance(cell2, cell1)
                else:
                    cost2_a += self.get_manhattan_distance(cell1, n_c[n])
        return cost1_b, cost1_a, cost2_b, cost2_a

    def get_manhattan_distance(self, cell1: int, cell2: int) -> int:
        cell1_x = cell1 % self.n_cells_sqrt
        cell1_y = cell1 // self.n_cells_sqrt
        cell2_x = cell2 % self.n_cells_sqrt
        cell2_y = cell2 // self.n_cells_sqrt
        return abs(cell1_y - cell2_y) + abs(cell1_x - cell2_x)