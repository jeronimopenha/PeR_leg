import math
from random import choice
import random
from src.graph_generator.placement import Placement
from src.graph_generator.router import Router
class GraphGenerator:
    @staticmethod
    def generate_random_graph(num_vertexes:int,adj_list:list[tuple[int,int]]):
        vertexes = [i for i in range(num_vertexes)]
        dim_arch = int(math.ceil(math.sqrt(num_vertexes)))

        PEs = [(i,j) for i in range(dim_arch) for j in range(dim_arch)]

        placement_n2c,placement_c2n = Placement.random_placement(vertexes,PEs)

        vertex = choice(list(placement_n2c.keys()))

        routing = Router.create_tree_by_pe(placement_c2n, placement_n2c[vertex],adj_list)

        dfg_edges = []
        for (a,b) in routing:
            dfg_edges.append((placement_c2n[a],placement_c2n[b]))
        
        return vertexes,dfg_edges,placement_c2n