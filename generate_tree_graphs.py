import math
import random
from src.graph_exporter.graph_exporter import GraphExporter
from src.graph_generator.graph_generator import GraphGenerator
import pygraphviz as pgv
import networkx as nx
from src.util.util import Util

def generate_connected_balanced_trees_by_heights(heights:list):
    graph_generator =  GraphGenerator
    for height in heights:
        print(f'Height Complete Binary Tree = {height}')
        vertexes, edges = graph_generator.generate_binary_tree(height)
        path = Util.get_project_root() + f'/dot_db/graphs0_tree/'
        filename = f'BBT-h{height}'

        GraphExporter.export_dot_graph(vertexes,edges,path,filename)

def generate_connected_unbalanced_trees_by_num_vertexes(num_vertexes:list):
    graph_generator =  GraphGenerator
    for num_vertex in num_vertexes:
        qtd_pe = int(math.pow(math.ceil(math.sqrt(num_vertex)),2))
        dim_arch = int(math.sqrt(qtd_pe))
        print(f'Num Vertexes = {num_vertex} - qtd_pe {qtd_pe}')
        connected = False
        while not connected:
            vertexes, edges_dfg, placement_c2n = graph_generator.generate_random_tree_graph(num_vertex,[(0,1),(0,-1),(1,0),(-1,0)])
            G = nx.Graph(directed=True)
            G.add_nodes_from(vertexes)
            G.add_edges_from(edges_dfg)
            connected = nx.is_connected(G)
        path = Util.get_project_root() + f'/dot_db/graphs0_tree/'
        filename = f'tree {num_vertex} - {dim_arch}x{dim_arch}'
        GraphExporter.export_dot_graph(vertexes,edges_dfg,path,filename)

generate_connected_unbalanced_trees_by_num_vertexes([i for i in range(10,400,10)])
generate_connected_balanced_trees_by_heights([i for i in range(2,8)])