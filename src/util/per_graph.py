from typing import Tuple, List

import pygraphviz as pgv
import networkx as nx
import random
from math import ceil, sqrt


class PeRGraph:

    def __init__(self, dot_path: str, dot_name: str):
        self.dot_path: str = dot_path
        self.dot_name: str = dot_name
        self.gv: pgv.AGraph = pgv.AGraph(self.dot_path, strict=False, directed=True)
        self.g: nx.DiGraph = nx.DiGraph(self.gv)
        self.nodes: list = []
        self.n_nodes: int = 0
        self.edges_str: list[list] = []
        self.n_edges: int = 0
        self.nodes_to_idx: dict = {}
        self.neighbors: dict = {}
        self.n_cells: int = 0
        self.n_cells_sqrt: int = 0
        self.get_dot_vars()

    def get_dot_vars(self) -> None:
        self.nodes = list(self.g.nodes)
        self.n_nodes = len(self.nodes)
        self.edges_str = list(self.g.edges)
        self.n_edges = len(self.edges_str)

        for i in range(self.n_nodes):
            self.nodes_to_idx[self.nodes[i]] = i

        for e in self.edges_str:
            if self.nodes_to_idx[e[0]] not in self.neighbors.keys():
                self.neighbors[self.nodes_to_idx[e[0]]] = []
            if self.nodes_to_idx[e[1]] not in self.neighbors.keys():
                self.neighbors[self.nodes_to_idx[e[1]]] = []
            self.neighbors[self.nodes_to_idx[e[0]]].append(
                self.nodes_to_idx[e[1]])
            self.neighbors[self.nodes_to_idx[e[1]]].append(
                self.nodes_to_idx[e[0]])

        self.n_cells_sqrt = ceil(sqrt(self.n_nodes))
        self.n_cells = pow(self.n_cells_sqrt, 2)

    # FIXME
    def get_edges_depth_first(self) -> list[list]:
        # FIXME Acertar o algoritmo para grafos não conectados
        # FIXME docstring
        """_summary_
            Returns a list of edges according
            to the depth first algorithm

        Args:
            self (_type_): _description_

        Returns:
            _type_: _description_
        """
        temp_edges: list = list(self.g.edges_str)
        r_edges: list = []

        # finding the bottom node (with no successors)
        lower_node: str = ""
        for p in self.g._succ:
            if len(self.g._succ[p]) == 0:
                lower_node = p
                break

        # creating the edges list
        r: str = lower_node
        q: list = []
        q.append(r)
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

    def get_edges_zigzag(self, shuffle: bool = True) -> tuple[list[list], list, list]:
        # FIXME docstring
        """_summary_
            Returns a list of edges according
            to the zigzag algorithm
        Returns:
            _type_: _description_
        """

        output_list: list = []
        # get the node inputs
        for node in self.g.nodes():
            if self.g.out_degree(node) == 0:
                output_list.append([node, 'IN'])

        if shuffle:
            random.shuffle(output_list)
        stack: list = output_list.copy()
        edges: list = []
        visited: list = []
        cycle: list = []

        fanin: dict = {}
        fanout: dict = {}
        for node in self.g.nodes():
            fanin[node] = list(self.g.predecessors(node))
            fanout[node] = list(self.g.successors(node))
            if shuffle:
                random.shuffle(fanin[node])
                random.shuffle(fanout[node])

        while stack:
            a, direction = stack.pop(0)  # get the top1

            n_fanin: int = len(fanin[a])  # get size n_fanin
            n_fanout: int = len(fanout[a])  # get size n_fanout

            if direction == 'IN':  # direction == 'IN'

                if n_fanout >= 1:  # Case 3

                    b: str = fanout[a][-1]  # get the element more the right side

                    for i in range(n_fanin):
                        stack.insert(0, [a, 'IN'])
                    stack.insert(0, [b, 'OUT'])  # insert into stack

                    fanout[a].remove(b)
                    fanin[b].remove(a)

                    if b in visited:
                        cycle.append([a, b])

                    edges.append([a, b, 'OUT'])

                elif n_fanin >= 1:  # Case 2

                    b: str = fanin[a][-1]  # get the elem more in the right

                    stack.insert(0, [a, 'IN'])
                    for i in range(n_fanin):
                        stack.insert(0, [b, 'IN'])

                    fanin[a].remove(b)
                    fanout[b].remove(a)

                    if b in visited:
                        cycle.append([a, b])

                    edges.append([a, b, 'IN'])

            else:  # direction == 'OUT'

                if n_fanin >= 1:  # Case 3

                    b = fanin[a][0]  # get the element more left side

                    for i in range(n_fanout):
                        stack.insert(0, [a, 'OUT'])
                    stack.insert(0, [b, 'IN'])

                    fanin[a].remove(b)
                    fanout[b].remove(a)

                    if b in visited:
                        cycle.append([a, b])

                    edges.append([a, b, 'IN'])

                elif n_fanout >= 1:  # Case 2

                    b = fanout[a][0]  # get the element more left side

                    stack.insert(0, [a, 'OUT'])
                    for i in range(n_fanout):
                        stack.insert(0, [b, 'OUT'])

                    fanout[a].remove(b)
                    fanin[b].remove(a)

                    if b in visited:
                        cycle.append([a, b])

                    edges.append([a, b, 'OUT'])
            visited.append(a)

        return self.remove_nodes_already_placed(edges), edges, cycle

    @staticmethod
    def remove_nodes_already_placed(edges: list[list]) -> list[list]:
        dic: dict = {edges[0][0]: True,
                     edges[0][1]: True}
        new_edges: list[list] = [edges[0][:2]]
        for edge in (edges[1:]):
            n1, n2 = edge[:2]
            if dic.get(n2) is None:
                dic[n2] = True
                new_edges.append([n1, n2])
        return new_edges
