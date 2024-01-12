import random as rnd
from src.util.per_graph import PeRGraph
from src.util.sa.sa_util import SaUtil


class SaPipelineSwlUtil(SaUtil):
    def __init__(self, proj_graph: PeRGraph):
        super().__init__(proj_graph)

    def get_total_cost(self, c_n, n_c):
        costs = {}
        cost = 0
        for i in range(len(c_n)):
            if c_n[i] is None:
                continue
            total_cost = 0
            for n in self.proj_graph.neighbors[c_n[i]]:
                cost += self.get_manhattan_distance(i, n_c[n])
                total_cost += cost
            costs[c_n[i]] = total_cost
        # print(costs)
        # print(sorted(costs.items(), key=lambda x: x[0]))
        return cost  # costs

    def get_cost(self, n_c, node1, node2, cell1, cell2) -> tuple[int, int, int, int]:
        cost1_b = 0
        cost1_a = 0
        cost2_b = 0
        cost2_a = 0
        if node1 is not None:
            for n in self.proj_graph.neighbors[node1]:
                cost1_b += self.get_manhattan_distance(cell1, n_c[n])
                if cell2 == n_c[n]:
                    cost1_a += self.get_manhattan_distance(cell1, cell2)
                else:
                    cost1_a += self.get_manhattan_distance(cell2, n_c[n])
        if node2 is not None:
            for n in self.proj_graph.neighbors[node2]:
                cost2_b += self.get_manhattan_distance(cell2, n_c[n])
                if cell1 == n_c[n]:
                    cost2_a += self.get_manhattan_distance(cell2, cell1)
                else:
                    cost2_a += self.get_manhattan_distance(cell1, n_c[n])
        return cost1_b, cost1_a, cost2_b, cost2_a

    def get_manhattan_distance(self, cell1: int, cell2: int) -> int:
        cell1_x = cell1 % self.proj_graph.n_cells_sqrt
        cell1_y = cell1 // self.proj_graph.n_cells_sqrt
        cell2_x = cell2 % self.proj_graph.n_cells_sqrt
        cell2_y = cell2 // self.proj_graph.n_cells_sqrt
        return abs(cell1_y - cell2_y) + abs(cell1_x - cell2_x)
