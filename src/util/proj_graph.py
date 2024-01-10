import pygraphviz as pgv
import networkx as nx
from math import ceil, sqrt


class ProjGraph:

    def __init__(self, dot: str):
        self.dot = dot
        self.gv = pgv.AGraph(self.dot, strict=False, directed=True)
        self.g = nx.DiGraph(self.gv)
        self.nodes = []
        self.n_nodes = 0
        self.edges = []
        self.n_edges = 0
        self.nodes_to_idx = {}
        self.neighbors = {}
        self.n_cells = 0
        self.n_cells_sqrt = 0
        self.get_dot_vars()

    def get_dot_vars(self):
        self.nodes = list(self.g.nodes)
        self.n_nodes = len(self.nodes)
        self.edges = list(self.g.edges)
        self.n_edges = len(self.edges)
        self.nodes_to_idx = {}
        self.neighbors = {}
        for i in range(self.n_nodes):
            self.nodes_to_idx[self.nodes[i]] = i

        for e in self.edges:
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

    def get_edges_depth_first(self) -> list(list()):
        # FIXME Acertar o algoritmo para grafos não conectados
        # FIXME docstring
        """_summary_
            Returns a list of edges according
            with the depth first algorithm

        Args:
            self (_type_): _description_

        Returns:
            _type_: _description_
        """
        temp_edges = list(self.g.edges)
        r_edges = []

        # finding the bottom node (with no successors)
        lower_node = None
        for p in self.g._succ:
            if len(self.g._succ[p]) == 0:
                lower_node = p
                break

        # creating the edges list
        r = lower_node
        q = []
        q.append(r)
        working = True
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

    def get_edges_zigzag(self) -> list(list()):
        # FIXME docstring
        """_summary_
            Returns a list of edges according
            with the zig zag algorithm
        Returns:
            _type_: _description_
        """

        output_list = []
        # get the node inputs
        for n in self.g.nodes():
            if self.g.out_degree(n) == 0:
                output_list.append([n, 'IN'])

        stack = output_list.copy()

        edges = []

        l_fanin, l_fanout = {}, {}
        for no in self.g:
            l_fanin[no] = list(self.g.predecessors(no))
            l_fanout[no] = list(self.g.successors(no))

        while stack:
            a, direction = stack.pop(0)  # get the top1

            fanin = len(l_fanin[a])  # get size fanin
            fanout = len(l_fanout[a])  # get size fanout

            if direction == 'IN':  # direction == 'IN'

                if fanout >= 1:  # Case 3

                    b = l_fanout[a][-1]  # get the element more the right side

                    for i in range(fanin):
                        stack.insert(0, [a, 'IN'])
                    stack.insert(0, [b, 'OUT'])  # insert into stack

                    l_fanout[a].remove(b)
                    l_fanin[b].remove(a)

                    edges.append([a, b, 'OUT'])

                elif fanin >= 1:  # Case 2

                    b = l_fanin[a][-1]  # get the elem more in the right

                    stack.insert(0, [a, 'IN'])
                    for i in range(fanin):
                        stack.insert(0, [b, 'IN'])

                    l_fanin[a].remove(b)
                    l_fanout[b].remove(a)

                    edges.append([a, b, 'IN'])

            else:  # direction == 'OUT'

                if fanin >= 1:  # Case 3

                    b = l_fanin[a][0]  # get the element more left side

                    for i in range(fanout):
                        stack.insert(0, [a, 'OUT'])
                    stack.insert(0, [b, 'IN'])

                    l_fanin[a].remove(b)
                    l_fanout[b].remove(a)

                    edges.append([a, b, 'IN'])

                elif fanout >= 1:  # Case 2

                    b = l_fanout[a][0]  # get the element more left side

                    stack.insert(0, [a, 'OUT'])
                    for i in range(fanout):
                        stack.insert(0, [b, 'OUT'])

                    l_fanout[a].remove(b)
                    l_fanin[b].remove(a)

                    edges.append([a, b, 'OUT'])

        return edges
